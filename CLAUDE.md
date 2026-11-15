# 치키의 공룡 마을 — 어린이 동요·스토리 영상 프로젝트

이 프로젝트는 아기 공룡 "치키(Chiqui)"가 주인공인 어린이 영상 시리즈를 Higgsfield로 제작하는 작업 공간이다.
대본·가사는 Claude 채팅에서 확정해 `episodes/` 폴더에 넣고, Claude Code는 그걸 받아 이미지·영상·음성을 생성하고 정리한다.
최종 편집은 캡컷에서 사람이 직접 한다.

## 1. 기본 정보

- 대상: 2~6세
- 언어: 한국어(원본) → 영어, 스페인어
- 길이: 본편 1~2분 노래/스토리 영상 + 쇼츠·릴스용 30초 컷
- 예산: 한 달 약 10만원, 월 3편 목표. 크레딧 소모가 큰 작업은 실행 전 반드시 비용을 먼저 알려주고 확인받는다.

## 2. 캐릭터 (반드시 레퍼런스 시트 기준으로 일관성 유지)

| 캐릭터 | 종 | 색 | 성격 / 특징 | 기준 시안 |
|---|---|---|---|---|
| 치키 (Chiqui) | 아기 트리케라톱스 | 주황 | 주인공. 호기심 많고 덤벙댐. 캐치프레이즈 "치키치키 출발!" | `characters/candidates/A_chiqui.png` |
| 옥이 (Okki) | 아기 문어 | 분홍 (기분에 따라 몸 색이 바뀜) | 다정한 장난꾸러기. "옥이옥이 짠!" 색깔·숫자(다리 8개)·감정 담당 | `characters/candidates/B_okki.png` |
| 주주 (Zuzu) | 꼬마 꿀벌 | 노랑·갈색 줄무늬, 꽃 가방 | 부지런한 도우미. "붕붕 도와줄게!" 돕기·나누기, 춤 동요 담당 | `characters/candidates/D_zuzu.png` |
| 포실이 (Posil) | 아기 알파카 | 하양 털, 분홍 머리털, 무지개 목도리 | 수줍고 다정함. 겁이 많지만 친구를 잘 챙김 | `characters/candidates/K_alpaca.png` |
| 부리 박사님 (Dr. Buri / Doctor Buri) | 아기 부엉이 | 청록·크림, 머리 위 안경, 책 | 아는 게 많은 박사님, 상식 코너 담당 | `characters/candidates/J_owl.png` |

- 출연진 확정: 2026-11-15. 이름은 세 언어 공통. 앞서 정했던 토롱·피오·바우 할아버지는 쓰지 않는다.
- 각 캐릭터 시안의 Higgsfield Job ID는 `characters/candidates/README.md`에 있다. 레퍼런스 시트가 완성되면 `characters/`에 저장하고 이 표의 기준 시안을 교체한다.
- 배경: 알록달록한 화산섬 마을 (옥이가 사는 바닷가 석호, 주주의 꽃밭, 포실이의 풀밭 언덕, 부리 박사님의 나무 위 도서관)
- 화풍: 부드러운 3D 장난감(클레이)풍. 후보 시안 프롬프트의 문구를 모든 생성에 그대로 붙인다:
  `Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers`

## 3. 에피소드 구성 원칙

- 같은 후렴 틀에 가사만 바꾸는 "시리즈형 후렴"을 기본으로 한다.
- 주제 예시: 양치·손 씻기 생활습관, 1~10 숫자 세기, 색깔 숨바꼭질(옥이), 감정 이름 붙이기(옥이의 몸 색), 부리 박사님의 상식 코너
- 더빙 친화적으로 구성: 캐릭터 입이 크게 움직이는 클로즈업 대사보다 춤·걷기·놀이 장면과 내레이션 위주로 간다.

## 4. 제작 파이프라인 (에피소드 1편 기준)

1. `episodes/epXX/script.md`에서 대본과 장면 목록을 읽는다.
2. 캐릭터 레퍼런스(Higgsfield Elements/캐릭터)를 사용해 장면별 이미지를 생성한다.
3. 장면 이미지로 4~8초 영상 클립을 10~15개 생성한다.
4. 한국어 노래/내레이션 음성을 생성한다.
5. 영어·스페인어 음성을 만든다. **동요 가사는 단순 번역 더빙 대신 `lyrics_en.md`, `lyrics_es.md`에 따로 다듬은 가사로 음성을 생성한다.** (운율 유지)
6. 결과물을 아래 폴더 구조대로 저장하고, 클립 순서표(`edit_order.md`)를 만들어 캡컷 편집에 넘긴다.

## 5. 폴더 구조

```
episodes/
  ep01/
    script.md        # 대본 + 장면 목록 (채팅에서 작성)
    lyrics_ko.md
    lyrics_en.md
    lyrics_es.md
    images/          # 장면 이미지
    clips/           # 영상 클립
    audio/           # ko / en / es 음성
    edit_order.md    # 캡컷용 클립 순서표
characters/          # 캐릭터 레퍼런스 시트
```

## 6. 업로드 전략

- 유튜브: **채널 1개**. 한국어 원본에 영어·스페인어 음성을 다국어 오디오 트랙으로 추가한다. 언어별 음성 파일을 따로 내보내 둔다.
- 인스타그램·틱톡: **언어별 계정 분리**. 처음엔 1~2개 언어만 운영하고, 유튜브 언어 트랙 반응을 보고 확장한다.
- 채널명에 "디노(Dino)"는 쓰지 않는다.

## 7. Higgsfield 연결

Claude Code에서 Higgsfield MCP를 연결해 사용한다.

```
claude mcp add --transport http higgsfield https://mcp.higgsfield.ai/mcp
```

## 8. 작업 규칙

- 생성 전 예상 크레딧을 먼저 보여주고 확인받는다.
- 캐릭터 외형이 레퍼런스와 다르게 나오면 다음 단계로 넘어가지 말고 재생성 여부를 묻는다.
- 실존 캐릭터·브랜드와 닮은 디자인은 피한다.

## 참고: 이전 버전 (레인보우 밸리)

이 문서 이전에 만든 1화 「치키의 세 가지 인사」 자료(`assets/`, `audio/`, `remotion/`, `characters.md`, `pipeline.md`, `songs.md`, `episodes/ep01_*`)는 이전 설정(연두색 치키, 브론티·피코·티노) 기준이다. 이전 규칙은 `archive/CLAUDE_v1_rainbow_valley.md`에 있다. 새 설정과 다르므로 그대로 이어 쓰지 말고, 재사용 여부는 사용자에게 확인한다.
