<script setup>
import { ref } from 'vue';
import GroceryItem from './components/GroceryItem.vue';

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
</script>

<template>
  <header>
    <h1>Hello World!</h1>
  </header>
  <main>
    <ol>
      <GroceryItem v-for="product in products" :key="product.id" :item="product" />
    </ol>
  </main>
</template>

<style scoped>
header {
  text-align: center;
}
</style>
