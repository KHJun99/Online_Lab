<script setup>
import { useBalanceStore } from '@/stores/balance'
import { useRoute } from 'vue-router'

const route = useRoute()
const store = useBalanceStore()

const name = route.params.name

const person = store.balances.find(b => b.name === name)

const handleUpdate = () => {
  store.updateBalance(name, 1000)
}
</script>

<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <p>이름: {{ person.name }}</p>
    <p>잔고: {{ person.balance }}</p>
    <button @click="handleUpdate">+</button>
  </div>
</template>

<style scoped>
</style>
