import { ref } from 'vue';

export const habitlist = ref([
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

export default habitlist;
