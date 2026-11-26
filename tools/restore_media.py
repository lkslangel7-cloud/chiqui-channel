"""새 대화(새 컨테이너)에서 합격 그림·영상을 Higgsfield 공유 링크로 다시 받는다.
사용: python3 -I tools/restore_media.py [ep13 ep14 ...]   (없으면 전부)
파일 이름 끝의 코드(S##_CODE.png)가 https://higgsfield.ai/s/CODE 이다."""
import re, subprocess, sys, html, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
want = sys.argv[1:]
for line in open(os.path.join(ROOT, "tools/media_manifest.txt"), encoding="utf-8"):
    rel = line.strip()
    if not rel or (want and rel.split("/")[1] not in want): continue
    dst = os.path.join(ROOT, rel)
    if os.path.exists(dst): continue
    stem, ext = os.path.splitext(os.path.basename(rel)); ext = ext[1:]
    if re.search(r"(_fix|_bright|_local_zoom|_bad|_backup|old_teal)$|^(both|sheet_\d)$", stem):
        print("건너뜀(git에 있거나 안 쓰는 파일)", rel); continue
    code = stem[-11:]
    page = subprocess.run(["curl", "-sSL", "-m", "40", f"https://higgsfield.ai/s/{code}"], capture_output=True, text=True).stdout
    if ext == "mp4":
        v = re.findall(r'https://d8j0ntlcm91z4\.cloudfront\.net/[^"\\]+\.mp4', page); url = v[0] if v else None
    else:
        og = re.search(r'og:image" content="([^"]+)"', page); url = html.unescape(og.group(1)) if og else None
    if not url: print("못 받음", rel); continue
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    r = subprocess.run(["curl", "-sSf", "-m", "180", "-o", dst, url])
    print("받음" if r.returncode == 0 else "실패", rel)
