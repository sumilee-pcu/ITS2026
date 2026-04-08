# 데이터 폴더 안내

이 폴더에 실습용 이미지와 동영상을 넣어주세요.

```
data/
├── images/   ← .jpg, .jpeg, .png, .bmp
└── videos/   ← .mp4 권장 (.wmv는 Google Colab에서 재생 불가)
```

## 샘플 데이터 구하기

### AIHub (공공데이터)
- https://aihub.or.kr/ → 교통 관련 데이터셋 검색

### 빠른 테스트용 공개 이미지
```python
import urllib.request
urllib.request.urlretrieve('https://ultralytics.com/images/bus.jpg', 'data/images/bus.jpg')
urllib.request.urlretrieve('https://ultralytics.com/images/zidane.jpg', 'data/images/zidane.jpg')
```

### Google Colab 수강생용 샘플 동영상
```bash
# .wmv는 Colab에서 재생 불가 — .mov/.mp4 사용
wget -q https://ultralytics.com/assets/decelera_landscape_min.mov -O data/videos/sample.mov
```

## 주의사항

- `data/images/` 와 `data/videos/` 폴더는 `.gitignore` 에 포함되어 있어 커밋되지 않습니다.
- 개인 데이터나 저작권이 있는 파일은 이 폴더에만 넣고 외부에 공유하지 마세요.
