<template>
  <div class="quiz-view">
    <div class="quiz-create-section">
      <h2 class="section-title">퀴즈 생성</h2>

      <div class="form-group">
        <label class="form-label">문제</label>
        <textarea
          v-model="newQuiz.question"
          class="form-textarea"
          rows="4"
          placeholder="문제를 입력하세요"
        ></textarea>
      </div>

      <div class="form-group">
        <label class="form-label">답안</label>
        <input
          v-model="newQuiz.answer"
          type="text"
          class="form-input"
          placeholder="답안을 입력하세요"
        />
      </div>

      <button @click="createQuiz" class="create-button">퀴즈 생성</button>
    </div>

    <div class="quiz-list-section">
      <div class="quiz-item" v-for="quiz in sortedQuizzes" :key="quiz.pk">
        <RouterLink :to="{ name: 'quiz-detail', params: { id: quiz.pk } }" class="quiz-link">
          <h3 class="quiz-title">{{ quiz.pk }}번 문제. {{ quiz.question }}</h3>
        </RouterLink>
        <label class="answer-label">정답 입력</label>
        <input type="text" class="answer-input" placeholder="답을 입력하세요" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { RouterLink } from 'vue-router'

const quizzes = ref([
  {
    pk: 1,
    question: 'Python 팁 프레임워크 중 하나로, 마이크로 웹 프레임워크로 빠른 개발을 지원하는 것은?',
    answer: 'flask'
  },
  {
    pk: 2,
    question: 'HTML에서 텍스트 입력란을 만드는 데 사용되는 요소는?',
    answer: 'input'
  },
  {
    pk: 3,
    question: '웹 애플리케이션에서 클라이언트의 데이터를 서버로 전송할 때 주로 사용되는 HTTP 메서드는?',
    answer: 'post'
  },
  {
    pk: 4,
    question: 'Python의 가상 환경을 만들어 프로젝트 별로 라이브러리 의존성을 격리시키는 명령어는?',
    answer: 'virtualenv'
  },
  {
    pk: 5,
    question: '웹 애플리케이션을 개발할 때, 사용자의 브라우저에 보여지는 부분을 렌더링하는 언어는 무엇인가요?',
    answer: 'html'
  }
])

const newQuiz = ref({
  question: '',
  answer: ''
})

const sortedQuizzes = computed(() => {
  return [...quizzes.value].sort((a, b) => b.pk - a.pk)
})

const createQuiz = () => {
  if (newQuiz.value.question.trim() && newQuiz.value.answer.trim()) {
    const newPk = Math.max(...quizzes.value.map(q => q.pk)) + 1
    quizzes.value.push({
      pk: newPk,
      question: newQuiz.value.question,
      answer: newQuiz.value.answer
    })
    newQuiz.value.question = ''
    newQuiz.value.answer = ''
  }
}
</script>

<style scoped>
.quiz-view {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
}

.quiz-create-section {
  background: white;
  padding: 30px;
  margin-bottom: 30px;
  border-radius: 8px;
  border: 1px solid #ddd;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
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

.quiz-list-section {
  margin-top: 30px;
}

.quiz-item {
  background: white;
  padding: 25px;
  margin: 20px 0;
  border-radius: 8px;
  border: 1px solid #ddd;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.quiz-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.quiz-link:hover .quiz-title {
  color: #007bff;
}

.quiz-title {
  margin: 0 0 20px 0;
  font-size: 16px;
  line-height: 1.6;
  font-weight: 500;
  color: #333;
  transition: color 0.2s;
}

.answer-label {
  display: block;
  margin: 15px 0 8px 0;
  font-weight: 500;
  font-size: 14px;
  color: #555;
}

.answer-input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  box-sizing: border-box;
}

.answer-input:focus {
  outline: none;
  border-color: #007bff;
}
</style>
