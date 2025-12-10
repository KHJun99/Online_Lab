<template>
  <div class="child-page">
    <h3>자식 페이지</h3>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

defineProps({
  child: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.child-page {
  border: 1px solid #999;
  padding: 1rem;
  margin-bottom: 0.5rem;
  background-color: white;
  text-align: center;
}

h3 {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

p {
  margin: 0;
}
</style>
