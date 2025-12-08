# Vue 기본 문법 (1)

## 주요 개념

### 1. 디렉티브 (Directives)
- **v-bind**: 속성 바인딩 (단축: `:`)
- **v-on**: 이벤트 리스너 (단축: `@`)
- **v-if**: 조건부 렌더링
- **v-show**: 조건부 표시 (display 속성 변경)
- **v-for**: 리스트 렌더링

### 2. v-bind
```html
<!-- 속성 바인딩 -->
<img v-bind:src="imageUrl">
<img :src="imageUrl">  <!-- 단축 표기 -->

<!-- 클래스 바인딩 -->
<div :class="{ active: isActive }"></div>
<div :class="[class1, class2]"></div>

<!-- 스타일 바인딩 -->
<div :style="{ color: textColor, fontSize: size }"></div>
```

### 3. v-on
```html
<!-- 이벤트 리스너 -->
<button v-on:click="handleClick">클릭</button>
<button @click="handleClick">클릭</button>  <!-- 단축 표기 -->

<!-- 이벤트 수식어 -->
<form @submit.prevent="onSubmit"></form>
<button @click.stop="onClick"></button>
```

### 4. v-if vs v-show
- **v-if**: 조건이 false면 렌더링하지 않음
- **v-show**: 조건이 false면 display: none

## 예시 코드

### v-bind 활용
```html
<div id="app">
  <img :src="imageUrl" :alt="imageAlt">

  <div :class="{ active: isActive, 'text-danger': hasError }">
    클래스 바인딩
  </div>

  <div :style="{ color: activeColor, fontSize: fontSize + 'px' }">
    스타일 바인딩
  </div>
</div>

<script>
const { createApp } = Vue

createApp({
  data() {
    return {
      imageUrl: 'image.jpg',
      imageAlt: '이미지 설명',
      isActive: true,
      hasError: false,
      activeColor: 'blue',
      fontSize: 20
    }
  }
}).mount('#app')
</script>
```

### v-on 이벤트 처리
```html
<div id="app">
  <p>{{ count }}</p>
  <button @click="increment">증가</button>
  <button @click="count--">감소</button>

  <input @input="handleInput" :value="message">
  <p>{{ message }}</p>

  <form @submit.prevent="onSubmit">
    <input v-model="text">
    <button type="submit">제출</button>
  </form>
</div>

<script>
createApp({
  data() {
    return {
      count: 0,
      message: '',
      text: ''
    }
  },
  methods: {
    increment() {
      this.count++
    },
    handleInput(event) {
      this.message = event.target.value
    },
    onSubmit() {
      console.log('제출:', this.text)
    }
  }
}).mount('#app')
</script>
```

### v-if 조건부 렌더링
```html
<div id="app">
  <button @click="toggle">토글</button>

  <p v-if="isVisible">보입니다!</p>
  <p v-else>숨겨졌습니다!</p>

  <div v-if="type === 'A'">A</div>
  <div v-else-if="type === 'B'">B</div>
  <div v-else>C</div>
</div>

<script>
createApp({
  data() {
    return {
      isVisible: true,
      type: 'A'
    }
  },
  methods: {
    toggle() {
      this.isVisible = !this.isVisible
    }
  }
}).mount('#app')
</script>
```

## 기본 코드 템플릿

### 디렉티브 종합
```html
<div id="app">
  <!-- v-bind -->
  <img :src="imageUrl">
  <div :class="{ active: isActive }">클래스 바인딩</div>

  <!-- v-on -->
  <button @click="handleClick">클릭</button>
  <input @input="handleInput">

  <!-- v-if -->
  <p v-if="show">조건부 렌더링</p>

  <!-- v-show -->
  <p v-show="show">조건부 표시</p>
</div>

<script>
createApp({
  data() {
    return {
      imageUrl: '',
      isActive: true,
      show: true
    }
  },
  methods: {
    handleClick() {
      console.log('클릭됨')
    },
    handleInput(event) {
      console.log(event.target.value)
    }
  }
}).mount('#app')
</script>
```

## 연습 파일
- v-bind 속성 바인딩
- v-on 이벤트 처리
- v-if 조건부 렌더링
