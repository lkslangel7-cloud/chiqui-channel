# 1화. 치키의 세 가지 인사 — 대본과 생성 프롬프트

- 화면 비율: 16:9 (유튜브 롱폼)
- 장면 10개 / 장면 그림 10장 / 5초 영상 조각 5개
- 캐릭터 자리에는 Element ID 플레이스홀더를 넣었다. 캐릭터 등록 후 `characters.md`의 ID로 바꾼다.
  - `<<<CHIQUI>>>` 치키, `<<<BRONTI>>>` 브론티, `<<<PICO>>>` 피코, `<<<TINO>>>` 티노
- 모든 이미지 프롬프트 끝에는 `characters.md`의 공통 스타일 문구가 이미 붙어 있다.
- 영어·스페인어 대본은 한국어 대본 확정 후 작성한다.

## 예상 크레딧

| 작업 | 수량 | 예상 |
| --- | --- | --- |
| 캐릭터 기준 이미지 (`characters.md` 프롬프트) | 4장 | 약 1 |
| 장면 그림 | 10장 | 약 2.5 |
| 5초 영상 (Kling 3.0) | 5개 | 50 |
| 합계 | | 약 54 (다시 생성 여유 제외) |

영상 조각 없이 그림 + 확대·이동 효과로만 만들면 약 3.5크레딧이다.

---

## 장면 01 — 레인보우 밸리 (오프닝 노래)

**나레이션**: 화산 너머 작은 섬, 레인보우 밸리예요.
**노래**: 오프닝 "치키의 인사 노래" (`songs.md`)

**이미지 프롬프트 (`ep01_s01.png`)**
```
Wide establishing shot of Rainbow Valley, a small cozy island beyond a gentle sleeping volcano. Rolling green hills, a sparkling blue lake, a soft round forest, fluffy cloud hills, and a faint rainbow arching across a bright morning sky. Peaceful, welcoming, no characters. Clean 2D children's cartoon style, smooth soft shading, thick friendly outlines, simple shapes easy to animate, pastel colors, preschool animation look, no text.
```

**영상 프롬프트 (`ep01_c01.mp4`, 장면 01 그림 → 5초)**
```
Slow gentle camera pan from left to right across the valley. Clouds drift softly, the lake shimmers, the rainbow glows a little brighter. Calm, smooth motion, no characters appear.
```

## 장면 02 — 치키가 이사 왔어요

**나레이션**: 오늘 레인보우 밸리에 새 친구가 이사 왔어요.
**치키**: 와, 여기가 우리 새 동네야!

**이미지 프롬프트 (`ep01_s02.png`)**
```
<<<CHIQUI>>> Chiqui the baby triceratops arriving at the edge of Rainbow Valley, carrying a small bundle wrapped in a big leaf on its back, looking around with wide amazed eyes. A winding dirt path leads into green hills and a lake in the distance. Bright morning light. Clean 2D children's cartoon style, smooth soft shading, thick friendly outlines, simple shapes easy to animate, pastel colors, preschool animation look, no text.
```

## 장면 03 — 저기 친구들이 있어요

**나레이션**: 호숫가에서 친구들이 놀고 있어요.
**치키**: 나도 친구가 되고 싶다…

**이미지 프롬프트 (`ep01_s03.png`)**
```
<<<CHIQUI>>> Chiqui peeking out from behind a round green bush in the foreground, only Chiqui's head and three horns visible. In the background by the sparkling lake, <<<BRONTI>>> Bronti the sky-blue brontosaurus, <<<PICO>>> Pico the yellow pteranodon flying low, and <<<TINO>>> Tino the orange baby tyrannosaurus are playing happily. Clean 2D children's cartoon style, smooth soft shading, thick friendly outlines, simple shapes easy to animate, pastel colors, preschool animation look, no text.
```

## 장면 04 — 수줍은 치키

**나레이션**: 그런데 치키는 너무 부끄러웠어요.
**치키**: 뭐라고 말을 걸지? 왜 이렇게 떨릴까?

**이미지 프롬프트 (`ep01_s04.png`)**
```
Close-up of <<<CHIQUI>>> Chiqui hiding behind the bush, blushing, looking down shyly and fidgeting with its front feet, small nervous sweat drop. Soft blurred lake background. Clean 2D children's cartoon style, smooth soft shading, thick friendly outlines, simple shapes easy to animate, pastel colors, preschool animation look, no text.
```

## 장면 05 — 뿔 세 개가 반짝!

**나레이션**: 그때, 치키의 뿔 세 개가 반짝반짝 빛났어요.
**나레이션**: 뿔 하나마다 다른 나라 인사를 알려줬어요. 안녕! Hello! Hola!
**치키**: 우와, 인사하는 방법이 세 가지나 있네!

**이미지 프롬프트 (`ep01_s05.png`)**
```
<<<CHIQUI>>> Chiqui looking up in wonder as Chiqui's three horns glow with soft magical light, one pink, one sky blue, one golden yellow, with tiny sparkles and small stars floating around Chiqui's head. Gentle magical moment, warm background. Clean 2D children's cartoon style, smooth soft shading, thick friendly outlines, simple shapes easy to animate, pastel colors, preschool animation look, no text.
```

**영상 프롬프트 (`ep01_c02.mp4`, 장면 05 그림 → 5초)**
```
The three horns light up one by one, pink, then blue, then yellow, with soft twinkling sparkles. Chiqui's eyes widen into a bright smile. Gentle magical glow, slow camera push-in.
```

## 장면 06 — 브론티에게 "안녕!"

**나레이션**: 치키는 용기를 내서 브론티에게 갔어요.
**치키**: 용기를 내서… 안녕! 나는 치키야!
**브론티**: 안녕, 치키! 천천히 해도 괜찮아.

**이미지 프롬프트 (`ep01_s06.png`)**
```
<<<CHIQUI>>> Chiqui standing bravely and waving one front foot up at <<<BRONTI>>> Bronti the tall sky-blue brontosaurus, who lowers her long neck kindly so her head is close to Chiqui, warm smile. Chiqui's pink horn glows softly. Lakeside meadow with flowers. Clean 2D children's cartoon style, smooth soft shading, thick friendly outlines, simple shapes easy to animate, pastel colors, preschool animation look, no text.
```

## 장면 07 — 피코에게 "Hello!"

**나레이션**: 하늘에서 피코가 슝 내려왔어요.
**치키**: Hello! 나는 치키야!
**피코**: Hello! 내가 먼저 보고 올게… 아니, 벌써 친구다!

**이미지 프롬프트 (`ep01_s07.png`)**
```
<<<PICO>>> Pico the butter-yellow baby pteranodon swooping down from the sky with wings spread wide and a cheeky grin, toward <<<CHIQUI>>> Chiqui who is waving up happily. Chiqui's blue horn glows softly. Bright blue sky with fluffy clouds. Clean 2D children's cartoon style, smooth soft shading, thick friendly outlines, simple shapes easy to animate, pastel colors, preschool animation look, no text.
```

**영상 프롬프트 (`ep01_c03.mp4`, 장면 07 그림 → 5초)**
```
Pico swoops down in a playful loop and lands softly in front of Chiqui, flapping both wings. Chiqui waves back happily. Light breeze moves the grass. Smooth cheerful motion.
```

## 장면 08 — 티노에게 "Hola!"

**나레이션**: 나무 뒤에 티노가 살짝 숨어 있었어요.
**치키**: Hola! 나는 치키야!
**티노**: 나도… 나도 같이 해도 돼?
**치키**: 그럼! 우리 같이 놀자!

**이미지 프롬프트 (`ep01_s08.png`)**
```
<<<TINO>>> Tino the shy tangerine-orange baby tyrannosaurus half hiding behind a big tree trunk, tiny arms held together, blushing with a gentle nervous smile. <<<CHIQUI>>> Chiqui stands in front of Tino with a warm friendly smile, one front foot raised in greeting. Chiqui's golden yellow horn glows softly. Soft forest edge. Clean 2D children's cartoon style, smooth soft shading, thick friendly outlines, simple shapes easy to animate, pastel colors, preschool animation look, no text.
```

**영상 프롬프트 (`ep01_c04.mp4`, 장면 08 그림 → 5초)**
```
Tino slowly peeks out from behind the tree, hesitates, then steps out and gives a small shy wave. Tino's nervous smile turns into a happy smile. Gentle, slow, heartwarming motion.
```

## 장면 09 — 넷은 첫 친구 (오프닝 노래 다 같이)

**나레이션**: 먼저 인사했더니, 친구가 세 명이나 생겼어요.
**모두**: 안녕! 헬로! 올라!
**노래**: 오프닝 "치키의 인사 노래"를 넷이 처음으로 함께 부른다 (동요 포인트, 숏폼 구간)

**이미지 프롬프트 (`ep01_s09.png`)**
```
<<<CHIQUI>>> Chiqui, <<<BRONTI>>> Bronti, <<<PICO>>> Pico and <<<TINO>>> Tino standing together in a row on a grassy hill by the lake, all smiling and waving at the viewer, Pico hovering just above. Chiqui's three horns glow softly in pink, blue and yellow. Golden afternoon light, rainbow in the sky. Clean 2D children's cartoon style, smooth soft shading, thick friendly outlines, simple shapes easy to animate, pastel colors, preschool animation look, no text.
```

**영상 프롬프트 (`ep01_c05.mp4`, 장면 09 그림 → 5초)**
```
The four friends bounce happily in rhythm as if singing together, Pico flaps its wings, Bronti sways her long neck, Tino and Chiqui hop. Joyful, rhythmic, simple dance motion. Camera stays still.
```

## 장면 10 — 오늘의 교훈 + 엔딩 노래

**나레이션**: 먼저 인사하면 친구가 생겨요. 여러분도 오늘 인사해 볼까요?
**치키**: 안녕! 또 만나!
**노래**: 엔딩 "또 만나요 노래" (`songs.md`)

**이미지 프롬프트 (`ep01_s10.png`)**
```
Sunset over Rainbow Valley. <<<CHIQUI>>> Chiqui in the center front, waving goodbye directly at the viewer with a big happy smile, friends <<<BRONTI>>> Bronti, <<<PICO>>> Pico and <<<TINO>>> Tino behind also waving. Warm orange and pink sky, first stars appearing. Clean 2D children's cartoon style, smooth soft shading, thick friendly outlines, simple shapes easy to animate, pastel colors, preschool animation look, no text.
```

---

## 숏폼 (9:16) — 장면 09 동요 구간

**이미지 프롬프트 (`ep01_s09_vertical.png`)**
```
Vertical composition. <<<CHIQUI>>> Chiqui in the front center, <<<TINO>>> Tino and <<<BRONTI>>> Bronti behind, <<<PICO>>> Pico flying above at the top of the frame, all waving at the viewer and smiling. Chiqui's three horns glow softly in pink, blue and yellow. Grassy hill, rainbow in the sky. Clean 2D children's cartoon style, smooth soft shading, thick friendly outlines, simple shapes easy to animate, pastel colors, preschool animation look, no text.
```

## TTS 목소리 방향 (세 언어 공통)

| 역할 | 목소리 방향 |
| --- | --- |
| 나레이터 | 따뜻하고 차분한 성인 여성, 동화 읽어주듯 천천히 |
| 치키 | 밝고 높은 어린아이 목소리, 호기심 많고 약간 빠르게 |
| 브론티 | 부드럽고 느긋한 언니 목소리, 천천히 |
| 피코 | 장난스럽고 톡톡 튀는 어린아이 목소리, 빠르게 |
| 티노 | 작고 수줍은 어린아이 목소리, 말끝이 살짝 작아짐 |
