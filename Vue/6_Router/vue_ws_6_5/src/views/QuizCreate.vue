<template>
  <div class="quiz-create">
    <div class="create-card">
      <h2 class="section-title">퀴즈 생성</h2>

      <div class="form-group">
        <label class="form-label">문제</label>
        <textarea
          v-model="question"
          class="form-textarea"
          rows="4"
          placeholder="vue.js의 라이프 사이클 중 화면 구성에 사용할 데이터를 가져올 때 가장 적절한 시점은?"
        ></textarea>
      </div>

      <div class="form-group">
        <label class="form-label">답안</label>
        <input
          v-model="answer"
          type="text"
          class="form-input"
          placeholder=""
        />
      </div>

      <button @click="createQuiz" class="create-button">퀴즈 생성</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { onBeforeRouteLeave } from 'vue-router'

const question = ref('')
const answer = ref('')
const isWriting = ref(false)

// 입력값이 변경될 때마다 isWriting 상태 업데이트
const updateWritingStatus = () => {
  isWriting.value = question.value.trim() !== '' || answer.value.trim() !== ''
}

// question과 answer의 변경을 감지
const questionInput = ref(question)
const answerInput = ref(answer)

// beforeRouteLeave 가드
onBeforeRouteLeave((to, from, next) => {
  // 작성 중인 내용이 있는지 확인
  if (question.value.trim() || answer.value.trim()) {
    const confirmed = window.confirm('작성중인 문제가 있습니다. 다른 경로로 이동하시 작성중이던 내용은 소멸됩니다. 이동하시겠습니까?')
    if (confirmed) {
      next()
    } else {
      next(false)
    }
  } else {
    next()
  }
})

const createQuiz = () => {
  if (question.value.trim() && answer.value.trim()) {
    // localStorage에서 기존 퀴즈 가져오기
    const savedQuizzes = localStorage.getItem('quizzes')
    const quizzes = savedQuizzes ? JSON.parse(savedQuizzes) : []

    // 새 퀴즈 ID 생성 (기존 퀴즈 중 가장 큰 ID + 1)
    const newId = quizzes.length > 0 ? Math.max(...quizzes.map(q => q.id)) + 1 : 1

    // 새 퀴즈 추가
    const newQuiz = {
      id: newId,
      question: question.value.trim(),
      answer: answer.value.trim()
    }
    quizzes.push(newQuiz)

    // localStorage에 저장
    localStorage.setItem('quizzes', JSON.stringify(quizzes))

    alert('퀴즈가 생성되었습니다!')
    question.value = ''
    answer.value = ''
  }
}
</script>

<style scoped>
.quiz-create {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
}

.create-card {
  background: #f0f0f0;
  padding: 30px;
  border-radius: 8px;
  border: 1px solid #ddd;
}

.section-title {
  margin: 0 0 25px 0;
  font-size: 24px;
  font-weight: bold;
  color: #333;
}

.form-group {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  font-size: 14px;
  color: #333;
}

.form-textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  font-family: inherit;
  box-sizing: border-box;
  resize: vertical;
  background: white;
}

.form-textarea:focus {
  outline: none;
  border-color: #007bff;
}

.form-input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  box-sizing: border-box;
  background: white;
}

.form-input:focus {
  outline: none;
  border-color: #007bff;
}

.create-button {
  width: 100%;
  padding: 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.2s;
}

.create-button:hover {
  background-color: #0056b3;
}
</style>
