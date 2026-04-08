from __future__ import annotations

from collections import Counter
from pathlib import Path

from common import build_basic_parser, ensure_output_dir, image_sources, print_header, save_csv


def main() -> None:
    parser = build_basic_parser("이미지 폴더 일괄 객체검출")
    parser.add_argument("--source-dir", type=str, default=None, help="입력 이미지 폴더 (생략 시 data/images/ 사용)")
    args = parser.parse_args()

    if args.source_dir:
        source_dir = Path(args.source_dir)
    else:
        images = image_sources()
        if not images:
            raise FileNotFoundError(
                "처리할 이미지가 없습니다.\n"
                "  → data/images/ 에 .jpg / .png 파일을 넣어주세요."
            )
        source_dir = images[0].parent

    if not source_dir.exists():
        raise FileNotFoundError(f"입력 폴더를 찾을 수 없습니다: {source_dir}")

    from ultralytics import YOLO

    print_header("이미지 폴더 일괄 객체검출")
    print("입력 폴더:", source_dir)
    print("conf:", args.conf)

    output_dir = ensure_output_dir()
    model = YOLO("yolov8n.pt")
    results = model.predict(
        source=str(source_dir),
        conf=args.conf,
        save=True,
        project=str(output_dir),
        name="detect_batch",
        exist_ok=True,
    )

    rows = []
    counter = Counter()
    for result in results:
        image_name = Path(result.path).name
        detect_count = len(result.boxes)
        rows.append({"image": image_name, "detect_count": detect_count})
        for class_id in result.boxes.cls.tolist():
            counter[result.names[int(class_id)]] += 1

    csv_path = output_dir / "batch_summary.csv"
    save_csv(rows, csv_path, fieldnames=["image", "detect_count"])

    print("\n처리 이미지 수:", len(rows))
    print("출력 폴더:", output_dir / "detect_batch")
    print("요약 CSV:", csv_path)
    print("\n클래스별 검출 수")
    for key, value in sorted(counter.items()):
        print(f"  - {key}: {value}")


if __name__ == "__main__":
    main()
