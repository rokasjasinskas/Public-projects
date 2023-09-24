<script setup>
import { defineProps } from 'vue';
// eslint-disable-next-line import/no-unresolved
import HabitViewList from '@/components/habits/HabitViewList.vue';

// eslint-disable-next-line no-unused-vars
const props = defineProps({
  // eslint-disable-next-line vue/require-default-prop
  selectedHabit: Object,
  // eslint-disable-next-line vue/require-default-prop
  habitList: Object
});
const emit = defineEmits(['habit-clicked']);
const handleHabitClick = habit => {
  emit('habit-clicked', habit);
};
</script>

<template>
  <div class="view-content span-cells">
    <!-- Check if there's a selected habit -->
    <div v-if="selectedHabit">
      <h2>{{ selectedHabit.title }}</h2>
      <p>{{ selectedHabit.description }}</p>
      <p v-if="selectedHabit.startdate">Start Date: {{ selectedHabit.startdate }}</p>
      <p v-if="selectedHabit.enddate">End Date: {{ selectedHabit.enddate }}</p>
      <p>Repeat: {{ selectedHabit.repeat ? 'Yes' : 'No' }}</p>
    </div>
    <!-- Check if there's a habit header is selected -->
    <div v-else-if="habitList">
      <HabitViewList @habit-clicked="handleHabitClick" :habitList="habitList" />
    </div>
    <!-- Default content if nothins is selected -->
    <p v-else>View Content</p>
  </div>
</template>

<style scoped>
.span-cells {
  grid-row: span 5;
  grid-column: span 0;
}

h2 {
  font-weight: bold;
}
</style>
