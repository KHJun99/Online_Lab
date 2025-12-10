<script setup>
import NavigationBar from '@/components/NavigationBar.vue'
</script>

<template>
  <div id="app">
    <NavigationBar />
    <router-view />
  </div>
</template>

<style scoped>
#app {
  font-family: Arial, sans-serif;
}
</style>
