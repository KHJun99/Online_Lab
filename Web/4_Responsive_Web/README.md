# Responsive Web - 반응형 웹 디자인

## 주요 개념

### 1. 반응형 웹이란?
- **하나의 웹사이트**: 다양한 화면 크기에 자동 대응
- **유동적 레이아웃**: 화면 크기에 따라 요소 재배치
- **미디어 쿼리**: 조건에 따라 다른 스타일 적용
- **모바일 우선**: 모바일부터 디자인 시작

### 2. Bootstrap 반응형 기능
- **Grid System**: 12컬럼 기반 반응형 레이아웃
- **Breakpoints**: `sm`, `md`, `lg`, `xl`, `xxl`
- **Responsive Navbar**: 작은 화면에서 햄버거 메뉴로 전환
- **Utility Classes**: 화면 크기별 표시/숨김

### 3. Viewport 메타 태그
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```
- **width=device-width**: 기기 너비에 맞춤
- **initial-scale=1**: 초기 확대 비율 1

### 4. Bootstrap Breakpoints
- **xs**: < 576px (Extra small)
- **sm**: ≥ 576px (Small)
- **md**: ≥ 768px (Medium)
- **lg**: ≥ 992px (Large)
- **xl**: ≥ 1200px (Extra large)
- **xxl**: ≥ 1400px (Extra extra large)

## 예시 코드

### 반응형 Navbar
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <nav class="navbar navbar-expand-lg bg-primary">
      <div class="container-fluid">
        <a class="navbar-brand text-light" href="#">여행 블로그</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link active text-light" href="#">홈</a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-light" href="#">목적지</a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-light" href="#">여행 팁</a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-light" href="#">갤러리</a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-light" href="#">접속자 정보</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
```

### 반응형 Grid
```html
<div class="container">
  <div class="row">
    <!-- 모바일: 12컬럼(전체), 태블릿: 6컬럼(절반), 데스크톱: 4컬럼(1/3) -->
    <div class="col-12 col-md-6 col-lg-4">
      <div class="card">
        <div class="card-body">Card 1</div>
      </div>
    </div>
    <div class="col-12 col-md-6 col-lg-4">
      <div class="card">
        <div class="card-body">Card 2</div>
      </div>
    </div>
    <div class="col-12 col-md-6 col-lg-4">
      <div class="card">
        <div class="card-body">Card 3</div>
      </div>
    </div>
  </div>
</div>
```

### 미디어 쿼리 (CSS)
```css
/* 모바일 기본 스타일 */
.container {
  width: 100%;
  padding: 10px;
}

/* 태블릿 이상 */
@media (min-width: 768px) {
  .container {
    width: 750px;
    margin: 0 auto;
  }
}

/* 데스크톱 이상 */
@media (min-width: 992px) {
  .container {
    width: 970px;
  }
}

/* 큰 데스크톱 */
@media (min-width: 1200px) {
  .container {
    width: 1170px;
  }
}
```

## 기본 코드 템플릿

### 반응형 페이지 기본 구조
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>반응형 웹</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <!-- 반응형 네비게이션 -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <a class="navbar-brand" href="#">Logo</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="#">About</a></li>
          <li class="nav-item"><a class="nav-link" href="#">Contact</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- 반응형 컨텐츠 -->
  <div class="container mt-4">
    <div class="row">
      <div class="col-12 col-md-8">
        <h1>메인 컨텐츠</h1>
        <p>내용</p>
      </div>
      <div class="col-12 col-md-4">
        <h2>사이드바</h2>
        <p>추가 정보</p>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### 반응형 이미지
```html
<!-- Bootstrap 반응형 이미지 -->
<img src="image.jpg" class="img-fluid" alt="반응형 이미지">

<!-- CSS로 반응형 이미지 -->
<style>
  .responsive-img {
    max-width: 100%;
    height: auto;
  }
</style>
```

### Display 유틸리티 (화면 크기별 표시/숨김)
```html
<!-- 모바일에서만 표시 -->
<div class="d-block d-md-none">모바일 전용</div>

<!-- 태블릿 이상에서만 표시 -->
<div class="d-none d-md-block">태블릿/데스크톱 전용</div>

<!-- 데스크톱에서만 표시 -->
<div class="d-none d-lg-block">데스크톱 전용</div>
```

## 연습 파일
- `web_ws_4_a/`: 반응형 Navbar 구현
