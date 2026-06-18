# Puesta en marcha — GitHub + Rutina automática

Esta guía te lleva de cero a tener CineRadar en GitHub y, opcionalmente, generándose solo cada viernes.

---

## 1. Subir el repositorio a GitHub

Desde la carpeta `Cine_radar/`:

```bash
# Inicializa el repositorio (si aún no lo está)
git init
git add .
git commit -m "CineRadar: sistema de newsletter automatizado"

# Crea el repo en GitHub y súbelo (requiere GitHub CLI autenticado)
gh repo create cine-radar --public --source=. --remote=origin --push
```

Si no tienes `gh`:
1. Crea un repositorio vacío en https://github.com/new (ej. `cine-radar`).
2. Conéctalo y sube:
   ```bash
   git remote add origin https://github.com/TU_USUARIO/cine-radar.git
   git branch -M main
   git push -u origin main
   ```

> ✅ Cualquiera que clone el repo y abra Claude Code dentro podrá ejecutar `/generar-newsletter` y reproducir el newsletter — toda la lógica vive en `CLAUDE.md` y `docs/`.

---

## 2. Convertir la generación en una rutina semanal

Hay dos formas, según cómo trabajes.

### Opción A — Rutina en la nube con `/schedule` (recomendada)

Dentro de Claude Code, en este repositorio, pide:

```
/schedule cada viernes a las 9:00 ejecuta /generar-newsletter
```

Esto crea un **agente programado (routine)** que corre en la nube cada viernes, ejecuta el flujo completo y genera la edición. Puedes listar, editar o borrar tus rutinas con el mismo comando `/schedule`.

> La generación de imágenes y la búsqueda web funcionan dentro de la rutina igual que en una sesión normal.

### Opción B — Loop local con `/loop`

Si prefieres dispararlo manualmente y dejarlo corriendo en tu máquina mientras trabajas:

```
/loop /generar-newsletter
```

Útil para iterar varias ediciones de prueba en una sola sesión.

---

## 3. Mantener las ediciones versionadas

Cada edición generada queda en `editions/cineradar_XXX.html`. Para guardarla en el historial:

```bash
git add editions/
git commit -m "Edición #XXX — [fecha]"
git push
```

Así tienes un archivo histórico navegable de todas las ediciones publicadas.

---

## 4. Publicar el newsletter

El HTML generado está listo para:
- **Plataformas de email:** importa el HTML en Mailchimp, Beehiiv, ConvertKit o Brevo. La plataforma re-aloja las imágenes en su propio CDN automáticamente.
- **Web / GitHub Pages:** si activas GitHub Pages sobre la carpeta `editions/`, cada edición queda accesible como página pública. (Settings → Pages → Source → rama `main`, carpeta `/`).

---

## 5. Personalizar el sistema

| Quieres cambiar… | Edita… |
|------------------|--------|
| Voz, fuentes, fact-checking | `docs/EDITORIAL_GUIDELINES.md` |
| Paleta, tipografía, layout | `docs/DESIGN_SYSTEM.md` |
| Cómo se elige el contenido | `docs/CONTENT_SELECTION.md` |
| El paso a paso de generación | `docs/WORKFLOW.md` |
| El comando de generación | `.claude/commands/generar-newsletter.md` |
| Configuración global / idioma | `CLAUDE.md` |

Tras cualquier cambio, la siguiente ejecución de `/generar-newsletter` lo respeta automáticamente.
