<script setup>
import HeaderComponent from './components/HeaderComponent.vue'
import MainComponent from './components/MainComponent.vue'
import ArticleComponent from './components/ArticleComponent.vue'
import FooterComponent from './components/FooterComponent.vue'
</script>

<template>
  <div>
    <HeaderComponent />
    <MainComponent>
      <ArticleComponent />
    </MainComponent>
    <FooterComponent />
  </div>
</template>

<style scoped></style>
