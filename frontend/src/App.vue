<script setup>
  import SongCard from './components/SongCard.vue';
  import AlbumCard from './components/AlbumCard.vue';
</script>

<template>
  <div id="app">
    <h1>Gooseberry</h1>
    <h2>Canciones</h2>
    <SongCard title="For Honor! For Toussaint!" artistName="Marcin Przybylowicz"/>
    <SongCard title="The Trial" artistName="Marcin Przybylowicz" />
    <h2>Albumes</h2>
    <AlbumCard title="The Witcher 3: The Wild Hunt(OST)" artistName="Marcin Przybylowicz"/>
  </div>
</template>

<style>
  #app{
    max-width: 600px;
    margin: 0 auto;
    padding: 24px;
  }
  h2{
    margin: 24px 0 12px;
    font-size: 18px;
  }
</style>