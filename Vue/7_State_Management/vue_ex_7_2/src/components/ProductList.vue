<template>
  <div>
    <h1>Product List</h1>
    <ul>
      <li v-for="product in store.products" :key="product.id">
        {{ product.id }} - {{ product.title }} - {{ product.body }}
        <button @click="store.deleteProduct(product.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'

const store = useProductStore()
</script>
