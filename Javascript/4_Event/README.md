# JavaScript Event

## 주요 개념

### 1. 이벤트란?
- **사용자 동작**: 클릭, 입력, 마우스 이동 등
- **이벤트 리스너**: 이벤트 발생 시 실행될 함수
- **이벤트 핸들러**: 이벤트를 처리하는 함수

### 2. 이벤트 리스너 등록
- **addEventListener()**: 이벤트 리스너 추가
- **이벤트 타입**: 'click', 'submit', 'input', 'change' 등
- **콜백 함수**: 이벤트 발생 시 실행될 함수

### 3. 이벤트 객체
- **event.preventDefault()**: 기본 동작 막기
- **event.target**: 이벤트가 발생한 요소
- **event.currentTarget**: 이벤트 리스너가 등록된 요소

### 4. DOM 요소 생성
- **document.createElement()**: 새 요소 생성
- **appendChild()**: 자식 요소로 추가
- **textContent**: 텍스트 내용 설정

## 예시 코드

### Form Submit 이벤트와 카드 생성
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container">
    <form id="form" class="my-3">
      <div class="mb-3">
        <input type="text" class="form-control" id="title">
      </div>
      <div class="mb-3">
        <textarea class="form-control" id="content" rows="3"></textarea>
      </div>
      <div class="d-grid gap-2">
        <button class="btn btn-primary">add</button>
      </div>
    </form>

    <section id="cardsSection" class="row"></section>
  </div>

  <script>
    const form = document.querySelector('#form')
    const titleInput = document.querySelector('#title')
    const contentInput = document.querySelector('#content')
    const cardsSection = document.querySelector('#cardsSection')

    // createCard 함수: 카드를 생성
    function createCard(title, content) {
      const article = document.createElement('article')
      article.classList.add('col-4')

      const card = document.createElement('div')
      card.classList.add('card', 'm-1')

      const cardBody = document.createElement('div')
      cardBody.classList.add('card-body')

      const cardTitle = document.createElement('h5')
      cardTitle.classList.add('card-title')
      cardTitle.textContent = title

      const cardText = document.createElement('p')
      cardText.classList.add('card-text')
      cardText.textContent = content

      cardBody.appendChild(cardTitle)
      cardBody.appendChild(cardText)
      card.appendChild(cardBody)
      article.appendChild(card)

      return article
    }

    // submit 이벤트 리스너
    form.addEventListener('submit', (event) => {
      event.preventDefault()

      const title = titleInput.value
      const content = contentInput.value

      const newCard = createCard(title, content)
      cardsSection.appendChild(newCard)

      titleInput.value = ''
      contentInput.value = ''
    })
  </script>
</body>
</html>
```

### 다양한 이벤트 예시
```javascript
// 클릭 이벤트
const button = document.querySelector('#myButton')
button.addEventListener('click', () => {
  console.log('버튼 클릭!')
})

// 입력 이벤트
const input = document.querySelector('#myInput')
input.addEventListener('input', (event) => {
  console.log('입력값:', event.target.value)
})

// 변경 이벤트
const select = document.querySelector('#mySelect')
select.addEventListener('change', (event) => {
  console.log('선택값:', event.target.value)
})

// 마우스 이벤트
const box = document.querySelector('#myBox')
box.addEventListener('mouseenter', () => {
  console.log('마우스 진입')
})
box.addEventListener('mouseleave', () => {
  console.log('마우스 떠남')
})
```

## 기본 코드 템플릿

### 이벤트 리스너 기본
```html
<!DOCTYPE html>
<html>
<head>
  <title>Event Example</title>
</head>
<body>
  <button id="myButton">클릭</button>
  <input type="text" id="myInput">
  <div id="result"></div>

  <script>
    // 클릭 이벤트
    const button = document.querySelector('#myButton')
    button.addEventListener('click', (event) => {
      console.log('버튼 클릭됨')
      event.target.textContent = '클릭됨!'
    })

    // 입력 이벤트
    const input = document.querySelector('#myInput')
    const result = document.querySelector('#result')
    input.addEventListener('input', (event) => {
      result.textContent = event.target.value
    })
  </script>
</body>
</html>
```

### Form 처리 템플릿
```javascript
const form = document.querySelector('#myForm')

form.addEventListener('submit', (event) => {
  // 기본 동작(페이지 새로고침) 막기
  event.preventDefault()

  // 입력값 가져오기
  const inputValue = document.querySelector('#myInput').value

  // 데이터 처리
  console.log('입력값:', inputValue)

  // 입력 필드 초기화
  event.target.reset()
})
```

### 동적 요소 생성 템플릿
```javascript
function createElement(tag, className, text) {
  const element = document.createElement(tag)
  if (className) element.classList.add(className)
  if (text) element.textContent = text
  return element
}

// 사용 예시
const newDiv = createElement('div', 'container', 'Hello')
document.body.appendChild(newDiv)
```

## 연습 파일
- `javascript_ws_4_3/`: Form submit 이벤트와 동적 카드 생성
