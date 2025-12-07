<template>
  <div class="singer-detail">
    <div class="singer-card">
      <h1>{{ singer.name }}</h1>
      <div class="image-container">
        <img src="@/assets/singer.jpg" alt="Singer" class="singer-image">
      </div>
      <p class="singer-intro">가수 소개글</p>
      <div class="albums-container">
        <SingerAlbum v-for="album in 2" :key="album" />
      </div>
    </div>
  </div>
</template>

<script setup>
import SingerAlbum from './SingerAlbum.vue'

defineProps({
  singer: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.singer-detail {
  display: inline-block;
  width: 46%;
  margin: 20px;
  vertical-align: top;
}

.singer-card {
  border: 1px solid #ddd;
  padding: 30px;
  text-align: center;
  background-color: #fff;
}

h1 {
  font-size: 2em;
  margin-bottom: 20px;
  color: #000;
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
  margin: 20px 0;
}

.albums-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 20px;
}
</style>
