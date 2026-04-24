# argentina.html 완전 정확 반영 플랜

> **목표**: `table.md`의 모든 항목을 단 하나도 빠뜨리지 않고 `argentina.html`에 반영하고,  
> 모든 장소를 클릭 시 정확한 구글 지도로 연결한다.

---

## 1. 현황 진단: 누락된 이벤트 목록

`table.md` ↔ `RAW_EVENTS` 1:1 대조 결과.

### 4월 26일 (일)
| table.md 항목 | HTML 반영 여부 | 비고 |
|---|---|---|
| 11:06 멘도사 공항 도착 | ✅ | |
| 12:00 픽업 이동 | ✅ | |
| 12:30 파크 하얏트 도착 | ✅ | |
| 13:00 점심 & 휴식 | ✅ | |
| 19:20 로비 집합 | ✅ | |
| 19:30 저녁 @ Soberana | ✅ | |
| **21:30 호텔 복귀 및 휴식** | ❌ **누락** | |

### 4월 27일 (월)
| table.md 항목 | HTML 반영 여부 | 비고 |
|---|---|---|
| 07:00 조식 | ✅ | |
| 09:00 체크아웃 | ✅ | |
| 09:10 와이너리 이동 | ✅ | |
| 10:00 와이너리 도착 | ✅ | |
| 10:10 피라미드 투어 | ✅ | |
| 10:40 와인 연구소 소개 | ✅ | |
| 11:20 말벡 블렌딩 세션 | ✅ | |
| 12:20 Nicolas Catena 시음 | ✅ | |
| **12:40 Angelica 이동** | ❌ **누락** | |
| 13:00 점심 @ Angelica Cocina Maestra | ✅ | |
| 15:30 증류소 방문 | ✅ | |
| 15:45 La Piramide Vineyard | ✅ | |
| **16:30 Angelica Vineyard 이동** | ❌ **누락** | |
| 17:00 Angelica Vineyard 방문 | ✅ | |
| **17:30 La Vendimia 이동** | ❌ **누락** | |
| 19:00 La Vendimia 도착 & 체크인 | ✅ | |
| 19:30 고기 손질 클래스 | ✅ | |
| 20:30 아르헨티나 전통 아사도 저녁 | ✅ | |
| **22:30 휴식** | ❌ **누락** | |

### 4월 28일 (화)
| table.md 항목 | HTML 반영 여부 | 비고 |
|---|---|---|
| 07:30 조식 | ✅ | |
| 08:00 Adrianna 이동 | ✅ | |
| 10:30 Adrianna 투어/시음 | ✅ | |
| **12:30 La Bodeguita 이동** | ❌ **누락** | 별도 장소, 지도 URL도 없음 |
| 12:35 포도밭 야외 점심 | ✅ (시간 맞음) | |
| **15:30 La Vendimia 복귀 이동 시작** | ❌ **누락** | |
| **18:00 La Vendimia 도착** | ⚠️ **부정확** | 현재 '켈틱 명상'만 있음, 도착 이벤트 별도 필요 |
| **18:30~20:00 휴식** | ❌ **누락** | |
| 20:00 Malbec Argentino 저녁 | ✅ | |
| **22:30 휴식** | ❌ **누락** | |

### 4월 29일 (수)
| table.md 항목 | HTML 반영 여부 | 비고 |
|---|---|---|
| 10:30 체크아웃 & Achaval 픽업 | ✅ | |
| **11:30 Achaval Ferrer 도착** | ❌ **누락** | |
| 11:40 Finca Bella Vista 방문 | ✅ | |
| 12:15 와인 시음 | ✅ | |
| **13:15 Quimera Bistro 이동** | ❌ **누락** | |
| 13:30 점심 @ Quimera Bistro | ✅ | |
| **15:45 호텔 이동** | ❌ **누락** | |
| 16:15 HUENTALA 체크인 | ✅ | |
| **17:00 자유 시간** | ❌ **누락** | |
| **19:45 저녁 픽업** | ❌ **누락** | |
| 20:00 저녁 식사 | ✅ | |
| **22:30 호텔 복귀** | ❌ **누락** | |

### 4월 30일 (목)
| table.md 항목 | HTML 반영 여부 | 비고 |
|---|---|---|
| 10:30 픽업 → Quimera 이동 | ✅ | |
| 11:00 Quimera Winery 도착 | ✅ | |
| 12:30 아사도 점심 | ✅ | |
| 15:30 멘도사 시티 투어 | ✅ | |
| **18:00 호텔 도착** | ❌ **누락** | |
| **19:45 저녁 픽업** | ❌ **누락** | |
| 20:00 저녁 식사 | ✅ | |
| **22:30 호텔 복귀** | ❌ **누락** | |

### 5월 1일 (금) — 출국
| table.md 항목 | HTML 반영 여부 | 비고 |
|---|---|---|
| 04:45 공항 이동 픽업 | ✅ | |
| **05:15 공항 도착** | ❌ **누락** | |
| **07:35 LATAM 출발 → 리마** | ⚠️ **날짜 오류** | HTML에서 `2026-05-02`로 잘못 설정됨 → `2026-05-01`로 수정 필요 |

---

## 2. 구글 지도 URL 문제 목록

### 현재 MAPS 객체 정의 문제점

```
현재 HTML의 MAPS 키 → 실제 연결되는 장소 → 문제
```

| 키 | 현재 검색어 | 문제 |
|---|---|---|
| `MDZ` | Governor Francisco Gabrielli International Airport | ✅ 괜찮음 |
| `HYATT` | Park Hyatt Mendoza | ✅ 괜찮음 |
| `SOBERANA` | Soberana Mendoza | ✅ 괜찮음 (레스토랑 검색됨) |
| `CATENA` | Catena Zapata Winery | ✅ 괜찮음 (와이너리 본체) |
| `ANGELICA` | Angelica Cocina Maestra | ✅ 괜찮음 (레스토랑) |
| `VENDIMIA` | Catena Zapata La Vendimia | ⚠️ 검색 결과 불확실 — 더 구체적인 주소 필요 |
| `ADRIANNA` | Adrianna Vineyard | ⚠️ 위치 결과 불확실 — "Adrianna Vineyard Gualtallary Mendoza" 권장 |
| `ACHAVAL` | Achaval Ferrer Winery | ✅ 괜찮음 |
| `QUIMERA` | Quimera Bistro Mendoza | ⚠️ **치명적 오류**: 4/30일 Quimera **Winery**도 동일 URL 사용 중 — 별도 키 필요 |
| `HUENTALA` | Huentala Hotel Mendoza | ✅ 괜찮음 |

### 추가로 필요한 MAPS 키 (현재 정의 없음)

| 추가 키 | 장소 | 권장 검색어 |
|---|---|---|
| `BODEGUITA` | La Bodeguita (4/28 야외 점심) | `La Bodeguita Gualtallary Alto Mendoza` |
| `FINCA_BELLA` | Finca Bella Vista (4/29) | `Finca Bella Vista Achaval Ferrer Mendoza` |
| `QUIMERA_WINERY` | Quimera Winery (4/30, Bistro와 다른 장소) | `Quimera Winery Perdriel Mendoza` |
| `LA_PIRAMIDE` | La Piramide Vineyard (4/27) | `La Piramide Vineyard Catena Zapata Agrelo` |
| `ANGELICA_VYD` | Angelica Vineyard (4/27, Catena 소유) | `Angelica Vineyard Catena Zapata Agrelo Mendoza` |
| `MENDOZA_CITY` | 멘도사 시티 (시티 투어 4/30) | `Mendoza City Center Argentina` |
| `LATAM_MDZ` | 멘도사 공항 (출발 5/1) | MDZ 와 동일하므로 재사용 가능 |

---

## 3. 수정할 RAW_EVENTS 전체 (교체 기준)

아래가 `table.md` 기준 **완전한** 이벤트 목록이다.  
이 목록으로 HTML의 `RAW_EVENTS` 배열 전체를 교체한다.

```javascript
const RAW_EVENTS = [
  // ── 4/25 (ART) ── 비행편 (한국→LA→멘도사 경유)
  { date: '2026-04-25', time: '02:30', duration: 11.1,  task: '✈️ 한국 출국 (KE017)', type: 'flight', url: MAPS.MDZ },
  { date: '2026-04-25', time: '13:40', duration: 6.25,  task: '🇺🇸 LAX 대기', type: 'flight' },
  { date: '2026-04-25', time: '19:55', duration: 10.6,  task: '✈️ LA 출발 (LA603)', type: 'flight' },

  // ── 4/26 (ART) ──
  { date: '2026-04-26', time: '06:35', duration: 3.4,   task: '🇨🇱 산티아고 대기', type: 'flight' },
  { date: '2026-04-26', time: '10:00', duration: 1.1,   task: '✈️ 산티아고 출발', type: 'flight' },
  { date: '2026-04-26', time: '11:06', duration: 0.9,   task: '🍷 멘도사(MDZ) 도착', type: 'wine', url: MAPS.MDZ },
  { date: '2026-04-26', time: '12:00', duration: 0.5,   task: '🚗 카테나 팀 픽업', type: 'wine' },
  { date: '2026-04-26', time: '12:30', duration: 0.5,   task: '🏨 파크 하얏트 도착', type: 'stay', url: MAPS.HYATT },
  { date: '2026-04-26', time: '13:00', duration: 6.33,  task: '🍴 테라스 점심 & 체크인 & 휴식', type: 'stay', url: MAPS.HYATT },
  { date: '2026-04-26', time: '19:20', duration: 0.17,  task: '📍 로비 집합', type: 'wine', url: MAPS.HYATT },
  { date: '2026-04-26', time: '19:30', duration: 2.0,   task: '🍽️ 저녁 @ Soberana', type: 'wine', url: MAPS.SOBERANA },
  { date: '2026-04-26', time: '21:30', duration: 0.5,   task: '🛏️ 호텔 복귀 & 휴식', type: 'stay', url: MAPS.HYATT },

  // ── 4/27 (ART) ── Catena Zapata
  { date: '2026-04-27', time: '07:00', duration: 2.0,   task: '🍳 호텔 조식', type: 'stay', url: MAPS.HYATT },
  { date: '2026-04-27', time: '09:00', duration: 0.17,  task: '🔑 체크아웃', type: 'stay', url: MAPS.HYATT },
  { date: '2026-04-27', time: '09:10', duration: 0.83,  task: '🚗 와이너리 이동 (50분)', type: 'wine' },
  { date: '2026-04-27', time: '10:00', duration: 0.17,  task: '🍇 Catena Zapata 도착', type: 'wine', url: MAPS.CATENA },
  { date: '2026-04-27', time: '10:10', duration: 0.5,   task: '📐 피라미드 투어 & 역사 소개', type: 'wine', url: MAPS.CATENA },
  { date: '2026-04-27', time: '10:40', duration: 0.67,  task: '🔬 카테나 와인 연구소 소개', type: 'wine', url: MAPS.CATENA },
  { date: '2026-04-27', time: '11:20', duration: 1.0,   task: '🧪 말벡 블렌딩 세션 (Nesti Bajda)', type: 'wine', url: MAPS.CATENA },
  { date: '2026-04-27', time: '12:20', duration: 0.33,  task: '🍷 Nicolas Catena Zapata 시음', type: 'wine', url: MAPS.CATENA },
  { date: '2026-04-27', time: '12:40', duration: 0.33,  task: '🚗 Angelica 이동', type: 'wine' },
  { date: '2026-04-27', time: '13:00', duration: 2.5,   task: '🌟 점심 @ Angelica Cocina (미슐랭1*)', type: 'wine', url: MAPS.ANGELICA },
  { date: '2026-04-27', time: '15:30', duration: 0.25,  task: '🥃 증류소 방문 & 시음', type: 'wine', url: MAPS.CATENA },
  { date: '2026-04-27', time: '15:45', duration: 0.75,  task: '🌿 La Piramide Vineyard (카베르네 소비뇽)', type: 'wine', url: MAPS.LA_PIRAMIDE },
  { date: '2026-04-27', time: '16:30', duration: 0.5,   task: '🚗 Angelica Vineyard 이동 (30분)', type: 'wine' },
  { date: '2026-04-27', time: '17:00', duration: 0.5,   task: '🍇 Angelica Vineyard (말벡 올드바인)', type: 'wine', url: MAPS.ANGELICA_VYD },
  { date: '2026-04-27', time: '17:30', duration: 1.5,   task: '🚗 La Vendimia 이동 (1시간 20분)', type: 'wine' },
  { date: '2026-04-27', time: '19:00', duration: 0.5,   task: '🏠 La Vendimia 도착 & 체크인', type: 'stay', url: MAPS.VENDIMIA },
  { date: '2026-04-27', time: '19:30', duration: 1.0,   task: '🥩 고기 손질 클래스', type: 'wine', url: MAPS.VENDIMIA },
  { date: '2026-04-27', time: '20:30', duration: 2.0,   task: '🔥 전통 아사도 저녁', type: 'wine', url: MAPS.VENDIMIA },
  { date: '2026-04-27', time: '22:30', duration: 0.5,   task: '🛏️ 휴식', type: 'stay', url: MAPS.VENDIMIA },

  // ── 4/28 (ART) ── Adrianna Vineyard
  { date: '2026-04-28', time: '07:30', duration: 0.5,   task: '🍳 조식', type: 'stay', url: MAPS.VENDIMIA },
  { date: '2026-04-28', time: '08:00', duration: 2.5,   task: '🚗 Adrianna 이동 (2시간 30분)', type: 'wine' },
  { date: '2026-04-28', time: '10:30', duration: 2.0,   task: '🍇 Adrianna Vineyard 투어 & 시음', type: 'wine', url: MAPS.ADRIANNA },
  { date: '2026-04-28', time: '12:30', duration: 0.08,  task: '🚗 La Bodeguita 이동 (5분)', type: 'wine' },
  { date: '2026-04-28', time: '12:35', duration: 2.92,  task: '🍴 포도밭 야외 점심 (La Bodeguita)', type: 'wine', url: MAPS.BODEGUITA },
  { date: '2026-04-28', time: '15:30', duration: 2.5,   task: '🚗 La Vendimia 복귀 (2시간 30분)', type: 'wine' },
  { date: '2026-04-28', time: '18:00', duration: 0.5,   task: '🧘 La Vendimia 도착 & 켈틱 명상', type: 'stay', url: MAPS.VENDIMIA },
  { date: '2026-04-28', time: '18:30', duration: 1.5,   task: '😴 휴식', type: 'stay', url: MAPS.VENDIMIA },
  { date: '2026-04-28', time: '20:00', duration: 2.5,   task: '🍷 Malbec Argentino 저녁', type: 'wine', url: MAPS.VENDIMIA },
  { date: '2026-04-28', time: '22:30', duration: 0.5,   task: '🛏️ 휴식', type: 'stay', url: MAPS.VENDIMIA },

  // ── 4/29 (ART) ── Achaval Ferrer
  { date: '2026-04-29', time: '10:30', duration: 1.0,   task: '🚗 체크아웃 & Achaval 픽업', type: 'wine', url: MAPS.VENDIMIA },
  { date: '2026-04-29', time: '11:30', duration: 0.17,  task: '🍇 Achaval Ferrer 도착', type: 'wine', url: MAPS.ACHAVAL },
  { date: '2026-04-29', time: '11:40', duration: 0.58,  task: '🌿 Finca Bella Vista (110년 올드바인)', type: 'wine', url: MAPS.FINCA_BELLA },
  { date: '2026-04-29', time: '12:15', duration: 1.0,   task: '🍷 Achaval Ferrer 와인 시음', type: 'wine', url: MAPS.ACHAVAL },
  { date: '2026-04-29', time: '13:15', duration: 0.25,  task: '🚗 Quimera Bistro 이동', type: 'wine' },
  { date: '2026-04-29', time: '13:30', duration: 2.25,  task: '🍴 점심 @ Quimera Bistro (미슐랭 추천)', type: 'wine', url: MAPS.QUIMERA },
  { date: '2026-04-29', time: '15:45', duration: 0.5,   task: '🚗 Huentala 이동', type: 'wine' },
  { date: '2026-04-29', time: '16:15', duration: 0.75,  task: '🏨 HUENTALA 체크인', type: 'stay', url: MAPS.HUENTALA },
  { date: '2026-04-29', time: '17:00', duration: 2.75,  task: '☕ 자유 시간 & 휴식', type: 'stay', url: MAPS.HUENTALA },
  { date: '2026-04-29', time: '19:45', duration: 0.25,  task: '🚗 저녁 식사 픽업', type: 'wine', url: MAPS.HUENTALA },
  { date: '2026-04-29', time: '20:00', duration: 2.5,   task: '🍽️ 저녁 식사 (장소 추후 확정)', type: 'wine' },
  { date: '2026-04-29', time: '22:30', duration: 0.5,   task: '🛏️ 호텔 복귀 & 휴식', type: 'stay', url: MAPS.HUENTALA },

  // ── 4/30 (ART) ── Quimera Winery + 멘도사 시티
  { date: '2026-04-30', time: '10:30', duration: 0.5,   task: '🚗 Quimera Winery 이동', type: 'wine', url: MAPS.HUENTALA },
  { date: '2026-04-30', time: '11:00', duration: 1.5,   task: '🍇 Quimera Winery 방문 & 시음', type: 'wine', url: MAPS.QUIMERA_WINERY },
  { date: '2026-04-30', time: '12:30', duration: 3.0,   task: '🔥 포도밭 전통 아사도 점심', type: 'wine', url: MAPS.QUIMERA_WINERY },
  { date: '2026-04-30', time: '15:30', duration: 2.5,   task: '🏙️ 멘도사 시티 투어', type: 'wine', url: MAPS.MENDOZA_CITY },
  { date: '2026-04-30', time: '18:00', duration: 1.75,  task: '🏨 호텔 도착 & 휴식', type: 'stay', url: MAPS.HUENTALA },
  { date: '2026-04-30', time: '19:45', duration: 0.25,  task: '🚗 저녁 식사 픽업', type: 'wine', url: MAPS.HUENTALA },
  { date: '2026-04-30', time: '20:00', duration: 2.5,   task: '🍽️ 저녁 식사 (장소 추후 확정)', type: 'wine' },
  { date: '2026-04-30', time: '22:30', duration: 0.5,   task: '🛏️ 호텔 복귀 & 휴식', type: 'stay', url: MAPS.HUENTALA },

  // ── 5/1 (ART) ── 출국 ← 날짜 수정 필요 (기존 5/2로 잘못 기재)
  { date: '2026-05-01', time: '04:45', duration: 0.5,   task: '🚗 공항 이동 픽업', type: 'flight', url: MAPS.HUENTALA },
  { date: '2026-05-01', time: '05:15', duration: 2.33,  task: '🛫 멘도사 공항 도착 & 수속', type: 'flight', url: MAPS.MDZ },
  { date: '2026-05-01', time: '07:35', duration: 4.0,   task: '✈️ LATAM 출발 → 리마(페루)', type: 'flight', url: MAPS.MDZ },
];
```

---

## 4. 수정할 MAPS 객체 (교체 기준)

```javascript
const MAPS = {
  MDZ:           'https://www.google.com/maps/search/Mendoza+Airport+Governor+Francisco+Gabrielli+International',
  HYATT:         'https://www.google.com/maps/search/Park+Hyatt+Mendoza+Chile+1124',
  SOBERANA:      'https://www.google.com/maps/search/Soberana+Restaurante+Mendoza',
  CATENA:        'https://www.google.com/maps/search/Catena+Zapata+Winery+Agrelo+Lujan+de+Cuyo',
  ANGELICA:      'https://www.google.com/maps/search/Angelica+Cocina+Maestra+Lujan+de+Cuyo+Mendoza',
  ANGELICA_VYD:  'https://www.google.com/maps/search/Angelica+Vineyard+Catena+Zapata+Agrelo+Mendoza',
  LA_PIRAMIDE:   'https://www.google.com/maps/search/La+Piramide+Vineyard+Catena+Zapata+Lujan+de+Cuyo',
  VENDIMIA:      'https://maps.app.goo.gl/zeDAwGpeW8fUSnBK8',
  ADRIANNA:      'https://maps.app.goo.gl/onuFdoDm28WSqRbx5',
  BODEGUITA:     'https://www.google.com/maps/search/La+Bodeguita+Gualtallary+Alto+Mendoza',
  ACHAVAL:       'https://www.google.com/maps/search/Achaval+Ferrer+Winery+Mendoza',
  FINCA_BELLA:   'https://www.google.com/maps/search/Finca+Bella+Vista+Achaval+Ferrer+Perdriel+Mendoza',
  QUIMERA:       'https://www.google.com/maps/search/Quimera+Bistro+Mendoza',
  QUIMERA_WINERY:'https://www.google.com/maps/search/Quimera+Winery+Perdriel+Lujan+de+Cuyo+Mendoza',
  HUENTALA:      'https://www.google.com/maps/search/Huentala+Hotel+Primitivo+de+la+Reta+1007+Mendoza',
  MENDOZA_CITY:  'https://www.google.com/maps/search/Mendoza+City+Center+Plaza+Independencia+Argentina',
};
```

---

## 5. 작업 순서 (구현 체크리스트)

- [ ] **Step 1**: `argentina.html` 내 `MAPS` 객체 전체를 섹션 4의 내용으로 교체
- [ ] **Step 2**: `argentina.html` 내 `RAW_EVENTS` 배열 전체를 섹션 3의 내용으로 교체
- [ ] **Step 3**: `DATES` 배열 확인 — 5/1까지 포함되어 있는지 확인 (현재 5/3까지 있어 ✅)
- [ ] **Step 4**: 5/1 출발 이벤트 날짜가 `2026-05-01`로 정확한지 검증
- [ ] **Step 5**: 브라우저에서 열어서 각 날짜 컬럼의 이벤트 개수가 table.md와 일치하는지 육안 교차 검증

---

## 6. 누락 방지 원칙 (향후 AI 협업 시 지침)

1. **줄 번호 1:1 대조**: table.md의 각 `-` 항목에 RAW_EVENTS 항목이 정확히 하나씩 대응되는지 번호로 확인
2. **이동/픽업 이벤트도 반드시 포함**: "이동", "픽업", "복귀", "집합" 등 이동 동선도 생략 없이 넣기
3. **휴식 이벤트도 포함**: "휴식", "자유 시간" 등도 시각표에 표시하여 공백 없는 타임라인 구성
4. **날짜 교차 검증**: 각 일자별로 마지막 이벤트가 22:30 전후인지 확인
5. **URL 신규 장소 체크**: 새 장소가 등장하면 MAPS에 키 추가 후 이벤트에 연결 — 빈 URL 방치 금지
