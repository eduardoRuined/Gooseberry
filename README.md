<div align="center">

# Gooseberry

Pequeña aplicación de música usada para el entretenimiento 

Proyecto personal — **Eduardo Hernández Contreras** — 2026

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=#3776AB)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django&logoColor=#092E20)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-red?logo=django&logoColor=#00529B)](https://www.django-rest-framework.org/)
[![Vue](https://img.shields.io/badge/Vue.js-3-4FC08D?logo=vue.js&logoColor=#4FC08D)](https://vuejs.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-4169E1?logo=postgresql&logoColor=#4169E1)](https://www.postgresql.org/)
[![Node.js](https://img.shields.io/badge/Node.js-18+-339933?logo=node.js&logoColor=#5FA04E)](https://nodejs.org/)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=#F03C2E)](https://git-scm.com/)

</div>

## Progreso del desarrollo

### Semana 0 — Setup inicial 
- Repositorio configurado con estructura backend/frontend
- Flujo de Git con ramas por feature

### Semana 1 — Fundamentos de Django 
- Proyecto Django creado con app `music`
- Django REST Framework configurado
- Entorno virtual y `requirements.txt` documentado   

### Semana 2 — Modelos y base de datos
- Modelos Artist, Album, Song, Playlist y Favorite creadas con sus relaciones ForeignKey y ManyToMany
- Creacion y configuración del SuperUsuario para el panel de Django
- Migraciones aplicadas coorectamente sobre SQLite
- Inserción de datos de prueba en Django Administration

### Semana 3 — API REST con Django REST Framework
- Serializers, ViewSets y Router configurados para los 5 modelos
- Endpoints CRUD funcionando: /api/songs/, /api/artists/, /api/albums/, /api/playlists/, /api/favorites/
- Relaciones anidadas en SongSerializer para mostrar nombre de artista y album sin peticiones exta 

### Semana 4 — Autenticación
- JWT configurado con djangorestframework-simplejwt
- Endpoints de registro y login funcionando
- Permisos personalizados: solo el dueño de una playlist puede editarla o borrarla
- Owner asignado automáticamente al crear playlists mediante perform_create

### Semana 5 — Fundamentos de Vue 3
- Proyecto Vue 3 + Vite inicializado en frontend/
- Extensión Vue - Official configurada en VS Code
- Componentes SongCard y AlbumCard creados con props tipadas

### Semana 6 — Ruteo y estado global
- Vue Router configurado con rutas Home y Search
- Store de Pinia(usePlayerStore) para el estado global del reproductor
- PlayerBar conectando al store, persiste su estado al navegar entre vistas 

 ### Semana 7 -- Conectando frontend y backend 
 - CORS configurado para permitir peticiones desde Vue (localhost:5173) 
 - Cliente Axios centralizado con interceptor de token JWT 
 - Canciones reales cargadas desde la API en HomeView 
 - Reproductor de audio funcional (play, pausa, barra de progreso, seek) sincronizado con el store de Pinia 
 - Archivos de audio servidos correctamente en desarrollo via MEDIA_URL

 ### Semana 8 -- Playlists, favoritos y busqueda 
 - Login funcional desde el frontend con store de autenticacion (Pinia)
 - CRUD de playlists: crear, listar y eliminar desde la interfaz 
 - Sistema de favoritos con sincronizacion real entre frontend y backend (endpoint /favorites/check/)  
 - Busqueda de canciones con debounce, usando SearchFilter de Django REST Framework 
 - Resueltos varios bugs de sincronizacion de estado y permisos por usuario

 ### Semana 9 -- Pulido tecnico
 - HTTP Range requests implementado para streaming real de audio (permite avanzar/retroceder sin reiniciar la cancion)
 -  Suite de tests automatizados con APITestCase: cobertura de endpoints publicos, busqueda, y permisos de playlists
 - Diseno responsive para PlayerBar y navegacion en pantallas moviles   
 - Tema oscuro fijo (por decision de diseno, sin alternador claro/oscuro)