## ✅ 1. Project Overview (프로젝트 개요)

**목적:**
- DJ, 음악 프로듀서, 콘텐츠 크리에이터를 위한 최신 트렌드 음악 차트 데이터를 매일 자동 수집 및 정제하여, 누구나 쉽게 확인할 수 있는 웹 서비스를 제공한다.
- Github Action을 활용해 매일 지정된 시간에 데이터를 수집/정제하고, DB에 저장하여 과거 데이터까지 관리한다.
- React 기반 Github Pages로 시각화하여, 곡 순위, 유튜브 영상 임베드, 나라별/연령대별 차트 등 다양한 정보를 제공한다.

**배경:**
- 반복적이고 수작업이 많은 트렌드 곡 수집/분석 업무를 자동화하여, 효율적이고 신뢰성 있는 데이터 기반 DJ Set 기획을 지원한다.

---

## ✅ 2. Core Functionality (핵심 기능)

1. **크롤링 대상 플랫폼 및 데이터**
   * Spotify (Top 50, Viral 50, 신곡)
   * YouTube Music Charts
   * SoundCloud Charts (Trending, New & Hot)
   * TikTok Viral Sound (API 연동 or 비공식 크롤링)
   * Beatport (Top 100, Genre별)
   * 각 플랫폼별로 국가/연령대별 차트 데이터 수집 (가능한 경우)

2. **정기 실행 및 데이터 저장**
   * Github Actions로 매일 지정된 시간(예: 오전 7시)에 자동 실행
   * 크롤링/수집된 데이터를 정규화하여 DB(예: SQLite, PostgreSQL 등)에 저장
   * 날짜별로 데이터가 누적되어, 전날/그전날 등 과거 데이터도 조회 가능
   * 실패 시 알림(이메일, Slack/Discord 등) 연동 (선택)

3. **크롤링/정제 로직**
   * 각 플랫폼 API 또는 HTML 파싱
   * Top 20~50개 항목에 대해 곡명, 아티스트명, 링크, 장르, 플랫폼, 순위, 국가, 연령대, 유튜브 영상 링크 등 정규화
   * 중복 곡 처리, 장르 태깅, 국가/연령대별 필터링

4. **DB 및 파일 저장 구조**
   * DB 테이블 예시:
     - tracks (id, title, artist, platform, rank, genre, country, age_group, date, youtube_url, ...)
   * 백업용 JSON도 날짜별로 저장 가능
   * 예시:
     ```bash
     /data/YYYY-MM-DD/
         spotify.json
         youtube.json
         soundcloud.json
         tiktok.json
         beatport.json
     ```

5. **Github Pages (React) 시각화**
   * React 기반 SPA로 Github Pages에 배포
   * 주요 기능:
     - 날짜별 차트 데이터 확인 (캘린더/날짜 선택)
     - 플랫폼별/국가별/연령대별 탭 및 필터
     - 곡 순위, 아티스트, 장르, 플랫폼, 국가, 연령대 등 정보 표시
     - 곡별 유튜브 영상 임베드(가능한 경우)
     - 곡 링크(Spotify/YouTube/SoundCloud 등) 제공
     - 최근 7일/30일 인기 변화 추이 그래프
   * 반응형 UI, 직관적이고 그럴듯한 디자인 적용

6. **선택/확장 기능**
   * 트렌드 곡 키워드 기반 추천
   * 유사 BPM, Key 기반 필터 (Music Analysis API 연동 시)
   * GPT 기반 자동 요약/추천 문장 생성

---

## ✅ 3. Tech Stack (기술 스택)

* **GitHub Actions**: 스케줄러 및 CI/CD 자동화
* **Python**: 크롤러 및 데이터 처리
* **BeautifulSoup / Selenium**: HTML 파싱 (API 미지원 시)
* **DB**: SQLite(로컬) 또는 PostgreSQL(확장성 고려)
* **React**: Github Pages용 프론트엔드 SPA
* **Chart.js, recharts 등**: 트렌드 그래프 시각화
* **Pandas/Jinja2/Markdown**: 데이터 정리 및 백업

---

## ✅ 4. 개발 순서

1. [ ] DB 스키마 설계 및 초기화 스크립트 작성
2. [ ] 각 플랫폼별 크롤러 구현 (API 우선, 국가/연령대별 데이터 포함)
3. [ ] 크롤링 데이터 DB 저장 및 날짜별 백업 구조 구현
4. [ ] Github Actions 워크플로우 작성 (`.github/workflows/crawler.yml`)
5. [ ] React 기반 Github Pages 프로젝트 생성 및 기본 UI 구현
6. [ ] 날짜/플랫폼/국가/연령대별 차트 조회 기능 구현
7. [ ] 곡별 유튜브 임베드, 링크, 그래프 등 시각화 기능 구현
8. [ ] 배포 및 테스트, 알림 연동(선택)

---

## ✅ 5. 추가 Notes

* TikTok 등 일부 플랫폼은 비공식 API 또는 트렌드 추적 도구(Tokboard, Trendpop 등) 활용 필요
* 크롤링 요청은 속도 제한/차단 우려 있으므로 User-Agent, 시간차 실행 등 고려
* 국가/연령대별 데이터는 플랫폼 API 지원 범위 내에서만 제공
* 요일별/기간별 트렌드 비교, 추천, 자동 요약 등은 추후 고도화 시점에 도입

---

## ✅ 6. 결과물 예시 (React UI)

- 날짜별/플랫폼별/국가별/연령대별 차트 리스트
- 곡별 유튜브 영상 임베드 및 플랫폼 링크
- 인기 변화 추이 그래프
- 예시 스크린샷/구성도는 개발 중 추가
