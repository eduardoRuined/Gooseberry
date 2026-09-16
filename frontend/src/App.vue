<script setup>
import { RouterLink, RouterView } from 'vue-router';
import PlayerBar from './components/PlayerBar.vue';
</script>

<template>
  <div id="app">
    <nav>
      <RouterLink to="/">Inicio</RouterLink>
      <RouterLink to="/search">Buscar</RouterLink>
      <RouterLink to="/login">Iniciar sesión</RouterLink>
      <RouterLink to="/playlists">Playlists</RouterLink>
    </nav>
    <main>
      <RouterView/>
    </main>
    <PlayerBar/>
  </div>
</template>

<style>
  #app{
    max-width: 900px;
    margin: 0 auto;
    padding: 24px;
    padding-bottom: 100px;
  }
  nav{
    display: flex;
    gap: 16px;
    margin-bottom: 24px;
  }
  nav a{
    color: var(--text-muted);
    text-decoration: none;
    font-weight: 600;
    font-family: var(--font-body);
  }
  nav a.router-link-active{
    color: var(--berry);
  }
  @media(max-width: 640px){
    #app{
      padding: 12px;
      padding-bottom: 100px;
    }
    nav{
      flex-wrap: wrap;
      gap: 12px;
    }
  }
</style>