<script setup>
import { ref } from 'vue';
import { usePlayerStore } from '../stores/player';
import api from '../services/api';

    const props= defineProps({
            songId:{type:Number, required:true}, 
            title:{type:String, required:true}, 
            artistName:{type:String,required:true},
            coverUrl:{type:String, default:""},
            audioUrl:{type:String, required:true},
            isFavorite:{type:Boolean, required:false} 
        })
    const emit=defineEmits(['favorite-toggled'])

    const player= usePlayerStore()
    const favorited=ref(props.isFavorite)
    const loadingFavorite=ref(false)

    function handleClick(){
        player.playSong({
            title:props.title,
            artistName:props.artistName,
            coverUrl:props.coverUrl,
            audioUrl:props.audioUrl
        })
    }
    async function toggleFavorite(event) {
        event.stopPropagation()
        if(loadingFavorite.value) return
        loadingFavorite.value=true
        try{
            if(favorited.value){
                await api.delete(`/favorites/remove/${props.songId}/`)
            }else{
                await api.post('/favorites/', {song:props.songId})
            }
            favorited.value=!favorited.value
            emit('favorite-toggled')
       }catch(err){
        console.error(err)
       }finally{
        loadingFavorite.value=false
       }
        
    }
</script>

<template>
    <div class="song-card" @click="handleClick">
        <img :src="coverUrl" alt="" class="cover"/>
        <div class="info">
            <p class="title">{{ title }}</p>
            <p class="artist">{{ artistName }}</p>
        </div>
        <button class="favorite-btn" @click="toggleFavorite" :disabled="loadingFavorite">
            {{ favorited ? '♥' : '♡' }}
        </button>
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
        justify-content: space-between;
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
    .favorite-btn{
        background: none;
        border: none;
        color: #b3b3b3;
        font-size: 20px;
        cursor: pointer;
        padding: 4px 8px;
    }
    .favorite-btn:hover{
        color: #1db954;
    }
</style>