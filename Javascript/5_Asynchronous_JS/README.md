# Asynchronous JavaScript - 비동기 JavaScript

## 주요 개념

### 1. 동기 vs 비동기
- **동기(Synchronous)**: 코드가 순차적으로 실행
- **비동기(Asynchronous)**: 코드가 동시에 실행될 수 있음
- **블로킹 vs 논블로킹**: 대기 여부

### 2. Promise
- **Promise 객체**: 비동기 작업의 결과를 나타내는 객체
- **상태**: pending, fulfilled, rejected
- **then()**: 성공 시 실행
- **catch()**: 실패 시 실행
- **finally()**: 항상 실행

### 3. async/await
- **async 함수**: 항상 Promise를 반환
- **await**: Promise가 완료될 때까지 대기
- **try-catch**: 에러 처리

### 4. Fetch API
- **fetch()**: HTTP 요청 보내기
- **response.json()**: JSON 응답 파싱
- **AJAX**: 페이지 새로고침 없이 데이터 요청

## 예시 코드

### Promise 기본
```javascript
// Promise 생성
const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    const success = true
    if (success) {
      resolve('성공!')
    } else {
      reject('실패!')
    }
  }, 1000)
})

// Promise 사용
myPromise
  .then(result => {
    console.log(result)  // '성공!'
  })
  .catch(error => {
    console.error(error)
  })
  .finally(() => {
    console.log('완료')
  })
```

### async/await
```javascript
// async 함수 정의
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data')
    const data = await response.json()
    console.log(data)
    return data
  } catch (error) {
    console.error('에러 발생:', error)
  }
}

// async 함수 호출
fetchData()
```

### Fetch API 사용
```javascript
// GET 요청
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => response.json())
  .then(data => {
    console.log(data)
  })
  .catch(error => {
    console.error('에러:', error)
  })

// POST 요청
fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    title: '제목',
    body: '내용',
    userId: 1
  })
})
  .then(response => response.json())
  .then(data => {
    console.log('생성됨:', data)
  })
```

### 여러 Promise 동시 처리
```javascript
// Promise.all - 모두 완료될 때까지 대기
const promise1 = fetch('https://api.example.com/data1')
const promise2 = fetch('https://api.example.com/data2')
const promise3 = fetch('https://api.example.com/data3')

Promise.all([promise1, promise2, promise3])
  .then(responses => {
    return Promise.all(responses.map(r => r.json()))
  })
  .then(data => {
    console.log('모든 데이터:', data)
  })

// Promise.race - 가장 빠른 것 하나만
Promise.race([promise1, promise2, promise3])
  .then(response => response.json())
  .then(data => {
    console.log('가장 빠른 데이터:', data)
  })
```

## 기본 코드 템플릿

### async/await 패턴
```javascript
// 데이터 가져오기
async function getData() {
  try {
    const response = await fetch('API_URL')
    if (!response.ok) {
      throw new Error('HTTP 에러: ' + response.status)
    }
    const data = await response.json()
    return data
  } catch (error) {
    console.error('에러 발생:', error)
    throw error
  }
}

// 사용
async function main() {
  try {
    const data = await getData()
    console.log(data)
  } catch (error) {
    console.error('메인 에러:', error)
  }
}

main()
```

### API 요청 함수
```javascript
// GET 요청
async function get(url) {
  const response = await fetch(url)
  return await response.json()
}

// POST 요청
async function post(url, data) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  })
  return await response.json()
}

// 사용
const users = await get('https://api.example.com/users')
const newUser = await post('https://api.example.com/users', {
  name: '홍길동',
  email: 'hong@example.com'
})
```

### setTimeout을 Promise로
```javascript
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

// 사용
async function example() {
  console.log('시작')
  await delay(2000)
  console.log('2초 후')
}
```

## 연습 파일
- Promise, async/await, Fetch API 활용
