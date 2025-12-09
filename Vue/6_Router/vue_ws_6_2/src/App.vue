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
  </div>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}

.quiz-app {
  max-width: 800px;
  margin: 0 auto;
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
  margin-bottom: 20px;
}

.app-header {
  background: #ff9933;
  color: white;
  text-align: center;
  padding: 20px;
}

.app-header h1 {
  margin: 0;
  font-size: 28px;
}

.app-description {
  text-align: center;
  padding: 15px;
  color: #666;
}

.app-description p {
  margin: 0;
}

.app-nav {
  background: #333;
  color: white;
  text-align: center;
  padding: 12px;
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 0 15px;
  font-weight: 500;
}

.nav-link:hover {
  text-decoration: underline;
}
</style>
