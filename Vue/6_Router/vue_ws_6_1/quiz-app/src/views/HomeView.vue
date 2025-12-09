<template>
  <div class="home-container">
    <div class="quiz-card">
      <h2 class="title">Quiz 퀴즈</h2>
      <p class="subtitle">여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>

      <div class="home-link">
        <span>Home</span>
      </div>

      <h3 class="section-title">퀴즈 앱 사용 방법</h3>

      <div class="instruction-section">
        <h4>1. 퀴즈 목록 확인하기</h4>
        <p>퀴즈 목록 페이지에서 다양한 퀴즈를 확인하세요.</p>

        <div class="question-box">
          <p class="question-title">5번 문제. 웹 애플리케이션을 개발할 때, 사용자의 브라우저에 보여지는 부분을 렌더링하는 언어는 무엇인가요?</p>
          <label class="answer-label">정답 입력</label>
          <input type="text" class="answer-input" />
        </div>

        <div class="question-box">
          <p class="question-title">4번 문제. Python의 가상 환경을 만들어 프로젝트 별로 라이브러리 의존성을 격리시키는 명령어는?</p>
          <label class="answer-label">정답 입력</label>
          <input type="text" class="answer-input" />
        </div>

        <div class="question-box">
          <p class="question-title">3번 문제. 웹 애플리케이션에서 클라이언트의 데이터를 서버로 전송할 때 주로 사용되는 HTTP 메서드는?</p>
          <label class="answer-label">정답 입력</label>
          <input type="text" class="answer-input" />
        </div>

        <div class="question-box">
          <p class="question-title">2번 문제. HTML에서 텍스트 입력란을 만드는 데 사용되는 요소는?</p>
          <label class="answer-label">정답 입력</label>
          <input type="text" class="answer-input" />
        </div>
      </div>

      <div class="instruction-section">
        <h4>2. 퀴즈 생성하기</h4>
        <p>퀴즈를 직접 생성 할 수 있어요.</p>

        <div class="create-form">
          <h4>퀴즈 생성</h4>
          <label>문제</label>
          <textarea class="form-textarea" rows="4"></textarea>

          <label>답안</label>
          <input type="text" class="form-input" />

          <button class="submit-btn">퀴즈 생성</button>
        </div>
      </div>

      <div class="instruction-section">
        <h4>3. 정답 페이지</h4>
        <p>작성한 답안이 정답인지 확인하세요.</p>

        <div class="result-box correct">
          <h4>5번 문제<br />정답 확인</h4>
          <p class="result-text correct-text">정답입니다!</p>
          <p>나의 제출 답안: <span class="answer-value">html</span></p>
          <p>정답: <span class="answer-value">html</span></p>
        </div>

        <div class="result-box incorrect">
          <h4>5번 문제<br />정답 확인</h4>
          <p class="result-text incorrect-text">오답입니다.</p>
          <p>나의 제출 답안: <span class="answer-value">json</span></p>
          <p>정답: <span class="answer-value">html</span></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.home-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.quiz-card {
  background: white;
  border-radius: 8px;
  padding: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.title {
  background: #ff9933;
  color: white;
  text-align: center;
  padding: 15px;
  margin: -30px -30px 20px -30px;
  border-radius: 8px 8px 0 0;
  font-size: 24px;
  font-weight: bold;
}

.subtitle {
  text-align: center;
  color: #666;
  margin-bottom: 20px;
}

.home-link {
  background: #333;
  color: white;
  text-align: center;
  padding: 10px;
  margin-bottom: 20px;
  cursor: pointer;
}

.section-title {
  font-size: 20px;
  margin: 30px 0 20px 0;
  font-weight: bold;
}

.instruction-section {
  margin: 30px 0;
}

.instruction-section h4 {
  font-size: 18px;
  margin: 20px 0 10px 0;
}

.question-box {
  background: white;
  padding: 20px;
  margin: 15px 0;
  border-radius: 8px;
  border: 1px solid #ddd;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.question-title {
  margin-bottom: 15px;
  line-height: 1.6;
  font-size: 16px;
  font-weight: 500;
}

.answer-label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  font-size: 14px;
}

.answer-input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
  font-size: 14px;
}

.create-form {
  background: #f0f0f0;
  padding: 20px;
  border-radius: 4px;
  margin-top: 10px;
}

.create-form h4 {
  margin-top: 0;
}

.create-form label {
  display: block;
  margin: 15px 0 5px 0;
  font-weight: bold;
}

.form-input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
  font-size: 14px;
}

.form-textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
  font-size: 14px;
  font-family: Arial, sans-serif;
  resize: vertical;
}

.submit-btn {
  background: #007bff;
  color: white;
  border: none;
  padding: 10px 30px;
  margin-top: 15px;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;
}

.submit-btn:hover {
  background: #0056b3;
}

.result-box {
  background: white;
  border: 2px solid #ddd;
  padding: 20px;
  margin: 15px 0;
  border-radius: 4px;
  text-align: center;
}

.result-box.correct {
  border-color: #28a745;
}

.result-box.incorrect {
  border-color: #dc3545;
}

.result-box h4 {
  margin-top: 0;
  background: #f8f8f8;
  padding: 10px;
  margin: -20px -20px 15px -20px;
}

.result-text {
  font-size: 20px;
  font-weight: bold;
  margin: 15px 0;
}

.correct-text {
  color: #28a745;
}

.incorrect-text {
  color: #dc3545;
}

.result-box p {
  margin: 10px 0;
  text-align: left;
}

.answer-value {
  color: #007bff;
  font-weight: 500;
}
</style>
