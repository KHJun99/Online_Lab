# JavaScript 동기와 비동기

## 문제
JavaScript에서 동기, 비동기 등록의 차이점을 md 파일에 작성하여 제출하시오

## 요구사항
해당 사항 없음

---

## 동기(Synchronous)와 비동기(Asynchronous)의 차이점

### 1. 동기(Synchronous) 처리

**정의**: 작업을 순차적으로 실행하며, 하나의 작업이 완료될 때까지 다음 작업이 대기하는 방식

**특징**:
- 코드가 작성된 순서대로 실행됨
- 이전 작업이 완료되어야 다음 작업 실행
- 실행 흐름을 예측하기 쉬움
- 긴 작업이 있으면 전체 프로그램이 블로킹(blocking)됨

**예시**:
```javascript
console.log('첫 번째')
console.log('두 번째')
console.log('세 번째')

// 출력 순서:
// 첫 번째
// 두 번째
// 세 번째
```

**장점**:
- 코드의 흐름을 이해하기 쉬움
- 디버깅이 간단함
- 실행 순서가 명확함

**단점**:
- 시간이 오래 걸리는 작업이 있으면 전체 프로그램이 멈춤
- 사용자 경험이 저하될 수 있음
- 효율적이지 않음

---

### 2. 비동기(Asynchronous) 처리

**정의**: 작업을 시작하고 완료를 기다리지 않고 다음 작업을 실행하는 방식. 작업이 완료되면 콜백 함수 등을 통해 결과를 처리

**특징**:
- 작업이 완료되기를 기다리지 않고 다음 코드 실행
- 병렬적으로 여러 작업 처리 가능
- 시간이 오래 걸리는 작업(API 호출, 파일 읽기 등)에 적합
- 논블로킹(non-blocking) 방식

**예시**:
```javascript
console.log('첫 번째')

setTimeout(() => {
  console.log('두 번째')
}, 1000)

console.log('세 번째')

// 출력 순서:
// 첫 번째
// 세 번째
// 두 번째 (1초 후)
```

**비동기 처리 방법**:

1. **콜백 함수(Callback)**
```javascript
function getData(callback) {
  setTimeout(() => {
    callback('데이터')
  }, 1000)
}

getData((data) => {
  console.log(data)
})
```

2. **Promise**
```javascript
function getData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('데이터')
    }, 1000)
  })
}

getData()
  .then(data => console.log(data))
  .catch(error => console.error(error))
```

3. **async/await**
```javascript
async function fetchData() {
  try {
    const data = await getData()
    console.log(data)
  } catch (error) {
    console.error(error)
  }
}
```

**장점**:
- 긴 작업이 있어도 프로그램이 멈추지 않음
- 사용자 경험 향상
- 효율적인 리소스 사용
- 동시에 여러 작업 처리 가능

**단점**:
- 코드의 실행 순서를 예측하기 어려움
- 디버깅이 복잡함
- 콜백 지옥(Callback Hell) 발생 가능

---

### 3. 비교표

| 구분 | 동기(Synchronous) | 비동기(Asynchronous) |
|------|-------------------|----------------------|
| 실행 방식 | 순차적 실행 | 병렬적 실행 |
| 대기 | 작업 완료까지 대기 | 작업 완료를 기다리지 않음 |
| 블로킹 | 블로킹(Blocking) | 논블로킹(Non-blocking) |
| 예측 가능성 | 높음 | 낮음 |
| 사용 사례 | 간단한 연산, 순서가 중요한 작업 | API 호출, 파일 I/O, 타이머 |
| 성능 | 긴 작업 시 성능 저하 | 효율적 |

---

### 4. JavaScript에서 비동기가 필요한 이유

1. **Single Thread 언어**: JavaScript는 단일 스레드로 동작하므로, 동기적으로만 처리하면 긴 작업에서 UI가 멈춤
2. **사용자 경험**: 네트워크 요청이나 파일 읽기 등의 작업 중에도 사용자가 다른 작업을 할 수 있어야 함
3. **효율성**: 대기 시간 동안 다른 작업을 처리하여 전체적인 성능 향상

---

### 5. 실제 사용 예시

**동기 처리가 적합한 경우**:
- 간단한 계산
- 변수 할당
- 순서가 중요한 로직

**비동기 처리가 적합한 경우**:
- HTTP 요청 (fetch, axios 등)
- 파일 읽기/쓰기
- 타이머 (setTimeout, setInterval)
- 사용자 이벤트 처리
- 데이터베이스 쿼리
