# 🎬 CineRadar

> Un briefing semanal curado para amantes del cine. Cada viernes, las 5 historias que de verdad importan — generadas automáticamente con Claude Code.

CineRadar no es un sitio de noticias, ni de reseñas, ni un blog de entretenimiento. Es un **newsletter premium en HTML** que filtra el ruido de la industria y presenta solo lo que merece la atención del lector. El objetivo es que el lector sienta: *"no me perdí nada importante esta semana"* y *"ahora sé exactamente qué películas merecen mi atención"*.

Este repositorio contiene **todo lo necesario para reproducir el newsletter de forma consistente** con [Claude Code](https://claude.com/claude-code), e incluso convertirlo en una **rutina automática semanal**.

---

## ✨ Qué hace este sistema

- 🔎 **Investiga** las noticias de cine reales de la semana (Variety, Deadline, THR, Collider, IndieWire, Rotten Tomatoes).
- 🧠 **Selecciona** las 5 historias más relevantes según una jerarquía editorial definida.
- 🖼️ **Obtiene imágenes oficiales** (posters y backdrops) desde TMDB.
- ✍️ **Redacta** en español con una voz de crítico-amigo cinéfilo.
- 🎨 **Maqueta** una edición en HTML con estética cinematográfica (paleta inspirada en *Oppenheimer*).
- 📁 **Archiva** cada edición numerada en `editions/`.

---

## 🚀 Uso rápido

1. Abre este repositorio con Claude Code:
   ```bash
   cd Cine_radar
   claude
   ```
2. Ejecuta el comando:
   ```
   /generar-newsletter
   ```
3. Claude investiga, selecciona, redacta y genera `editions/cineradar_XXX.html`.
4. Abre el archivo en el navegador para revisarlo, o impórtalo a tu plataforma de email.

> 💡 También puedes pedirlo en lenguaje natural: *"Genera la edición de esta semana de CineRadar"*.

---

## 📐 Estructura del repositorio

| Ruta | Contenido |
|------|-----------|
| [`CLAUDE.md`](CLAUDE.md) | Instrucciones maestras para Claude Code |
| [`docs/EDITORIAL_GUIDELINES.md`](docs/EDITORIAL_GUIDELINES.md) | Voz, tono, fuentes aprobadas, fact-checking |
| [`docs/DESIGN_SYSTEM.md`](docs/DESIGN_SYSTEM.md) | Paleta, tipografía, layout, reglas de imagen |
| [`docs/CONTENT_SELECTION.md`](docs/CONTENT_SELECTION.md) | Jerarquía de selección automática de contenido |
| [`docs/WORKFLOW.md`](docs/WORKFLOW.md) | Proceso paso a paso de generación |
| [`templates/newsletter_template.html`](templates/newsletter_template.html) | Plantilla base con marcadores |
| [`editions/`](editions/) | Ediciones generadas (incluye ejemplo `cineradar_001.html`) |
| [`.claude/commands/`](.claude/commands/) | Slash command `/generar-newsletter` |
| [`SETUP.md`](SETUP.md) | Cómo subir a GitHub y automatizar como rutina |

---

## ⚙️ Configuración editorial

| Parámetro | Valor |
|-----------|-------|
| Idioma | Español (títulos en inglés original) |
| Mercado | Hollywood / EE.UU. |
| Tipos de cine | Blockbusters · trending · autor/premiado |
| Frecuencia | Semanal (viernes) |
| Secciones | Película de la semana · Top 5 · Qué ver · RT Tracker · Recomendación personal |

---

## 🤖 Convertirlo en rutina

Consulta [`SETUP.md`](SETUP.md) para:
- Subir el repositorio a GitHub.
- Programar la generación automática cada viernes con `/schedule`.

---

## 📜 Principio rector

> **Nunca inventar información.** Todo dato proviene de una fuente legítima y verificable. La precisión siempre gana a la velocidad. La credibilidad es el activo más valioso de CineRadar.

---

*Until the next screening.* — **CineRadar**
