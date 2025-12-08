<template>
  <li>
    {{ product.name }} - {{ product.price }}원
    <button @click="$emit('add-to-cart', product)">장바구니에 추가</button>
  </li>
</template>

<script setup>
defineProps({
  product: {
    type: Object,
    required: true
  }
})

defineEmits(['add-to-cart'])
</script>
