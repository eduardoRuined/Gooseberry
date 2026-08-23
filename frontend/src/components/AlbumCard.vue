<script setup>
    defineProps({title: { type: String, required: true }, artistName: { type: String, required: true }, coverUrl: { type: String, default: '' }})
</script>

<template>
    <div class="album-card">
        <img :src="coverUrl" alt="" class="cover"/>
        <p class="title">{{ title }}</p>
        <p class="artist">{{ artistName }}</p>
    </div>
</template>

<style scoped>
    .album-card{
        width: 160px;
        padding: 12px;
        border-radius: 8px;
        cursor: pointer;
    }
    .album-card:hover{
        background: #282828;
    }
    .cover{
        width: 100%;
        aspect-ratio: 1;
        border-radius: 6px;
        background: #333;
        object-fit: cover;
        margin-bottom: 12px;
    }
    .title{
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 4px;
    }
    .artist{
        font-size: 12px;
        color: #b3b3b3;
    }
</style>