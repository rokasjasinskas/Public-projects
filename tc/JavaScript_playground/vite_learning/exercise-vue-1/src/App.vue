<script setup>
import { ref } from 'vue';

const message = ref('Hello World!');

function reversetext() {
  message.value = message.value.split('').reverse().join('');
}
function append() {
  message.value += '!';
}
</script>

<template>
  <header>
    <h1>{{ message }}</h1>
  </header>

  <main>
    <button @click="reversetext" class="reverse" type="button">Reverse Message</button>
    <button @click="append" class="append" type="button">Append !</button>
  </main>
</template>

<style scoped>
button {
  display: block;
  margin-bottom: 1rem;
}
</style>
