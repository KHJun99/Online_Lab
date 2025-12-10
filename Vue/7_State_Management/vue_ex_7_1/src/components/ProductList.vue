<template>
  <div>
    <h1>Product List</h1>
    <ul>
      <li v-for="product in products" :key="product.id">
        {{ product.id }} - {{ product.title }} - {{ product.body }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'

const productStore = useProductStore()
const { products } = productStore
</script>

<style scoped>
</style>
