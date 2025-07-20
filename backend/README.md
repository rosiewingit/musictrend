# Backend (크롤러/DB)

이 디렉토리는 음악 트렌드 차트 데이터 크롤링, 정제, DB 저장을 담당합니다.

## 주요 역할
- Spotify, YouTube, SoundCloud, TikTok, Beatport 등 다양한 플랫폼의 차트 데이터 수집
- 국가/연령대별, 날짜별 데이터 정규화 및 저장
- SQLite 기반 DB 관리 및 JSON 백업
- Github Actions에서 자동 실행

## 개발 환경
- Python 3.9 이상
- 주요 패키지: requests, beautifulsoup4, sqlite-utils
- 가상환경: `python3 -m venv venv && source venv/bin/activate`

## 구조 예시
- `crawler/` : 각 플랫폼별 크롤러 모듈
- `db/` : DB 초기화 및 관리 스크립트
- `main.py` : 전체 실행 진입점
- `utils/` : 공통 유틸리티

---

> 개발/테스트 시 `venv` 활성화 후 진행하세요.
