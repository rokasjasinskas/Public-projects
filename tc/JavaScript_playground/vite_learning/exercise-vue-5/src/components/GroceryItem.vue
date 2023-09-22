<script setup>
import { defineProps } from 'vue';

// eslint-disable-next-line no-unused-vars
const props = defineProps({
  // eslint-disable-next-line vue/require-default-prop
  item: Object
});
</script>

<template>
  <li>
    {{ item.text }}
  </li>
</template>
