<script setup>
    import {ref, onMounted} from  'vue'
    import api from '../services/api';

    const playlists= ref([])
    const newPlaylistName=ref('')
    const loading= ref(true)
    const creating=ref(false)

    async function loadPlaylist() {
        loading.value=true
        try{
            const response= await api.get('/playlists/')
            playlists.value=response.data
        }
        catch(err){
            console.error(err)
        }finally{
            loading.value=false
        }
    }
    async function createPlaylist() {
        if(!newPlaylistName.value.trim()) return 
        creating.value=true
        try{
            await api.post('/playlists/',{name:newPlaylistName.value})
            newPlaylistName.value = '' 
            await loadPlaylist()  
        }
        catch(err){
            console.error(err)
        }finally{
            creating.value=false
        }
    }
    async function deletePlaylist(id) {
        try{
            await api.delete(`/playlists/${id}/`)
            await loadPlaylist()
        }
        catch(err){
            console.error(err)
        }
    }   
    onMounted(loadPlaylist)
</script>

<template>
    <div>
        <h1>Tus Playlists</h1>
        <form @submit.prevent="createPlaylist" class="new-playlist">
            <input v-model="newPlaylistName" type="text" placeholder="Nombre de la nueva playlist"/>
            <button type="submit" :disabled="creating">Crear</button>
        </form>
        <p v-if="loading">Cargando...</p>
        <p v-else-if="playlists.length===0">Aún no tienes playlists</p>
        <ul v-else class="playlist-list">
            <li v-for="playlist in playlists" :key="playlist.id" class="playlist-item">
                <span>{{ playlist.name }}</span>
                <span class="count">{{ playlist.songs.length }} canciones</span>
                <button class="delete-btn" @click="deletePlaylist(playlist.id)">Eliminar</button>
            </li>
        </ul>
    </div>
</template>

<style scoped>
    .new-playlist{
        display: flex;
        gap: 8px;
        margin: 16px 0 24px;
    }
    .new-playlist input{
        flex: 1;
        padding: 10px;
        border-radius: 4px;
        border: 1px solid #333;
        background: #121212;
        color: #fff;
    }
    .new-playlist button{
        background: #1db954;
        color: #000;
        border: none;
        border-radius: 20px;
        padding: 10px 20px;
        font-weight: 600;
        cursor: pointer;
    }
    .playlist-list{
        list-style: none;
        padding: 0;
    }
    .playlist-item{
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 12px 8px;
        border-bottom: 1px solid #282828;
    }
    .count{
        color: #b3b3b3;
        font-size: 13px;
        flex: 1;
    }
    .delete-btn{
        background: none;
        border: 1px solid #b3b3b3;
        color: #b3b3b3;
        border-radius: 16px;
        padding: 4px 12px;
        cursor: pointer;
        font-size: 12px;
    }
    .delete-btn:hover{
        border-color: #f15e6c;
        color: #f15e6c;
    }
</style>