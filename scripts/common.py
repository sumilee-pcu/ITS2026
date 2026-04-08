from __future__ import annotations

import argparse
import csv
import importlib.util
from pathlib import Path
from typing import Iterable

# ── 경로 설정 ─────────────────────────────────────────────────
# 이 파일 위치: <repo_root>/scripts/common.py
# ROOT_DIR     : <repo_root>/
ROOT_DIR    = Path(__file__).resolve().parent.parent
DATA_DIR    = ROOT_DIR / "data"
IMAGE_DIR   = DATA_DIR / "images"
VIDEO_DIR   = DATA_DIR / "videos"
OUTPUT_DIR  = ROOT_DIR / "outputs"

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp"}
VIDEO_EXTS = {".mp4", ".avi", ".mov", ".wmv", ".mkv"}


def ensure_output_dir() -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR


def find_files(directory: Path, exts: set[str]) -> list[Path]:
    if not directory.exists():
        return []
    return sorted([p for p in directory.iterdir() if p.is_file() and p.suffix.lower() in exts])


def image_sources() -> list[Path]:
    """data/images/ 우선 사용. 없으면 data/ 전체에서 탐색."""
    imgs = find_files(IMAGE_DIR, IMAGE_EXTS)
    if imgs:
        return imgs
    return find_files(DATA_DIR, IMAGE_EXTS)


def video_sources() -> list[Path]:
    """data/videos/ 우선 사용. 없으면 data/ 전체에서 탐색."""
    vids = find_files(VIDEO_DIR, VIDEO_EXTS)
    if vids:
        return vids
    return find_files(DATA_DIR, VIDEO_EXTS)


def default_image() -> Path:
    images = image_sources()
    if not images:
        raise FileNotFoundError(
            "이미지 파일이 없습니다.\n"
            f"  → {IMAGE_DIR} 에 .jpg / .png 파일을 넣어주세요."
        )
    return images[0]


def default_video() -> Path:
    videos = video_sources()
    if not videos:
        raise FileNotFoundError(
            "동영상 파일이 없습니다.\n"
            f"  → {VIDEO_DIR} 에 .mp4 파일을 넣어주세요.\n"
            "  ※ Google Colab 환경에서는 .wmv 재생이 안 됩니다. .mp4를 권장합니다."
        )
    return videos[0]


def print_header(title: str) -> None:
    print("=" * 72)
    print(title)
    print("=" * 72)


def resolve_source(path_str: str | None, kind: str) -> Path:
    if path_str:
        source = Path(path_str).expanduser()
        if not source.is_absolute():
            source = ROOT_DIR / source
        return source
    if kind == "image":
        return default_image()
    if kind == "video":
        return default_video()
    raise ValueError(f"지원하지 않는 source kind: {kind}")


def has_module(module_name: str) -> bool:
    return importlib.util.find_spec(module_name) is not None


def save_csv(rows: Iterable[dict], output_path: Path, fieldnames: list[str]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_basic_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--conf", type=float, default=0.25, help="confidence threshold (기본 0.25)")
    return parser
