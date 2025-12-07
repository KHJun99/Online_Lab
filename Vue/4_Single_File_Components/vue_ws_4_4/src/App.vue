<script setup>
import MainPage from './components/MainPage.vue'
import SingerList from './components/SingerList.vue'
</script>

<template>
  <div id="app">
    <MainPage />
    <SingerList />
  </div>
</template>

<style scoped>
#app {
  width: 100%;
  min-height: 100vh;
  background-color: #f5f5f5;
}
</style>
