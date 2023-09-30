<!-- eslint-disable import/no-unresolved -->
<script setup>
import HabitItem from '@/components/habits/HabitItem.vue';
import HabitsListActions from '@/components/habits/HabitsListActions.vue';
// eslint-disable-next-line import/extensions, import/no-unresolved
import { habitlist } from '@/data/habitlist';
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
