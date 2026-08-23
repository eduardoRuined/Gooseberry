<script setup>
import { RouterLink, RouterView } from 'vue-router';
import PlayerBar from './components/PlayerBar.vue';
</script>

<template>
  <div id="app">
    <nav>
      <RouterLink to="/">Inicio</RouterLink>
      <RouterLink to="/search">Buscar</RouterLink>
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
  }
  nav{
    display: flex;
    gap: 16px;
    margin-bottom: 24px;
  }
  nav a{
    color: #b3b3b3;
    text-decoration: none;
    font-weight: 600;
  }
  nav a.router-link-active{
    color: #ffffff;
  }
</style>