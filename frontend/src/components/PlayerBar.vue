<script setup>
    import { usePlayerStore } from '../stores/player';
    const player= usePlayerStore()
</script>

<template>
    <div class="player-bar">
        <div v-if="player.currentSong">
            <p class="title">{{ player.currentSong.title }}</p>
            <p class="artist">{{ player.currentSong.artistName }}</p>
        </div>
        <div v-else>
            <p class="empty">Ninguna canción reproduciondose</p>
        </div>
        <button @click="player.togglePlay()">{{ player.isPlaying?'Pausar':'Reproducir'}}</button>
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
        display: felx;
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
</style>