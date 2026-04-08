from __future__ import annotations

import platform
import sys

from common import (
    DATA_DIR,
    IMAGE_DIR,
    VIDEO_DIR,
    OUTPUT_DIR,
    ROOT_DIR,
    default_image,
    default_video,
    has_module,
    print_header,
)


def main() -> None:
    print_header("실습 환경 점검")

    print("Python 버전:", sys.version.replace("\n", " "))
    print("플랫폼:", platform.platform())
    print("워크스페이스 루트:", ROOT_DIR)
    print("데이터 폴더:", DATA_DIR)
    print("이미지 폴더:", IMAGE_DIR)
    print("동영상 폴더:", VIDEO_DIR)
    print("출력 폴더:", OUTPUT_DIR)

    print("\n패키지 점검")
    for module_name in ["ultralytics", "cv2", "matplotlib", "pandas", "PIL"]:
        status = "OK" if has_module(module_name) else "MISSING ← pip install 필요"
        print(f"  - {module_name}: {status}")

    print("\n샘플 파일 점검")
    try:
        print("  - 기본 이미지:", default_image())
    except FileNotFoundError as exc:
        print("  - 기본 이미지:", exc)

    try:
        print("  - 기본 동영상:", default_video())
    except FileNotFoundError as exc:
        print("  - 기본 동영상:", exc)


if __name__ == "__main__":
    main()
