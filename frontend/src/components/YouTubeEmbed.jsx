import React from 'react';

// 유튜브 URL에서 videoId 추출
function getYouTubeId(url) {
    const match = url.match(/(?:v=|youtu.be\/)([\w-]{11})/);
    return match ? match[1] : null;
}

// 유튜브 임베드 컴포넌트
function YouTubeEmbed({ url }) {
    const videoId = getYouTubeId(url);
    if (!videoId) return null;
    return (
        <div style={{ marginTop: '0.5rem' }}>
            <iframe
                width="320"
                height="180"
                src={`https://www.youtube.com/embed/${videoId}`}
                title="YouTube video player"
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
            ></iframe>
        </div>
    );
}

export default YouTubeEmbed; 