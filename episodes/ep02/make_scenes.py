"""2화 장면 데이터(scenes.json) 만들기. 웹에서 쓰는 그림·영상 프롬프트."""
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
BAL = "shiny round toy balloon with a curly white string"
def bal(c): return f"one bright {c} {BAL}"

def img(chars, scene, extra=""):
    if chars:
        head = "Use the attached character sheet" + ("s" if len(chars) > 1 else "") + " for the exact look of " + ", ".join(D[c] for c in chars) + ". "
        count = f" Draw exactly one of each character, never duplicated ({len(chars)} character{'s' if len(chars) > 1 else ''} in total)."
    else:
        head, count = "", " No characters in this scene."
    return f"{head}{scene}{count}{(' ' + extra) if extra else ''} Match the art style, colors, textures and lighting of the attached village picture (style only, do not copy its layout). 16:9 wide shot. {STYLE}"

S = [
 ("S02", "바우 할아버지의 풍선", "0:20–0:30", "B", 10,
  img("B", f"{D['B']} walks slowly and happily along a grassy path in a colorful volcanic-island dinosaur village, holding the strings of four balloons floating above: {bal('red')}, {bal('yellow')}, {bal('green')} and {bal('blue')}. Sunny sky, soft clouds, flowers.", "Exactly four balloons."),
  "Grandpa Bau walks slowly toward the camera with a warm smile; the four balloons bob gently above. Camera slowly follows. " + KEEP),
 ("S03", "친구들이 폴짝폴짝", "0:30–0:35", "BCRTP", 5,
  img("BCRTP", f"{D['C']}, {D['R']}, {D['T']} and {D['P']} (flying low) hurry happily toward {D['B']}, who holds four balloons (red, yellow, green, blue) on a grassy meadow. Everyone smiles.", "Exactly four balloons."),
  "The four young friends hop up and down with excitement around Grandpa Bau; Pio flaps a happy little loop. The balloons bob. " + KEEP),
 ("S04", "풍선 네 개 클로즈업", "0:35–0:40", "", 5,
  img("", f"Close-up of four balloons in a row against a bright blue sky with soft clouds, from left to right: {bal('red')}, {bal('yellow')}, {bal('green')}, {bal('blue')}.", "Exactly four balloons."),
  "One continuous shot with no cuts. The four balloons bob gently; a soft sparkle shines on each balloon one after another, left to right: red, yellow, green, blue. Keep the soft 3D clay style unchanged."),
 ("S05", "바람이 휘잉!", "0:40–0:45", "BC", 5,
  img("BC", f"A gust of wind with swirling leaves. The four balloon strings (red, yellow, green, blue balloons) slip out of the paw of {D['B']}, who looks surprised. {D['C']} stands next to him with mouth open, pointing up.", "Exactly four balloons."),
  "A gust of wind blows leaves past; the balloon strings slip out of Grandpa Bau's paw and the four balloons rise up. Chiqui points up in surprise. " + KEEP),
 ("S06", "풍선이 날아가요", "0:45–0:50", "", 5,
  img("", f"Four small balloons (red, yellow, green, blue) drifting apart high in the sky above a colorful volcanic-island dinosaur village with a gentle smiling volcano, palm trees and round clay houses.", "Exactly four balloons."),
  "One continuous shot with no cuts. The four balloons float away slowly in four different directions: one toward a big rock, one toward a tall tree, one toward fluffy cloud hills, and the red one out of sight. Clouds drift. Keep the soft 3D clay style unchanged."),
 ("S07", "친구들아, 같이 찾자!", "0:50–0:55", "CRTP", 5,
  img("CRTP", f"{D['C']} waves both arms to call friends. {D['R']}, {D['T']} and {D['P']} gather around and nod eagerly. Grassy meadow, sunny.", "No balloons in this scene."),
  "Chiqui waves to the friends, and they all nod and cheer together. " + KEEP),
 ("S08", "다 같이 출발", "1:00–1:05", "CRTP", 5,
  img("CRTP", f"{D['C']}, {D['R']} and {D['T']} march happily side by side along a flowery path, with {D['P']} flying just above them. Seen from the side, bright morning.", "No balloons in this scene."),
  "The friends march forward together with bouncy steps; Pio glides along above them. Camera tracks sideways. " + KEEP),
 ("S09", "로로 · 노란 풍선", "1:05–1:15", "R", 10,
  img("R", f"{D['R']} stands on top of a big round play rock, reaching for {bal('yellow')} whose string is caught on the rock. Grassy playground, blue sky.", "Exactly one balloon."),
  "Roro grabs the yellow balloon's string, holds the balloon up high and does a cute little roar of joy, wiggling happily. " + KEEP),
 ("S10", "토롱 · 초록 풍선", "1:15–1:25", "T", 10,
  img("T", f"{D['T']} stretches the long neck up toward the top of a big leafy tree where {bal('green')} is stuck in the branches.", "Exactly one balloon."),
  "Torong stretches the neck up slowly, gently takes the green balloon's string in the mouth, brings it down and smiles proudly. " + KEEP),
 ("S11", "피오 · 파란 풍선", "1:25–1:35", "P", 10,
  img("P", f"{D['P']} flies above soft fluffy cloud hills, holding the string of {bal('blue')} in the beak. Bright sky.", "Exactly one balloon."),
  "Pio flies happily across the cloud hills with the blue balloon trailing behind, doing a gentle swoop. " + KEEP),
 ("S12", "치키 풍선은?", "1:35–1:45", "C", 10,
  img("C", f"{D['C']} stands alone in a grassy meadow looking around with a puzzled, slightly sad face. No balloon anywhere.", "No balloons in this scene."),
  "Chiqui looks left, then right, then up, searching; the shoulders droop a little. " + KEEP),
 ("S13", "같이 찾아 줄게", "1:45–1:55", "CRTP", 10,
  img("CRTP", f"{D['R']} holding {bal('yellow')}, {D['T']} holding {bal('green')} and {D['P']} holding {bal('blue')} come to {D['C']}, who has no balloon. They all look around together kindly.", "Exactly three balloons: yellow, green, blue."),
  "The friends gather around Chiqui, give a gentle pat, and all look around together, turning their heads. " + KEEP),
 ("S14", "빨간 풍선은 어디?", "1:55–2:00", "C", 5,
  img("C", f"Close-up of {D['C']} looking straight at the viewer with a curious face, head tilted, as if asking a question.", "No balloons in this scene."),
  "Chiqui tilts the head, blinks and looks at the viewer as if asking 'Where is it?'. " + KEEP),
 ("S15", "저기 있다!", "2:00–2:05", "B", 5,
  img("B", f"{D['B']} seen from behind, walking away slowly; the string of {bal('red')} is wrapped around the round club at the end of the tail, and the red balloon floats above the tail.", "Exactly one balloon."),
  "Grandpa Bau walks slowly; the red balloon bobs above the tail club with each step. " + KEEP),
 ("S16", "허허, 여기 있단다", "2:05–2:10", "B", 5,
  img("B", f"{D['B']} turns the head back over the shoulder and smiles kindly at the viewer; {bal('red')} is tied to the tail club.", "Exactly one balloon."),
  "Grandpa Bau turns around with a warm chuckle and wiggles the tail so the red balloon bobs. " + KEEP),
 ("S17", "고마워요, 할아버지!", "2:10–2:20", "BC", 10,
  img("BC", f"{D['B']} hands {bal('red')} to {D['C']}, who reaches up happily. Grassy meadow, sunny.", "Exactly one balloon."),
  "Chiqui takes the red balloon, jumps with joy and gives Grandpa Bau a big hug. " + KEEP),
 ("S18a", "노랑이랑 파랑을 섞으면?", "2:20–2:25", "BCRTP", 5,
  img("BCRTP", f"{D['B']} sits in front of a big flat white stone with two small clay bowls of paint, one bright yellow and one bright blue. {D['C']}, {D['R']}, {D['T']} and {D['P']} sit around watching with curious faces.", "No balloons in this scene."),
  "Grandpa Bau picks up the two paint bowls; the friends lean in curiously. " + KEEP),
 ("S18b", "짠! 초록이 됐네!", "2:25–2:30", "", 5,
  img("", "Close-up from above of a big flat white stone: a blob of bright yellow paint and a blob of bright blue paint swirling together in the middle, starting to turn green.", ""),
  "One continuous shot with no cuts. The yellow and blue paint swirl together and turn into bright green, with a little sparkle. Keep the soft 3D clay style unchanged."),
 ("S19", "무슨 색일까?", "2:30–2:40", "CRTP", 10,
  img("CRTP", f"The four friends stand in a row, each holding their own balloon, from left to right: {D['C']} with {bal('red')}, {D['R']} with {bal('yellow')}, {D['T']} with {bal('green')}, {D['P']} with {bal('blue')}.", "Exactly four balloons."),
  "One by one from left to right, each friend lifts the balloon up high: red, yellow, green, blue. " + KEEP),
 ("S20", "풍선 들고 춤", "2:40–2:50", "BCRTP", 10,
  img("BCRTP", f"All five friends dance happily in a flowery meadow: {D['C']} with {bal('red')}, {D['R']} with {bal('yellow')}, {D['T']} with {bal('green')}, {D['P']} with {bal('blue')}, and {D['B']} clapping.", "Exactly four balloons."),
  "Everyone dances in a happy circle, balloons bobbing; Grandpa Bau claps along. " + KEEP),
 ("S21", "내일 또 만나요", "2:50–3:00", "BCRTP", 10,
  img("BCRTP", f"Golden sunset over the dinosaur village. All five friends stand together facing the viewer and wave goodbye: {D['C']} with {bal('red')}, {D['R']} with {bal('yellow')}, {D['T']} with {bal('green')}, {D['P']} with {bal('blue')}, and {D['B']}.", "Exactly four balloons."),
  "Everyone waves goodbye to the viewer; the balloons sway softly in the evening breeze. " + KEEP),
]
out = [dict(id=a, name=b, time=c, refs=list(d), sec=e, img=f, vid=g) for a, b, c, d, e, f, g in S]
Path(__file__).with_name("scenes.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(len(out), "scenes,", sum(x["sec"] for x in out), "sec")
