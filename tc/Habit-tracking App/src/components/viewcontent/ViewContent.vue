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
  <div class="view-content span-4-cells">
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
.span-4-cells {
  grid-row: span 4;
}

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
