<script setup>
import { ref } from 'vue';

const message = ref('Placeholder for paragraph');
const hover = ref('Message after hover');
const redtext = ref(true);
const textcolor = ref('green');

function togglered() {
  redtext.value = !redtext.value;
}

function alternate() {
  textcolor.value = textcolor.value === 'green' ? 'blue' : 'green';
}
</script>

<template>
  <header>
    <h1>Hello World!</h1>
  </header>
  <main>
    <div>
      <span :title="hover">{{ message }}</span>
    </div>
    <div>
      <span :class="{ red: redtext }" @click="togglered" @keyup.enter="togglered">{{
        message
      }}</span>
    </div>
    <div>
      <span @click="alternate" :style="{ color: textcolor }" @keyup.enter="alternate">{{
        message
      }}</span>
    </div>
  </main>
</template>

<style scoped>
header,
main {
  text-align: center;
}

.red {
  color: red;
}
</style>
