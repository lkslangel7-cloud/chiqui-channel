"""16~20화 대본·가사·장면 프롬프트. 인기 유아 채널에서 반응이 좋은 '형식'만 참고하고 이야기·노래는 새로 만든다.
16 목욕 노래(몸 이름) · 17 다쳤을 때(아야! 괜찮아) · 18 차례 지키기(미끄럼틀) · 19 첫눈 놀이 · 20 빵집 역할놀이
도우미(img, vid, scenes, write)와 안전 문장은 make_ep11_15.py → make_ep06_10.py 것을 그대로 쓴다.
사용법: python3 -I prompts/make_ep16_20.py
"""
from pathlib import Path

_p = Path(__file__).resolve().parent / "make_ep11_15.py"
_src = _p.read_text(encoding="utf-8")
_ns = {"__file__": str(_p)}
exec(_src.split("\nEPS = {}")[0], _ns)
img, vid, scenes, write, D, HOME, NODOLL = (_ns[k] for k in ("img", "vid", "scenes", "write", "D", "HOME", "NODOLL"))

EPS = {}
# ---------------- 16화 목욕하자 뽀글뽀글 (몸 이름) ----------------
SPRING = ("At a warm shallow round hot-spring pool at the foot of the friendly volcano, with soft white bubbles on the water, smooth round stones around the edge "
          "and a little gentle steam. ")
EPS["ep16"] = dict(
 title="16화. 목욕하자 뽀글뽀글! — 몸 씻기 노래", short="목욕하자 뽀글뽀글!", song_id="bath", song_short="목욕 노래",
 theme="몸 씻기 습관 + 몸 이름 (머리·꼬리·목·날개·발가락). 화산 아래 따뜻한 온천에서 다 같이 목욕. 수건은 친구 몸 색.",
 twist="다 씻었는데… 치키 발가락에만 진흙이 콕! 화면 밖 아이가 찾아 준다.",
 bau="씻고 나면 기분도 반짝!",
 lines=[("치키","아이, 지저분해!",""),("바우","다 같이 목욕하자!",""),("모두","좋아!","♻ 1화 07"),("내레이션","보글보글 따뜻해요.",""),
        ("치키","머리부터 쓱쓱!",""),("내레이션","어디가 아직 지저분할까?","뒤에 3초 쉼"),("치키","발가락이다!",""),("모두","하하하!","♻ 3화 11"),
        ("바우","씻고 나면 기분도 반짝!","바우 할아버지 한마디"),("모두","깨끗해!","♻ 6화 14"),("치키","안녕!","♻ 1화 18")],
 verses=[("머리를 쓱쓱쓱","치키 뿔도 반짝","뽀글뽀글 (뽀글!)"),("꼬리를 쓱쓱쓱","크앙! 로로 꼬리","뽀글뽀글 (뽀글!)"),
         ("목을 쭈욱 쓱쓱","토롱 긴 목도","뽀글뽀글 (뽀글!)"),("날개를 팔랑 쓱쓱","슝~ 피오 날개","뽀글뽀글 (뽀글!)")],
 chorus="목욕하자 뽀글뽀글",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "목욕하자 뽀글뽀글 (뽀글뽀글!)", "머리부터 발끝까지", "치키치키 깨끗!"],
 scenes=scenes([
  ("아이, 지저분해!", "CRTP", "On a sunny meadow after playing, Chiqui, Roro, Torong and Pio have little brown mud spots on their bodies and laugh at each other.", "Only small mud spots; everyone keeps their own body color.", False,
   "The friends look at their muddy spots and giggle."),
  ("다 같이 목욕하자!", "B", SPRING + f"{D['B']} stands at the edge of the pool and points at the warm water with a big smile.", "", False,
   "Grandpa Bau points at the pool twice and nods with a smile."),
  ("좋아!", "CRTP", SPRING + "Chiqui, Roro, Torong and Pio stand at the edge of the pool, cheering.", "", False, "The friends cheer and bounce on the spot."),
  ("첨벙!", "CRTP", SPRING + "Chiqui, Roro and Torong step into the shallow pool with a little splash; Pio stands on a smooth stone at the edge with both feet in the water.", "", False,
   "The friends step into the water one by one with small splashes and laugh."),
  ("보글보글 따뜻해요", "C", SPRING + f"{D['C']} sits in the warm water up to the tummy with eyes closed, smiling happily, bubbles around.", "", False,
   "Chiqui sways gently left and right with a happy sigh; bubbles float up."),
  ("머리부터 쓱쓱!", "C", SPRING + f"{D['C']} sits in the water and rubs the top of the head with both front paws, soft white bubbles on the head.", "", False,
   "Chiqui rubs the head round and round, four times; the bubbles grow."),
  ("치키 뿔도 반짝", "C", SPRING + f"Close view of {D['C']} with a small crown of white bubbles around the three horns, the yellow-spotted frill shiny and clean.", "", True,
   "Chiqui nods the head; the bubble crown wobbles and Chiqui giggles."),
  ("로로 꼬리", "R", SPRING + f"{D['R']} sits in the water and scrubs the tail with soft white bubbles, smiling.", "", False,
   "Roro wags the bubbly tail left and right four times and giggles."),
  ("토롱 긴 목", "T", SPRING + f"{D['T']} stands in the shallow water; soft white bubbles slide down the very long neck.", "", False,
   "Torong sways the long neck slowly left and right; bubbles slide down the neck."),
  ("피오 날개", "P", SPRING + f"{D['P']} stands on a smooth stone at the edge and splashes both wide wings in the shallow water, small bubbles on the wings.", "", False,
   "Pio flaps both wings in the water four times; little bubbles fly up."),
  ("다 같이 뽀글뽀글", "BCRTP", SPRING + "All five friends sit together in the bubbly pool, smiling; Pio sits on a stone at the edge.", "", False,
   "Everyone scrubs and splashes gently, laughing together."),
  ("어디가 아직 지저분할까?", "C", SPRING + f"{D['C']} stands on a flat stone at the edge, clean and shiny, but one front foot still has a small brown mud spot on the toes. Chiqui looks at the viewer, curious.", "Only the toes of one foot are muddy.", False,
   "Chiqui looks at the viewer and tilts the head, as if asking 'Where?'."),
  ("발가락이다!", "C", SPRING + f"{D['C']} sits at the edge and dips the muddy toes into the water, laughing.", "", False,
   "Chiqui wiggles the toes in the water; the mud washes away and Chiqui laughs."),
  ("씻고 나면 기분도 반짝!", "B", SPRING + f"{D['B']} sits by the pool wrapped in a soft PURPLE towel, smiling warmly.", "", False,
   "Grandpa Bau pats the towel and nods warmly."),
  ("뽀송뽀송", "CRTP", "On the grass next to the pool, Chiqui, Roro, Torong and Pio dry off with soft towels in their own body colors: ORANGE towel for Chiqui, YELLOW for Roro, GREEN for Torong, SKY-BLUE for Pio.", "Each towel matches its owner's body color.", False,
   "The friends rub themselves dry with the towels and giggle."),
  ("깨끗해!", "BCRTP", "On the grass next to the hot-spring pool, all five friends stand in a row facing the viewer, clean and shiny, with towels around their shoulders.", "", False,
   "Everyone shows how clean they are and cheers."),
 ]))
# ---------------- 17화 아야! 괜찮아 (다쳤을 때) ----------------
EPS["ep17"] = dict(
 title="17화. 아야! 괜찮아? — 다쳤을 때", short="아야! 괜찮아?", song_id="ouch", song_short="아야 괜찮아",
 theme="넘어졌을 때 말하기, 친구 위로하기, 반창고(치키 주황). 뛸 때는 천천히 조심조심.",
 twist="울던 치키가 친구들 토닥·호~ 덕분에 다시 웃는다. 화면 밖 아이도 '호~' 해 준다.",
 bau="다치면 꼭 어른에게 말하렴.",
 lines=[("치키","누가 누가 빠를까!",""),("로로","나야 나!",""),("치키","아야!",""),("치키","아파…",""),("모두","괜찮아?",""),
        ("바우","호~ 해 줄게.",""),("내레이션","우리도 같이 호~ 해 볼까?","뒤에 3초 쉼"),("치키","주황 반창고다!",""),
        ("바우","다치면 꼭 어른에게 말하렴.","바우 할아버지 한마디"),("모두","천천히, 조심조심!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("아야 아야 무릎이","크앙! 로로가 와서","토닥토닥 (토닥!)"),("아야 아야 눈물이","쭈욱~ 토롱이 와서","괜찮아 괜찮아 (괜찮아!)"),
         ("아야 아야 아파요","슝~ 피오가 와서","호~ 불어 줘 (호~!)"),("주황 반창고 붙이고","이제 괜찮아 (괜찮아!)","웃음이 쏙 (하하!)")],
 chorus="아야! 괜찮아?",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "아야! 괜찮아? (괜찮아?)", "친구가 곁에 있어", "치키치키 힘내!"],
 scenes=scenes([
  ("누가 누가 빠를까!", "CRTP", "On a sunny meadow path, Chiqui, Roro, Torong and Pio line up at a start line drawn in the dirt, ready to race, smiling.", "", False,
   "The friends crouch, ready, and wiggle with excitement."),
  ("나야 나!", "R", f"{D['R']} runs fast along the meadow path, laughing.", "", False, "Roro runs forward happily with bouncy steps."),
  ("슝슝 달려요", "C", f"{D['C']} runs fast along the meadow path with a determined happy face.", "", False, "Chiqui runs forward quickly with big steps."),
  ("아야!", "C", f"{D['C']} sits on the soft grass after a little fall, holding one knee with both front paws; the knee has a tiny pink scratch. No blood.", "No blood; only a tiny pink scratch.", False,
   "Chiqui sits on the grass and holds the knee with a surprised 'ouch' face."),
  ("아파…", "C", f"Close view of {D['C']} sitting on the grass with big teary eyes, holding the knee.", "No blood.", True,
   "Chiqui's eyes fill with tears and Chiqui sniffles once."),
  ("괜찮아?", "RTP", "Roro, Torong and Pio hurry over across the meadow with worried faces.", "", False, "The three friends hurry forward with worried faces."),
  ("로로 · 토닥토닥", "CR", f"{D['R']} sits next to {D['C']} on the grass and gently pats Chiqui's back with one small front paw.", "", False,
   "Roro pats Chiqui's back gently two times; Chiqui sniffles."),
  ("토롱 · 괜찮아", "CT", f"{D['T']} bends the long neck down low and gently touches Chiqui's cheek with the nose; {D['C']} sits on the grass.", "", False,
   "Torong lowers the neck slowly and nuzzles Chiqui's cheek once; Chiqui smiles a little."),
  ("피오 · 호~", "CP", f"{D['P']} stands next to {D['C']} and blows softly on Chiqui's knee with the beak, cheeks puffed.", "No blood.", False,
   "Pio puffs the cheeks and blows softly; Chiqui giggles."),
  ("할아버지가 왔어요", "BC", f"{D['B']} walks over carrying a small PURPLE first-aid pouch with a white cross; {D['C']} sits on the grass.", "", False,
   "Grandpa Bau walks over gently and sits down next to Chiqui."),
  ("호~ 해 줄게", "BC", f"{D['B']} kneels next to {D['C']} and blows softly on Chiqui's knee.", "No blood.", False,
   "Grandpa Bau blows softly on the knee; Chiqui smiles."),
  ("우리도 호~", "C", f"Close view of {D['C']} sitting on the grass holding out the knee toward the viewer, smiling hopefully.", "No blood.", True,
   "Chiqui looks at the viewer and waits, smiling."),
  ("주황 반창고다!", "C", f"{D['C']} sits on the grass, one small ORANGE bandage on the knee, smiling proudly and pointing at it.", "Exactly one orange bandage.", False,
   "Chiqui points at the orange bandage and laughs."),
  ("어른에게 말하렴", "B", f"{D['B']} sits on the meadow smiling warmly, one front paw raised gently.", "", False, "Grandpa Bau nods warmly."),
  ("천천히, 조심조심!", "CRTP", "On the meadow path, Chiqui, Roro, Torong and Pio walk slowly together side by side, carefully, smiling.", "", False,
   "The friends walk slowly and carefully together, step by step."),
  ("다 같이 웃어요", "BCRTP", "All five friends stand together on the meadow facing the viewer, smiling; Chiqui has one small ORANGE bandage on the knee.", "", False,
   "Everyone laughs together and cheers."),
 ]))
# ---------------- 18화 내 차례 네 차례 (미끄럼틀) ----------------
SLIDE = "Roro's play rock: a big rounded rock with a wide smooth clay slide and little stone steps on the side. "
EPS["ep18"] = dict(
 title="18화. 내 차례 네 차례! — 차례 지키기", short="내 차례 네 차례!", song_id="turn", song_short="차례 노래",
 theme="차례 지키기, 한 줄로 서기, 기다리기. 놀이터 바위 미끄럼틀. 마지막 차례는 할아버지!",
 twist="다 탔다고 생각했는데… 마지막 차례는 바우 할아버지! 할아버지도 슝~",
 bau="차례를 지키면 모두 신나지!",
 lines=[("치키","미끄럼틀이다!",""),("로로","내가 먼저!",""),("모두","나도! 나도!",""),("내레이션","어, 한꺼번에 타면 안 돼요!",""),
        ("바우","한 줄로 서 볼까?",""),("모두","좋아!","♻ 1화 07"),("내레이션","마지막은 누구 차례일까?","뒤에 3초 쉼"),("모두","할아버지!",""),
        ("바우","차례를 지키면 모두 신나지!","바우 할아버지 한마디"),("모두","한 번 더!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("하나 치키 슝~","미끄럼틀 쭈욱","내 차례 끝 (끝!)"),("둘 로로 슝~","크앙! 신나게","네 차례야 (네 차례!)"),
         ("셋 토롱 슝~","쭈욱~ 긴 목도","네 차례야 (네 차례!)"),("넷 피오 슝~","작은 날개 펴고","네 차례야 (네 차례!)")],
 chorus="내 차례 네 차례",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "내 차례 네 차례 (차례 차례!)", "한 줄로 서서", "치키치키 슝!"],
 scenes=scenes([
  ("미끄럼틀이다!", "C", f"On a sunny day at {SLIDE}{D['C']} stands at the bottom of the slide, pointing up with a big excited smile.", "", False,
   "Chiqui points at the slide and hops with excitement."),
  ("내가 먼저!", "R", f"At {SLIDE}{D['R']} runs toward the stone steps, laughing.", "", False, "Roro runs to the steps with bouncy steps."),
  ("나도! 나도!", "CRTP", f"At {SLIDE}Chiqui, Roro, Torong and Pio all crowd together at the bottom of the stone steps at the same time, squeezed and bumping softly, with funny faces.", "", False,
   "The friends squeeze and wobble together at the steps, nobody can go up."),
  ("한꺼번에 타면 안 돼요", "CRTP", f"At {SLIDE}Chiqui, Roro, Torong and Pio sit in a funny tangled little pile at the bottom of the steps, laughing.", "", False,
   "The friends untangle themselves slowly and laugh."),
  ("한 줄로 서 볼까?", "B", f"At {SLIDE}{D['B']} smiles and points at the ground in front of the steps with one front paw.", "", False,
   "Grandpa Bau points and nods kindly."),
  ("한 줄로", "CRTP", f"At {SLIDE}Chiqui, Roro, Torong and Pio stand in one neat line in front of the steps, in this order: Chiqui first, then Roro, then Torong, then Pio.", "", False,
   "The friends wait in line and nod happily."),
  ("치키 슝~", "C", f"At {SLIDE}{D['C']} slides down the wide slide with both arms up, laughing.", "", False, "Chiqui slides down happily and lands softly at the bottom."),
  ("로로 슝~", "R", f"At {SLIDE}{D['R']} slides down the wide slide, mouth open in a happy roar.", "", False, "Roro slides down and lands with a happy roar."),
  ("토롱 슝~", "T", f"At {SLIDE}{D['T']} slides down the wide slide on the tummy, the long neck stretched forward, smiling.", "", False,
   "Torong slides down slowly and gently and lands smiling."),
  ("피오 슝~", "P", f"At {SLIDE}{D['P']} slides down the wide slide with both wings spread open, smiling.", "", False, "Pio slides down with wings open and hops at the bottom."),
  ("다 같이 박수", "CRTP", f"At {SLIDE}Chiqui, Roro, Torong and Pio stand at the bottom of the slide clapping and cheering.", "", False, "The friends clap and cheer together."),
  ("마지막은 누구 차례?", "C", f"Close view of {D['C']} at the play rock looking at the viewer with a curious face, one paw up.", "", True,
   "Chiqui tilts the head and looks at the viewer as if asking 'Who is next?'."),
  ("할아버지 슝~", "B", f"At {SLIDE}{D['B']} slides down the wide slide, laughing happily with eyes closed, the round glasses on.", "", False,
   "Grandpa Bau slides down slowly and laughs at the bottom."),
  ("차례를 지키면 신나지", "B", f"At {SLIDE}{D['B']} sits at the bottom of the slide smiling warmly.", "", False, "Grandpa Bau nods warmly and chuckles."),
  ("한 번 더!", "CRTP", f"At {SLIDE}Chiqui, Roro, Torong and Pio line up again in one line, cheering.", "", False, "The friends line up again and cheer."),
  ("모두 신나요", "BCRTP", f"At {SLIDE}all five friends stand in a row facing the viewer, smiling big.", "", False, "Everyone cheers together and smiles at the viewer."),
 ]))
# ---------------- 19화 첫눈이 와요 ----------------
SNOW = ("Snowy winter day in the dinosaur village: soft white snow covers the ground, the palm trees and the round cave houses, and gentle snowflakes fall from a pale blue-gray sky. "
        "NO rainbow anywhere, no sun. ")
SCARF = "Chiqui wears an ORANGE scarf, Roro a YELLOW scarf, Torong a GREEN scarf, Pio a SKY-BLUE scarf"
MAN = "a plain simple snowman made of two white snowballs (a big one below, a smaller one on top) with ONLY two small dark pebble eyes: NO mouth, NO hat, NO scarf, NO buttons, NO stick arms; the snowman is a still object and never moves"
EPS["ep19"] = dict(
 title="19화. 첫눈이 와요! — 눈 놀이", short="첫눈이 와요!", song_id="snow", song_short="첫눈 노래",
 theme="계절(겨울), 눈 놀이, 따뜻하게 입기. 목도리는 친구 몸 색. 눈사람 만들기.",
 twist="눈사람에 코가 없다! 화면 밖 아이가 '당근 코!' — 치키가 주황 당근을 콕.",
 bau="눈은 작은 얼음 꽃이란다.",
 lines=[("치키","어? 하얀 게 내려요!",""),("내레이션","첫눈이에요!",""),("모두","와아~","♻ 1화 15"),("바우","따뜻하게 입자.",""),
        ("치키","목도리 두르고!",""),("모두","눈사람 만들자!",""),("내레이션","눈사람에게 무엇이 필요할까?","뒤에 3초 쉼"),("치키","주황 당근 코!",""),
        ("바우","눈은 작은 얼음 꽃이란다.","바우 할아버지 상식"),("모두","아이 추워!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("하얀 눈이 펄펄","크앙! 로로가","눈을 데굴데굴 (데굴!)"),("눈덩이 하나 둘","쭈욱~ 토롱이","높이 올려 (영차!)"),
         ("동글동글 까만 눈","슝~ 피오가","콕콕 붙여 (콕!)"),("무엇이 필요할까?","두리번 두리번 (어디 있지?)","동글동글 코 (코!)")],
 chorus="하얀 눈이 펄펄",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "하얀 눈이 펄펄 (펄펄!)", "친구들아 같이 놀자", "치키치키 눈 놀이!"],
 scenes=scenes([
  ("하얀 게 내려요!", "C", SNOW + f"{D['C']} stands at the round door of the cave house, looking up at the falling snowflakes with wide surprised eyes.", "", False,
   "Chiqui looks up, holds out one paw and catches a snowflake, amazed."),
  ("첫눈이에요!", "", SNOW + "A wide view of the quiet snowy village with gentle snowflakes falling.", "", True,
   "Snowflakes fall gently over the quiet village."),
  ("와아~", "CRTP", SNOW + "Chiqui, Roro, Torong and Pio jump happily in the fresh snow.", "", False, "The friends jump in the snow and laugh; snow puffs up."),
  ("따뜻하게 입자", "B", SNOW + f"{D['B']} stands in the snow holding a small pile of soft scarves in four colors: orange, yellow, green and sky-blue.", "Exactly four scarves.", False,
   "Grandpa Bau holds up the scarves and smiles."),
  ("목도리 두르고!", "C", SNOW + f"{D['C']} wears a soft ORANGE scarf and hugs it happily.", "", False, "Chiqui snuggles into the orange scarf and smiles."),
  ("눈사람 만들자!", "CRTP", SNOW + f"Chiqui, Roro, Torong and Pio stand in the snow wearing scarves: {SCARF}. They cheer.", "Each scarf matches its owner's body color.", False,
   "The friends cheer and bounce in the snow."),
  ("로로 · 데굴데굴", "R", SNOW + f"{D['R']} wearing a YELLOW scarf rolls a big snowball across the snow.", "", False, "Roro pushes the snowball forward; it grows bigger."),
  ("토롱 · 영차", "T", SNOW + f"{D['T']} wearing a GREEN scarf bends the long neck and gently places a smaller snowball on top of a big snowball with the mouth.", "", False,
   "Torong lifts the small snowball with the mouth and places it on top carefully."),
  ("피오 · 콕콕", "P", SNOW + f"{D['P']} wearing a SKY-BLUE scarf flies next to {MAN}, pressing a small dark pebble eye onto the top snowball with the beak.", "", False,
   "Pio presses the second pebble eye on and flaps happily."),
  ("무엇이 필요할까?", "CRTP", SNOW + f"Chiqui, Roro, Torong and Pio look at {MAN}; the snowman has NO nose yet. {SCARF}; each scarf matches its owner's body color exactly (no red, no purple, no swapped colors).", "No nose on the snowman.", False,
   "The friends tilt their heads, looking at the snowman."),
  ("다 같이 생각해요", "CRTP", SNOW + f"Chiqui, Roro, Torong and Pio stand around {MAN}, thinking with paws on their chins. {SCARF}; each scarf matches its owner's body color exactly (no red, no purple, no swapped colors).", "No nose on the snowman.", False,
   "The friends look at each other, thinking."),
  ("코가 없네?", "C", SNOW + f"Close view of {D['C']} in an ORANGE scarf looking at the viewer with a curious face.", "", True,
   "Chiqui looks at the viewer and tilts the head, as if asking."),
  ("주황 당근 코!", "C", SNOW + f"{D['C']} in an ORANGE scarf puts one ORANGE carrot nose onto {MAN}, laughing.", "Exactly one carrot nose.", False,
   "Chiqui pushes the carrot nose in and jumps with joy."),
  ("눈은 작은 얼음 꽃", "B", SNOW + f"{D['B']} looks at one big sparkly snowflake resting on the front paw, smiling wisely.", "", True,
   "Grandpa Bau looks at the snowflake and smiles."),
  ("아이 추워!", "BCRTP", SNOW + f"All five friends stand next to the finished snowman: the same plain snowman made of two white snowballs with two pebble eyes and one ORANGE carrot nose (no mouth, no hat, no scarf, no buttons, no stick arms). They hug themselves and shiver with funny faces. {SCARF}.", "", False,
   "Everyone shivers and laughs together."),
  ("따뜻한 집", "BCRTP", HOME + f"All five friends sit by a warm glowing fireplace inside the cave house holding warm mugs; snow falls outside the round window. {SCARF}.", "", False,
   "Everyone sips from the mugs and smiles warmly."),
 ]))
# ---------------- 20화 공룡 빵집 놀이 ----------------
SHOP = ("THE SAME bakery stall in every scene: one small toy-like wooden bakery stall standing alone on a sunny flower meadow, seen from the front. "
        "It has exactly this shape: a light-wood front counter box at waist height, two thin wooden posts at the back corners, and on top a flat awning with "
        "wide ORANGE and cream-white vertical stripes and a wavy scalloped front edge; a small round cream-white sign with one simple bread-loaf picture (no letters) hangs in the middle of the awning. "
        "Behind the stall there is only open meadow, a few palm trees and the far volcano; NO other shops, houses, shelves, walls, windows or roofs behind it. "
        "The stall never changes shape, color or size. ")
BREADS = "five small round breads on the counter: one YELLOW corn bread, one GREEN bread, one dark BLUE blueberry bread, one PURPLE grape bread and one ORANGE bread"
EPS["ep20"] = dict(
 title="20화. 공룡 빵집 놀이! — 역할놀이", short="공룡 빵집 놀이!", song_id="bakery", song_short="빵집 노래",
 theme="가게 역할놀이, 인사말(어서 오세요·주세요·고맙습니다), 하나씩 세기. 빵은 친구 몸 색.",
 twist="할아버지 보라 빵이 없다! 치키 볼이 빵빵… 치키가 먹었다! 그래서 다 같이 새 빵을 만든다.",
 bau="같이 만든 빵이 제일 맛있지!",
 lines=[("치키","빵집 놀이 하자!",""),("모두","좋아!","♻ 1화 07"),("치키","어서 오세요!",""),("모두","빵 주세요!",""),
        ("치키","여기 있어요!",""),("모두","고맙습니다!",""),("내레이션","할아버지 빵은 어디 갔을까?","뒤에 3초 쉼"),("모두","치키가 먹었다!",""),
        ("치키","헤헤, 같이 만들어요!",""),("바우","같이 만든 빵이 제일 맛있지!","바우 할아버지 한마디"),("치키","안녕!","♻ 1화 18")],
 verses=[("노란 옥수수빵","크앙! 로로가","하나 주세요 (주세요!)"),("초록 빵 동글동글","쭈욱~ 토롱이","하나 주세요 (주세요!)"),
         ("파란 블루베리빵","슝~ 피오가","하나 주세요 (주세요!)"),("보라 포도빵 하나","할아버지 빵인데 (어디 갔지?)","냠냠 소리 (냠!)")],
 chorus="빵 사세요",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "빵 사세요 빵집 (빵집!)", "주세요 고맙습니다", "치키치키 빵집!"],
 scenes=scenes([
  ("빵집 놀이 하자!", "C", f"On a sunny meadow, {D['C']} stands next to {SHOP}cheering with both arms up.", "", False, "Chiqui hops and cheers next to the stall."),
  ("좋아!", "RTP", "On a sunny meadow, Roro, Torong and Pio cheer and nod happily.", "", False, "The friends cheer and bounce."),
  ("어서 오세요!", "C", f"{D['C']} stands behind the counter of {SHOP}wearing a small white baker hat and an ORANGE apron, waving one paw.", "", False,
   "Chiqui waves and bows a little, smiling."),
  ("빵이 가득", "", f"Close view of the counter of {SHOP}with {BREADS}, warm and soft.", "Exactly five breads.", True, "Soft warm light glows on the breads; nothing moves except a little steam."),
  ("빵 주세요!", "RTP", f"Roro, Torong and Pio stand in a line in front of {SHOP}smiling politely.", "", False, "The friends wait politely and smile."),
  ("손님이 왔어요", "CRTP", f"Chiqui in a baker hat and ORANGE apron stands behind the counter of {SHOP}; Roro, Torong and Pio stand in front of the counter, smiling.", "", False,
   "Chiqui waves; the friends wave back."),
  ("로로 · 노란 빵", "CR", f"At {SHOP}{D['C']} in a baker hat hands one YELLOW corn bread across the counter to {D['R']}.", "Exactly one yellow bread being handed.", False,
   "Chiqui hands over the bread; Roro takes it and bows a little."),
  ("토롱 · 초록 빵", "CT", f"At {SHOP}{D['C']} in a baker hat holds up one GREEN bread; {D['T']} bends the long neck down and takes it gently with the mouth.", "Exactly one green bread being handed.", False,
   "Torong takes the bread gently and nods."),
  ("피오 · 파란 빵", "CP", f"At {SHOP}{D['C']} in a baker hat hands one dark BLUE blueberry bread to {D['P']}.", "Exactly one blue bread being handed.", False,
   "Pio takes the bread and flaps once happily."),
  ("할아버지 차례", "BC", f"At {SHOP}{D['B']} arrives at the counter smiling; {D['C']} in a baker hat stands behind the counter with puffed-out cheeks; the plate on the counter is EMPTY.", "No bread on the counter.", False,
   "Grandpa Bau looks at the empty plate; Chiqui keeps the cheeks puffed and looks away."),
  ("보라 빵이 없네?", "BRTP", f"At {SHOP}Grandpa Bau, Roro, Torong and Pio look at the empty plate on the counter, puzzled.", "", False,
   "Everyone looks at the empty plate and tilts their heads."),
  ("할아버지 빵은 어디?", "C", f"Close view of {D['C']} in a baker hat facing the viewer with big puffed-out cheeks and a few purple crumbs on the mouth, eyes looking sideways.", "", True,
   "Chiqui chews slowly with puffed cheeks and looks sideways, trying not to laugh."),
  ("치키가 먹었다!", "BCRTP", f"At {SHOP}Grandpa Bau, Roro, Torong and Pio point at Chiqui and laugh; Chiqui laughs shyly, purple crumbs on the mouth.", "", False,
   "Everyone points and laughs; Chiqui laughs too."),
  ("같이 만들어요!", "BCRTP", "On a sunny meadow, all five friends stand around a low wooden table, pressing soft round dough together, smiling.", "", False,
   "Everyone pats the dough together and smiles."),
  ("같이 만든 빵", "B", f"{D['B']} holds one warm round PURPLE grape bread, smiling warmly.", "Exactly one purple bread.", False, "Grandpa Bau sniffs the warm bread and smiles."),
  ("다 같이 냠냠", "BCRTP", "On a sunny meadow, all five friends sit together on a picnic blanket, each holding a small round bread in their own body color, happily eating.", "", False,
   "Everyone takes a bite and smiles at the viewer."),
 ]))

for ep, e in EPS.items():
    write(ep, e)
