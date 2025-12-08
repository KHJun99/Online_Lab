# Vue 기본 문법 (2)

## 주요 개념

### 1. v-for 리스트 렌더링
- **배열 순회**: `v-for="item in items"`
- **인덱스 사용**: `v-for="(item, index) in items"`
- **객체 순회**: `v-for="(value, key) in object"`
- **key 속성**: 각 요소의 고유 식별자 (필수)

### 2. v-model 양방향 바인딩
- **입력 필드**: `<input v-model="message">`
- **체크박스**: `<input type="checkbox" v-model="checked">`
- **라디오**: `<input type="radio" v-model="picked">`
- **셀렉트**: `<select v-model="selected">`

### 3. Computed 속성
- **계산된 속성**: 의존 데이터가 변경될 때만 재계산
- **캐싱**: 효율적인 성능
- **읽기 전용**: getter만 정의

### 4. Watch 속성
- **데이터 변화 감지**: 특정 데이터의 변화를 감지
- **비동기 작업**: API 호출 등에 유용

## 예시 코드

### v-for 리스트 렌더링
```html
<div id="app">
  <!-- 배열 순회 -->
  <ul>
    <li v-for="(item, index) in items" :key="item.id">
      {{ index }}: {{ item.name }}
    </li>
  </ul>

  <!-- 객체 순회 -->
  <div v-for="(value, key) in user" :key="key">
    {{ key }}: {{ value }}
  </div>

  <!-- 숫자 범위 -->
  <span v-for="n in 10" :key="n">{{ n }}</span>
</div>

<script>
createApp({
  data() {
    return {
      items: [
        { id: 1, name: 'Apple' },
        { id: 2, name: 'Banana' },
        { id: 3, name: 'Cherry' }
      ],
      user: {
        name: '홍길동',
        age: 20,
        city: '서울'
      }
    }
  }
}).mount('#app')
</script>
```

### v-model 양방향 바인딩
```html
<div id="app">
  <!-- 텍스트 입력 -->
  <input v-model="message" placeholder="메시지 입력">
  <p>{{ message }}</p>

  <!-- 체크박스 -->
  <input type="checkbox" v-model="checked" id="checkbox">
  <label for="checkbox">{{ checked }}</label>

  <!-- 여러 체크박스 -->
  <input type="checkbox" value="Apple" v-model="checkedFruits">
  <input type="checkbox" value="Banana" v-model="checkedFruits">
  <p>선택: {{ checkedFruits }}</p>

  <!-- 라디오 -->
  <input type="radio" value="A" v-model="picked">
  <input type="radio" value="B" v-model="picked">
  <p>선택: {{ picked }}</p>

  <!-- 셀렉트 -->
  <select v-model="selected">
    <option>A</option>
    <option>B</option>
    <option>C</option>
  </select>
  <p>선택: {{ selected }}</p>
</div>

<script>
createApp({
  data() {
    return {
      message: '',
      checked: false,
      checkedFruits: [],
      picked: '',
      selected: ''
    }
  }
}).mount('#app')
</script>
```

### Computed 속성
```html
<div id="app">
  <input v-model="firstName">
  <input v-model="lastName">
  <p>전체 이름: {{ fullName }}</p>

  <ul>
    <li v-for="item in filteredItems" :key="item.id">
      {{ item.name }}
    </li>
  </ul>
</div>

<script>
createApp({
  data() {
    return {
      firstName: '길동',
      lastName: '홍',
      items: [
        { id: 1, name: 'Apple', active: true },
        { id: 2, name: 'Banana', active: false },
        { id: 3, name: 'Cherry', active: true }
      ]
    }
  },
  computed: {
    fullName() {
      return this.lastName + this.firstName
    },
    filteredItems() {
      return this.items.filter(item => item.active)
    }
  }
}).mount('#app')
</script>
```

### Watch 속성
```html
<div id="app">
  <input v-model="question">
  <p>{{ answer }}</p>
</div>

<script>
createApp({
  data() {
    return {
      question: '',
      answer: '질문을 입력하세요'
    }
  },
  watch: {
    question(newQuestion) {
      if (newQuestion.includes('?')) {
        this.answer = '생각 중...'
        setTimeout(() => {
          this.answer = '답변입니다!'
        }, 1000)
      }
    }
  }
}).mount('#app')
</script>
```

## 기본 코드 템플릿

### 종합 예제
```html
<div id="app">
  <!-- v-for -->
  <ul>
    <li v-for="item in items" :key="item.id">
      {{ item.name }}
    </li>
  </ul>

  <!-- v-model -->
  <input v-model="newItem">
  <button @click="addItem">추가</button>

  <!-- computed -->
  <p>총 개수: {{ itemCount }}</p>
</div>

<script>
createApp({
  data() {
    return {
      items: [],
      newItem: ''
    }
  },
  computed: {
    itemCount() {
      return this.items.length
    }
  },
  methods: {
    addItem() {
      if (this.newItem) {
        this.items.push({
          id: Date.now(),
          name: this.newItem
        })
        this.newItem = ''
      }
    }
  },
  watch: {
    items(newItems) {
      console.log('아이템 변경:', newItems)
    }
  }
}).mount('#app')
</script>
```

## 연습 파일
- v-for 리스트 렌더링
- v-model 양방향 바인딩
- computed 계산된 속성
- watch 데이터 감지
