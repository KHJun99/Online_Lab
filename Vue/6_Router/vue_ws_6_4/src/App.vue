<template>
  <div class="quiz-app">
    <div class="app-header">
      <h1>Quiz 퀴즈</h1>
    </div>
    <div class="app-description">
      <p>여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>
    </div>
    <nav class="app-nav">
      <RouterLink to="/" class="nav-link">Home</RouterLink> |
      <RouterLink to="/quiz" class="nav-link">Quiz</RouterLink>
    </nav>

    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>
.quiz-app {
  min-height: 100vh;
  background-color: #f5f5f5;
}

.app-header {
  background-color: #ff9800;
  color: white;
  text-align: center;
  padding: 30px 20px;
  margin: 0;
}

.app-header h1 {
  margin: 0;
  font-size: 32px;
  font-weight: bold;
}

.app-description {
  background-color: white;
  text-align: center;
  padding: 20px;
  border-bottom: 1px solid #ddd;
}

.app-description p {
  margin: 0;
  color: #666;
  font-size: 16px;
  line-height: 1.6;
}

.app-nav {
  background-color: #333;
  padding: 15px 20px;
  text-align: center;
}

.nav-link {
  color: white;
  text-decoration: none;
  margin: 0 10px;
  font-size: 16px;
}

.nav-link:hover {
  color: #ff9800;
}
</style>
