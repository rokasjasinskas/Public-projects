<script setup>
import { defineProps, defineEmits } from 'vue';

// eslint-disable-next-line no-unused-vars
const props = defineProps({
  // eslint-disable-next-line vue/require-default-prop
  selectedHabit: Object
});
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
    <div v-else-if="showhabits"></div>
    <!-- Default content if nothins is selected -->
    <p v-else>View Content</p>
  </div>
</template>

<style scoped>
.span-4-cells {
  grid-row: span 4;
}
</style>
