"""3화 장면 데이터(scenes.json) 만들기. 웹에서 쓰는 그림·영상 프롬프트."""
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
BRUSH = "a small toothbrush with a round orange handle and white bristles"
CUP = "a little round yellow clay cup"
PASTE = "a small toothpaste tube that is BRIGHT GREEN all over (green tube body and green cap, the same green as Torong, not mint, not teal, not blue)"
TOWEL = "a small soft sky-blue towel"

AT = {"C": "@chiqui", "R": "@roro", "T": "@torong", "P": "@pio", "B": "@bau"}

FULL = "Show every character's full body from head to feet, with empty space around them; nothing is cut off at the edges. Keep the characters in the middle of the frame. "

def img(chars, scene, extra=""):
    # 웹사이트 Elements(@이름)로 캐릭터·화풍을 넣는다. 시트를 따로 올리지 않아도 된다.
    if chars:
        head = "Characters: " + "; ".join(f"{AT[c]} is {D[c]}" for c in chars) + ". Draw them exactly like their element images. "
        count = f" Draw exactly one of each character, never duplicated ({len(chars)} character{'s' if len(chars) > 1 else ''} in total)."
    else:
        head, count = "", " No characters in this scene."
    return f"Wide horizontal 16:9 landscape image, like a TV screen (1920x1080), not square. {head}{scene}{count}{(' ' + extra) if extra else ''} {FULL if 'Close' not in scene else ''}Match the art style, colors, textures and lighting of @village (style only, do not copy its layout). {STYLE}"

S = [
 ("S02", "아침이에요!", "0:20–0:30", "C", 10,
  img("C", f"Bright morning sun rising over the dinosaur village. {D['C']} stands in front of a round cave house with a green leaf door, stretching both arms up and yawning a big sleepy yawn.", "No toothbrush in this scene."),
  "Chiqui stretches slowly, gives a big sleepy yawn, then blinks and smiles at the morning sun. " + KEEP),
 ("S03", "치키야, 이 닦자!", "0:30–0:35", "BC", 5,
  img("BC", f"{D['B']} walks up to {D['C']} in front of the cave house, holding {CUP} and smiling warmly.", "Exactly one cup."),
  "Grandpa Bau walks up with the yellow cup, nods and smiles kindly; Chiqui looks up at him. " + KEEP),
 ("S04", "어? 칫솔이 없다!", "0:35–0:40", "C", 5,
  img("C", f"{D['C']} stands in front of a round stone wash basin with a small empty wooden toothbrush holder on it, looking at the empty holder with big surprised eyes and an open mouth.", "No toothbrush anywhere in this scene."),
  "Chiqui looks at the empty holder, jumps a little in surprise and looks left and right. " + KEEP),
 ("S05", "칫솔이 사라졌어요!", "0:40–0:45", "C", 5,
  img("C", f"Inside a cozy round cave house with soft toys, blocks and a little bed scattered around, {D['C']} searches, lifting a pillow and peeking under it.", "No toothbrush anywhere in this scene."),
  "Chiqui lifts the pillow, peeks under the bed, then scratches the head, puzzled. " + KEEP),
 ("S06", "친구들아, 같이 찾자!", "0:45–0:50", "C", 5,
  img("C", f"{D['C']} stands outside the cave house door in a sunny meadow, waving both arms high and calling out to friends far away.", "No toothbrush in this scene."),
  "Chiqui waves both arms and calls out happily toward the distance. " + KEEP),
 ("S07", "좋아!", "0:50–0:55", "CRTP", 5,
  img("CRTP", f"{D['R']}, {D['T']} and {D['P']} (flying low) arrive and gather around {D['C']} on a sunny meadow, all nodding and smiling eagerly.", "No toothbrush in this scene."),
  "The friends nod together and cheer, bouncing a little with excitement. " + KEEP),
 ("S09", "로로 · 노란 컵", "1:05–1:15", "R", 10,
  img("R", f"{D['R']} peeks behind a big round play rock on a grassy playground with a swing and a slide, and finds {CUP} lying in the grass.", "Exactly one cup."),
  "Roro picks up the yellow cup, holds it up high and does a cute little happy roar, wiggling with joy. " + KEEP),
 ("S10", "토롱 · 초록 치약", "1:15–1:25", "T", 10,
  img("T", f"{D['T']} stretches the long neck up toward a high branch of a big leafy tree where {PASTE} is resting.", "Exactly one toothpaste tube."),
  "Torong stretches the neck up slowly, gently takes the bright green toothpaste tube in the mouth, brings it down and smiles proudly. The toothpaste tube stays bright green the whole time. " + KEEP),
 ("S11", "피오 · 파란 수건", "1:25–1:35", "P", 10,
  img("P", f"{D['P']} flies above soft fluffy cloud hills holding {TOWEL} in the beak, the towel fluttering in the breeze.", "Exactly one towel."),
  "Pio flies happily across the cloud hills with the blue towel fluttering, doing a gentle swoop. " + KEEP),
 ("S12", "치키 칫솔은?", "1:35–1:45", "C", 10,
  img("C", f"Front view of {D['C']} standing alone in a grassy meadow, looking around with a puzzled, slightly sad face. Only the front of the frill is visible.", "No toothbrush visible anywhere in this scene."),
  "Chiqui looks left, then right, then down, searching; the shoulders droop a little. Chiqui keeps facing the camera. " + KEEP),
 ("S13", "같이 찾아 줄게", "1:45–1:55", "CRTP", 10,
  img("CRTP", f"{D['R']} holding {CUP}, {D['T']} holding {PASTE} in the mouth and {D['P']} holding {TOWEL} come to {D['C']}, who has nothing. They all look around together kindly. Chiqui faces the camera.", "Exactly one cup, one toothpaste tube and one towel. No toothbrush."),
  "The friends gather around Chiqui, give a gentle pat, and all look around together, turning their heads. The cup stays yellow, the toothpaste tube stays bright green and the towel stays sky-blue the whole time. " + KEEP),
 ("S14", "칫솔은 어디 있을까?", "1:55–2:00", "C", 5,
  img("C", f"Close-up of {D['C']} facing the viewer with a curious face, head tilted, as if asking a question. Only the front of the face and frill is visible.", "No toothbrush visible."),
  "Chiqui tilts the head, blinks and looks at the viewer as if asking 'Where is it?'. " + KEEP),
 ("S15", "치키 머리에 있다!", "2:00–2:05", "C", 5,
  img("C", f"{D['C']} seen from behind and slightly to the side. {BRUSH} is stuck upright in the top of the frill, between the yellow spots, clearly visible.", "Exactly one toothbrush."),
  "Chiqui wiggles the head; the toothbrush stuck in the frill wobbles back and forth. " + KEEP),
 ("S16", "어? 여기 있었네!", "2:05–2:10", "CRTP", 5,
  img("CRTP", f"{D['C']} pulls {BRUSH} out of the top of the frill and laughs. {D['R']}, {D['T']} and {D['P']} laugh happily around Chiqui.", "Exactly one toothbrush."),
  "Chiqui holds up the toothbrush and laughs; the friends giggle and bounce. " + KEEP),
 ("S17", "이제 치카치카 해 볼까?", "2:10–2:20", "BCRTP", 10,
  img("BCRTP", f"{D['B']} stands in front of the four friends holding a purple toothbrush, smiling. {D['C']} holds {BRUSH}; {D['R']}, {D['T']} and {D['P']} each hold a toothbrush in their own color. They stand by the round stone wash basin.", "Each character holds exactly one toothbrush."),
  "Grandpa Bau lifts the toothbrush and nods; the friends lift their toothbrushes too, ready. " + KEEP),
 ("S18a", "위아래로 치카치카", "2:20–2:25", "B", 5,
  img("B", f"Close view of {D['B']} smiling with the mouth open in a big grin, holding a purple toothbrush to the front teeth, showing how to brush.", "Exactly one toothbrush."),
  "Grandpa Bau brushes the front teeth gently up and down, up and down, with a cheerful face. " + KEEP),
 ("S18b", "동글동글 치카치카", "2:25–2:30", "B", 5,
  img("B", f"Close view of {D['B']} smiling with the mouth open, holding a purple toothbrush to the side teeth, with a few small soft white bubbles.", "Exactly one toothbrush."),
  "Grandpa Bau brushes the side teeth in small gentle circles, round and round, and a few soft bubbles float up. " + KEEP),
 ("S19", "반짝반짝!", "2:30–2:40", "BCRTP", 10,
  img("BCRTP", f"All five friends stand in a row by a round stone wash basin, brushing their teeth together with soft white foam bubbles. Each one holds exactly one toothbrush whose handle is the SAME COLOR AS ITS OWN BODY: {D['C']} holds an ORANGE toothbrush; {D['R']} holds a YELLOW toothbrush; {D['T']} holds a GREEN toothbrush; {D['P']} holds a SKY-BLUE toothbrush; {D['B']} holds a PURPLE toothbrush. No pink, no teal, no mixed-up colors.", "Exactly five toothbrushes: orange, yellow, green, sky-blue, purple, each matching its owner's body color."),
  "Everyone brushes up and down with little foam bubbles, then they all smile wide together and their teeth sparkle with a twinkle. Each toothbrush keeps exactly the same color and stays in the same character's hand the whole time: Chiqui orange, Roro yellow, Torong green, Pio sky-blue, Grandpa Bau purple. " + KEEP),
 ("S20", "칫솔 들고 춤", "2:40–2:50", "BCRTP", 10,
  img("BCRTP", f"All five friends dance happily in a flowery meadow with sparkling clean smiles. Each one holds up exactly one toothbrush whose handle is the SAME COLOR AS ITS OWN BODY: {D['C']} holds an ORANGE toothbrush; {D['R']} holds a YELLOW toothbrush; {D['T']} holds a GREEN toothbrush; {D['P']} holds a SKY-BLUE toothbrush; {D['B']} holds a PURPLE toothbrush. No pink, no teal, no mixed-up colors.", "Exactly five toothbrushes: orange, yellow, green, sky-blue, purple, each matching its owner's body color."),
  "Everyone dances in a happy circle, waving their toothbrushes; Grandpa Bau claps along. Each toothbrush keeps exactly the same color and stays in the same character's hand the whole time: Chiqui orange, Roro yellow, Torong green, Pio sky-blue, Grandpa Bau purple. " + KEEP),
 ("S21", "내일 또 만나요", "2:50–3:00", "BCRTP", 10,
  img("BCRTP", f"Golden sunset over the dinosaur village. All five friends stand together facing the viewer, smiling big sparkling smiles and waving goodbye: {D['C']}, {D['R']}, {D['T']}, {D['P']} and {D['B']}.", "No toothbrushes in this scene."),
  "Everyone waves goodbye to the viewer with big sparkling smiles in the soft evening light. " + KEEP),
]
out = [dict(id=a, name=b, time=c, refs=list(d), sec=e, img=f, vid=g) for a, b, c, d, e, f, g in S]
Path(__file__).with_name("scenes.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(len(out), "scenes,", sum(x["sec"] for x in out), "sec")
