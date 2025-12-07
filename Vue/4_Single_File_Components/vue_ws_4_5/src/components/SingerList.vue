<template>
  <div class="singer-list">
    <div class="singers-grid">
      <SingerDetail
        v-for="singer in singers"
        :key="singer.name"
        :singer="singer"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import SingerDetail from './singers/SingerDetail.vue'

const singers = ref([
  { name: 'adele' },
  { name: 'maroon 5' },
  { name: 'Dua Lipa' }
])
</script>

<style scoped>
.singer-list {
  padding: 40px 20px;
}

.singers-grid {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-wrap: wrap;
  margin-bottom: 40px;
}

.single-singer {
  display: flex;
  justify-content: center;
  margin-top: 40px;
}

.singer-card {
  border: 1px solid #ddd;
  padding: 30px;
  text-align: center;
  background-color: #fff;
  max-width: 500px;
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
