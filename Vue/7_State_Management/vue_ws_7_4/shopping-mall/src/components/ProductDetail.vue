<template>
  <div class="product-card">
    <h3>{{ product.name }}</h3>
    <img :src="getImagePath(product.imagePath)" :alt="product.name" />
    <p class="price">₩ {{ product.price.toLocaleString() }}</p>
    <button @click="toggleFavorite" class="favorite-btn">
      <svg
        :class="{ 'filled': product.isFavorite }"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 24 24"
        width="24"
        height="24"
      >
        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
      </svg>
    </button>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import { useProductStore } from '@/stores/product'

const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})

const store = useProductStore()

const getImagePath = (path) => {
  // Convert the path to work with Vite
  const fileName = path.split('/').pop()
  return new URL(`../assets/${fileName}`, import.meta.url).href
}

const toggleFavorite = () => {
  store.toggleFavorite(props.product.name)
}
</script>

<style scoped>
.product-card {
  border: 1px solid #ddd;
  padding: 1.5rem;
  text-align: center;
  background: white;
  position: relative;
}

.product-card h3 {
  font-size: 1.2rem;
  margin-bottom: 1rem;
}

.product-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  margin-bottom: 1rem;
}

.price {
  font-size: 1.1rem;
  color: #333;
  margin: 1rem 0;
}

.favorite-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  display: inline-block;
}

.favorite-btn svg {
  fill: none;
  stroke: #333;
  stroke-width: 2;
  transition: all 0.3s;
}

.favorite-btn svg.filled {
  fill: #ff0000;
  stroke: #ff0000;
}

.favorite-btn:hover svg {
  stroke: #ff0000;
}
</style>
