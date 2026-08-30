<script setup>
    import { ref, watch } from 'vue';
    import api from '../services/api';
    import SongCard from '../components/SongCard.vue';

    const query=ref('')
    const results=ref([])
    const searching=ref(false)

    let debounceTimer=null 

    watch(query,(newQuery)=>{
        clearTimeout(debounceTimer)
        if(!newQuery.trim()) {
            results.value=[]
            return
        }
        debounceTimer = setTimeout(async () => { 
            searching.value = true 
            try { 
                const response = await api.get('/songs/', { params: { search: newQuery } }) 
                results.value = response.data }
            catch(err){
                console.error(err)
            }finally{
                searching.value=false
            }
        },400)
    })
</script>

<template>
    <div>
        <h1>Buscar</h1>
        <input v-model="query" type="text" placeholder="Buscar canciones o artistas..." class="search-input"/>
        <p v-if="searching">Buscando...</p>
        <SongCard v-for="song in results" 
            :key="song.id"
            :song-id="song.id"
            :title="song.title"
            :artist-name="song.artist_name"
            :audio-url="song.stream_url"/>
    </div>
</template>

<style scoped>
    .search-input{
        width: 100%;
        padding: 12px;
        border-radius: 4px;
        border: 1px solid #333;
        background: #121212;
        color: #fff;
        margin: 16px 0 24px;
        box-sizing: border-box;
    }
</style>