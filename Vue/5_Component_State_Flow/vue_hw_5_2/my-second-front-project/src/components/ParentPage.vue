<template>
  <div class="parent-page">
    <h2>부모 페이지입니다.</h2>
    <div class="children-container">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.parent-page {
  padding: 2rem;
  border: 2px solid #333;
  margin: 1rem;
}

.parent-page h2 {
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
  color: #333;
}

.children-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>
