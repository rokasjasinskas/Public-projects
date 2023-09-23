<!-- eslint-disable import/no-unresolved -->
<script setup>
// eslint-disable-next-line import/no-unresolved
import ViewContentHeader from '@/components/viewcontent/ViewContentHeader.vue';
import ViewContent from '@/components/viewcontent/ViewContent.vue';
import AppHeader from '@/components/appheader/AppHeader.vue';
import DailySection from '@/components/dailysection/DailySection.vue';
import MonthlySection from '@/components/monthlysection/MonthlySection.vue';
import HabitsList from '@/components/habits/HabitsList.vue';
</script>

<template>
  <div class="app-container">
    <AppHeader />
    <main>
      <div class="container">
        <DailySection />
        <ViewContentHeader />
        <MonthlySection />
        <ViewContent />
        <HabitsList />
        <div>Emty1</div>
        <div>Emty2</div>
      </div>
    </main>
  </div>
</template>

<style scoped>
header {
  text-align: center;
}

/* Made app.container to cover background header and footer as well */
.app-container {
  position: relative;
  min-height: 100vh;
}

.app-container::before {
  content: '';
  position: absolute;
  inset: 0;
  background: url('@/assets/images/background.jpg');
  filter: blur(20px);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: -1;
}

main {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr;
  justify-items: center;
  align-items: center;
  font-family: sans-serif;
}

.container {
  display: grid;
  grid-template-columns: 30% 70%;
  grid-template-rows: repeat(5, 1fr);
  padding: 10px;
  border-radius: 10px;
  margin-top: 40px;
  height: 80vh;
  width: 90vw;
  align-items: stretch;
  justify-items: stretch;
  grid-gap: 5px;
  box-sizing: border-box;
  background-color: rgb(241 240 240);
  opacity: 0.8;
}

.container > div {
  border: 2px solid gray;
  box-sizing: border-box;
  margin: 0;
  display: grid;
  align-items: top;
  justify-content: left;
  max-width: 100%;
  max-height: 100%;
  padding: 5px;
}

@media (width >= 768px) {
  .container {
    height: 60vh;
    width: 60vw;
  }
}

@media (width >= 1024px) {
  .container {
    height: 50vh;
    width: 50vw;
  }
}
</style>
