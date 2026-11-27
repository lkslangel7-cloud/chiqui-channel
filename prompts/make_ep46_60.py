"""46~60화 대본·가사·장면 프롬프트 (2026-11-27).
인기 유아 채널(코코멜론·핑크퐁·뽀로로·베베핀)에서 아이들이 좋아하는 '소재'만 참고했다
(설날 세배, 몸 이름 율동, 화날 때 숨쉬기, 반대말, 알, 어둠, 색 섞기, 공놀이, 물 마시기, 봄, 소풍, 보물찾기,
공룡 먹이, 날씨, 어린이날 연날리기). 이야기·노래·그림은 모두 새로 만든다. 1~45화와 같은 주제는 피했다.
도우미(img·vid·scenes·write·CHEER·WAVE·BAU·MEADOW·LEGS)는 make_ep41_45.py 것을 그대로 쓴다
(치키·바우 다리 규칙, 토롱 네 발 규칙, 영상 LOCK이 자동으로 붙는다).
41~45화에서 배운 것: 반복 소품은 한 문장으로 고정(자리·색·개수), 토롱·바우는 물건을 들지 않는다(입·코로),
치키가 앞발을 쓰면 뒷다리 둘로 선다, 몸 구조상 안 되는 동작을 쓰지 않는다, 카메라 고정, 동작은 결과까지.
사용법: python3 -I prompts/make_ep46_60.py
"""
from pathlib import Path
import collections as _col, json as _json

_p = Path(__file__).resolve().parent / "make_ep41_45.py"
_src = _p.read_text(encoding="utf-8")
_ns = {"__file__": str(_p)}
exec(_src.split("\nEPS = {}\n\n# ---------------- 41화")[0], _ns)
img, vid, scenes, write, D, HOME, NODOLL, NEAR, MEADOW, CHEER, WAVE, BAU = (
    _ns[k] for k in ("img", "vid", "scenes", "write", "D", "HOME", "NODOLL", "NEAR", "MEADOW", "CHEER", "WAVE", "BAU"))

B4V = " Grandpa Bau keeps exactly 4 legs with all four feet flat on the ground; he never lifts a front foot."
CUPV = " Chiqui stays standing UPRIGHT on the two back legs the whole time (only two feet on the ground, exactly four legs)."
EPS = {}

# (2026-11-27, 사용자: 46화에 한복) 친구마다 몸 색 저고리 + 색동 소매. 다리·꼬리·프릴·바우 등딱지는 가리지 않는다(다리 수 확인이 쉽게).
# 공통 컷(좋아!·안녕!)은 한복이 없으니 46화는 이 두 장면도 한복을 입혀 따로 만든다.
HANBOK = {
 "C": "Chiqui wears one short soft ORANGE hanbok jacket (jeogori) with rainbow-striped saekdong sleeves and a small red ribbon tie on the chest",
 "R": "Roro wears one short soft YELLOW hanbok jacket with rainbow-striped saekdong sleeves and a small red ribbon tie",
 "T": "Torong wears one short soft GREEN hanbok jacket over the round body only (not on the neck) with a small red ribbon tie",
 "P": "Pio wears one tiny soft SKY-BLUE hanbok vest on the chest, the wings stay free and uncovered",
 "B": "Grandpa Bau wears one short soft PURPLE hanbok vest on the chest and front shoulders only, with a small gold ribbon tie; his back plates and tail club stay uncovered",
}
HB_RULE = (" The hanbok clothes are short and simple: they never cover the legs, feet, tail, frill or horns, so every leg is easy to see. "
           "Each friend wears only their own one hanbok in their own body color.")
HB_V = " Everyone keeps wearing the same hanbok clothes the whole time; the clothes never change color, never come off and never cover the legs."
def _hanbok(rows):
    out = []
    for n, r, sc, x, c, v in rows:
        if r:
            sc = sc + " " + "; ".join(HANBOK[k] for k in "CRTPB" if k in r) + "." + HB_RULE
            v = v + HB_V
        out.append((n, r, sc, x, c, v))
    return out

# ---------------- 46화 새해 복 많이 받으세요! (설날 세배) ----------------
ROOM46 = (HOME + "It is New Year's morning: one low round wooden table in the middle of the room and one round soft PURPLE floor cushion "
          "on the RIGHT side of the room. ")
SOUP46 = ("five small round bowls of white rice-cake soup with steam on the low round table, one bowl for each friend in their body color: "
          "ORANGE, YELLOW, GREEN, SKY-BLUE and PURPLE bowls")
EPS["ep46"] = dict(
 title="46화. 새해 복 많이 받으세요! — 설날 세배", short="새해 복 많이 받으세요!", song_id="newyear", song_short="세배 노래",
 theme="설날 아침, 알록달록 한복(색동 저고리) 입고 바우 할아버지께 꾸벅 세배, 덕담 듣기, 떡국 먹고 한 살 쑥. 인사 예절.",
 twist="치키가 너무 힘차게 꾸벅하다 데굴데굴 굴러요! 다 같이 웃고, 다시 천천히 꾸벅. 화면 밖 친구도 같이 꾸벅!",
 bau="공룡들도 해마다 쑥쑥 자랐단다!",
 lines=[("치키","새해다!",""),("치키","세배하러 가자!",""),("모두","좋아!","♻ 1화 07"),("모두","새해 복 많이 받으세요!",""),
        ("내레이션","어? 데굴데굴!",""),("모두","하하하!","♻ 3화 11"),("바우","새해 복 많이 받아라!",""),
        ("내레이션","우리 친구도 꾸벅!","뒤에 3초 쉼"),("모두","잘 먹겠습니다!",""),("치키","한 살 더 먹었다!",""),
        ("바우","공룡들도 해마다 쑥쑥 자랐단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("알록달록 색동옷","새해 아침 (아침!)","곱게 입었어요 (곱다!)"),("앞발 모으고 꾸벅","세배해요 (꾸벅!)","복 많이 받으세요 (복!)"),
         ("하얀 떡국 호호","한 그릇 냠냠 (냠냠!)","한 살 쑥 (쑥!)"),("키가 쑥쑥 자랐네","우리 모두 (쑥쑥!)","새해에도 사이좋게 (좋게!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "새해 복 많이 (받으세요!)", "꾸벅꾸벅 인사해요", "치키치키 새해!"],
 scenes=scenes(_hanbok([
  ("새해 아침", "C", HOME + f"{D['C']} stands UPRIGHT on ONLY the two back legs like a toddler (exactly two feet on the floor, the body upright, NOT on all fours) at the round window, both front paws resting on the round window sill, looking out at the big round rising morning sun, eyes sparkling with excitement; the tail rests on the floor behind.", "Exactly one sun.", False,
   "Chiqui bounces once on the same spot at the window and smiles." + CUPV),
  ("좋아!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio stand in a happy row in front of one round cave house with a round green door, cheering and bouncing with big smiles.", "Exactly one door.", False,
   "The friends cheer and bounce on the same spot for a moment, then turn their heads toward the green door and smile, ready to go in. The camera stays still."),
  ("세배하러 가자", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio stand in a happy row in front of one round cave house with a round green door, cheering and bouncing with big smiles.", "Exactly one door.", False,
   "The friends cheer and bounce on the same spot for a moment, then turn their heads toward the green door and smile, ready to go in. The camera stays still."),
  BAU(ROOM46, "할아버지가 기다려요", "sits on the round PURPLE floor cushion on the RIGHT side of the room, smiling warmly, glasses shining."),
  ("꾸벅! 세배", "BCRTP", ROOM46 + f"{D['B']} sits on the PURPLE cushion on the RIGHT; on the LEFT, Chiqui, Roro, Torong and Pio face him in a row, all doing the traditional Korean New Year deep bow (sebae): each one kneels down on the rug with the back legs folded under the body, puts the front paws (Pio: the wing tips) together flat on the floor in front, and lowers the forehead down onto the paws, the back rounded like a little ball, very polite; Torong lies down low with all four legs tucked under the body and bows the long neck so the chin touches the floor; nobody stands.", "", False,
   "Chiqui, Roro, Torong and Pio stay in the deep bow with foreheads on their paws for a moment, then slowly sit up on their knees and smile; Grandpa Bau smiles and nods." + B4V + " The camera stays still."),
  ("데굴데굴!", "BCRTP", ROOM46 + f"The same room and the same places as the bowing scene: {D['B']} sits on the PURPLE cushion on the RIGHT; on the LEFT, Roro, Torong and Pio are still kneeling in a row on the rug, lifting their heads from the deep bow and looking with big surprised eyes at Chiqui; in the middle of the rug in front of them, Chiqui has done the deep kneeling bow so hard that Chiqui tipped forward and is rolling over sideways like a round ball, eyes wide in funny surprise. Only one Chiqui appears.", "", False,
   "Chiqui rolls over once on the same spot on the rug and lands sitting up, blinking in surprise; Roro, Torong and Pio stay kneeling in their places and gasp; Grandpa Bau's eyebrows go up. Only one Chiqui appears." + B4V + " The camera stays still."),
  ("하하하! 다시 꾸벅", "BCRTP", ROOM46 + f"The same room and the same places as the bowing scene: {D['B']} sits on the PURPLE cushion on the RIGHT, laughing warmly with the eyes closed; on the LEFT, Chiqui, Roro, Torong and Pio are on their knees in a row on the rug facing him (back legs folded under the body, nobody stands up), all laughing together; Chiqui sits up on the knees with the body upright and scratches the head shyly with one front paw; Torong lies low with all four legs tucked under the body.", "Nobody stands up.", False,
   "Everyone laughs; then they slowly do the deep kneeling bow once again, foreheads down to their paws, and sit back up. The camera stays still."),
  BAU(ROOM46, "새해 복 많이 받아라", "sits on the PURPLE cushion nodding kindly with a big warm smile, as if saying good wishes.",
      " He nods two times slowly."),
  ("떡국이에요", "", ROOM46 + f"Close view of the low round table with {SOUP46}. No characters.", "Exactly five bowls, colors exactly as written.", True,
   "Soft steam rises gently from the five bowls; nothing else moves."),
  ("호호 불어요", "BCRTP", ROOM46 + f"All five friends sit around the low round table with {SOUP46}; {D['C']} stands UPRIGHT at the ORANGE bowl, cheeks puffed, blowing gently on the steam; Roro, Torong, Pio and Grandpa Bau (on his PURPLE cushion) smile and watch, each next to their own bowl. {NEAR}", "Exactly five bowls.", False,
   "Chiqui blows on the soup two times; the steam drifts away; the others smile and nod." + CUPV + B4V + " The camera stays still."),
  ("냠냠 떡국", "BCRTP", ROOM46 + f"All five friends eat rice-cake soup together around the low round table with {SOUP46}: Chiqui, Roro and Pio sip from their ORANGE, YELLOW and SKY-BLUE bowls; Torong bends the neck down to the GREEN bowl and Grandpa Bau lowers his head to the PURPLE bowl on the table, never holding them. {NEAR}", "Exactly five bowls.", False,
   "Everyone takes one sip and smiles with happy cheeks." + B4V + " The camera stays still."),
  ("한 살 더!", "CRTP", HOME + f"{D['C']} stands UPRIGHT with the back against one tall wooden height chart painted on the wall, one front paw on top of the head, proud big smile; Roro, Torong and Pio stand next to the chart cheering for Chiqui.", "Exactly one height chart.", False,
   "Chiqui stands tall, then hops once on the same spot proudly; the friends clap and cheer." + CUPV + " The camera stays still."),
  ("쑥쑥 자랐네", "CRTP", HOME + "Chiqui, Roro, Torong and Pio stand proudly in a row in the cozy room, standing tall and smiling.", "", False,
   "Everyone stretches up tall on the same spot and smiles. The camera stays still."),
  BAU(ROOM46, "해마다 쑥쑥", "sits on the PURPLE cushion smiling wisely, glasses shining."),
  ("새해 춤", "BCRTP", MEADOW + "All five friends dance happily together in the sunny New Year morning.", "", False,
   "Chiqui, Roro and Pio dance on the same spot; Torong sways the neck; Grandpa Bau wags the tail club." + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ])))

# ---------------- 47화 머리 어깨 꼬리 뿔! (몸 이름 율동) ----------------
EPS["ep47"] = dict(
 title="47화. 머리 어깨 꼬리 뿔! — 몸 이름 율동", short="머리 어깨 꼬리 뿔!", song_id="body", song_short="몸 노래",
 theme="몸 이름 따라 하기(머리·어깨·목·꼬리), 친구마다 다른 몸(치키 뿔 셋, 로로 짧은 팔, 토롱 긴 목, 피오 날개, 바우 꼬리 곤봉).",
 twist="노래가 점점 빨라지자 다들 엉켜서 꽈당! 다 같이 웃고 천천히 다시. 화면 밖 친구는 꼬리 대신 엉덩이 흔들!",
 bau="안킬로사우루스는 꼬리 곤봉으로 몸을 지켰단다!",
 lines=[("치키","율동 시간!",""),("모두","좋아!","♻ 1화 07"),("치키","머리 톡톡!",""),("로로","어깨 들썩!",""),("토롱","목 쭈욱!",""),
        ("바우","꼬리 살랑!",""),("내레이션","더 빨리!",""),("모두","하하하!","♻ 3화 11"),("내레이션","우리 친구도 머리 톡톡!","뒤에 3초 쉼"),
        ("바우","안킬로사우루스는 꼬리 곤봉으로 몸을 지켰단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("머리 머리 톡톡톡","치키 뿔은 (셋!)","반짝반짝 (반짝!)"),("어깨 어깨 들썩들썩","로로 팔은 (짧아!)","짝짝짝 (짝!)"),
         ("목을 목을 쭈욱쭈욱","토롱 목은 (길어!)","하늘까지 (쭈욱!)"),("꼬리 꼬리 살랑살랑","할아버지 (곤봉!)","둥둥둥 (둥!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "머리 어깨 (꼬리 뿔!)", "따라 해요 율동", "치키치키 율동!"],
 scenes=scenes([
  ("율동 시간!", "C", MEADOW + f"{D['C']} stands UPRIGHT with both front paws raised high, ready to dance, a big excited smile.", "", False,
   "Chiqui bounces two times on the same spot with both paws up." + CUPV),
  CHEER(MEADOW),
  ("머리 톡톡", "C", MEADOW + f"{D['C']} stands UPRIGHT and taps the top of the head with both front paws, eyes closed in a happy smile.", "", False,
   "Chiqui taps the top of the head two times with both paws and giggles." + CUPV),
  ("어깨 들썩", "R", MEADOW + f"{D['R']} shrugs both shoulders up high with the two short arms bent, a cheeky grin.", "", False,
   "Roro shrugs the shoulders up and down three times on the same spot."),
  ("꼬리 살랑", "B", MEADOW + f"{D['B']} stands on all four feet, looking back over the shoulder at his own tail club, wagging it to one side with a playful smile.", "", False,
   "Grandpa Bau wags the tail club left and right three times." + B4V + " The camera stays still."),
  ("목 쭈욱", "T", MEADOW + f"{D['T']} stretches the long neck straight up high toward the sky, all four feet on the ground, proud smile.", "", False,
   "Torong stretches the neck up slowly and then lowers it back, smiling; the neck keeps its normal length; all four feet stay on the ground."),
  ("뿔 셋 반짝", "C", MEADOW + f"Close view of {D['C']} standing UPRIGHT and pointing proudly with one front paw at the three horns on the head, which shine with a little sparkle.", "Exactly three horns.", True,
   "Chiqui points at the horns and smiles; a small sparkle twinkles on the horns." + CUPV),
  ("짧은 팔 짝짝", "R", MEADOW + f"{D['R']} claps the two short arms together in front of the tummy, laughing.", "", False,
   "Roro claps the short arms three times and laughs on the same spot."),
  ("날개 팔랑", "P", MEADOW + f"{D['P']} stands on the grass and opens both wide wings and flaps them happily.", "", False,
   "Pio flaps both wings three times on the same spot, hopping once."),
  ("더 빨리!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio dance very fast together in a funny wobbly way: Roro and Pio bump softly into each other, Chiqui wobbles, Torong sways the neck quickly.", "", False,
   "Everyone dances faster and faster on the same spot, wobbling and laughing. The camera stays still."),
  ("꽈당! 하하하", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio sit down on the grass in a happy heap after dancing too fast, laughing out loud together.", "", False,
   "Everyone laughs, rocking a little on the same spot. The camera stays still."),
  ("우리 친구도 머리 톡톡", "C", MEADOW + f"Close view of {D['C']} standing UPRIGHT facing the viewer, tapping the head with one front paw, inviting the viewer to copy.", "", True,
   "Chiqui taps the head once, then points the other paw at the viewer and waits, smiling." + CUPV),
  ("천천히 다시", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio stand in a row and dance slowly and neatly together: Chiqui taps the head, Roro shrugs, Torong stretches the neck up, Pio opens the wings.", "", False,
   "Everyone does the moves slowly together on the same spot. The camera stays still."),
  BAU(MEADOW, "꼬리 곤봉으로", "stands on all four feet showing his round tail club proudly to the side, smiling wisely."),
  ("다 같이 율동", "BCRTP", MEADOW + "All five friends dance together on the meadow; Grandpa Bau wags his tail club.", "", False,
   "Chiqui, Roro and Pio dance; Torong sways the neck; Grandpa Bau wags the tail club." + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 48화 화가 나면 후~ (마음 가라앉히기) ----------------
# (2026-11-27 사용자) 33화(블록 탑 와르르·미안해 괜찮아)와 겹쳐서 이야기 바꿈: 마지막 퍼즐 조각이 안 들어가 속상 → 후~ → 돌려 보니 쏙!
PUZ48 = ("one low flat square wooden puzzle tray lying on the grass with a simple picture of a big smiling yellow sun on a sky-blue background, "
         "made of exactly FOUR big chunky jigsaw pieces in a 2 by 2 grid")
HOLE48 = PUZ48 + "; three pieces are already in the tray and the top-right corner is an empty hole"
DONE48 = PUZ48 + ", all four pieces in place, the smiling sun picture complete"
PIECE48 = "one big chunky jigsaw piece with part of the sun picture on it"
EPS["ep48"] = dict(
 title="48화. 화가 나면 후~ — 마음 가라앉히기", short="화가 나면 후~", song_id="calm", song_short="후~ 노래",
 theme="잘 안 돼서 속상하고 화날 때: 숨을 크게 쉬고 셋 세기, 마음을 말로 하기, 천천히 다시 해 보기.",
 twist="로로의 해님 퍼즐, 마지막 한 조각이 아무리 눌러도 안 들어가요! 크앙 화가 났지만 '후~' 숨쉬기로 마음이 사르르. 천천히 빙글 돌려 보니… 쏙!",
 bau="큰 공룡도 숨을 크게 쉬었단다!",
 lines=[("로로","해님 퍼즐 놀이!",""),("모두","좋아!","♻ 1화 07"),("로로","어? 안 들어가!",""),("내레이션","꾹꾹! 그래도 안 들어가요.",""),("로로","크앙! 화났어!",""),
        ("바우","후~ 숨을 쉬어 보렴.",""),("모두","하나, 둘, 셋, 후~",""),("로로","속상했어. 이제 괜찮아.",""),("로로","빙글 돌려 볼까?",""),("내레이션","우리 친구도 후~","뒤에 3초 쉼"),
        ("로로","쏙! 맞았다!",""),("바우","큰 공룡도 숨을 크게 쉬었단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("얼굴이 빨개 부글부글","화가 났어요 (크앙!)","어떡하지? (어떡해?)"),("앞발을 배에 올리고","숨을 크게 (흡!)","후우~ (후~)"),
         ("하나 둘 셋 세어 봐요","천천히 (하나 둘 셋!)","마음이 사르르 (사르르!)"),("천천히 다시 해 봐","빙글 돌려 (빙글!)","쏙 맞았다 (쏙!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "화가 나면 (후~!)", "숨을 크게 쉬어요", "치키치키 후~!"],
 scenes=scenes([
  ("해님 퍼즐", "R", MEADOW + f"{D['R']} sits on the grass next to {HOLE48}, holding {PIECE48} in both short arms, happy and excited.", "Exactly three pieces in the tray and one piece in Roro's arms.", False,
   "Roro looks at the piece in the arms and at the empty corner, then smiles and nods, ready to put it in. The tray stays still."),
  CHEER(MEADOW),
  ("어? 안 들어가!", "R", MEADOW + f"{D['R']} sits next to {HOLE48} and presses {PIECE48} onto the empty corner, but the piece sits crooked and sticks up because it is turned the wrong way; Roro looks puzzled.", "Exactly four pieces in total.", False,
   "Roro presses the piece down two times but it stays crooked and does not go in; Roro tilts the head, puzzled. The tray stays still."),
  ("꾹꾹! 안 돼", "R", MEADOW + f"Close view (the camera close on this friend): {D['R']} pushes hard with both short arms on the crooked puzzle piece in the corner of the wooden tray, cheeks puffed, frustrated.", "", True,
   "Roro pushes on the piece two more times, cheeks puffing; the piece still does not go in."),
  ("크앙! 화났어", "R", MEADOW + f"Close view of {D['R']} with puffed red cheeks and a grumpy frown, little steam puffs above the head, stamping one foot, angry but cute, never scary.", "", True,
   "Roro stamps one foot two times and puffs the cheeks, grumpy but cute."),
  ("친구들이 걱정해요", "CRTP", MEADOW + f"{D['R']} sits grumpy with crossed short arms next to {HOLE48}, the last piece lying on the grass beside it; Chiqui, Torong and Pio stand close by looking at Roro with worried, kind faces.", "Exactly four pieces in total.", False,
   "Chiqui, Torong and Pio lean a little toward Roro with worried faces; Roro stays grumpy. The camera stays still."),
  ("바우 할아버지", "BR", MEADOW + f"Close view (the camera close on these two friends): {D['R']} sits on the grass on the LEFT with crossed short arms, still grumpy with puffed cheeks; {D['B']} stands on all four feet on the RIGHT, facing Roro, smiling calmly and kindly at Roro.", "Roro on the LEFT, Grandpa Bau on the RIGHT.", True,
   "Grandpa Bau nods gently at Roro; Roro looks up at him." + B4V + " The camera stays still."),
  ("후~ 숨 쉬기", "BR", MEADOW + f"Close view (the camera close on these two friends): {D['R']} sits on the grass on the LEFT with eyes closed, puts both short arms on the tummy and breathes out slowly, a small soft puff of air coming out of the mouth; {D['B']} stands on all four feet on the RIGHT right next to Roro, eyes closed, breathing slowly together with Roro.", "Roro on the LEFT, Grandpa Bau on the RIGHT.", True,
   "Roro and Grandpa Bau breathe in, then out slowly 'whoo', two times together." + B4V + " The camera stays still."),
  ("하나 둘 셋 후~", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio stand in a row with eyes closed, breathing slowly together, calm faces.", "", False,
   "Everyone breathes in and out slowly two times together on the same spot. The camera stays still."),
  ("마음이 사르르", "R", MEADOW + f"Close view (the camera close on this friend): {D['R']} opens the eyes with a calm, soft smile, the red cheeks gone, relaxed.", "", True,
   "Roro smiles softly and lets the shoulders drop, relaxed."),
  ("빙글 돌려 볼까?", "R", MEADOW + f"{D['R']} sits calmly next to {HOLE48}, holding {PIECE48} up in both short arms and slowly turning it around, looking at it carefully with a curious smile.", "Exactly three pieces in the tray and one piece in Roro's arms.", False,
   "Roro slowly turns the piece around once in the arms, looks at the sun picture on it, and smiles, having an idea. The tray stays still."),
  ("우리 친구도 후~", "C", MEADOW + f"Close view of {D['C']} standing UPRIGHT facing the viewer with both front paws on the tummy, breathing out slowly, inviting the viewer to breathe too.", "", True,
   "Chiqui breathes in, then out slowly, and smiles at the viewer." + CUPV),
  ("쏙! 맞았다", "CRTP", MEADOW + f"Roro sits next to {DONE48}, both short arms up in joy; Chiqui, Torong and Pio stand close around and cheer.", "Exactly four pieces, all in the tray.", False,
   "Roro cheers with both arms up; Chiqui and Pio clap, Torong sways the neck happily; the puzzle stays still. The camera stays still."),
  BAU(MEADOW, "숨을 크게", "stands on all four feet with eyes closed, taking a big calm breath, smiling wisely."),
  ("다 같이 짝짝", "BCRTP", MEADOW + f"All five friends clap and dance around {DONE48}.", "Exactly four pieces, all in the tray.", False,
   "Chiqui, Roro and Pio clap; Torong sways the neck; Grandpa Bau nods; the puzzle stays still." + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 49화 크다 작다! (반대말 놀이) ----------------
EPS["ep49"] = dict(
 title="49화. 크다 작다! — 반대말 놀이", short="크다 작다!", song_id="opposite", song_short="반대말 노래",
 theme="반대말: 크다·작다(토롱·피오), 길다·짧다(토롱 목·로로 팔), 높다·낮다(피오 하늘·치키 땅), 빠르다·느리다(로로·바우).",
 twist="제일 작은 피오가 날아오르니 제일 큰 토롱보다 높이! 작아도 높이 날 수 있어요.",
 bau="브라키오사우루스는 키가 아주아주 컸단다!",
 lines=[("치키","반대말 놀이!",""),("모두","좋아!","♻ 1화 07"),("치키","크다!",""),("치키","작다!",""),("로로","나는 빨라!",""),
        ("바우","나는 느릿느릿~",""),("내레이션","누가 제일 높을까?","뒤에 3초 쉼"),("모두","피오다!",""),("피오","내가 제일 높아!",""),
        ("바우","브라키오사우루스는 키가 아주아주 컸단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("토롱 토롱 크다 (크다!)","피오 피오 작다 (작다!)","크다 작다 (크다 작다!)"),("토롱 목은 길다 (길다!)","로로 팔은 짧다 (짧다!)","길다 짧다 (길다 짧다!)"),
         ("피오 하늘 높다 (높다!)","치키 꼭꼭 낮다 (낮다!)","높다 낮다 (높다 낮다!)"),("로로 다다다 빠르다 (빠르다!)","할아버지 느릿느릿 (느리다~)","빠르다 느리다 (빠르다 느리다!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "크다 작다 (반대말!)", "거꾸로 말해 봐요", "치키치키 반대!"],
 scenes=scenes([
  ("반대말 놀이", "C", MEADOW + f"{D['C']} stands UPRIGHT between one BIG round grey rock on the LEFT and one TINY round grey pebble on the RIGHT, pointing at both with the front paws, curious smile.", "Exactly one big rock and one tiny pebble.", False,
   "Chiqui points at the big rock, then at the tiny pebble, and smiles." + CUPV),
  CHEER(MEADOW),
  ("크다!", "T", MEADOW + f"{D['T']} stands tall on all four feet, the long neck stretched up high, filling the picture from the grass to the sky, proud smile.", "", False,
   "Torong lifts the head up proudly and smiles; all four feet stay on the ground."),
  ("작다!", "P", MEADOW + f"{D['P']} stands on the grass right next to the same BIG round grey rock as in the first scene; the rock is about TWICE as tall as Pio, so Pio looks small and cute beside it, peeking up at the rock. Pio keeps the normal size (Pio is never smaller than a flower).", "Exactly one big grey rock, about twice as tall as Pio.", False,
   "Pio peeks around and hops once on the same spot."),
  ("크다 작다", "TP", MEADOW + f"{D['T']} and {D['P']} stand side by side: Torong is huge and Pio is tiny next to Torong's front foot; they smile at each other.", "", False,
   "Torong lowers the head a little toward Pio; Pio flaps once; both smile. The camera stays still."),
  ("길다!", "T", MEADOW + f"{D['T']} seen from the SIDE, standing on all four feet on the LEFT, stretches the long neck all the way up at a slant toward the RIGHT, fully stretched, to nibble one green leaf at the very top of one TALL palm tree on the RIGHT; Torong's head is high up near the top of the picture, far above the body, and the long stretched neck is easy to see, happy smile. The neck keeps exactly its normal length and thickness from Torong's element image (never longer, never thinner, never like a rope).", "Torong's neck has its normal length, exactly like the element image.", True,
   "Torong sways the long neck gently once; the neck keeps its normal length."),
  ("짧다!", "R", MEADOW + f"{D['R']} holds out the two very short arms, looking at them with a funny surprised face.", "", False,
   "Roro wiggles the short arms and laughs."),
  ("높다!", "P", MEADOW + f"{D['P']} flies high up in the blue sky near the white clouds, wings wide open, tiny over the village.", "", False,
   "Pio glides a little left and right high in the sky, staying the same size."),
  ("낮다!", "C", MEADOW + f"{D['C']} crouches very low on the grass on all four feet, chin close to the ground, peeking with a playful smile.", "", False,
   "Chiqui stays low and wiggles the tail, peeking left and right."),
  ("빠르다!", "R", MEADOW + f"{D['R']} runs fast on the same spot with legs blurred, little dust puffs behind, a big happy grin.", "", False,
   "Roro runs fast on the same spot; little dust puffs pop; Roro does not move across the picture."),
  ("느리다~", "B", MEADOW + f"{D['B']} takes one very slow tiny step on all four feet, sleepy happy smile, eyes half closed.", "", False,
   "Grandpa Bau sways slowly and smiles sleepily on the same spot." + B4V),
  ("누가 제일 높을까?", "C", MEADOW + f"Close view of {D['C']} standing UPRIGHT facing the viewer, one front paw on the chin, thinking, asking the viewer.", "", True,
   "Chiqui tilts the head and waits, then smiles at the viewer." + CUPV),
  ("피오가 제일 높이!", "CRTP", MEADOW + "Pio flies high in the sky above Torong's head; Chiqui, Roro and Torong look up at Pio and cheer.", "", False,
   "Pio flaps above Torong's head on the same spot; the others cheer and point up. The camera stays still."),
  BAU(MEADOW, "아주아주 컸단다", "stands on all four feet next to one very tall palm tree, looking up at its top and smiling wisely."),
  ("다 같이 크게 작게", "BCRTP", MEADOW + "All five friends play together: Chiqui, Roro and Pio stretch up tall on tiptoe; Torong stretches the neck up; Grandpa Bau smiles.", "", False,
   "Everyone stretches up tall, then crouches down small, then laughs, on the same spot." + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))
# ---------------- 50화 공룡알이 톡톡! (50화 특집) ----------------
EGG50 = ("THE SAME one big oval cream-white egg with small ORANGE spots, as tall as Chiqui, sitting in one round nest of soft golden straw on the grass")
EPS["ep50"] = dict(
 title="50화. 공룡알이 톡톡! — 50화 특집", short="공룡알이 톡톡!", song_id="egg50", song_short="알 노래",
 theme="50화 특집: 커다란 알을 따뜻하게 지키고, 귀 기울여 기다리기. 공룡도 알에서 태어나요.",
 twist="알에서 톡톡 소리… 누가 나올까? 하나 둘 셋, 펑! 알록달록 풍선이 쏟아져요 — 바우 할아버지의 50화 깜짝 선물!",
 bau="공룡도 알에서 태어났단다!",
 lines=[("치키","커다란 알이다!",""),("치키","우리가 지켜 주자!",""),("모두","좋아!","♻ 1화 07"),("내레이션","누구 알일까?","뒤에 3초 쉼"),
        ("치키","쉿, 들어 봐!",""),("모두","톡톡!",""),("내레이션","하나, 둘, 셋!",""),("모두","와아~","♻ 1화 15"),
        ("바우","깜짝 선물이란다!",""),("바우","공룡도 알에서 태어났단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("동글동글 커다란 알","누구 알일까? (누구?)","궁금해요 (궁금해!)"),("담요 덮어 따뜻하게","꼭 안아 줘요 (꼭!)","포근포근 (포근!)"),
         ("귀를 대면 톡톡톡","무슨 소리? (톡톡!)","두근두근 (두근!)"),("쩍 하고 금이 가요","하나 둘 셋 (펑!)","깜짝 선물 (와아!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "공룡알이 (톡톡!)", "두근두근 기다려요", "치키치키 톡톡!"],
 scenes=scenes([
  ("커다란 알!", "C", MEADOW + f"{D['C']} stands UPRIGHT next to {EGG50}, both front paws up in amazement, eyes wide.", "Exactly one egg.", False,
   "Chiqui gasps and bounces once on the same spot next to the egg; the egg stays still." + CUPV),
  CHEER(MEADOW),
  ("누구 알일까?", "CRTP", MEADOW + f"Chiqui, Roro, Torong and Pio stand around {EGG50}, looking at it curiously.", "Exactly one egg.", False,
   "The friends tilt their heads curiously; the egg stays still. The camera stays still."),
  ("따뜻하게", "CRTP", MEADOW + f"{D['C']} stands UPRIGHT and gently lays one soft ORANGE blanket over the top of {EGG50}, a caring smile; Roro, Torong and Pio stand around the egg watching kindly.", "Exactly one egg and one blanket.", False,
   "Chiqui pats the blanket on the egg gently two times; the friends smile." + CUPV + " The camera stays still."),
  ("쉿 들어 봐", "CRP", MEADOW + f"Chiqui, Roro and Pio lean close to {EGG50} with one ear near the shell, listening with wide eyes; the ORANGE blanket lies on top of the egg.", "Exactly one egg.", False,
   "The friends listen quietly, then their eyes go wide in surprise. The egg stays in place."),
  ("톡톡!", "", MEADOW + f"Close view of {EGG50}; the ORANGE blanket has slipped down to the nest; one small zigzag crack appears on the shell with tiny 'tap' marks. No characters.", "Exactly one egg.", True,
   "The egg wobbles gently two times; the small crack grows a little longer. Nothing comes out."),
  ("쩍! 금이 갔어", "CRTP", MEADOW + f"{EGG50} has one long zigzag crack across the middle; Chiqui, Roro, Torong and Pio step back a little and gasp with excited faces.", "Exactly one egg.", False,
   "The egg wobbles once; the friends gasp and hold their breath. Nothing comes out. The camera stays still."),
  ("바우 할아버지", "BCRTP", MEADOW + f"{D['B']} stands on all four feet next to {EGG50}, which has one long zigzag crack, smiling wisely and mysteriously; Chiqui, Roro, Torong and Pio turn to look at him with curious faces.", "Exactly one egg.", False,
   "Grandpa Bau nods once and smiles mysteriously; the friends look at him curiously." + B4V + " The camera stays still."),
  ("하나 둘 셋!", "CRTP", MEADOW + f"Chiqui, Roro, Torong and Pio stand in a row in front of {EGG50} with the long crack, counting together with excited faces.", "Exactly one egg.", False,
   "The friends count with three small bounces on the same spot. The egg stays still. The camera stays still."),
  ("펑!", "", MEADOW + f"The top of {EGG50} pops open: colorful paper confetti and exactly five round balloons (ORANGE, YELLOW, GREEN, SKY-BLUE, PURPLE) float up out of the open egg into the sky. No characters.", "Exactly five balloons.", False,
   "The five balloons float up slowly and the confetti flutters down; the egg shell stays in the nest."),
  ("와아~ 풍선!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio cheer with arms and wings up next to the open egg shell in the nest, while five round balloons (ORANGE, YELLOW, GREEN, SKY-BLUE, PURPLE) float above them.", "Exactly five balloons.", False,
   "Everyone cheers and bounces on the same spot; the balloons sway gently. The camera stays still."),
  ("깜짝 선물!", "B", MEADOW + f"{D['B']} stands on all four feet laughing happily next to the open egg shell in the nest, five colorful balloons floating above.", "Exactly five balloons.", False,
   "Grandpa Bau laughs and nods two times; the balloons sway." + B4V),
  ("우리 친구도 축하해!", "C", MEADOW + f"Close view of {D['C']} standing UPRIGHT facing the viewer, both front paws up in celebration, confetti falling.", "", True,
   "Chiqui cheers with both paws up and bounces once." + CUPV),
  BAU(MEADOW, "알에서 태어났단다", "stands on all four feet next to the open egg shell in the nest, smiling wisely."),
  ("다 같이 축하 춤", "BCRTP", MEADOW + "All five friends dance happily together under five floating balloons (ORANGE, YELLOW, GREEN, SKY-BLUE, PURPLE) with confetti.", "Exactly five balloons.", False,
   "Chiqui, Roro and Pio dance; Torong sways the neck; Grandpa Bau wags the tail club; the balloons sway." + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 51화 깜깜해도 괜찮아! (어둠이 무서울 때) ----------------
NIGHT51 = ("INDOORS in Chiqui's cozy round bedroom at NIGHT: soft cream walls, one small round bed with an ORANGE blanket, "
           "one round window on the RIGHT showing the dark blue night sky with little stars, one little mushroom-shaped night lamp on a low wooden shelf next to the bed; "
           "NOT outdoors. " + NODOLL)
LAMPS51 = "one small glowing YELLOW star-shaped lantern and one small glowing SKY-BLUE star-shaped lantern"
EPS["ep51"] = dict(
 title="51화. 깜깜해도 괜찮아! — 어둠이 무서울 때", short="깜깜해도 괜찮아!", song_id="dark", song_short="깜깜 노래",
 theme="불을 끄면 무서운 마음, 그림자의 정체 알기, 작은 불빛과 친구들, 밤하늘 별 보며 편안하게 잠들기.",
 twist="벽에 커다란 긴 그림자! 무서워서 이불 속에 쏙… 똑똑, 창밖에서 \"치키야, 나야!\" 토롱의 긴 목이었어요.",
 bau="밤이 되면 공룡들도 쿨쿨 잤단다!",
 lines=[("치키","잘 자요~",""),("치키","불을 끌까?",""),("내레이션","깜깜!",""),("치키","저건 뭐지?",""),("치키","무서워…",""),
        ("토롱","치키야, 나야!",""),("치키","토롱이었구나!",""),("로로","등불 가져왔어!",""),("내레이션","깜깜해도 괜찮아.",""),
        ("내레이션","우리 친구도 괜찮아.","뒤에 3초 쉼"),("바우","밤이 되면 공룡들도 쿨쿨 잤단다!","바우 할아버지 상식"),("치키","잘 자!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("불을 끄면 깜깜해","어디 있니? (어디?)","두근두근 (두근!)"),("벽에 커다란 그림자","누구일까? (누구?)","토롱이었네 (휴~!)"),
         ("작은 등불 반짝반짝","친구들이 (왔어요!)","포근포근 (포근!)"),("창밖에 별님 반짝","깜깜해도 (괜찮아!)","잘 자요 (쿨쿨!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "깜깜해도 (괜찮아!)", "친구들이 함께해", "치키치키 잘 자!"],
 scenes=scenes([
  ("잘 자요", "C", NIGHT51 + f"{D['C']} lies in the small round bed under the ORANGE blanket, head on the pillow, the mushroom night lamp glowing warmly.", "", False,
   "Chiqui yawns and snuggles under the blanket, then sits up, reaches one front paw to the mushroom night lamp and taps it once; the lamp goes dark."),
  ("불을 끌까?", "C", NIGHT51 + f"{D['C']} sits up in the bed under the ORANGE blanket, reaching one front paw toward the glowing mushroom night lamp to turn it off.", "", False,
   "Chiqui reaches toward the lamp and taps it once; the lamp goes dark."),
  ("깜깜!", "C", NIGHT51.replace("one little mushroom-shaped night lamp", "one little mushroom-shaped night lamp, now turned OFF and dark,") + f"The room is dark blue and dim; only {D['C']}'s big wide eyes peek out from under the ORANGE blanket.", "", False,
   "Chiqui's eyes blink and look left and right nervously under the blanket."),
  ("저건 뭐지?", "", NIGHT51.replace("one little mushroom-shaped night lamp", "one little mushroom-shaped night lamp, turned OFF,") + "The room is dim; on the wall one big long curvy shadow shaped like a long neck with a small round head stretches across. No characters.", "Exactly one shadow.", False,
   "The long shadow on the wall sways slowly left and right; nothing else moves."),
  ("무서워…", "C", NIGHT51.replace("one little mushroom-shaped night lamp", "one little mushroom-shaped night lamp, turned OFF,") + f"{D['C']} hides completely under the ORANGE blanket in the bed, trembling a little; only the tip of the frill shows.", "", False,
   "The blanket trembles a little; Chiqui peeks out once and hides again."),
  ("똑똑!", "T", f"OUTSIDE Chiqui's cave house at night under a starry dark blue sky: {D['T']} stands on all four feet next to the round window of the house, the long neck bent so the smiling head is right at the window, glowing moon behind.", "", False,
   "Torong taps the window gently with the nose two times and smiles; all four feet stay on the ground."),
  ("토롱이었구나!", "CT", NIGHT51.replace("one little mushroom-shaped night lamp", "one little mushroom-shaped night lamp, turned ON and glowing,") + f"{D['C']} sits up in the bed, relieved and laughing, looking at the round window where {D['T']}'s smiling head peeks in from outside.", "Only Torong's head shows at the window.", False,
   "Chiqui laughs with relief and waves one paw; Torong's head nods at the window."),
  ("친구들이 왔어요", "RP", NIGHT51.replace("one little mushroom-shaped night lamp", "one little mushroom-shaped night lamp, turned ON and glowing,") + f"{D['R']} stands at the bedroom doorway holding one small glowing YELLOW star-shaped lantern in both short arms; {D['P']} flies next to Roro holding one small glowing SKY-BLUE star-shaped lantern by its string in the beak.", "Exactly two lanterns.", False,
   "Roro and Pio smile; the two lanterns glow softly."),
  ("반짝반짝", "CRP", NIGHT51.replace("one little mushroom-shaped night lamp", "one little mushroom-shaped night lamp, turned ON and glowing,") + f"The room glows softly with {LAMPS51} on the shelf; Chiqui sits in the bed, Roro and Pio sit on the edge of the bed, all smiling cozily.", "Exactly two star lanterns.", False,
   "The lanterns twinkle softly; the friends smile at each other."),
  ("창밖에 별님", "CRP", NIGHT51.replace("one little mushroom-shaped night lamp", "one little mushroom-shaped night lamp, turned ON and glowing,") + "Chiqui, Roro and Pio look out of the round window at the twinkling stars in the night sky, smiling with wonder.", "", False,
   "The stars twinkle; the friends point at the stars and smile."),
  ("깜깜해도 괜찮아", "C", NIGHT51.replace("one little mushroom-shaped night lamp", "one little mushroom-shaped night lamp, turned ON and glowing softly,") + f"Close view of {D['C']} lying in bed under the ORANGE blanket, smiling peacefully, no longer scared.", "", True,
   "Chiqui smiles and snuggles into the pillow, then turns the face to the viewer and nods gently with a reassuring smile."),
  ("우리 친구도 괜찮아", "C", NIGHT51.replace("one little mushroom-shaped night lamp", "one little mushroom-shaped night lamp, turned ON and glowing softly,") + f"Close view of {D['C']} sitting up in bed facing the viewer with a gentle reassuring smile.", "", True,
   "Chiqui nods gently at the viewer and smiles."),
  ("잘 자, 친구들", "CRP", NIGHT51.replace("one little mushroom-shaped night lamp", "one little mushroom-shaped night lamp, turned ON and glowing softly,") + f"Chiqui lies in the bed under the ORANGE blanket; Roro and Pio stand next to the bed, waving goodnight with one short arm and one wing tip, yawning sleepily; {LAMPS51} glow on the shelf.", "Exactly two star lanterns.", False,
   "Roro and Pio wave goodnight slowly; Chiqui waves back from the bed and yawns."),
  BAU(f"OUTSIDE on the meadow at night under a starry dark blue sky with a round moon: ", "쿨쿨 잤단다", "lies down on the grass with eyes closed, sleeping peacefully, smiling."),
  ("쿨쿨", "C", NIGHT51.replace("one little mushroom-shaped night lamp", "one little mushroom-shaped night lamp, turned ON and glowing softly,") + f"{D['C']} sleeps soundly in the bed under the ORANGE blanket, eyes closed, a tiny happy smile; {LAMPS51} glow on the shelf.", "Exactly two star lanterns.", False,
   "Chiqui breathes slowly in sleep; the lanterns glow softly; nothing else moves."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 52화 빨강 노랑 섞으면? (색깔 섞기) ----------------
PAINT52 = ("one low wooden table on the grass with exactly three small round pots of paint in one row: RED on the LEFT, YELLOW in the MIDDLE, BLUE on the RIGHT, "
           "and one white round mixing bowl in front of them")
EPS["ep52"] = dict(
 title="52화. 빨강 노랑 섞으면? — 색깔 섞기", short="빨강 노랑 섞으면?", song_id="mix", song_short="색깔 노래",
 theme="물감 섞기: 빨강+노랑=주황(치키 색), 노랑+파랑=초록(토롱 색), 빨강+파랑=보라(바우 색). 화면 밖 아이가 먼저 맞히게 쉬어 준다.",
 twist="로로가 '다 섞어 볼래!' — 빙글빙글… 어? 갈색! 다 같이 웃고, 남은 물감으로 커다란 무지개 그림 완성.",
 bau="어떤 공룡은 알록달록 깃털이 있었단다!",
 lines=[("치키","그림 그리자!",""),("모두","좋아!","♻ 1화 07"),("치키","빨강이랑 노랑!",""),("내레이션","무슨 색이 될까?","뒤에 3초 쉼"),
        ("치키","주황이다!",""),("토롱","초록이다!",""),("바우","허허, 보라구나!",""),("로로","다 섞어 볼래!",""),("모두","어? 갈색!",""),
        ("모두","하하하!","♻ 3화 11"),("모두","무지개다!",""),("바우","어떤 공룡은 알록달록 깃털이 있었단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("빨강 노랑 빙글빙글","무슨 색이 될까? (무슨 색?)","주황 치키 (주황!)"),("노랑 파랑 빙글빙글","무슨 색이 될까? (무슨 색?)","초록 토롱 (초록!)"),
         ("빨강 파랑 빙글빙글","무슨 색이 될까? (무슨 색?)","보라 할아버지 (보라!)"),("모두 모두 빙글빙글","무슨 색이 될까? (무슨 색?)","어? 갈색! (하하!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "섞어 섞어 (빙글빙글!)", "알록달록 물감 놀이", "치키치키 짠!"],
 scenes=scenes([
  ("그림 그리자!", "C", MEADOW + f"{D['C']} stands UPRIGHT next to {PAINT52}, holding one paintbrush up in one front paw, excited.", "Exactly three paint pots and one bowl.", False,
   "Chiqui waves the brush a little and bounces once on the same spot." + CUPV),
  CHEER(MEADOW),
  ("빨강 노랑", "C", MEADOW + f"Close view of the white mixing bowl on the table with a swirl of RED and YELLOW paint inside; {D['C']}'s front paw stirs it with the brush.", "", True,
   "The brush stirs the paint in a circle; the red and yellow swirl together and turn ORANGE."),
  ("주황이다!", "C", MEADOW + f"{D['C']} stands UPRIGHT next to {PAINT52}; the mixing bowl is full of bright ORANGE paint; Chiqui points at the bowl and then at the own orange tummy, delighted.", "The bowl is orange.", False,
   "Chiqui points at the bowl, then at the own tummy, and laughs." + CUPV),
  ("노랑 파랑", "CT", MEADOW + f"{PAINT52}; the mixing bowl shows a swirl of YELLOW and BLUE paint; {D['C']} stirs it with the brush; {D['T']} bends the long neck down to watch closely. {NEAR}", "", False,
   "Chiqui stirs; the paint turns GREEN; Torong's eyes go wide." + CUPV),
  ("초록이다!", "T", MEADOW + f"{D['T']} stands on all four feet next to the low wooden table where the white mixing bowl is full of bright GREEN paint, smiling proudly at the same green as the own body.", "The bowl is green.", False,
   "Torong sways the neck happily and smiles; all four feet stay on the ground."),
  ("빨강 파랑", "BC", MEADOW + f"{PAINT52}; the mixing bowl shows a swirl of RED and BLUE paint; {D['C']} stirs it with the brush; {D['B']} watches with raised eyebrows.", "", False,
   "Chiqui stirs; the paint turns PURPLE; Grandpa Bau's eyebrows go up." + CUPV + B4V),
  ("보라다!", "B", MEADOW + f"{D['B']} stands on all four feet next to the low table where the mixing bowl is full of bright PURPLE paint, laughing happily at the same purple as his body.", "The bowl is purple.", False,
   "Grandpa Bau laughs and nods two times." + B4V),
  ("다 섞어 볼래!", "R", MEADOW + f"{D['R']} stands at the low table stirring the white mixing bowl with one paintbrush held in both short arms; the bowl has a big swirl of all colors.", "", False,
   "Roro stirs fast in circles; the colors swirl together and turn muddy BROWN."),
  ("어? 갈색!", "CR", MEADOW + f"{D['C']} and {D['R']} stare at the white mixing bowl full of muddy BROWN paint with funny surprised faces, mouths open.", "The bowl is brown.", False,
   "Chiqui and Roro look at each other, blink, and burst out laughing."),
  ("하하하!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio laugh together next to the low table with the bowl of brown paint; little paint dots are on Chiqui's and Roro's paws.", "", False,
   "Everyone laughs on the same spot. The camera stays still."),
  ("무슨 색이 될까?", "C", MEADOW + f"Close view of {D['C']} standing UPRIGHT facing the viewer, holding up the paintbrush, a curious questioning face.", "", True,
   "Chiqui tilts the head and waits, then smiles at the viewer." + CUPV),
  ("무지개 그림", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio stand proudly around one big white paper lying flat on the grass, painted with a big bright rainbow arc (red, orange, yellow, green, blue, purple); paint dots on their paws.", "Exactly one paper with one rainbow.", False,
   "Everyone cheers next to the rainbow painting on the same spot; the painting stays still. The camera stays still."),
  BAU(MEADOW, "알록달록 깃털", "stands on all four feet next to the big rainbow painting on the grass, smiling wisely."),
  ("다 같이 물감 춤", "BCRTP", MEADOW + "All five friends dance happily together next to the big rainbow painting on the grass.", "", False,
   "Chiqui, Roro and Pio dance; Torong sways the neck; Grandpa Bau nods; the painting stays still." + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 53화 데굴데굴 공놀이! (주고받기) ----------------
BALL53 = "THE SAME one big round soft ball with ORANGE, YELLOW, GREEN, SKY-BLUE and PURPLE stripes"
EPS["ep53"] = dict(
 title="53화. 데굴데굴 공놀이! — 주고받기", short="데굴데굴 공놀이!", song_id="ball", song_short="공놀이 노래",
 theme="동그랗게 모여 공 주고받기: 치키는 코로, 로로는 발로, 토롱은 머리로, 피오는 부리로, 바우는 꼬리로. 차례로 주고받는 즐거움.",
 twist="로로가 뻥! 너무 세게 찼더니 공이 하늘 높이… 어디로 갔지? 콩! 토롱 머리 위에 쏙!",
 bau="아기 공룡들도 함께 뛰어놀았단다!",
 lines=[("치키","공놀이 하자!",""),("모두","좋아!","♻ 1화 07"),("바우","동그랗게 모여라!",""),("치키","데굴데굴~",""),("로로","뻥!",""),
        ("내레이션","어디로 갔을까?","뒤에 3초 쉼"),("토롱","콩! 여기 있네!",""),("모두","하하하!","♻ 3화 11"),("피오","콕콕!",""),("바우","통!",""),
        ("내레이션","우리 친구에게 데굴~","뒤에 3초 쉼"),("바우","아기 공룡들도 함께 뛰어놀았단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("치키 코로 데굴데굴","공이 간다 (데굴!)","받아라 (받았다!)"),("로로 발로 뻥뻥","공이 간다 (뻥!)","받아라 (받았다!)"),
         ("토롱 머리 톡톡","공이 간다 (톡!)","받아라 (받았다!)"),("피오 부리 콕콕","공이 간다 (콕!)","받아라 (받았다!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "데굴데굴 (공놀이!)", "주고 받고 신나요", "치키치키 데굴!"],
 scenes=scenes([
  ("공놀이 하자!", "C", MEADOW + f"{D['C']} stands UPRIGHT next to {BALL53} on the grass, both front paws up, excited.", "Exactly one ball.", False,
   "Chiqui bounces once on the same spot; the ball stays still." + CUPV),
  CHEER(MEADOW),
  ("동그랗게 모여라", "BCRTP", MEADOW + f"All five friends stand in a wide circle on the grass with {BALL53} in the middle, smiling.", "Exactly one ball.", False,
   "Everyone smiles and bounces a little in place; the ball stays still." + B4V + " The camera stays still."),
  ("치키 데굴", "C", MEADOW + f"Close view (the camera close on this friend): {D['C']} stands on all four feet and gently pushes {BALL53} forward with the nose, the ball rolling on the grass.", "Exactly one ball.", True,
   "Chiqui nudges the ball with the nose; the ball rolls a little to the side and stops."),
  ("로로 뻥!", "R", MEADOW + f"Close view (the camera close on this friend): {D['R']} kicks {BALL53} with one foot, the ball flying up off the grass, a big happy grin.", "Exactly one ball.", True,
   "Roro kicks; the ball flies up and out of the top of the frame; Roro looks up."),
  ("높이 높이", "", MEADOW + f"{BALL53} flies high in the blue sky among white clouds over the village. No characters.", "Exactly one ball.", False,
   "The ball floats up a little, then starts to fall; nothing else moves."),
  ("토롱 머리에 콩!", "T", MEADOW + f"Close view (the camera close on this friend): {D['T']} stands on all four feet with {BALL53} sitting on top of the head, eyes looking up at it in funny surprise, smiling.", "Exactly one ball.", True,
   "Torong blinks, looks up at the ball, and smiles; the ball stays balanced; all four feet stay on the ground."),
  ("하하하!", "CRTP", MEADOW + f"Chiqui, Roro and Pio laugh, pointing at {D['T']}, who has {BALL53} on top of the head.", "Exactly one ball.", False,
   "Everyone laughs on the same spot; the ball stays on Torong's head. The camera stays still."),
  ("토롱 톡", "T", MEADOW + f"Close view (the camera close on this friend): {D['T']} bends the long neck down and gently taps {BALL53} on the grass with the forehead, all four feet on the ground.", "Exactly one ball.", True,
   "Torong taps the ball with the head; the ball rolls a little away; all four feet stay on the ground."),
  ("피오 콕콕", "P", MEADOW + f"Close view (the camera close on this friend): {D['P']} stands on the grass and pushes {BALL53}, which is as big as Pio, with the beak.", "Exactly one ball.", True,
   "Pio pushes the ball with the beak two times; the ball rolls a little."),
  ("할아버지 통!", "B", MEADOW + f"Close view (the camera close on this friend): {D['B']} stands on all four feet and gently taps {BALL53} on the grass with his tail club, which is at the back end of his body.", "Exactly one ball.", True,
   "Grandpa Bau swings the tail club gently and taps the ball; the ball rolls a little." + B4V),
  ("우리 친구에게 데굴", "C", MEADOW + f"Close view of {D['C']} on all four feet nudging {BALL53} toward the viewer with the nose, smiling.", "Exactly one ball.", True,
   "Chiqui nudges the ball toward the viewer and waits, smiling."),
  ("주고받기", "CRTP", MEADOW + f"Chiqui, Roro, Torong and Pio stand in a circle passing {BALL53} to each other on the grass, laughing.", "Exactly one ball.", False,
   "The ball rolls slowly from Chiqui toward Roro; everyone laughs on the same spot. The camera stays still."),
  BAU(MEADOW, "함께 뛰어놀았단다", f"stands on all four feet next to {BALL53}, smiling wisely."),
  ("다 같이 공놀이", "BCRTP", MEADOW + f"All five friends play together around {BALL53} on the grass, cheering.", "Exactly one ball.", False,
   "Everyone cheers on the same spot; the ball rolls a little in the middle." + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 54화 물 꿀꺽꿀꺽! (물 마시기) ----------------
CUPS54 = ("one low wooden table on the grass with exactly five small round cups of clear water in one row: ORANGE, YELLOW, GREEN, SKY-BLUE, PURPLE")
FLOWER54 = "one small ORANGE flower in the grass"
EPS["ep54"] = dict(
 title="54화. 물 꿀꺽꿀꺽! — 물 마시기", short="물 꿀꺽꿀꺽!", song_id="water", song_short="물 노래",
 theme="더운 날 신나게 놀고 나면 물 마시기. 친구마다 자기 색 컵. 물을 마시면 힘이 쑥.",
 twist="시들시들 작은 꽃도 목이 말라요! 치키가 물을 주자 꽃이 활짝. 화면 밖 친구도 꿀꺽꿀꺽!",
 bau="공룡들도 물을 꿀꺽꿀꺽 마셨단다!",
 lines=[("모두","더워~",""),("치키","목말라~",""),("바우","물 마시자!",""),("모두","꿀꺽꿀꺽!",""),("모두","힘이 쑥쑥!",""),
        ("치키","꽃이 시들시들…",""),("내레이션","꽃도 목이 마를까?","뒤에 3초 쉼"),("치키","꽃도 꿀꺽!",""),("모두","와아~","♻ 1화 15"),
        ("내레이션","우리 친구도 꿀꺽꿀꺽!","뒤에 3초 쉼"),("바우","공룡들도 물을 꿀꺽꿀꺽 마셨단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("해님 쨍쨍 덥지요","목이 말라요 (말라요!)","물 한 컵 (꿀꺽!)"),("로로도 꿀꺽꿀꺽","토롱도 꿀꺽 (꿀꺽!)","피오도 콕콕 (콕!)"),
         ("물 마시면 힘이 쑥","몸이 튼튼 (튼튼!)","신나게 놀자 (놀자!)"),("시들시들 작은 꽃","물을 주면 (쪼르르!)","활짝 웃어요 (활짝!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "물 마셔요 (꿀꺽꿀꺽!)", "하루에 여러 번", "치키치키 꿀꺽!"],
 scenes=scenes([
  ("해님 쨍쨍", "CRTP", MEADOW + "Under a very bright hot sun, Chiqui, Roro, Torong and Pio stand on the meadow looking hot and tired, tongues out a little, little sweat drops.", "", False,
   "The friends fan themselves and pant a little on the same spot. The camera stays still."),
  ("목말라~", "C", MEADOW + f"Close view of {D['C']} with the tongue sticking out, looking thirsty under the hot sun, a funny face.", "", True,
   "Chiqui pants with the tongue out and droops the head a little."),
  BAU(MEADOW, "물 마시자!", f"stands on all four feet next to {CUPS54}, smiling kindly."),
  ("다섯 컵", "", MEADOW + f"Close view of {CUPS54}, the water sparkling in the sun. No characters.", "Exactly five cups, colors exactly as written.", True,
   "The water in the cups sparkles gently; nothing else moves."),
  ("치키 꿀꺽", "C", MEADOW + f"Close view (the camera close on this friend): {D['C']} stands UPRIGHT next to the low table, drinking from the ORANGE cup held in both front paws, eyes closed happily.", "Exactly one cup in Chiqui's paws.", True,
   "Chiqui drinks two gulps and says ahh with a happy face." + CUPV),
  ("로로도 꿀꺽", "R", MEADOW + f"Close view (the camera close on this friend): {D['R']} stands next to the low table drinking from the YELLOW cup held in both short arms.", "Exactly one cup in Roro's arms.", True,
   "Roro drinks two gulps and smiles."),
  ("토롱도 꿀꺽", "T", MEADOW + f"Close view (the camera close on this friend): {D['T']} bends the long neck down and drinks from the GREEN cup standing on the low wooden table, never holding it. {NEAR}", "Exactly one green cup on the table.", True,
   "Torong sips from the cup on the table two times and smiles; all four feet stay on the ground."),
  ("피오 콕콕", "P", MEADOW + f"Close view (the camera close on this friend): {D['P']} stands on the low wooden table and sips water from the SKY-BLUE cup with the beak.", "Exactly one sky-blue cup.", True,
   "Pio sips with the beak two times and flaps once happily."),
  ("할아버지 꿀꺽", "B", MEADOW + f"Close view (the camera close on this friend): {D['B']} stands on all four feet and drinks from the PURPLE cup standing on the low wooden table in front of his mouth, never holding it.", "Exactly one purple cup on the table.", True,
   "Grandpa Bau sips from the cup on the table two times and smiles." + B4V),
  ("힘이 쑥쑥!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio jump happily on the meadow, full of energy, big smiles.", "", False,
   "Everyone jumps once on the same spot and lands softly, cheering. The camera stays still."),
  ("꽃이 시들시들", "C", MEADOW + f"{D['C']} on all four feet looks sadly at {FLOWER54}, which droops down, wilting.", "Exactly one flower.", False,
   "Chiqui tilts the head sadly; the flower droops a little more."),
  ("꽃도 꿀꺽", "C", MEADOW + f"{D['C']} stands UPRIGHT and gently pours water from the ORANGE cup onto {FLOWER54}.", "Exactly one flower and one cup.", False,
   "Water pours gently onto the flower; the flower slowly lifts up." + CUPV),
  ("활짝!", "C", MEADOW + f"{FLOWER54} stands up straight and blooms wide open with little sparkles; {D['C']} on all four feet beams with delight.", "Exactly one flower.", False,
   "The flower opens a little wider with sparkles; Chiqui laughs happily."),
  BAU(MEADOW, "꿀꺽꿀꺽 마셨단다", "stands on all four feet next to a small clear blue pond, smiling wisely."),
  ("다 같이 꿀꺽 춤", "BCRTP", MEADOW + f"All five friends dance happily next to {CUPS54}.", "Exactly five cups.", False,
   "Chiqui, Roro and Pio dance; Torong sways the neck; Grandpa Bau nods; the cups stay still." + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 55화 봄이 왔어요! (봄 찾기) ----------------
SPRING = ("On a sunny SPRING meadow of the volcano-island village with palm trees, round cave houses and the far volcano; "
          "the grass is plain fresh green with no lines or paths drawn on it; small spring flowers dot the grass. ")
EPS["ep55"] = dict(
 title="55화. 봄이 왔어요! — 봄 찾기", short="봄이 왔어요!", song_id="spring", song_short="봄 노래",
 theme="봄 찾기: 새싹, 꽃봉오리가 활짝, 연두 잎, 따뜻한 바람. 눈·코·귀로 봄을 느껴요.",
 twist="피오 날개 바람에 꽃잎이 팔랑팔랑 — 꽃잎 비가 내려요! 화면 밖 친구는 어떤 꽃이 좋아?",
 bau="공룡 시대에도 꽃이 피었단다!",
 lines=[("치키","봄 냄새가 나!",""),("치키","봄 찾으러 가자!",""),("모두","좋아!","♻ 1화 07"),("치키","새싹이 쏙!",""),("로로","꽃이 활짝!",""),
        ("토롱","잎이 반짝!",""),("피오","바람이 따뜻해!",""),("내레이션","어? 꽃잎이 팔랑팔랑!",""),("모두","꽃잎 비다!",""),
        ("내레이션","우리 친구는 어떤 꽃이 좋아?","뒤에 3초 쉼"),("바우","공룡 시대에도 꽃이 피었단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("땅속에서 쏙쏙쏙","새싹이 (안녕!)","봄이 왔어요 (봄!)"),("꽁꽁 봉오리 활짝","꽃이 피었어요 (활짝!)","알록달록 (알록!)"),
         ("나무에 연두 잎","반짝반짝 (반짝!)","바람도 살랑 (살랑!)"),("꽃잎이 팔랑팔랑","꽃잎 비 (와아!)","봄이 좋아 (좋아!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "봄이 왔어요 (봄!)", "살랑살랑 바람 타고", "치키치키 봄!"],
 scenes=scenes([
  ("봄 냄새", "C", SPRING + f"{D['C']} stands on all four feet sniffing the warm air with eyes closed and a happy smile.", "", False,
   "Chiqui sniffs two times and smiles dreamily."),
  CHEER(MEADOW),
  ("새싹이 쏙", "C", SPRING + f"Close view of one tiny light-green sprout with two little leaves poking out of the soil; {D['C']} on all four feet peeks at it with wide happy eyes.", "Exactly one sprout.", True,
   "The sprout wiggles its two leaves gently; Chiqui gasps happily."),
  ("꽃봉오리", "R", SPRING + f"{D['R']} looks closely at one closed round YELLOW flower bud on a stem, curious.", "Exactly one bud.", False,
   "Roro leans in and tilts the head; then the bud slowly opens into one big YELLOW flower and Roro jumps a little in delight and claps the short arms."),
  ("활짝!", "R", SPRING + f"{D['R']} jumps back in delight as one big YELLOW flower blooms wide open in front of Roro.", "Exactly one big yellow flower.", False,
   "The flower opens a little wider; Roro claps the short arms."),
  ("꽃 냄새", "R", SPRING + f"{D['R']} sniffs the big YELLOW flower with eyes closed, a happy smile.", "Exactly one big yellow flower.", False,
   "Roro sniffs and sways happily."),
  ("연두 잎 반짝", "T", SPRING + f"{D['T']} stands on all four feet next to one tall tree covered in fresh light-green new leaves, the head among the leaves, smiling.", "", False,
   "Torong sways the head gently among the leaves; the leaves shimmer; all four feet stay on the ground."),
  ("따뜻한 바람", "P", SPRING + f"{D['P']} glides in the sunny sky with wings wide open, enjoying the warm breeze, eyes half closed happily.", "", False,
   "Pio glides a little left and right, staying the same size."),
  ("꽃잎이 팔랑팔랑", "CP", SPRING + f"{D['P']} flaps above a blooming pink tree; soft pink petals flutter down around {D['C']}, who looks up amazed.", "", False,
   "Pio flaps; pink petals flutter down slowly; Chiqui looks up and smiles."),
  ("꽃잎 비다!", "CRTP", SPRING + "Chiqui, Roro, Torong and Pio laugh with joy in a shower of soft pink petals falling from a blooming tree.", "", False,
   "The petals fall slowly; everyone laughs on the same spot. The camera stays still."),
  ("봄 찾았다!", "CRTP", SPRING + "Chiqui, Roro, Torong and Pio stand in a flower field with ORANGE, YELLOW, GREEN-white, SKY-BLUE and PURPLE flowers, cheering.", "", False,
   "Everyone cheers on the same spot; the flowers sway. The camera stays still."),
  ("어떤 꽃이 좋아?", "C", SPRING + f"Close view of {D['C']} standing UPRIGHT facing the viewer holding one small ORANGE flower, asking the viewer.", "Exactly one flower in Chiqui's paw.", True,
   "Chiqui smells the flower, then smiles and waits at the viewer." + CUPV),
  ("꽃밭에서", "CRTP", SPRING + "Chiqui, Roro, Torong and Pio sit happily in the middle of a colorful flower field, smiling at each other.", "", False,
   "Everyone sways gently and smiles; the flowers sway. The camera stays still."),
  BAU(SPRING, "꽃이 피었단다", "stands on all four feet among spring flowers, one flower near his nose, smiling wisely."),
  ("다 같이 봄 춤", "BCRTP", SPRING + "All five friends dance happily together in the spring flower field.", "", False,
   "Chiqui, Roro and Pio dance; Torong sways the neck; Grandpa Bau wags the tail club." + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 56화 봄 소풍 가요! (깨끗하게 놀기) ----------------
HILL56 = ("On a sunny grassy hill of the volcano-island village with spring flowers, palm trees and the far volcano; the grass is plain green with no lines or paths drawn on it. ")
BLANKET56 = "one big ORANGE-and-white checkered picnic blanket on the grass"
BIN56 = "one round GREEN bin with an open top standing on the grass"
TRASH56 = "exactly three pieces of crumpled white paper and one apple core lying on the grass"
EPS["ep56"] = dict(
 title="56화. 봄 소풍 가요! — 깨끗하게 놀기", short="봄 소풍 가요!", song_id="picnic", song_short="소풍 노래",
 theme="봄 소풍, 맛있는 도시락, 놀고 난 자리 깨끗하게(쓰레기는 쓰레기통에). 하나 줍고 둘 줍고.",
 twist="다 주웠다! 했는데 덤불 꼭대기에 종이가 하나 더… 키 큰 토롱이 쭈욱! 쓰레기통에 쏙.",
 bau="공룡들도 둥지의 알을 소중히 지켰단다!",
 lines=[("치키","소풍 가자!",""),("모두","좋아!","♻ 1화 07"),("모두","잘 먹겠습니다!",""),("로로","배불러~",""),("치키","어? 쓰레기다.",""),
        ("바우","우리가 논 곳은 깨끗하게!",""),("모두","하나 줍고, 둘 줍고!",""),("피오","저기 위에도!",""),("토롱","내가 할게!",""),("모두","깨끗해!",""),
        ("내레이션","우리 친구도 쓰레기는 쏙!","뒤에 3초 쉼"),("바우","공룡들도 둥지의 알을 소중히 지켰단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("돗자리 펴고 앉아","도시락 (냠냠!)","맛있어요 (맛있어!)"),("어? 쓰레기 떨어졌네","하나 줍고 (하나!)","둘 줍고 (둘!)"),
         ("높은 곳은 토롱이","쭈욱 (쭈욱!)","쏙 넣어요 (쏙!)"),("깨끗한 풀밭","꽃도 웃어요 (방긋!)","또 놀러 와요 (또 와요!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "봄 소풍 (가요!)", "깨끗하게 놀아요", "치키치키 소풍!"],
 scenes=scenes([
  ("소풍 가자!", "C", HILL56 + f"{D['C']} stands UPRIGHT on top of the grassy hill with both front paws up, excited, looking at the view.", "", False,
   "Chiqui bounces once on the same spot and cheers." + CUPV),
  CHEER(MEADOW),
  ("돗자리 펴요", "CRTP", HILL56 + f"Chiqui, Roro, Torong and Pio stand around {BLANKET56}, smiling.", "Exactly one blanket.", False,
   "The friends smile and bounce a little around the blanket. The camera stays still."),
  ("도시락 냠냠", "BCRTP", HILL56 + f"All five friends sit and stand around {BLANKET56} eating round rice balls from one big round plate in the middle; Torong and Grandpa Bau eat from the plate with the mouth.", "Exactly one plate.", False,
   "Everyone takes one bite and smiles with full cheeks." + B4V + " The camera stays still."),
  ("배불러~", "R", HILL56 + f"Close view (the camera close on this friend): {D['R']} sits on the blanket patting the round full tummy with both short arms, a happy sleepy smile.", "", True,
   "Roro pats the tummy two times and sighs happily."),
  ("어? 쓰레기", "C", HILL56 + f"{D['C']} on all four feet frowns a little, looking at {TRASH56} next to the blanket.", "Exactly three papers and one apple core.", False,
   "Chiqui tilts the head and frowns a little; the trash stays still."),
  BAU(HILL56, "깨끗하게!", f"stands on all four feet next to {BIN56}, smiling kindly, as if saying 'let's clean up'."),
  ("하나 줍고", "C", HILL56 + f"Close view (the camera close on this friend): {D['C']} stands UPRIGHT next to {BIN56}, dropping one crumpled white paper into it with one front paw.", "Exactly one bin.", True,
   "Chiqui drops the paper into the bin and smiles proudly." + CUPV),
  ("둘 줍고", "R", HILL56 + f"Close view (the camera close on this friend): {D['R']} drops one apple core into {BIN56} with both short arms, smiling.", "Exactly one bin.", True,
   "Roro drops the apple core into the bin and claps once."),
  ("토롱은 입으로", "T", HILL56 + f"Close view (the camera close on this friend): {D['T']} bends the long neck down and drops one crumpled white paper from the mouth into {BIN56}, all four feet on the ground.", "Exactly one bin.", True,
   "Torong lets go of the paper into the bin and smiles; all four feet stay on the ground."),
  ("저기 위에도!", "PT", HILL56 + f"One crumpled white paper is stuck on top of a tall round bush; {D['P']} flies next to it pointing with one wing tip; {D['T']} stretches the long neck up toward it.", "Exactly one paper on the bush.", False,
   "Torong gently picks the paper off the bush with the mouth; Pio cheers; all four feet stay on the ground."),
  ("깨끗해!", "CRTP", HILL56 + f"Chiqui, Roro, Torong and Pio stand proudly on the clean grass next to {BLANKET56} and {BIN56}; no trash anywhere on the grass.", "No trash on the grass.", False,
   "Everyone cheers on the same spot. The camera stays still."),
  ("우리 친구도 쏙!", "C", HILL56 + f"Close view of {D['C']} standing UPRIGHT next to {BIN56}, facing the viewer, pointing at the bin with one paw.", "", True,
   "Chiqui points at the bin, then smiles and waits at the viewer." + CUPV),
  BAU(HILL56, "알을 소중히 지켰단다", "stands on all four feet next to one round neat nest of golden straw on the grass with exactly three smooth cream eggs inside it, smiling wisely and looking gently at the eggs."),
  ("다 같이 소풍 춤", "BCRTP", HILL56 + f"All five friends dance happily on the clean grassy hill next to {BLANKET56}.", "", False,
   "Chiqui, Roro and Pio dance; Torong sways the neck; Grandpa Bau wags the tail club." + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 57화 보물 지도를 따라가요! (위·아래·앞·뒤) ----------------
STAR57 = "one small shiny golden star-shaped stone"
MAP57 = "one unrolled paper treasure map with a dotted path drawn from a rock to a leaf to a tree to a round door and ending at a red X mark, no words"
CHEST57 = "one small wooden treasure chest"
EPS["ep57"] = dict(
 title="57화. 보물 지도를 따라가요! — 위 아래 앞 뒤", short="보물 지도를 따라가요!", song_id="treasure", song_short="보물 노래",
 theme="자리 말 배우기: 위·아래·뒤·앞. 지도 따라 반짝 별 돌 넷을 찾고 보물 상자 열기.",
 twist="별 돌을 다 모아 X 표시로! 상자를 열자 친구 색 반짝 메달 다섯 개 — 하나씩 목에 걸어요.",
 bau="땅속 공룡 뼈 화석은 진짜 보물이란다!",
 lines=[("치키","보물 지도다!",""),("모두","좋아!","♻ 1화 07"),("내레이션","바위 위에!",""),("로로","찾았다!",""),("내레이션","잎 아래에!",""),
        ("내레이션","나무 뒤에!",""),("내레이션","문 앞에!",""),("내레이션","별은 어디에 있을까?","뒤에 3초 쉼"),("모두","보물이다!",""),("모두","와아~","♻ 1화 15"),
        ("바우","땅속 공룡 뼈 화석은 진짜 보물이란다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("커다란 바위 위에","반짝반짝 (위에!)","별을 찾았다 (찾았다!)"),("동그란 잎 아래에","반짝반짝 (아래!)","별을 찾았다 (찾았다!)"),
         ("키 큰 나무 뒤에","반짝반짝 (뒤에!)","별을 찾았다 (찾았다!)"),("동굴 집 문 앞에","반짝반짝 (앞에!)","별을 찾았다 (찾았다!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "위 아래 (앞 뒤!)", "보물 지도 따라가요", "치키치키 보물!"],
 scenes=scenes([
  ("보물 지도!", "C", MEADOW + f"{D['C']} stands UPRIGHT holding {MAP57} open in both front paws, eyes sparkling.", "Exactly one map.", False,
   "Chiqui holds the map up and bounces once with excitement." + CUPV),
  CHEER(MEADOW),
  ("지도를 봐요", "", f"Close view of {MAP57}, lying on the grass. No characters.", "Exactly one map.", True,
   "A soft sparkle runs along the dotted path to the red X; nothing else moves."),
  ("바위 위에!", "R", MEADOW + f"{D['R']} points up with both short arms at {STAR57} sitting ON TOP of one big round grey rock, excited.", "Exactly one star stone.", False,
   "Roro points and hops once; the star stone twinkles."),
  ("잎 아래에!", "P", MEADOW + f"{D['P']} lifts one big round green leaf with the beak, showing {STAR57} hidden UNDER the leaf on the grass.", "Exactly one star stone.", False,
   "Pio lifts the leaf a little higher; the star stone twinkles."),
  ("나무 뒤에!", "T", MEADOW + f"{D['T']} peeks around BEHIND one tall palm tree with the long neck, smiling at {STAR57} on the grass behind the tree.", "Exactly one star stone.", False,
   "Torong peeks and smiles; the star stone twinkles; all four feet stay on the ground."),
  ("문 앞에!", "C", MEADOW + f"{D['C']} on all four feet finds {STAR57} on the grass IN FRONT OF one round green door of a cave house, delighted.", "Exactly one star stone.", False,
   "Chiqui gasps and wiggles the tail; the star stone twinkles."),
  ("별이 넷", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio stand around exactly four small shiny golden star-shaped stones lined up in a row on the grass, cheering.", "Exactly four star stones.", False,
   "The four star stones twinkle; everyone cheers on the same spot. The camera stays still."),
  ("X 표시", "CRTP", MEADOW + f"Chiqui, Roro, Torong and Pio gasp at {CHEST57} half-buried in a small patch of soft sand at a red X mark on the meadow.", "Exactly one chest.", False,
   "The friends lean in with excited faces; the chest stays still. The camera stays still."),
  ("상자를 열어요", "CRTP", MEADOW + f"{D['C']} stands UPRIGHT and lifts the lid of {CHEST57} with both front paws; a warm golden glow shines out; Roro, Torong and Pio lean in around the chest with amazed faces.", "Exactly one chest.", False,
   "Chiqui lifts the lid slowly; the golden glow grows brighter; the friends gasp." + CUPV + " The camera stays still."),
  ("반짝 메달", "", MEADOW + f"Close view inside the open {CHEST57}: exactly five round shiny medals on ribbons, in ORANGE, YELLOW, GREEN, SKY-BLUE and PURPLE. No characters.", "Exactly five medals.", True,
   "The medals shine and sparkle softly; nothing else moves."),
  ("보물이다!", "BCRTP", MEADOW + "All five friends wear one round shiny medal on a ribbon around the neck in their own body color, cheering proudly next to the open chest.", "Exactly five medals, one each.", False,
   "Everyone cheers and the medals sparkle." + B4V + " The camera stays still."),
  ("별은 어디에?", "C", MEADOW + f"Close view of {D['C']} standing UPRIGHT facing the viewer, one front paw shading the eyes like searching, a playful questioning face, wearing an ORANGE medal.", "", True,
   "Chiqui looks left and right, then smiles and waits at the viewer." + CUPV),
  BAU(MEADOW, "진짜 보물", "stands on all four feet wearing a PURPLE medal, next to one cream-colored fossil bone peeking out of the soil, smiling wisely."),
  ("다 같이 보물 춤", "BCRTP", MEADOW + "All five friends dance together wearing their own-color medals next to the open treasure chest.", "Exactly five medals.", False,
   "Chiqui, Roro and Pio dance; Torong sways the neck; Grandpa Bau nods; the medals sparkle." + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 58화 공룡은 뭘 먹을까? (공룡 상식 특집) ----------------
TREE58 = "one very tall tree with leafy branches high up"
FERN58 = "a patch of low green fern plants on the grass"
APPLE58 = "one apple tree with shiny red apples"
EPS["ep58"] = dict(
 title="58화. 공룡은 뭘 먹을까? — 공룡 상식 특집", short="공룡은 뭘 먹을까?", song_id="food58", song_short="먹이 노래",
 theme="공룡 상식: 키 큰 브라키오사우루스는 높은 나뭇잎, 트리케라톱스·안킬로사우루스는 낮은 풀. 화면 밖 아이가 먼저 맞히게 쉬어 준다.",
 twist="로로는 사과가 좋아! 그런데 사과가 높이 높이… 피오가 슝 날아가 하나씩 톡톡 따 줘요. 그럼 진짜 티라노사우루스는? 바우 할아버지: \"고기를 먹었단다. 우리 로로는 사과도 냠냠!\"",
 bau="진짜 티라노사우루스는 고기를 먹었단다!",
 lines=[("모두","배고파~",""),("치키","맛있는 거 찾자!",""),("모두","좋아!","♻ 1화 07"),("바우","공룡은 뭘 먹었을까?",""),
        ("내레이션","높은 나뭇잎은 누가 먹을까?","뒤에 3초 쉼"),("모두","토롱!",""),("내레이션","낮은 풀은 누가 먹을까?","뒤에 3초 쉼"),("모두","치키!",""),
        ("로로","나는 사과!",""),("피오","내가 따 줄게!",""),("내레이션","우리 친구는 뭘 좋아해?","뒤에 3초 쉼"),
        ("바우","진짜 티라노사우루스는 고기를 먹었단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("높이 높이 나뭇잎","누가 먹을까? (누구?)","토롱이 쭈욱 (쭈욱!)"),("낮게 낮게 고사리","누가 먹을까? (누구?)","치키가 냠냠 (냠냠!)"),
         ("동글동글 빨간 사과","누가 먹을까? (누구?)","로로가 와앙 (와앙!)"),("높은 가지 사과는","누가 딸까? (누구?)","피오가 슝 (슝!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "공룡은 뭘 (먹을까?)", "냠냠 쩝쩝 맛있게", "치키치키 냠냠!"],
 scenes=scenes([
  ("배고파~", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio stand in a row holding their tummies, hungry funny faces, little rumble lines near their tummies.", "", False,
   "The friends rub their tummies and make funny hungry faces on the same spot. The camera stays still."),
  CHEER(MEADOW),
  BAU(MEADOW, "뭘 먹었을까?", f"stands on all four feet between {TREE58} on the LEFT and {FERN58} on the RIGHT, eyebrows raised playfully as if asking a question."),
  ("높은 나뭇잎", "", MEADOW + f"Looking up at the top of {TREE58} with fresh green leaves against the blue sky. No characters.", "", False,
   "The leaves rustle gently in the breeze; nothing else moves."),
  ("토롱 쭈욱 냠", "T", MEADOW + f"{D['T']} stands on all four feet next to {TREE58} and munches leaves from the high branches with the mouth, happy face.", "", False,
   "Torong chews the leaves slowly and smiles; the neck keeps its normal length; all four feet stay on the ground."),
  ("낮은 풀", "", MEADOW + f"Close view of {FERN58}. No characters.", "", True,
   "The ferns sway gently; nothing else moves."),
  ("치키 냠냠", "C", MEADOW + f"{D['C']} stands on all four feet and munches the low green fern leaves with the mouth, happy face.", "", False,
   "Chiqui chews and nods happily; all four feet stay on the ground."),
  ("할아버지도 냠", "B", MEADOW + f"{D['B']} stands on all four feet and munches low green fern leaves with the mouth, smiling.", "", False,
   "Grandpa Bau chews slowly and smiles." + B4V),
  ("로로는?", "R", MEADOW + f"{D['R']} stands with one short arm on the chin, thinking, looking up at {APPLE58}.", "", False,
   "Roro tilts the head, thinking, then smiles brightly."),
  ("빨간 사과", "R", MEADOW + f"{D['R']} stands under {APPLE58}, reaching up with both short arms but the apples are much too high, a funny face.", "", False,
   "Roro hops on the same spot, reaching up, but cannot reach; Roro laughs."),
  ("피오가 슝", "P", MEADOW + f"{D['P']} flies up next to the high branches of {APPLE58} and picks one shiny red apple with the beak.", "", False,
   "Pio pulls the apple off the branch with the beak and flaps, staying the same size."),
  ("다 같이 냠냠", "CRTP", MEADOW + "Chiqui, Roro and Pio each hold one shiny red apple and take a bite, while Torong munches leaves from a tall tree, all smiling.", "", False,
   "Everyone takes one bite and smiles with full cheeks; a small bite mark shows on each apple. The camera stays still."),
  ("뭘 좋아해?", "C", MEADOW + f"Close view of {D['C']} standing UPRIGHT facing the viewer, one front paw on the chin, asking the viewer what they like to eat.", "", True,
   "Chiqui tilts the head and waits, then smiles at the viewer." + CUPV),
  BAU(MEADOW, "티라노는 고기를", f"stands on all four feet next to {APPLE58}, smiling wisely and kindly, one eyebrow raised as if telling a fun fact."),
  ("다 같이 냠냠 춤", "BCRTP", MEADOW + f"All five friends dance happily together next to {APPLE58}.", "", False,
   "Chiqui, Roro and Pio dance; Torong sways the neck; Grandpa Bau wags the tail club." + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 59화 셋이서 콩콩콩! (침대에서 뛰지 않아요) ----------------
# (2026-11-27, 사용자: 59·60화를 완전히 새 내용으로) 인기 동요의 '침대에서 뛰다 쿵' 세기 놀이 소재만 참고, 이야기는 새로.
# 침대가 작아서 치키·로로·피오 셋만 뛴다. 토롱(너무 큼)은 침대 옆에 서서 걱정, 바우는 문에서 등장 → 장면마다 같은 자리.
ROOM59 = NIGHT51.replace("one little mushroom-shaped night lamp", "one little mushroom-shaped night lamp, turned ON and glowing,")
TOR59 = f"{D['T']} stands on all four feet on the floor at the LEFT side of the bed, too big for the bed, watching with a worried face"
RUG59 = "one round soft cream rug on the floor at the RIGHT side of the bed"
EPS["ep59"] = dict(
 title="59화. 셋이서 콩콩콩! — 침대에서 뛰지 않아요", short="셋이서 콩콩콩!", song_id="bounce59", song_short="콩콩 노래",
 theme="잘 시간에 침대에서 콩콩 뛰다가 하나씩 쿵(3→2→1→0 거꾸로 세기). 침대는 자는 곳, 뛰는 건 밖에서. 다친 데 없이 살짝 쿵, 무섭지 않게.",
 twist="셋이 콩콩 뛰다 로로가 쿵! 피오가 쿵! 마지막 치키도 쿵! 아무도 없는 침대… 다음 날 아침, 바우 할아버지와 풀밭에서 다 같이 콩콩 — 토롱도 같이!",
 bau="공룡 화석에도 다친 자국이 있단다!",
 lines=[("내레이션","잘 시간이에요.",""),("치키","더 놀고 싶어!",""),("모두","콩콩 콩콩!",""),("로로","쿵! 아야!",""),("바우","침대에서 콩콩 안 돼요!",""),
        ("내레이션","몇 명이 남았을까?","뒤에 3초 쉼"),("모두","아무도 없어요!",""),("바우","침대는 자는 곳!",""),("모두","밖에서 콩콩!",""),
        ("바우","공룡 화석에도 다친 자국이 있단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("세 친구가 콩콩콩","침대 위에서 (콩콩!)","로로가 쿵 (아야!)"),("두 친구가 콩콩콩","침대 위에서 (콩콩!)","피오가 쿵 (아야!)"),
         ("한 친구가 콩콩콩","침대 위에서 (콩콩!)","치키도 쿵 (아야!)"),("아무도 안 뛰어요","침대에서는 (안 돼!)","쉿 잘 자요 (쿨쿨!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "침대에서 콩콩 (안 돼요!)", "콩콩은 밖에서 해요", "치키치키 콩콩!"],
 scenes=scenes([
  ("잘 시간이에요", "C", ROOM59 + f"{D['C']} sits wide awake on the small round bed under the ORANGE blanket, eyes sparkling, not sleepy at all.", "", False,
   "Chiqui wiggles under the blanket and grins, wide awake, on the same spot."),
  ("친구들이 왔어요", "CRTP", ROOM59 + f"{D['C']}, {D['R']} and {D['P']} sit together on the small round bed in a row, giggling; {TOR59}; {RUG59}.", "", False,
   "Chiqui, Roro and Pio giggle and bounce a little sitting on the bed; Torong smiles but stays beside the bed. The camera stays still."),
  ("콩콩 뛰자!", "CRTP", ROOM59 + f"Chiqui, Roro and Pio stand UPRIGHT on the bed and jump happily, all three in the air together above the mattress; {TOR59}; {RUG59}.", "Exactly three friends on the bed.", False,
   "Chiqui, Roro and Pio bounce up and down on the bed two times, laughing; Torong watches beside the bed with all four feet on the floor. The camera stays still."),
  ("셋이 콩콩", "CRP", ROOM59 + "Close view of the bed: Chiqui, Roro and Pio bounce high in the air side by side, laughing, the blanket flying.", "Exactly three friends.", True,
   "The three friends bounce two times on the same spot, laughing."),
  ("쿵! 아야", "R", ROOM59 + f"{D['R']} sits on {RUG59} next to the bed, rubbing the head with one short arm, one small round pink bump on the head, a funny surprised face, not hurt badly.", "Only one Roro.", False,
   "Roro rubs the head two times, then giggles; Roro stays sitting on the rug."),
  ("침대에서 콩콩 안 돼요!", "BCRTP", ROOM59 + f"{D['B']} stands on all four feet in the doorway on the far LEFT, shaking the head kindly but firmly; Chiqui and Pio stop jumping and stand still on the bed; Roro sits on {RUG59}; {TOR59}.", "", False,
   "Grandpa Bau shakes the head slowly two times; Chiqui and Pio freeze on the bed and look at him; Roro rubs the head." + B4V + " The camera stays still."),
  ("둘이 콩콩", "CRTP", ROOM59 + f"Chiqui and Pio jump on the bed again, both in the air, giggling; Roro sits on {RUG59} watching; {TOR59}.", "Exactly two friends on the bed.", False,
   "Chiqui and Pio bounce two times on the bed; Roro claps on the rug; Torong watches with all four feet on the floor. The camera stays still."),
  ("쿵! 피오", "P", ROOM59 + f"{D['P']} sits on the soft pillow at the end of the bed, a little dizzy, three tiny cartoon stars circling above the head, one small pink bump on the crest.", "Only one Pio.", True,
   "The three tiny stars circle once above Pio's head; Pio blinks and giggles."),
  ("혼자 콩콩", "CRTP", ROOM59 + f"Only Chiqui jumps on the bed now, high in the air; Roro and Pio sit side by side on {RUG59} watching; {TOR59}.", "Exactly one friend on the bed.", False,
   "Chiqui bounces two times on the bed; Roro and Pio watch from the rug and gasp. The camera stays still."),
  ("쿵! 치키", "C", ROOM59 + f"{D['C']} sits on {RUG59} next to the bed, rubbing the frill with one front paw, one small round pink bump on the head, a sheepish smile.", "Only one Chiqui.", True,
   "Chiqui rubs the head and gives a sheepish giggle, sitting on the rug."),
  ("아무도 없어요", "BCRTP", ROOM59 + f"The small round bed is EMPTY and neat; Chiqui, Roro and Pio sit in a row on {RUG59}, each with a tiny pink bump, smiling sheepishly; {D['B']} stands on all four feet in the doorway on the far LEFT smiling kindly; {TOR59.replace('watching with a worried face', 'smiling with relief')}.", "Nobody on the bed.", False,
   "Everyone looks at the empty bed and laughs softly; Grandpa Bau nods." + B4V + " The camera stays still."),
  BAU(ROOM59, "침대는 자는 곳", "stands on all four feet next to the small round bed and points the nose at the soft pillow, smiling kindly, as if saying the bed is for sleeping."),
  ("밖에서 콩콩!", "BCRTP", MEADOW + "The next sunny morning, all five friends hop happily together on the soft green grass: Chiqui, Roro and Pio jump high, Torong bobs the long neck up and down with all four feet on the grass, Grandpa Bau stomps happily with all four feet on the grass.", "", False,
   "Chiqui, Roro and Pio jump two times on the same spot; Torong bobs the neck; Grandpa Bau stomps." + B4V + " The camera stays still."),
  BAU(MEADOW, "다친 자국이 있단다", "stands on all four feet next to one smooth cream fossil bone with a small healed bump on it, lying on a low flat rock, smiling wisely."),
  ("쉿, 잘 자요", "CRTP", ROOM59 + f"Night again: {D['C']} sleeps peacefully in the small round bed under the ORANGE blanket; Roro and Pio sleep curled up on {RUG59}; {D['T']} sleeps lying on the floor at the LEFT side of the bed with the long neck resting on the floor.", "", False,
   "Everyone sleeps, breathing slowly; nobody moves. The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 60화 커서 뭐가 될까? (60화 특집 · 직업 놀이) ----------------
# (2026-11-27, 사용자: 59·60화를 완전히 새 내용으로) 인기 채널의 직업 놀이 소재만 참고. 옷·소품은 친구 몸 색.
# 한 번 입은 옷은 S13·S14·S17까지 그대로(옷 이어짐). 토롱은 물건을 들지 않고 목에 거는 청진기만.
CHEST60 = "one big PURPLE wooden dress-up chest standing open on the grass, full of colorful hats"
COST60 = {
 "C": "Chiqui wears one shiny ORANGE firefighter helmet",
 "R": "Roro wears one tall YELLOW chef hat and one small YELLOW apron",
 "T": "Torong wears one small GREEN doctor cap and one GREEN toy stethoscope hanging around the neck",
 "P": "Pio wears one pair of round SKY-BLUE pilot goggles on the forehead and one small SKY-BLUE scarf",
}
def COSTS60(keys): return "; ".join(COST60[k] for k in keys) + ". Each friend wears only their own costume in their own body color; the costumes never cover the legs. "
COSTV60 = " Everyone keeps the same costume the whole time; no costume changes, comes off or swaps."
EPS["ep60"] = dict(
 title="60화. 커서 뭐가 될까? — 직업 놀이 60화 특집", short="커서 뭐가 될까?", song_id="dream60", song_short="꿈 노래",
 theme="60화 특집 직업 놀이: 바우 할아버지의 보라 옷 상자에서 소방관·요리사·의사·비행사 옷을 꺼내 입고 흉내 내기. 커서 뭐가 되고 싶은지 말해 보기.",
 twist="다들 옷을 입고 나서 물어봐요. \"할아버지는 커서 뭐가 되고 싶었어요?\" 할아버지가 웃으며 \"이야기 박사! 그래서 지금 너희랑 있지.\" 화면 밖 친구는 커서 뭐가 될까?",
 bau="트리케라톱스는 자라면서 뿔 모양이 바뀌었단다!",
 lines=[("바우","얘들아, 이리 오렴!",""),("모두","좋아!","♻ 1화 07"),("모두","와아~","♻ 1화 15"),("치키","커서 뭐가 될까?",""),
        ("치키","나는 소방관!",""),("로로","나는 요리사!",""),("토롱","나는 의사!",""),("피오","나는 비행사!",""),
        ("내레이션","우리 친구는 커서 뭐가 될까?","뒤에 3초 쉼"),("모두","할아버지는요?",""),("바우","할아버지는 이야기 박사란다!",""),
        ("바우","트리케라톱스는 자라면서 뿔 모양이 바뀌었단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("칙칙 물을 뿌려요","치키는 소방관 (칙칙!)","도와줄게요 (출동!)"),("보글보글 맛있게","로로는 요리사 (보글!)","냠냠 맛있다 (냠!)"),
         ("콩닥콩닥 들어 봐","토롱은 의사 (콩닥!)","튼튼해요 (튼튼!)"),("슝슝 하늘 높이","피오는 비행사 (슝!)","구름 위로 (슝슝!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "커서 뭐가 될까? (뭐가 될까?)", "꿈을 꾸어 봐요", "치키치키 꿈!"],
 scenes=scenes([
  BAU(MEADOW, "이리 오렴!", f"stands on all four feet next to one big PURPLE wooden dress-up chest standing CLOSED on the grass, smiling warmly as if calling the friends."),
  CHEER(MEADOW),
  ("옷 상자다!", "CRTP", MEADOW + f"Chiqui, Roro, Torong and Pio gather around {CHEST60}, peeking in with wide amazed eyes; nobody wears a costume yet.", "Exactly one chest.", False,
   "The friends lean toward the open chest and gasp happily on the same spot. The camera stays still."),
  ("커서 뭐가 될까?", "C", MEADOW + f"Close view of {D['C']} standing UPRIGHT on the two back legs next to {CHEST60}, one front paw on the chin, thinking, looking at the viewer; no costume yet.", "", True,
   "Chiqui tilts the head, thinking, then smiles brightly." + CUPV),
  ("나는 소방관!", "C", MEADOW + f"{D['C']} stands UPRIGHT on the two back legs wearing one shiny ORANGE firefighter helmet, proudly holding one short ORANGE toy hose in both front paws, next to {CHEST60}.", "Exactly one helmet and one hose.", False,
   "Chiqui salutes proudly with a big grin; the helmet stays on." + CUPV),
  ("나는 요리사!", "R", MEADOW + f"{D['R']} wears one tall YELLOW chef hat and one small YELLOW apron, stirring one small YELLOW pot on a low stump with one wooden spoon in the short arms, next to {CHEST60}.", "Exactly one pot.", False,
   "Roro stirs the pot two times and sniffs happily; the chef hat stays on."),
  ("칙칙 소방관", "C", MEADOW + f"{D['C']} stands UPRIGHT on the two back legs wearing the ORANGE firefighter helmet, spraying a gentle little stream of clear water from the short ORANGE toy hose onto one flower pot, proud and happy.", "", False,
   "A gentle stream of water sprays onto the flower pot; Chiqui grins; the helmet stays on." + CUPV),
  ("보글보글 요리사", "R", MEADOW + f"Close view of {D['R']} in the tall YELLOW chef hat and YELLOW apron tasting soup from one wooden spoon over the small YELLOW pot, a big happy 'yum' face.", "", True,
   "Roro tastes from the spoon and smiles with full cheeks; small steam rises from the pot."),
  ("콩닥콩닥 의사", "TP", MEADOW + f"{D['T']} wears one small GREEN doctor cap and one GREEN toy stethoscope around the neck, lowering the head gently toward {D['P']}, who sits on a low stump smiling; the stethoscope's round end rests on Pio's chest.", "", False,
   "Torong lowers the head a little and smiles; Pio giggles; Torong's four feet stay on the ground."),
  ("슝슝 비행사", "P", MEADOW + f"{D['P']} wears round SKY-BLUE pilot goggles and a small SKY-BLUE scarf, flying happily in the sky above the meadow, the scarf fluttering.", "", False,
   "Pio glides a little to the left and right in the sky, staying the same size; the scarf flutters."),
  ("꿈 행진", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio march happily in a row on the grass in their costumes. " + COSTS60("CRTP"), "", False,
   "The friends march in place two times, smiling proudly; Torong nods the neck to the beat." + COSTV60 + " The camera stays still."),
  ("할아버지는요?", "BCRTP", MEADOW + f"Chiqui, Roro, Torong and Pio, still in their costumes, look up curiously at {D['B']}, who stands on all four feet next to {CHEST60}. " + COSTS60("CRTP"), "", False,
   "The friends tilt their heads, curious; Grandpa Bau smiles." + COSTV60 + B4V + " The camera stays still."),
  BAU(MEADOW, "이야기 박사", "stands on all four feet next to one big open storybook on a low wooden stand, glasses shining, smiling proudly and warmly."),
  BAU(MEADOW, "뿔 모양이 바뀌었단다", "stands on all four feet next to two cream fossil triceratops skulls on a low flat rock: one SMALL skull with short little horns and one BIG skull with long horns, smiling wisely."),
  ("다 같이 꿈 퍼레이드", "BCRTP", MEADOW + f"All five friends parade happily on the grass: Chiqui, Roro, Torong and Pio in their costumes, {D['B']} walking with them with all four feet on the grass, smiling. " + COSTS60("CRTP"), "", False,
   "Everyone marches in place two times and cheers." + COSTV60 + B4V + " The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

for ep, e in EPS.items():
    write(ep, e)

# ---------- 공통 컷: 26~60화에서 그림 프롬프트가 같은 장면은 같은 그림·영상 하나를 쓴다 ----------
_ROOT = Path(__file__).resolve().parent.parent
_COMMON_NAME = {"안녕!": "ending_meadow", "좋아!": "cheer_meadow"}
_known = {}
for _n in range(26, 46):
    _f = _ROOT / f"episodes/ep{_n}/scenes.json"
    if _f.exists():
        for _s in _json.loads(_f.read_text(encoding="utf-8")):
            if _s.get("common"): _known[_s["img"]] = _s["common"]
_groups = _col.defaultdict(list)
for _ep in EPS:
    for _s in _json.loads((_ROOT / f"episodes/{_ep}/scenes.json").read_text(encoding="utf-8")):
        _groups[_s["img"]].append((_ep, _s["id"], _s["name"]))
for _ep in EPS:
    _f = _ROOT / f"episodes/{_ep}/scenes.json"
    _sc = _json.loads(_f.read_text(encoding="utf-8"))
    for _s in _sc:
        _v = _groups[_s["img"]]
        if _s["img"] in _known: _s["common"] = _known[_s["img"]]
        elif len(_v) > 1: _s["common"] = _COMMON_NAME.get(_v[0][2], f"common_{_v[0][0]}_{_v[0][1]}")
        else: _s.pop("common", None)
    _f.write_text(_json.dumps(_sc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(_ep, "common:", [(s["id"], s["common"]) for s in _sc if s.get("common")])

# (2026-11-27, 사용자: 같은 화면은 두 번 만들지 않기) 46화 S03·S04는 그림이 같다 → S03에서 10초 영상 하나, S04는 그 뒷부분.
SAMEPIC = {  # 장면: (그림·영상을 만드는 장면, 쓰는 부분)
 "ep46": {"S04": ("S03", "뒷부분"), "S05": ("S10", "앞부분"), "S16": ("S10", "전체")},
 "ep47": {"S06": ("S16", "앞부분")},
 "ep48": {},
 "ep50": {"S14": ("S16", "앞부분")},
 "ep51": {"S03": ("S02", "뒷부분"), "S14": ("S13", "뒷부분")},
 "ep53": {"S16": ("S13", "전체")},
 "ep55": {"S06": ("S05", "뒷부분")},
}
for _ep, _m in SAMEPIC.items():
    _f = Path(__file__).resolve().parent.parent / f"episodes/{_ep}/scenes.json"
    _sc = _json.loads(_f.read_text(encoding="utf-8"))
    for _s in _sc:
        _bases = {v[0] for v in _m.values()}
        if _s["id"] in _m or _s["id"] in _bases: _s.pop("common", None)  # 같은 화 안에서 같은 그림은 공통 컷이 아님
        if _s["id"] in _m:
            _b, _part = _m[_s["id"]]; _s["samevid"] = _b; _s["samevid_part"] = _part
            _base = next(x for x in _sc if x["id"] == _b); _s["img"], _s["vid"] = _base["img"], _base["vid"]
        if _s["id"] in _bases: _s["sec"] = 10
    _f.write_text(_json.dumps(_sc, ensure_ascii=False, indent=1), encoding="utf-8")

