# Bootstrap

## 주요 개념

### 1. Bootstrap 소개
- **CSS 프레임워크**: 미리 만들어진 CSS 클래스와 컴포넌트
- **반응형 디자인**: 다양한 화면 크기에 자동 대응
- **CDN 사용**: 별도 다운로드 없이 링크로 사용 가능

### 2. Bootstrap 설치
```html
<!-- CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- JavaScript Bundle -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
```

### 3. Bootstrap 주요 컴포넌트
- **Form Controls**: 입력 필드 스타일
- **Buttons**: 버튼 스타일
- **Grid System**: 반응형 레이아웃
- **Cards**: 카드 컴포넌트
- **Navbar**: 네비게이션 바

### 4. Bootstrap 유틸리티 클래스
- **Spacing**: `m-*` (margin), `p-*` (padding)
- **Text**: `text-center`, `text-primary`, `fw-bold`
- **Display**: `d-flex`, `d-none`, `d-block`
- **Colors**: `bg-primary`, `text-danger` 등

## 예시 코드

### Form 컴포넌트 (Floating Labels)
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .email-title {
            margin-top: 5px;
            margin-bottom: 4px;
            font-weight: 600;
        }
    </style>
  </head>
  <body>
    <div><p class="email-title">Email address</p></div>
    <div class="form-floating mb-3">
      <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">name@example.com</label>
    </div>

    <div><p class="email-title">Password</p></div>
    <div class="form-floating">
      <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword"></label>
    </div>

    <div>
        <p>비밀번호 구성은 8자리 이상, 영문 대소문자, 숫자, 특수문자를 사용하세요.</p>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
```

### Bootstrap 버튼
```html
<!-- 기본 버튼 -->
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>

<!-- 크기 변형 -->
<button type="button" class="btn btn-primary btn-lg">Large</button>
<button type="button" class="btn btn-primary btn-sm">Small</button>
```

### Grid System
```html
<div class="container">
  <div class="row">
    <div class="col-md-4">Column 1</div>
    <div class="col-md-4">Column 2</div>
    <div class="col-md-4">Column 3</div>
  </div>

  <div class="row">
    <div class="col-sm-6 col-md-3">Responsive Column</div>
    <div class="col-sm-6 col-md-9">Responsive Column</div>
  </div>
</div>
```

## 기본 코드 템플릿

### Bootstrap 기본 템플릿
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bootstrap Template</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <!-- 네비게이션 -->
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
    </div>
  </nav>

  <!-- 메인 컨텐츠 -->
  <div class="container mt-5">
    <div class="row">
      <div class="col-12">
        <h1>제목</h1>
        <p>내용</p>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### Bootstrap Card
```html
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
```

### Bootstrap Form
```html
<form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1">
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

## 연습 파일
- `web_ws_3_a/`: Bootstrap Form 컴포넌트
