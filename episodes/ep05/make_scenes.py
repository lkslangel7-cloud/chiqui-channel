"""5화 장면 데이터(scenes.json) 만들기. 웹에서 쓰는 그림·영상 프롬프트."""
import json
from pathlib import Path

STYLE = "Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text."
KEEP = "One continuous shot with no cuts and no scene changes. Keep every character exactly as in the start image and keep the soft 3D clay style unchanged. No new characters appear. Gentle, smooth motion."
D = {
    "C": "Chiqui, the orange baby triceratops with a yellow-spotted frill",
    "R": "Roro, the yellow baby T-rex with orange spots on the back",
    "T": "Torong, the green baby brachiosaurus with light-green spots",
    "P": "Pio, the little sky-blue pteranodon with a yellow beak",
    "B": "Grandpa Bau, the purple ankylosaurus with round glasses and white eyebrows",
}


AT = {"C": "@chiqui", "R": "@roro", "T": "@torong", "P": "@pio", "B": "@bau"}

FULL = "Show every character's full body from head to feet, with empty space around them; nothing is cut off at the edges. Keep the characters in the middle of the frame. "

def img(chars, scene, extra=""):
    # 웹사이트 Elements(@이름)로 캐릭터·화풍을 넣는다. 시트를 따로 올리지 않아도 된다.
    if chars:
        head = "Characters: " + "; ".join(f"{AT[c]} is {D[c]}" for c in chars) + ". Draw them exactly like their element images. "
        count = f" Draw exactly one of each character, never duplicated ({len(chars)} character{'s' if len(chars) > 1 else ''} in total)."
    else:
        head, count = "", " No characters in this scene."
    return f"Wide horizontal 16:9 landscape image, like a TV screen (1920x1080), not square. {head}{scene}{count}{(' ' + extra) if extra else ''} {FULL if not any(w in scene for w in ('Close', 'Close-up')) else 'Keep the characters in the middle of the frame. '}Match the art style, colors, textures and lighting of @village (style only, do not copy its layout). {STYLE}"

TALL = " SIZE RULE: Torong is MUCH TALLER than everyone else, with a very long neck, and Torong's head is high above all the other friends' heads; Pio is the smallest."
NOHANDS = " Torong never touches the face with front legs; Torong's front legs stay on the ground."
RAIN = "soft gentle rain falling as small clay droplets, grey-blue cloudy sky, still cute and cozy, not dark or scary"
KEEPT = "Torong stays much taller than everyone with a long neck the whole time. "
S = [
 ("S02", "소풍 가자!", "0:20–0:30", "BCRTP", 10,
  img("BCRTP", f"Bright sunny morning in a flower meadow. {D['C']} bounces happily with both arms up, and {D['R']}, {D['T']}, {D['P']} (flying low) and {D['B']} gather around smiling, excited.{TALL}", ""),
  "Chiqui bounces with excitement; the friends cheer and nod together. ONLY these 5 characters are in this scene: Grandpa Bau, Chiqui, Roro, Torong, Pio; no other character, animal or creature appears at any time. " + KEEPT + KEEP),
 ("S03", "비가 와요, 슬퍼", "0:30–0:35", "C", 5,
  img("C", f"The sky turns cloudy and {RAIN}. {D['C']} stands in the meadow looking up at the rain with a sad, droopy face and teary eyes.", ""),
  "Raindrops start to fall; Chiqui looks up, the shoulders droop and the face turns sad. ONLY Chiqui is in this scene from start to end; no other character, animal or creature appears at any time. " + KEEP),
 ("S04", "무서워…", "0:35–0:40", "T", 5,
  img("T", f"{RAIN}, a small cute lightning flash far away in the clouds. {D['T']} pulls the long neck down and in, hunches the body and looks scared with wide worried eyes, trembling a little.{NOHANDS}", ""),
  "A soft flash in the far clouds; Torong flinches, pulls the neck in and trembles a little, with the front legs on the ground. Only one Torong appears. ONLY Torong is in this scene from start to end; no other character, animal or creature appears at any time. " + KEEP),
 ("S05", "이리 오렴, 괜찮아", "0:40–0:45", "B", 5,
  img("B", f"{RAIN} around a big leafy tree that keeps the ground underneath dry. {D['B']} stands dry under the tree and waves one front paw kindly, calling friends to come, with a warm smile.", ""),
  "Grandpa Bau waves kindly and nods with a warm smile under the tree while the rain falls around. ONLY Grandpa Bau is in this scene from start to end; no other character, animal or creature appears at any time. " + KEEP),
 ("S06", "괜찮아!", "0:45–0:50", "BCRTP", 5,
  img("BCRTP", f"Under a big leafy tree, dry, while {RAIN} falls outside. {D['C']}, {D['R']}, {D['P']} and {D['B']} snuggle close together, and {D['T']} stands tall behind them with the long neck curved over them like a roof, now smiling softly.{TALL}{NOHANDS}", ""),
  "Everyone snuggles closer and smiles; Torong relaxes and smiles, gently curving the neck over the friends. ONLY these 5 characters are in this scene: Grandpa Bau, Chiqui, Roro, Torong, Pio; no other character, animal or creature appears at any time. " + KEEPT + KEEP),
 ("S07", "비가 그쳤다!", "0:50–0:55", "C", 5,
  img("C", f"The rain has stopped, the sun peeks out of the clouds and the wet meadow sparkles. {D['C']} jumps up happily under the big tree with arms raised.", "No rainbow yet in the sky."),
  "The sun comes out; Chiqui jumps up with joy and points ahead. ONLY Chiqui is in this scene from start to end; no other character, animal or creature appears at any time. " + KEEP),
 ("S09", "로로 · 웅덩이 첨벙", "1:05–1:15", "R", 10,
  img("R", f"After the rain, {D['R']} jumps into a shallow blue puddle in the meadow, splashing small clay water drops, laughing happily.", ""),
  "Roro hops and splashes in the puddle again and again, laughing with a cute little roar. Only one Roro appears. ONLY Roro is in this scene from start to end; no other character, animal or creature appears at any time. " + KEEP),
 ("S10", "토롱 · 살펴봐요", "1:15–1:25", "T", 10,
  img("T", f"After the rain, {D['T']} stretches the very long neck up high and looks far away across the hills with a curious face. Fluffy clouds, no rainbow visible yet.{NOHANDS}", "No rainbow in this scene."),
  "Torong stretches the neck up high and turns the head left and right, searching, then tilts the head, puzzled. Only one Torong appears and stays tall. ONLY Torong is in this scene from start to end; no other character, animal or creature appears at any time. " + KEEP),
 ("S11", "피오 · 무지개 발견", "1:25–1:35", "P", 10,
  img("P", f"{D['P']} flies high above fluffy white clouds and sees a big bright rainbow arching across the sky, with a delighted, sparkling face.", "Exactly one rainbow."),
  "Pio flies higher, sees the rainbow, gasps happily and does a joyful loop. Only one Pio appears and stays small. ONLY Pio is in this scene from start to end; no other character, animal or creature appears at any time. " + KEEP),
 ("S12", "치키 · 안 보여요", "1:35–1:45", "C", 10,
  img("C", f"{D['C']} stands in front of tall grass and bushes that are taller than Chiqui, jumping to try to see over them, with a slightly sad, frustrated face.", "No rainbow visible in this scene."),
  "Chiqui hops up and down trying to see over the tall grass, then the shoulders droop a little, sad. ONLY Chiqui is in this scene from start to end; no other character, animal or creature appears at any time. " + KEEP),
 ("S13", "친구들이 토닥토닥", "1:45–1:55", "CRTP", 10,
  img("CRTP", f"{D['R']}, {D['T']} and {D['P']} come to {D['C']}, who looks a little sad, and comfort Chiqui with gentle pats and kind smiles. Tall grass behind.{TALL}{NOHANDS}", ""),
  "The friends gather around Chiqui and give gentle pats; Chiqui slowly smiles again. ONLY these 4 characters are in this scene: Chiqui, Roro, Torong, Pio; no other character, animal or creature appears at any time. " + KEEPT + KEEP),
 ("S14", "치키는 어떻게 볼까?", "1:55–2:00", "C", 5,
  img("C", f"Close-up of {D['C']} facing the viewer with a hopeful, curious face, head tilted, as if asking a question.", ""),
  "Chiqui tilts the head and looks at the viewer hopefully. ONLY Chiqui is in this scene from start to end; no other character, animal or creature appears at any time. " + KEEP),
 ("S15", "내가 도와줄게!", "2:00–2:10", "CT", 10,
  img("CT", f"{D['T']} lowers the long neck all the way down to the ground with a kind smile, and {D['C']} climbs up and sits on top of Torong's head, holding on happily.{NOHANDS}", "Torong is much bigger than Chiqui."),
  "Torong slowly lifts the neck up, carrying Chiqui higher and higher on top of the head; Chiqui holds on and giggles. Only one Torong and one Chiqui appear. ONLY these 2 characters are in this scene: Chiqui, Torong; no other character, animal or creature appears at any time. " + KEEP),
 ("S16", "와! 무지개다!", "2:10–2:20", "CT", 10,
  img("CT", f"{D['C']} sits on top of the head of {D['T']}, whose long neck is stretched up high above the tall grass. In front of them a big bright rainbow arches across the sky. Chiqui throws both arms up with a huge happy face.{NOHANDS}", "Exactly one rainbow. Torong is much bigger than Chiqui."),
  "Chiqui cheers with arms up, looking at the rainbow; Torong smiles proudly and sways gently. Torong stays tall the whole time. ONLY these 2 characters are in this scene: Chiqui, Torong; no other character, animal or creature appears at any time. " + KEEP),
 ("S17", "슬퍼도 괜찮아", "2:20–2:30", "BCRTP", 10,
  img("BCRTP", f"{D['B']} smiles warmly at the friends, {D['C']}, {D['R']}, {D['T']} and {D['P']}, who sit close together in the sparkling wet meadow. A big rainbow arches in the sky behind them.{TALL}{NOHANDS}", "Exactly one rainbow."),
  "Grandpa Bau nods and smiles warmly; the friends lean in and smile back. ONLY these 5 characters are in this scene: Grandpa Bau, Chiqui, Roro, Torong, Pio; no other character, animal or creature appears at any time. " + KEEPT + KEEP),
 ("S18", "지금 기분은? 기뻐!", "2:30–2:40", "BCRTP", 10,
  img("BCRTP", f"All five friends stand in a row facing the viewer with big happy smiles under a big rainbow: {D['C']}, {D['R']}, {D['T']}, {D['P']} and {D['B']}.{TALL}{NOHANDS}", "Exactly one rainbow."),
  "Everyone looks at the viewer for a moment, then all cheer and bounce happily together. ONLY these 5 characters are in this scene: Grandpa Bau, Chiqui, Roro, Torong, Pio; no other character, animal or creature appears at any time. " + KEEPT + KEEP),
]
out = [dict(id=a, name=b, time=c, refs=list(d), sec=e, img=f, vid=g) for a, b, c, d, e, f, g in S]
Path(__file__).with_name("scenes.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(len(out), "scenes,", sum(x["sec"] for x in out), "sec")
