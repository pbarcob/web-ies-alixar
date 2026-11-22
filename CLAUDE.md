# Web del IES Alixar: normas de trabajo

Web publicada con GitHub Pages: https://pbarcob.github.io/web-ies-alixar/ (rama `main`, carpeta `/docs`).

## Cómo se hace un cambio
1. El contenido está en `src/base.html` y es **único para las tres versiones**. El aspecto de cada versión está en `themes/<estilo>/`.
2. Después de editar, ejecuta siempre `python3 build.py`: regenera `docs/index.html` (Atrevida, la versión por defecto), `docs/clasica.html` y `docs/institucional.html`.
3. Antes de subir, revisa las páginas afectadas en escritorio y en móvil.
4. Sube los fuentes y `docs/` en el mismo commit, con un mensaje en español que describa el cambio.

## Criterios de contenido acordados con la dirección
- Las tres versiones solo se diferencian en lo visual. Ningún cambio de contenido puede afectar a una sola de ellas.
- Matrícula, escolarización, ACREDITA, pruebas de obtención de título (POT), Moodle Centros, anulaciones y renuncias de FP, iANDE e iPasen: solo enlaces a las fuentes oficiales de la Junta de Andalucía y vídeos de canales oficiales. Contenido propio mínimo.
- Secretaría: horario (días lectivos, de 9:00 a 14:00), indicaciones generales y enlaces oficiales. Sin plazas vacantes ni datos que ya publica la Junta.
- Instagram (@ies_alixar y @BiblioAlixar): con protagonismo en portada, con enlace a las cuentas y con las últimas publicaciones cargadas solas (`FEEDS`, feeds JSON de Behold). Sin página propia.
- Plan de Centro: carpeta de Drive incrustada.
- Menú: Inicio · El centro · Secretaría · ESO y Bachillerato · Formación Profesional · ACREDITA · Convivencia.
