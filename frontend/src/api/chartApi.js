// 플랫폼별 차트 데이터 fetch 함수
export async function fetchChartData(date, platform = 'Spotify') {
  // 파일명 결정
  const file = platform.toLowerCase() + '.json';
  const url = `/data/${date}/${file}`;
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error('데이터를 불러올 수 없습니다');
    const data = await res.json();
    return data;
  } catch (e) {
    // 에러 시 빈 배열 반환
    return [];
  }
} 