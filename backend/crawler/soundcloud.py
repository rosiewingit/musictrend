import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import date

CHART_URL = 'https://soundcloud.com/charts/top?genre=all-music&country=all-countries'
DB_PATH = 'backend/musictrend.db'

# 유튜브 검색 URL 템플릿
YOUTUBE_SEARCH_URL = 'https://www.youtube.com/results?search_query={}'

def get_youtube_url(title, artist):
    query = f"{title} {artist} official audio"
    return YOUTUBE_SEARCH_URL.format(requests.utils.quote(query))

def crawl_soundcloud_chart():
    resp = requests.get(CHART_URL, headers={
        'User-Agent': 'Mozilla/5.0 (compatible; MusicTrendBot/1.0)'
    })
    soup = BeautifulSoup(resp.text, 'html.parser')
    cards = soup.select('li.chartTracks__item')
    print(f'[DEBUG] cards found: {len(cards)}')  # 크롤링 결과 개수 출력
    if len(cards) == 0:
        print('[WARNING] 사운드클라우드 차트 크롤링 결과가 없습니다. 셀렉터/사이트 구조를 점검하세요.')
    result = []
    for i, card in enumerate(cards[:10]):
        title_tag = card.select_one('a.chartTrack__title')
        artist_tag = card.select_one('a.chartTrack__username')
        title = title_tag.text.strip() if title_tag else f'Sample Song {i+1}'
        artist = artist_tag.text.strip() if artist_tag else f'Artist {i+1}'
        rank = i + 1
        genre = 'All'
        country = 'GLOBAL'
        age_group = 'all'
        chart_date = str(date.today())
        youtube_url = get_youtube_url(title, artist)
        result.append({
            'title': title,
            'artist': artist,
            'platform': 'SoundCloud',
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
    chart_data = crawl_soundcloud_chart()
    save_to_db(chart_data)
    print('SoundCloud Trending Top 10 저장 완료!') 