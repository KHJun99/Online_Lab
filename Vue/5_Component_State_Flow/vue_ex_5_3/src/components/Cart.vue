<template>
  <div>
    <h2>총 가격: {{ totalPrice }}원</h2>
    <h2>장바구니</h2>
    <ul>
      <li v-for="item in cartItems" :key="item.id">
        {{ item.name }} - {{ item.price }}원
        <button @click="$emit('remove-from-cart', item.id)">삭제</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  cartItems: {
    type: Array,
    required: true
  }
})

defineEmits(['remove-from-cart'])

const totalPrice = computed(() => {
  return props.cartItems.reduce((sum, item) => sum + item.price, 0)
})
</script>
