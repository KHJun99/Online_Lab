<template>
  <div class="singer-detail">
    <div class="singer-card">
      <h2>가수 이름</h2>
      <div class="image-container">
        <img src="@/assets/singer.jpg" alt="Singer" class="singer-image">
      </div>
      <p class="singer-intro">가수 소개글</p>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.singer-detail {
  display: flex;
  justify-content: center;
  padding: 20px;
}

.singer-card {
  border: 1px solid #ddd;
  padding: 30px;
  max-width: 600px;
  text-align: center;
  background-color: #fff;
}

h2 {
  font-size: 2em;
  margin-bottom: 20px;
  color: #2c3e50;
}

.image-container {
  margin: 20px 0;
}

.singer-image {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  object-fit: cover;
}

.singer-intro {
  font-size: 1.1em;
  color: #666;
  margin-top: 20px;
}
</style>
