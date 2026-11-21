"""11~15화 대본·가사·장면 프롬프트를 만든다. 찾기 이야기에서 벗어난 새 형식 (편식, 체조, 건강 검진, 생일, 기차).
도우미 함수(img, vid, items, write)와 안전 문장은 make_ep06_10.py 것을 그대로 쓴다.
사용법: python3 -I prompts/make_ep11_15.py
"""
from pathlib import Path

_src = (Path(__file__).resolve().parent / "make_ep06_10.py").read_text(encoding="utf-8")
_ns = {"__file__": __file__}
exec(_src.split("EPS = {}")[0], _ns)
exec(_src[_src.index("def write"):_src.index("for ep, e in EPS.items()")].replace("2026-11-18", "2026-11-20"), _ns)
img, vid, items, write, D = _ns["img"], _ns["vid"], _ns["items"], _ns["write"], _ns["D"]

NODOLL = "No toy dinosaurs, dolls, stuffed animals or animal figures anywhere. "
HOME = "INDOORS inside a cozy round room of the cave house (soft cream walls, a round window, wooden shelves); NOT outdoors: no meadow, no open sky, no rainbow, no volcano. " + NODOLL
CLINIC = ("INDOORS inside Grandpa Bau's cozy round check-up room in the cave house (soft cream walls, a round window, a tall wooden height chart "
          "painted on the wall, a low wooden bench); NOT outdoors: no meadow, no open sky, no rainbow, no volcano. " + NODOLL)
COAT = "Grandpa Bau wears a small white doctor coat and a simple stethoscope around the neck"
T = ["0:20–0:30", "0:30–0:35", "0:35–0:40", "0:40–0:45", "0:45–0:50", "0:50–0:55",
     "1:05–1:15", "1:15–1:25", "1:25–1:35", "1:35–1:45", "1:45–1:55", "1:55–2:00", "2:00–2:10", "2:10–2:20", "2:20–2:30", "2:30–2:40"]
IDS = ["S02", "S03", "S04", "S05", "S06", "S07", "S09", "S10", "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18"]
SEC = [10, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 5, 10, 10, 10, 10]


def scenes(rows):
    """rows: (이름, 친구, 그림 문장, 덧붙임, 가까이?, 영상 문장) 16개 → write()가 쓰는 장면 튜플."""
    assert len(rows) == 16
    return [(IDS[i], n, T[i], r, SEC[i], img(r, s, x, c), vid(r, v)) for i, (n, r, s, x, c, v) in enumerate(rows)]


EPS = {}
FOOD = {"C": "ORANGE carrot sticks", "R": "one YELLOW corn cob", "T": "GREEN broccoli florets", "P": "dark BLUE blueberries", "B": "PURPLE grapes"}
# ---------------- 11화 골고루 냠냠 (편식) ----------------
EPS["ep11"] = dict(
 title="11화. 골고루 냠냠! — 편식 없이 먹기", short="골고루 냠냠!", song_id="yum", song_short="골고루 냠냠",
 theme="편식하지 않기, 한 입 도전. 친구마다 자기 몸 색 음식 (치키 당근, 로로 옥수수, 토롱 브로콜리, 피오 블루베리, 바우 포도).",
 twist="당근만 먹던 치키가 초록 브로콜리를 한 입 먹어 보고 \"어? 맛있다!\" (화면 밖 아이도 같이 한 입 도전)",
 bau="큰 공룡도 초록 잎을 먹었단다!",
 lines=[("치키","점심 먹자!",""),("모두","좋아!","♻ 1화 07"),("바우","알록달록 도시락!",""),("치키","나는 당근만!",""),
        ("치키","으~ 초록색은 싫어.",""),("바우","한 입만 먹어 볼까?",""),("모두","우리가 보여 줄게!",""),
        ("내레이션","치키도 먹어 볼까?","뒤에 3초 쉼"),("치키","어? 맛있다!",""),("모두","와아~","♻ 1화 15"),
        ("바우","큰 공룡도 초록 잎을 먹었단다!","바우 할아버지 상식"),("모두","힘이 쑥쑥!",""),("모두","잘 먹었습니다!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("노란 옥수수 톡톡톡","크앙! 로로가 와앙","옥수수 냠냠 (냠냠!)"),("초록 브로콜리 작은 나무","쭈욱~ 토롱이 냠","브로콜리 냠냠 (냠냠!)"),
         ("파란 블루베리 콩콩콩","슝~ 피오가 콕","블루베리 냠냠 (냠냠!)"),("치키도 한 입 해 볼까?","망설망설 (할 수 있어!)","한 입만 냠 (냠!)")],
 chorus="골고루 냠냠!",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "골고루 냠냠! (냠냠!)", "한 입 두 입 맛있게", "치키치키 냠냠!"],
 scenes=scenes([
  ("점심 먹자!", "BCRTP", "On a sunny flower meadow, all five friends sit around a big round picnic blanket with a closed picnic basket, cheering happily.", "", False,
   "Everyone claps and bounces a little on the picnic blanket, smiling."),
  ("알록달록 도시락", "B", f"{D['B']} sits at a picnic blanket and opens a big picnic basket, showing five small bowls of food: {', '.join(FOOD.values())}.",
   "Exactly five bowls, one food each, colors exactly as written.", False, "Grandpa Bau lifts the basket lid and smiles warmly at the colorful bowls."),
  ("나는 당근만!", "C", f"{D['C']} sits on the picnic blanket holding one ORANGE carrot stick happily, with a plate that has only orange carrots.",
   "Only orange carrots on Chiqui's plate.", False, "Chiqui munches the carrot stick happily, then hugs the plate of carrots."),
  ("으~ 초록색은 싫어", "C", f"Close view of {D['C']} looking at a small bowl of GREEN broccoli with a funny 'yuck' face, tongue sticking out a little, turning the head away.",
   "", True, "Chiqui scrunches the face, sticks the tongue out a little and turns the head away from the broccoli, in a funny way."),
  ("한 입만 먹어 볼까?", "B", f"{D['B']} sits on a soft YELLOW-and-white checkered picnic blanket on the sunny meadow, holding up one small GREEN broccoli floret, smiling kindly with a gentle wink.",
   "Exactly one broccoli floret.", False, "Grandpa Bau holds up the broccoli, winks once and nods gently."),
  ("우리가 보여 줄게!", "RTP", "On the picnic blanket, Roro, Torong and Pio raise their own food with big smiles: Roro holds one YELLOW corn cob; Torong holds one GREEN broccoli floret in the mouth; Pio holds one dark BLUE blueberry in the beak.",
   "", False, "Roro, Torong and Pio raise their food and nod together, cheering."),
  ("로로 · 옥수수 와앙", "R", f"{D['R']} sits on the picnic blanket holding one YELLOW corn cob with both little arms, mouth wide open for a big bite.",
   "Exactly one corn cob.", False, "Roro takes a big crunchy bite of the corn: one, two, three bites, then smiles with puffy cheeks."),
  ("토롱 · 브로콜리 냠", "T", f"{D['T']} on the meadow bends the long neck down to a small bowl of GREEN broccoli florets on the picnic blanket.",
   "One bowl of broccoli.", False, "Torong picks up one broccoli floret with the mouth, chews slowly and nods happily."),
  ("피오 · 블루베리 콕", "P", f"{D['P']} stands on the picnic blanket next to a small bowl of dark BLUE blueberries, picking one with the beak.",
   "One bowl of blueberries.", False, "Pio pecks up blueberries one by one, three times, then flaps both wings once happily."),
  ("치키도 한 입?", "C", f"{D['C']} sits on the picnic blanket holding one small GREEN broccoli floret close to the mouth, eyes squeezed, unsure.",
   "Exactly one broccoli floret.", False, "Chiqui slowly brings the broccoli closer, stops, peeks at it with one eye, and brings it a little closer again."),
  ("한 입! 한 입!", "CRTP", "On the picnic blanket, Roro, Torong and Pio cheer for Chiqui, who holds one small green broccoli floret.",
   "", False, "The friends clap and cheer for Chiqui, bouncing a little."),
  ("치키도 먹어 볼까?", "C", f"Close-up of {D['C']} facing the viewer holding one small GREEN broccoli floret, with a brave, curious face.", "", True,
   "Chiqui looks at the viewer, then at the broccoli, and nods bravely once."),
  ("어? 맛있다!", "C", f"{D['C']} sits on the picnic blanket chewing, eyes wide with happy surprise, holding half a GREEN broccoli floret.", "", False,
   "Chiqui chews, eyes go wide, then smiles big and takes another bite."),
  ("큰 공룡도 초록 잎을", "B", f"{D['B']} sits under a big leafy tree next to the picnic, holding one big green leaf and smiling wisely.", "Exactly one leaf in the paw.", False,
   "Grandpa Bau lifts the leaf, nods wisely and smiles."),
  ("힘이 쑥쑥!", "BCRTP", "All five friends stand on the meadow next to the picnic blanket, flexing their front legs proudly like strong heroes, smiling.", "", False,
   "Everyone flexes proudly and jumps once together, landing softly."),
  ("잘 먹었습니다!", "BCRTP", "All five friends sit around the picnic blanket with empty clean plates, facing the viewer and bowing a little politely with happy smiles.",
   "All plates are empty.", False, "Everyone pats the tummy and bows a little to the viewer with a smile."),
 ]))
# ---------------- 12화 공룡 체조 (율동) ----------------
EPS["ep12"] = dict(
 title="12화. 공룡 체조! — 따라 하는 율동", short="공룡 체조!", song_id="gym", song_short="공룡 체조",
 theme="몸 움직이기 율동 노래. 친구마다 자기 몸 자랑 동작 (치키 머리 끄덕, 로로 꼬리 흔들, 토롱 목 쭈욱, 피오 날개 팔랑, 바우 발 쿵쿵). 화면 밖 아이가 따라 한다.",
 twist="치키는 토롱처럼 목이 안 늘어나고, 로로는 팔이 짧아 피오처럼 팔랑이 안 된다 — 모두 깔깔. 각자 달라도 다 멋져!",
 bau="티라노사우루스는 팔이 짧았단다.",
 lines=[("치키","잘 잤다!",""),("바우","아침 체조 시간!",""),("모두","좋아!","♻ 1화 07"),("치키","몸이 쭈욱~",""),
        ("내레이션","우리도 같이 해요!",""),("치키","어? 목이 안 늘어나!",""),("로로","내 팔은 짧아!",""),("모두","하하하!","♻ 3화 11"),
        ("바우","티라노사우루스는 팔이 짧았단다.","바우 할아버지 상식"),("모두","하나 둘! 하나 둘!",""),("모두","튼튼해졌다!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("머리를 끄덕끄덕","뿔이 셋 치키처럼","끄덕끄덕 (끄덕!)"),("꼬리를 흔들흔들","크앙! 로로처럼","흔들흔들 (흔들!)"),
         ("목을 쭈욱 쭈욱","길쭉 토롱처럼","쭈욱쭈욱 (쭈욱!)"),("팔을 팔랑팔랑","슝~ 피오처럼","팔랑팔랑 (팔랑!)")],
 chorus="공룡 체조 시작!",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "공룡 체조 시작! (시작!)", "하나 둘 셋 넷", "치키치키 체조!"],
 scenes=scenes([
  ("잘 잤다!", "C", f"Early morning in the dinosaur village: {D['C']} steps out of the round cave house door, stretching both arms up with a big happy yawn.", "", False,
   "Chiqui yawns, stretches both arms up high, then smiles and steps forward."),
  ("아침 체조 시간!", "B", f"{D['B']} stands on a sunny morning meadow, raising one front paw cheerfully like a gym teacher.", "", False,
   "Grandpa Bau raises the paw and stomps one front foot happily."),
  ("좋아!", "CRTP", "On the sunny morning meadow, Chiqui, Roro, Torong and Pio stand in a row, cheering and ready to exercise.", "", False,
   "The friends cheer and bounce on the spot."),
  ("몸이 쭈욱~", "C", f"{D['C']} stands on the meadow stretching the whole body up tall with both arms high, eyes closed happily.", "", False,
   "Chiqui stretches up tall, holds it for two seconds, then relaxes with a happy sigh."),
  ("우리도 같이 해요!", "C", f"{D['C']} faces the viewer on the meadow, waving one paw toward the viewer as if inviting them to join.", "", False,
   "Chiqui waves toward the viewer twice, inviting them to join, and smiles."),
  ("준비!", "BCRTP", "All five friends stand in a row on the sunny meadow facing the viewer, in a ready pose with front paws on their hips.", "", False,
   "Everyone bends the knees a little and gets ready, smiling."),
  ("치키처럼 끄덕끄덕", "C", f"{D['C']} faces the viewer on the meadow, nodding the head down, showing the three horns and yellow-spotted frill proudly.", "", False,
   "Chiqui nods the head down and up four times to a steady beat, smiling."),
  ("로로처럼 흔들흔들", "R", f"{D['R']} stands on the meadow seen from the side, wagging the tail with a big happy smile.", "", False,
   "Roro wags the tail left and right four times to a steady beat, giggling."),
  ("토롱처럼 쭈욱쭈욱", "T", f"{D['T']} stands on the meadow stretching the very long neck straight up toward the sky, smiling.", "", False,
   "Torong lowers the neck, then stretches it up tall, two times, slowly and happily."),
  ("피오처럼 팔랑팔랑", "P", f"{D['P']} stands on the meadow with both wide wings open, flapping them gently.", "", False,
   "Pio flaps both wings up and down four times to a steady beat, hopping a little."),
  ("할아버지 쿵쿵", "BCRTP", "All five friends dance together on the meadow; Grandpa Bau in the middle stomps one front foot, everyone smiling.", "", False,
   "Everyone stomps one foot, then the other, four times, and claps."),
  ("목이 안 늘어나!", "C", f"Close view of {D['C']} standing on tiptoe on the meadow, chin lifted up, cheeks puffed and eyes squeezed with a funny straining face, trying to look tall. Chiqui's neck stays SHORT and round exactly like the element image: the frill sits right on the shoulders, no long neck at all. Chiqui's body shape is unchanged.", "The neck must NOT look longer than normal.", True,
   "Chiqui stretches the neck up as far as possible, it stays short, and Chiqui laughs at it."),
  ("내 팔은 짧아!", "R", f"{D['R']} stands on the meadow trying to flap the two tiny short arms like wings, with a funny proud face.", "", False,
   "Roro flaps the tiny arms quickly, nothing happens, and Roro bursts out laughing."),
  ("티라노는 팔이 짧았단다", "B", f"{D['B']} sits on the meadow smiling wisely, holding up one front paw as if telling a fun fact.", "", False,
   "Grandpa Bau nods and chuckles warmly."),
  ("하나 둘! 하나 둘!", "BCRTP", "All five friends dance in a circle on the sunny meadow, each doing a happy move.", "", False,
   "Everyone turns around once in place and claps together, smiling."),
  ("튼튼해졌다!", "BCRTP", "All five friends stand in a row facing the viewer, flexing proudly with big smiles after exercise.", "", False,
   "Everyone flexes, then waves at the viewer happily."),
 ]))
# ---------------- 13화 아~ 해 보세요 (건강 검진) ----------------
STAR = "small star sticker on the chest"
EPS["ep13"] = dict(
 title="13화. 아~ 해 보세요! — 건강 검진", short="아~ 해 보세요!", song_id="doc", song_short="건강 검진",
 theme="병원·검진이 무섭지 않아요. 키 재기, 청진기 콩닥콩닥, 입 아~. 끝나면 자기 몸 색 별 스티커.",
 twist="무서워서 숨었던 로로가 친구들을 보고 용기를 내고, 노란 '용감한 별'을 받는다.",
 bau="아프면 꼭 말해 주렴.",
 lines=[("바우","오늘은 건강 검진 날!",""),("로로","무서워…","작고 떨리게"),("바우","괜찮아, 하나도 안 아파.",""),("치키","내가 먼저 할래!",""),
        ("로로","나는… 나중에.",""),("모두","로로야, 같이 하자!",""),("내레이션","로로는 무엇을 받았을까?","뒤에 3초 쉼"),("로로","용감한 별이다!",""),
        ("모두","와아~","♻ 1화 15"),("바우","아프면 꼭 말해 주렴.","바우 할아버지 한마디"),("모두","우리 모두 용감한 별!",""),("모두","건강해!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("키 재기 쭈욱쭈욱","토롱이 제일 커","쭉쭉 컸네 (와!)"),("콩닥콩닥 청진기","치키 마음 소리","콩닥콩닥 (콩닥!)"),
         ("입을 크게 아~","피오도 아~","아~ 잘했어요 (아~!)"),("로로 차례 두근두근","눈을 꼭 감고 (할 수 있어!)","하나도 안 아파 (짝짝!)")],
 chorus="아~ 해 보세요!",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "아~ 해 보세요! (아~!)", "하나도 안 무서워", "치키치키 튼튼!"],
 scenes=scenes([
  ("건강 검진 날!", "BCRTP", CLINIC + f"{COAT}, smiling kindly; Chiqui, Roro, Torong and Pio stand in a line on the floor waiting their turn.", "No needles or syringes anywhere.", False,
   "Grandpa Bau waves kindly; the friends wave back, Roro looks a little nervous."),
  ("무서워…", "R", CLINIC + f"{D['R']} peeks out from behind the low wooden bench, looking a little scared.", "", False,
   "Roro hides behind the bench, peeks out slowly, then hides again. Only one Roro appears."),
  ("하나도 안 아파", "B", CLINIC + f"{D['B']}; {COAT}. Bau kneels down low and smiles gently, holding the stethoscope.", "No needles or syringes anywhere.", False,
   "Grandpa Bau nods gently and smiles softly."),
  ("내가 먼저 할래!", "C", CLINIC + f"{D['C']} raises one paw high, excited and brave, ready to go first.", "", False,
   "Chiqui raises the paw and hops once with excitement."),
  ("나는… 나중에", "R", CLINIC + f"{D['R']} stands next to the bench, fiddling the tiny hands shyly, looking down.", "", False,
   "Roro looks down, wiggles the tiny hands and peeks up once."),
  ("같이 하자!", "CRTP", CLINIC + "Chiqui, Torong and Pio gather around Roro, smiling and cheering Roro on kindly.", "", False,
   "The friends nod at Roro and smile; Roro smiles back a little."),
  ("토롱 · 키 재기", "BT", CLINIC + f"{D['T']} stands next to the tall height chart on the wall; the head is near the very top. {COAT}, looking up at Torong amazed.", "", False,
   "Torong stretches the neck up proudly next to the height chart; Grandpa Bau looks up and claps."),
  ("치키 · 청진기 콩닥", "BC", CLINIC + f"{COAT}. Bau gently holds the stethoscope to the chest of {D['C']}, who sits on the low bench smiling.", "", False,
   "Grandpa Bau listens with the stethoscope; Chiqui giggles and nods."),
  ("피오 · 아~", "BP", CLINIC + f"{D['P']} sits on the low bench with the beak wide open saying 'ahh'; {COAT}, looking with a small flashlight.", "", False,
   "Pio opens the beak wide, then closes it and smiles; Grandpa Bau nods."),
  ("로로 차례 두근두근", "BR", CLINIC + f"{D['R']} sits on the low bench with eyes squeezed shut bravely; {COAT}, holding the stethoscope gently near Roro's chest.", "", False,
   "Roro keeps the eyes shut, then opens one eye, then both, and smiles in surprise."),
  ("하나도 안 무서워!", "CRTP", CLINIC + "Chiqui, Roro, Torong and Pio jump and cheer together; Roro looks proud and happy.", "", False,
   "Everyone cheers and claps for Roro, bouncing a little."),
  ("로로는 무엇을 받았을까?", "R", CLINIC + f"Close-up of {D['R']} facing the viewer with a happy, curious face, hiding something behind the back.", "", True,
   "Roro smiles at the viewer and wiggles a little, keeping the hands behind the back."),
  ("용감한 별이다!", "R", CLINIC + f"{D['R']} proudly shows one YELLOW {STAR}, pointing at it with a big smile.", "Exactly one yellow star sticker.", False,
   "Roro points at the yellow star sticker and does a cute happy roar."),
  ("아프면 꼭 말해 주렴", "B", CLINIC + f"{D['B']}; {COAT}. Bau smiles warmly, one front paw on the chest.", "", False,
   "Grandpa Bau nods warmly and pats the own chest gently."),
  ("우리 모두 용감한 별!", "BCRTP", CLINIC + f"All five friends stand in a row facing the viewer, each with one {STAR} in their own body color: "
   "Chiqui ORANGE star, Roro YELLOW star, Torong GREEN star, Pio SKY-BLUE star, Grandpa Bau PURPLE star.", "Exactly five star stickers, one each.", False,
   "Everyone points proudly at their own star sticker and smiles."),
  ("건강해!", "BCRTP", CLINIC + "All five friends jump happily together facing the viewer, smiling big.", "", False,
   "Everyone jumps once together and waves at the viewer."),
 ]))
# ---------------- 14화 치키의 깜짝 생일 ----------------
CAKE = "round ORANGE birthday cake with exactly FOUR tall candles standing in one straight row on top (count them: one, two, three, four; NOT three, NOT five, no extra short or broken candle)"
EPS["ep14"] = dict(
 title="14화. 치키의 깜짝 생일! — 생일 파티", short="치키의 깜짝 생일!", song_id="bday", song_short="깜짝 생일 준비",
 theme="친구 생일 축하, 깜짝 준비, 촛불 세기(1~4). 친구마다 자기 몸 색 장식 (로로 노란 풍선, 토롱 초록 깃발, 피오 하늘색 꽃, 바우 주황 케이크).",
 twist="다들 잊어버린 줄 알았는데… 친구들이 몰래 깜짝 파티를 준비하고 있었다!",
 bau="치키도 알에서 태어났단다.",
 lines=[("치키","오늘은 내 생일!",""),("치키","다들 바쁜가 봐…",""),("바우","치키야, 눈 꼭 감아 볼래?",""),("모두","쉿!",""),
        ("내레이션","하나, 둘, 셋… 짠!",""),("모두","생일 축하해!",""),("치키","와! 고마워!",""),("바우","치키도 알에서 태어났단다.","바우 할아버지 상식 (1화 공룡알과 이어짐)"),
        ("내레이션","촛불이 몇 개일까?","뒤에 3초 쉼"),("모두","하나, 둘, 셋, 넷!",""),("치키","후~!",""),("모두","와아~","♻ 1화 15"),("치키","안녕!","♻ 1화 18")],
 verses=[("노란 풍선 후우후","크앙! 로로가 빵빵","풍선 완성 (빵빵!)"),("초록 깃발 높이높이","쭈욱~ 토롱이 척","깃발 완성 (척!)"),
         ("하늘색 꽃 한 아름","슝~ 피오가 쏙","꽃도 완성 (쏙!)"),("주황 케이크 촛불 넷","하나 둘 셋 넷 (넷!)","케이크 완성 (짠!)")],
 chorus="쉿! 깜짝 준비",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "쉿! 깜짝 준비 (쉿!)", "치키 몰래 살금살금", "치키치키 생일!"],
 scenes=scenes([
  ("오늘은 내 생일!", "C", f"Sunny morning in the dinosaur village: {D['C']} hops out of the round cave house with a huge excited smile.", "No decorations yet.", False,
   "Chiqui hops twice with joy and spins around once."),
  ("다들 바쁜가 봐…", "C", f"{D['C']} stands alone on a quiet meadow, looking around with a slightly sad face.", "", False,
   "Chiqui looks left, then right, then the shoulders drop a little."),
  ("눈 꼭 감아 볼래?", "B", f"{D['B']} smiles with a playful wink, holding one front paw up as if keeping a secret.", "", False,
   "Grandpa Bau winks once and chuckles."),
  ("쉿!", "RTP", "Roro and Pio stand close together peeking out from behind a big bush, Roro holding one tiny paw near the mouth and Pio one wing near the beak, saying 'shh'; "
   "Torong stands behind them and bends the long neck down low to listen.", "", False,
   "Roro and Pio whisper 'shh' and giggle quietly; Torong nods slowly."),
  ("치키 데리고 가기", "BC", f"{D['C']} covers both eyes with both front paws and walks slowly; {D['B']} walks beside, guiding gently.", "", False,
   "Chiqui walks slowly with eyes covered; Grandpa Bau guides gently, smiling."),
  ("살금살금 준비", "RTP", "On a sunny meadow, Roro, Torong and Pio tiptoe around a picnic table, carrying decorations carefully.", "No cake yet.", False,
   "The friends tiptoe carefully and look around with 'shh' faces."),
  ("로로 · 노란 풍선", "R", f"{D['R']} blows up one YELLOW balloon, cheeks puffed, standing on a meadow.", "Exactly one yellow balloon.", False,
   "Roro puffs three times, the yellow balloon grows bigger, and Roro ties it and smiles."),
  ("토롱 · 초록 깃발", "T", f"{D['T']} stretches the long neck up high to hang a string of small GREEN triangle flags between two trees.", "All flags green.", False,
   "Torong lifts the flag string up high with the mouth and hangs it neatly, then smiles."),
  ("피오 · 하늘색 꽃", "P", f"{D['P']} flies low over a meadow carrying a small bunch of SKY-BLUE flowers in the beak.", "All flowers sky-blue.", False,
   "Pio glides down and places the sky-blue flowers on the table, then flaps once happily."),
  ("케이크 촛불 넷", "B", f"{D['B']} places a {CAKE} on a wooden picnic table, smiling.", "Exactly four candles, not lit yet.", False,
   "Grandpa Bau carefully sets the cake down and counts the candles with one paw."),
  ("다 같이 숨어요", "BRTP", f"Grandpa Bau, Roro, Torong and Pio hide behind a big bush next to the decorated picnic table with the {CAKE}, yellow balloons and green flags.", "", False,
   "Everyone ducks down behind the bush and giggles quietly."),
  ("하나, 둘, 셋… 짠!", "C", f"Close-up of {D['C']} facing the viewer, both front paws covering the eyes, smiling in excitement.", "", True,
   "Chiqui slowly lowers the paws and opens the eyes wide with surprise."),
  ("생일 축하해!", "BCRTP", f"Surprise party on a sunny meadow: Roro, Torong, Pio and Grandpa Bau jump out cheering around Chiqui, next to a picnic table with the {CAKE}, "
   "YELLOW balloons, GREEN flags and SKY-BLUE flowers.", "Exactly four candles.", False,
   "Everyone throws the arms up and cheers; Chiqui hugs both cheeks with joy."),
  ("치키도 알에서 태어났단다", "B", f"{D['B']} sits by the party table holding one small cracked pastel egg shell, smiling warmly.", "Exactly one egg shell.", False,
   "Grandpa Bau shows the egg shell and smiles warmly."),
  ("촛불 하나 둘 셋 넷, 후~", "C", f"{D['C']} leans toward the {CAKE} with the four candles lit, cheeks puffed, ready to blow.", "Exactly four lit candles.", False,
   "Chiqui blows 'whoo' once; the four little flames go out one by one; Chiqui cheers."),
  ("와아~ 파티!", "BCRTP", f"All five friends dance happily around the party table with the {CAKE}, YELLOW balloons, GREEN triangle flags and SKY-BLUE flowers, facing the viewer.", "Exactly four candles. Balloons only yellow, flags only green.", False,
   "Everyone dances and spins once, then waves at the viewer."),
 ]))
# ---------------- 15화 칙칙폭폭 공룡 기차 ----------------
TRAIN = ("a small toy-like train on a wooden track: one PURPLE engine in front, then four open little cars in this order: ORANGE car, YELLOW car, "
         "long GREEN car (open top), SKY-BLUE car")
EPS["ep15"] = dict(
 title="15화. 칙칙폭폭 공룡 기차! — 기차 놀이", short="칙칙폭폭 공룡 기차!", song_id="train", song_short="공룡 기차",
 theme="탈것·차례대로 타기. 바우 할아버지 보라 기차가 역마다 친구를 태운다 (자기 몸 색 칸). 터널에서 토롱이 고개 숙이기.",
 twist="터널이 나타났는데 토롱 목이 길다! 화면 밖 아이가 \"고개 숙여!\" 외쳐 주면 통과.",
 bau="브라키오사우루스는 집보다 컸단다.",
 lines=[("치키","심심해~",""),("바우","칙칙폭폭, 기차 출발!",""),("치키","내가 첫 번째 손님!",""),("치키","친구들 태우러 가자!",""),
        ("내레이션","다음 역은 어디일까?",""),("내레이션","토롱아, 고개 숙여!","아이가 따라 외치게 2초 쉼"),("토롱","휴~ 통과!",""),("모두","와아~","♻ 1화 15"),
        ("바우","브라키오사우루스는 집보다 컸단다.","바우 할아버지 상식"),("모두","도착!",""),("모두","또 타자!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("놀이터 바위 역","크앙! 로로가 타요","노란 칸에 쏙 (쏙!)"),("큰 나무 역","쭈욱~ 토롱이 타요","초록 칸에 쏙 (쏙!)"),
         ("구름 언덕 역","슝~ 피오가 타요","파란 칸에 쏙 (쏙!)"),("앗! 터널이다","토롱 목이 길어 (어떡하지?)","고개 숙여! (숙여!)")],
 chorus="칙칙폭폭 공룡 기차",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "칙칙폭폭 공룡 기차 (칙칙폭폭!)", "친구들아 어서 타", "치키치키 출발!"],
 scenes=scenes([
  ("심심해~", "C", f"{D['C']} sits on a grassy hill in the village with the chin on both paws, looking bored.", "", False,
   "Chiqui sighs, rolls onto the back in the grass and looks at the sky."),
  ("기차 출발!", "B", f"{D['B']} sits in the PURPLE engine of {TRAIN}, all cars empty, waving happily.", "All four cars are empty.", False,
   "Grandpa Bau waves and a little puff of white steam rises from the engine."),
  ("첫 번째 손님!", "BC", f"{D['C']} climbs happily into the ORANGE car of {TRAIN}; {D['B']} sits in the PURPLE engine smiling back.", "Yellow, green and sky-blue cars are empty.", False,
   "Chiqui sits down in the orange car and claps; Grandpa Bau nods."),
  ("칙칙폭폭 출발", "BC", f"{TRAIN} rolls along the wooden track through a flower meadow; {D['B']} drives the PURPLE engine and {D['C']} rides in the ORANGE car.",
   "Yellow, green and sky-blue cars are empty.", False, "The train rolls slowly forward along the track; Chiqui waves; small puffs of steam rise."),
  ("다음 역은 어디일까?", "C", f"Close view of {D['C']} sitting in the ORANGE train car, leaning out and looking ahead curiously with one paw above the eyes.", "", True,
   "Chiqui leans out, looks ahead and smiles excitedly."),
  ("친구들 태우러 가자!", "BC", f"{TRAIN} waits on the track; {D['B']} in the PURPLE engine, {D['C']} in the ORANGE car raising one paw high.", "Yellow, green and sky-blue cars are empty.", False,
   "Chiqui raises the paw and cheers; Grandpa Bau rings a little bell on the engine."),
  ("놀이터 바위 역 · 로로", "BCR", f"{TRAIN} stops next to a big play rock; {D['R']} hops into the YELLOW car. Grandpa Bau drives the PURPLE engine and Chiqui rides in the ORANGE car.",
   "Green and sky-blue cars are empty.", False, "Roro hops into the yellow car and does a cute happy roar; Chiqui claps."),
  ("큰 나무 역 · 토롱", "BCRT", f"{TRAIN} stops next to a big leafy tree; {D['T']} steps into the long open GREEN car, the long neck sticking up high. "
   "Grandpa Bau in the PURPLE engine, Chiqui in the ORANGE car, Roro in the YELLOW car.", "The sky-blue car is empty.", False,
   "Torong steps into the green car and settles down, smiling; the friends cheer."),
  ("구름 언덕 역 · 피오", "BCRTP", f"{TRAIN} stops on a soft cloud hill; {D['P']} glides down into the SKY-BLUE car. Grandpa Bau in the PURPLE engine, Chiqui ORANGE car, "
   "Roro YELLOW car, Torong GREEN car.", "", False, "Pio lands in the sky-blue car and flaps once; everyone cheers."),
  ("앗! 터널이다", "BCRTP", f"{TRAIN} with all five friends riding rolls toward a round low stone tunnel in a green hill; Torong's long neck is much taller than the tunnel.",
   "Exactly one tunnel.", False, "The train rolls slowly toward the tunnel; the friends point at it with worried faces."),
  ("다 같이 칙칙폭폭", "BCRTP", f"{TRAIN} with all five friends riding in their own colored cars rolls happily along a sunny meadow.", "", False,
   "The train rolls forward; everyone sways side to side and waves."),
  ("토롱아, 고개 숙여!", "T", f"Close view of {D['T']} sitting in the long GREEN train car, looking at the viewer with a worried face, the long neck up high.", "", True,
   "Torong looks at the viewer, then slowly bends the long neck down low."),
  ("휴~ 통과!", "BCRTP", f"{TRAIN} comes out of the round stone tunnel; Torong lifts the long neck back up with a relieved smile; everyone cheers.", "Exactly one tunnel.", False,
   "The train rolls out of the tunnel; Torong raises the neck and everyone cheers."),
  ("브라키오사우루스는 집보다 컸단다", "B", HOME.replace("a cozy round room of the cave house", "Grandpa Bau's cozy round fossil library").replace("wooden shelves", "wooden shelves with old books and fossil stones")
   + f"{D['B']} stands next to a big fossil bone, smiling wisely.", "Exactly one big fossil bone.", False, "Grandpa Bau pats the fossil bone gently and smiles."),
  ("도착!", "BCRTP", f"{TRAIN} stops in front of the round entrance of a cozy fossil library; all five friends climb out happily.", "", False,
   "Everyone hops out of the cars and cheers."),
  ("또 타자!", "BCRTP", f"All five friends stand in front of {TRAIN}, facing the viewer, waving goodbye with big smiles.", "", False,
   "Everyone waves at the viewer; a small puff of steam rises from the engine."),
 ]))

for ep, e in EPS.items():
    write(ep, e)
