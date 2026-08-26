<script setup>
    import {ref, watch} from 'vue' 
    import { usePlayerStore } from '../stores/player';
    const player= usePlayerStore()
    const audioRef=ref(null)
    const currentTime=ref(0)
    const duration=ref(0)
    watch(()=> player.currentSong,(newSong)=>{
        if(newSong && audioRef.value){
            audioRef.value.src=newSong.audioUrl
            audioRef.value.play()
        }
    })
    watch(()=>player.isPlaying,(playing)=>{
        if(!audioRef.value)
            return 
        if(playing){
            audioRef.value.play()
        }
        else{
            audioRef.value.pause()
        }
    })
    function onTimeUpdate(){
        currentTime.value= audioRef.value.currentTime
        duration.value=audioRef.value.duration || 0 
    }
    function seek(event){
        const newTime= Number(event.target.value)
        audioRef.value.currentTime=newTime
        currentTime.value=newTime
    }
    function formatTime(seconds) { 
        if (!seconds || isNaN(seconds)) 
            return '0:00' 
        const mins = Math.floor(seconds / 60) 
        const secs = Math.floor(seconds % 60) 
        return `${mins}:${secs.toString().padStart(2, '0')}` 
    } 
</script>

<template>
    <div class="player-bar">
        <audio ref="audioRef" @timeupdate="onTimeUpdate" @loadedmetadata="onTimeUpdate"></audio>
        <div v-if="player.currentSong" class="song-info">
            <p class="title">{{ player.currentSong.title }}</p>
            <p class="artist">{{ player.currentSong.artistName }}</p>
        </div>
        <div v-else>
            <p class="empty">Ninguna canción reproduciondose</p>
        </div>
        <div class="controls">
            <button @click="player.togglePlay()">{{ player.isPlaying?'Pausar':'Reproducir'}}</button>
            <div class="progress">
                <span>{{ formatTime(currentTime) }}</span>
                <input type="range" min="0" :max="duration" :value="currentTime" @input="seek"/>
                <span>{{ formatTime(duration) }}</span>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .player-bar{
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #181818;
        border-top: 1px solid #282828;
        padding: 16px 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .title{
        font-size: 14px;
        font-weight: 600;
    }
    .artist{
        font-size: 12px;
        color: #b3b3b3;
    }
    .empty{
        color: #b3b3b3;
        font-size: 14px;
    }
    button{
        background: #1db954;
        color: #000;
        border: none;
        border-radius: 20px;
        padding: 8px 20px;
        font-weight: 600;
        cursor: pointer;
    }
    .controls{
        display: flex;
        align-items: center;
        gap: 16px;
        flex: 1;
        margin-left: 24px;
    }
    .progress{
        display: flex;
        align-items: center;
        gap: 8px;
        flex: 1;
        font-size: 12px;
        color: #b3b3b3;
    }
    .progress input[type='range']{
        flex: 1;
        accent-color: #1db954;
    }
</style>