import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  const products = ref([])

  const productCount = computed(() => products.value.length)

  const getProducts = async () => {
    try {
      const response = await axios.get('https://jsonplaceholder.typicode.com/posts')
      products.value = response.data
    } catch (error) {
      console.error('Error fetching products:', error)
    }
  }

  const deleteProduct = function (productId) {
    const index = products.value.findIndex(product => product.id === productId)
    if (index !== -1) {
      products.value.splice(index, 1)
    }
  }

  return { products, productCount, getProducts, deleteProduct }
})
