"""Photos : balises <img> complètes (alt, dimensions, chargement) à partir de marqueurs {{PHOTO:clé}}.
  {{PHOTO:clé}}        -> image de contenu, chargement différé
  {{PHOTO:clé:eager}}  -> image principale (haut de page) : chargée en priorité
Les photos sont intégrées en WebP (base64) dans les maquettes; build_offline les extrait en fichiers."""
import base64, os, re
from PIL import Image
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img') + '/'
FILES = {'hero': 'hero', 'equipe': 'equipe', 'residentiel': 'residentiel', 'commercial': 'commercial', 'thermo': 'thermopompe',
         'entretien': 'entretien', 'chauffage': 'chauffage', 'guide': 'guide-thermopompe', 'conduits': 'conduits', 'fer': 'ferblanterie', 'refrig': 'refrigeration'}
# Descriptions pour Google Images et les lecteurs d'écran (à adapter quand les vraies photos de Bédard remplaceront les photos temporaires)
ALT = {
 'hero': "Une cliente détendue sur son canapé, dans une maison confortable toute l'année",
 'residentiel': "Thermopompe installée à l'extérieur d'une maison",
 'commercial': "Salle mécanique d'un bâtiment commercial avec conduits de ventilation",
 'thermo': "Unité extérieure de thermopompe installée contre un mur de brique",
 'entretien': "Unité extérieure de climatiseur pendant un entretien",
 'chauffage': "Femme se réchauffant près d'un chauffage électrique d'appoint",
 'guide': "Unité extérieure de thermopompe sur une dalle de béton",
 'equipe': "Technicien en chauffage et climatisation avec ses manomètres de réfrigération",
 'conduits': "Conduits de ventilation en tôle fabriqués sur mesure",
 'fer': "Conduits de ventilation installés dans un bâtiment commercial",
 'refrig': "Chambre froide commerciale avec évaporateur",
}
def uri(key):
    return 'data:image/webp;base64,' + base64.b64encode(open(D + FILES[key] + '.webp', 'rb').read()).decode()
def tag(key, mode=''):
    w, h = Image.open(D + FILES[key] + '.webp').size
    pri = 'fetchpriority="high" decoding="async"' if mode == 'eager' else 'loading="lazy" decoding="async"'
    return f'<img src="{uri(key)}" alt="{ALT[key]}" width="{w}" height="{h}" {pri}>'
def fill(html):
    return re.sub(r'\{\{PHOTO:([a-z]+)(?::(eager))?\}\}', lambda m: tag(m.group(1), m.group(2) or ''), html)
