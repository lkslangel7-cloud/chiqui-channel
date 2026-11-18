"""4화 장면 데이터(scenes.json) 만들기. 웹에서 쓰는 그림·영상 프롬프트."""
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
    return f"Wide horizontal 16:9 landscape image, like a TV screen (1920x1080), not square. {head}{scene}{count}{(' ' + extra) if extra else ''} {FULL if not any(w in scene for w in ('Close', 'hide', 'crouches', 'covering')) else 'Keep the characters in the middle of the frame. '}Match the art style, colors, textures and lighting of @village (style only, do not copy its layout). {STYLE}"

FLOWER = "a huge round pink flower, as big as a beach ball, with soft petals"
BUSH = "a small round green bush, much smaller than Grandpa Bau"
S = [
 ("S02", "숨바꼭질 하자!", "0:20–0:30", "BCRTP", 10,
  img("BCRTP", f"In a sunny flower meadow, {D['C']} jumps happily and waves both arms, suggesting a game to {D['R']}, {D['T']}, {D['P']} (flying low) and {D['B']}, who all smile and lean in.", ""),
  "Chiqui bounces with excitement and waves; the friends nod and cheer together. " + KEEP),
 ("S03", "하나, 둘, 셋, 넷, 다섯!", "0:30–0:40", "C", 10,
  img("C", f"{D['C']} stands facing a big tree trunk, forehead against the tree, covering both eyes with both hands, counting. Flower meadow around.", ""),
  "Chiqui keeps both eyes covered and nods the head gently as if counting slowly, the tail wagging. " + KEEP),
 ("S04", "쉿! 살금살금~", "0:40–0:45", "BRTP", 5,
  img("BRTP", f"{D['R']}, {D['T']}, {D['B']} tiptoe away in different directions across a flower meadow with sneaky happy faces, and {D['P']} glides away low and quiet. They put a finger to their mouths saying shh.", ""),
  "The friends tiptoe away in different directions, sneaky and giggling quietly; Pio glides off softly. " + KEEP),
 ("S05", "다 숨었니?", "0:45–0:50", "C", 5,
  img("C", f"{D['C']} by the big tree takes the hands off the eyes and turns around with a curious, excited face.", ""),
  "Chiqui uncovers the eyes, turns around and looks across the meadow with a big curious smile. " + KEEP),
 ("S06", "친구들은 어디 있을까?", "0:50–0:55", "C", 5,
  img("C", f"A wide empty flower meadow with a big round rock, a big leafy tree, {FLOWER} and {BUSH} in the distance. {D['C']} stands small in the middle looking left and right. No one else is visible.", ""),
  "Chiqui looks left and right across the quiet meadow, puzzled and excited. " + KEEP),
 ("S08", "살금살금 찾기", "1:00–1:05", "C", 5,
  img("C", f"{D['C']} tiptoes across the flower meadow with a sneaky playful face, peeking around, searching.", ""),
  "Chiqui tiptoes forward in big funny careful steps, peeking left and right. " + KEEP),
 ("S09", "로로 꼬리 보여", "1:05–1:15", "CR", 10,
  img("CR", f"{D['R']} hides behind a big round rock, but the yellow tail with orange spots sticks out from the side of the rock. {D['C']} tiptoes toward the rock, pointing at the tail with a delighted face.", ""),
  "Chiqui sneaks up and taps the tail; Roro pops up from behind the rock with a cute little roar and they both laugh. " + KEEP),
 ("S10", "토롱 목이 보여", "1:15–1:25", "CT", 10,
  img("CT", f"{D['T']} hides behind a big leafy tree, but the long neck and head stick up above the leaves, clearly visible. {D['C']} looks up at Torong's head and giggles.", ""),
  "Chiqui points up and laughs; Torong peeks down shyly, then smiles and steps out from behind the tree. " + KEEP),
 ("S11", "피오는 작아요", "1:25–1:35", "CP", 10,
  img("CP", f"{D['P']} is tiny and hides inside {FLOWER}, only the eyes and beak peeking out between the petals. {D['C']} leans close to the flower with a surprised happy face.", ""),
  "The flower petals wiggle; Pio pops out with a shy giggle and flutters up; Chiqui claps happily. " + KEEP),
 ("S12", "다 보여요 할아버지", "1:35–1:45", "BC", 10,
  img("BC", f"{D['B']} crouches behind {BUSH}; almost the whole big purple body is visible around the little bush, and Grandpa smiles with eyes closed as if hidden. {D['C']} stands nearby laughing.", ""),
  "Grandpa Bau peeks over the little bush and chuckles warmly; Chiqui laughs and points. " + KEEP),
 ("S13", "다 찾았다!", "1:45–1:55", "BCRTP", 10,
  img("BCRTP", f"All five friends gather together in the flower meadow laughing happily: {D['C']}, {D['R']}, {D['T']}, {D['P']} and {D['B']}.", ""),
  "Everyone laughs and bounces together in a happy little huddle. " + KEEP),
 ("S14", "누가 클까?", "1:55–2:00", "TP", 5,
  img("TP", f"{D['T']} stands tall next to {D['P']}, who stands on the grass right beside Torong's front feet, looking very small. Side by side, clear size difference, plain meadow background.", ""),
  "Torong and Pio stand side by side and look at each other, then at the viewer, smiling. " + KEEP),
 ("S15", "토롱!", "2:00–2:05", "T", 5,
  img("T", f"{D['T']} stretches the long neck up high proudly, smiling, in the flower meadow.", ""),
  "Torong stretches the neck up tall and proud, then gives a happy little nod. " + KEEP),
 ("S16", "누가 작을까?", "2:05–2:10", "P", 5,
  img("P", f"{D['P']} stands small on the grass with a shy smile, little wings slightly open, among tall flowers.", ""),
  "Pio smiles shyly and flutters the little wings. " + KEEP),
 ("S17", "피오!", "2:10–2:20", "TP", 10,
  img("TP", f"{D['P']} sits on top of the head of {D['T']}, and both smile happily at the viewer.", ""),
  "Pio flutters up and lands on Torong's head; they both laugh and wiggle happily. " + KEEP),
 ("S18", "커도 작아도, 다 좋은 친구!", "2:20–2:30", "BCRTP", 10,
  img("BCRTP", f"{D['B']} gives a warm hug to {D['T']} and {D['P']}, while {D['C']} and {D['R']} stand close, smiling. SIZE RULE: Torong is MUCH TALLER than everyone else, with a very long neck, and Torong\'s head is high above all the other friends\' heads; Pio is the smallest.", ""),
  "Grandpa Bau hugs Torong and Pio warmly; Chiqui and Roro join the hug, everyone smiling. Torong stays much taller than everyone with a long neck the whole time. " + KEEP),
 ("S19", "까꿍!", "2:30–2:40", "BCRTP", 10,
  img("BCRTP", f"All five friends stand in a row facing the viewer, covering their eyes with their hands, ready to play peekaboo: {D['C']}, {D['R']}, {D['T']}, {D['P']} and {D['B']}. SIZE RULE: Torong is MUCH TALLER than everyone else, with a very long neck, and Torong\'s head is high above all the other friends\' heads; Pio is the smallest.", ""),
  "Everyone keeps their eyes covered for a moment, then opens their hands wide at the same time with big happy surprised faces, peekaboo! Torong stays much taller than everyone with a long neck the whole time. " + KEEP),
 ("S20", "다 같이 춤", "2:40–2:50", "BCRTP", 10,
  img("BCRTP", f"All five friends dance happily in a circle in the flower meadow: {D['C']}, {D['R']}, {D['T']}, {D['P']} and {D['B']}. SIZE RULE: Torong is MUCH TALLER than everyone else, with a very long neck, and Torong\'s head is high above all the other friends\' heads; Pio is the smallest.", ""),
  "Everyone dances in a happy circle; Grandpa Bau claps along. Torong stays much taller than everyone with a long neck the whole time. " + KEEP),
 ("S21", "내일 또 만나요", "2:50–3:00", "BCRTP", 10,
  img("BCRTP", f"Golden sunset over the dinosaur village. All five friends stand together facing the viewer and wave goodbye: {D['C']}, {D['R']}, {D['T']}, {D['P']} and {D['B']}. SIZE RULE: Torong is MUCH TALLER than everyone else, with a very long neck, and Torong\'s head is high above all the other friends\' heads; Pio is the smallest.", ""),
  "Everyone waves goodbye to the viewer, swaying softly in the evening light. Torong stays much taller than everyone with a long neck the whole time. " + KEEP),
]
out = [dict(id=a, name=b, time=c, refs=list(d), sec=e, img=f, vid=g) for a, b, c, d, e, f, g in S]
Path(__file__).with_name("scenes.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(len(out), "scenes,", sum(x["sec"] for x in out), "sec")
