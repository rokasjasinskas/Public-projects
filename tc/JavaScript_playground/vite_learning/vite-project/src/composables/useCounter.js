import { ref } from "vue";

export function useCounter() {
  const counter = ref(0);
  const setCount = (number) => {
    counter.value += number;
  };
  return { counter, setCount };
}
