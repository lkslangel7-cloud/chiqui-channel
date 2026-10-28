import type { Episode } from "../types";

// 1화 30초 버전 (한국어, 음성: ElevenLabs v4). 시간 단위는 초.
// 영어·스페인어 버전은 같은 장면 구성에 lines의 audio/text만 바꿔 만든다.
export const ep01Ko: Episode = {
  title: "치키의 세 가지 인사",
  bgm: "audio/bgm.wav",
  scenes: [
    {
      kind: "image",
      src: "scenes/ep01_s02.png",
      duration: 3.75,
      lines: [{ at: 0.05, audio: "audio/l01_narr.wav", speaker: "나레이션", text: "레인보우 밸리에 아기 공룡 치키가 이사 왔어요." }],
    },
    {
      kind: "image",
      src: "scenes/ep01_s04.png",
      duration: 3.55,
      lines: [{ at: 0.08, audio: "audio/l02_narr.wav", speaker: "나레이션", text: "친구를 사귀고 싶지만, 너무 부끄러웠어요." }],
    },
    {
      kind: "video",
      src: "clips/ep01_c02.mp4",
      duration: 5.8,
      lines: [
        { at: 0.1, audio: "audio/l03_narr.wav", speaker: "나레이션", text: "그때, 뿔 세 개가 반짝 빛났어요!" },
        { at: 3.35, audio: "audio/l04_chiqui.wav", speaker: "치키", text: "안녕! Hello! Hola!" },
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s06.png",
      duration: 4.6,
      lines: [
        { at: 0.1, audio: "audio/l05_chiqui.wav", speaker: "치키", text: "안녕! 나는 치키야!" },
        { at: 2.2, audio: "audio/l06_bronti.wav", speaker: "브론티", text: "안녕, 치키! 반가워." },
      ],
    },
    {
      kind: "video",
      src: "clips/ep01_c03.mp4",
      duration: 3.8,
      lines: [
        { at: 0.1, audio: "audio/l07_chiqui.wav", speaker: "치키", text: "Hello!" },
        { at: 0.9, audio: "audio/l08_pico.wav", speaker: "피코", text: "Hello! 나는 피코야!" },
      ],
    },
    {
      kind: "video",
      src: "clips/ep01_c04.mp4",
      duration: 4.1,
      lines: [
        { at: 0.1, audio: "audio/l09_chiqui.wav", speaker: "치키", text: "Hola!" },
        { at: 0.95, audio: "audio/l10_tino.wav", speaker: "티노", text: "나도… 같이 해도 돼?" },
      ],
    },
    {
      kind: "image",
      src: "scenes/ep01_s09.png",
      duration: 4.4,
      lines: [{ at: 0.3, audio: "audio/l12_narr.wav", speaker: "나레이션", text: "먼저 인사하면, 친구가 생겨요!" }],
    },
  ],
};
