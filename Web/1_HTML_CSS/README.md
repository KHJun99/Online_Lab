# HTML & CSS 기초

## 주요 개념

### 1. HTML 기본 구조
- **DOCTYPE**: HTML 문서 타입 선언 `<!DOCTYPE html>`
- **html**: 최상위 요소
- **head**: 메타데이터, 스타일, 제목 등
- **body**: 화면에 표시될 내용

### 2. HTML 주요 태그
- **제목**: `<h1>` ~ `<h6>` (제목 레벨)
- **단락**: `<p>` (문단)
- **링크**: `<a href="">` (하이퍼링크)
- **구조**: `<header>`, `<div>`, `<dl>`, `<dt>`, `<dd>`
- **목록**: `<dl>` (정의 목록), `<dt>` (용어), `<dd>` (설명)

### 3. CSS 선택자
- **클래스 선택자**: `.class-name` (여러 요소에 적용)
- **ID 선택자**: `#id-name` (고유한 요소에 적용)
- **태그 선택자**: `h2`, `p` (모든 해당 태그에 적용)

### 4. CSS 주요 속성
- **텍스트 정렬**: `text-align: center/left/right`
- **배경색**: `background-color: #color`
- **크기**: `height`, `width`
- **여백**: `margin`, `padding`

## 예시 코드

### HTML 기본 구조
```html
<!DOCTYPE html>
<html>
<head>
  <title>The World Wide Web project</title>
  <style>
    .title {
      text-align: center;
      background-color: #c5c5c5;
      height: 120px;
      margin-bottom: 40px;
    }
    .text dt {
      margin: 0px;
      padding: 0px;
      text-align: left;
    }
    .text dd {
      margin: 0px;
      padding: 0px;
      text-align: left;
    }
  </style>
</head>
<body>
<header>
  <div class="title">
    <h1>World Wide Web</h1>
    <p>The WorldWideWeb (W3) is a wide-area <a href="">hypermedia</a> information retrieval initiative.</p>
  </div>
</header>
<h3>Everything there is online about W3</h3>
<p>Everything there is online about W3 is linked directly or indirectly to this document.</p>
<dl class="text">
  <dt><h3>What's out there?</h3></dt>
  <dd>Pointers to the world's online information, <a href="">subjects</a>, <a href="">W3 servers</a>, etc.</dd>
  <dt><h3>Help</h3></dt>
  <dd>On the browser you are using</dd>
</dl>
</body>
</html>
```

### CSS 선택자 예시
```css
/* 태그 선택자 */
h2 {
  color: blue;
  font-size: 24px;
}

p {
  line-height: 1.6;
  margin: 10px 0;
}

/* 클래스 선택자 */
.blue {
  color: blue;
}

.green {
  color: green;
}

/* ID 선택자 */
#red {
  color: red;
}
```

## 기본 코드 템플릿

### HTML 템플릿
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>페이지 제목</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>사이트 제목</h1>
    <nav>
      <a href="#home">홈</a>
      <a href="#about">소개</a>
    </nav>
  </header>

  <main>
    <section>
      <h2>섹션 제목</h2>
      <p>내용</p>
    </section>
  </main>

  <footer>
    <p>&copy; 2024</p>
  </footer>
</body>
</html>
```

### CSS 템플릿
```css
/* 전역 스타일 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* 바디 스타일 */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
}

/* 헤더 스타일 */
header {
  background-color: #f4f4f4;
  padding: 20px;
  text-align: center;
}

/* 클래스 스타일 */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

/* ID 스타일 */
#main-content {
  min-height: 500px;
}
```

## 연습 파일
- `web_ws_1_2/index.html`: HTML 기본 구조와 스타일
- `web_ws_1_3/`: HTML과 외부 CSS 파일 연결
