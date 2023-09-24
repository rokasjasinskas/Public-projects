<script setup>
import { defineProps } from 'vue';
// eslint-disable-next-line import/no-unresolved
import HabitItem from '@/components/habits/HabitItem.vue';

// eslint-disable-next-line no-unused-vars
const props = defineProps({
  // eslint-disable-next-line vue/require-default-prop
  habitList: Object
});
const emit = defineEmits(['habit-clicked']);
const handleHabitClick = habit => {
  emit('habit-clicked', habit);
};
</script>

<template>
  <h2>Current habits:</h2>
  <ul class="habits-list">
    <HabitItem
      v-for="item in habitList"
      :key="item.id"
      :item="item"
      @habit-clicked="handleHabitClick"
    />
  </ul>
</template>

<style scoped>
h2 {
  font-weight: bold;
}

.habits-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 1px;
}
</style>
