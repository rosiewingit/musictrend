import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import date

CHART_URL = 'https://charts.youtube.com/charts/TopSongs/global'
DB_PATH = 'backend/musictrend.db'

# 유튜브 검색 URL 템플릿
YOUTUBE_SEARCH_URL = 'https://www.youtube.com/results?search_query={}'

def get_youtube_url(title, artist):
    query = f"{title} {artist} official audio"
    return YOUTUBE_SEARCH_URL.format(requests.utils.quote(query))

def crawl_youtube_chart():
    resp = requests.get(CHART_URL, headers={
        'User-Agent': 'Mozilla/5.0 (compatible; MusicTrendBot/1.0)'
    })
    soup = BeautifulSoup(resp.text, 'html.parser')
    rows = soup.select('ytmc-entity-row')
    print(f'[DEBUG] rows found: {len(rows)}')  # 크롤링 결과 개수 출력
    if len(rows) == 0:
        print('[WARNING] 유튜브 차트 크롤링 결과가 없습니다. 셀렉터/사이트 구조를 점검하세요.')
    result = []
    for i, row in enumerate(rows[:10]):
        # YouTube Music Charts는 구조가 자주 바뀌므로, 실제로는 API나 더 정교한 파싱 필요
        title = row.select_one('ytmc-entity-title').text.strip() if row.select_one('ytmc-entity-title') else f'Sample Song {i+1}'
        artist = row.select_one('ytmc-entity-artists').text.strip() if row.select_one('ytmc-entity-artists') else f'Artist {i+1}'
        rank = i + 1
        genre = 'Pop'
        country = 'GLOBAL'
        age_group = 'all'
        chart_date = str(date.today())
        youtube_url = get_youtube_url(title, artist)
        result.append({
            'title': title,
            'artist': artist,
            'platform': 'YouTube',
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
    chart_data = crawl_youtube_chart()
    save_to_db(chart_data)
    print('YouTube Music Charts Top 10 저장 완료!') 