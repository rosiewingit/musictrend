import React, { useState, useEffect } from 'react';
import ChartList from '../components/ChartList';
import DateSelector from '../components/DateSelector';
import { fetchChartData } from '../api/chartApi';

const PLATFORMS = [
    { label: 'Spotify', value: 'Spotify' },
    { label: 'YouTube', value: 'YouTube' },
    { label: 'SoundCloud', value: 'SoundCloud' },
    { label: 'Beatport', value: 'Beatport' }
];

function Home() {
    const [date, setDate] = useState(() => {
        const d = new Date();
        return d.toISOString().slice(0, 10);
    });
    const [platform, setPlatform] = useState('Spotify');
    const [tracks, setTracks] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    // 날짜/플랫폼 변경 시 차트 데이터 fetch
    useEffect(() => {
        setLoading(true);
        setError('');
        fetchChartData(date, platform)
            .then(data => setTracks(data))
            .catch(() => setError('차트 데이터를 불러올 수 없습니다.'))
            .finally(() => setLoading(false));
    }, [date, platform]);

    return (
        <div>
            <h1>Music Trend Chart</h1>
            <DateSelector date={date} onChange={setDate} />
            <div style={{ marginBottom: '1rem' }}>
                <label>
                    플랫폼 선택:
                    <select value={platform} onChange={e => setPlatform(e.target.value)}>
                        {PLATFORMS.map(p => (
                            <option key={p.value} value={p.value}>{p.label}</option>
                        ))}
                    </select>
                </label>
            </div>
            {loading && <div>로딩 중...</div>}
            {error && <div style={{ color: 'red' }}>{error}</div>}
            <ChartList tracks={tracks} />
        </div>
    );
}

export default Home; 