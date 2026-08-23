<script setup>
import { usePlayerStore } from '../stores/player';

    const props= defineProps({
        title: {type:String, required: true},
        artistName:{type:String, required: true},
        coverUrl:{type:String, default:''}
    })
    const player= usePlayerStore()

    function handleClick(){
        player.playSong({
            title: props.title,
            artistName:props.artistName,
            coverUrl:props.coverUrl
        })
    }
</script>

<template>
    <div class="song-card" @click="handleClick">
        <img :src="coverUrl" alt="" class="cover"/>
        <div class="info">
            <p class="title">{{ title }}</p>
            <p class="artist">{{ artistName }}</p>
        </div>
    </div>
</template>

<style scoped>
    .song-card{
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px;
        border-radius: 6px;
        cursor: pointer;
    }
    .song-card:hover{
        background: #282828;
    }
    .cover{
        width: 48px;
        height: 48px;
        border-radius: 4px;
        background: #333;
        object-fit: cover;
    }
    .title{
        font-size: 14px;
        font-weight: 500;
    }
    .artist{
        font-size: 12px;
        color: #b3b3b3;
    }
</style>