<script setup>
import ParentPage from './components/ParentPage.vue'
import ChildPage from './components/ChildPage.vue'
</script>

<template>
  <div class="app-container">
    <ParentPage>
      <ChildPage name="김하나" :age="30" />
      <ChildPage name="김두리" :age="20" />
      <ChildPage name="김서이" :age="10" />
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
