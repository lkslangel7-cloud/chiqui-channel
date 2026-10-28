# 캐릭터 설정

## 세계관

치키와 친구들은 화산 너머 작은 섬, **레인보우 밸리**에 산다. 숲, 호수, 구름 언덕, 별이 잘 보이는 언덕이 있어 에피소드마다 배경을 바꿔 쓸 수 있다. 한 편은 3~5분, 아이들이 일상에서 겪는 감정과 습관(인사, 나눔, 양치, 잠자리)을 다룬다.

## 캐릭터 표

| 이름 | 공룡 종류 | 성격 | 말버릇 | 색깔 |
| --- | --- | --- | --- | --- |
| 치키 (Chiqui) | 아기 트리케라톱스 | 호기심 많고 질문이 끝없음, 가끔 서두르다 실수 | "왜 그럴까?" | 연두색 |
| 브론티 (Bronti) | 브론토사우루스 | 키 크고 느긋한 맏언니, 친구들을 챙김 | "천천히 해도 괜찮아." | 하늘색 |
| 피코 (Pico) | 아기 프테라노돈 | 장난꾸러기, 하늘을 날며 소식을 전함 | "내가 먼저 보고 올게!" | 노란색 |
| 티노 (Tino) | 아기 티라노사우루스 | 울음소리는 크지만 수줍음 많고 다정함 | "나도 같이 해도 돼?" | 주황색 |

- 치키의 뿔 세 개 = "뿔 하나마다 다른 나라 말을 기억하는 공룡" (채널 소개 문구로 활용)
- 피코(Pico)는 스페인어로 "부리"라는 뜻

## 공통 스타일 프롬프트

모든 이미지 프롬프트 끝에 붙인다.

```
Clean 2D children's cartoon style, smooth soft shading, thick friendly outlines, simple shapes easy to animate, pastel colors, preschool animation look, no text.
```

## 캐릭터 기준 이미지 프롬프트

### 치키 (Chiqui)
```
Character design of Chiqui, a cute baby triceratops. Soft light lime-green body with a cream-colored belly, round chubby body, big sparkling dark eyes with white highlights, rosy cheeks, small friendly smile. Three short rounded horns (two above the eyes, one small on the nose) in pale peach, small rounded frill with tiny pastel dots. Short stubby legs, tiny tail. Curious cheerful expression, full-body front three-quarter view, waving one front foot hello. Plain white background.
```

### 브론티 (Bronti)
```
Character design of Bronti, a gentle young brontosaurus. Soft sky-blue body with a pale cream belly, very long graceful neck, small round head, calm half-closed kind eyes, warm smile, a few lighter blue spots on the back. Tall but soft and rounded, motherly big-sister feeling. Full-body side three-quarter view, head lowered kindly. Plain white background.
```

### 피코 (Pico)
```
Character design of Pico, a playful baby pteranodon. Bright butter-yellow body, light orange wing membranes, small pointed crest on the head, short rounded beak, big mischievous eyes, cheeky grin. Small round body, wings spread wide mid-flight. Full-body front view. Plain white background.
```

### 티노 (Tino)
```
Character design of Tino, a shy baby tyrannosaurus. Soft tangerine-orange body with a cream belly, big head, tiny short arms held together shyly, small rounded teeth showing in a gentle nervous smile, big round eyes, slightly blushing cheeks. Chubby and cute, not scary at all. Full-body front three-quarter view. Plain white background.
```

## 일관성 유지 방법

1. 위 프롬프트로 시안을 만들고 사용자가 고른 이미지를 `assets/characters/`에 저장한다.
2. Higgsfield에서 고른 이미지를 레퍼런스 Element로 등록하고 Element ID를 아래에 기록한다.
3. 이후 장면 생성 프롬프트에는 Element ID 플레이스홀더(`<<<ID>>>`)를 넣어 같은 모습을 유지한다.

| 캐릭터 | Element ID | 기준 이미지 Job ID (1차 시안) |
| --- | --- | --- |
| 치키 | (등록 후 기입) | 5d664a1a-9713-4137-a9f1-a9b0158ab950 |
| 브론티 | (등록 후 기입) | cbd8415f-1f31-4336-873b-41bb40a643be |
| 피코 | (등록 후 기입) | ae98cf54-428b-4643-8f8b-60377f756e4d |
| 티노 | (등록 후 기입) | 76bb8130-38a3-47a4-a731-9a51025b2da6 |

- 1차 시안: 2026-10-28, GPT Image 2 (medium, 1:1, 장당 1크레딧). 파일은 `assets/characters/`.
- Job ID는 장면 생성 시 레퍼런스 이미지(`medias`)로 바로 넣을 수 있다.

## 확정된 제작 방식 (1화에서 검증, 2026-10-28)

- 장면 그림: `gpt_image_2_5`, quality `medium`, 16:9, 위 기준 이미지 Job ID를 `image_references`로 넣고 프롬프트 첫머리에 "Use the reference images as the exact character designs: 1 Chiqui …"처럼 순서대로 이름을 붙인다. 이 방식으로 1화 장면 18장 모두 캐릭터가 일관되게 나왔다.
- 영상 조각: `kling3_0`, mode `std`, sound `off`, 장면 그림 Job ID를 `start_image`로. 프롬프트 끝에 "Keep the flat 2D cartoon style and character designs unchanged."

## 캐릭터 목소리 (ElevenLabs v4, `elevenlabs_v4` 모델)

Seed Audio 기본 음성은 한국어 억양이 어색해서 쓰지 않는다.

| 역할 | 프리셋 이름 | voice_id |
| --- | --- | --- |
| 나레이터 | Hana | c25f78a0-714e-42af-8da3-a399cef94968 |
| 치키 | Pixie | 0178ef57-ada4-43d9-992b-8d9221045bb4 |
| 브론티 | Luna | 375a3398-e3b4-4f91-845d-42181e352899 |
| 피코 | Kayla | 5c615d8a-5135-539d-8ab0-497b7ceabbae |
| 티노 | Zoe | d0374db1-44b9-4f05-939e-0a9ae9dbbe6a |
