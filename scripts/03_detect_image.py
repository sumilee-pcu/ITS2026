from __future__ import annotations

from pathlib import Path

from common import build_basic_parser, ensure_output_dir, print_header, resolve_source


def main() -> None:
    parser = build_basic_parser("단일 이미지 객체검출")
    parser.add_argument("--source", type=str, default=None, help="입력 이미지 경로 (생략 시 data/images/ 첫 번째 파일 사용)")
    args = parser.parse_args()

    source = resolve_source(args.source, kind="image")
    if not source.exists():
        raise FileNotFoundError(f"입력 이미지를 찾을 수 없습니다: {source}")

    from ultralytics import YOLO

    print_header("단일 이미지 객체검출")
    print("입력 파일:", source)
    print("conf:", args.conf)
    print("※ 첫 실행 시 yolov8n.pt (~6MB) 가 자동 다운로드됩니다. (인터넷 연결 필요)")

    output_dir = ensure_output_dir()
    model = YOLO("yolov8n.pt")
    results = model.predict(
        source=str(source),
        conf=args.conf,
        save=True,
        project=str(output_dir),
        name="detect_single",
        exist_ok=True,
    )

    result = results[0]
    print("\n검출 개수:", len(result.boxes))
    print("출력 폴더:", output_dir / "detect_single")

    if len(result.boxes) > 0:
        print("\n상위 검출 결과")
        names = result.names
        for idx, box in enumerate(result.boxes[:10]):
            class_id = int(box.cls.item())
            score = float(box.conf.item())
            print(f"  {idx + 1}. {names[class_id]} ({score:.3f})")


if __name__ == "__main__":
    main()
