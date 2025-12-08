<template>
  <ProductListItem
    v-for="product in products"
    :key="product.id"
    :product="product"
  />
</template>

<script setup>
import ProductListItem from './ProductListItem.vue'

defineProps({
  products: {
    type: Array,
    required: true
  }
})
</script>
