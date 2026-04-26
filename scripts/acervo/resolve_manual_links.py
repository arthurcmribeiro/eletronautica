from __future__ import annotations

import argparse
import json
import ssl
import sys
import urllib.error
import urllib.request
from collections import deque
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qsl, urljoin, urlparse, urlunparse, urlencode


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT, write_json  # noqa: E402


DEFAULT_QUEUE = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "manual-resolution-queue.json"
DEFAULT_RESULTS = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "manual-resolution-results.json"
USER_AGENT = "Mozilla/5.0 (Codex Manual Link Resolver)"
MANUAL_EXTENSIONS = {".pdf"}
SOURCE_ORDER = ("official", "secondary", "mirror", "unknown")
SOURCE_BONUS = {
    "official": 8,
    "secondary": 4,
    "mirror": 1,
    "unknown": 0,
}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[dict[str, str]] = []
        self._current_href = ""
        self._current_text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for key, value in attrs:
            if key == "href" and value:
                self._current_href = value
                self._current_text_parts = []
                break

    def handle_data(self, data: str) -> None:
        if self._current_href:
            self._current_text_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != "a" or not self._current_href:
            return
        label = " ".join(part.strip() for part in self._current_text_parts if part.strip()).strip()
        self.links.append({"href": self._current_href, "label": label})
        self._current_href = ""
        self._current_text_parts = []


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Visita paginas oficiais e registra links candidatos a manuais sem baixar arquivos."
    )
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE, help="Fila JSON de resolucao.")
    parser.add_argument("--results", type=Path, default=DEFAULT_RESULTS, help="Arquivo JSON de saida.")
    parser.add_argument("--only", nargs="*", default=[], help="Canonicos especificos a processar.")
    parser.add_argument("--limit", type=int, default=0, help="Limite de itens a processar.")
    parser.add_argument("--timeout", type=int, default=30, help="Timeout por requisicao.")
    parser.add_argument("--dry-run", action="store_true", help="Nao acessa a rede; apenas mostra o plano.")
    return parser.parse_args()


def load_queue(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def fetch_url(url: str, timeout: int) -> tuple[str, str]:
    context = ssl.create_default_context()
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
        content_type = response.headers.get("Content-Type", "")
        payload = response.read()
    return content_type, payload.decode("utf-8", errors="ignore")


def normalize_url(url: str) -> str:
    parsed = urlparse(url.strip())
    query_pairs = parse_qsl(parsed.query, keep_blank_values=True)

    if "manualslib.com" in parsed.netloc.lower():
        query_pairs = [
            (key, value)
            for key, value in query_pairs
            if key.lower() not in {"page", "print"}
        ]

    normalized_query = urlencode(query_pairs)
    normalized = parsed._replace(fragment="", query=normalized_query)
    return urlunparse(normalized)


def is_direct_document_url(url: str) -> bool:
    lower_url = url.lower()
    return any(lower_url.endswith(ext) for ext in MANUAL_EXTENSIONS)


def source_tier_for_url(item: dict[str, object], url: str) -> str:
    domain = urlparse(url).netloc.lower()
    source_layers = item.get("source_layers", {})

    for tier in SOURCE_ORDER:
        tier_payload = source_layers.get(tier, {})
        tier_domains = [str(domain_name).lower() for domain_name in tier_payload.get("domains", [])]
        if any(domain_name and domain_name in domain for domain_name in tier_domains):
            return tier

    return "unknown"


def allowed_for_item(item: dict[str, object], url: str) -> bool:
    domain = urlparse(url).netloc.lower()
    allowed_domains = [str(domain_name).lower() for domain_name in item.get("allowed_domains", [])]
    return any(domain_name and domain_name in domain for domain_name in allowed_domains)


def score_candidate(item: dict[str, object], url: str, label: str, source_tier: str) -> int:
    haystack = f"{label} {url}".lower()
    score = SOURCE_BONUS.get(source_tier, 0)

    for keyword in item["resolver_profile"]["manual_keywords"]:
        if keyword.lower() in haystack:
            score += 2

    for keyword in item["resolver_profile"]["reject_keywords"]:
        if keyword.lower() in haystack:
            score -= 3

    for alias in item.get("aliases", []):
        if str(alias).lower() in haystack:
            score += 3

    for alias in item.get("child_aliases", []):
        if str(alias).lower() in haystack:
            score += 2

    for alias in item.get("product_aliases", []):
        if str(alias).lower() in haystack:
            score += 2

    if is_direct_document_url(url):
        score += 6

    return score


def classify_candidate(url: str, label: str, document_type: str = "") -> str:
    if document_type:
        return document_type

    haystack = f"{label} {url}".lower()
    if is_direct_document_url(url):
        return "pdf_direct"
    if "manual" in haystack:
        return "manual_page"
    if "catalog" in haystack or "brochure" in haystack or "guide" in haystack:
        return "catalog_or_guide"
    if "support" in haystack or "download" in haystack or "document" in haystack:
        return "support_or_library"
    return "candidate_page"


def candidate_sort_key(candidate: dict[str, object]) -> tuple[int, int, str, str]:
    tier = str(candidate.get("source_tier", "unknown"))
    try:
        tier_rank = SOURCE_ORDER.index(tier)
    except ValueError:
        tier_rank = len(SOURCE_ORDER)

    return (
        tier_rank,
        -int(candidate["score"]),
        str(candidate["kind"]),
        str(candidate["url"]),
    )


def add_candidate(
    item: dict[str, object],
    candidates: dict[str, dict[str, object]],
    url: str,
    label: str,
    found_from: str,
    document_type: str = "",
    family: str = "",
    forced_source_tier: str = "",
) -> None:
    normalized_url = normalize_url(url)
    source_tier = forced_source_tier or source_tier_for_url(item, normalized_url)
    score = score_candidate(item, normalized_url, label, source_tier)

    if score <= 0:
        return

    entry = candidates.setdefault(
        normalized_url,
        {
            "url": normalized_url,
            "label": label,
            "score": score,
            "kind": classify_candidate(normalized_url, label, document_type=document_type),
            "source_tier": source_tier,
            "family": family,
            "found_from": [],
        },
    )

    entry["score"] = max(int(entry["score"]), score)
    if label and not entry.get("label"):
        entry["label"] = label
    if family and not entry.get("family"):
        entry["family"] = family
    if document_type:
        entry["kind"] = classify_candidate(normalized_url, label, document_type=document_type)

    if found_from not in entry["found_from"]:
        entry["found_from"].append(found_from)


def crawl_item(item: dict[str, object], timeout: int) -> dict[str, object]:
    max_depth = int(item["resolver_profile"]["max_depth"])
    max_seed_pages = int(item["resolver_profile"]["max_seed_pages"])
    max_links = int(item["resolver_profile"]["max_links_per_item"])

    queue: deque[tuple[str, int]] = deque(
        (normalize_url(url), 0)
        for url in item.get("seed_urls", [])[:max_seed_pages]
    )
    visited: set[str] = set()
    candidates: dict[str, dict[str, object]] = {}
    errors: list[str] = []

    for curated in item.get("curated_candidates", []):
        add_candidate(
            item,
            candidates,
            str(curated.get("url", "")),
            str(curated.get("label", "")),
            "curated",
            document_type=str(curated.get("document_type", "")),
            family=str(curated.get("family", "")),
            forced_source_tier=str(curated.get("source_tier", "")),
        )

    while queue and len(visited) < max_links:
        url, depth = queue.popleft()
        if url in visited or not url:
            continue
        visited.add(url)

        if is_direct_document_url(url):
            add_candidate(item, candidates, url, "", "seed")
            continue

        try:
            content_type, html = fetch_url(url, timeout=timeout)
        except (urllib.error.URLError, TimeoutError, ssl.SSLError) as exc:
            errors.append(f"{url}: {exc}")
            continue

        if "html" not in content_type.lower():
            add_candidate(item, candidates, url, "", "fetch")
            continue

        parser = LinkParser()
        parser.feed(html)

        for raw_link in parser.links:
            href = raw_link["href"].strip()
            if not href:
                continue

            absolute_url = normalize_url(urljoin(url, href))
            if not allowed_for_item(item, absolute_url):
                continue

            label = raw_link["label"].strip()
            source_tier = source_tier_for_url(item, absolute_url)
            score = score_candidate(item, absolute_url, label, source_tier)

            if score > 0:
                add_candidate(item, candidates, absolute_url, label, url)

            if depth + 1 <= max_depth and absolute_url not in visited:
                queue.append((absolute_url, depth + 1))

    sorted_candidates = sorted(candidates.values(), key=candidate_sort_key)
    source_layer_counts = {
        tier: sum(1 for candidate in sorted_candidates if candidate.get("source_tier") == tier)
        for tier in SOURCE_ORDER
    }

    return {
        "canonical": item["canonical"],
        "visited_pages": len(visited),
        "seed_urls": item.get("seed_urls", []),
        "curated_candidate_count": len(item.get("curated_candidates", [])),
        "candidate_count": len(sorted_candidates),
        "source_layer_counts": source_layer_counts,
        "candidates": sorted_candidates[:max_links],
        "errors": errors[:25],
    }


def main() -> int:
    args = parse_args()
    payload = load_queue(args.queue)
    items = list(payload.get("items", []))

    if args.only:
        only_set = set(args.only)
        items = [item for item in items if item.get("canonical") in only_set]

    if args.limit > 0:
        items = items[: args.limit]

    if args.dry_run:
        results = [
            {
                "canonical": item["canonical"],
                "seed_urls": item.get("seed_urls", []),
                "allowed_domains": item.get("allowed_domains", []),
                "source_layers": item.get("source_layers", {}),
                "curated_candidates": item.get("curated_candidates", []),
                "status": "planned",
            }
            for item in items
        ]
    else:
        results = [crawl_item(item, timeout=args.timeout) for item in items]

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "queue_path": args.queue.relative_to(ROOT).as_posix(),
        "result_count": len(results),
        "dry_run": bool(args.dry_run),
        "results": results,
    }
    write_json(args.results, output)

    print(f"Itens processados: {len(results)}")
    print(f"Dry-run: {args.dry_run}")
    print(f"Resultados: {args.results}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
