export type Line = {
  at: number; // 장면 시작 기준 초
  audio: string; // public/ 기준 경로
  speaker: string;
  text: string;
};

export type Scene = {
  kind: "image" | "video";
  src: string;
  duration: number; // 초
  lines: Line[];
};

export type Episode = {
  title: string;
  bgm?: string;
  scenes: Scene[];
};

export const FPS = 30;

export const episodeFrames = (ep: Episode) =>
  ep.scenes.reduce((sum, s) => sum + Math.round(s.duration * FPS), 0);
