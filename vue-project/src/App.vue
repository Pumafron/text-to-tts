<template>
  <header class="header">
    <h1>app text to tts</h1>
  </header>
  <main class="content">
    <div>
      <h2>config and text area</h2>
      <generateText/>
      <config/>
    </div>
    <div>
      <h2>avalaibleVoices</h2>
      <voice v-for="i, index in Object.keys(example_obj)" :key="index" :VoiceName="i" :Data="example_obj[i]"></voice>
    </div>
  </main>
</template>
<style>
.content {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}

.header {
  text-align: center;
}
</style>

<script setup>
import { ref,onMounted } from "vue";
import axios from 'axios';
import voice from "./components/voice.vue"
import generateText from "./components/generatetext.vue"
import config from "./components/config.vue"
const example_obj = ref({});
async function fetchData() {
  try {
    const response = await axios.get('http://localhost:5000/api/getVoicesAvalaible');
    example_obj.value = response.data;
  } catch (error) {
    console.error('Error en la solicitud: ', error);
  }
}

// Llama a la función para obtener los datos cuando el componente se monte
onMounted(() => {
  fetchData();
});
</script>