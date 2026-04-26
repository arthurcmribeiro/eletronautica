from __future__ import annotations

import py_compile
from pathlib import Path


SCRIPTS_ROOT = Path(__file__).resolve().parent


def python_files(root: Path = SCRIPTS_ROOT) -> list[Path]:
    return sorted(path for path in root.rglob("*.py") if path.is_file())


def compile_file(path: Path) -> tuple[bool, str]:
    try:
        py_compile.compile(str(path), doraise=True)
    except py_compile.PyCompileError as exc:
        return False, str(exc)
    return True, ""


def main() -> int:
    files = python_files()
    failures: list[tuple[Path, str]] = []

    for path in files:
        ok, error = compile_file(path)
        relative = path.relative_to(SCRIPTS_ROOT.parent).as_posix()
        if ok:
            print(f"OK: {relative}")
            continue
        failures.append((path, error))
        print(f"ERROR: {relative}")
        print(error)

    print("")
    print(f"Scripts analisados: {len(files)}")
    print(f"Falhas de compilação: {len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
