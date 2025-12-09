<template>
  <div>
    <h1>router 연습하기</h1>
    <div>
      <RouterLink to="/">Some</RouterLink> |
      <RouterLink to="/other">Other</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
