<template>
  <div class="product">
    <h1>상품 목록 페이지</h1>
    <div class="product-grid">
      <ProductDetail
        v-for="(product, index) in store.productList"
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
.product {
  padding: 2rem;
}

h1 {
  font-size: 2rem;
  margin-bottom: 2rem;
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
