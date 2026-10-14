"""Convertit les photos sources (img/*.jpg) en WebP allégé (img/*.webp).
Cible : photo du haut < 100 Ko, les autres < 150 Ko. Usage : python3 -I make_webp.py"""
import glob, os
from PIL import Image
MAXW = {'hero': 1600, 'equipe': 1400, 'commercial': 900, 'ferblanterie': 900, 'conduits': 700, 'thermopompe': 900, 'residentiel': 1000}
for f in sorted(glob.glob('img/*.jpg')):
    n = os.path.basename(f)[:-4]
    im = Image.open(f).convert('RGB')
    w = MAXW.get(n, 1100)
    if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    q = 76
    while True:
        im.save(f'img/{n}.webp', 'WEBP', quality=q, method=6)
        kb = os.path.getsize(f'img/{n}.webp') / 1024
        if kb <= (100 if n == 'hero' else 150) or q <= 56: break
        q -= 4
    print(f'{n:16s} {os.path.getsize(f)/1024:5.0f} Ko -> {kb:5.0f} Ko  {im.size} q{q}')
