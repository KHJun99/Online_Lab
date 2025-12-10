import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
    },
    {
      name: '김두리',
      balance: 10000
    },
    {
      name: '김서이',
      balance: 100
    }
  ])

  function updateBalance(name, amount) {
    const person = balances.value.find(b => b.name === name)
    if (person) {
      person.balance += amount
    }
  }

  return { balances, updateBalance }
})
