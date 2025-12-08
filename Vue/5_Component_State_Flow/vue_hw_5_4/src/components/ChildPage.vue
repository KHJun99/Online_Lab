<template>
  <div class="child-page">
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ name }}</p>
    <p>나이 : {{ age }}</p>
    <p>총돈 : {{ balance }}</p>
    <button @click="giveMeAllowance">용돈 주세요</button>
  </div>
</template>

<script setup>
defineProps({
  name: {
    type: String,
    required: true
  },
  age: {
    type: Number,
    required: true
  },
  balance: {
    type: Number,
    required: true
  }
})

const emit = defineEmits(['give-allowance'])

const giveMeAllowance = () => {
  emit('give-allowance')
}
</script>

<style scoped>
.child-page {
  padding: 1.5rem;
  border: 1px solid #999;
  background-color: #f9f9f9;
  border-radius: 4px;
}

.child-page h3 {
  font-size: 1.3rem;
  margin-bottom: 1rem;
  color: #555;
}

.child-page p {
  font-size: 1rem;
  color: #666;
  margin: 0.5rem 0;
}

button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background-color: #1e90ff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
}

button:hover {
  background-color: #1c7ed6;
}
</style>
