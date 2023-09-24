<script setup></script>

<template>
  <div class="header-container"><h1>Welcome to Habit APP</h1></div>
</template>

<style scoped>
.header-container {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr;
  padding: 8px;
  border-radius: 10px;
  margin: 20px;
  margin-bottom: 5px;
  height: 15vh;
  width: 90vw;
  background-color: rgb(241 240 240);
  opacity: 0.8;
  align-items: center;
  text-align: center;
}

h1 {
  font-weight: bold;
}

@media (width >= 768px) {
  .header-container {
    height: 15vh;
    width: 60vw;
  }
}

@media (width >= 1024px) {
  .header-container {
    height: 8vh;
    width: 50vw;
  }
}
</style>
