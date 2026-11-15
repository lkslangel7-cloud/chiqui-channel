import re, html, sys, json
src = open(sys.argv[1], encoding="utf-8").read()
out = sys.argv[2]
video_only = len(sys.argv) > 3 and sys.argv[3] == "--video"
blocks = re.split(r"\n### ", src)[1:]
scenes = []
for b in blocks:
    head = b.split("\n", 1)[0].strip()
    m = re.match(r"(S\d+)\s+(.*?)\s*\((.*?)\)", head)
    sid, name, t = m.group(1), m.group(2), m.group(3)
    ref = re.search(r"\[레퍼런스\]\s*(.*)", b).group(1).strip()
    codes = re.findall(r"```\n(.*?)\n```", b, re.S)
    vlen = re.search(r"\[영상\]\s*(.*)", b).group(1).strip()
    scenes.append(dict(id=sid, name=name, time=t, ref=ref, img=codes[0].strip(), vid=codes[1].strip(), vlen=vlen))
style_line = "Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text."
egg = "round cream-colored dinosaur eggs with soft pastel polka dots"
baby = "five tiny round chubby baby dinosaurs, each a different pastel color (pink, mint, lilac, peach, sky blue), with tiny horn nubs and big sparkling eyes"

IMAGE_STEPS = '    <ol class="steps">\n      <li>Image에서 Unlimited 표시가 있는 모델을 고르고, 비율은 16:9.</li>\n      <li>캐릭터 시트 5장을 레퍼런스로 <b>한 번만</b> 넣고, 장면이 바뀌어도 그대로 둔다. S17~S19만 S16 그림을 하나 더 넣는다.</li>\n      <li>그림 프롬프트 붙여 넣기 → 시트와 모습이 같은 그림만 고르기.</li>\n      <li>고른 그림을 Video의 시작 이미지로 넣고 영상 프롬프트 붙여 넣기. 소리는 끈다.</li>\n      <li>10초 장면은 10초로 만들거나, 5초 영상 2개를 이어 붙인다.</li>\n      <li>파일 이름은 ep01_s01.png, ep01_c01.mp4처럼 장면 번호와 같게.</li>\n    </ol>'
VIDEO_STEPS = '    <ol class="steps">\n      <li>Video 메뉴에서 Unlimited 표시가 있는 영상 모델(예: Kling 3.0)을 고른다.</li>\n      <li>시작 이미지(Start image)에 그 장면 그림을 넣는다.</li>\n      <li>아래 영상 프롬프트를 복사해 붙여 넣는다. 소리(Sound/Audio)는 끈다.</li>\n      <li>길이가 10초인 장면은 10초로 만들거나, 5초 영상 2개를 만들어 이어 붙인다.</li>\n      <li>캐릭터 모습이 녹아내리거나 바뀌면 다시 만든다.</li>\n      <li>파일 이름은 ep01_c01.mp4처럼 장면 번호와 같게.</li>\n    </ol>'

def card(s):
    e = html.escape
    return f'''
<article class="scene" id="{s['id'].lower()}">
  <header class="scene-head">
    <span class="sid">{e(s['id'])}</span>
    <h2>{e(s['name'])}</h2>
    <span class="time">{e(s['time'])}</span>
  </header>
  <p class="ref"><span class="label">{"시작 이미지" if video_only else "레퍼런스"}</span> {e(("ep01_" + s['id'].lower() + ".png (이 장면 그림)") if video_only else s['ref'])}</p>
{"" if video_only else f"""  <div class="prompt">
    <div class="prompt-head"><span class="kind">그림 · 16:9</span><button type="button" class="copy" data-target="{s['id']}-img">복사</button></div>
    <pre id="{s['id']}-img">{e(s['img'])}</pre>
  </div>
"""}  <div class="prompt">
    <div class="prompt-head"><span class="kind">영상 · {e(s['vlen'])} · 소리 끔</span><button type="button" class="copy" data-target="{s['id']}-vid">복사</button></div>
    <pre id="{s['id']}-vid">{e(s['vid'])}</pre>
  </div>
</article>'''

nav = "".join(f'<a href="#{s["id"].lower()}">{s["id"][1:]}</a>' for s in scenes)
cards = "".join(card(s) for s in scenes)
FIXED = f'''    <div class="prompt">
      <div class="prompt-head"><span class="kind">고정 문구 · 알</span><button type="button" class="copy" data-target="fx-egg">복사</button></div>
      <pre id="fx-egg">{html.escape(egg)}</pre>
    </div>
    <div class="prompt">
      <div class="prompt-head"><span class="kind">고정 문구 · 아기 공룡 (S16 그림을 S17~S19 레퍼런스로)</span><button type="button" class="copy" data-target="fx-baby">복사</button></div>
      <pre id="fx-baby">{html.escape(baby)}</pre>
    </div>
    <div class="prompt">
      <div class="prompt-head"><span class="kind">고정 문구 · 화풍 (모든 그림 끝에 이미 들어 있음)</span><button type="button" class="copy" data-target="fx-style">복사</button></div>
      <pre id="fx-style">{html.escape(style_line)}</pre>
    </div>
'''
TITLE = '공룡알 하나 둘 셋 영상' if video_only else '공룡알 하나 둘 셋 프롬프트'
STEPS = VIDEO_STEPS if video_only else IMAGE_STEPS
H1 = '1화 · 영상 프롬프트' if video_only else '1화 · 공룡알 하나 둘 셋'
page = f'''<title>{TITLE}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;600&family=IBM+Plex+Mono:wght@400&display=swap">
<style>
/* Layout: 한 열 작업 목록. 위에 고정 문구, 장면 번호 바로가기, 장면마다 그림·영상 프롬프트 카드 */
:root {{
  --bg: #fbf7f0; --surface: #ffffff; --ink: #2b2620; --muted: #76695a;
  --line: #eadfce; --accent: #e8711c; --accent-ink: #ffffff; --code: #f6efe3;
  --display: "Jua", "Noto Sans KR", system-ui, sans-serif;
  --body: "Noto Sans KR", system-ui, -apple-system, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #1d1a16; --surface: #27231e; --ink: #f2ebe0; --muted: #b3a593;
  --line: #3a342c; --accent: #f08a3c; --accent-ink: #1d1a16; --code: #2f2a24; color-scheme: dark; }} }}
:root[data-theme="dark"] {{
  --bg: #1d1a16; --surface: #27231e; --ink: #f2ebe0; --muted: #b3a593;
  --line: #3a342c; --accent: #f08a3c; --accent-ink: #1d1a16; --code: #2f2a24; color-scheme: dark; }}
body {{ background: var(--bg); color: var(--ink); font-family: var(--body); line-height: 1.6; }}
.wrap {{ max-width: 760px; margin: 0 auto; padding-block: 28px 64px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px));
  display: grid; gap: 20px; }}
h1 {{ font-family: var(--display); font-weight: 400; font-size: 2rem; margin: 0; text-wrap: balance; }}
.lead {{ margin: 0; color: var(--muted); }}
.steps {{ margin: 0; padding-left: 1.2em; display: grid; gap: 4px; }}
.fixed {{ background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 16px; display: grid; gap: 14px; }}
.fixed h2, .scene h2 {{ font-family: var(--display); font-weight: 400; margin: 0; font-size: 1.25rem; }}
nav.jump {{ display: flex; flex-wrap: wrap; gap: 6px; position: sticky; top: env(safe-area-inset-top, 0px); background: var(--bg); padding-block: 8px; z-index: 5; }}
body::before {{ content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--bg); }}
nav.jump a {{ min-width: 2.4em; text-align: center; padding: 4px 8px; border: 1px solid var(--line); border-radius: 999px; color: var(--ink); text-decoration: none; font-variant-numeric: tabular-nums; font-size: .9rem; }}
nav.jump a:hover, nav.jump a:focus-visible {{ border-color: var(--accent); outline: none; }}
.scene {{ display: grid; gap: 10px; padding-block: 16px; border-top: 1px solid var(--line); scroll-margin-top: 56px; }}
.scene-head {{ display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px 12px; }}
.sid {{ font-family: var(--mono); color: var(--accent); font-size: .95rem; }}
.time {{ margin-left: auto; color: var(--muted); font-size: .9rem; font-variant-numeric: tabular-nums; }}
.ref {{ margin: 0; font-size: .95rem; }}
.label, .kind {{ font-size: .78rem; letter-spacing: .04em; color: var(--muted); margin-right: 6px; }}
.prompt {{ background: var(--surface); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; min-width: 0; }}
.prompt-head {{ display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 8px 10px 8px 12px; border-bottom: 1px solid var(--line); }}
pre {{ margin: 0; padding: 12px; white-space: pre-wrap; word-break: break-word; font-family: var(--mono); font-size: .82rem; line-height: 1.55; background: var(--code); color: var(--ink); }}
button.copy {{ font: inherit; font-size: .85rem; font-weight: 600; padding: 6px 14px; border-radius: 999px; border: 1px solid var(--accent); background: var(--accent); color: var(--accent-ink); cursor: pointer; }}
button.copy:focus-visible {{ outline: 2px solid var(--ink); outline-offset: 2px; }}
button.copy.done {{ background: transparent; color: var(--accent); }}
@media (prefers-reduced-motion: no-preference) {{ html {{ scroll-behavior: smooth; }} }}
</style>
<div class="wrap">
  <header style="display:grid;gap:8px">
    <h1>{H1}</h1>
    <p class="lead">장면마다 <b>복사</b>를 눌러 Higgsfield에 그대로 붙여 넣으세요. 장면 {len(scenes)}개, 약 3분.</p>
  </header>
  <section class="fixed">
    <h2>쓰는 순서</h2>
{STEPS}
{"" if video_only else FIXED}  </section>
  <nav class="jump" aria-label="장면 바로가기">{nav}</nav>
  {cards}
</div>
<script>
document.addEventListener('click', function (ev) {{
  var btn = ev.target.closest('button.copy');
  if (!btn) return;
  var el = document.getElementById(btn.dataset.target);
  var text = el.textContent;
  function done() {{ btn.textContent = '복사됨'; btn.classList.add('done');
    setTimeout(function () {{ btn.textContent = '복사'; btn.classList.remove('done'); }}, 1600); }}
  function fallback() {{ var r = document.createRange(); r.selectNodeContents(el);
    var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); btn.textContent = '선택됨 · 길게 눌러 복사'; }}
  try {{ navigator.clipboard.writeText(text).then(done, fallback); }} catch (e) {{ fallback(); }}
}});
</script>
'''
open(out, "w", encoding="utf-8").write(page)
print(len(scenes), "scenes")
