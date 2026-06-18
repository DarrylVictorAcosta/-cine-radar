# Workflow de Generación — CineRadar

Proceso paso a paso para producir una edición. Sigue este orden cada semana.

---

## Paso 0 — Contexto

- Determina la **fecha de edición** (el viernes de esta semana).
- Determina el **número de edición**: revisa `editions/` y usa el siguiente número correlativo (`cineradar_XXX.html`).

## Paso 1 — Investigar

Usa búsqueda web para encontrar las noticias de cine de la semana. Consultas sugeridas:

- `biggest movie news [mes año] Hollywood`
- `movies in theaters [mes año] box office`
- `Rotten Tomatoes scores new movies [mes año]`
- `[película] review Rotten Tomatoes score` (por cada candidata)
- `best indie film theaters [mes año] limited release`

Restringe a las **fuentes aprobadas** (`variety.com`, `deadline.com`, `hollywoodreporter.com`, `collider.com`, `indiewire.com`, `rottentomatoes.com`). Ver [EDITORIAL_GUIDELINES.md](EDITORIAL_GUIDELINES.md#fuentes-aprobadas).

## Paso 2 — Seleccionar

Aplica la jerarquía de [CONTENT_SELECTION.md](CONTENT_SELECTION.md):
- 1 película de la semana
- 5 historias (ordenadas por relevancia)
- 3 picks de fin de semana (blockbuster / indie / sorpresa)
- 5+ entradas para el RT Tracker
- 1 recomendación personal

**Verifica cada dato.** Si algo no se puede confirmar, se excluye.

## Paso 3 — Obtener imágenes (TMDB)

Para cada película seleccionada, obtén `poster_path` y `backdrop_path`:

```
# Buscar ID:
https://api.themoviedb.org/3/search/movie?api_key={KEY}&query={TITULO}&year={AÑO}

# Detalles (poster + backdrop):
https://api.themoviedb.org/3/movie/{ID}?api_key={KEY}

# URL final de imagen:
https://image.tmdb.org/t/p/{TAMAÑO}{path}
```

Asigna el **formato correcto** según el espacio (ver [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md#formato-correcto-según-el-espacio-clave-para-no-recortar-mal)):
- Banners/hero → **backdrop** (`w1280`)
- Poster sobrepuesto, picks, RT tracker → **poster** (`w92`–`w500`)

> TMDB tiene una API key pública de demostración ampliamente usada en ejemplos: `8265bd1679663a7ea12ac168da84d2e8`. Para producción seria, registra tu propia key gratuita en https://www.themoviedb.org/settings/api.

## Paso 4 — Redactar

Escribe en **español**, títulos en inglés, con la voz de [EDITORIAL_GUIDELINES.md](EDITORIAL_GUIDELINES.md#tono-de-voz):
- Historias: 120–180 palabras + "nuestra opinión" + fuente.
- Recomendación personal: máx. 150 palabras, cálida y en primera persona.
- Cierre: cita de cine memorable + `Until the next screening. — CineRadar`.

## Paso 5 — Maquetar

Parte de [templates/newsletter_template.html](../templates/newsletter_template.html). Reemplaza los marcadores `{{...}}` con el contenido y las URLs de imagen. Respeta el [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md):
- Paleta Oppenheimer.
- Ancho 600–620px, columna única, mobile-first.
- 60% visual / 40% texto.

## Paso 6 — Verificar calidad

Antes de guardar, confirma las 7 preguntas del checklist en [CLAUDE.md](../CLAUDE.md#verificación-de-calidad-antes-de-entregar-cualquier-edición). Si alguna es "no", mejora.

## Paso 7 — Guardar y entregar

- Guarda en `editions/cineradar_XXX.html`.
- Informa al usuario la ruta y un resumen de qué se seleccionó y por qué.
- Recuerda: las imágenes externas cargan en navegador; al importar a una plataforma de email, esta las re-aloja en su CDN.

---

## Resumen en una línea

> Investiga (fuentes aprobadas) → selecciona (jerarquía + filtro maestro) → imágenes TMDB (formato correcto) → redacta (voz cinéfila, español) → maqueta (paleta Oppenheimer, plantilla) → verifica (checklist) → guarda en `editions/`.
