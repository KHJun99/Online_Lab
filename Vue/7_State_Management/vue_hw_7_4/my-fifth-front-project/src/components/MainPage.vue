<script setup>
import { useBalanceStore } from '@/stores/balance'

const store = useBalanceStore()
</script>

<template>
  <div>
    <h2>메인 페이지</h2>
    <div v-for="person in store.balances" :key="person.name">
      <p>이름: {{ person.name }}</p>
      <p>잔고: {{ person.balance }}</p>
      <router-link :to="`/update/${person.name}`">
        <button>updateBalance</button>
      </router-link>
      <hr>
    </div>
  </div>
</template>

<style scoped>
button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 8px 16px;
  cursor: pointer;
  border-radius: 4px;
}

button:hover {
  background-color: #0056b3;
}
</style>
