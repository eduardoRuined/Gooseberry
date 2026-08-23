import { defineStore } from "pinia";
import { ref } from "vue";

export const usePlayerStore= defineStore('player',()=>{
    const currentSong= ref(null)
    const isPlaying= ref(false)
    const queue= ref([])

    function playSong(song){
        currentSong.value=song
        isPlaying.value=true
    }

    function togglePlay(){
        isPlaying.value=!isPlaying.value
    }

    function pause(){
        isPlaying.value=false
    }
    return{
        currentSong,
        isPlaying,
        queue,
        playSong,
        togglePlay,
        pause
    }
})