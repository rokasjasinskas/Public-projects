<script setup>
// eslint-disable-next-line import/no-unresolved
import AppCalendar from '@/components/calendar/AppCalendar.vue';

const emit = defineEmits(['toggleCalendar']);
const toggleCalendarView = () => {
  emit('toggleCalendar');
};
</script>

<template>
  <div class="daily">
    <h3 @click="toggleCalendarView" @keydown.enter="toggleCalendarView">View calendar</h3>
    <AppCalendar v-if="showCalendar" :height="1000" />
  </div>
</template>

<style scoped>
h3 {
  font-weight: bold;
  cursor: pointer;
}
</style>
