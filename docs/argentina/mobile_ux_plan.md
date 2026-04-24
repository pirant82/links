# 아르헨티나 일정표 모바일 UX 혁신 플랜

> **핵심 목표**
> 1. 짧은 일정 글자 잘림 해결
> 2. 모바일 최우선 레이아웃으로 전환
> 3. 지도 링크를 명시적 버튼으로 표시
> 4. 기존 그리드 타임테이블은 하단에 접기/펼치기로 보존

---

## 1. 현재 문제 진단

| 문제 | 원인 |
|---|---|
| 짧은 이벤트(10~20분) 글자 잘림 | `height: calc(duration*100% - 2px)` → 픽셀 높이 너무 작아 overflow:hidden으로 잘림 |
| 모바일 가로 스크롤 필요 | 그리드가 `min-width: 1200px` 고정 |
| 지도 링크 인식 안 됨 | 이벤트 블록 전체가 링크라 탭 영역도 불명확 |
| 글자 너무 작음 | `font-size: 0.7rem` |

---

## 2. 새 레이아웃 구조

```
┌─────────────────────────────┐
│  🕐 시계 / D-Day 카운트다운    │  ← 유지
├─────────────────────────────┤
│  [4/26] [4/27] [4/28] ...   │  ← 새로: 가로 스크롤 날짜 탭
├─────────────────────────────┤
│  세로 타임라인 (선택된 날)      │  ← 새로: 메인 뷰
│  ┌──────┬──────────────┬──┐ │
│  │07:35 │✈️ 멘도사 출발 │📍│ │
│  │ ART  │LA2434        │  │ │
│  │19:35 │              │  │ │
│  │ KST  │              │  │ │
│  └──────┴──────────────┴──┘ │
├─────────────────────────────┤
│  🏠 숙소 안내                │  ← 유지
├─────────────────────────────┤
│  💬 응원 채팅                │  ← 유지
├─────────────────────────────┤
│  ▼ 전체 그리드 타임테이블 보기  │  ← 새로: 접기/펼치기
│  (기존 가로 스크롤 그리드)      │
└─────────────────────────────┘
```

---

## 3. 세부 구현 명세

### 3-A. 날짜 탭 바 (Day Tab Bar)

```css
/* 가로 스크롤 탭, 스크롤바 숨김 */
.day-tabs {
  display: flex;
  overflow-x: auto;
  scrollbar-width: none;
  gap: 8px;
  padding: 12px 16px;
  background: #fff;
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 20;
}
.day-tab {
  flex-shrink: 0;
  padding: 8px 16px;
  border-radius: 20px;
  border: 1.5px solid var(--border);
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
  background: #fff;
  white-space: nowrap;
}
.day-tab.active {
  background: var(--green);
  color: #fff;
  border-color: var(--green);
}
```

- 탭 레이블: `4/26 일`, `4/27 월`, `4/28 화`, `4/29 수`, `4/30 목`, `5/1 금`, `5/2 토`
- 페이지 로드 시 **오늘 날짜 탭이 자동 선택** (없으면 첫 탭)
- 탭 클릭 → 해당 날짜의 이벤트만 타임라인에 표시

### 3-B. 세로 타임라인 카드

```
┌─────────────────────────────────────┐
│  ● 11:06                            │
│    (23:06 KST)                      │
│  🍷 멘도사(MDZ) 도착              📍 │ ← 이벤트 카드
│                                     │
│  ●─────────────────────── (30분)    │  ← 수직선 연결
│                                     │
│  ● 12:00                            │
│  🚗 카테나 팀 픽업                    │
```

**카드 구조 (HTML)**:
```html
<div class="timeline-item event-wine [past|current]">
  <div class="tl-time">
    <span class="tl-art">11:06</span>
    <span class="tl-kst">23:06 KST</span>
  </div>
  <div class="tl-dot"></div>  <!-- 타임라인 점 -->
  <div class="tl-content">
    <div class="tl-title">🍷 멘도사(MDZ) 도착</div>
    <div class="tl-duration">30분</div>
  </div>
  <a href="구글맵URL" target="_blank" class="tl-map-btn">
    📍
  </a>
</div>
```

**CSS 핵심**:
```css
.timeline-item {
  display: grid;
  grid-template-columns: 60px 20px 1fr 44px;
  align-items: flex-start;
  gap: 8px;
  padding: 12px 16px;
  min-height: 56px;       /* 최소 높이 보장 → 글자 잘림 없음 */
  border-bottom: 1px solid var(--border);
}
.tl-time {
  display: flex;
  flex-direction: column;
  font-weight: 700;
  font-size: 0.85rem;
  color: var(--green);
}
.tl-kst {
  font-size: 0.65rem;
  color: var(--sub);
}
.tl-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--green);
  margin-top: 4px;
  flex-shrink: 0;
  position: relative;
}
/* 세로 연결선 */
.tl-dot::after {
  content: '';
  position: absolute;
  top: 12px; left: 5px;
  width: 2px;
  height: calc(100% + 20px);  /* 다음 아이템까지 연결 */
  background: var(--border);
}
.tl-title {
  font-size: 0.9rem;
  font-weight: 700;
  line-height: 1.3;
}
.tl-duration {
  font-size: 0.72rem;
  color: var(--sub);
  margin-top: 2px;
}
.tl-map-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #f0fdf4;
  font-size: 1.1rem;
  text-decoration: none;
  border: 1.5px solid #bbf7d0;
  flex-shrink: 0;
}
.tl-map-btn:active { background: #dcfce7; }

/* url 없는 이벤트는 지도 버튼 숨김 */
.tl-map-btn.no-url { visibility: hidden; }

/* 상태 */
.timeline-item.past .tl-title { text-decoration: line-through; color: var(--sub); }
.timeline-item.past .tl-dot   { background: #d1d5db; }
.timeline-item.current { background: #f0fdf4; border-left: 4px solid var(--green); }
.timeline-item.current .tl-dot { animation: pulse-dot 1.5s infinite; }
@keyframes pulse-dot { 0%,100% { transform: scale(1); } 50% { transform: scale(1.4); } }
```

### 3-C. 이벤트 타입별 색상

| type | dot 색상 | 배경 강조 |
|---|---|---|
| `flight` | `#1d4ed8` (파랑) | `#eff6ff` |
| `wine` | `#be185d` (핑크) | `#fdf2f8` |
| `stay` | `#166534` (초록) | `#f0fdf4` |

### 3-D. 기존 그리드 타임테이블 — 접기/펼치기

```html
<div class="grid-toggle-section">
  <button id="grid-toggle-btn" onclick="toggleGrid()">
    📊 전체 그리드 타임테이블 보기 ▼
  </button>
  <div id="grid-wrapper" class="timetable-wrapper" style="display:none;">
    <!-- 기존 그리드 그대로 -->
  </div>
</div>
```

```javascript
function toggleGrid() {
  const w = document.getElementById('grid-wrapper');
  const btn = document.getElementById('grid-toggle-btn');
  const isHidden = w.style.display === 'none';
  w.style.display = isHidden ? 'block' : 'none';
  btn.textContent = isHidden
    ? '📊 전체 그리드 타임테이블 접기 ▲'
    : '📊 전체 그리드 타임테이블 보기 ▼';
}
```

---

## 4. 짧은 이벤트 글자 잘림 — 완전 해결

현재 구조(grid absolute positioning)에서는 `duration < 0.3h`이면 픽셀 높이가 ~20px 이하라 텍스트가 무조건 잘림.

**해결**: 세로 타임라인에서는 **모든 이벤트가 flex row**이므로 픽셀 높이와 무관하게 텍스트 전체 표시. `min-height: 56px` 보장.

---

## 5. 구현 순서

- [ ] **Step 1**: CSS에 `day-tabs`, `timeline-item` 관련 스타일 추가
- [ ] **Step 2**: HTML에 `#day-tabs-bar`와 `#timeline-view` 섹션 추가 (기존 timetable-wrapper 위에)
- [ ] **Step 3**: `initTimeline()` JS 함수 작성
  - RAW_EVENTS를 날짜별로 그룹화
  - 선택된 날짜의 이벤트를 `.timeline-item` 카드로 렌더링
  - KST 변환 (ART + 12시간)
  - 현재/과거/미래 상태 계산
- [ ] **Step 4**: 기존 `initTimetable()` 호출을 그리드 영역으로 이동, 접기/펼치기 래퍼 적용
- [ ] **Step 5**: `updateUI()`에 현재 진행 중 이벤트 하이라이트 로직 추가 (타임라인 뷰 자동 갱신)

---

## 6. KST 변환 로직

```javascript
function artToKst(dateStr, timeStr) {
  // ART = UTC-3, KST = UTC+9 → 차이 = +12h
  const [h, m] = timeStr.split(':').map(Number);
  let kstH = h + 12;
  let kstDate = dateStr;
  if (kstH >= 24) {
    kstH -= 24;
    // 날짜 하루 증가
    const d = new Date(dateStr);
    d.setDate(d.getDate() + 1);
    kstDate = d.toISOString().slice(0,10);
  }
  return `${kstH.toString().padStart(2,'0')}:${m.toString().padStart(2,'0')} KST`;
}
```

---

## 7. 최종 UX 흐름 (모바일)

1. 페이지 열기 → 시계/카운트다운 보임
2. 날짜 탭 바에서 오늘 날짜 자동 선택 (출장 기간이면 해당 날짜)
3. 세로 타임라인 스크롤 → 각 이벤트 카드 확인
4. 현재 진행 중인 이벤트 초록 하이라이트로 즉시 파악
5. 📍 버튼 탭 → 구글 지도 바로 이동
6. 하단 "전체 그리드 보기" → 기존 가로 스크롤 그리드 펼쳐짐
