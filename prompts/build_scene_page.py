"""장면 프롬프트 복사 페이지 (Higgsfield 웹사이트에서 따라 하기용).
사용법: python3 -I prompts/build_scene_page.py episodes/ep02 "2화 · 알록달록 풍선 어디 있니?"
episodes/epXX/scenes.json을 읽어 scene_prompts_page.html과 prompts.md를 만든다.
시트 그림은 페이지 옆 sheets/ 폴더로 함께 게시한다 (Artifact files).
"""
import html, json, re, sys
from pathlib import Path

ep = Path(sys.argv[1]); title = sys.argv[2]
scenes = json.loads((ep / "scenes.json").read_text(encoding="utf-8"))
e = html.escape
CH = {"C": ("치키", "chiqui", "#f08a2c"), "R": ("로로", "roro", "#f2c230"), "T": ("토롱", "torong", "#5fb35a"),
      "P": ("피오", "pio", "#5aa7e6"), "B": ("바우 할아버지", "bau", "#9a7ad1")}

def chips(refs):
    village = '<span class="chip">🏝 마을 그림</span>'
    if not refs:
        return village + '<span class="none">+ 시트는 넣지 않기 (캐릭터가 안 나와요)</span>'
    return village + "".join(f'<span class="chip"><i style="background:{CH[r][2]}"></i>{CH[r][0]}</span>' for r in refs)

def box(kind, bid, text):
    return (f'<div class="prompt"><div class="prompt-head"><span class="kind">{e(kind)}</span>'
            f'<button type="button" class="copy" data-target="{bid}">복사</button></div><pre id="{bid}">{e(text)}</pre></div>')

cards = []
for i, s in enumerate(scenes, 1):
    cards.append(f'''<article class="scene" id="{s['id'].lower()}">
  <header class="scene-head"><span class="sid">{i}/{len(scenes)} · {e(s['id'])}</span><h2>{e(s['name'])}</h2><span class="time">{e(s['time'])}</span></header>
  <div class="step"><b>① 넣을 시트</b> <span class="chips">{chips(s['refs'])}</span></div>
  <div class="step"><b>② 그림 만들기</b> · 16:9</div>
  {box("그림 프롬프트", s['id'] + "-i", s['img'])}
  <div class="step"><b>③ 영상 만들기</b> · 방금 그림을 시작 이미지로 · <b class="sec">{s['sec']}초</b> · 소리 끔</div>
  {box("영상 프롬프트", s['id'] + "-v", s['vid'])}
</article>''')

sheets = "".join(f'<a class="sheet" href="sheets/{CH[k][1]}_sheet.png" target="_blank" rel="noopener"><img src="sheets/{CH[k][1]}_sheet.png" alt="{CH[k][0]} 시트" loading="lazy"><span><i style="background:{CH[k][2]}"></i>{CH[k][0]}</span></a>' for k in "CRTPB")
nav = "".join(f'<a href="#{s["id"].lower()}">{e(s["id"][1:])}</a>' for s in scenes)
src = (Path(__file__).parent / "build_prompt_page.py").read_text(encoding="utf-8")
css = re.search(r"<style>\n(.*?)</style>", src, re.S).group(1).replace("{{", "{").replace("}}", "}")
js = re.search(r"<script>\n(.*?)</script>", src, re.S).group(1).replace("{{", "{").replace("}}", "}")
css += """h1 { word-break: keep-all; }
nav.jump { flex-wrap: nowrap; overflow-x: auto; scrollbar-width: none; }
nav.jump a { flex: none; }
.big { margin: 0; padding-left: 1.3em; display: grid; gap: 10px; font-size: 1.02rem; }
.big li::marker { font-family: var(--display); color: var(--accent); }
.warn { margin: 0; padding: 10px 12px; border-radius: 10px; background: var(--code); border: 1px solid var(--line); }
.step { font-size: .95rem; }
.sec { color: var(--accent); }
.chips { display: inline-flex; flex-wrap: wrap; gap: 6px; vertical-align: middle; }
.chip { display: inline-flex; align-items: center; gap: 6px; padding: 2px 10px; border-radius: 999px; border: 1px solid var(--line); background: var(--surface); font-size: .9rem; }
.chip i, .sheet i { width: .7em; height: .7em; border-radius: 50%; display: inline-block; }
.none { color: var(--muted); font-size: .9rem; }
.sheets { display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 10px; }
.sheet { display: grid; gap: 4px; text-decoration: none; color: var(--ink); font-size: .9rem; }
.sheet img { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; border-radius: 8px; border: 1px solid var(--line); background: var(--code); }
.sheet span { display: inline-flex; align-items: center; gap: 6px; }
"""
page = f'''<title>{e(title)} 장면</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;600&family=IBM+Plex+Mono:wght@400&display=swap">
<style>
{css}</style>
<div class="wrap">
  <header style="display:grid;gap:8px">
    <h1>{e(title)}</h1>
    <p class="lead">Higgsfield 웹사이트에서 장면 {len(scenes)}개를 하나씩 만들어요. 장면마다 ①→②→③ 순서만 지키면 돼요.</p>\n    <p class="warn">🧪 <b>먼저 S02, S03 두 장면만</b> 그림과 영상까지 만들고 "두 개 만들었어"라고 알려 주세요. 1화와 그림체가 같은지 제가 확인한 뒤에 나머지를 만들어요.</p>
  </header>
  <section class="fixed">
    <h2>준비: 캐릭터 시트 저장하기</h2>
    <p class="lead">시트 파일은 채팅으로 따로 보내 드렸어요. Higgsfield에서 레퍼런스를 넣을 때 <b>내 생성 기록(History)</b>에서 골라도 돼요. 아래 그림으로 어떤 시트인지 확인하세요.</p>
    <div class="sheets">{sheets}<a class="sheet" href="sheets/style_village.png" target="_blank" rel="noopener"><img src="sheets/style_village.png" alt="마을 그림" loading="lazy"><span>🏝 마을 그림 (화풍 기준)</span></a></div>
  </section>
  <section class="fixed">
    <h2>② 그림 만드는 법</h2>
    <ol class="big">
      <li>Higgsfield에서 <b>Image</b>를 누르고, 모델은 <b>GPT Image 2.6 Sunburst</b>(무제한)를 골라요.</li>
      <li>크기(비율)는 <b>16:9</b>로 해요.</li>
      <li><b>🏝 마을 그림</b>은 장면마다 항상 넣어요 (1화와 그림체를 맞추는 기준이에요). 그리고 그 장면의 <b>① 넣을 시트</b>에 적힌 친구 시트만 올려요. <b>적혀 있지 않은 친구 시트는 빼요!</b> (같이 넣으면 친구가 두 번 나와요)</li>
      <li>그림 프롬프트 옆 <b>복사</b>를 누르고 붙여 넣은 다음 <b>Generate</b>를 눌러요.</li>
      <li>그림을 확인해요. 친구 모습이 시트와 같고, 똑같은 친구가 두 번 나오지 않고, 풍선 개수와 색이 맞으면 성공이에요. 이상하면 한 번 더 만들어요.</li>
    </ol>
  </section>
  <section class="fixed">
    <h2>③ 영상 만드는 법</h2>
    <ol class="big">
      <li><b>Video</b>를 누르고, 모델은 <b>Seedance 2.5</b>(무제한)를 골라요.</li>
      <li><b>Unlimited(무제한)</b> 스위치를 켜요.</li>
      <li>방금 만든 그림을 <b>시작 이미지(Start frame / 첫 프레임)</b>에 넣어요. <b>캐릭터 시트는 넣지 않아요!</b> 그림 한 장만 넣어요.</li>
      <li>영상 프롬프트를 복사해서 붙여 넣고, 길이(<b>5초</b> 또는 <b>10초</b>)를 장면에 적힌 대로 맞춰요. 소리(Audio) 스위치가 있으면 <b>꺼요.</b> 화질은 <b>1080p</b>.</li>
      <li><b>Generate</b> 버튼을 눌러요.</li>
    </ol>
    <p class="warn">⚠️ Generate 버튼에 <b>크레딧 숫자</b>가 보이면 누르지 말고 멈춰요. 무제한이 안 켜진 거예요. 스위치를 다시 확인하거나 저한테 알려 주세요.</p>
  </section>
  <section class="fixed">
    <h2>다 만들면</h2>
    <p class="lead">파일 이름을 바꾸거나 올릴 필요 없어요. 여기 채팅에 <b>"다 만들었어"</b>라고만 말해 주세요. 같은 계정이라 제가 가져와서 확인하고 노래·대사를 붙여 완성할게요. 오프닝(0:00–0:20)과 치키 달리기(0:55–1:00)는 1화 영상을 다시 써서 안 만들어도 돼요.</p>
  </section>
  <nav class="jump" aria-label="장면 바로가기">{nav}</nav>
  {"".join(cards)}
</div>
<script>
{js}</script>
'''
(ep / "scene_prompts_page.html").write_text(page, encoding="utf-8")
md = [f"# {title} — 장면 프롬프트 (웹사이트용)", "", "그림: GPT Image 2.6 Sunburst(웹 무제한), 16:9, 적힌 시트만 레퍼런스. 영상: Seedance 2.5(웹 무제한), 그림 한 장만 시작 프레임으로, 끊김 없는 한 컷, 소리 끔.", ""]
for s in scenes:
    refs = ", ".join(CH[r][0] for r in s["refs"]) or "없음"
    md += [f"### {s['id']} {s['name']} ({s['time']})", f"[레퍼런스] {refs}", "[그림]", "```", s["img"], "```", f"[영상] {s['sec']}초", "```", s["vid"], "```", ""]
(ep / "prompts.md").write_text("\n".join(md), encoding="utf-8")
print("ok", len(scenes))
