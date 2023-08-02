<script setup>
import { ref } from "vue";
import propriety from "./propriety.vue"
const nameT = "{{name}}"
const showArticle = ref(false);
const swapVisibility = () => {
  if (showArticle.value ){
    showArticle.value = false
  } else {
    showArticle.value = true
  }
}


</script>

<template>
  <div class="nametag">
    <div class="nametag__header">
      <p>{{ VoiceName }}</p>
      <button @click="swapVisibility">hide</button>
    </div>
  <div>
    <article v-show="showArticle" class="nametag__article">
     <section>
     <propriety :propriety_value="Data['voice']" propriety_name="Voice: "></propriety>
     <propriety :propriety_value="Data['prefix']" propriety_name="Prefix"></propriety>
     <propriety :propriety_value="Data['pitch']" propriety_name="Pitch"></propriety>
     <propriety :propriety_value="Data['rate']" propriety_name="Rate"></propriety>
     </section>
     <section><img src="@/assets/profilePIC.png" alt="profile pic"></section>
    </article>
  </div>

  </div>
</template>
<style>
  .nametag{
  background-color: bisque;
    display: flex;
    flex-direction: column;
  }
  .nametag__header{
    display: grid;
    grid-template-columns: repeat(2,1fr);
  }
  .nametag__header button{
    color: rgb(124, 80, 22);
    max-width: 50px;
  }
  .nametag__article{
    display: grid;
    grid-template-columns: 80% 20%;
    background-color: aquamarine;
  }
</style>
<script>
    export default {
        props:{
            VoiceName:{
                type:String,
                default : "Name"
            },
            Data:{
                type:Object,
                default:{}
            }
        
        },
        setup(){
          
            return {
              
            }
        }

    }
</script>