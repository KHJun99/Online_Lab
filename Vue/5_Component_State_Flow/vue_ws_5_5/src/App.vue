<script setup>
import { ref, computed } from 'vue'
import BusinessCard from './components/BusinessCard.vue'
import CreateCardForm from './components/CreateCardForm.vue'

let nextId = 6

const businessCards = ref([
  { id: 1, name: '일론 머스크', title: '테슬라 테크노킹' },
  { id: 2, name: '래리 엘리슨', title: '오라클 창업주' },
  { id: 3, name: '빌 게이츠', title: '마이크로소프트 공동창업주' },
  { id: 4, name: '래리 페이지', title: '구글 공동창업주' },
  { id: 5, name: '세르게이 브린', title: '구글 공동창업주' }
])

const newCard = ref({
  name: '',
  title: ''
})

const cardCount = computed(() => businessCards.value.length)

const createCard = (cardData) => {
  businessCards.value.push({
    id: nextId++,
    name: cardData.name,
    title: cardData.title
  })
  newCard.value = { name: '', title: '' }
}

const deleteCard = (cardId) => {
  const index = businessCards.value.findIndex(card => card.id === cardId)
  if (index !== -1) {
    businessCards.value.splice(index, 1)
  }
}
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

      <section class="form-section">
        <CreateCardForm :new-card="newCard" @create-card="createCard" />
      </section>

      <section class="cards-section">
        <h2>보유 명함 목록</h2>
        <p class="card-count">현재 보유중인 명함 수 : {{ cardCount }}</p>
        <div v-if="cardCount > 0" class="cards-container">
          <BusinessCard
            v-for="card in businessCards"
            :key="card.id"
            :name="card.name"
            :title="card.title"
            @delete-card="deleteCard(card.id)"
          />
        </div>
        <div v-else class="empty-message">
          <p>명함이 없습니다. 새로운 명함을 추가해 주세요.</p>
        </div>
      </section>
    </main>
  </div>
</template>

<style scoped>
.app-container {
  min-height: 100vh;
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
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
  flex: 1;
  max-width: 1200px;
  width: 100%;
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

.form-section {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}

.cards-section {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
}

.cards-section h2 {
  text-align: center;
  font-size: 1.8rem;
  margin-bottom: 1rem;
  color: #333;
}

.card-count {
  text-align: center;
  font-size: 1rem;
  color: #666;
  margin-bottom: 2rem;
}

.cards-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
}

.empty-message {
  text-align: center;
  padding: 3rem;
  color: #666;
}

.empty-message p {
  font-size: 1.1rem;
}
</style>
