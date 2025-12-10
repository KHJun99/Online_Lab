<template>
  <div class="favorite">
    <h1>장바구니 페이지</h1>
    <div v-if="store.favoriteProducts.length === 0" class="empty-message">
      <p>즐겨찾기에 추가된 상품이 없습니다.</p>
    </div>
    <div v-else class="product-grid">
      <ProductDetail
        v-for="(product, index) in store.favoriteProducts"
        :key="index"
        :product="product"
      />
    </div>
  </div>
</template>

<script setup>
import ProductDetail from '@/components/ProductDetail.vue'
import { useProductStore } from '@/stores/product'

const store = useProductStore()
</script>

<style scoped>
.favorite {
  padding: 2rem;
}

h1 {
  font-size: 2rem;
  margin-bottom: 2rem;
}

.empty-message {
  text-align: center;
  padding: 3rem;
  color: #666;
  font-size: 1.2rem;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  max-width: 1200px;
}

@media (max-width: 768px) {
  .product-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .product-grid {
    grid-template-columns: 1fr;
  }
}
</style>
