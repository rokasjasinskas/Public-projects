<!-- eslint-disable vue/require-default-prop -->
<script setup>
import { defineProps, defineEmits, ref } from 'vue';

const props = defineProps({
  item: Object
});
const itemClicked = ref(false);

const emit = defineEmits(['habit-clicked']);

const handleClick = () => {
  itemClicked.value = !itemClicked.value;
  emit('habit-clicked', props.item);

  setTimeout(() => {
    itemClicked.value = false;
  }, 300);
};
</script>

<template>
  <li
    @click="handleClick"
    @keydown.enter="handleClick"
    class="clickable-item"
    :class="{ clicked: itemClicked }"
  >
    {{ item.title }}
  </li>
</template>

<style scoped>
.clickable-item {
  cursor: pointer;
  padding: 5px;
  transition: rgb(175 167 167) 0.1s ease;

  /* Add a hover effect for better UX */
}

.clickable-item:hover {
  font-weight: bold;
}

.clickable-item.clicked {
  background-color: rgb(175 167 167);
  border-radius: 5px;
}
</style>
