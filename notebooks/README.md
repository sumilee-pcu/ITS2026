# 실습 노트북 안내

## 추천 진행 순서

1. `01_환경점검_데이터확인.ipynb` — 환경과 샘플 데이터 확인
2. `02_단일이미지_객체검출.ipynb` — 단일 이미지 YOLOv8 검출 + conf 비교
3. `03_일괄검출_동영상분석.ipynb` — 폴더 일괄 처리 + 동영상 검출/추적
4. `04_결과요약_실무적용.ipynb` — 결과 정리, 발표, ITS 아이디어 도출

## 통합 실습 (시연/복습용)

- `00_통합실습노트북.ipynb` — 전체 흐름을 셀 5개로 한번에 진행

## 실행 전 공통 확인사항

```
⚠️ Jupyter는 반드시 ITS2026/ 루트에서 실행하세요.

  cd ITS2026
  jupyter notebook

  notebooks/ 폴더 안에서 직접 열면 경로 오류가 발생합니다.
```

## Google Colab 수강생

1. Colab에서 저장소 클론:
   ```python
   !git clone https://github.com/sumilee-pcu/ITS2026.git
   %cd ITS2026
   ```
2. 노트북 파일 열기: `notebooks/` 폴더에서 원하는 파일 선택
3. `.wmv` 동영상은 Colab에서 재생 불가 → `.mp4` 또는 공개 샘플 URL 사용
