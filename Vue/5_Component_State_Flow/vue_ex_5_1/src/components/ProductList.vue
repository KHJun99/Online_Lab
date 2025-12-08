<template>
  <ul>
    <li v-for="product in products" :key="product.id">
      {{ product.name }} - {{ product.price }}원
    </li>
  </ul>
</template>

<script setup>
defineProps({
  products: {
    type: Array,
    required: true
  }
})
</script>
