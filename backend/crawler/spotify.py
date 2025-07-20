import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import date
import re

# Spotify Top 50 Korea 차트 URL (공식 API가 아니므로 웹 크롤링)
CHART_URL = 'https://spotifycharts.com/regional/kr/daily/latest'
DB_PATH = 'backend/musictrend.db'

# 유튜브 검색 URL 템플릿 (간단 매칭용)
YOUTUBE_SEARCH_URL = 'https://www.youtube.com/results?search_query={}'

# 유튜브 링크를 실제로 자동 추출하려면 별도 API나 크롤링 필요(여기선 생략)
def get_youtube_url(title, artist):
    # 실제 구현 시 YouTube Data API 또는 검색 결과 파싱 필요
    # 여기선 검색 URL만 반환
    query = f"{title} {artist} official audio"
    return YOUTUBE_SEARCH_URL.format(requests.utils.quote(query))

# Spotify 차트 크롤링 함수
def crawl_spotify_chart():
    resp = requests.get(CHART_URL, headers={
        'User-Agent': 'Mozilla/5.0 (compatible; MusicTrendBot/1.0)'
    })
    soup = BeautifulSoup(resp.text, 'html.parser')
    rows = soup.select('table.chart-table tbody tr')
    result = []
    for i, row in enumerate(rows[:10]):  # Top 10만
        rank = int(row.select_one('.chart-table-position').text.strip())
        title = row.select_one('.chart-table-track strong').text.strip()
        artist = row.select_one('.chart-table-track span').text.strip().replace('by ', '')
        # 장르, 연령대, 국가는 샘플로 고정
        genre = 'Pop'
        country = 'KR'
        age_group = 'all'
        chart_date = str(date.today())
        youtube_url = get_youtube_url(title, artist)
        result.append({
            'title': title,
            'artist': artist,
            'platform': 'Spotify',
            'rank': rank,
            'genre': genre,
            'country': country,
            'age_group': age_group,
            'chart_date': chart_date,
            'youtube_url': youtube_url
        })
    return result

def save_to_db(data):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    for track in data:
        cur.execute('''
            INSERT INTO tracks (title, artist, platform, rank, genre, country, age_group, chart_date, youtube_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            track['title'], track['artist'], track['platform'], track['rank'], track['genre'],
            track['country'], track['age_group'], track['chart_date'], track['youtube_url']
        ))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    chart_data = crawl_spotify_chart()
    save_to_db(chart_data)
    print('Spotify 실시간 차트 Top 10 저장 완료!') 