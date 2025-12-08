<template>
  <div class="card-detail">
    <h3>이름 : {{ name }}</h3>
    <p>직함 : {{ title }}</p>
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
}
</style>
