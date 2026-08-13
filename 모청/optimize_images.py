"""
images-original/ 안의 원본 사진을 웹용으로 리사이즈·압축해서 images/ 에 저장한다.
사진을 새로 추가/교체할 때: images-original/ 에 원본을 넣고 이 스크립트를 다시 실행하면 된다.

사용법:
    python optimize_images.py

필요 패키지: pip install pillow
"""
import os
from PIL import Image, ImageOps

SRC_DIR = "images-original"
DST_DIR = "images"

MAX_EDGE_HERO = 2200      # main.jpg (커버 사진) 긴 변 최대 길이
MAX_EDGE_GALLERY = 1800   # 나머지 갤러리 사진 긴 변 최대 길이
QUALITY = 82

VALID_EXT = (".jpg", ".jpeg", ".png")


def optimize(fname):
    src_path = os.path.join(SRC_DIR, fname)
    dst_path = os.path.join(DST_DIR, os.path.splitext(fname)[0] + ".jpg")

    im = Image.open(src_path)
    im = ImageOps.exif_transpose(im)  # EXIF 방향값대로 회전시키고, 이후 EXIF는 저장하지 않음(메타데이터/위치정보 제거)
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")

    max_edge = MAX_EDGE_HERO if fname.lower() == "main.jpg" else MAX_EDGE_GALLERY
    w, h = im.size
    scale = min(1.0, max_edge / max(w, h))
    if scale < 1.0:
        im = im.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)

    im.save(dst_path, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    return os.path.getsize(src_path), os.path.getsize(dst_path)


def main():
    if not os.path.isdir(SRC_DIR):
        raise SystemExit(f"'{SRC_DIR}' 폴더가 없습니다. 원본 사진을 그 안에 넣어주세요.")
    os.makedirs(DST_DIR, exist_ok=True)

    files = [f for f in sorted(os.listdir(SRC_DIR)) if f.lower().endswith(VALID_EXT)]
    if not files:
        raise SystemExit(f"'{SRC_DIR}' 안에 이미지가 없습니다.")

    total_before = total_after = 0
    ok_count = 0
    failed = []
    for fname in files:
        try:
            before, after = optimize(fname)
        except Exception as e:
            print(f"  {fname}: 건너뜀 (읽기 실패: {e})")
            failed.append(fname)
            continue
        total_before += before
        total_after += after
        ok_count += 1
        print(f"  {fname}: {before/1024:.0f}KB -> {after/1024:.0f}KB")

    print(f"\n{ok_count}/{len(files)}장 처리 완료")
    print(f"전체: {total_before/1024/1024:.1f}MB -> {total_after/1024/1024:.1f}MB")
    if failed:
        print(f"\n실패한 파일 ({len(failed)}개) - 원본이 손상됐을 수 있습니다. images-original/ 안의 해당 파일을 확인해주세요:")
        for f in failed:
            print(f"  - {f}")


if __name__ == "__main__":
    main()
