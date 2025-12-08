# Vue.js 소개

## 주요 개념

### 1. Vue.js란?
- **프로그레시브 프레임워크**: 점진적으로 도입 가능
- **반응형 데이터 바인딩**: 데이터와 DOM 자동 동기화
- **컴포넌트 기반**: 재사용 가능한 UI 조각
- **선언적 렌더링**: HTML 템플릿으로 UI 선언

### 2. Vue 인스턴스
- **createApp()**: Vue 애플리케이션 생성
- **mount()**: DOM에 마운트
- **data()**: 반응형 데이터 정의
- **methods**: 메소드 정의

### 3. 템플릿 문법
- **보간법 (Interpolation)**: `{{ message }}`
- **디렉티브**: `v-bind`, `v-if`, `v-for`, `v-on` 등
- **단축 표기**: `:` (v-bind), `@` (v-on)

## 예시 코드

### Vue 기본 구조
```html
<!DOCTYPE html>
<html>
<head>
  <title>Vue App</title>
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
</head>
<body>
  <div id="app">
    <h1>{{ message }}</h1>
    <button @click="changeMessage">클릭</button>
  </div>

  <script>
    const { createApp } = Vue

    createApp({
      data() {
        return {
          message: '안녕하세요, Vue!'
        }
      },
      methods: {
        changeMessage() {
          this.message = '메시지가 변경되었습니다!'
        }
      }
    }).mount('#app')
  </script>
</body>
</html>
```

### 반응형 데이터
```javascript
const app = createApp({
  data() {
    return {
      count: 0,
      message: 'Hello',
      isVisible: true,
      items: ['Apple', 'Banana', 'Cherry']
    }
  },
  methods: {
    increment() {
      this.count++
    },
    toggle() {
      this.isVisible = !this.isVisible
    }
  }
})

app.mount('#app')
```

## 기본 코드 템플릿

### Vue 애플리케이션 기본
```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://unpkg.com/vue@3"></script>
</head>
<body>
  <div id="app">
    {{ message }}
  </div>

  <script>
    const { createApp } = Vue

    createApp({
      data() {
        return {
          message: 'Hello Vue!'
        }
      }
    }).mount('#app')
  </script>
</body>
</html>
```

## 연습 파일
- Vue 기본 인스턴스 생성
- 데이터 바인딩
- 메소드 정의
