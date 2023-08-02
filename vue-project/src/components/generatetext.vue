<template>
    <div class="container_generateAudios">
        <div >
            <textarea class="container_generateAudios--textarea" name="" id="" cols="30" rows="10"></textarea>
        </div>
        <div class="container_generateAudios--config">
            <a href="http://localhost:5000/api/getAudios">Download Audios</a>
            <p>status</p>
            <button>Generate</button>
        </div>
    </div>
</template>
<style>
.container_generateAudios{
    display: grid;
    grid-template-columns: repeat(2 ,1fr);
    gap:1rem;
}
.container_generateAudios--textarea{
    width: 100%;
    height: 100%;
    background-color: rgb(255, 255, 255);
    resize:none;
}
</style>