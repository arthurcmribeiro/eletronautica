from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from vault_tools import ROOT, load_notes, manifest_payload, write_json


def main() -> None:
    notes = load_notes(ROOT)
    payload = manifest_payload(notes)
    payload["generated_at"] = datetime.now(timezone.utc).isoformat()
    payload["note_count"] = len(notes)

    output_path = ROOT / "manifest" / "content-manifest.json"
    write_json(output_path, payload)
    print(f"Manifesto gerado em: {output_path}")


if __name__ == "__main__":
    main()
