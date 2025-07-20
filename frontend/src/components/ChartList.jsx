import React from 'react';
import YouTubeEmbed from './YouTubeEmbed';

// 차트 리스트 컴포넌트
function ChartList({ tracks }) {
    return (
        <div>
            <h2>차트 리스트</h2>
            <ul>
                {tracks.map((track, idx) => (
                    <li key={idx} style={{ marginBottom: '2rem' }}>
                        <div><b>{track.rank}위</b> - {track.title} / {track.artist} ({track.platform})</div>
                        <div>장르: {track.genre} | 국가: {track.country} | 연령대: {track.age_group}</div>
                        <div>
                            <a href={track.youtube_url} target="_blank" rel="noopener noreferrer">유튜브로 이동</a>
                        </div>
                        <YouTubeEmbed url={track.youtube_url} />
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ChartList; 