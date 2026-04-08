from __future__ import annotations

from common import ensure_output_dir, print_header, resolve_source


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="동영상 객체검출 또는 추적")
    parser.add_argument("--source", type=str, default=None,
                        help="입력 동영상 경로 (생략 시 data/videos/ 첫 번째 파일 사용)")
    parser.add_argument("--conf", type=float, default=0.3, help="confidence threshold (기본 0.3)")
    parser.add_argument(
        "--mode",
        choices=["predict", "track"],
        default="predict",
        help="predict(검출) 또는 track(추적, ID 부여)",
    )
    args = parser.parse_args()

    source = resolve_source(args.source, kind="video")
    if not source.exists():
        raise FileNotFoundError(f"입력 동영상을 찾을 수 없습니다: {source}")

    # WMV 포맷 경고
    if source.suffix.lower() == ".wmv":
        print("⚠️  WMV 파일은 Google Colab(Linux) 환경에서 재생되지 않습니다.")
        print("   로컬(Windows) 환경에서는 정상 동작합니다.")

    from ultralytics import YOLO

    print_header("동영상 객체검출")
    print("입력 파일:", source)
    print("mode:", args.mode, ("(프레임별 독립 검출)" if args.mode == "predict" else "(객체 ID 추적)"))
    print("conf:", args.conf)

    output_dir = ensure_output_dir()
    model = YOLO("yolov8n.pt")

    if args.mode == "track":
        model.track(
            source=str(source),
            conf=args.conf,
            save=True,
            project=str(output_dir),
            name="video_track",
            exist_ok=True,
        )
        print("\n출력 폴더:", output_dir / "video_track")
    else:
        model.predict(
            source=str(source),
            conf=args.conf,
            save=True,
            project=str(output_dir),
            name="video_detect",
            exist_ok=True,
        )
        print("\n출력 폴더:", output_dir / "video_detect")


if __name__ == "__main__":
    main()
