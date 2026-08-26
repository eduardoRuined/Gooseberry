<script setup>
    import { ref,onMounted } from 'vue';
    import api from '../services/api.js';
    import SongCard from '../components/SongCard.vue'
    import AlbumCard from '../components/AlbumCard.vue'

    const songs=ref([])
    const loading=ref(true)
    const error=ref(null)

    onMounted(async()=> {
        try{
            const response =await api.get('/songs/')
            songs.value=response.data
        }
        catch(err){
            error.value='No se pudieron cargar las canciones'
            console.error(err)
        }
        finally{loading.value=false}
    })
</script>

<template>
    <div>
        <h1>Inicio</h1>

        <h2>Canciones</h2>
        <p v-if="loading">Cargando...</p>
        <p v-else-if="error">{{ error }}</p>
        <SongCard v-else v-for="song in songs" 
            :key="song.id" 
            :title="song.title" 
            :artist-name="song.artist_name"
            :audio-url="song.audio_file"/>
    </div>
</template>