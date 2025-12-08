# CSS Layout

## 주요 개념

### 1. Position 속성
- **static**: 기본값, 일반적인 문서 흐름
- **relative**: 상대 위치 (원래 위치 기준)
- **absolute**: 절대 위치 (부모 요소 기준)
- **fixed**: 고정 위치 (뷰포트 기준, 스크롤해도 고정)
- **sticky**: 스크롤 시 고정

### 2. Flexbox
- **display: flex**: 플렉스 컨테이너 생성
- **justify-content**: 주축 정렬 (center, space-between, space-around 등)
- **align-items**: 교차축 정렬 (center, flex-start, flex-end 등)
- **flex-direction**: 주축 방향 (row, column)

### 3. Box Model
- **margin**: 외부 여백
- **padding**: 내부 여백
- **border**: 테두리
- **width/height**: 너비/높이
- **box-sizing**: 박스 크기 계산 방식

### 4. 기타 레이아웃 속성
- **border-radius**: 둥근 모서리
- **display**: 요소 표시 방식 (block, inline, flex, grid 등)
- **cursor**: 마우스 커서 모양

## 예시 코드

### Fixed Position - 우하단 TOP 버튼
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Business card</title>
  <style>
    .container {
      width: 80%;
      height: 1800px;
      background-color: #f2f2f2;
      border: 1px solid black;
      margin: 0 auto;
    }

    /* 고정/우하단/높이40px/둥근 테두리 */
    .top-btn {
      position: fixed;
      right: 20px;
      bottom: 20px;

      width: 40px;
      height: 40px;
      border-radius: 50%;  /* 완전한 원형 */

      display: flex;        /* 내부 텍스트 중앙 정렬 */
      align-items: center;
      justify-content: center;

      border: 1px solid #ccc;
      background: #fff;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="container"></div>
  <button class="top-btn" aria-label="맨 위로">TOP</button>
</body>
</html>
```

### Flexbox 중앙 정렬
```css
.flex-container {
  display: flex;
  justify-content: center;  /* 가로 중앙 */
  align-items: center;      /* 세로 중앙 */
  height: 100vh;
}

.flex-item {
  width: 200px;
  height: 200px;
  background-color: lightblue;
}
```

### Position 예시
```css
/* Relative */
.relative-box {
  position: relative;
  top: 10px;
  left: 20px;
}

/* Absolute */
.parent {
  position: relative;
}

.absolute-box {
  position: absolute;
  top: 0;
  right: 0;
}

/* Fixed */
.fixed-header {
  position: fixed;
  top: 0;
  width: 100%;
  background: white;
  z-index: 100;
}
```

## 기본 코드 템플릿

### Flexbox 레이아웃
```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px;
    }

    .item {
      flex: 1;
      margin: 10px;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="item">Item 1</div>
    <div class="item">Item 2</div>
    <div class="item">Item 3</div>
  </div>
</body>
</html>
```

### Position 레이아웃
```css
/* 상단 고정 네비게이션 */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: #333;
  z-index: 1000;
}

/* 하단 고정 버튼 */
.scroll-top {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

/* 중앙 배치 */
.center-box {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

## 연습 파일
- `web_ws_2_a/`: Fixed position TOP 버튼
