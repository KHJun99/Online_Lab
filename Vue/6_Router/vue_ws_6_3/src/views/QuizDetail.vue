<template>
  <div class="quiz-detail">
    <div class="detail-card" v-if="quiz">
      <h2 class="detail-title">{{ quiz.pk }}번 문제</h2>

      <div class="detail-content">
        <h3 class="question-text">{{ quiz.question }}</h3>
        <p class="answer-info">정답: <span class="answer-value">{{ quiz.answer }}</span></p>
      </div>
    </div>

    <div v-else class="no-quiz">
      <p>퀴즈를 찾을 수 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const quizzes = [
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
]

const quiz = ref(null)

onMounted(() => {
  const quizId = parseInt(route.params.id)
  quiz.value = quizzes.find(q => q.pk === quizId)
})
</script>

<style scoped>
.quiz-detail {
  max-width: 700px;
  margin: 40px auto;
  padding: 20px;
}

.detail-card {
  background: white;
  border-radius: 8px;
  border: 2px solid #ddd;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.detail-title {
  background: #f8f8f8;
  text-align: center;
  padding: 20px;
  margin: 0;
  font-size: 22px;
  line-height: 1.6;
  border-bottom: 1px solid #ddd;
  color: #333;
}

.detail-content {
  padding: 30px;
}

.question-text {
  font-size: 18px;
  line-height: 1.8;
  margin: 0 0 25px 0;
  color: #333;
  font-weight: 500;
}

.answer-info {
  font-size: 16px;
  margin: 15px 0;
  line-height: 1.8;
  color: #333;
}

.answer-value {
  color: #007bff;
  font-weight: 600;
  font-size: 17px;
}

.no-quiz {
  text-align: center;
  padding: 40px;
  background: white;
  border-radius: 8px;
}
</style>
