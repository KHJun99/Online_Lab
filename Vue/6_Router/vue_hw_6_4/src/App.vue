<template>
  <div>
    <MainPage />
    <RouterView />
  </div>
</template>

<script setup>
import MainPage from './components/MainPage.vue'
import { RouterView } from 'vue-router'
</script>

<style scoped>
</style>
