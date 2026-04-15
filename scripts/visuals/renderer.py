from __future__ import annotations

import json
import math
import struct
import unicodedata
import zlib
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
SPEC_DIR = ROOT / "_visuals" / "specs"
GENERATED_DIR = ROOT / "_visuals" / "generated"

PALETTE = {
    "background": "#F6F2EA",
    "panel": "#FFFDF8",
    "text": "#1F2933",
    "muted": "#5B6B79",
    "grid": "#D9E2EC",
    "blue": "#1D6FD8",
    "orange": "#DB7C26",
    "green": "#2A9D57",
    "yellow": "#E0A100",
    "red": "#D9534F",
    "purple": "#7C5CC4",
    "teal": "#168A8A",
    "ink": "#0F172A",
}

BITMAP_FONT = {
    "A": ("01110", "10001", "10001", "11111", "10001", "10001", "10001"),
    "B": ("11110", "10001", "10001", "11110", "10001", "10001", "11110"),
    "C": ("01110", "10001", "10000", "10000", "10000", "10001", "01110"),
    "D": ("11100", "10010", "10001", "10001", "10001", "10010", "11100"),
    "E": ("11111", "10000", "10000", "11110", "10000", "10000", "11111"),
    "F": ("11111", "10000", "10000", "11110", "10000", "10000", "10000"),
    "G": ("01110", "10001", "10000", "10111", "10001", "10001", "01110"),
    "H": ("10001", "10001", "10001", "11111", "10001", "10001", "10001"),
    "I": ("11111", "00100", "00100", "00100", "00100", "00100", "11111"),
    "J": ("00111", "00010", "00010", "00010", "10010", "10010", "01100"),
    "K": ("10001", "10010", "10100", "11000", "10100", "10010", "10001"),
    "L": ("10000", "10000", "10000", "10000", "10000", "10000", "11111"),
    "M": ("10001", "11011", "10101", "10101", "10001", "10001", "10001"),
    "N": ("10001", "11001", "10101", "10011", "10001", "10001", "10001"),
    "O": ("01110", "10001", "10001", "10001", "10001", "10001", "01110"),
    "P": ("11110", "10001", "10001", "11110", "10000", "10000", "10000"),
    "Q": ("01110", "10001", "10001", "10001", "10101", "10010", "01101"),
    "R": ("11110", "10001", "10001", "11110", "10100", "10010", "10001"),
    "S": ("01111", "10000", "10000", "01110", "00001", "00001", "11110"),
    "T": ("11111", "00100", "00100", "00100", "00100", "00100", "00100"),
    "U": ("10001", "10001", "10001", "10001", "10001", "10001", "01110"),
    "V": ("10001", "10001", "10001", "10001", "10001", "01010", "00100"),
    "W": ("10001", "10001", "10001", "10101", "10101", "10101", "01010"),
    "X": ("10001", "10001", "01010", "00100", "01010", "10001", "10001"),
    "Y": ("10001", "10001", "01010", "00100", "00100", "00100", "00100"),
    "Z": ("11111", "00001", "00010", "00100", "01000", "10000", "11111"),
    "0": ("01110", "10001", "10011", "10101", "11001", "10001", "01110"),
    "1": ("00100", "01100", "00100", "00100", "00100", "00100", "01110"),
    "2": ("01110", "10001", "00001", "00010", "00100", "01000", "11111"),
    "3": ("11110", "00001", "00001", "01110", "00001", "00001", "11110"),
    "4": ("00010", "00110", "01010", "10010", "11111", "00010", "00010"),
    "5": ("11111", "10000", "10000", "11110", "00001", "00001", "11110"),
    "6": ("01110", "10000", "10000", "11110", "10001", "10001", "01110"),
    "7": ("11111", "00001", "00010", "00100", "01000", "01000", "01000"),
    "8": ("01110", "10001", "10001", "01110", "10001", "10001", "01110"),
    "9": ("01110", "10001", "10001", "01111", "00001", "00001", "01110"),
    "-": ("00000", "00000", "00000", "11111", "00000", "00000", "00000"),
    ":": ("00000", "00100", "00100", "00000", "00100", "00100", "00000"),
    "/": ("00001", "00010", "00100", "01000", "10000", "00000", "00000"),
    ".": ("00000", "00000", "00000", "00000", "00000", "00110", "00110"),
    ",": ("00000", "00000", "00000", "00000", "00110", "00100", "01000"),
    "%": ("11001", "11010", "00100", "01000", "10110", "00110", "00000"),
    "+": ("00000", "00100", "00100", "11111", "00100", "00100", "00000"),
    "=": ("00000", "11111", "00000", "11111", "00000", "00000", "00000"),
    "(": ("00010", "00100", "01000", "01000", "01000", "00100", "00010"),
    ")": ("01000", "00100", "00010", "00010", "00010", "00100", "01000"),
    ">": ("10000", "01000", "00100", "00010", "00100", "01000", "10000"),
    " ": ("00000", "00000", "00000", "00000", "00000", "00000", "00000"),
}


def load_specs(spec_dir: Path = SPEC_DIR) -> list[dict]:
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(spec_dir.glob("*.json"))
    ]


def normalize_ascii(text: str) -> str:
    cleaned = (
        unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    )
    return cleaned.upper()


def hex_to_rgb(color: str) -> tuple[int, int, int]:
    color = color.lstrip("#")
    return tuple(int(color[index : index + 2], 16) for index in (0, 2, 4))


def escape_svg(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def wrap_text(text: str, max_chars: int) -> list[str]:
    words = text.split()
    if not words:
        return [""]
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if len(candidate) <= max_chars:
            current = candidate
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


class SvgCanvas:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.parts = [
            (
                f'<svg xmlns="http://www.w3.org/2000/svg" '
                f'viewBox="0 0 {width} {height}" width="{width}" height="{height}">'
            )
        ]

    def rect(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        fill: str,
        stroke: str | None = None,
        stroke_width: float = 1,
        radius: float = 18,
    ) -> None:
        attrs = [
            f'x="{x}"',
            f'y="{y}"',
            f'width="{width}"',
            f'height="{height}"',
            f'fill="{fill}"',
            f'rx="{radius}"',
            f'ry="{radius}"',
        ]
        if stroke:
            attrs.append(f'stroke="{stroke}"')
            attrs.append(f'stroke-width="{stroke_width}"')
        self.parts.append(f"<rect {' '.join(attrs)}/>")

    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        color: str,
        width: float = 2,
        dash: str | None = None,
    ) -> None:
        attrs = [
            f'x1="{x1}"',
            f'y1="{y1}"',
            f'x2="{x2}"',
            f'y2="{y2}"',
            f'stroke="{color}"',
            f'stroke-width="{width}"',
            'stroke-linecap="round"',
        ]
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        self.parts.append(f"<line {' '.join(attrs)}/>")

    def polyline(
        self, points: Iterable[tuple[float, float]], color: str, width: float = 4
    ) -> None:
        serialized = " ".join(f"{x},{y}" for x, y in points)
        self.parts.append(
            (
                f'<polyline points="{serialized}" fill="none" '
                f'stroke="{color}" stroke-width="{width}" '
                'stroke-linejoin="round" stroke-linecap="round"/>'
            )
        )

    def text(
        self,
        x: float,
        y: float,
        text: str,
        color: str,
        size: int = 20,
        anchor: str = "start",
        weight: str = "400",
    ) -> None:
        self.parts.append(
            (
                f'<text x="{x}" y="{y}" fill="{color}" '
                f'font-family="Segoe UI, Arial, sans-serif" font-size="{size}" '
                f'font-weight="{weight}" text-anchor="{anchor}">'
                f"{escape_svg(text)}</text>"
            )
        )

    def text_block(
        self,
        x: float,
        y: float,
        text: str,
        color: str,
        size: int,
        max_chars: int,
        line_gap: int = 8,
        anchor: str = "start",
        weight: str = "400",
    ) -> None:
        line_height = size + line_gap
        for index, line in enumerate(wrap_text(text, max_chars)):
            self.text(
                x,
                y + index * line_height,
                line,
                color,
                size=size,
                anchor=anchor,
                weight=weight,
            )

    def finalize(self) -> str:
        return "\n".join([*self.parts, "</svg>"]) + "\n"


class RasterCanvas:
    def __init__(self, width: int, height: int, background: str) -> None:
        self.width = width
        self.height = height
        self.buffer = bytearray(width * height * 3)
        self.fill(background)

    def fill(self, color: str) -> None:
        r, g, b = hex_to_rgb(color)
        row = bytes([r, g, b]) * self.width
        for y in range(self.height):
            start = y * self.width * 3
            self.buffer[start : start + len(row)] = row

    def set_pixel(self, x: int, y: int, color: str) -> None:
        if not (0 <= x < self.width and 0 <= y < self.height):
            return
        r, g, b = hex_to_rgb(color)
        index = (y * self.width + x) * 3
        self.buffer[index : index + 3] = bytes((r, g, b))

    def rect(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        fill: str,
        stroke: str | None = None,
        stroke_width: float = 1,
        radius: float = 0,
    ) -> None:
        del radius
        x0 = max(0, int(round(x)))
        y0 = max(0, int(round(y)))
        x1 = min(self.width, int(round(x + width)))
        y1 = min(self.height, int(round(y + height)))
        for py in range(y0, y1):
            for px in range(x0, x1):
                self.set_pixel(px, py, fill)
        if stroke:
            for offset in range(max(1, int(round(stroke_width)))):
                self.line(x0, y0 + offset, x1 - 1, y0 + offset, stroke)
                self.line(x0, y1 - 1 - offset, x1 - 1, y1 - 1 - offset, stroke)
                self.line(x0 + offset, y0, x0 + offset, y1 - 1, stroke)
                self.line(x1 - 1 - offset, y0, x1 - 1 - offset, y1 - 1, stroke)

    def line(self, x1: float, y1: float, x2: float, y2: float, color: str, width: int = 1) -> None:
        x1_i = int(round(x1))
        y1_i = int(round(y1))
        x2_i = int(round(x2))
        y2_i = int(round(y2))
        dx = abs(x2_i - x1_i)
        sx = 1 if x1_i < x2_i else -1
        dy = -abs(y2_i - y1_i)
        sy = 1 if y1_i < y2_i else -1
        error = dx + dy
        while True:
            half = max(0, width // 2)
            for oy in range(-half, half + 1):
                for ox in range(-half, half + 1):
                    self.set_pixel(x1_i + ox, y1_i + oy, color)
            if x1_i == x2_i and y1_i == y2_i:
                break
            twice = 2 * error
            if twice >= dy:
                error += dy
                x1_i += sx
            if twice <= dx:
                error += dx
                y1_i += sy

    def polyline(
        self, points: Iterable[tuple[float, float]], color: str, width: int = 3
    ) -> None:
        points = list(points)
        for index in range(len(points) - 1):
            x1, y1 = points[index]
            x2, y2 = points[index + 1]
            self.line(x1, y1, x2, y2, color, width)

    def measure_text(self, text: str, scale: int = 2) -> int:
        normalized = normalize_ascii(text)
        return len(normalized) * 6 * scale - scale

    def text(
        self,
        x: float,
        y: float,
        text: str,
        color: str,
        size: int = 16,
        anchor: str = "left",
        weight: str = "400",
    ) -> None:
        del weight
        scale = max(1, size // 8)
        normalized = normalize_ascii(text)
        if anchor == "center":
            x = x - self.measure_text(normalized, scale) / 2
        elif anchor == "right":
            x = x - self.measure_text(normalized, scale)
        cursor_x = int(round(x))
        cursor_y = int(round(y))
        for char in normalized:
            glyph = BITMAP_FONT.get(char, BITMAP_FONT[" "])
            for row_index, row in enumerate(glyph):
                for col_index, bit in enumerate(row):
                    if bit == "1":
                        for oy in range(scale):
                            for ox in range(scale):
                                self.set_pixel(
                                    cursor_x + col_index * scale + ox,
                                    cursor_y + row_index * scale + oy,
                                    color,
                                )
            cursor_x += 6 * scale

    def text_block(
        self,
        x: float,
        y: float,
        text: str,
        color: str,
        size: int,
        max_chars: int,
        line_gap: int = 8,
        anchor: str = "left",
        weight: str = "400",
    ) -> None:
        del weight
        line_height = size + line_gap
        for index, line in enumerate(wrap_text(text, max_chars)):
            self.text(
                x,
                y + index * line_height,
                line,
                color,
                size=size,
                anchor=anchor,
            )

    def save_png(self, path: Path) -> None:
        raw = bytearray()
        stride = self.width * 3
        for y in range(self.height):
            raw.append(0)
            start = y * stride
            raw.extend(self.buffer[start : start + stride])
        payload = zlib.compress(bytes(raw), level=9)

        def chunk(name: bytes, data: bytes) -> bytes:
            return (
                struct.pack("!I", len(data))
                + name
                + data
                + struct.pack("!I", zlib.crc32(name + data) & 0xFFFFFFFF)
            )

        png = bytearray(b"\x89PNG\r\n\x1a\n")
        png.extend(
            chunk(
                b"IHDR",
                struct.pack("!IIBBBBB", self.width, self.height, 8, 2, 0, 0, 0),
            )
        )
        png.extend(chunk(b"IDAT", payload))
        png.extend(chunk(b"IEND", b""))
        path.write_bytes(bytes(png))


def write_svg(path: Path, payload: str) -> None:
    path.write_text(payload, encoding="utf-8")


def draw_header(canvas, spec: dict) -> None:
    canvas.rect(50, 38, 1300, 116, "#FFFDF8", stroke="#E4D8C8", stroke_width=1, radius=22)
    canvas.text(78, 68, "ELETRO NAUTICA / VISUAL TECNICO", PALETTE["muted"], size=12, weight="700")
    canvas.text_block(
        78,
        92,
        spec["title"],
        PALETTE["ink"],
        size=24,
        max_chars=68,
        line_gap=6,
        weight="700",
    )
    canvas.text_block(
        78,
        128,
        spec["summary"],
        PALETTE["muted"],
        size=13,
        max_chars=132,
        line_gap=5,
    )


def draw_footer(canvas, spec: dict) -> None:
    canvas.text(
        70,
        862,
        f"FORMATO: {spec['format'].upper()}  |  PRIORIDADE: {spec['priority'].upper()}",
        PALETTE["muted"],
        size=14,
    )


def draw_arrow(canvas, x1: float, y1: float, x2: float, y2: float, color: str, width: int = 3) -> None:
    canvas.line(x1, y1, x2, y2, color, width=width)
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 18
    for delta in (math.radians(150), math.radians(-150)):
        canvas.line(
            x2,
            y2,
            x2 + math.cos(angle + delta) * size,
            y2 + math.sin(angle + delta) * size,
            color,
            width=width,
        )


def draw_card(
    canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    title: str,
    detail: str,
    color: str,
    items: list[str] | None = None,
) -> None:
    canvas.rect(x, y, width, height, PALETTE["panel"], stroke=PALETTE["grid"], stroke_width=1)
    canvas.rect(x, y, width, 12, color, radius=10)
    canvas.text_block(x + 24, y + 44, title, PALETTE["ink"], size=18, max_chars=24, line_gap=5, weight="700")
    canvas.text_block(x + 24, y + 92, detail, PALETTE["muted"], size=14, max_chars=34, line_gap=6)
    if items and height >= 220:
        item_y = y + height - 76
        for item in items[:3]:
            canvas.rect(x + 24, item_y - 11, 8, 8, color)
            canvas.text_block(x + 42, item_y, item, PALETTE["text"], size=12, max_chars=31, line_gap=4)
            item_y += 24


def draw_grid(canvas, x: int, y: int, width: int, height: int) -> None:
    canvas.rect(x, y, width, height, PALETTE["panel"], stroke=PALETTE["grid"], stroke_width=1)
    for index in range(1, 6):
        canvas.line(
            x,
            y + height * index / 6,
            x + width,
            y + height * index / 6,
            PALETTE["grid"],
            width=1,
        )
    for index in range(1, 8):
        canvas.line(
            x + width * index / 8,
            y,
            x + width * index / 8,
            y + height,
            PALETTE["grid"],
            width=1,
        )


def wave_points(
    x: int,
    y: int,
    width: int,
    height: int,
    cycles: float,
    mode: str,
    samples: int = 180,
) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    for sample in range(samples + 1):
        ratio = sample / samples
        px = x + ratio * width
        angle = ratio * cycles * math.tau
        if mode == "sine":
            value = math.sin(angle)
        elif mode == "square":
            value = 1.0 if math.sin(angle) >= 0 else -1.0
        else:
            raise ValueError(f"Unsupported wave mode: {mode}")
        py = y + height / 2 - value * (height * 0.32)
        points.append((px, py))
    return points


def render_wave_compare(spec: dict) -> tuple[str, RasterCanvas]:
    width, height = 1400, 900
    svg = SvgCanvas(width, height)
    png = RasterCanvas(width, height, PALETTE["background"])
    for canvas in (svg, png):
        draw_header(canvas, spec)
        canvas.rect(70, 140, 1260, 72, "#FFF7E8", stroke="#F0C36D", stroke_width=2)
        canvas.text(
            700,
            185,
            spec["hero_label"],
            PALETTE["ink"],
            size=18,
            anchor="center",
            weight="700",
        )
        panel_x = 70
        panel_y = 245
        panel_width = 860
        panel_height = 220
        for index, panel in enumerate(spec["panels"]):
            box_y = panel_y + index * 255
            draw_grid(canvas, panel_x, box_y, panel_width, panel_height)
            canvas.text(panel_x + 24, box_y + 34, panel["label"], panel["color"], size=22, weight="700")
            points = wave_points(
                panel_x + 20,
                box_y + 30,
                panel_width - 40,
                panel_height - 60,
                panel["cycles"],
                panel["wave"],
            )
            canvas.polyline(points, panel["color"], width=4)
            canvas.text(
                panel_x + panel_width - 24,
                box_y + 34,
                panel["tag"],
                PALETTE["muted"],
                size=14,
                anchor="right",
            )
        canvas.rect(970, 245, 360, 475, PALETTE["panel"], stroke=PALETTE["grid"], stroke_width=1)
        canvas.text(995, 280, "IMPLICACOES PRATICAS", PALETTE["ink"], size=18, weight="700")
        bullet_y = 320
        for bullet in spec["bullets"]:
            canvas.rect(995, bullet_y - 12, 10, 10, bullet["color"])
            canvas.text(1018, bullet_y, bullet["title"], PALETTE["text"], size=16, weight="700")
            canvas.text_block(
                1018,
                bullet_y + 24,
                bullet["detail"],
                PALETTE["muted"],
                size=14,
                max_chars=34,
            )
            bullet_y += 96
        draw_footer(canvas, spec)
    return svg.finalize(), png


def render_frequency_compare(spec: dict) -> tuple[str, RasterCanvas]:
    width, height = 1400, 900
    svg = SvgCanvas(width, height)
    png = RasterCanvas(width, height, PALETTE["background"])
    for canvas in (svg, png):
        draw_header(canvas, spec)
        canvas.rect(70, 140, 1260, 72, "#EEF7FF", stroke="#8CB9F4", stroke_width=2)
        canvas.text(700, 185, spec["hero_label"], PALETTE["ink"], size=18, anchor="center", weight="700")
        for index, panel in enumerate(spec["panels"]):
            box_y = 245 + index * 255
            draw_grid(canvas, 70, box_y, 860, 220)
            canvas.text(94, box_y + 34, panel["label"], panel["color"], size=22, weight="700")
            canvas.text(900, box_y + 34, panel["tag"], PALETTE["muted"], size=14, anchor="right")
            points = wave_points(90, box_y + 30, 820, 160, panel["cycles"], "sine")
            canvas.polyline(points, panel["color"], width=4)
        canvas.rect(970, 245, 360, 475, PALETTE["panel"], stroke=PALETTE["grid"], stroke_width=1)
        canvas.text(995, 280, "O QUE MUDA NA PRATICA", PALETTE["ink"], size=18, weight="700")
        bullet_y = 320
        for bullet in spec["bullets"]:
            canvas.rect(995, bullet_y - 12, 10, 10, bullet["color"])
            canvas.text(1018, bullet_y, bullet["title"], PALETTE["text"], size=16, weight="700")
            canvas.text_block(
                1018,
                bullet_y + 24,
                bullet["detail"],
                PALETTE["muted"],
                size=14,
                max_chars=34,
            )
            bullet_y += 96
        draw_footer(canvas, spec)
    return svg.finalize(), png


def render_battery_zone(spec: dict) -> tuple[str, RasterCanvas]:
    width, height = 1400, 900
    svg = SvgCanvas(width, height)
    png = RasterCanvas(width, height, PALETTE["background"])
    bar_x = 110
    bar_y = 360
    bar_width = 1180
    bar_height = 110
    vmin = spec["voltage_min"]
    vmax = spec["voltage_max"]

    def to_x(value: float) -> float:
        return bar_x + (value - vmin) / (vmax - vmin) * bar_width

    for canvas in (svg, png):
        draw_header(canvas, spec)
        canvas.rect(70, 140, 1260, 100, "#FFF7E8", stroke="#F0C36D", stroke_width=2)
        canvas.text(700, 180, spec["hero_label"], PALETTE["ink"], size=18, anchor="center", weight="700")
        canvas.text(700, 210, spec["caution_short"], PALETTE["muted"], size=14, anchor="center")
        canvas.rect(bar_x, bar_y, bar_width, bar_height, PALETTE["panel"], stroke=PALETTE["grid"], stroke_width=1)
        for zone in spec["zones"]:
            zone_x = to_x(zone["start"])
            zone_width = to_x(zone["end"]) - zone_x
            canvas.rect(zone_x, bar_y, zone_width, bar_height, zone["color"], stroke=None, radius=8)
            canvas.text(zone_x + zone_width / 2, bar_y + 48, zone["label"], PALETTE["ink"], size=18, anchor="center", weight="700")
            canvas.text(zone_x + zone_width / 2, bar_y + 78, zone["range"], PALETTE["text"], size=14, anchor="center")
        for mark in spec["marks"]:
            x = to_x(mark["value"])
            canvas.line(x, bar_y + bar_height, x, bar_y + bar_height + 26, PALETTE["ink"], width=2)
            canvas.text(x, bar_y + bar_height + 48, mark["label"], PALETTE["text"], size=14, anchor="center")
        canvas.rect(90, 560, 1240, 160, PALETTE["panel"], stroke=PALETTE["grid"], stroke_width=1)
        canvas.text(120, 598, "COMO LER ESTE QUADRO", PALETTE["ink"], size=18, weight="700")
        text_y = 636
        for bullet in spec["bullets"]:
            canvas.rect(120, text_y - 12, 10, 10, bullet["color"])
            canvas.text(144, text_y, bullet["title"], PALETTE["text"], size=16, weight="700")
            canvas.text_block(
                144,
                text_y + 24,
                bullet["detail"],
                PALETTE["muted"],
                size=14,
                max_chars=84,
            )
            text_y += 42
        draw_footer(canvas, spec)
    return svg.finalize(), png


def render_flow_diagram(spec: dict) -> tuple[str, RasterCanvas]:
    width, height = 1400, 900
    svg = SvgCanvas(width, height)
    png = RasterCanvas(width, height, PALETTE["background"])
    nodes = spec["nodes"]
    callouts = spec.get("callouts", [])
    node_count = len(nodes)
    gap = 22
    node_width = (1260 - gap * (node_count - 1)) / node_count
    node_height = 190
    node_y = 300

    for canvas in (svg, png):
        draw_header(canvas, spec)
        canvas.rect(70, 178, 1260, 80, "#EEF7FF", stroke="#8CB9F4", stroke_width=2)
        canvas.text_block(700, 208, spec["hero_label"], PALETTE["ink"], size=18, max_chars=72, anchor="center", weight="700")
        for index, node in enumerate(nodes):
            x = 70 + index * (node_width + gap)
            draw_card(
                canvas,
                x,
                node_y,
                node_width,
                node_height,
                node["title"],
                node["detail"],
                node.get("color", PALETTE["blue"]),
                node.get("items"),
            )
            if index < node_count - 1:
                draw_arrow(
                    canvas,
                    x + node_width + 4,
                    node_y + node_height / 2,
                    x + node_width + gap - 6,
                    node_y + node_height / 2,
                    PALETTE["muted"],
                    width=2,
                )
        canvas.rect(70, 560, 1260, 165, PALETTE["panel"], stroke=PALETTE["grid"], stroke_width=1)
        canvas.text(100, 598, spec.get("callout_title", "PONTOS DE ATENCAO"), PALETTE["ink"], size=18, weight="700")
        columns = max(1, min(3, len(callouts)))
        column_width = 1180 / columns
        for index, callout in enumerate(callouts[:6]):
            column = index % columns
            row = index // columns
            x = 100 + column * column_width
            y = 635 + row * 54
            color = callout.get("color", PALETTE["orange"])
            canvas.rect(x, y - 13, 10, 10, color)
            canvas.text(x + 24, y, callout["title"], PALETTE["text"], size=15, weight="700")
            canvas.text_block(x + 24, y + 22, callout["detail"], PALETTE["muted"], size=12, max_chars=36, line_gap=4)
        draw_footer(canvas, spec)
    return svg.finalize(), png


def render_comparison_cards(spec: dict) -> tuple[str, RasterCanvas]:
    width, height = 1400, 900
    svg = SvgCanvas(width, height)
    png = RasterCanvas(width, height, PALETTE["background"])
    cards = spec["cards"]
    columns = min(4, max(2, spec.get("columns", len(cards))))
    rows = math.ceil(len(cards) / columns)
    gap = 24
    card_width = (1260 - gap * (columns - 1)) / columns
    card_height = 190 if rows == 2 else 260

    for canvas in (svg, png):
        draw_header(canvas, spec)
        canvas.rect(70, 178, 1260, 80, "#FFF7E8", stroke="#F0C36D", stroke_width=2)
        canvas.text_block(700, 208, spec["hero_label"], PALETTE["ink"], size=18, max_chars=72, anchor="center", weight="700")
        for index, card in enumerate(cards):
            column = index % columns
            row = index // columns
            x = 70 + column * (card_width + gap)
            y = 300 + row * (card_height + 34)
            draw_card(
                canvas,
                x,
                y,
                card_width,
                card_height,
                card["title"],
                card["detail"],
                card.get("color", PALETTE["blue"]),
                card.get("items"),
            )
        draw_footer(canvas, spec)
    return svg.finalize(), png


def render_cause_effect(spec: dict) -> tuple[str, RasterCanvas]:
    width, height = 1400, 900
    svg = SvgCanvas(width, height)
    png = RasterCanvas(width, height, PALETTE["background"])
    columns = spec["columns"]
    column_width = 386
    gap = 42
    start_x = 70

    for canvas in (svg, png):
        draw_header(canvas, spec)
        canvas.rect(70, 178, 1260, 80, "#FFF0F0", stroke="#E9A2A2", stroke_width=2)
        canvas.text_block(700, 208, spec["hero_label"], PALETTE["ink"], size=18, max_chars=72, anchor="center", weight="700")
        for column_index, column in enumerate(columns):
            x = start_x + column_index * (column_width + gap)
            canvas.rect(x, 300, column_width, 425, PALETTE["panel"], stroke=PALETTE["grid"], stroke_width=1)
            color = column.get("color", PALETTE["red"])
            canvas.rect(x, 300, column_width, 14, color, radius=10)
            canvas.text(x + 24, 350, column["title"], PALETTE["ink"], size=20, weight="700")
            y = 402
            for item in column["items"]:
                canvas.rect(x + 24, y - 13, 10, 10, color)
                canvas.text_block(x + 46, y, item, PALETTE["text"], size=14, max_chars=34, line_gap=5)
                y += 72
            if column_index < len(columns) - 1:
                draw_arrow(canvas, x + column_width + 8, 512, x + column_width + gap - 10, 512, PALETTE["muted"], width=2)
        draw_footer(canvas, spec)
    return svg.finalize(), png


def render_spec(spec: dict) -> dict[str, str | RasterCanvas]:
    kind = spec["kind"]
    if kind == "wave_compare":
        svg_payload, png_canvas = render_wave_compare(spec)
    elif kind == "frequency_compare":
        svg_payload, png_canvas = render_frequency_compare(spec)
    elif kind == "battery_zone":
        svg_payload, png_canvas = render_battery_zone(spec)
    elif kind == "flow_diagram":
        svg_payload, png_canvas = render_flow_diagram(spec)
    elif kind == "comparison_cards":
        svg_payload, png_canvas = render_comparison_cards(spec)
    elif kind == "cause_effect":
        svg_payload, png_canvas = render_cause_effect(spec)
    else:
        raise ValueError(f"Unsupported spec kind: {kind}")

    markdown = build_markdown(spec)
    return {
        "svg": svg_payload,
        "png": png_canvas,
        "md": markdown,
    }


def build_markdown(spec: dict) -> str:
    lines = [
        f"# {spec['title']}",
        "",
        "## Objetivo didático",
        "",
        spec["didactic_goal"],
        "",
        "## Formato recomendado",
        "",
        f"- Tipo: `{spec['format']}`",
        f"- Prioridade: `{spec['priority']}`",
        "",
        "## Como ler",
        "",
    ]
    for bullet in spec["notes"]:
        lines.append(f"- {bullet}")
    lines.extend(
        [
            "",
            "## Cautelas",
            "",
            f"- {spec['caution']}",
            "",
            "## Notas sugeridas para embedding",
            "",
        ]
    )
    for note_path in spec["target_notes"]:
        lines.append(f"- `{note_path}`")
    lines.extend(
        [
            "",
            "## Arquivos gerados",
            "",
            f"- `{spec['slug']}.svg`",
            f"- `{spec['slug']}.png`",
            f"- `{spec['slug']}.md`",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"
