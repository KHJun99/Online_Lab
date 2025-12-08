<template>
  <ul>
    <ProductListItem
      v-for="product in products"
      :key="product.id"
      :product="product"
      @add-to-cart="$emit('add-to-cart', $event)"
    />
  </ul>
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue'

defineProps({
  products: {
    type: Array,
    required: true
  }
})

defineEmits(['add-to-cart'])
</script>
