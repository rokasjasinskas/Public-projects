<!-- eslint-disable import/no-unresolved -->
<script setup>
import { ref } from 'vue';
import HabitItem from '@/components/habits/HabitItem.vue';
import HabitsListActions from '@/components/habits/HabitsListActions.vue';

const habitlist = ref([
  {
    id: 1,
    title: 'Reading',
    description: 'Reading books',
    repeat: false,
    completedDates: ['2023-09-24', '2023-09-23', '2023-09-22']
  },
  {
    id: 2,
    title: 'Exercise',
    description: 'Morning workout',
    repeat: true,
    completedDates: ['2023-09-24', '2023-09-23', '2023-09-22']
  },
  {
    id: 3,
    title: 'Meditation',
    description: 'Evening relaxation',
    repeat: true,
    completedDates: ['2023-09-24', '2023-09-23', '2023-09-22']
  },
  {
    id: 4,
    title: 'Journaling',
    description: 'Writing daily thoughts',
    repeat: false,
    completedDates: ['2023-09-24', '2023-09-23', '2023-09-22']
  },
  {
    id: 5,
    title: 'Learning',
    description: 'Studying a new topic',
    repeat: true,
    completedDates: ['2023-09-24', '2023-09-23', '2023-09-22']
  }
]);
</script>

<template>
  <div class="habits span-3-cells">
    <HabitsListActions
      :habitlist="habitlist"
      @header-habit-clicked="$emit('header-habit-clicked', $event)"
    />
    <ul class="habits-list">
      <HabitItem
        v-for="item in habitlist"
        :key="item.id"
        :item="item"
        @habit-clicked="$emit('habit-clicked', $event)"
      />
    </ul>
  </div>
</template>

<style scoped>
h3 {
  font-weight: bold;
}

.habits {
  display: grid;
  height: auto;
  overflow: auto;
  padding-right: 10px;
  grid-template-rows: auto 1fr 1fr 1fr 1fr;
}

.habits-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 2px;
}

.span-3-cells {
  grid-row: span 3;
}
</style>
