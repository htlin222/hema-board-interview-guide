#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow>=10.0"]
# ///
"""產生站台的品牌圖檔：favicon 與 OG image。

標誌設計：血滴輪廓（血液科）內含羅盤指針（推理架構）——正好對應站台的兩個核心，
也跟每個主題頁「🧭 推理架構」段落用的 compass 圖示同源。

配色取自 Catppuccin（站台主題）：Mocha base #1e1e2e、Mauve #cba6f7。

用法：
    python3 scripts/make-brand-assets.py     # → public/og.png、public/favicon.svg 等
"""

from __future__ import annotations

import math
import pathlib

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"

# Catppuccin Mocha
BASE = (30, 30, 46)
MANTLE = (24, 24, 37)
MAUVE = (203, 166, 247)
TEXT = (205, 214, 244)
SUBTEXT = (166, 173, 200)
OVERLAY = (127, 132, 156)

FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size)


def droplet(draw: ImageDraw.ImageDraw, cx: float, cy: float, r: float, color) -> None:
    """血滴：用水滴參數曲線畫，避免「圓形+三角形」拼接處的折角。

    曲線 (cos t, sin t · sinᵐ(t/2)) 的尖端在 t=0、圓肚在 t=π，
    旋轉 -90° 讓尖端朝上。cy 為圓肚中心，r 對應圓肚半徑。
    """
    m, n = 1.35, 240
    raw = []
    for i in range(n):
        t = 2 * math.pi * i / n
        raw.append((math.sin(t) * (math.sin(t / 2) ** m), -math.cos(t)))

    # 以「最寬處」定義圓肚中心，並把半寬正規化成 r，
    # 這樣呼叫端傳進來的 (cx, cy, r) 就等同一個圓肚：指針放 (cx, cy) 必定置中。
    half_w = max(abs(x) for x, _ in raw)
    y_belly = next(y for x, y in raw if abs(abs(x) - half_w) < 1e-9)
    k = r / half_w

    pts = [(cx + x * k, cy + (y - y_belly) * k) for x, y in raw]
    draw.polygon(pts, fill=color)


def needle(draw: ImageDraw.ImageDraw, cx: float, cy: float, r: float, color) -> None:
    """羅盤指針：NE–SW 走向的細長菱形。"""
    d = math.sqrt(0.5)
    tip, waist = r, r * 0.30
    draw.polygon(
        [
            (cx + tip * d, cy - tip * d),   # NE 尖端
            (cx + waist * d, cy + waist * d),
            (cx - tip * d, cy + tip * d),   # SW 尖端
            (cx - waist * d, cy - waist * d),
        ],
        fill=color,
    )


def make_favicon_svg() -> str:
    """SVG favicon：向量、任何尺寸都清晰，深淺色瀏覽器介面都看得見。"""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        # 血滴（實心，自帶底色所以深淺背景都成立）
        '<path d="M32 4c0 0 19 21.5 19 34.5a19 19 0 0 1-38 0C13 25.5 32 4 32 4Z" fill="#8839ef"/>'
        # 羅盤指針（挖空成白色）
        '<path transform="translate(5.6 15.6) scale(2.2)" fill="#fff" '
        'd="m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411'
        'a2 2 0 0 1 1.265-1.265z"/>'
        "</svg>\n"
    )


def make_icon_png(size: int) -> Image.Image:
    """點陣圖示（apple-touch-icon 等用途），畫在圓角深色底上。"""
    ss = 4  # 超取樣，邊緣才不會鋸齒
    img = Image.new("RGBA", (size * ss, size * ss), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    s = size * ss
    d.rounded_rectangle([0, 0, s, s], radius=s * 0.22, fill=BASE)
    cx, cy, r = s / 2, s * 0.58, s * 0.30
    droplet(d, cx, cy, r, MAUVE)
    needle(d, cx, cy, r * 0.78, BASE)
    return img.resize((size, size), Image.LANCZOS)


def make_og() -> Image.Image:
    """OG image。整張以 2 倍尺寸繪製再縮小，讓形狀邊緣也有抗鋸齒。"""
    S = 2
    W, H = 1200 * S, 630 * S
    img = Image.new("RGB", (W, H), BASE)

    # 右下角淡淡的大血滴，當背景紋理（先畫，才會被文字蓋在上面）
    ghost = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    droplet(ImageDraw.Draw(ghost), W - 155 * S, H - 118 * S, 118 * S, (*MAUVE, 18))
    img = Image.alpha_composite(img.convert("RGBA"), ghost).convert("RGB")
    d = ImageDraw.Draw(img)

    # 左側強調色帶
    d.rectangle([0, 0, 14 * S, H], fill=MAUVE)

    # 標誌
    mx, my, mr = 132 * S, 196 * S, 48 * S
    droplet(d, mx, my, mr, MAUVE)
    needle(d, mx, my, mr * 0.78, BASE)

    # 標題
    d.text((216 * S, 138 * S), "血液科", font=font(76 * S), fill=TEXT)
    d.text((216 * S, 226 * S), "口試走向指南", font=font(76 * S), fill=TEXT)

    # 分隔線
    d.rectangle([80 * S, 360 * S, W - 80 * S, 362 * S], fill=(49, 50, 68))

    # 副標：站台的四層結構
    d.text((80 * S, 400 * S), "推理架構 × 破題關鍵句 × 擬答 × 追問", font=font(40 * S), fill=MAUVE)

    # 說明
    d.text(
        (80 * S, 470 * S),
        "整理歷屆考生口試心得，去名化後只保留考試走向本身",
        font=font(30 * S),
        fill=SUBTEXT,
    )

    # 頁尾網址
    d.text(
        (80 * S, 540 * S),
        "htlin222.github.io/hema-board-interview-guide",
        font=font(26 * S),
        fill=OVERLAY,
    )

    return img.resize((1200, 630), Image.LANCZOS)


def main() -> None:
    PUBLIC.mkdir(exist_ok=True)

    (PUBLIC / "favicon.svg").write_text(make_favicon_svg(), encoding="utf-8")
    print("wrote public/favicon.svg")

    for size, name in [(180, "apple-touch-icon.png"), (32, "favicon-32.png")]:
        make_icon_png(size).save(PUBLIC / name)
        print(f"wrote public/{name}  ({size}x{size})")

    og = make_og()
    og.save(PUBLIC / "og.png")
    print(f"wrote public/og.png  ({og.width}x{og.height})")


if __name__ == "__main__":
    main()
