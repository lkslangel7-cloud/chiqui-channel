# 1화 진행 상태

## 한국어판: 완료 · 한국어 채널에 업로드함 (2026-11-16)

- 최종 영상: `output/ep01_ko_v5.mp4` (화면 자막), `output/ep01_ko_nosubs.mp4` + `subtitles_ko.srt`
  - mp4는 git에 없음. 다시 만들 때: `python3 -I scripts/assemble_episode.py episodes/ep01 output/ep01_ko_v5.mp4` (`--no-subs` 옵션 가능)
- 편집 정보: `edit_order.json` (영상 30컷, 대사, 노래·배경음악 위치, 노래 가사 자막)
- 노래: `audio/songs/` opening·egg_song·ending·bgm (Suno). 이전 오프닝·엔딩은 `*_v1.wav`
- 업로드 정보: `upload_info.md`, 썸네일 `thumbnail.png`

## 영어판·스페인어판: 아직 (사용자가 요청하면 만든다)

1. `lyrics_en.md`, `lyrics_es.md` — 한국어 노래와 같은 박자·같은 자리로 다듬은 가사 (번역 아님)
2. 노래 프롬프트 페이지 (`prompts/build_song_page.py` 참고) → 사용자가 Suno로 오프닝·알 찾기 노래·엔딩 제작 (배경음악 bgm.wav는 그대로)
3. 대사 음성: `edit_order.json`의 lines를 해당 언어로 (elevenlabs_v4, 같은 목소리 ID), 길이 차이는 at 값으로 조정
4. `edit_order_en.json` / `edit_order_es.json` 만들어 같은 클립으로 조립 → 화면 자막판, 자막 없는 판, SRT
5. 썸네일은 이미 있음: `thumbnail_en.png`, `thumbnail_es.png`
6. 언어별 제목·설명·태그, 채널 배너·설명(`branding/`)
