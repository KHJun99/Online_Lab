<template>
  <div class="singer-list">
    <h1 class="title">가수 목록</h1>
    <div class="card-container">
      <SingerDetail />
      <SingerDetail />
    </div>
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
  color: orangered;
  margin-bottom: 40px;
}

.card-container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-wrap: wrap;
}
</style>
