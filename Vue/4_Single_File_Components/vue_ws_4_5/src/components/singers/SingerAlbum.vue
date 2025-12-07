<template>
  <div class="album">
    <h3>앨범 제목</h3>
    <ul>
      <li>노래 곡목 1</li>
      <li>노래 곡목 2</li>
      <li>노래 곡목 3</li>
    </ul>
  </div>
</template>

<script setup>
</script>

<style scoped>
.album {
  border: 1px solid #ddd;
  padding: 15px;
  margin: 10px;
  background-color: #fff;
  min-width: 150px;
}

h3 {
  margin: 0 0 10px 0;
  font-size: 1em;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  color: orangered;
  margin: 5px 0;
  font-size: 0.9em;
}
</style>
