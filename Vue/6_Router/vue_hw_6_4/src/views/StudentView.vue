<template>
  <div class="student-view">
    <h2>학생 상세 정보 목록 입니다.</h2>
    <div class="student-links">
      <RouterLink :to="{ name: 'student-detail', params: { name: '김하나' } }">
        김하나 학생 정보 보기
      </RouterLink>
      <RouterLink :to="{ name: 'student-detail', params: { name: '김두리' } }">
        김두리 학생 정보 보기
      </RouterLink>
      <RouterLink :to="{ name: 'student-detail', params: { name: '김서이' } }">
        김서이 학생 정보 보기
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.student-view {
  padding: 20px;
}

.student-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 20px;
}

.student-links a {
  color: #0066cc;
  text-decoration: none;
}

.student-links a:hover {
  text-decoration: underline;
}
</style>
