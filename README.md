# Web del IES Alixar

Web del IES Alixar (Castilleja de la Cuesta, Sevilla) en tres estilos visuales con **el mismo contenido**:

| Estilo | Archivo publicado |
|---|---|
| Atrevida (por defecto) | `docs/index.html` |
| Clásica | `docs/clasica.html` |
| Institucional | `docs/institucional.html` |

El visitante puede cambiar de estilo desde el pie de página; su elección se recuerda en su navegador.

## Estructura

```
src/base.html        Contenido único de la web (todas las páginas y textos)
themes/<estilo>/     Aspecto de cada versión: style.css, fonts.html, defs.svg, hero.svg
build.py             Genera las tres versiones en docs/
docs/                Web lista para publicar (GitHub Pages: rama main, carpeta /docs)
assets/              Escudo del centro en SVG y PNG
```

## Cómo se actualiza

1. Los cambios de **contenido** se hacen en `src/base.html`; los de **aspecto**, en `themes/<estilo>/`.
2. Se regenera la web: `python3 build.py`
3. Se sube a GitHub: `git add -A && git commit -m "Descripción del cambio" && git push`
4. GitHub Pages publica la nueva versión en uno o dos minutos.

## Pendiente

- Fotos reales del centro.
- Feeds automáticos de Instagram (Behold): pegar las URL en `FEEDS`, dentro del script de `src/base.html`.
