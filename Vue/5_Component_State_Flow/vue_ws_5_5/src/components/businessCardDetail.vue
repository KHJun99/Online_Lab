<template>
  <div class="card-detail">
    <h3>이름 : {{ name }}</h3>
    <p>직함 : {{ title }}</p>
    <button @click="$emit('delete-card')">명함 삭제</button>
  </div>
</template>

<script setup>
defineProps({
  name: {
    type: String,
    required: true
  },
  title: {
    type: String,
    required: true
  }
})

defineEmits(['delete-card'])
</script>

<style scoped>
.card-detail h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  color: #333;
}

.card-detail p {
  font-size: 1rem;
  color: #666;
  margin-bottom: 1rem;
}

button {
  padding: 0.5rem 1rem;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
}

button:hover {
  background-color: #f5f5f5;
}
</style>
