#!/usr/bin/env python3
"""Genera la web del IES Alixar a partir de un único contenido (src/base.html)
y un tema visual por carpeta (themes/<nombre>/).

Salida en docs/ (carpeta que publica GitHub Pages):
  docs/index.html          -> versión Atrevida (la que se ve por defecto)
  docs/clasica.html        -> versión Clásica
  docs/institucional.html  -> versión Institucional

Uso:  python3 build.py
"""
import os
B=os.path.dirname(os.path.abspath(__file__))
THEMES={'atrevida':['clasica'],'clasica':[],'institucional':['clasica']}
OUT={'atrevida':'index.html','clasica':'clasica.html','institucional':'institucional.html'}
base=open(os.path.join(B,'src','base.html'),encoding='utf-8').read()
def rd(theme,name):
    f=os.path.join(B,'themes',theme,name)
    return open(f,encoding='utf-8').read() if os.path.exists(f) else None
os.makedirs(os.path.join(B,'docs'),exist_ok=True)
for th,parents in THEMES.items():
    style=''.join(rd(p,'style.css') or '' for p in parents)+(rd(th,'style.css') or '')
    fonts=rd(th,'fonts.html') or rd('clasica','fonts.html')
    defs=rd(th,'defs.svg') or rd('clasica','defs.svg')
    hero=rd(th,'hero.svg') if rd(th,'hero.svg') is not None else rd('clasica','hero.svg')
    out=(base.replace('{{FONTS}}',fonts).replace('{{STYLE}}',style).replace('{{DEFS}}',defs)
             .replace('{{HERO_ART}}',hero).replace('{{THEME}}',th))
    assert '{{' not in out, th
    with open(os.path.join(B,'docs',OUT[th]),'w',encoding='utf-8') as f: f.write(out)
    print(f'{th:14} -> docs/{OUT[th]}  ({len(out)//1024} KB)')
