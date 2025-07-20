import sqlite3
import os
import json
from datetime import date

# DB 파일 경로
DB_PATH = 'musictrend.db'
DATA_DIR = '../data'

# DB 초기화 함수
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            artist TEXT,
            platform TEXT,
            rank INTEGER,
            genre TEXT,
            country TEXT,
            age_group TEXT,
            chart_date TEXT,
            youtube_url TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 샘플 데이터 삽입 함수
def insert_sample():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO tracks (title, artist, platform, rank, genre, country, age_group, chart_date, youtube_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        'Sample Song', 'Sample Artist', 'Spotify', 1, 'Pop', 'KR', '20s', str(date.today()), 'https://youtube.com/watch?v=xxxx'
    ))
    conn.commit()
    conn.close()

# DB에서 특정 날짜의 Spotify 차트 데이터 조회
def export_spotify_chart_to_json(target_date=None):
    if target_date is None:
        target_date = str(date.today())
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        SELECT title, artist, platform, rank, genre, country, age_group, chart_date, youtube_url
        FROM tracks
        WHERE platform = 'Spotify' AND chart_date = ?
        ORDER BY rank ASC
    ''', (target_date,))
    rows = cur.fetchall()
    conn.close()
    # dict로 변환
    chart = [
        {
            'title': r[0], 'artist': r[1], 'platform': r[2], 'rank': r[3],
            'genre': r[4], 'country': r[5], 'age_group': r[6], 'chart_date': r[7], 'youtube_url': r[8]
        }
        for r in rows
    ]
    # 저장 경로 생성
    out_dir = os.path.join(DATA_DIR, target_date)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'spotify.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(chart, f, ensure_ascii=False, indent=2)
    print(f'Spotify 차트 데이터가 {out_path}에 저장되었습니다.')

# DB에서 특정 날짜의 YouTube 차트 데이터 조회
def export_youtube_chart_to_json(target_date=None):
    if target_date is None:
        target_date = str(date.today())
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        SELECT title, artist, platform, rank, genre, country, age_group, chart_date, youtube_url
        FROM tracks
        WHERE platform = 'YouTube' AND chart_date = ?
        ORDER BY rank ASC
    ''', (target_date,))
    rows = cur.fetchall()
    conn.close()
    chart = [
        {
            'title': r[0], 'artist': r[1], 'platform': r[2], 'rank': r[3],
            'genre': r[4], 'country': r[5], 'age_group': r[6], 'chart_date': r[7], 'youtube_url': r[8]
        }
        for r in rows
    ]
    out_dir = os.path.join(DATA_DIR, target_date)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'youtube.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(chart, f, ensure_ascii=False, indent=2)
    print(f'YouTube 차트 데이터가 {out_path}에 저장되었습니다.')

def export_soundcloud_chart_to_json(target_date=None):
    if target_date is None:
        target_date = str(date.today())
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        SELECT title, artist, platform, rank, genre, country, age_group, chart_date, youtube_url
        FROM tracks
        WHERE platform = 'SoundCloud' AND chart_date = ?
        ORDER BY rank ASC
    ''', (target_date,))
    rows = cur.fetchall()
    conn.close()
    chart = [
        {
            'title': r[0], 'artist': r[1], 'platform': r[2], 'rank': r[3],
            'genre': r[4], 'country': r[5], 'age_group': r[6], 'chart_date': r[7], 'youtube_url': r[8]
        }
        for r in rows
    ]
    out_dir = os.path.join(DATA_DIR, target_date)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'soundcloud.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(chart, f, ensure_ascii=False, indent=2)
    print(f'SoundCloud 차트 데이터가 {out_path}에 저장되었습니다.')

def export_beatport_chart_to_json(target_date=None):
    if target_date is None:
        target_date = str(date.today())
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        SELECT title, artist, platform, rank, genre, country, age_group, chart_date, youtube_url
        FROM tracks
        WHERE platform = 'Beatport' AND chart_date = ?
        ORDER BY rank ASC
    ''', (target_date,))
    rows = cur.fetchall()
    conn.close()
    chart = [
        {
            'title': r[0], 'artist': r[1], 'platform': r[2], 'rank': r[3],
            'genre': r[4], 'country': r[5], 'age_group': r[6], 'chart_date': r[7], 'youtube_url': r[8]
        }
        for r in rows
    ]
    out_dir = os.path.join(DATA_DIR, target_date)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'beatport.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(chart, f, ensure_ascii=False, indent=2)
    print(f'Beatport 차트 데이터가 {out_path}에 저장되었습니다.')

if __name__ == '__main__':
    # DB 초기화 및 샘플 데이터 삽입(기존 코드 유지)
    init_db()
    insert_sample()
    print('DB 초기화 및 샘플 데이터 삽입 완료!')
    # 날짜별 Spotify/YouTube 차트 JSON 내보내기
    export_spotify_chart_to_json()
    export_youtube_chart_to_json()
    export_soundcloud_chart_to_json()
    export_beatport_chart_to_json() 