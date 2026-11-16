"""에피소드 썸네일(1280x720): 장면 그림 + 아래쪽 큰 글자.
사용법: python3 -I scripts/make_thumbnail.py <배경 png> <출력 png> "<글자>"
글자를 비우면("") 숫자 공 1~5만 넣은 언어 없는 썸네일을 만든다.
"""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from pathlib import Path

R = Path(__file__).resolve().parent.parent
F = str(R / "remotion/public/fonts/Jua.ttf")
src, out, text = sys.argv[1], sys.argv[2], sys.argv[3]
im = Image.open(src).convert("RGBA").resize((1280, 720), Image.LANCZOS)
g = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(g)
for y in range(470, 720):
    d.line((0, y, 1280, y), fill=(70, 40, 10, int(150 * (y - 470) / 250)))
im.alpha_composite(g)

def draw(t, size, xy, fill, stroke, sw):
    f = ImageFont.truetype(F, size)
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((xy[0] + 5, xy[1] + 8), t, font=f, fill=(50, 30, 10, 160), stroke_width=sw, stroke_fill=(50, 30, 10, 160))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)))
    ImageDraw.Draw(im).text(xy, t, font=f, fill=fill, stroke_width=sw, stroke_fill=stroke)

if text:
    size = 124
    while ImageFont.truetype(F, size).getlength(text) > 1000:
        size -= 4
    w = ImageFont.truetype(F, size).getlength(text)
    draw(text, size, ((1280 - w) / 2 - 40, 560 + (124 - size) // 2), (255, 138, 36), (255, 255, 255), 12)
else:  # 숫자 공 1~5 (알 색)
    cols = [(255, 170, 190), (140, 215, 175), (255, 205, 90), (175, 160, 235), (120, 190, 245)]
    r, gap = 62, 28
    x0 = (1280 - (5 * 2 * r + 4 * gap)) / 2 - 40
    for i, c in enumerate(cols):
        cx, cy = x0 + r + i * (2 * r + gap), 625
        sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).ellipse((cx - r + 4, cy - r + 8, cx + r + 4, cy + r + 8), fill=(50, 30, 10, 140))
        im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)))
        ImageDraw.Draw(im).ellipse((cx - r, cy - r, cx + r, cy + r), fill=c + (255,), outline=(255, 255, 255, 255), width=8)
        f = ImageFont.truetype(F, 92); n = str(i + 1)
        ImageDraw.Draw(im).text((cx, cy + 4), n, font=f, anchor="mm", fill=(255, 255, 255), stroke_width=6, stroke_fill=(90, 60, 30))
im.convert("RGB").save(out)
print("ok", out)
