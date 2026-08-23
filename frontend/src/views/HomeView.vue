<script setup>
    import SongCard from '../components/SongCard.vue'
    import AlbumCard from '../components/AlbumCard.vue'
</script>

<template>
    <div>
        <h1>Inicio</h1>

        <h2>Canciones</h2>
        <SongCard title="For Honor! For Toussaint!" artistName="Marcin Przybylowicz"/>
        <SongCard title="The Trial" artistName="Marcin Przybylowicz"/>

        <h2>Álbumes</h2>
        <AlbumCard title="The Witcher 3: The Wild Hunt(OST)" artistName="Marcin Przybylowicz"/>
    </div>
</template>