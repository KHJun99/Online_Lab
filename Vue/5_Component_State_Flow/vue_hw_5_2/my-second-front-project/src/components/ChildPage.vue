<template>
  <div class="child-page">
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ name }}</p>
    <p>나이 : {{ age }}</p>
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
  }
})
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
</style>
