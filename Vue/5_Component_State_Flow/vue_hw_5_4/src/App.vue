<script setup>
import { ref } from 'vue'
import ParentPage from './components/ParentPage.vue'
import ChildPage from './components/ChildPage.vue'

const children = ref([
  { name: '김하나', age: 30, balance: 100000 },
  { name: '김두리', age: 20, balance: 10000 },
  { name: '김서이', age: 10, balance: 1000 }
])

const updateBalance = (index) => {
  children.value[index].balance += 1000
}
</script>

<template>
  <div class="app-container">
    <ParentPage>
      <ChildPage
        v-for="(child, index) in children"
        :key="index"
        :name="child.name"
        :age="child.age"
        :balance="child.balance"
        @give-allowance="updateBalance(index)"
      />
    </ParentPage>
  </div>
</template>

<style scoped>
.app-container {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}
</style>
