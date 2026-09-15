# 🍇 Gooseberry — Identidad de Marca

## Origen del nombre

Gooseberry toma su nombre de un detalle literario: un personaje que siempre huele a "lilas y grosellas" — una combinación de aroma floral y frutal, suave y ácido a la vez. Esa dualidad es la base de la identidad visual y de tono de la aplicación: cálida pero con carácter, orgánica pero con un punto distintivo.

## Paleta de colores

| Token CSS | Hex | Nombre | Uso principal |
|---|---|---|---|
| `--lilac` | `#B4A0C4` | Lila | Acentos florales, hover states, texto secundario destacado |
| `--berry` | `#7D3C5C` | Grosella | Color principal de marca, botones activos, elementos de acción primaria |
| `--moss` | `#5C7A4F` | Musgo | Acentos secundarios, estados de éxito/confirmación |
| `--amber` | `#D9A441` | Ámbar | Highlights, favoritos, elementos interactivos destacados |
| `--cream` | `#F2E9DC` | Crema | Texto claro sobre fondo oscuro |
| `--bg-dark` | `#221D1A` | Fondo principal | Base de toda la interfaz — marrón muy oscuro, no negro puro |
| `--bg-elevated` | `#2E2723` | Superficie elevada | Tarjetas, paneles, elementos por encima del fondo |

**Por qué no negro puro:** el `#121212` que usa la mayoría de apps de streaming se siente frío y corporativo. Un marrón muy oscuro mantiene la legibilidad del modo oscuro pero se siente más cálido y orgánico, coherente con la identidad de Gooseberry.

## Tipografía

- **Encabezados / títulos:** [Fraunces](https://fonts.google.com/specimen/Fraunces) — serif cálida con carácter, disponible en Google Fonts
- **Cuerpo de texto / UI:** [Inter](https://fonts.google.com/specimen/Inter) o Work Sans — sans-serif limpia y legible

El contraste entre una serif con personalidad y una sans neutra es intencional: le da a Gooseberry un toque "boutique" sin sacrificar legibilidad en textos largos (nombres de canciones, artistas, etc.)

## Tono de voz

La interfaz debe sentirse cálida, cercana y con un toque poético — nunca corporativa ni genérica. Algunos principios:

- **Estados vacíos:** en vez de "No hay resultados", algo como "Nada por aquí todavía — prueba con otra búsqueda"
- **Errores:** honestos pero sin alarmar, ej. "Algo no salió como esperábamos, inténtalo de nuevo"
- **Confirmaciones:** breves y cálidas, ej. "Agregada a tu colección" en vez de "Favorito añadido exitosamente"

## Logo (concepto)

Pendiente de diseño final — dirección sugerida: una forma orgánica simple (silueta de grosella o una hoja/gota estilizada) en `--berry` o `--lilac`, combinada con el nombre en Fraunces.

## Aplicación en componentes existentes

Los siguientes componentes de la Fase 1 usan actualmente colores de Spotify (`#1db954`, `#121212`, `#b3b3b3`) y deben migrarse en la Semana 12:

- `PlayerBar.vue`
- `SongCard.vue`
- `AlbumCard.vue`
- `App.vue` (navegación)
- `LoginView.vue`
- `PlaylistView.vue`
- `SearchView.vue`
