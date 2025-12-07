<template>
  <div>
    <header class="bg-light py-4 mb-4">
      <div class="container">
        <h1 class="display-4 text-center">My Gallery</h1>
      </div>
    </header>

    <main class="container">
      <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
        <div class="col" v-for="i in 4" :key="i">
          <div class="card h-100">
            <img src="../assets/sample.png" class="card-img-top" alt="sample">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
</script>

<style scoped>
</style>
