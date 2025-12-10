<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/products">Products</router-link>
    <router-link to="/favorite" class="favorite-link">
      Favorite
      <span v-if="store.favoriteCount > 0" class="badge">{{ store.favoriteCount }}</span>
    </router-link>
  </nav>
</template>

<script setup>
import { useProductStore } from '@/stores/product'

const store = useProductStore()
</script>

<style scoped>
nav {
  background-color: #333;
  padding: 1rem;
  display: flex;
  gap: 2rem;
  justify-content: center;
}

nav a {
  color: white;
  text-decoration: none;
  font-size: 1.1rem;
  position: relative;
}

nav a:hover {
  color: #ffa500;
}

nav a.router-link-active {
  color: #ffa500;
}

.favorite-link {
  position: relative;
}

.badge {
  position: absolute;
  top: -8px;
  right: -12px;
  background-color: #ff0000;
  color: white;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: bold;
}
</style>
