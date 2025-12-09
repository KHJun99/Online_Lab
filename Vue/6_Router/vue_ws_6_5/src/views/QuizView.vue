<template>
  <div class="quiz-view">
    <div class="quiz-item" v-for="quiz in quizzes" :key="quiz.id">
      <h3 class="quiz-title">{{ quiz.id }}번 문제. {{ quiz.question }}</h3>
      <label class="answer-label">정답 입력</label>
      <input
        v-model="userAnswers[quiz.id]"
        type="text"
        class="answer-input"
        placeholder="답을 입력하세요"
        @keyup.enter="checkAnswer(quiz.id, quiz.answer)"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const quizzes = ref([])
const userAnswers = ref({})

// 초기 퀴즈 데이터 로드
onMounted(() => {
  const savedQuizzes = localStorage.getItem('quizzes')
  if (savedQuizzes) {
    quizzes.value = JSON.parse(savedQuizzes)
  } else {
    // 기본 퀴즈 데이터
    quizzes.value = [
      {
        id: 1,
        question: 'Python 팁 프레임워크 중 하나로, 마이크로 웹 프레임워크로 빠른 개발을 지원하는 것은?',
        answer: 'flask'
      },
      {
        id: 2,
        question: 'HTML에서 텍스트 입력란을 만드는 데 사용되는 요소는?',
        answer: 'input'
      },
      {
        id: 3,
        question: '웹 애플리케이션에서 클라이언트의 데이터를 서버로 전송할 때 주로 사용되는 HTTP 메서드는?',
        answer: 'post'
      },
      {
        id: 4,
        question: 'Python의 가상 환경을 만들어 프로젝트 별로 라이브러리 의존성을 격리시키는 명령어는?',
        answer: 'virtualenv'
      },
      {
        id: 5,
        question: '웹 애플리케이션을 개발할 때, 사용자의 브라우저에 보여지는 부분을 렌더링하는 언어는 무엇인가요?',
        answer: 'html'
      }
    ]
    localStorage.setItem('quizzes', JSON.stringify(quizzes.value))
  }
})

const checkAnswer = (quizId, correctAnswer) => {
  const userAnswer = userAnswers.value[quizId]
  if (userAnswer && userAnswer.trim()) {
    const confirmed = window.confirm(`${userAnswer} 을/를 답안으로 제출합니다. 확실합니까?`)
    if (confirmed) {
      if (userAnswer.toLowerCase().trim() === correctAnswer.toLowerCase()) {
        alert('정답입니다!')
      } else {
        alert('오답입니다.')
      }
    }
  }
}
</script>

<style scoped>
.quiz-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 10px 20px 20px 20px;
}

.quiz-item {
  background: white;
  padding: 25px;
  margin: 15px 0;
  border-radius: 8px;
  border: 1px solid #ddd;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.quiz-item:first-child {
  margin-top: 0;
}

.quiz-title {
  margin: 0 0 20px 0;
  font-size: 16px;
  line-height: 1.6;
  font-weight: 500;
  color: #333;
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
