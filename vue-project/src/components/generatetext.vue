<template>
    <div class="container_generateAudios">
        <div>
            <textarea v-model="textarea_String" class="container_generateAudios--textarea" name="" id="" cols="30"
                rows="10"></textarea>
        </div>
        <div class="container_generateAudios--config">
            <a href="http://localhost:5000/api/getAudios">Download Audios</a>
            <p>{{ status }}</p>
            <button @click="GenerateAudios">Generate</button>
        </div>
    </div>
</template>
<script setup>
import { ref } from 'vue';
import axios from 'axios';

const textarea_String = ref("")
const status = ref("redy")

const GenerateAudios = async () => {
    console.log(textarea_String.value);
    status.value = "generating";
    try {
        let headersList = {
            "Content-Type": "application/json"
        }

        let bodyContent = JSON.stringify({
            "contenttext": textarea_String.value.toString()
        });
        
        let reqOptions = {
            url: "http://localhost:5000/api/generate",
            method: "POST",
            headers: headersList,
            data: bodyContent,
        }

        let response = await axios.request(reqOptions);
        console.log(response.data);
        status.value = "ready";
    } catch (error) {
        console.error('Error en la solicitud:', error);
        status.value = error;
        alert(error);
    }
}
</script>
<style>
.container_generateAudios {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
}

.container_generateAudios--textarea {
    width: 100%;
    height: 100%;
    background-color: rgb(255, 255, 255);
    resize: none;
}
</style>