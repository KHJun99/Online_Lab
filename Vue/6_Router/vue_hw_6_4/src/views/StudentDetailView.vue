<template>
  <div class="student-detail">
    <h2>학생 상세 정보 페이지입니다.</h2>
    <p>이름 : {{ name }}</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()
const name = computed(() => route.params.name)
</script>

<style scoped>
.student-detail {
  padding: 20px;
}

.student-detail p {
  margin-top: 10px;
  font-size: 16px;
}
</style>
