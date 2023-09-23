<!-- eslint-disable import/no-unresolved -->
<script setup>
import HabitItem from '@/components/habits/HabitItem.vue';
</script>

<template>
  <div class="habits">
    <h3 class="habits-header">HABITS:</h3>
    <HabitItem />
    <HabitItem />
    <HabitItem />
    <HabitItem />
    <HabitItem />
  </div>
</template>

<style scoped>
h3 {
  font-weight: bold;
}
</style>
