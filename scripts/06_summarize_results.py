from __future__ import annotations

from pathlib import Path

from common import ensure_output_dir, image_sources, print_header, save_csv


def main() -> None:
    from ultralytics import YOLO

    print_header("결과 요약 CSV 생성")

    images = image_sources()
    if not images:
        raise FileNotFoundError(
            "요약할 이미지 샘플이 없습니다.\n"
            "  → data/images/ 에 .jpg / .png 파일을 넣어주세요."
        )

    model = YOLO("yolov8n.pt")
    results = model.predict(source=[str(p) for p in images], conf=0.25, save=False)

    rows = []
    for result in results:
        names = result.names
        classes = [names[int(c)] for c in result.boxes.cls.tolist()]
        rows.append(
            {
                "image": Path(result.path).name,
                "detect_count": len(result.boxes),
                "detected_classes": ", ".join(classes) if classes else "",
                "notes": "",
            }
        )

    output_dir = ensure_output_dir()
    csv_path = output_dir / "result_summary.csv"
    save_csv(
        rows,
        csv_path,
        fieldnames=["image", "detect_count", "detected_classes", "notes"],
    )

    print("요약 파일:", csv_path)
    print("처리 건수:", len(rows))
    print("\n(notes 열에 직접 메모를 추가하여 활용하세요)")


if __name__ == "__main__":
    main()
