<template>
  <div class="business-card">
    <BusinessCardDetail :name="name" :title="title" />
  </div>
</template>

<script setup>
import BusinessCardDetail from './businessCardDetail.vue'

defineProps({
  name: {
    type: String,
    required: true
  },
  title: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.business-card {
  border: 1px solid #ddd;
  padding: 2rem;
  margin: 1rem;
  border-radius: 8px;
  background-color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  min-width: 300px;
  text-align: center;
}
</style>
