from __future__ import annotations

from common import image_sources, print_header, video_sources


def main() -> None:
    print_header("실습 데이터 확인")

    images = image_sources()
    videos = video_sources()

    print("[이미지 샘플]")
    if images:
        for path in images:
            print("  -", path)
    else:
        print("  - 이미지 파일이 없습니다. data/images/ 에 파일을 넣어주세요.")

    print("\n[동영상 샘플]")
    if videos:
        for path in videos:
            print("  -", path)
    else:
        print("  - 동영상 파일이 없습니다. data/videos/ 에 .mp4 파일을 넣어주세요.")
        print("  ※ Google Colab 환경에서는 .wmv 재생이 안 됩니다. .mp4를 권장합니다.")


if __name__ == "__main__":
    main()
