<script setup></script>

<template>
  <div class="app-container">
    <header>
      <h1>Hello World!</h1>
    </header>

    <main>
      <div class="container">
        <div class="daily"><h3>Daily</h3></div>
        <div class="view-header"><h3>View Header</h3></div>
        <div class="monthly"><h3>Monthly</h3></div>
        <div class="placeholder span-4-cells"><p>View Content</p></div>
        <div class="habits">
          <h3 class="habits-header">HABITS:</h3>
          <div class="habits-item">Habit Name</div>
          <div class="habits-item">Habit Name</div>
          <div class="habits-item">Habit Name</div>
          <div class="habits-item">Habit Name</div>
        </div>
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

/* made this to cover background header and footer as well */
.app-container {
  position: relative;
  min-height: 100vh;
}

.app-container::before {
  content: ''; /* Essential for the pseudo-element to show */
  position: absolute; /* Absolute positioning */
  inset: 0; /* Cover the entire parent element */
  background: url('@/components/pictures/background.jpg');
  filter: blur(20px);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: -1; /* Place it behind the content of .app-container */
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

.span-4-cells {
  grid-row: span 4;
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
