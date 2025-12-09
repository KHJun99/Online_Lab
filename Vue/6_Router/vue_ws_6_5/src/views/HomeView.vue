<template>
  <div class="home-view">
    <div class="welcome-section">
      <h2>퀴즈 앱에 오신 것을 환영합니다!</h2>
      <p>다양한 퀴즈를 풀고 여러분의 지식을 테스트해보세요.</p>
      <p>상단 메뉴에서 Quiz를 선택하여 시작하세요.</p>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.home-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 0;
}

.welcome-section {
  background: white;
  padding: 20px 40px 60px 40px;
  border-radius: 0;
  text-align: center;
  box-shadow: none;
  margin: 0;
}

.welcome-section h2 {
  color: #333;
  margin-bottom: 20px;
  font-size: 28px;
}

.welcome-section p {
  color: #666;
  font-size: 16px;
  line-height: 1.8;
  margin: 10px 0;
}
</style>
