<template>
    <div class="propriety_data">
        <div class="propriety_data--name">
        <p>{{propriety_name}}</p>
        </div>
        <div>
        <p>{{ propriety_value }}</p>
        </div>
    </div>
</template>
<style>
.propriety_data{
    display: flex;
    gap: 0.2rem;
    line-height: 0rem;
}
</style>
<script>
    export default {
        props:{
            propriety_value:{
                type:String,
                default : "undefined"
            },
            propriety_name:{
                type:String,
                default:"No name Prop"
            }
        
        },
        setup(){
            return {
            }
        }

    }
</script>