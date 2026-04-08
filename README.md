# 📷 AI 딥러닝 기반 영상처리 기초 실습

> **공공데이터 활용 AI 딥러닝 기반 영상분석 기초 실습** 자료입니다.
> 2026.04.09 | 강사: 이수미 | 컨소시엄 공동훈련센터(안양) 604호

안녕하세요! 오늘 하루 함께 **YOLOv8로 객체 검출**을 직접 해볼 거예요 🎉
막히는 부분이 있으면 언제든지 손 들어 주세요. 같이 해결합시다!

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

## 🚀 실습 전 준비 (오전 10:30 전까지 완료!)

아래 3단계를 순서대로 따라해 주세요.
**처음 설정이 제일 중요합니다.** 이 단계만 잘 되면 나머지는 수월해요!
오전 강의 듣는 동안 미리 준비해두면 딱 좋아요 😊

### STEP 1 — 저장소 받기

```bash
git clone https://github.com/sumilee-pcu/ITS2026.git
cd ITS2026
```

> 💡 git이 없다면? → [git-scm.com](https://git-scm.com/download/win) 에서 설치 후 재시도

---

### STEP 2 — 가상환경 만들고 패키지 설치

```bash
# 가상환경 생성 (처음 한 번만)
conda create -n yolo_practice python=3.10
conda activate yolo_practice

# 패키지 설치
pip install -r requirements.txt
```

> ✅ `Successfully installed ultralytics` 메시지가 나오면 성공!
>
> ⚠️ **Python 버전 안내**
> 이번 실습은 `pip install ultralytics` 방식으로 Python **3.10** 을 씁니다.
> (교재 부록의 3.9 환경은 PyTorch 직접 설치 방식이라 다를 수 있어요.)

---

### STEP 3 — 실습용 데이터 넣기

```
ITS2026/
├── data/
│   ├── images/   ← 이미지 파일(.jpg, .png)을 여기에 복사
│   └── videos/   ← 동영상 파일(.mp4 권장)을 여기에 복사
```

> 📂 데이터는 강사가 USB 또는 공유드라이브로 나눠드립니다.
>
> ⚠️ Google Colab 환경에서는 `.wmv` 재생이 안 됩니다. **`.mp4` 파일**을 사용해 주세요.

---

### STEP 4 — Jupyter 실행

```bash
# ⚠️ 반드시 ITS2026/ 루트 폴더에서 실행하세요!
jupyter notebook
```

> 🚨 `notebooks/` 폴더 **안에서** 실행하면 경로 오류가 납니다.
> 터미널에서 `cd ITS2026` 후 실행하는 것이 포인트!

---

## 📚 실습 순서 가이드

오늘 실습은 **노트북 파일 4개**를 순서대로 진행합니다.

---

### 🔵 실습 01 · 환경점검 & 데이터 확인 `(오전)`

📄 파일: `notebooks/01_환경점검_데이터확인.ipynb`

```
이 노트북에서 할 일:
✅ Python / ultralytics 버전 확인
✅ YOLOv8 모델 자동 다운로드 확인 (yolov8n.pt, 약 6MB)
✅ data/ 폴더 내 이미지·동영상 파일 목록 출력
```

> 💡 모델 다운로드가 느리면 잠시 기다려 주세요. 한 번 받으면 재사용됩니다.

---

### 🟢 실습 02 · 단일 이미지 객체검출 `(오후 1교시)`

📄 파일: `notebooks/02_단일이미지_객체검출.ipynb`

```
이 노트북에서 할 일:
✅ 이미지 1장에 YOLOv8 적용
✅ 검출 결과 이미지 시각화 (바운딩박스 + 라벨)
✅ 신뢰도(confidence) 값 조정해보기
```

> 💡 CLI 방식으로도 할 수 있어요:
> ```bash
> python scripts/03_detect_image.py --source data/images/sample.jpg --conf 0.4
> ```

---

### 🟡 실습 03 · 일괄검출 & 동영상 분석 `(오후 2교시)`

📄 파일: `notebooks/03_일괄검출_동영상분석.ipynb`

```
이 노트북에서 할 일:
✅ 폴더 내 이미지 전체 일괄 검출
✅ 동영상 프레임별 객체검출
✅ 객체 추적 (Object Tracking) — 같은 사람에게 고유 ID 부여
```

> ⚠️ 동영상 파일이 없으면 동영상 관련 셀은 자동으로 건너뜁니다. 당황하지 마세요!

---

### 🔴 실습 04 · 결과 요약 & 실무 적용 `(오후 3교시)`

📄 파일: `notebooks/04_결과요약_실무적용.ipynb`

```
이 노트북에서 할 일:
✅ 검출 결과 CSV 파일로 저장
✅ 클래스별 검출 건수 집계
✅ 실무 활용 시나리오 (CCTV, 품질검사 등) 토의
```

---

### 🟣 보너스 · 통합 노트북 (복습용)

📄 파일: `notebooks/00_통합실습노트북.ipynb`

실습 01~04 내용을 **한 파일에서** 순서대로 실행해볼 수 있어요.
수업 후 혼자 복습할 때 유용합니다!

---

## 📁 전체 폴더 구조

```
ITS2026/
├── README.md                        ← 지금 읽고 있는 파일
├── requirements.txt                 ← pip 설치 목록
├── run_practice.ps1                 ← Windows 런처 스크립트
├── .gitignore
├── notebooks/
│   ├── 00_통합실습노트북.ipynb      ← 복습용 (전체 흐름)
│   ├── 01_환경점검_데이터확인.ipynb ← 실습 01
│   ├── 02_단일이미지_객체검출.ipynb ← 실습 02
│   ├── 03_일괄검출_동영상분석.ipynb ← 실습 03
│   └── 04_결과요약_실무적용.ipynb   ← 실습 04
├── scripts/                         ← CLI 실행용 파이썬 스크립트
│   ├── common.py
│   ├── 01_check_env.py
│   ├── 02_explore_data.py
│   ├── 03_detect_image.py
│   ├── 04_detect_batch.py
│   ├── 05_detect_video.py
│   └── 06_summarize_results.py
├── data/
│   ├── images/   ← ✋ 이미지 파일 여기에
│   └── videos/   ← ✋ 동영상 파일 여기에
└── outputs/      ← 검출 결과 자동 저장됨
```

---

## 🌐 Google Colab으로 하는 분들께

노트북이나 PC 사양이 걱정되시면 Google Colab을 이용하세요!
아래 코드를 **Colab 첫 번째 셀**에 붙여넣고 실행하면 됩니다.

```python
# 패키지 설치 + 저장소 다운로드
!pip install ultralytics -q
!git clone https://github.com/sumilee-pcu/ITS2026.git
%cd ITS2026

# 샘플 이미지 준비 (파일이 없을 때)
import os, urllib.request
os.makedirs('data/images', exist_ok=True)
os.makedirs('data/videos', exist_ok=True)
urllib.request.urlretrieve(
    'https://ultralytics.com/images/bus.jpg',
    'data/images/bus.jpg'
)
print("✅ 준비 완료! 이제 노트북을 실행하세요.")
```

> ⚠️ Colab에서는 `.wmv` 동영상 재생이 안 됩니다. `.mp4` 파일을 사용하세요.
> ⚠️ 세션이 끊기면 위 설정을 다시 실행해야 합니다.

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

## 🛠️ CLI 실행 방법 (스크립트 방식)

노트북 대신 터미널에서 바로 실행할 수도 있어요.

```bash
python scripts/01_check_env.py            # 환경 점검
python scripts/02_explore_data.py         # 데이터 확인
python scripts/03_detect_image.py         # 이미지 검출
python scripts/03_detect_image.py --source data/images/sample.jpg --conf 0.4
python scripts/04_detect_batch.py         # 이미지 일괄 처리
python scripts/05_detect_video.py         # 동영상 검출
python scripts/05_detect_video.py --mode track   # 동영상 추적
python scripts/06_summarize_results.py    # 결과 요약 CSV
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

## 🆘 자주 묻는 문제 (FAQ)

| 이런 문제가 생겼어요 | 원인 | 이렇게 해보세요 |
|---------------------|------|----------------|
| `yolov8n.pt` 다운로드가 너무 느려요 | 네트워크 속도 | 잠시 기다려 주세요. 한 번 받으면 재사용됩니다 |
| `FileNotFoundError` (경로 오류) | Jupyter 실행 위치 문제 | `ITS2026/` 루트에서 `jupyter notebook` 실행 |
| WMV 동영상이 Colab에서 안 열려요 | Linux에서 WMV 코덱 미지원 | `.mp4` 파일로 변환하거나 위 샘플 URL 사용 |
| `이미지 파일이 없다`는 오류 | `data/images/` 폴더가 비어 있음 | `.jpg` / `.png` 파일을 폴더에 넣고 재실행 |
| `동영상 파일이 없다`는 오류 | `data/videos/` 폴더가 비어 있음 | `.mp4` 파일을 폴더에 넣고 재실행 (없으면 건너뜀) |
| `conda activate` 가 안 돼요 | conda 초기화 필요 | `conda init` 실행 후 터미널 재시작 |
| 패키지 설치 중 에러가 나요 | pip 버전 또는 네트워크 | `pip install --upgrade pip` 후 재시도 |

---

> 오늘 실습 자료는 수업 후에도 GitHub에서 언제든 다시 받을 수 있습니다.
> 질문이나 피드백은 강사 이메일로 보내주세요 😊
