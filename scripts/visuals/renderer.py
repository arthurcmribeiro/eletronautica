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

    def circle(
        self,
        x: float,
        y: float,
        radius: float,
        fill: str,
        stroke: str | None = None,
        stroke_width: float = 1,
    ) -> None:
        attrs = [
            f'cx="{x}"',
            f'cy="{y}"',
            f'r="{radius}"',
            f'fill="{fill}"',
        ]
        if stroke:
            attrs.append(f'stroke="{stroke}"')
            attrs.append(f'stroke-width="{stroke_width}"')
        self.parts.append(f"<circle {' '.join(attrs)}/>")

    def polygon(
        self,
        points: Iterable[tuple[float, float]],
        fill: str,
        stroke: str | None = None,
        stroke_width: float = 1,
    ) -> None:
        serialized = " ".join(f"{x},{y}" for x, y in points)
        attrs = [f'points="{serialized}"', f'fill="{fill}"']
        if stroke:
            attrs.append(f'stroke="{stroke}"')
            attrs.append(f'stroke-width="{stroke_width}"')
        self.parts.append(f"<polygon {' '.join(attrs)}/>")

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
                f'font-family="Bahnschrift, Segoe UI, Arial, sans-serif" font-size="{size}" '
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
    def __init__(self, width: int, height: int, background: str, scale: int = 2) -> None:
        self.width = width
        self.height = height
        self.scale_factor = scale
        self.pixel_width = width * scale
        self.pixel_height = height * scale
        self.buffer = bytearray(self.pixel_width * self.pixel_height * 3)
        self.fill(background)

    def fill(self, color: str) -> None:
        r, g, b = hex_to_rgb(color)
        row = bytes([r, g, b]) * self.pixel_width
        for y in range(self.pixel_height):
            start = y * self.pixel_width * 3
            self.buffer[start : start + len(row)] = row

    def set_pixel(self, x: int, y: int, color: str) -> None:
        if not (0 <= x < self.pixel_width and 0 <= y < self.pixel_height):
            return
        r, g, b = hex_to_rgb(color)
        index = (y * self.pixel_width + x) * 3
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
        scale = self.scale_factor
        x0 = max(0, int(round(x * scale)))
        y0 = max(0, int(round(y * scale)))
        x1 = min(self.pixel_width, int(round((x + width) * scale)))
        y1 = min(self.pixel_height, int(round((y + height) * scale)))
        if x1 <= x0 or y1 <= y0:
            return
        r, g, b = hex_to_rgb(fill)
        row = bytes([r, g, b]) * (x1 - x0)
        for py in range(y0, y1):
            start = (py * self.pixel_width + x0) * 3
            self.buffer[start : start + len(row)] = row
        if stroke:
            stroke_px = max(1, int(round(stroke_width * scale)))
            for offset in range(stroke_px):
                self.line(x0, y0 + offset, x1 - 1, y0 + offset, stroke, scaled=True)
                self.line(x0, y1 - 1 - offset, x1 - 1, y1 - 1 - offset, stroke, scaled=True)
                self.line(x0 + offset, y0, x0 + offset, y1 - 1, stroke, scaled=True)
                self.line(x1 - 1 - offset, y0, x1 - 1 - offset, y1 - 1, stroke, scaled=True)

    def circle(
        self,
        x: float,
        y: float,
        radius: float,
        fill: str,
        stroke: str | None = None,
        stroke_width: float = 1,
    ) -> None:
        scale = self.scale_factor
        cx = int(round(x * scale))
        cy = int(round(y * scale))
        outer = int(round(radius * scale))
        inner = max(0, int(round((radius - stroke_width) * scale)))
        outer_sq = outer * outer
        inner_sq = inner * inner
        for py in range(cy - outer, cy + outer + 1):
            for px in range(cx - outer, cx + outer + 1):
                distance_sq = (px - cx) * (px - cx) + (py - cy) * (py - cy)
                if distance_sq <= outer_sq:
                    if stroke and distance_sq >= inner_sq:
                        self.set_pixel(px, py, stroke)
                    else:
                        self.set_pixel(px, py, fill)

    def polygon(
        self,
        points: Iterable[tuple[float, float]],
        fill: str,
        stroke: str | None = None,
        stroke_width: float = 1,
    ) -> None:
        scale = self.scale_factor
        points = [(x * scale, y * scale) for x, y in points]
        if len(points) < 3:
            return
        min_x = max(0, int(math.floor(min(x for x, _ in points))))
        max_x = min(self.pixel_width - 1, int(math.ceil(max(x for x, _ in points))))
        min_y = max(0, int(math.floor(min(y for _, y in points))))
        max_y = min(self.pixel_height - 1, int(math.ceil(max(y for _, y in points))))
        for py in range(min_y, max_y + 1):
            for px in range(min_x, max_x + 1):
                inside = False
                j = len(points) - 1
                for i, point in enumerate(points):
                    xi, yi = point
                    xj, yj = points[j]
                    intersects = (yi > py) != (yj > py) and px < (
                        (xj - xi) * (py - yi) / ((yj - yi) or 1e-9) + xi
                    )
                    if intersects:
                        inside = not inside
                    j = i
                if inside:
                    self.set_pixel(px, py, fill)
        if stroke:
            for index, point in enumerate(points):
                next_point = points[(index + 1) % len(points)]
                self.line(
                    point[0],
                    point[1],
                    next_point[0],
                    next_point[1],
                    stroke,
                    max(1, int(stroke_width * scale)),
                    scaled=True,
                )

    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        color: str,
        width: int = 1,
        dash: str | None = None,
        scaled: bool = False,
    ) -> None:
        del dash
        scale = 1 if scaled else self.scale_factor
        x1_i = int(round(x1 * scale))
        y1_i = int(round(y1 * scale))
        x2_i = int(round(x2 * scale))
        y2_i = int(round(y2 * scale))
        width = max(1, int(round(width * scale)))
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
        logical_scale = max(1, size // 8)
        normalized = normalize_ascii(text)
        if anchor == "center":
            x = x - self.measure_text(normalized, logical_scale) / 2
        elif anchor == "right":
            x = x - self.measure_text(normalized, logical_scale)
        glyph_scale = logical_scale * self.scale_factor
        cursor_x = int(round(x * self.scale_factor))
        cursor_y = int(round(y * self.scale_factor))
        for char in normalized:
            glyph = BITMAP_FONT.get(char, BITMAP_FONT[" "])
            for row_index, row in enumerate(glyph):
                for col_index, bit in enumerate(row):
                    if bit == "1":
                        for oy in range(glyph_scale):
                            for ox in range(glyph_scale):
                                self.set_pixel(
                                    cursor_x + col_index * glyph_scale + ox,
                                    cursor_y + row_index * glyph_scale + oy,
                                    color,
                                )
            cursor_x += 6 * glyph_scale

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
        stride = self.pixel_width * 3
        for y in range(self.pixel_height):
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
                struct.pack("!IIBBBBB", self.pixel_width, self.pixel_height, 8, 2, 0, 0, 0),
            )
        )
        png.extend(chunk(b"IDAT", payload))
        png.extend(chunk(b"IEND", b""))
        path.write_bytes(bytes(png))


def write_svg(path: Path, payload: str) -> None:
    path.write_text(payload, encoding="utf-8")


def draw_header(canvas, spec: dict) -> None:
    canvas.rect(0, 0, canvas.width, canvas.height, PALETTE["background"], radius=0)
    canvas.circle(1238, 96, 118, "#E8F1FB")
    canvas.circle(1320, 32, 64, "#F8E6CC")
    canvas.rect(50, 34, 1300, 132, "#FFFDF8", stroke="#E4D8C8", stroke_width=1, radius=24)
    canvas.rect(50, 34, 14, 132, PALETTE["orange"], radius=20)
    canvas.text(82, 64, "CARTILHA VISUAL | ELETRO NAUTICA", PALETTE["muted"], size=12, weight="700")
    canvas.text_block(
        82,
        96,
        spec["title"],
        PALETTE["ink"],
        size=25,
        max_chars=62,
        line_gap=6,
        weight="700",
    )
    canvas.text_block(
        82,
        138,
        spec["summary"],
        PALETTE["muted"],
        size=13,
        max_chars=116,
        line_gap=5,
    )
    canvas.rect(1130, 58, 176, 58, "#0F172A", radius=18)
    canvas.text(1218, 80, "SVG + PNG", "#FFFDF8", size=14, anchor="center", weight="700")
    canvas.text(1218, 104, "versionavel", "#D9E2EC", size=11, anchor="center")


def draw_footer(canvas, spec: dict) -> None:
    canvas.line(70, 842, 1330, 842, "#E4D8C8", width=1)
    canvas.text(
        70,
        868,
        f"FORMATO: {spec['format'].upper()} | PRIORIDADE: {spec['priority'].upper()} | USE COMO APOIO DIDATICO, NAO COMO NORMA ISOLADA",
        PALETTE["muted"],
        size=12,
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


def text_y(canvas, y: float, raster_offset: float = -8) -> float:
    if isinstance(canvas, RasterCanvas):
        return y + raster_offset
    return y


def draw_badge(
    canvas,
    x: float,
    y: float,
    label: str,
    color: str,
    radius: float = 34,
    text_color: str = "#FFFDF8",
) -> None:
    canvas.circle(x, y, radius + 5, "#FFFFFF", stroke="#E4D8C8", stroke_width=1)
    canvas.circle(x, y, radius, color)
    canvas.text(x, text_y(canvas, y + 7, -10), label, text_color, size=20, anchor="center", weight="700")


def draw_pill(canvas, x: float, y: float, text: str, color: str, width: float | None = None) -> None:
    pill_width = width if width is not None else max(86, min(210, len(text) * 9 + 28))
    canvas.rect(x, y, pill_width, 28, "#FFFDF8", stroke=color, stroke_width=1, radius=14)
    canvas.circle(x + 16, y + 14, 5, color)
    canvas.text_block(x + 29, y + 18, text, PALETTE["text"], size=11, max_chars=max(10, int((pill_width - 42) / 7)), line_gap=2)


def draw_section_label(canvas, x: float, y: float, label: str, color: str) -> None:
    canvas.rect(x, y, 10, 28, color, radius=6)
    canvas.text(x + 20, y + 20, label.upper(), color, size=13, weight="700")


def draw_info_panel(
    canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    label: str,
    title: str,
    body: str,
    color: str,
) -> None:
    canvas.rect(x, y, width, height, PALETTE["panel"], stroke="#E4D8C8", stroke_width=1, radius=24)
    draw_section_label(canvas, x + 22, y + 22, label, color)
    canvas.text_block(x + 24, y + 78, title, PALETTE["ink"], size=19, max_chars=max(16, int(width / 13)), line_gap=5, weight="700")
    canvas.text_block(x + 24, y + 142, body, PALETTE["muted"], size=13, max_chars=max(28, int(width / 8)), line_gap=6)


def draw_note_strip(
    canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    title: str,
    notes: list[str],
    color: str,
    columns: int = 3,
) -> None:
    canvas.rect(x, y, width, height, "#FFFDF8", stroke="#E4D8C8", stroke_width=1, radius=24)
    canvas.text(x + 24, y + 34, title.upper(), PALETTE["ink"], size=15, weight="700")
    columns = max(1, columns)
    column_width = (width - 52) / columns
    for index, note in enumerate(notes[:columns]):
        item_x = x + 24 + index * column_width
        canvas.circle(item_x + 10, y + 72, 10, color)
        canvas.text(item_x + 10, text_y(canvas, y + 78, -6), str(index + 1), "#FFFDF8", size=10, anchor="center", weight="700")
        canvas.text_block(item_x + 30, y + 69, note, PALETTE["muted"], size=12, max_chars=max(22, int((column_width - 42) / 7)), line_gap=4)


def draw_signal_bars(canvas, x: float, y: float, color: str) -> None:
    for index, bar_height in enumerate((22, 38, 56, 74)):
        canvas.rect(x + index * 20, y - bar_height, 12, bar_height, color, radius=5)
    canvas.line(x - 10, y, x + 92, y, PALETTE["grid"], width=2)


def draw_simple_icon(canvas, x: float, y: float, title: str, color: str) -> None:
    normalized = normalize_ascii(title)
    if any(token in normalized for token in ("BATERIA", "BANCO", "TENS", "FONTE")):
        canvas.rect(x - 26, y - 14, 44, 28, "#FFFDF8", stroke=color, stroke_width=3, radius=5)
        canvas.rect(x + 18, y - 6, 8, 12, color, radius=2)
        canvas.line(x - 14, y, x - 2, y, color, width=3)
        canvas.line(x + 5, y, x + 15, y, color, width=3)
        canvas.line(x + 10, y - 5, x + 10, y + 5, color, width=3)
    elif any(token in normalized for token in ("AGUA", "BOMBA", "HIDRAUL", "TANQUE")):
        canvas.circle(x, y - 3, 18, "#FFFDF8", stroke=color, stroke_width=3)
        canvas.line(x, y - 28, x - 15, y - 5, color, width=3)
        canvas.line(x, y - 28, x + 15, y - 5, color, width=3)
    elif any(token in normalized for token in ("RADAR", "AIS", "VHF", "ANTENA", "GPS", "DSC")):
        canvas.line(x, y + 24, x, y - 24, color, width=4)
        canvas.line(x - 22, y + 22, x, y - 2, color, width=3)
        canvas.line(x + 22, y + 22, x, y - 2, color, width=3)
        canvas.circle(x, y - 2, 6, color)
    elif any(token in normalized for token in ("FUSIVEL", "DISJUNTOR", "PROTE", "EXTINTOR", "ALARME")):
        canvas.polygon(((x, y - 30), (x + 26, y - 16), (x + 20, y + 22), (x, y + 32), (x - 20, y + 22), (x - 26, y - 16)), "#FFFDF8", stroke=color, stroke_width=3)
        canvas.line(x - 10, y - 2, x, y + 10, color, width=3)
        canvas.line(x, y + 10, x + 14, y - 12, color, width=3)
    elif any(token in normalized for token in ("MED", "MULT", "CALC", "OHM", "CORRENTE")):
        canvas.rect(x - 24, y - 24, 48, 48, "#FFFDF8", stroke=color, stroke_width=3, radius=10)
        canvas.polyline(((x - 14, y + 6), (x - 5, y - 8), (x + 6, y + 2), (x + 15, y - 16)), color, width=3)
    else:
        canvas.circle(x, y, 22, "#FFFDF8", stroke=color, stroke_width=3)
        canvas.line(x - 12, y, x + 12, y, color, width=3)
        canvas.line(x, y - 12, x, y + 12, color, width=3)


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

    for canvas in (svg, png):
        draw_header(canvas, spec)
        canvas.rect(70, 188, 850, 74, "#EEF7FF", stroke="#8CB9F4", stroke_width=2, radius=24)
        canvas.text_block(96, 218, spec["hero_label"], PALETTE["ink"], size=18, max_chars=62, weight="700")
        canvas.rect(950, 188, 380, 74, "#0F172A", radius=24)
        canvas.text(1140, 217, "LEITURA EM CAMPO", "#FFFDF8", size=15, anchor="center", weight="700")
        canvas.text(1140, 242, "siga evidencias, nao palpites", "#D9E2EC", size=12, anchor="center")

        canvas.rect(70, 292, 1260, 304, "#FFFDF8", stroke="#E4D8C8", stroke_width=1, radius=30)
        draw_section_label(canvas, 102, 322, "mapa do processo", PALETTE["teal"])
        canvas.text_block(102, 356, "Leia como uma sequencia de decisoes: cada etapa deixa uma evidencia para a proxima.", PALETTE["muted"], size=12, max_chars=82, line_gap=5)
        canvas.line(150, 466, 1250, 466, "#D9E2EC", width=2, dash="8 10")

        positions: list[tuple[float, float]] = []
        for index in range(node_count):
            ratio = 0.0 if node_count == 1 else index / (node_count - 1)
            positions.append((170 + ratio * 1060, 422 if index % 2 == 0 else 514))
        for index in range(node_count - 1):
            x1, y1 = positions[index]
            x2, y2 = positions[index + 1]
            draw_arrow(canvas, x1 + 40, y1, x2 - 40, y2, PALETTE["muted"], width=2)

        for index, node in enumerate(nodes):
            x, y = positions[index]
            color = node.get("color", PALETTE["blue"])
            draw_badge(canvas, x, y, str(index + 1), color, radius=32)
            draw_simple_icon(canvas, x, y - 66, node["title"], color)
            label_y = y + 46 if y < 470 else y - 118
            label_x = min(1220, max(92, x - 92))
            canvas.rect(label_x, label_y, 184, 78, "#FEFCF5", stroke="#E4D8C8", stroke_width=1, radius=18)
            canvas.text_block(label_x + 16, label_y + 26, node["title"], PALETTE["ink"], size=14, max_chars=19, line_gap=4, weight="700")
            lead = node.get("items", [node["detail"]])[0] if node.get("items") else node["detail"]
            canvas.text_block(label_x + 16, label_y + 52, lead, PALETTE["muted"], size=10, max_chars=24, line_gap=4)

        canvas.rect(70, 622, 388, 82, "#FFFDF8", stroke="#E4D8C8", stroke_width=1, radius=22)
        draw_section_label(canvas, 96, 642, "pergunta-guia", PALETTE["blue"])
        canvas.text_block(96, 680, spec["didactic_goal"], PALETTE["muted"], size=11, max_chars=48, line_gap=4)

        canvas.rect(486, 622, 392, 82, "#FFFDF8", stroke="#E4D8C8", stroke_width=1, radius=22)
        draw_section_label(canvas, 512, 642, "aplique assim", PALETTE["green"])
        canvas.text_block(512, 680, "Confirme entrada, caminho, protecao, carga e registro antes de concluir.", PALETTE["muted"], size=11, max_chars=48, line_gap=4)

        canvas.rect(906, 622, 424, 82, "#FFFDF8", stroke="#E4D8C8", stroke_width=1, radius=22)
        draw_section_label(canvas, 932, 642, "atencao", PALETTE["orange"])
        canvas.text_block(932, 680, spec.get("callout_title", "PONTOS DE ATENCAO"), PALETTE["muted"], size=11, max_chars=52, line_gap=4)

        callout_source = callouts if callouts else [{"title": "Aplique", "detail": note, "color": PALETTE["orange"]} for note in spec.get("notes", [])]
        strip_notes = [f"{callout['title']}: {callout['detail']}" for callout in callout_source[:4]]
        if len(strip_notes) < 4:
            strip_notes.extend(spec.get("notes", [])[: 4 - len(strip_notes)])
        draw_note_strip(
            canvas,
            70,
            724,
            1260,
            98,
            "erros comuns e leituras uteis",
            strip_notes,
            PALETTE["teal"],
            columns=4,
        )
        draw_footer(canvas, spec)
    return svg.finalize(), png


def render_comparison_cards(spec: dict) -> tuple[str, RasterCanvas]:
    width, height = 1400, 900
    svg = SvgCanvas(width, height)
    png = RasterCanvas(width, height, PALETTE["background"])
    cards = spec["cards"]

    for canvas in (svg, png):
        draw_header(canvas, spec)
        canvas.rect(70, 188, 1260, 74, "#FFF7E8", stroke="#F0C36D", stroke_width=2, radius=24)
        canvas.text_block(700, 218, spec["hero_label"], PALETTE["ink"], size=18, max_chars=68, anchor="center", weight="700")

        draw_info_panel(
            canvas,
            70,
            292,
            306,
            385,
            "ideia-chave",
            "Compare antes de aplicar.",
            spec["didactic_goal"],
            PALETTE["orange"],
        )
        canvas.text(105, 636, "pergunte sempre:", PALETTE["ink"], size=13, weight="700")
        canvas.text_block(105, 660, "O que muda? O que nao muda? Onde isso aparece no barco?", PALETTE["muted"], size=12, max_chars=31, line_gap=5)

        canvas.rect(408, 292, 612, 385, "#FFFDF8", stroke="#E4D8C8", stroke_width=1, radius=32)
        draw_section_label(canvas, 438, 322, "mapa comparativo", PALETTE["purple"])
        center_x, center_y = 714, 486
        canvas.circle(center_x, center_y, 74, "#0F172A")
        canvas.text(center_x, text_y(canvas, center_y - 6, -18), "COMPARE", "#FFFDF8", size=16, anchor="center", weight="700")
        canvas.text(center_x, text_y(canvas, center_y + 20, 4), "funcoes", "#D9E2EC", size=11, anchor="center")
        radius_x, radius_y = 210, 125
        for index, card in enumerate(cards):
            angle = -math.pi / 2 + math.tau * index / max(1, len(cards))
            x = center_x + math.cos(angle) * radius_x
            y = center_y + math.sin(angle) * radius_y
            color = card.get("color", PALETTE["blue"])
            canvas.line(center_x, center_y, x, y, "#D9E2EC", width=2)
            canvas.circle(x, y, 49, "#FFFDF8", stroke=color, stroke_width=4)
            draw_simple_icon(canvas, x, y, card["title"], color)
            if y < center_y - 20:
                label_x, label_y = x - 74, max(314, y - 58)
                max_chars = 17
                show_pills = False
            elif y > center_y + 20:
                label_x, label_y = x - 74, min(648, y + 58)
                max_chars = 17
                show_pills = False
            elif x < center_x:
                label_x, label_y = max(330, x - 170), y - 10
                max_chars = 18
                show_pills = True
            else:
                label_x, label_y = min(970, x + 64), y - 10
                max_chars = 18
                show_pills = True
            canvas.text_block(label_x, label_y, card["title"], color, size=14, max_chars=max_chars, line_gap=4, weight="700")
            if show_pills:
                for item_index, item in enumerate(card.get("items", [])[:2]):
                    draw_pill(canvas, label_x, label_y + 26 + item_index * 30, item, color, width=86)

        canvas.rect(1052, 292, 278, 385, "#FFFDF8", stroke="#E4D8C8", stroke_width=1, radius=28)
        draw_section_label(canvas, 1080, 322, "na pratica", PALETTE["green"])
        y = 382
        for index, note in enumerate(spec.get("notes", [])[:4]):
            color = cards[index % len(cards)].get("color", PALETTE["green"])
            canvas.circle(1090, y + 8, 12, color)
            canvas.text(1090, text_y(canvas, y + 13, -5), str(index + 1), "#FFFDF8", size=10, anchor="center", weight="700")
            canvas.text_block(1116, y + 11, note, PALETTE["muted"], size=12, max_chars=28, line_gap=5)
            y += 70

        draw_note_strip(
            canvas,
            70,
            708,
            1260,
            114,
            "leitura rapida da cartilha",
            [card["detail"] for card in cards[:4]],
            PALETTE["orange"],
            columns=min(4, len(cards)),
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
        canvas.rect(70, 188, 1260, 74, "#FFF0F0", stroke="#E9A2A2", stroke_width=2, radius=24)
        canvas.text_block(700, 218, spec["hero_label"], PALETTE["ink"], size=18, max_chars=68, anchor="center", weight="700")
        canvas.rect(70, 292, 1260, 86, "#FFFDF8", stroke="#E4D8C8", stroke_width=1, radius=26)
        canvas.text(100, 330, "RACIOCINIO DE DIAGNOSTICO", PALETTE["ink"], size=16, weight="700")
        canvas.text_block(100, 356, spec["didactic_goal"], PALETTE["muted"], size=12, max_chars=126, line_gap=5)
        draw_arrow(canvas, 100, 428, 1280, 428, "#E9A2A2", width=4)

        zone_fills = ("#FFF7F7", "#FFF7E8", "#F1FFF6")
        for column_index, column in enumerate(columns):
            x = start_x + column_index * (column_width + gap)
            color = column.get("color", PALETTE["red"])
            skew = 22
            canvas.polygon(
                (
                    (x + skew, 466),
                    (x + column_width, 466),
                    (x + column_width - skew, 682),
                    (x, 682),
                ),
                zone_fills[column_index % len(zone_fills)],
                stroke="#E4D8C8",
                stroke_width=1,
            )
            canvas.circle(x + 52, 492, 34, color)
            canvas.text(x + 52, text_y(canvas, 500, -10), str(column_index + 1), "#FFFDF8", size=19, anchor="center", weight="700")
            canvas.text_block(x + 102, 492, column["title"], PALETTE["ink"], size=19, max_chars=24, line_gap=5, weight="700")
            draw_simple_icon(canvas, x + column_width - 52, 504, column["title"], color)
            y = 554
            for item in column["items"][:4]:
                canvas.circle(x + 42, y + 4, 9, color)
                canvas.text_block(x + 62, y + 8, item, PALETTE["text"], size=13, max_chars=39, line_gap=5)
                y += 42
            if column_index < len(columns) - 1:
                draw_arrow(canvas, x + column_width + 10, 572, x + column_width + gap - 12, 572, PALETTE["muted"], width=2)
        draw_note_strip(
            canvas,
            70,
            720,
            1260,
            102,
            "evidencia antes de conclusao",
            spec.get("notes", []) or [spec.get("caution", "")],
            PALETTE["red"],
            columns=3,
        )
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
