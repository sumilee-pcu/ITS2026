# 📷 AI 딥러닝 기반 영상처리 기초 실습

> **공공데이터 활용 AI 딥러닝 기반 영상분석 기초 실습** 자료임.
> 2026.04.09 | 강사: 이수미 | 컨소시엄 공동훈련센터(안양) 604호

**YOLOv8 기반 객체 검출**을 직접 실습하는 자료임.
실습 중 막히는 부분은 강사에게 문의 바람.

---

## 🕐 오늘의 일정

| 시간 | 내용 | 비고 |
|------|------|------|
| 10:00 – 10:50 | 🎓 이론 강의 1부 — AI·딥러닝·영상처리 개론 | 강의 |
| 10:50 – 11:00 | ☕ 휴식 | |
| 11:00 – 11:50 | 🎓 이론 강의 2부 — YOLOv8 소개 + 실습 준비 | 강의 |
| 11:50 – 12:00 | ☕ 휴식 | |
| 12:00 – 13:00 | 🍱 점심 | |
| 13:00 – 13:50 | 💻 **실습 01** — 환경설정 + 환경점검 | 실습 |
| 13:50 – 14:00 | ☕ 휴식 | |
| 14:00 – 14:50 | 🔍 **실습 02** — 단일이미지 객체검출 | 실습 |
| 14:50 – 15:00 | ☕ 휴식 | |
| 15:00 – 15:50 | 🎬 **실습 03** — 일괄검출 + 동영상 분석 | 실습 |
| 15:50 – 16:00 | ☕ 휴식 | |
| 16:00 – 16:50 | 📊 **실습 04** — 결과 요약 + 실무 적용 | 실습 |
| 16:50 – 17:00 | ☕ 휴식 | |
| 17:00 – 17:50 | 💬 Q&A + 마무리 | |

---

## 🚀 실습 전 준비

아래 4단계를 순서대로 진행 바람.
오전 강의 시작 전까지 STEP 1~2를 완료해두면 실습이 원활함.

### STEP 1 — 저장소 클론

```bash
git clone https://github.com/sumilee-pcu/ITS2026.git
cd ITS2026
```

> 💡 git 미설치 시 → [git-scm.com](https://git-scm.com/download/win) 에서 설치 후 재시도 바람.

---

### STEP 2 — 가상환경 생성 및 패키지 설치

```bash
# 가상환경 생성 (최초 1회)
conda create -n yolo_practice python=3.10
conda activate yolo_practice

# 패키지 설치
pip install -r requirements.txt
```

> ✅ `Successfully installed ultralytics` 메시지 확인 시 설치 완료임.
>
> ⚠️ **Python 버전 안내**
> 본 실습은 `pip install ultralytics` 방식으로 Python **3.10** 기준임.
> 교재 부록의 3.9 환경은 PyTorch 직접 설치 방식으로 본 실습과 상이할 수 있음.

---

### STEP 3 — 실습용 데이터 배치

```
ITS2026/
├── data/
│   ├── images/   ← 이미지 파일(.jpg, .png) 복사
│   └── videos/   ← 동영상 파일(.mp4 권장) 복사
```

> 📂 실습 데이터는 강사가 USB 또는 공유드라이브로 배포함.
>
> ⚠️ Google Colab 환경에서는 `.wmv` 재생 불가. **`.mp4` 파일** 사용 권장.

---

### STEP 4 — Jupyter 실행

```bash
# ⚠️ 반드시 ITS2026/ 루트 폴더에서 실행할 것
jupyter notebook
```

> 🚨 `notebooks/` 폴더 내부에서 실행 시 경로 오류 발생함.
> 터미널에서 `cd ITS2026` 후 실행 필요.

---

## 📚 실습 순서 가이드

노트북 파일 4개를 순서대로 진행함.

---

### 🔵 실습 01 · 환경점검 & 데이터 확인

📄 `notebooks/01_환경점검_데이터확인.ipynb`

```
✅ Python / ultralytics 버전 확인
✅ YOLOv8 모델 자동 다운로드 확인 (yolov8n.pt, 약 6MB)
✅ data/ 폴더 내 이미지·동영상 파일 목록 출력
```

> 💡 모델 다운로드 속도가 느릴 수 있음. 최초 1회 다운로드 후 재사용됨.

---

### 🟢 실습 02 · 단일 이미지 객체검출

📄 `notebooks/02_단일이미지_객체검출.ipynb`

```
✅ 이미지 1장에 YOLOv8 적용
✅ 검출 결과 시각화 (바운딩박스 + 라벨)
✅ 신뢰도(confidence) 임계값 조정
```

> 💡 CLI 방식 동일 실행:
> ```bash
> python scripts/03_detect_image.py --source data/images/sample.jpg --conf 0.4
> ```

---

### 🟡 실습 03 · 일괄검출 & 동영상 분석

📄 `notebooks/03_일괄검출_동영상분석.ipynb`

```
✅ 폴더 내 이미지 전체 일괄 검출
✅ 동영상 프레임별 객체검출
✅ 객체 추적 (Object Tracking) — 동일 객체에 고유 ID 부여
```

> ⚠️ 동영상 파일 미존재 시 동영상 관련 셀은 자동 건너뜀.

---

### 🔴 실습 04 · 결과 요약 & 실무 적용

📄 `notebooks/04_결과요약_실무적용.ipynb`

```
✅ 검출 결과 CSV 저장
✅ 클래스별 검출 건수 집계
✅ 실무 활용 시나리오 검토 (CCTV, 품질검사 등)
```

---

### 🟣 보너스 · 통합 노트북 (복습용)

📄 `notebooks/00_통합실습노트북.ipynb`

실습 01~04 내용을 단일 파일에서 순서대로 실행 가능함. 수업 후 복습용으로 활용 바람.

---

## 📁 전체 폴더 구조

```
ITS2026/
├── README.md                        ← 본 파일
├── requirements.txt                 ← pip 설치 목록
├── run_practice.ps1                 ← Windows 런처 스크립트
├── .gitignore
├── notebooks/
│   ├── 00_통합실습노트북.ipynb      ← 복습용 (전체 흐름)
│   ├── 01_환경점검_데이터확인.ipynb ← 실습 01
│   ├── 02_단일이미지_객체검출.ipynb ← 실습 02
│   ├── 03_일괄검출_동영상분석.ipynb ← 실습 03
│   └── 04_결과요약_실무적용.ipynb   ← 실습 04
├── scripts/                         ← CLI 실행용 스크립트
│   ├── common.py
│   ├── 01_check_env.py
│   ├── 02_explore_data.py
│   ├── 03_detect_image.py
│   ├── 04_detect_batch.py
│   ├── 05_detect_video.py
│   └── 06_summarize_results.py
├── data/
│   ├── images/   ← 이미지 파일 배치
│   └── videos/   ← 동영상 파일 배치
└── outputs/      ← 검출 결과 자동 저장
```

---

## 🌐 Google Colab 사용 시

PC 사양 문제 등으로 Colab 사용 시, 아래 코드를 **첫 번째 셀**에 붙여넣고 실행 바람.

```python
# 패키지 설치 + 저장소 다운로드
!pip install ultralytics -q
!git clone https://github.com/sumilee-pcu/ITS2026.git
%cd ITS2026

# 샘플 이미지 준비 (데이터 미보유 시)
import os, urllib.request
os.makedirs('data/images', exist_ok=True)
os.makedirs('data/videos', exist_ok=True)
urllib.request.urlretrieve(
    'https://ultralytics.com/images/bus.jpg',
    'data/images/bus.jpg'
)
print("✅ 준비 완료")
```

> ⚠️ Colab에서는 `.wmv` 동영상 재생 불가. `.mp4` 파일 사용 바람.
> ⚠️ 세션 종료 시 위 설정을 재실행해야 함.

---

## 💾 결과 저장 위치

| 실습 항목 | 출력 폴더 |
|----------|----------|
| 단일 이미지 검출 | `outputs/detect_single/` |
| 이미지 일괄 검출 | `outputs/detect_batch/` |
| 동영상 검출 | `outputs/video_detect/` |
| 동영상 추적 | `outputs/video_track/` |
| 결과 요약 CSV | `outputs/result_summary.csv` |

---

## 🛠️ CLI 실행 방법

```bash
python scripts/01_check_env.py                                         # 환경 점검
python scripts/02_explore_data.py                                      # 데이터 확인
python scripts/03_detect_image.py                                      # 이미지 검출
python scripts/03_detect_image.py --source data/images/sample.jpg --conf 0.4
python scripts/04_detect_batch.py                                      # 이미지 일괄 처리
python scripts/05_detect_video.py                                      # 동영상 검출
python scripts/05_detect_video.py --mode track                        # 동영상 추적
python scripts/06_summarize_results.py                                 # 결과 요약 CSV
```

**Windows PowerShell 런처**

```powershell
powershell -ExecutionPolicy Bypass -File run_practice.ps1 -Step check
powershell -ExecutionPolicy Bypass -File run_practice.ps1 -Step image
powershell -ExecutionPolicy Bypass -File run_practice.ps1 -Step video
powershell -ExecutionPolicy Bypass -File run_practice.ps1 -Step track
powershell -ExecutionPolicy Bypass -File run_practice.ps1 -Step summary
```

---

## 🆘 트러블슈팅

| 증상 | 원인 | 조치 |
|------|------|------|
| `yolov8n.pt` 다운로드 지연 | 네트워크 속도 | 대기 후 재시도. 최초 1회 다운로드 후 재사용됨 |
| `FileNotFoundError` (경로 오류) | Jupyter 실행 위치 오류 | `ITS2026/` 루트에서 `jupyter notebook` 실행 필요 |
| WMV 동영상 Colab 재생 불가 | Linux WMV 코덱 미지원 | `.mp4` 파일 사용 또는 샘플 URL 활용 |
| 이미지 파일 없음 오류 | `data/images/` 폴더 비어 있음 | `.jpg` / `.png` 파일 배치 후 재실행 |
| 동영상 파일 없음 오류 | `data/videos/` 폴더 비어 있음 | `.mp4` 파일 배치 후 재실행 (없으면 자동 건너뜀) |
| `conda activate` 오류 | conda 초기화 미완료 | `conda init` 실행 후 터미널 재시작 |
| 패키지 설치 오류 | pip 버전 문제 | `pip install --upgrade pip` 후 재시도 |

---

> 본 실습 자료는 수업 종료 후에도 GitHub에서 재다운로드 가능함.
> 문의사항은 강사 이메일로 연락 바람.
