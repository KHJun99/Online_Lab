<script setup>
import { ref } from 'vue'

const colorInput = ref('')
const textColor = ref('black')

const changeColor = () => {
  textColor.value = colorInput.value
}
</script>

<template>
  <div>
    <input
      v-model="colorInput"
      @input="changeColor"
      type="text"
    />
    <p :style="{ color: textColor }">
      입력창에 올바른 색상 명을 입력하면 글자색이 바뀌요.
    </p>
  </div>
</template>

<style scoped>
</style>
