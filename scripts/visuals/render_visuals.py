from __future__ import annotations

from pathlib import Path

from renderer import GENERATED_DIR, SPEC_DIR, load_specs, render_spec, write_svg


def main() -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    specs = load_specs(SPEC_DIR)
    for spec in specs:
        slug = spec["slug"]
        rendered = render_spec(spec)
        svg_path = GENERATED_DIR / f"{slug}.svg"
        png_path = GENERATED_DIR / f"{slug}.png"
        md_path = GENERATED_DIR / f"{slug}.md"

        write_svg(svg_path, rendered["svg"])
        rendered["png"].save_png(png_path)
        md_path.write_text(rendered["md"], encoding="utf-8")

        print(f"Gerado: {svg_path}")
        print(f"Gerado: {png_path}")
        print(f"Gerado: {md_path}")


if __name__ == "__main__":
    main()
