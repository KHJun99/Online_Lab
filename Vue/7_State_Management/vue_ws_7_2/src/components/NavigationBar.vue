<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/products">Products</router-link>
    <router-link to="/favorite">Favorite</router-link>
  </nav>
</template>

<script setup>
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
}

nav a:hover {
  color: #ffa500;
}

nav a.router-link-active {
  color: #ffa500;
}
</style>
