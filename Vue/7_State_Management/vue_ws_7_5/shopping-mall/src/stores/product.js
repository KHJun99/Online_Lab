import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  // 초기 데이터 (localStorage에 데이터가 없을 때 사용)
  const defaultProducts = [
    {
      name: '상품 1',
      imagePath: 'src/assets/product1.png',
      price: 10000,
      isFavorite: false
    },
    {
      name: '상품 2',
      imagePath: 'src/assets/product2.png',
      price: 20000,
      isFavorite: false
    },
    {
      name: '상품 3',
      imagePath: 'src/assets/product3.png',
      price: 30000,
      isFavorite: false
    },
    {
      name: '상품 4',
      imagePath: 'src/assets/product4.png',
      price: 40000,
      isFavorite: false
    }
  ]

  // localStorage에서 데이터 불러오기
  const loadFromLocalStorage = () => {
    const saved = localStorage.getItem('productList')
    if (saved) {
      try {
        return JSON.parse(saved)
      } catch (e) {
        console.error('Error parsing localStorage data:', e)
        return defaultProducts
      }
    }
    return defaultProducts
  }

  // localStorage에서 불러오거나 기본 데이터 사용
  const productList = ref(loadFromLocalStorage())

  // productList 변경 감지하여 localStorage에 저장
  watch(
    productList,
    (newValue) => {
      localStorage.setItem('productList', JSON.stringify(newValue))
    },
    { deep: true }
  )

  // Getter: isFavorite가 true인 제품 개수 계산
  const favoriteCount = computed(() => {
    return productList.value.filter(product => product.isFavorite).length
  })

  // Getter: isFavorite가 true인 제품들만 반환
  const favoriteProducts = computed(() => {
    return productList.value.filter(product => product.isFavorite)
  })

  // Action: 제품의 isFavorite 상태 토글
  const toggleFavorite = (productName) => {
    const product = productList.value.find(p => p.name === productName)
    if (product) {
      product.isFavorite = !product.isFavorite
    }
  }

  return {
    productList,
    favoriteCount,
    favoriteProducts,
    toggleFavorite
  }
})
