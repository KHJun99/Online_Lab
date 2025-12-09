<template>
  <div class="answer-view">
    <div class="answer-card">
      <h2 class="card-title">{{ quizId }}번 문제</h2>
      <h3 class="card-subtitle">정답 확인</h3>

      <div class="result-box">
        <p :class="['result-message', isCorrect ? 'correct' : 'incorrect']">
          {{ isCorrect ? '정답입니다!' : '오답입니다.' }}
        </p>

        <div class="answer-details">
          <p class="detail-item user-answer-line">
            나의 제출 답안: <span class="user-answer">{{ userAnswer }}</span>
          </p>
          <p class="detail-item">
            정답: <span class="correct-answer">{{ correctAnswer }}</span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const quizzes = [
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

const quizId = ref(null)
const userAnswer = ref('')
const correctAnswer = ref('')

const isCorrect = computed(() => {
  return userAnswer.value.toLowerCase() === correctAnswer.value.toLowerCase()
})

onMounted(() => {
  quizId.value = parseInt(route.params.id)
  userAnswer.value = route.query.userAnswer || ''

  const quiz = quizzes.find(q => q.id === quizId.value)
  if (quiz) {
    correctAnswer.value = quiz.answer
  }
})
</script>

<style scoped>
.answer-view {
  max-width: 500px;
  margin: 20px auto;
  padding: 0;
}

.answer-card {
  background: #e8e8e8;
  border-radius: 8px;
  padding: 30px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border: 1px solid #ccc;
}

.card-title {
  text-align: center;
  margin: 0 0 10px 0;
  font-size: 16px;
  color: #333;
  font-weight: normal;
}

.card-subtitle {
  text-align: center;
  margin: 0 0 20px 0;
  font-size: 20px;
  color: #000;
  font-weight: bold;
}

.result-box {
  background: white;
  padding: 25px;
  border-radius: 8px;
  border: 1px solid #ddd;
}

.result-message {
  text-align: left;
  font-size: 16px;
  font-weight: normal;
  margin: 0 0 15px 0;
  padding: 0;
  border-radius: 0;
}

.result-message.correct {
  color: #28a745;
  background-color: transparent;
  border: none;
}

.result-message.incorrect {
  color: #dc3545;
  background-color: transparent;
  border: none;
}

.answer-details {
  background: transparent;
  padding: 0;
  border-radius: 0;
}

.detail-item {
  font-size: 14px;
  margin: 8px 0;
  line-height: 1.6;
  color: #333;
}

.user-answer-line {
  color: #dc3545;
}

.user-answer {
  color: #dc3545;
  font-weight: normal;
  font-size: 14px;
}

.correct-answer {
  color: #333;
  font-weight: normal;
  font-size: 14px;
}
</style>
