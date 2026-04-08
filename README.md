# AI 딥러닝 기반 영상처리 기초 실습

**공공데이터 활용 AI 딥러닝 기반 영상분석 기초 실습** 자료입니다.

> 2026.04.09 | 강사: 이수미 | 컨소시엄 공동훈련센터(안양) 604호

---

## 빠른 시작

### 1. 저장소 클론

```bash
git clone https://github.com/sumilee-pcu/ITS2026.git
cd ITS2026
```

### 2. 환경 설정 (Python 3.10 이상 권장)

```bash
conda create -n yolo_practice python=3.10
conda activate yolo_practice
pip install -r requirements.txt
```

> ℹ️ **Python 버전 안내**
> 이번 실습은 `ultralytics(YOLOv8)` 기반으로 Python 3.10에서 동작합니다.
> (교재 부록의 3.9는 PyTorch 직접 설치 기준이므로 이번 실습과 다릅니다.)

### 3. 샘플 데이터 준비

```
data/
├── images/   ← 실습용 이미지 파일(.jpg, .png)을 여기에 넣으세요
└── videos/   ← 실습용 동영상 파일(.mp4 권장)을 여기에 넣으세요
```

> ⚠️ Google Colab 환경에서는 `.wmv` 파일 재생이 불가합니다. `.mp4`를 권장합니다.

### 4. Jupyter 실행

```bash
# ⚠️ 반드시 ITS2026/ 루트 폴더에서 실행하세요
# (notebooks/ 폴더 안에서 직접 열면 경로 오류가 발생합니다)
jupyter notebook
```

---

## 폴더 구조

```
ITS2026/
├── README.md
├── requirements.txt
├── run_practice.ps1          # Windows PowerShell 런처
├── 실습진행순서.md
├── notebooks/
│   ├── 00_통합실습노트북.ipynb      # 전체 흐름 한번에 (시연/복습용)
│   ├── 01_환경점검_데이터확인.ipynb
│   ├── 02_단일이미지_객체검출.ipynb
│   ├── 03_일괄검출_동영상분석.ipynb
│   └── 04_결과요약_실무적용.ipynb
├── scripts/
│   ├── common.py
│   ├── 01_check_env.py
│   ├── 02_explore_data.py
│   ├── 03_detect_image.py
│   ├── 04_detect_batch.py
│   ├── 05_detect_video.py
│   └── 06_summarize_results.py
├── data/
│   ├── images/               # ← 이미지 파일 여기에
│   └── videos/               # ← 동영상 파일 여기에
└── outputs/                  # 검출 결과 자동 저장
```

---

## 실습 실행 (CLI 방식)

```bash
# 1. 환경 점검
python scripts/01_check_env.py

# 2. 데이터 확인
python scripts/02_explore_data.py

# 3. 단일 이미지 객체검출
python scripts/03_detect_image.py
python scripts/03_detect_image.py --source data/images/sample.jpg --conf 0.4

# 4. 이미지 일괄 처리
python scripts/04_detect_batch.py
python scripts/04_detect_batch.py --conf 0.35

# 5. 동영상 객체검출
python scripts/05_detect_video.py

# 6. 동영상 추적 (객체 ID 부여)
python scripts/05_detect_video.py --mode track

# 7. 결과 요약 CSV 생성
python scripts/06_summarize_results.py
```

### PowerShell 런처 (Windows)

```powershell
powershell -ExecutionPolicy Bypass -File run_practice.ps1 -Step check
powershell -ExecutionPolicy Bypass -File run_practice.ps1 -Step image
powershell -ExecutionPolicy Bypass -File run_practice.ps1 -Step batch -Conf 0.35
powershell -ExecutionPolicy Bypass -File run_practice.ps1 -Step video
powershell -ExecutionPolicy Bypass -File run_practice.ps1 -Step track
powershell -ExecutionPolicy Bypass -File run_practice.ps1 -Step summary
```

---

## Google Colab 수강생 안내

```python
# Colab 첫 셀에서 실행
!pip install ultralytics -q
!git clone https://github.com/sumilee-pcu/ITS2026.git
%cd ITS2026

# 샘플 이미지/동영상 다운로드
import urllib.request, os
os.makedirs('data/images', exist_ok=True)
os.makedirs('data/videos', exist_ok=True)
urllib.request.urlretrieve('https://ultralytics.com/images/bus.jpg', 'data/images/bus.jpg')
# 동영상 샘플 (.mp4 또는 .mov — .wmv는 Colab에서 재생 불가)
# !wget -q https://ultralytics.com/assets/decelera_landscape_min.mov -O data/videos/sample.mov
```

---

## 결과 저장 위치

| 실습 항목 | 출력 폴더 |
|----------|----------|
| 단일 이미지 검출 | `outputs/detect_single/` |
| 이미지 일괄 검출 | `outputs/detect_batch/` |
| 동영상 검출 | `outputs/video_detect/` |
| 동영상 추적 | `outputs/video_track/` |
| 결과 요약 CSV | `outputs/result_summary.csv` |

---

## 자주 묻는 문제

| 증상 | 원인 | 해결 |
|------|------|------|
| `yolov8n.pt` 다운로드가 느림 | 네트워크 상태 | 잠시 기다린 후 재시도 (슬라이드 266p 참고) |
| `FileNotFoundError` (경로 오류) | Jupyter 실행 위치 | `ITS2026/` 루트에서 `jupyter notebook` 실행 |
| WMV 재생 안 됨 (Colab) | Linux WMV 코덱 미지원 | `.mp4` 파일 사용 또는 위 샘플 URL 이용 |
| 이미지가 없다는 오류 | `data/images/` 폴더 비어있음 | 이미지 파일(.jpg/.png) 추가 후 재실행 |
| 동영상이 없다는 오류 | `data/videos/` 폴더 비어있음 | 동영상 파일(.mp4) 추가 후 재실행 |
