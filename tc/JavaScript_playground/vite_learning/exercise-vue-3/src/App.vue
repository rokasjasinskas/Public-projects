<script setup>
import { ref } from 'vue';

const numbers = ref([1, 2, 3]);
const listvisible = ref(true);
</script>

<template>
  <header>
    <h1>Hello World!</h1>
  </header>

  <main>
    <button @click="listvisible = !listvisible" class="toggle" type="button">Toggle List</button>
    <button @click="numbers.push(numbers.length + 1)" class="push" type="button">
      Push Number
    </button>
    <button @click="numbers.pop()" class="pop" type="button">Pop Number</button>
    <button @click="numbers.reverse()" class="reverse" type="button">Reverse Order</button>
    <ul v-if="listvisible && numbers.length">
      <ul v-for="number of numbers" :key="number">
        {{
          number
        }}
      </ul>
    </ul>
    <p v-else-if="numbers.length">List is not empty, but hidden.</p>
    <p v-else>List is empty</p>
  </main>
</template>

<style scoped>
header,
main {
  text-align: center;
}
</style>
