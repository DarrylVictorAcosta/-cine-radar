# Sistema de Selección Automática de Contenido — CineRadar

Este documento define **cómo Claude elige el contenido** de cada edición sin necesidad de input manual. El objetivo es que las decisiones sean consistentes semana tras semana.

## Principio

Claude busca el contenido vía búsqueda web cada edición, siguiendo la jerarquía de fuentes aprobadas ([EDITORIAL_GUIDELINES.md](EDITORIAL_GUIDELINES.md#fuentes-aprobadas)), y aplica los filtros editoriales para seleccionar lo que de verdad importa esa semana.

## Filtro maestro (toda historia debe cumplir ≥1)

1. Impacta a una película importante.
2. Ayuda al lector a decidir qué ver.
3. Representa un desarrollo significativo de la industria.
4. Genera conversación real entre los fans del cine.

Si una noticia no cumple ninguno → **se descarta**.

## Jerarquía por sección

### 🎬 Película de la semana
Elegir la película con la mayor **combinación** de:
- Estreno reciente o inminente (esta semana / fin de semana).
- Score alto en Rotten Tomatoes.
- Conversación / relevancia cultural generada.

> Empate → prioriza la que mejor sirva al lector para decidir su fin de semana.

### 📰 Top 5 historias
Seleccionar y **ordenar** por relevancia usando el filtro maestro. Mezcla recomendada para equilibrio:
- 1–2 sobre estrenos/scores que ayuden a decidir qué ver.
- 1–2 sobre desarrollos de industria (taquilla, fichajes, anuncios, fusiones).
- 1 sobre conversación cultural / fenómeno de audiencia.

Cada historia: 120–180 palabras, con resumen + "por qué importa" + "nuestra opinión" + **fuente citada**.

### 🍿 Qué ver este fin de semana
- **🎬 Blockbuster pick:** la película de mayor taquilla / alcance comercial en cartelera.
- **🎥 Independent pick:** la mejor opción de cine independiente / limitado (mejor score RT entre indies).
- **🍿 Surprise pick:** una joya inesperada — hidden gem en streaming o en cines que el lector podría pasar por alto.

### 🍅 Rotten Tomatoes Tracker
Tabla con las películas más relevantes en cartelera/streaming de la semana, ordenadas por score. Incluir movimiento semanal o score de audiencia cuando esté disponible.

### 💬 Recomendación personal
La película que más convenza editorialmente esa semana (no necesariamente la #1 en taquilla). Se escribe en primera persona, cálida, como un amigo cinéfilo. Máx. 150 palabras.

## Reglas de equilibrio

- **No** repetir la misma película en las 5 secciones de forma redundante. Puede aparecer en 2–3 como máximo si realmente lo amerita (ej. la película de la semana también es el blockbuster pick).
- Cubrir el mercado **Hollywood / EE.UU.** como base.
- Incluir variedad de tipos: **blockbusters, trending y cine de autor/premiado**.
- Si una semana es floja en estrenos, complementar con desarrollos de industria o estrenos en streaming relevantes — nunca rellenar con noticias que no pasen el filtro maestro.

## Verificación antes de redactar

- [ ] ¿Cada historia tiene fuente verificable de la lista aprobada?
- [ ] ¿Ningún dato es rumor, filtración o especulación?
- [ ] ¿Los scores de RT son los reales de esta semana?
- [ ] ¿Las fechas de estreno están confirmadas?
- [ ] ¿Hay equilibrio entre "qué ver" e "industria"?
