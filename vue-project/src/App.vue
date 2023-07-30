<script setup>
  import {ref} from "vue";
  import voice from "./components/voice.vue"
</script>
<template>
  <header class="header">
    <h1>app text to tts</h1>
  </header>
  <main class="content">
    <div>
      <h2>config and text area</h2>
    </div>
    <div>
      <h2>avalaibleVoices</h2>
      <voice></voice>
      <voice></voice>
      <voice></voice>
      <voice></voice>
      <voice></voice>
      <voice></voice>
      <voice></voice>
    </div>
  </main>
</template>
<style>
  .content{
    display: grid;
    grid-template-columns: repeat(2,1fr);
  }
  .header{
    text-align: center;
  }
</style>