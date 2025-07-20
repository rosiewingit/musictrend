import sqlite3

DB_PATH = '../musictrend.db'

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

if __name__ == '__main__':
    init_db()
    print('DB 초기화 완료!') 