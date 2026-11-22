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
- Menú: Inicio · El centro · Secretaría · Familias · Alumnado · ESO y Bachillerato · Formación Profesional · ACREDITA · Convivencia, más buscador e Instagram. Barra superior: Preguntas frecuentes · Calendario · Profesorado · Transparencia · Otros idiomas.
- Avisos de portada: cada `<li>` del recuadro de avisos lleva `data-hasta="AAAA-MM-DD"` y desaparece solo al día siguiente de esa fecha. Todo aviso nuevo debe llevar fecha de caducidad.
- No se inventan datos: lo que no conste en los documentos del centro o en fuentes oficiales se pregunta a la dirección antes de publicarlo.
- La página «Otros idiomas» (inglés, francés y árabe) debe actualizarse cuando cambien horario, dirección o canales de contacto.
