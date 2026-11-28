# 새 대화 시작용 인수인계 (2026-11-26)

새 대화의 Claude는 이 파일과 CLAUDE.md를 먼저 읽고 이어서 한다. 규칙은 모두 CLAUDE.md에 있다.

## 새 컨테이너에서 가장 먼저 (중요)

합격 그림·영상(약 6GB)과 `output/*.mp4`는 용량 때문에 git에 없다. 새 대화는 빈 컨테이너에서 시작하므로:

1. 합격 그림·영상: `python3 -I tools/restore_media.py` (전부) 또는 `python3 -I tools/restore_media.py ep32 ep33`(필요한 화만)
   - `tools/media_manifest.txt`(1052개)의 파일 이름 끝 11글자가 공유 코드라서 Higgsfield에서 같은 파일을 다시 받는다(테스트에서 바이트까지 동일).
   - 로컬로 고친 파일(`_fix`·`_bright`·`_local_zoom`, ep24 S04·S07 그림)은 git에 들어 있다.
   - 새로 합격시키면 manifest에 한 줄 추가한다: `ls episodes/*/images/web/* episodes/*/clips/web/* > tools/media_manifest.txt`
2. 완성 영상(9~12화 hq.mp4)은 클립을 받은 뒤 다시 조립하거나, 완성 영상 페이지에서 내려받는다.

## 페이지 (아티팩트, 같은 URL에 계속 다시 올림)

- 완성 영상 + 진행 현황 탭: https://claude.ai/artifact/VrXoeRAAETxzuRQbFUxKJ6
  - 만들기: `python3 prompts/build_video_page.py <스크래치패드>/videopage`
  - 올리기: index.html. 새로 완성한 화는 `v/epXX.mp4`·`t/epXX.jpg`·`th/epXX.jpg`도 `files`로 올린다(바꿀 때는 `overwrite_unread`).
  - 새 대화에서는 먼저 Artifact `read`로 이 URL을 읽어야 다시 올릴 수 있다.
- 쇼츠 미리보기: https://claude.ai/artifact/AHwnLSqUeQMDebTUCyaX7L (`prompts/build_shorts_page.py`)
- 화별 장면·노래 페이지: `episodes/pages.json`
  - 장면 페이지 다시 만들기: `prompts/build_scene_page.py episodes/epXX "N화. 제목"`

## 진행 상태 (2026-11-28 새벽 기준 · 정확한 수는 완성 영상 페이지 「진행 현황」 탭)

| 화 | 상태 |
|---|---|
| 1~8화 | 유튜브 업로드 완료 |
| 9~14화 | 고화질 완성 (`output/epXX_ko_vN_hq.mp4` + .srt, upload_info.md, 썸네일). 14화는 2026-11-27 완성 |
| 15~43화 | 그림·영상 16/16, **노래(Suno) 기다림** → 노래가 오면 아래 「한 화 완성하기」 |
| 44·45화 | 그림 16/16, 영상 시작 전 |
| 46~49화 | 그림 16/16, 영상 시작 전 (47화 JVEbHWoxe5M = S16 바우 영상일 수 있음, 아직 확인 안 함) |
| 50~60화 | 대본·가사·프롬프트 완료, 그림 시작 전. 48화(퍼즐), 50화(치키 타운 한 바퀴), 59·60화는 이야기를 새로 바꿈 |

- 웹 무제한은 2026-11-29(일)까지였는데 영상(Seedance)은 11-28에 이미 끝남, 그림(GPT Image 2.6)은 아직 무제한. (2026-11-28 사용자 결정) 남은 영상(49~58화 약 140개, 59·60화)은 그림책식(정지 그림) 조립 없이 **다음 달 크레딧이 나오면 그걸로 만든다**. 영상 1개 Kling 3.0 5초 = 10크레딧(11-28 잔액 39.6). 만들기 전에 매번 예상 크레딧을 알려 주고 확인받는다.
- 20화(크리스마스, 폴더 ep25)는 12월 중순 전에 올린다. 방송 번호는 `episodes/upload_order.json`을 따른다.
- 36화는 「고마워!」로 바꿨다. 가을 낙엽 주제는 `prompts/keep_ep36_fall.py`에 보관(내년용).

## 작업 방법

- 사용자가 Higgsfield 웹에서 만들고 `https://higgsfield.ai/s/CODE` 링크를 보낸다.
- 받기와 장면 맞추기:
  - `python3 -I tools/fetch_any.py <dir> CODE…` — 내려받으며 프롬프트로 장면을 찾는다.
  - `EP=epXX python3 -I tools/matchep.py <dir> -- CODE…` — `S##_CODE.png`로 이름을 바꾼다.
  - `tools/matchall.py` — 26~40화 전체에서 비슷한 프롬프트 상위 3개를 보여 준다.
- 합격 파일 저장 위치: `episodes/epXX/images/web/S##_CODE.png`, `clips/web/S##_CODE.mp4`. 공통 컷은 `episodes/common/`.
- 확인 방법:
  - 영상은 1초 간격 프레임 전부와 합격 그림을 한 장에 모아 본다.
  - (2026-11-26) 영상 링크는 `python3 -I tools/check_video.py CODE…` 한 줄로 받기+장면 찾기+한 장 만들기(허락 안 물음). 합격은 `python3 -I tools/check_video.py --accept epXX S## CODE "STATUS 한 줄"`. 셸 변수·for·&& 를 섞은 긴 명령은 허락을 물으니 쓰지 않는다.
  - (2026-11-27) 그림 링크도 한 줄: `python3 -I tools/check_image.py --ep epXX CODE…` → `/tmp/chiqui_check/CODE/view.jpg`(Read로 봄)와 `/tmp/chiqui_check/epXX_all.jpg`(그 화 합격 그림+새 그림 한 장). 소품 잘라 대조: `--crop epXX:S05 x0 y0 x1 y1 CODE x0 y0 x1 y1` → `crop.jpg`. 합격: `--accept epXX S## CODE "STATUS 한 줄"`(복사·manifest·STATUS·장면 페이지). 셸 변수·for·;·&& 를 쓰면 허락을 물으니 쓰지 않는다.
  - 반복 소품은 크게 잘라 특징 3~4개를 대조한다.
  - (2026-11-27) **뜻 확인**: 그림마다 "아이가 보면 무엇을 하는 장면인가"를 한 문장으로 쓰고 장면 이름과 맞춘다. 프롬프트대로 그려졌어도 뜻이 다르면 불합격(42화 S12: 코를 대야에 넣음 → 손 씻기가 아니라 물 마시기로 보임).
  - 화면을 보는지/대상을 보는지, 자세(앉음·누움), 소품 상태(켜짐·꺼짐·있음·없음)를 장면마다 적어 앞뒤 장면과 대조한다.
  - 다른 대화가 같은 화를 바꿨을 수 있다: 확인 전에 `git fetch` 후 그 화 STATUS.md 끝과 images/web 파일을 먼저 본다(39화: 돗자리를 없앤 새 그림이 있었는데 옛 그림과 비교해 잘못 불합격 줄 뻔함).
- 영상 프롬프트: 모든 영상 끝에 LOCK(카메라·크기·자리·소품 고정)이 자동으로 붙는다. 그림이 합격하면 영상 만들기 전에 합격 그림을 보고 make_ep26_40.py / make_ep41_45.py의 VIDFIX에 장면마다 동작을 다시 적는다(제자리 동작, 그림 속 자세·소품 상태). 생성기를 돌린 뒤에는 그 화 scenes.json의 vid만 바꾸고 img와 다른 화는 git으로 되돌린다.
- 그림 프롬프트 생성기: `prompts/make_ep26_40.py`. 다시 생성하면 다른 화의 STATUS.md는 되돌린다.
- 조립:
  - 11~12화 방식: `python3 -I scripts/build_ep11_15.py epXX` (노래 파일·길이를 거기에 추가)
  - 기본 2560×1440 고화질. **조립은 한 번에 하나만** 돌린다(동시에 돌리면 파일이 깨짐).
- 음성: elevenlabs_v4, 줄당 약 0.23크레딧. **크레딧을 쓰기 전에 반드시 비용을 알리고 확인받는다.**
  - voice_id: 치키 0178ef57-ada4-43d9-992b-8d9221045bb4, 바우 ca12fd00-218c-5198-b10c-7d36e768c12c, 내레이션 c25f78a0-714e-42af-8da3-a399cef94968, 로로 5c615d8a-5135-539d-8ab0-497b7ceabbae
- 커밋: `git -c user.name=lkslangel7 -c user.email=lkslangel7@gmail.com commit` 후 push.

## 나중에 할 일

- 11화부터 쇼츠 만들기
- 모음집 (1시간짜리 포함)
- 영어·스페인어판
- 업스케일 테스트 (선택)

## 한 화 완성하기 (14화에서 한 그대로)

1. 노래 wav를 `episodes/epXX/audio/songs/<이름>.wav`로 저장, faster-whisper(small, word_timestamps)로 받아써서 후렴·1~4절 시작 시각을 잰다.
2. 음성: 대본 「대사 모음」에서 새 줄만 elevenlabs_v4로(모두 = 치키+로로 두 목소리를 60ms 어긋나게 amix). 와아·안녕 등 ♻ 표시는 1화 파일 복사. **만들기 전에 크레딧(줄당 0.23)을 알리고 확인받는다.** 받아쓰기로 대사 확인.
3. `scripts/build_ep11_15.py`에 그 화 build(...) 추가 → edit_order.json. 노래 앞 첫 구간이 15초를 넘으면 1화 달리기 + 2화 출발로 나눈다(14화 블록 참고). 촛불 끄기처럼 대사와 동작이 맞아야 하는 컷은 speed로 늦춘다.
4. `python3 -I scripts/assemble_episode.py episodes/epXX output/epXX_ko_v1_hq.mp4` (백그라운드, 한 번에 하나). 3초 간격 프레임으로 전체 확인.
5. 썸네일 `scripts/make_thumbnail.py` (다리 수 맞는 합격 그림으로), 영어·스페인어용은 글자 없이 1280×720. upload_info.md는 13·14화 틀 그대로.
6. videos.json에 "file" 넣고 완성 영상 페이지 다시 만들기. **이 컨테이너에 output/*.mp4가 없으면 1~13화 길이가 0:00이 되므로**, 올라가 있는 페이지(Artifact read path=index.html)의 완성 화 패널을 새 index.html에 그대로 붙여 넣고 올린다. 새 화는 v/·t/·th/ 파일도 files로.
7. 완성 mp4는 git에 안 들어가니 SendUserFile로 사용자에게 보낸다.

## 확인할 때 자주 놓친 것 (2026-11-27 사용자 지적 모음)

- 네 발 친구(치키·바우·토롱) 발은 크게 잘라 하나씩 센다. 토롱·바우가 "손 흔들기·손 뻗기·제자리걸음"이 들어간 문장은 그림 만들기 전에 고친다(목 갸웃·끄덕임으로).
- 앞뒤 장면에서 친구 자리(왼쪽/오른쪽), 소품(퍼즐·북·상 위 음식)이 이어지는지 본다. 48화 S09: 바우·로로 자리가 앞뒤 장면과 반대여서 불합격.
- 크기를 억지로 바꾸지 않는다: "피오가 꽃보다 작다", "목이 세 배로 길다"는 말이 안 됨(49화). 비교는 바위·나무처럼 원래 큰 것과.
- 영상 프롬프트에 그 장면 소품(북 등)을 꼭 적는다. 안 적으면 사라진다(43화 S16). 코로 치기 같은 동작은 코가 늘어난다(43화 S02).
- 새 화 이야기는 앞 화와 겹치는지 본다(48화 ↔ 33화 블록 탑, 50화 깜짝 파티 ↔ 14화).
- 프롬프트를 고치면 장면 페이지·노래 페이지·진행 현황까지 모두 다시 올린다(CLAUDE.md 끝).
- 같은 링크를 다시 보내면 "이미 합격한 그림"이라고 알려 준다. 다른 화 링크가 섞여 오면 어느 화인지 찾아 알려 준다.

