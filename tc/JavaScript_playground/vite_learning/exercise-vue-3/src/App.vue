<script setup>
import { ref } from 'vue';

const numbers = ref([1, 2, 3]);
const listvisible = ref(true);

function toggle() {
  listvisible.value = !listvisible.value;
}
function push() {
  numbers.value.push(numbers.value.length + 1);
}
function pop() {
  numbers.value.pop();
}
function reverse() {
  numbers.value = numbers.value.reverse;
}
</script>

<template>
  <header>
    <h1>Hello World!</h1>
  </header>

  <main>
    <button @click="toggle" class="toggle" type="button">Toggle List</button>
    <button @click="push" class="push" type="button">Push Number</button>
    <button @click="pop" class="pop" type="button">Pop Number</button>
    <button @click="reverse" class="reverse" type="button">Reverse Order</button>
    <ul v-if="listvisible">
      <ul v-for="number in numbers" :key="number">
        {{
          number
        }}
      </ul>
    </ul>
  </main>
</template>

<style scoped>
header,
main {
  text-align: center;
}
</style>
