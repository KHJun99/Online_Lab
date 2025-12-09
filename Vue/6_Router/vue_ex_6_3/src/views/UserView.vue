<template>
  <div>
    <h2>User Profile</h2>
    <p>Username: {{ username }}</p>
    <hr />
    <RouterLink :to="{ name: 'user-profile', params: { username: username } }">상세 프로필</RouterLink>
    <span> | </span>
    <RouterLink :to="{ name: 'user-posts', params: { username: username } }">작성한 게시글</RouterLink>
    <hr />
    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, RouterLink, RouterView } from 'vue-router'

const route = useRoute()
const username = ref(route.params.username)
</script>
