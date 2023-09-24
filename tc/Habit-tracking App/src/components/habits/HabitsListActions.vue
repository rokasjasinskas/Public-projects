<!-- eslint-disable vue/require-default-prop -->
<script setup>
import { defineProps, defineEmits, ref } from 'vue';

const props = defineProps({
  habitlist: Object
});
const headerClicked = ref(false);

const emit = defineEmits(['header-habit-clicked']);

const handleHeaderClick = () => {
  headerClicked.value = !headerClicked.value;
  emit('header-habit-clicked', props.habitlist);

  setTimeout(() => {
    headerClicked.value = false;
  }, 300);
};
</script>

<template>
  <h3
    @click="handleHeaderClick"
    @keydown.enter="handleHeaderClick"
    :class="{ clicked: headerClicked }"
    class="habits-header"
  >
    Habits
  </h3>
</template>

<style scoped>
.habits-header {
  cursor: pointer;
  padding: 5px;
  transition: rgb(175 167 167) 0.1s ease;
}

.habits-header:hover {
  color: rgb(0 0 0 / 50%);
}

.habits-header.clicked {
  background-color: rgb(175 167 167);
  border-radius: 5px;
  color: rgb(0 0 0);
}
</style>
