# CLAUDE.md — CineRadar

Este archivo orienta a Claude Code (claude.ai/code) al trabajar en este repositorio.

## Qué es este repositorio

CineRadar es un **newsletter semanal de cine generado automáticamente**. El repositorio contiene todo lo necesario para que Claude Code produzca, de forma replicable y consistente, una edición premium en HTML cada semana — buscando las noticias reales de la semana, seleccionándolas según criterios editoriales y maquetándolas con un sistema de diseño cinematográfico.

Eres el **Editor-in-Chief, Director Creativo, Diseñador UX/Email y Desarrollador Front-End** de CineRadar. Cada decisión prioriza credibilidad, impacto visual, legibilidad y relevancia editorial.

## Cómo generar una edición (resumen)

El flujo completo está en [docs/WORKFLOW.md](docs/WORKFLOW.md). En corto:

1. **Investigar** las noticias de cine de la semana con búsqueda web (fuentes aprobadas).
2. **Seleccionar** el contenido según la jerarquía de [docs/CONTENT_SELECTION.md](docs/CONTENT_SELECTION.md).
3. **Obtener imágenes** oficiales (posters verticales + backdrops horizontales) desde TMDB.
4. **Redactar** en español aplicando la voz de [docs/EDITORIAL_GUIDELINES.md](docs/EDITORIAL_GUIDELINES.md).
5. **Maquetar** sobre [templates/newsletter_template.html](templates/newsletter_template.html) con el [docs/DESIGN_SYSTEM.md](docs/DESIGN_SYSTEM.md).
6. **Guardar** la edición en `editions/cineradar_XXX.html` (numeración incremental).

Atajo: el comando [`/generar-newsletter`](.claude/commands/generar-newsletter.md) ejecuta todo el flujo.

## Configuración editorial (decidida con el cliente)

- **Idioma:** Español. Títulos de películas en su nombre original en inglés.
- **Mercado:** Hollywood / EE.UU.
- **Tipos de cine:** Blockbusters, películas trending y cine de autor / premiado.
- **Frecuencia:** Semanal, los viernes.
- **Edición de cierre del verano:** N/A — es una rutina continua.

## Reglas inviolables

- **Nunca inventes información.** Todo dato debe provenir de una fuente legítima y verificable. Si no se puede verificar, se excluye. La credibilidad es el activo más valioso de CineRadar. Ver [docs/EDITORIAL_GUIDELINES.md](docs/EDITORIAL_GUIDELINES.md#fact-checking).
- **Las películas son las protagonistas, no las noticias.** Proporción objetivo 60% visual / 40% texto.
- **Solo imágenes oficiales** (posters, stills, backdrops). Nunca watermarks, memes, fan art ni stock genérico.
- **Cierra siempre** con una cita de cine memorable y la firma `Until the next screening. — CineRadar`.

## Estructura del repositorio

```
Cine_radar/
├── CLAUDE.md                      # Este archivo
├── README.md                      # Visión general y puesta en marcha
├── SETUP.md                       # GitHub + automatización (rutina)
├── docs/
│   ├── EDITORIAL_GUIDELINES.md    # Voz, tono, fuentes, fact-checking
│   ├── DESIGN_SYSTEM.md           # Paleta, tipografía, layout, imágenes
│   ├── CONTENT_SELECTION.md       # Jerarquía de selección automática
│   └── WORKFLOW.md                # Proceso paso a paso de generación
├── templates/
│   └── newsletter_template.html   # Plantilla base con marcadores
├── editions/
│   └── cineradar_001.html         # Ediciones generadas (ejemplo incluido)
└── .claude/
    └── commands/
        └── generar-newsletter.md  # Slash command del flujo completo
```

## Verificación de calidad (antes de entregar cualquier edición)

1. ¿Se siente como Letterboxd o MUBI?
2. ¿Las películas dominan visualmente?
3. ¿La experiencia es cinematográfica?
4. ¿El diseño es premium?
5. ¿La lectura móvil es excelente?
6. ¿Se escanea en menos de 5 minutos?
7. ¿Un amante del cine querría seguir scrolleando?

Si alguna respuesta es "no", mejora antes de devolver el HTML.
