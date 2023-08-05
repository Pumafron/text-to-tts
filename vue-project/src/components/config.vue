<script setup>
import { ref,onMounted } from "vue";
import axios from 'axios';
const selected = ref("Pls select")
const name_voice = ref("")
const prefix_voice = ref("")
const pitch_voice = ref("")
const rate_voice = ref("")



const voiceLists = ref({});
async function fetchData() {
  try {
    const response = await axios.get('http://localhost:5000/api/getVoices');
    voiceLists.value = response.data;
  } catch (error) {
    console.error('Error en la solicitud:', error);
  }
}
onMounted(() => {
  fetchData();
});
</script>
<template>
    <div>
        <div>
            <h3>new Voice</h3>
        </div>
        <div class="config__form">
            <div class="config__form--options">
                <div>
                    <p>Select Voice</p>
                    <select v-model="selected">
                <option disabled value="">Please select one</option>
                    <option v-for="voice,index in voiceLists['SAPI 4:']" :key="index">{{ voice }}</option>
                    <option v-for="voice,index in voiceLists['SAPI 5:']" :key="index">{{ voice }}</option>
                </select>
                </div>
                <div>
                    <p>Prefix</p>
                    <input v-model="prefix_voice" placeholder="edit me" />
                </div>
                <div>
                    <p>Pitch</p>
                    <input v-model="pitch_voice" placeholder="edit me" />
                </div>
                <div>
                    <p>Rate</p>
                    <input v-model="rate_voice" placeholder="edit me" />
                </div>
                <div>
                    <p>Voice Name</p>
                    <input v-model="name_voice" placeholder="edit me" >
                </div>
                <div>
                    <button>send</button>
                </div>
            </div>
        </div>
    </div>
</template>
<style>
.formulario{
    display: flex;
    flex-direction: column;
}
.config__form--options div {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem
}
</style>