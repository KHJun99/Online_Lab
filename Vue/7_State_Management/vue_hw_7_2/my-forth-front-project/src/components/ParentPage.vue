<template>
  <div class="parent-page">
    <div class="family-section">
      <h2>부모 컴포넌트</h2>
      <p>{{ family.father }}</p>
      <p>{{ family.mother }}</p>
    </div>

    <div class="children-section">
      <h2>자식 페이지</h2>
      <ChildPage
        v-for="(child, index) in family.children"
        :key="index"
        :child="child"
      />
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import ChildPage from './ChildPage.vue'

defineProps({
  family: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.parent-page {
  border: 2px solid #333;
  padding: 1.5rem;
  background-color: #f9f9f9;
  text-align: center;
}

.family-section {
  margin-bottom: 1.5rem;
}

.family-section h2 {
  font-size: 1.3rem;
  margin-bottom: 0.5rem;
}

.family-section p {
  margin: 0.3rem 0;
}

.children-section h2 {
  font-size: 1.3rem;
  margin-bottom: 1rem;
}
</style>
