# JavaScript 참조 타입

## 주요 개념

### 1. 배열 메소드
- **forEach()**: 배열 순회
- **map()**: 새로운 배열 반환
- **filter()**: 조건에 맞는 요소만 필터링
- **reduce()**: 배열을 하나의 값으로 축소
- **find()**: 조건에 맞는 첫 번째 요소 반환
- **some()**: 하나라도 조건을 만족하면 true
- **every()**: 모두 조건을 만족하면 true

### 2. 화살표 함수
- **기본 형태**: `const func = (param) => { return value }`
- **단축 형태**: `const func = param => value`
- **매개변수 없음**: `const func = () => value`

### 3. 객체 메소드
- **Object.keys()**: 모든 키를 배열로 반환
- **Object.values()**: 모든 값을 배열로 반환
- **Object.entries()**: 키-값 쌍을 배열로 반환

## 예시 코드

### 배열 메소드 활용
```javascript
const numbers = [1, 2, 3, 4, 5]

// forEach - 순회
numbers.forEach((num) => {
  console.log(num)
})

// map - 변환
const doubled = numbers.map((num) => num * 2)
console.log(doubled)  // [2, 4, 6, 8, 10]

// filter - 필터링
const evens = numbers.filter((num) => num % 2 === 0)
console.log(evens)  // [2, 4]

// reduce - 축소
const sum = numbers.reduce((acc, num) => acc + num, 0)
console.log(sum)  // 15

// find - 찾기
const found = numbers.find((num) => num > 3)
console.log(found)  // 4

// some - 하나라도
const hasEven = numbers.some((num) => num % 2 === 0)
console.log(hasEven)  // true

// every - 모두
const allPositive = numbers.every((num) => num > 0)
console.log(allPositive)  // true
```

### 화살표 함수
```javascript
// 일반 함수
function add(a, b) {
  return a + b
}

// 화살표 함수
const add = (a, b) => {
  return a + b
}

// 화살표 함수 단축
const add = (a, b) => a + b

// 매개변수가 하나인 경우
const double = num => num * 2

// 매개변수가 없는 경우
const greet = () => 'Hello'

// 객체 반환 시 괄호 필요
const makePerson = (name) => ({ name: name })
```

### 객체 메소드
```javascript
const person = {
  name: '홍길동',
  age: 20,
  city: '서울'
}

// 모든 키
const keys = Object.keys(person)
console.log(keys)  // ['name', 'age', 'city']

// 모든 값
const values = Object.values(person)
console.log(values)  // ['홍길동', 20, '서울']

// 키-값 쌍
const entries = Object.entries(person)
console.log(entries)  // [['name', '홍길동'], ['age', 20], ['city', '서울']]

// entries로 순회
entries.forEach(([key, value]) => {
  console.log(`${key}: ${value}`)
})
```

## 기본 코드 템플릿

### 배열 메소드 체이닝
```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// 체이닝: 짝수만 필터링 후 제곱하여 합계
const result = numbers
  .filter(num => num % 2 === 0)
  .map(num => num ** 2)
  .reduce((acc, num) => acc + num, 0)

console.log(result)  // 220
```

### 객체 배열 처리
```javascript
const users = [
  { name: '홍길동', age: 20 },
  { name: '김철수', age: 25 },
  { name: '이영희', age: 30 }
]

// 이름만 추출
const names = users.map(user => user.name)
console.log(names)  // ['홍길동', '김철수', '이영희']

// 25세 이상만 필터링
const adults = users.filter(user => user.age >= 25)
console.log(adults)

// 나이 평균
const avgAge = users.reduce((acc, user) => acc + user.age, 0) / users.length
console.log(avgAge)  // 25
```

## 연습 파일
- 배열 메소드와 화살표 함수 활용
