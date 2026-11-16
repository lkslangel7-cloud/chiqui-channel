"""채널 배너(2560x1440) 합성: 빈 배경 + 오려 낸 다섯 친구 + 채널 이름.
사용법: python3 -I scripts/make_banner.py
모든 중요한 것은 휴대폰에서도 보이는 가운데 1546x423 안에 둔다.
"""
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from pathlib import Path

R = Path(__file__).resolve().parent.parent
B = R / "branding"
W, H = 2560, 1440
SAFE = (507, 508, 2053, 931)
FONT = str(R / "remotion/public/fonts/Jua.ttf")

# 배경을 1.2배로 키우고 위로 올려 수평선을 위쪽에 둔다 (친구들이 풀밭 위에 서도록)
bg = Image.open(B / "banner_bg.png").convert("RGBA").resize((round(W * 1.2), round(H * 1.2)), Image.LANCZOS)
bg = bg.crop((round(W * 0.1), 276, round(W * 0.1) + W, 276 + H))
cut = Image.open(B / "banner_chars_cutout.png").convert("RGBA")
cut = cut.crop(cut.split()[-1].getbbox())
s = 400 / cut.height
cut = cut.resize((round(cut.width * s), 400), Image.LANCZOS)
cx, cy = SAFE[2] - 18 - cut.width, SAFE[1] + 8

# 발밑 그림자
sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(sh)
d.ellipse((cx + 10, cy + cut.height - 34, cx + cut.width - 10, cy + cut.height + 14), fill=(40, 80, 20, 70))
bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
bg.alpha_composite(cut, (cx, cy))

# 채널 이름
def text(img, xy, t, size, fill, stroke, sw):
    f = ImageFont.truetype(FONT, size)
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(glow).text((xy[0] + 6, xy[1] + 10), t, font=f, fill=(60, 40, 20, 90), stroke_width=sw, stroke_fill=(60, 40, 20, 90))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(8)))
    ImageDraw.Draw(img).text(xy, t, font=f, fill=fill, stroke_width=sw, stroke_fill=stroke)
    return ImageDraw.Draw(img).textbbox(xy, t, font=f, stroke_width=sw)

left = SAFE[0] + 40
area_w = cx - left - 40
size = 170
while ImageFont.truetype(FONT, size).getlength("치키 타운") + 28 > area_w:
    size -= 4
f1 = ImageFont.truetype(FONT, size)
f2 = ImageFont.truetype(FONT, int(size * 0.5))
h1 = f1.getbbox("치키 타운")[3]; h2 = f2.getbbox("Chiqui Town")[3]
top = (SAFE[1] + SAFE[3]) // 2 - (h1 + 24 + h2) // 2
w1 = f1.getlength("치키 타운"); w2 = f2.getlength("Chiqui Town")
x1 = left + (area_w - w1) / 2
text(bg, (x1, top), "치키 타운", size, (255, 138, 36), (255, 255, 255), 14)
text(bg, (left + (area_w - w2) / 2, top + h1 + 24), "Chiqui Town", int(size * 0.5), (255, 255, 255), (74, 140, 210), 9)

out = bg.convert("RGB")
out.save(B / "banner_2560x1440.png", optimize=True)

# 확인용: 휴대폰(가운데)·PC(가로 띠) 표시 영역
p = bg.copy()
d = ImageDraw.Draw(p)
d.rectangle((0, SAFE[1], W - 1, SAFE[3]), outline=(255, 255, 255, 255), width=6)
d.rectangle(SAFE, outline=(255, 40, 40, 255), width=8)
p.convert("RGB").resize((1280, 720)).save(B / "banner_safe_area_check.png")
out.crop(SAFE).save(B / "banner_mobile_view.png")
print("ok", size, cut.size, (cx, cy))
