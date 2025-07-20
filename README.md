# MusicTrend (음악 트렌드 자동화 시스템)

최신 음악 트렌드 차트 데이터를 매일 자동 수집/정제하여, React 기반 Github Pages로 시각화하는 서버리스 프로젝트입니다.

## 폴더 구조

- `backend/` : 크롤러, DB, 데이터 처리 (Python)
- `frontend/` : React 기반 Github Pages UI
- `data/` : 날짜별 크롤링 데이터(JSON)
- `.github/workflows/` : Github Actions 워크플로우

## 빠른 시작

### 1. 백엔드 (로컬 테스트)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### 2. 프론트엔드 (로컬 테스트)
```bash
cd frontend
npm install
npm run dev
```

### 3. Github Actions 자동화
- `.github/workflows/crawler.yml`에 워크플로우 작성 (예: 매일 7시 크롤러 실행)

## 주요 기능
- Spotify, YouTube, SoundCloud, TikTok, Beatport 등 차트 데이터 자동 수집
- 국가/연령대/날짜별 데이터 정규화 및 DB 저장
- React UI로 차트, 유튜브 임베드, 변화 추이 등 시각화

---

자세한 내용은 각 폴더의 README 참고