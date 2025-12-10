<template>
  <div class="main-page">
    <h1>pinia 연습하기</h1>
    <div class="family-list">
      <ParentPage
        v-for="(family, index) in store.familyInfo"
        :key="index"
        :family="family"
      />
    </div>
  </div>
</template>

<script setup>
import ParentPage from './ParentPage.vue'
import { useFamilyStore } from '@/stores/family'

const store = useFamilyStore()
</script>

<style scoped>
.main-page {
  padding: 2rem;
  text-align: center;
}

h1 {
  font-size: 2rem;
  margin-bottom: 2rem;
}

.family-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
</style>
