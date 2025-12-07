<template>
  <div class="singer-list">
    <h1 class="title">가수 목록</h1>
    <SingerDetail />
  </div>
</template>

<script setup>
import SingerDetail from './singers/SingerDetail.vue'
</script>

<style scoped>
.singer-list {
  padding: 40px 20px;
}

.title {
  text-align: center;
  font-size: 2.5em;
  color: #2c3e50;
  margin-bottom: 40px;
}
</style>
