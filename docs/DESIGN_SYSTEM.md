# Sistema de Diseño — CineRadar

## Filosofía visual

> **LAS PELÍCULAS SON LAS PROTAGONISTAS. NO LAS NOTICIAS.**

El newsletter debe sentirse como Letterboxd, MUBI, IMDb, A24 o Netflix Editorial. **No** como un blog, un periódico, un email genérico ni un reporte corporativo. El lector debe sentir que recorre una revista digital de cine premium.

### Mood
Cinematográfico · premium · oscuro · elegante · inmersivo · moderno · visual · curado. Cada sección se siente como la siguiente escena de una película.

### Jerarquía visual
Las imágenes pesan más que el texto. **Proporción objetivo: 60% visual / 40% texto.** Cada sección mayor lleva un elemento visual fuerte. Se evita el muro de texto; el ritmo lo crean las imágenes.

## Paleta de color (inspirada en *Oppenheimer*)

Paleta vintage y cinematográfica que reemplaza al negro/rojo Netflix por tonos más cálidos y sofisticados.

| Rol | Hex | Nombre |
|-----|-----|--------|
| Fondo exterior | `#1A252C` | Azul pizarra profundo |
| Superficie | `#232E35` | Slate |
| Tarjetas | `#1C2830` | Card dark |
| Tarjetas (alt) | `#18232A` | Card alt |
| **Acento principal** | `#8B3A2F` | Burnt Russet |
| Acento principal (claro) | `#C47A6E` | Russet claro |
| **Acento secundario** | `#C4A84F` | Cork (dorado) |
| **Acento terciario** | `#7A9BAD` | Cloudy Sky |
| Verde (scores altos) | `#6B7B6E` | Sage / Rainy Afternoon |
| Texto primario | `#E8E0D0` | Revere Pewter |
| Texto secundario | `#C4BBA8` | Pewter medio |
| Texto terciario | `#A8A098` | Pewter apagado |
| Líneas / divisores | `rgba(196,187,168,0.09)` | — |

### Uso de los acentos
- **Russet** `#8B3A2F`: números de sección, badges, barra de marca.
- **Cork** `#C4A84F`: scores, "nuestra opinión", citas, detalles dorados.
- **Sky** `#7A9BAD`: etiquetas secundarias, surprise pick.
- **Scores RT:** verde sage (alto) · cork (medio) · russet (bajo). Nunca el verde/amarillo/rojo de semáforo.

## Tipografía

| Uso | Stack | Tamaño |
|-----|-------|--------|
| Títulos / display | `Impact, 'Bebas Neue', Oswald, sans-serif` | Hero 42–50px · Sección 17–19px · Titular 18–22px |
| Cuerpo | `Inter, Helvetica, Arial, sans-serif` | 13–18px |
| Citas | `Georgia, 'Times New Roman', serif` (cursiva) | 18px |
| Metadata | `Inter` | 9–14px, mayúsculas, letter-spacing amplio |

## Layout

- **Mobile-first**, columna única.
- **Ancho máximo: 600–620px.**
- Espaciado generoso, padding amplio.
- Imágenes responsivas, carga rápida.
- **Dark mode nativo.** Sin saturación visual.

## Reglas de imagen

### Siempre priorizar
Posters oficiales · stills oficiales · imágenes promocionales oficiales · artwork de alta resolución.

### Nunca usar
Imágenes con watermark · memes · fan art · stock genérico · headshots de ejecutivos (salvo que sean absolutamente relevantes).

### Formato correcto según el espacio (clave para no recortar mal)

| Espacio | Tipo de imagen | Fuente TMDB |
|---------|----------------|-------------|
| Hero / banner horizontal | **Backdrop 16:9** | `backdrop_path` |
| Banner de historia | **Backdrop 16:9** | `backdrop_path` |
| Poster sobrepuesto / Película de la semana | **Poster vertical** | `poster_path` |
| Miniaturas RT Tracker | **Poster vertical** | `poster_path` |
| Picks fin de semana | **Poster vertical** | `poster_path` |

> ⚠️ **No metas posters verticales en banners horizontales** — se recortan mal. Usa backdrops y céntralos con `object-position` para que el foco visual quede correcto.

### Obtener imágenes de TMDB (API pública)

```
# Datos de la película (incluye poster_path y backdrop_path)
https://api.themoviedb.org/3/movie/{ID}?api_key={KEY}

# Buscar por título
https://api.themoviedb.org/3/search/movie?api_key={KEY}&query={TITULO}&year={AÑO}

# Construir la URL final de imagen:
https://image.tmdb.org/t/p/{TAMAÑO}{poster_path}

# Tamaños útiles:
#   Posters:   w92 (miniatura) · w185 · w342 · w500
#   Backdrops: w780 · w1280 (banner/hero)
```

## Requisitos del HTML

- CSS interno únicamente.
- Estructura compatible con email; responsiva; mobile-first; segura en Outlook donde sea posible.
- Tema oscuro por defecto, espaciado optimizado, estructura semántica, código limpio.
- Listo para pegar en Mailchimp, Beehiiv, ConvertKit, Brevo, etc.
- **JS opcional:** efectos de scroll/animación solo si la edición es para navegador. Deben degradar limpio en email (sin romper el layout).

## Anatomía visual de las secciones

- **Hero:** backdrop a sangre completa con doble degradado, logo + fecha + titular display + subtítulo. Barra tricolor (russet/cork/sky) debajo.
- **Película de la semana:** banner backdrop + poster vertical sobrepuesto + anillo/badge de score circular estilo IMDb.
- **Top 5:** tarjetas con banner backdrop, badge de número (#01), pill de score, titular sobre la imagen, resumen + "nuestra opinión" con borde cork.
- **Qué ver:** tarjetas horizontales con barra de acento de color + poster vertical + tipo de pick.
- **RT Tracker:** tabla con miniatura de poster + barra de progreso del tomatómetro + score + audiencia.
- **Recomendación:** bloque con borde izquierdo cork, cursiva, cálido.
- **Cierre:** comilla tipográfica grande + cita + firma.
