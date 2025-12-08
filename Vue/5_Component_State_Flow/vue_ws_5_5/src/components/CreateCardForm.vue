<template>
  <form @submit.prevent="handleSubmit" class="create-form">
    <div class="form-group">
      <label for="name">이름</label>
      <input
        id="name"
        v-model="formData.name"
        type="text"
        placeholder=""
        required
      />
    </div>
    <div class="form-group">
      <label for="title">직함</label>
      <input
        id="title"
        v-model="formData.title"
        type="text"
        placeholder=""
        required
      />
    </div>
    <button type="submit" class="submit-btn">명함 추가</button>
  </form>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  newCard: {
    type: Object,
    default: () => ({ name: '', title: '' })
  }
})

const emit = defineEmits(['create-card'])

const formData = ref({
  name: '',
  title: ''
})

// Watch for changes in newCard prop
watch(() => props.newCard, (newValue) => {
  formData.value = { ...newValue }
}, { immediate: true, deep: true })

const handleSubmit = () => {
  if (formData.value.name.trim() && formData.value.title.trim()) {
    emit('create-card', { ...formData.value })
    formData.value = { name: '', title: '' }
  }
}
</script>

<style scoped>
.create-form {
  display: flex;
  gap: 1rem;
  align-items: flex-end;
  justify-content: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.form-group label {
  font-size: 0.9rem;
  color: #333;
  font-weight: 500;
}

.form-group input {
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  min-width: 200px;
}

.form-group input:focus {
  outline: none;
  border-color: #1e90ff;
}

.submit-btn {
  padding: 0.5rem 1.5rem;
  background-color: #1e90ff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
}

.submit-btn:hover {
  background-color: #1c7ed6;
}
</style>
