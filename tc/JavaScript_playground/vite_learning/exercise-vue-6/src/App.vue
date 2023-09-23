<script setup>
import { ref, computed } from 'vue';
import { marked } from 'marked';

const markdowntext = ref('');
const renderedmarkdown = computed(() => {
  const htmlOutput = marked(markdowntext.value);
  return htmlOutput;
});
</script>

<template>
  <header>
    <h1>Hello World!</h1>
  </header>

  <main>
    <div class="area">
      <div class="left">
        <label for="markdownEditor">Markdown Editor placeholder</label>
        <textarea
          v-model="markdowntext"
          class="markdownText"
          placeholder="Type your markdown here..."
        >
        </textarea>
      </div>
      <div class="right" v-html="renderedmarkdown"></div>
    </div>
  </main>
</template>

<style scoped>
header {
  text-align: center;
}

.area {
  display: grid;
  grid-template-columns: 1fr 1fr;
  height: 90vh;
  padding: 10px;
}

.left {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 0 1fr; /* hiddes label name */
  border: 1px solid #ccc;
  background-color: #f9f9f9;
}

.right {
  white-space: normal;
  background-color: #f9f9f9;
  overflow-y: auto;
  padding: 10px;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

.right:hover {
  background-color: #fff;
}

.left:hover,
textarea:hover {
  background-color: #fff;
}

/* stylelint-disable-next-line no-descending-specificity */
textarea {
  width: 100%;
  height: 100%;
  margin: 0;
  border: none;
  resize: none;
  outline: none;
  box-sizing: border-box;
  font-family: monospace;
  background-color: #f9f9f9;
  padding: 10px;
}
</style>
