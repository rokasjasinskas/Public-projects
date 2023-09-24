<script setup>
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';
import { computed } from 'vue';

function handleDateClick(arg) {
  alert(`Date clicked! ${arg.dateStr}`);

  const habitsDoneToday = habitsData.value.filter(habit =>
    habit.completedDates.includes(arg.dateStr)
  );
  // Here, you can display habitsDoneToday somewhere or allow marking other habits as done
  // For this example, just log them
  console.log('Habits done on', arg.dateStr, habitsDoneToday);
}

const calendarOptions = computed(() => ({
  plugins: [dayGridPlugin, interactionPlugin],
  initialView: 'dayGridMonth',
  dateClick: handleDateClick,
  height: 'auto', // So it would be possible adjust from style part with css
  width: 'auto', // So it would be possible adjust from style part with css
  headerToolbar: {
    start: 'prev,next today', // buttons on the left
    center: 'title', // title in the center
    end: 'dayGridMonth,dayGridWeek,dayGridDay' // buttons on the right
  },
  events: [
    { title: 'event 1', date: '2023-09-24' },
    { title: 'event 2', date: '2023-09-23' }
  ]
}));
</script>
<template>
  <div class="calendar-container">
    <FullCalendar :options="calendarOptions" />
  </div>
</template>

<style scoped>
.calendar-container {
  width: 150px;
  height: 480px;
  overflow: scroll; /* To ensure content doesn't overflow */
}

@media (width >= 360px) {
  .calendar-container {
    width: 210px;
    height: 480px;
  }
}

@media (width >= 412px) {
  .calendar-container {
    width: 210px;
    height: 610px;
  }
}

@media (width >= 768px) {
  .calendar-container {
    width: 430px;
    height: 650px;
  }
}

@media (width >= 820px) {
  .calendar-container {
    width: 450px;
    height: 650px;
  }
}

@media (width >= 1024px) {
  .calendar-container {
    width: 600px;
  }
}

@media (width >= 1024px) {
  .calendar-container {
    width: 850px;
    height: 650px;
  }
}
</style>
