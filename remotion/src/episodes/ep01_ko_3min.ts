import type { Episode } from "../types";

// scripts/build_episode.py가 ep01_ko_3min.json에서 생성한 파일. 직접 고치지 말고 스펙을 고친 뒤 다시 생성한다.
// 전체 길이 187.8초
export const ep01Ko3min: Episode = {
  title: "치키의 세 가지 인사",
  bgm: "audio/bgm_3min.wav",
  scenes: [
    {
      kind: "image",
      src: "scenes/ep01_s01.png",
      duration: 5.00,
      lines: [
        
      ],
    },
    {
      kind: "video",
      src: "clips/ep01_c01.mp4",
      duration: 9.25,
      lines: [
        { at: 0.5, audio: "audio/k01.wav", speaker: "나레이션", text: "화산 너머 작은 섬, 레인보우 밸리예요." },
        { at: 4.45, audio: "audio/k02.wav", speaker: "나레이션", text: "숲도 있고, 호수도 있고, 구름 언덕도 있어요." }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s02.png",
      duration: 8.15,
      lines: [
        { at: 0.5, audio: "audio/l01_narr.wav", speaker: "나레이션", text: "레인보우 밸리에 아기 공룡 치키가 이사 왔어요." },
        { at: 4.66, audio: "audio/k03.wav", speaker: "치키", text: "와, 여기가 우리 새 동네야!" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s11.png",
      duration: 6.61,
      lines: [
        { at: 0.5, audio: "audio/k04.wav", speaker: "치키", text: "짐 정리 끝! 이제 뭐 하고 놀지?" },
        { at: 3.79, audio: "audio/k05.wav", speaker: "치키", text: "그래, 친구를 찾아보자!" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s03.png",
      duration: 6.23,
      lines: [
        { at: 0.5, audio: "audio/k06.wav", speaker: "나레이션", text: "호숫가에서 신나는 소리가 들려요." },
        { at: 3.58, audio: "audio/k07.wav", speaker: "치키", text: "우와, 친구들이다!" }
      ],
    },
    {
      kind: "video",
      src: "clips/ep01_c06.mp4",
      duration: 7.89,
      lines: [
        { at: 0.5, audio: "audio/k08.wav", speaker: "피코", text: "누가 누가 멀리 던지나! 하나, 둘, 셋!" },
        { at: 5.06, audio: "audio/k09.wav", speaker: "티노", text: "우와, 피코 최고!" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s04.png",
      duration: 8.48,
      lines: [
        { at: 0.5, audio: "audio/l02_narr.wav", speaker: "나레이션", text: "친구를 사귀고 싶지만, 너무 부끄러웠어요." },
        { at: 4.52, audio: "audio/k10.wav", speaker: "치키", text: "뭐라고 말을 걸지? 왜 이렇게 떨릴까?" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s13.png",
      duration: 8.02,
      lines: [
        { at: 0.5, audio: "audio/k11.wav", speaker: "나레이션", text: "치키는 그만 혼자 돌아서고 말았어요." },
        { at: 3.92, audio: "audio/k12.wav", speaker: "치키", text: "나는… 친구를 못 사귈지도 몰라." }
      ],
    },
    {
      kind: "video",
      src: "clips/ep01_c02.mp4",
      duration: 7.52,
      lines: [
        { at: 0.5, audio: "audio/l03_narr.wav", speaker: "나레이션", text: "그때, 뿔 세 개가 반짝 빛났어요!" },
        { at: 4.27, audio: "audio/l04_chiqui.wav", speaker: "치키", text: "안녕! Hello! Hola!" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s05.png",
      duration: 9.92,
      lines: [
        { at: 0.5, audio: "audio/k13.wav", speaker: "나레이션", text: "뿔 하나마다 다른 나라 인사를 알려 줬어요." },
        { at: 4.28, audio: "audio/k14.wav", speaker: "치키", text: "인사하는 방법이 세 가지나 있네!" },
        { at: 7.29, audio: "audio/k15.wav", speaker: "치키", text: "좋아, 용기를 내 보자!" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s14.png",
      duration: 7.54,
      lines: [
        { at: 0.5, audio: "audio/k16.wav", speaker: "나레이션", text: "치키는 먼저 키 큰 브론티에게 다가갔어요." },
        { at: 4.45, audio: "audio/k17.wav", speaker: "치키", text: "두근두근… 할 수 있어!" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s06.png",
      duration: 9.61,
      lines: [
        { at: 0.5, audio: "audio/l05_chiqui.wav", speaker: "치키", text: "안녕! 나는 치키야!" },
        { at: 2.98, audio: "audio/l06_bronti.wav", speaker: "브론티", text: "안녕, 치키! 반가워." },
        { at: 5.74, audio: "audio/k18b.wav", speaker: "브론티", text: "우리 같이 놀래?" },
        { at: 7.59, audio: "audio/k19.wav", speaker: "치키", text: "응, 좋아!" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s15.png",
      duration: 10.17,
      lines: [
        { at: 0.5, audio: "audio/k20.wav", speaker: "나레이션", text: "그때, 하늘에서 누군가 슝 내려왔어요." },
        { at: 4.84, audio: "audio/k41.wav", speaker: "피코", text: "어? 새로운 친구가 왔나?" },
        { at: 7.53, audio: "audio/k21.wav", speaker: "피코", text: "내가 먼저 보고 올게!" }
      ],
    },
    {
      kind: "video",
      src: "clips/ep01_c03.mp4",
      duration: 4.47,
      lines: [
        { at: 0.5, audio: "audio/l07_chiqui.wav", speaker: "치키", text: "Hello!" },
        { at: 1.7, audio: "audio/l08_pico.wav", speaker: "피코", text: "Hello! 나는 피코야!" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s07.png",
      duration: 8.55,
      lines: [
        { at: 0.5, audio: "audio/k22.wav", speaker: "피코", text: "너 새로 왔구나? 하늘에서 다 봤지!" },
        { at: 4.45, audio: "audio/k23.wav", speaker: "치키", text: "피코, 하늘을 나는 거 정말 멋지다!" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s16.png",
      duration: 11.40,
      lines: [
        { at: 0.5, audio: "audio/k24.wav", speaker: "나레이션", text: "그런데 나무 뒤에서 누가 살짝 보고 있었어요." },
        { at: 4.84, audio: "audio/k25.wav", speaker: "치키", text: "어? 저기 누구지?" },
        { at: 7.35, audio: "audio/k26.wav", speaker: "피코", text: "아, 티노야! 부끄럼쟁이 티노!" }
      ],
    },
    {
      kind: "video",
      src: "clips/ep01_c04.mp4",
      duration: 4.88,
      lines: [
        { at: 0.5, audio: "audio/l09_chiqui.wav", speaker: "치키", text: "Hola!" },
        { at: 1.7, audio: "audio/l10b_tino.wav", speaker: "티노", text: "나도… 같이 놀아도 돼?" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s08.png",
      duration: 11.43,
      lines: [
        { at: 0.5, audio: "audio/k27.wav", speaker: "치키", text: "그럼! 우리 같이 놀자!" },
        { at: 2.94, audio: "audio/k28.wav", speaker: "티노", text: "고마워. 사실 나도 인사하고 싶었는데, 부끄러웠어." },
        { at: 8.09, audio: "audio/k29.wav", speaker: "치키", text: "나도 그랬어! 우리 똑같다!" }
      ],
    },
    {
      kind: "video",
      src: "clips/ep01_c07.mp4",
      duration: 8.62,
      lines: [
        { at: 0.5, audio: "audio/k30.wav", speaker: "브론티", text: "우리 숨바꼭질 할까? 내가 술래 할게!" },
        { at: 4.17, audio: "audio/k31.wav", speaker: "브론티", text: "하나, 둘, 셋, 넷, 다섯!" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s18.png",
      duration: 11.15,
      lines: [
        { at: 0.5, audio: "audio/k32.wav", speaker: "브론티", text: "찾았다! 치키 뿔이 보여!" },
        { at: 3.28, audio: "audio/k33.wav", speaker: "치키", text: "헤헤, 뿔이 세 개라서 숨기 어려워!" },
        { at: 7.01, audio: "audio/k34.wav", speaker: "나레이션", text: "넷은 해가 질 때까지 신나게 놀았어요." }
      ],
    },
    {
      kind: "video",
      src: "clips/ep01_c05.mp4",
      duration: 3.78,
      lines: [
        { at: 0.5, audio: "audio/k35_all.wav", speaker: "모두", text: "우리는 이제 친구!" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s09.png",
      duration: 8.04,
      lines: [
        { at: 0.5, audio: "audio/l12_narr.wav", speaker: "나레이션", text: "먼저 인사하면, 친구가 생겨요!" },
        { at: 3.84, audio: "audio/k39.wav", speaker: "나레이션", text: "여러분도 오늘, 친구에게 먼저 인사해 볼까요?" }
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s10.png",
      duration: 11.05,
      lines: [
        { at: 0.5, audio: "audio/k40b.wav", speaker: "치키", text: "안녕! Bye! Adiós!" }
      ],
    },
  ],
};
