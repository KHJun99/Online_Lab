<template>
  <div class="main-page">
    <h1>router 연습하기</h1>
    <nav>
      <RouterLink to="/">Some</RouterLink> |
      <RouterLink to="/other">Other</RouterLink> |
      <RouterLink to="/students">Students</RouterLink>
    </nav>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.main-page {
  margin-bottom: 20px;
}

.main-page h1 {
  font-size: 32px;
  margin-bottom: 15px;
}

.main-page nav {
  font-size: 16px;
}

.main-page nav a {
  color: #0066cc;
  text-decoration: none;
  margin: 0 5px;
}

.main-page nav a:hover {
  text-decoration: underline;
}
</style>
