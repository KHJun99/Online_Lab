<template>
  <div>
    <Notice />
    <ProductList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Notice from '@/components/Notice.vue'
import { useProductStore } from '@/stores/product'

const store = useProductStore()

onMounted(() => {
  store.getProducts()
})
</script>

<style scoped>
</style>
