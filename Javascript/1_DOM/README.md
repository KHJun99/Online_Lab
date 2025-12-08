# DOM (Document Object Model)

## 주요 개념

### 1. DOM이란?
- **문서 객체 모델**: HTML 문서를 객체로 표현
- **트리 구조**: 요소들이 계층적으로 구성
- **JavaScript로 조작**: 동적으로 HTML 수정 가능

### 2. DOM 선택자
- **querySelector()**: CSS 선택자로 단일 요소 선택
- **querySelectorAll()**: CSS 선택자로 모든 요소 선택
- **getElementById()**: ID로 요소 선택
- **getElementsByClassName()**: 클래스로 요소들 선택

### 3. DOM 조작
- **textContent**: 텍스트 내용 변경
- **innerHTML**: HTML 내용 변경
- **classList**: 클래스 추가/제거/토글
  - `add()`: 클래스 추가
  - `remove()`: 클래스 제거
  - `toggle()`: 클래스 토글

### 4. DOM 요소 제거
- **remove()**: 요소 삭제
- **removeChild()**: 자식 요소 삭제

## 예시 코드

### DOM 선택과 조작
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <h1>오늘 할 일</h1>
  <hr>
  <ul>
    <li>수업 복습 하기</li>
    <li>실습 문제 풀기</li>
    <li>스터디 참여하기</li>
    <li>1 일 1 커밋하기</li>
    <li id="game">게임 하기</li>
  </ul>
  <script>
    // 1. h1 태그의 텍스트 콘텐츠를 '오늘 공부 목록'으로 변경
    const title = document.querySelector('h1')
    title.textContent = '오늘 공부 목록'

    // 2. li 태그를 선택하여 studyList 변수에 할당
    const studyList = document.querySelectorAll('li')

    // 3. li 태그에 study class를 추가
    studyList.forEach(li => {
      li.classList.add('study')
    })

    // 4. li 태그의 자식 요소 중 id가 game인 요소를 삭제
    const itemGame = document.querySelector('#game')
    itemGame.remove()
  </script>
</body>
</html>
```

### 다양한 DOM 선택 방법
```javascript
// ID로 선택
const element1 = document.getElementById('myId')

// 클래스로 선택 (단일)
const element2 = document.querySelector('.myClass')

// 클래스로 선택 (모두)
const elements = document.querySelectorAll('.myClass')

// 태그로 선택
const paragraphs = document.querySelectorAll('p')

// 복합 선택자
const special = document.querySelector('div.container > p.highlight')
```

### classList 메소드
```javascript
const element = document.querySelector('#myElement')

// 클래스 추가
element.classList.add('active')

// 클래스 제거
element.classList.remove('hidden')

// 클래스 토글 (있으면 제거, 없으면 추가)
element.classList.toggle('visible')

// 클래스 포함 여부 확인
if (element.classList.contains('active')) {
  console.log('활성 상태입니다')
}
```

## 기본 코드 템플릿

### DOM 조작 기본
```html
<!DOCTYPE html>
<html>
<head>
  <title>DOM 조작</title>
</head>
<body>
  <div id="container">
    <h1 class="title">제목</h1>
    <p class="content">내용</p>
  </div>

  <script>
    // 요소 선택
    const container = document.querySelector('#container')
    const title = document.querySelector('.title')
    const content = document.querySelector('.content')

    // 텍스트 변경
    title.textContent = '새로운 제목'
    content.textContent = '새로운 내용'

    // HTML 변경
    container.innerHTML = '<h2>완전히 새로운 내용</h2>'

    // 클래스 조작
    title.classList.add('highlight')
    content.classList.remove('old-style')

    // 스타일 직접 변경
    title.style.color = 'blue'
    title.style.fontSize = '24px'

    // 요소 제거
    const removeTarget = document.querySelector('#removeMe')
    if (removeTarget) {
      removeTarget.remove()
    }
  </script>
</body>
</html>
```

## 연습 파일
- `javascript_ws_1_2/`: DOM 선택과 조작, 클래스 추가, 요소 제거
