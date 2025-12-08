# JavaScript 기본 문법

## 주요 개념

### 1. 변수 선언
- **let**: 재할당 가능한 변수
- **const**: 재할당 불가능한 상수
- **var**: 구버전 변수 선언 (권장하지 않음)

### 2. 데이터 타입
- **원시 타입**: String, Number, Boolean, null, undefined
- **참조 타입**: Object, Array, Function
- **typeof**: 타입 확인 연산자

### 3. 배열 (Array)
- **배열 선언**: `const arr = [1, 2, 3]`
- **인덱싱**: `arr[0]` (0부터 시작)
- **길이**: `arr.length`

### 4. 객체 (Object)
- **객체 선언**: `const obj = { key: 'value' }`
- **속성 접근**: `obj.key` 또는 `obj['key']`
- **속성 추가**: `obj.newKey = 'newValue'`

### 5. 콘솔 출력
- **console.log()**: 브라우저 콘솔에 출력
- **디버깅**: 변수 값 확인용

## 예시 코드

### 변수와 데이터 타입
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <script>
    // 1. 문자열 'Hello World'를 변수 greeting에 할당 (재할당 가능)
    let greeting = 'Hello World'

    // 2. greeting을 console에 출력
    console.log(greeting)

    // 3. greeting에 문자열 'Hello JS'를 할당
    greeting = 'Hello JS'

    // 4. 배열 생성
    const numbers = [1, 2, 3, 4, 5]

    // 5. numbers를 console에 출력
    console.log(numbers)

    // 6. 객체 생성
    const person = {
      name: '홍길동'
    }

    // 7. person을 console에 출력
    console.log(person)
  </script>
</body>
</html>
```

### 변수 선언 방식 비교
```javascript
// let - 재할당 가능
let age = 25
age = 26  // OK

// const - 재할당 불가능
const name = '홍길동'
// name = '김철수'  // Error!

// const 객체는 속성 변경 가능
const user = { name: '홍길동' }
user.name = '김철수'  // OK
user.age = 20        // OK
```

### 배열 기본 조작
```javascript
// 배열 생성
const fruits = ['apple', 'banana', 'cherry']

// 인덱스로 접근
console.log(fruits[0])  // 'apple'

// 배열 길이
console.log(fruits.length)  // 3

// 요소 추가
fruits.push('date')
console.log(fruits)  // ['apple', 'banana', 'cherry', 'date']

// 요소 제거
fruits.pop()
console.log(fruits)  // ['apple', 'banana', 'cherry']
```

### 객체 기본 조작
```javascript
// 객체 생성
const person = {
  name: '홍길동',
  age: 20,
  city: '서울'
}

// 속성 접근
console.log(person.name)     // '홍길동'
console.log(person['age'])   // 20

// 속성 추가
person.job = '개발자'
console.log(person.job)      // '개발자'

// 속성 수정
person.age = 21
console.log(person.age)      // 21
```

## 기본 코드 템플릿

### 기본 JavaScript 구조
```javascript
// 변수 선언
let variable1 = 'value'
const constant1 = 'value'

// 배열
const myArray = [1, 2, 3, 4, 5]
console.log(myArray[0])
console.log(myArray.length)

// 객체
const myObject = {
  property1: 'value1',
  property2: 'value2',
  method: function() {
    console.log('메소드 호출')
  }
}

console.log(myObject.property1)
myObject.method()

// 조건문
if (condition) {
  // 코드
} else {
  // 코드
}

// 반복문
for (let i = 0; i < myArray.length; i++) {
  console.log(myArray[i])
}

// forEach
myArray.forEach((item) => {
  console.log(item)
})
```

### 타입 확인
```javascript
console.log(typeof 'Hello')      // 'string'
console.log(typeof 123)          // 'number'
console.log(typeof true)         // 'boolean'
console.log(typeof [1, 2, 3])    // 'object'
console.log(typeof {a: 1})       // 'object'
console.log(typeof null)         // 'object' (특이 케이스)
console.log(typeof undefined)    // 'undefined'
```

## 연습 파일
- `javascript_ws_2_1/`: 변수 선언, 배열, 객체 기본
