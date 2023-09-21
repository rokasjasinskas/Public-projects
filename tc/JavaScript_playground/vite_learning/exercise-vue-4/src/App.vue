<script setup>
import { ref } from 'vue';

const newitem = ref('');
const newitempriority = ref('');
const newitemdropdown = ref('');
const singlecheckbox = ref();
const multiplecheckbox = ref([]);
const multipledropdown = ref([]);
</script>

<template>
  <header>
    <h1>Hello World!</h1>
  </header>

  <main>
    <div class="freetext">
      <h2>Heading of free text input paragraph</h2>
      <label>
        <p>Free text input explanation message:</p>
        <p><input v-model.lazy="newitem" type="text" placeholder="Add an item" /></p>
        <p>{{ newitem }}</p>
      </label>
    </div>
    <div class="single-checkbox">
      <h2>Heading of single single-checkbox paragraph</h2>
      <label>
        <p>Single check-box input explanation message:</p>
        <p><input v-model="singlecheckbox" type="checkbox" /></p>
        <p>{{ singlecheckbox }}</p>
      </label>
    </div>
    <div class="multiple-checkbox">
      <h2>Heading of single multiple-checkbox paragraph</h2>
      <label>
        <p>First</p>
        <p><input v-model="multiplecheckbox" type="checkbox" value="First" /></p>
      </label>
      <label>
        <p>Second</p>
        <p><input v-model="multiplecheckbox" type="checkbox" value="Second" /></p>
      </label>
      <label>
        <p>Third</p>
        <p><input v-model="multiplecheckbox" type="checkbox" value="Third" /></p>
      </label>
      <label>
        <p>Fourth</p>
        <p><input v-model="multiplecheckbox" type="checkbox" value="Fourth" /></p>
      </label>
      <p>{{ multiplecheckbox.join(', ') }}</p>
    </div>
    <div class="radio-buttons">
      <h2>Heading of radio buttons paragraph</h2>
      <p>Radio button explanation message:</p>
      <p>
        <label>
          Super Low
          <input v-model="newitempriority" type="radio" value="Super Low" />
        </label>
      </p>
      <p>
        <label>
          Low
          <input v-model="newitempriority" type="radio" value="Low" />
        </label>
      </p>
      <p>
        <label>
          High
          <input v-model="newitempriority" type="radio" value="High" />
        </label>
      </p>
      <p>
        <label>
          Super High
          <input v-model="newitempriority" type="radio" value="Super High" />
        </label>
      </p>
      <p>{{ newitempriority }}</p>
    </div>

    <div class="dropdown">
      <h2>Heading for dropdown input paragraph</h2>
      <label>
        <p>Dropdown explanation message:</p>
        <p>
          <select v-model="newitemdropdown">
            <option value="First">First</option>
            <option value="Second">Second</option>
            <option value="Third">Third</option>
            <option value="Fourth">Fourth</option>
          </select>
        </p>
      </label>
      {{ newitemdropdown }}
    </div>
    <div class="multiple-dropdown">
      <h2>Heading for multiple dropdown input paragraph</h2>
      <label>
        <p>Multiple dropdown explanation message:</p>
        <p>
          <select v-model="multipledropdown" multiple>
            <option value="First">First</option>
            <option value="Second">Second</option>
            <option value="Third">Third</option>
            <option value="Fourth">Fourth</option>
          </select>
        </p>
      </label>
      {{ multipledropdown.join(', ') }}
    </div>
  </main>
</template>

<style scoped>
header {
  text-align: center;
}
</style>
