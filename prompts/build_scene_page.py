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
    village = '<span class="chip">🏝 @village</span>'
    if not refs:
        return village + '<span class="none">(친구는 안 나와요)</span>'
    return village + "".join(f'<span class="chip"><i style="background:{CH[r][2]}"></i>@{CH[r][1]} {CH[r][0]}</span>' for r in refs)

def box(kind, bid, text):
    return (f'<div class="prompt"><div class="prompt-head"><span class="kind">{e(kind)}</span>'
            f'<button type="button" class="copy" data-target="{bid}">복사</button></div><pre id="{bid}">{e(text)}</pre></div>')

import base64, glob, io
COMMON = json.loads((ep.parent / "common/common.json").read_text(encoding="utf-8")) if (ep.parent / "common/common.json").exists() else {}
def thumb(sid, cid=None):  # 합격 그림이 있으면 작은 사진으로 넣는다 (어떤 그림으로 몇 번 영상을 만드는지)
    fs = sorted(glob.glob(str(ep.parent / "common/images/web" / f"{cid}_*.png"))) if cid else []
    if cid and fs:
        from PIL import Image
        im = Image.open(fs[-1]).convert("RGB"); im.thumbnail((640, 360)); buf = io.BytesIO(); im.save(buf, "JPEG", quality=72)
        return (f'<figure class="ok"><img src="data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}" alt="{e(sid)} 공통 그림">'
                f'<figcaption>🔁 공통 그림 ({e(COMMON.get(cid, {}).get("from", ""))}) — 모든 화가 같이 써요</figcaption></figure>')
    fs = sorted(glob.glob(str(ep / "images/web" / f"{sid}_*.png")))
    if not fs: return ""
    from PIL import Image
    f = fs[-1]; code = Path(f).stem[len(sid) + 1:]
    im = Image.open(f).convert("RGB"); im.thumbnail((640, 360)); buf = io.BytesIO(); im.save(buf, "JPEG", quality=72)
    return (f'<figure class="ok"><img src="data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}" alt="{e(sid)} 합격 그림">'
            f'<figcaption>✅ 합격 그림 <code>{e(code)}</code> — 이 그림을 시작 이미지로</figcaption></figure>')

def common_note(s):
    cid = s.get("common")
    if not cid: return ""
    has_img = bool(glob.glob(str(ep.parent / "common/images/web" / f"{cid}_*.png")))
    has_vid = bool(glob.glob(str(ep.parent / "common/clips/web" / f"{cid}_*.mp4")))
    st = "그림·영상 모두 있어요 → 이 장면은 아무것도 만들지 마세요" if has_img and has_vid else ("그림은 있어요 → 영상만 한 번 만들면 다른 화도 같이 써요" if has_img else "아직 없어요 → 이 화에서 한 번만 만들면 다른 화도 같이 써요")
    return (f'<p class="common">🔁 <b>공통 컷</b> · {e(COMMON.get(cid, {}).get("name", cid))} — 여러 화에 똑같이 나오는 장면이라 한 번만 만들어요. {e(st)}</p>')

def samevid_note(s):  # 그림이 같은 다른 장면의 영상을 같이 쓴다 (영상은 그 장면에서 한 번만)
    o = s.get("samevid")
    return (f'<p class="common">🔁 <b>같은 영상</b> · 이 장면은 <b>{e(o)}</b>와 같은 그림·영상을 써요. 그림과 영상은 {e(o)}에서 한 번만 만들고 이 장면은 {"그 영상을 한 번 더" if s.get("samevid_part") == "전체" else "그 " + s.get("samevid_part", "앞부분") + "을"} 써요 → 그림도 영상도 만들지 마세요</p>') if o else ""

cards = []
for i, s in enumerate(scenes, 1):
    cards.append(f'''<article class="scene" id="{s['id'].lower()}">
  <header class="scene-head"><span class="sid">{i}/{len(scenes)} · {e(s['id'])}</span><h2>{e(s['name'])}</h2><span class="time">{e(s['time'])}</span></header>
  {common_note(s)}{samevid_note(s)}{('<p class="common">📝 <b>' + e(s['note']) + '</b></p>') if s.get('note') else ''}
  <div class="step"><b>① 나오는 친구</b> <span class="chips">{chips(s['refs'])}</span></div>
  <div class="step"><b>② 그림 만들기</b> · 16:9</div>
  {box("그림 프롬프트", s['id'] + "-i", s['img'])}
  {thumb(s['id'], s.get('common'))}
  <div class="step"><b>③ 영상 만들기</b> · 방금 그림을 시작 이미지로 · <b class="sec">{s['sec']}초</b> · 소리 끔</div>
  {box("영상 프롬프트", s['id'] + "-v", s['vid'])}
</article>''')

sheets = "".join(f'<a class="sheet" href="sheets/{CH[k][1]}_sheet.png" target="_blank" rel="noopener"><img src="sheets/{CH[k][1]}_sheet.png" alt="{CH[k][0]} 시트" loading="lazy"><span><i style="background:{CH[k][2]}"></i>@{CH[k][1]} {CH[k][0]}</span></a>' for k in "CRTPB")
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
.ok { margin: 0; display: grid; gap: 6px; }
.common { margin: 0; padding: 10px 12px; border-radius: 10px; background: color-mix(in srgb, var(--accent) 12%, transparent); border: 1.5px solid var(--accent); font-size: 0.92rem; }
.ok img { width: 100%; max-width: 480px; aspect-ratio: 16 / 9; object-fit: cover; border-radius: 10px; border: 2px solid var(--accent); }
.ok figcaption { font-size: .9rem; }
"""
page = f'''<title>{e(title)} 장면</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;600&family=IBM+Plex+Mono:wght@400&display=swap">
<style>
{css}</style>
<div class="wrap">
  <header style="display:grid;gap:8px">
    <h1>{e(title)}</h1>
    <p class="lead">Higgsfield 웹사이트에서 장면 {len(scenes)}개를 하나씩 만들어요. 장면마다 ①→②→③ 순서만 지키면 돼요.</p>\n    <p class="warn">📐 그림 화면에서 모델 이름 옆 <b>「⛶ 자동」</b> 버튼을 눌러 <b>16:9</b>로 바꾼 다음 만들어요. 다 만들면 공유 링크를 보내 주세요.</p>
  </header>
  <section class="fixed">
    <h2>저장해 둔 친구들 (Elements)</h2>
    <p class="lead">Higgsfield에 이미 저장해 두었어요. 웹사이트 프롬프트 칸에 <b>@</b>를 치면 목록에 나와요.</p>
    <div class="sheets">{sheets}<a class="sheet" href="sheets/style_village.png" target="_blank" rel="noopener"><img src="sheets/style_village.png" alt="마을 그림" loading="lazy"><span>🏝 @village 마을 (화풍 기준)</span></a></div>
  </section>
  <section class="fixed">
    <h2>② 그림 만드는 법</h2>
    <ol class="big">
      <li>Higgsfield에서 <b>Image</b>를 누르고, 모델은 <b>GPT Image 2.6 Sunburst</b>(무제한)를 골라요.</li>
      <li>프롬프트 아래 줄, 모델 이름 옆 <b>「⛶ 자동」</b>을 눌러 <b>16:9</b>로 바꿔요. (자동으로 두면 정사각형이 나와요!)</li>
      <li><b>시트는 올리지 않아요!</b> 친구들과 마을 그림은 Higgsfield에 <b>Elements</b>로 저장해 두었어요. 프롬프트 안에 <b>@chiqui</b>, <b>@village</b> 같은 이름이 들어 있어서 자동으로 들어가요.</li>
      <li>그림 프롬프트 옆 <b>복사</b>를 누르고 붙여 넣어요.</li>
      <li>붙여 넣은 뒤 <b>@이름</b>이 색깔 있는 칸(이름표)으로 바뀌었는지 봐요. 그냥 글자로 남아 있으면, 그 글자를 지우고 <b>@</b>를 직접 쳐서 목록에서 친구를 골라요. 그다음 <b>Generate</b>를 눌러요.</li>
      <li>그림을 확인해요. 친구 모습이 시트와 같고, 똑같은 친구가 두 번 나오지 않고, 풍선 개수와 색이 맞으면 성공이에요. 이상하면 한 번 더 만들어요.</li>
    </ol>
  </section>
  <section class="fixed">
    <h2>③ 영상 만드는 법</h2>
    <ol class="big">
      <li><b>Video</b>를 누르고, 모델은 <b>Seedance 2.5</b>(무제한)를 골라요.</li>
      <li><b>Unlimited(무제한)</b> 스위치를 켜요.</li>
      <li><b>「레퍼런스 추가하기」</b>를 눌러 그 장면에서 만든 그림을 넣어요. <b>첫 프레임(시작 프레임)</b> 선택지가 있으면 골라요. <b>캐릭터 시트나 @요소는 넣지 않아요!</b> 그림 한 장만 넣어요.</li>
      <li>길이는 장면에 적힌 대로(<b>5초</b> 또는 <b>10초</b>), 종횡비 <b>16:9</b>, 프롬프트 아래 <b>🔊 소리는 끔</b>으로 바꿔요.</li>
      <li>영상 프롬프트를 복사해서 붙여 넣고, 길이(<b>5초</b> 또는 <b>10초</b>)를 장면에 적힌 대로 맞춰요. 소리(Audio) 스위치가 있으면 <b>꺼요.</b> 화질은 <b>1080p</b>.</li>
      <li><b>Generate</b> 버튼을 눌러요.</li>
    </ol>
    <p class="warn">⚠️ Generate 버튼에 <b>크레딧 숫자</b>가 보이면 누르지 말고 멈춰요. 무제한이 안 켜진 거예요. 스위치를 다시 확인하거나 저한테 알려 주세요.</p>
  </section>
  <section class="fixed">
    <h2>다 만들면</h2>
    <p class="lead">파일 이름을 바꾸거나 올릴 필요 없어요. 여기 채팅에 <b>"다 만들었어"</b>라고만 말해 주세요. 같은 계정이라 제가 가져와서 확인하고 노래·대사를 붙여 완성할게요. 목록에 없는 장면(오프닝, 노래 시작 부분 등)은 앞 화 영상을 다시 써서 안 만들어도 돼요.</p>
  </section>
  <nav class="jump" aria-label="장면 바로가기">{nav}</nav>
  {"".join(cards)}
</div>
<script>
{js}</script>
'''
(ep / "scene_prompts_page.html").write_text(page, encoding="utf-8")
md = [f"# {title} — 장면 프롬프트 (웹사이트용)", "", "그림: GPT Image 2.6 Sunburst(웹 무제한), 16:9, 캐릭터·화풍은 Elements(@chiqui @roro @torong @pio @bau @village). 영상: Seedance 2.5(웹 무제한), 그림 한 장만 시작 프레임으로, 끊김 없는 한 컷, 소리 끔.", ""]
for s in scenes:
    refs = ", ".join(CH[r][0] for r in s["refs"]) or "없음"
    md += [f"### {s['id']} {s['name']} ({s['time']})", f"[레퍼런스] {refs}", "[그림]", "```", s["img"], "```", f"[영상] {s['sec']}초", "```", s["vid"], "```", ""]
(ep / "prompts.md").write_text("\n".join(md), encoding="utf-8")
print("ok", len(scenes))
