<script setup>
import { ref } from 'vue'
import BusinessCard from './components/BusinessCard.vue'

const businessCards = ref([
  { id: 1, name: '일론 머스크', title: '테슬라 테크노킹' },
  { id: 2, name: '래리 엘리슨', title: '오라클 창업주' },
  { id: 3, name: '빌 게이츠', title: '마이크로소프트 공동창업주' },
  { id: 4, name: '래리 페이지', title: '구글 공동창업주' },
  { id: 5, name: '세르게이 브린', title: '구글 공동창업주' }
])
</script>

<template>
  <div class="app-container">
    <header>
      <h1>명함 관리 페이지</h1>
    </header>
    <main>
      <article>
        <p>명함을 관리하는 <span class="highlight">페이지</span>입니다. 여기에 명함 목록이 표시됩니다.</p>
      </article>
      <section class="cards-section">
        <h2>보유 명함 목록</h2>
        <div class="cards-container">
          <BusinessCard
            v-for="card in businessCards"
            :key="card.id"
            :name="card.name"
            :title="card.title"
          />
        </div>
      </section>
    </main>
  </div>
</template>

<style scoped>
.app-container {
  min-height: 100vh;
  background-color: #f5f5f5;
}

header {
  background-color: #1e90ff;
  color: white;
  text-align: center;
  padding: 2rem;
}

header h1 {
  font-size: 2rem;
  font-weight: bold;
  margin: 0;
}

main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

article {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  margin-bottom: 2rem;
  text-align: center;
}

article p {
  font-size: 1.1rem;
  color: #333;
  margin: 0;
}

.highlight {
  color: #ff0000;
  font-weight: bold;
}

.cards-section {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
}

.cards-section h2 {
  text-align: center;
  font-size: 1.8rem;
  margin-bottom: 2rem;
  color: #333;
}

.cards-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
}
</style>
