<template>
  <div class="main-page">
    <h1>가수 정보 페이지에 오신 것을 환영합니다</h1>
    <p class="subtitle">여러분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요.</p>
    <div class="image-container">
      <img src="@/assets/microphone.jpg" alt="Microphone" class="microphone-image">
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.main-page {
  text-align: center;
  padding: 40px 20px;
}

h1 {
  font-size: 2.5em;
  color: #2c3e50;
  margin-bottom: 20px;
}

.subtitle {
  font-size: 1.2em;
  color: #666;
  margin-bottom: 40px;
}

.image-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.microphone-image {
  max-width: 200px;
  height: auto;
}
</style>
