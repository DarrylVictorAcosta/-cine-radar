---
description: Genera la edición semanal de CineRadar (investiga, selecciona, redacta y maqueta)
---

Genera una nueva edición del newsletter CineRadar siguiendo todo el sistema de este repositorio.

Contexto y reglas:
- Lee y respeta `CLAUDE.md`, `docs/EDITORIAL_GUIDELINES.md`, `docs/DESIGN_SYSTEM.md`, `docs/CONTENT_SELECTION.md` y `docs/WORKFLOW.md`.
- Configuración: español (títulos en inglés), mercado Hollywood/EE.UU., blockbusters + trending + autor/premiado, edición de los viernes.

Ejecuta el workflow completo de `docs/WORKFLOW.md`:
1. Determina la fecha del viernes de esta semana y el siguiente número de edición correlativo revisando la carpeta `editions/`.
2. Investiga con búsqueda web las noticias de cine de la semana, restringiendo a las fuentes aprobadas. **No inventes nada**: todo dato debe ser verificable.
3. Selecciona el contenido con la jerarquía de `docs/CONTENT_SELECTION.md`: 1 película de la semana, 5 historias, 3 picks de fin de semana, RT Tracker y 1 recomendación personal.
4. Obtén las imágenes oficiales desde TMDB — `backdrop_path` para banners/hero y `poster_path` para posters verticales y miniaturas. Usa el formato correcto para no recortar mal.
5. Redacta en español con la voz de crítico-amigo cinéfilo.
6. Maqueta sobre `templates/newsletter_template.html` aplicando la paleta Oppenheimer y todas las reglas de diseño.
7. Verifica el checklist de calidad de 7 puntos.
8. Guarda la edición en `editions/cineradar_XXX.html` y entrégame un resumen de qué seleccionaste y por qué.

Si algún argumento fue pasado al comando, interprétalo como instrucción adicional (ej. un tema a destacar o una película a incluir): $ARGUMENTS
