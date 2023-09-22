<script setup>
import { ref } from 'vue';

const products = ref([
  {
    text: 'apple',
    quantity: 5,
    id: '1'
  },
  {
    text: 'banana',
    quantity: 3,
    id: '2'
  },
  {
    text: 'carrot',
    quantity: 7,
    id: '3'
  }
]);

const groceryitem = ref();
</script>

<template>
  <header>
    <h1>Hello World!</h1>
  </header>
  <main>
    <li v-for="product in products" :key="product.id">
      {{ product.text }}
    </li>
  </main>
</template>

<style scoped>
header {
  text-align: center;
}
</style>
