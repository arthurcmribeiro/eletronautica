from __future__ import annotations

import argparse
import hashlib
import json
import ssl
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT, write_json  # noqa: E402


DEFAULT_QUEUE = ROOT / "90_Revisao_Manual" / "_Acervo_Local" / "acervo-download-queue.json"
DEFAULT_REPORT = ROOT / "90_Revisao_Manual" / "_Acervo_Local" / "acervo-download-report.json"
PDF_HEADER = b"%PDF"
USER_AGENT = "Mozilla/5.0 (Codex Acervo Downloader)"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Baixa arquivos do acervo a partir de uma fila JSON."
    )
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE, help="Arquivo JSON da fila.")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT, help="Arquivo JSON de saida.")
    parser.add_argument("--only", nargs="*", default=[], help="IDs especificos a processar.")
    parser.add_argument("--limit", type=int, default=0, help="Limite de itens processados.")
    parser.add_argument("--timeout", type=int, default=60, help="Timeout por requisicao em segundos.")
    parser.add_argument("--retries", type=int, default=2, help="Tentativas por item.")
    parser.add_argument("--force", action="store_true", help="Baixa novamente mesmo se o arquivo ja existir.")
    parser.add_argument("--dry-run", action="store_true", help="So valida a fila sem baixar.")
    return parser.parse_args()


def load_queue(path: Path) -> list[dict[str, str]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("items", [])


def sha256sum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ensure_within_root(path: Path) -> Path:
    resolved = path.resolve()
    root_resolved = ROOT.resolve()
    if root_resolved not in resolved.parents and resolved != root_resolved:
        raise ValueError(f"Destino fora do workspace: {resolved}")
    return resolved


def is_pdf(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 4:
        return False
    with path.open("rb") as handle:
        return handle.read(4) == PDF_HEADER


def download_to_path(url: str, target: Path, timeout: int, retries: int) -> None:
    context = ssl.create_default_context()
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    tmp_path = target.with_suffix(target.suffix + ".download")

    last_error: Exception | None = None
    for _ in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
                target.parent.mkdir(parents=True, exist_ok=True)
                with tmp_path.open("wb") as handle:
                    while True:
                        chunk = response.read(1024 * 1024)
                        if not chunk:
                            break
                        handle.write(chunk)
            tmp_path.replace(target)
            return
        except (urllib.error.URLError, TimeoutError, ssl.SSLError) as exc:
            last_error = exc
            if tmp_path.exists():
                tmp_path.unlink(missing_ok=True)

    if last_error is None:
        raise RuntimeError(f"Falha sem erro explicito para {url}")
    raise RuntimeError(str(last_error)) from last_error


def process_item(item: dict[str, str], args: argparse.Namespace) -> dict[str, str | int]:
    target = ensure_within_root(ROOT / item["target_relpath"])
    expected_type = item.get("expected_type", "").lower()
    result: dict[str, str | int] = {
        "id": item["id"],
        "url": item["url"],
        "target_relpath": item["target_relpath"],
        "expected_type": item.get("expected_type", ""),
        "notes": item.get("notes", ""),
        "status": "pending",
    }

    if args.dry_run:
        result["status"] = "dry_run"
        return result

    if target.exists() and not args.force:
        if expected_type == "pdf" and not is_pdf(target):
            result["status"] = "invalid_existing"
            result["error"] = "arquivo existente nao e PDF valido"
            return result
        result["status"] = "skipped_existing"
        result["size_bytes"] = target.stat().st_size
        result["sha256"] = sha256sum(target)
        return result

    try:
        download_to_path(item["url"], target, timeout=args.timeout, retries=args.retries)
        if expected_type == "pdf" and not is_pdf(target):
            target.unlink(missing_ok=True)
            result["status"] = "invalid_download"
            result["error"] = "conteudo baixado nao e PDF valido"
            return result
        result["status"] = "downloaded"
        result["size_bytes"] = target.stat().st_size
        result["sha256"] = sha256sum(target)
        return result
    except Exception as exc:  # noqa: BLE001
        result["status"] = "error"
        result["error"] = str(exc)
        return result


def main() -> int:
    args = parse_args()
    queue_path = ensure_within_root(args.queue)
    report_path = ensure_within_root(args.report)
    items = load_queue(queue_path)

    if args.only:
        only_set = set(args.only)
        items = [item for item in items if item.get("id") in only_set]

    if args.limit > 0:
        items = items[: args.limit]

    results = [process_item(item, args) for item in items]
    status_counts: dict[str, int] = {}
    for result in results:
        status = str(result["status"])
        status_counts[status] = status_counts.get(status, 0) + 1

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "queue_path": queue_path.relative_to(ROOT).as_posix(),
        "report_path": report_path.relative_to(ROOT).as_posix(),
        "item_count": len(results),
        "status_counts": status_counts,
        "results": results,
    }
    write_json(report_path, payload)

    success_count = sum(
        1 for result in results if result["status"] in {"downloaded", "skipped_existing"}
    )
    error_count = sum(
        1
        for result in results
        if result["status"] in {"error", "invalid_download", "invalid_existing"}
    )

    print(f"Fila processada: {len(results)} itens")
    print(f"Sucesso ou ja existente: {success_count}")
    print(f"Erros: {error_count}")
    print(f"Relatorio: {report_path}")
    for status, count in sorted(status_counts.items()):
        print(f"- {status}: {count}")

    return 1 if error_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
