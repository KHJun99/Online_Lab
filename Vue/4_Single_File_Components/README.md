# Single File Components (SFC) - 단일 파일 컴포넌트

## 주요 개념

### 1. SFC란?
- **.vue 파일**: 하나의 파일에 template, script, style 포함
- **컴포넌트 단위**: 재사용 가능한 독립적인 UI 조각
- **빌드 도구**: Vite, Webpack 등 필요

### 2. SFC 구조
```vue
<template>
  <!-- HTML 템플릿 -->
</template>

<script>
export default {
  // JavaScript 로직
}
</script>

<style>
/* CSS 스타일 */
</style>
```

### 3. 컴포넌트 통신
- **Props**: 부모 → 자식 데이터 전달
- **Emit**: 자식 → 부모 이벤트 전달
- **defineProps()**: Props 정의 (Composition API)
- **defineEmits()**: Emit 정의 (Composition API)

### 4. Vue 프로젝트 생성
```bash
npm create vue@latest
cd project-name
npm install
npm run dev
```

## 예시 코드

### 기본 컴포넌트 구조
```vue
<!-- MyComponent.vue -->
<template>
  <div class="my-component">
    <h2>{{ title }}</h2>
    <p>{{ message }}</p>
    <button @click="handleClick">클릭</button>
  </div>
</template>

<script>
export default {
  name: 'MyComponent',
  data() {
    return {
      title: '컴포넌트 제목',
      message: '컴포넌트 메시지'
    }
  },
  methods: {
    handleClick() {
      console.log('버튼 클릭됨')
    }
  }
}
</script>

<style scoped>
.my-component {
  padding: 20px;
  border: 1px solid #ccc;
}

h2 {
  color: blue;
}
</style>
```

### Props 사용
```vue
<!-- ChildComponent.vue -->
<template>
  <div>
    <h3>{{ title }}</h3>
    <p>{{ content }}</p>
  </div>
</template>

<script>
export default {
  name: 'ChildComponent',
  props: {
    title: {
      type: String,
      required: true
    },
    content: {
      type: String,
      default: '기본 내용'
    }
  }
}
</script>
```

### 부모 컴포넌트에서 Props 전달
```vue
<!-- App.vue -->
<template>
  <div id="app">
    <ChildComponent
      title="자식 컴포넌트"
      content="부모에서 전달한 내용"
    />
  </div>
</template>

<script>
import ChildComponent from './components/ChildComponent.vue'

export default {
  name: 'App',
  components: {
    ChildComponent
  }
}
</script>
```

### Emit 사용
```vue
<!-- ChildComponent.vue -->
<template>
  <button @click="sendMessage">메시지 전송</button>
</template>

<script>
export default {
  emits: ['message-sent'],
  methods: {
    sendMessage() {
      this.$emit('message-sent', '자식에서 보낸 메시지')
    }
  }
}
</script>
```

### 부모에서 Emit 받기
```vue
<!-- App.vue -->
<template>
  <div>
    <ChildComponent @message-sent="handleMessage" />
    <p>{{ receivedMessage }}</p>
  </div>
</template>

<script>
import ChildComponent from './components/ChildComponent.vue'

export default {
  components: {
    ChildComponent
  },
  data() {
    return {
      receivedMessage: ''
    }
  },
  methods: {
    handleMessage(message) {
      this.receivedMessage = message
    }
  }
}
</script>
```

### Composition API (script setup)
```vue
<template>
  <div>
    <h1>{{ count }}</h1>
    <button @click="increment">증가</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const count = ref(0)

function increment() {
  count.value++
}
</script>

<style scoped>
button {
  padding: 10px 20px;
  font-size: 16px;
}
</style>
```

## 기본 코드 템플릿

### 프로젝트 구조
```
vue-project/
├── src/
│   ├── components/
│   │   └── MyComponent.vue
│   ├── App.vue
│   └── main.js
├── index.html
├── package.json
└── vite.config.js
```

### main.js
```javascript
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```

### App.vue
```vue
<template>
  <div id="app">
    <MyComponent msg="Hello Vue!" />
  </div>
</template>

<script>
import MyComponent from './components/MyComponent.vue'

export default {
  name: 'App',
  components: {
    MyComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

### 컴포넌트 템플릿
```vue
<template>
  <div class="component">
    <!-- 템플릿 내용 -->
  </div>
</template>

<script>
export default {
  name: 'ComponentName',
  props: {},
  data() {
    return {}
  },
  computed: {},
  methods: {},
  mounted() {}
}
</script>

<style scoped>
/* 컴포넌트 스타일 */
</style>
```

## 연습 파일
- SFC 기본 구조
- Props와 Emit 사용
- 컴포넌트 통신
