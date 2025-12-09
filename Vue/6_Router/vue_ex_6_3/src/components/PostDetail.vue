<template>
  <div>
    <h3>{{ username }}이 작성한 게시글</h3>
    <ol>
      <li v-for="post in posts" :key="post.id">
        <RouterLink :to="{ name: 'user-posts-detail', params: { username: username, id: post.id } }">
          제목: {{ post.title }}
        </RouterLink>
      </li>
    </ol>
    <hr />
    <div v-if="currentPost">
      <p>번호 : {{ currentPost.id }}</p>
      <p>제목 : {{ currentPost.title }}</p>
      <p>내용 : {{ currentPost.content }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, RouterLink } from 'vue-router'

const route = useRoute()
const username = ref(route.params.username)

const posts = ref([
  { id: 1, title: 'Post 1', content: 'Content 1' },
  { id: 2, title: 'Post 2', content: 'Content 2' },
  { id: 3, title: 'Post 3', content: 'Content 3' }
])

const currentPost = computed(() => {
  const postId = parseInt(route.params.id)
  return posts.value.find(post => post.id === postId)
})
</script>

<style scoped>
</style>
