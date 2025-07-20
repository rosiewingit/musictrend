import React from 'react';

// 날짜 선택 컴포넌트
function DateSelector({ date, onChange }) {
    return (
        <div style={{ marginBottom: '1rem' }}>
            <label>
                날짜 선택:
                <input type="date" value={date} onChange={e => onChange(e.target.value)} />
            </label>
        </div>
    );
}

export default DateSelector; 