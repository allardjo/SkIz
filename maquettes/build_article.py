"""Assemble la page de service modèle à partir du gabarit v2 (CSS, en-tête, pied) et des fichiers de maquettes/src/."""
import base64, re, sys
sys.path.insert(0, '/home/user/SkIz/maquettes')
from typo import typo, add_css
ROOT = '/home/user/SkIz/maquettes/'
B = '/home/user/SkIz/assets/brand/svg/'
def svg(n): return 'data:image/svg+xml;base64,' + base64.b64encode(open(B + n, 'rb').read()).decode()
def jpg(n): return 'data:image/jpeg;base64,' + base64.b64encode(open(ROOT + 'img/' + n + '.jpg', 'rb').read()).decode()

base = open(ROOT + 'source-accueil-v2.template.html', encoding='utf-8').read()
s0 = base.index('\n<style>') + 8  # le commentaire Ballinger contient aussi le mot <style>
css = base[s0: base.index('</style>')]
header = base[base.index('<header class="site"'): base.index('</header>') + 9]
tail = base[base.index('<footer class="pied">'):]
extra = open(ROOT + 'src/service-extra.css', encoding='utf-8').read()
body = open(ROOT + 'src/article-prix-climatiseur-mural.body.html', encoding='utf-8').read()

css = re.sub(r'url\(\{\{IMG_[A-Z]+\}\}\)', 'none', css)  # images de l'accueil, inutiles ici
title = 'Prix d\'un climatiseur mural installé : guide | Bédard'
desc = "Combien coûte un climatiseur mural installé? Facteurs du prix, puissance (BTU), efficacité et conseils pour bien comparer vos soumissions."
assert len(title) <= 60 and len(desc) <= 160, (len(title), len(desc))

ld = '''{"@context":"https://schema.org","@graph":[
{"@type":"Article","@id":"https://cbedard.com/air-climatise-mural-a-quel-prix-sattendre/#article","headline":"Climatiseur mural installé : à quel prix s'attendre?","datePublished":"2022-05-31","dateModified":"2026-10-13","inLanguage":"fr-CA","author":{"@type":"Organization","name":"Bédard — Performance thermique"},"publisher":{"@type":"Organization","name":"Bédard — Performance thermique","@id":"https://cbedard.com/#entreprise"},"mainEntityOfPage":"https://cbedard.com/air-climatise-mural-a-quel-prix-sattendre/"},
{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://cbedard.com/"},{"@type":"ListItem","position":2,"name":"Blogue","item":"https://cbedard.com/blogue/"},{"@type":"ListItem","position":3,"name":"Prix d'un climatiseur mural"}]},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Combien coûte un climatiseur mural installé?","acceptedAnswer":{"@type":"Answer","text":"Pour un climatiseur mural dans une pièce, comptez entre 3 500 $ et 5 300 $ avant taxes, installation comprise. Le prix dépend de la puissance, du nombre d'unités, de la complexité de l'installation et du modèle. Nous établissons une soumission détaillée après avoir évalué votre projet."}},
{"@type":"Question","name":"Quelle puissance (BTU) choisir pour ma pièce?","acceptedAnswer":{"@type":"Answer","text":"Cela dépend de la superficie, de l'isolation et de l'ensoleillement. Un appareil trop puissant déshumidifie mal : nous dimensionnons l'appareil selon votre situation."}},
{"@type":"Question","name":"Un climatiseur mural chauffe-t-il?","acceptedAnswer":{"@type":"Answer","text":"Un climatiseur seul rafraîchit. Une thermopompe murale climatise aussi, et peut chauffer. Plusieurs modèles actuels sont des thermopompes."}},
{"@type":"Question","name":"Faut-il entretenir un climatiseur mural?","acceptedAnswer":{"@type":"Answer","text":"Oui. Un entretien périodique garde l'appareil performant plus longtemps. Nous offrons un service d'entretien périodique personnalisé."}}]}
]}'''

head = f'''<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://cbedard.com/air-climatise-mural-a-quel-prix-sattendre/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mona+Sans:ital,wdth,wght@0,75..125,200..900&display=swap" rel="stylesheet">
<style>{css}
{extra}</style>
<script type="application/ld+json">
{ld}
</script>
</head>
<body>

'''
html = head + header + '\n\n' + body + '\n' + tail

# images utilisées seulement
used = sorted(set(re.findall(r'var\(--img-([a-z]+)\)', html)))
files = {'thermo': 'thermopompe', 'hero': 'hero', 'equipe': 'equipe', 'residentiel': 'residentiel', 'commercial': 'commercial', 'entretien': 'entretien', 'chauffage': 'chauffage', 'guide': 'guide-thermopompe'}
decl = ''.join(f'--img-{k}:url({jpg(files[k])});' for k in used)
html = html.replace(':root{', ':root{' + decl, 1)

star = '<svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/></svg>'
html = (html.replace('{{SYMBOLE_BEIGE}}', svg('symbole-beige.svg'))
            .replace('{{LOGO_HORIZ_BEIGE}}', svg('logo-enonce-horizontal-beige.svg'))
            .replace('{{LOGO_HORIZ_MARINE}}', svg('logo-enonce-horizontal-marine.svg'))
            .replace('{{LOGO_ENONCE_BEIGE}}', svg('logo-enonce-horizontal-beige.svg'))
            .replace('{{ETOILES}}', star * 5))
html = typo(add_css(html))
left = re.findall(r'\{\{[A-Z_0-9]+\}\}', html)
print('images:', used, '| placeholders restants:', left, '| titre', len(title), 'car. | description', len(desc), 'car.')
out = ROOT + 'article-prix-climatiseur-mural.html'
open(out, 'w', encoding='utf-8').write(html)
print(len(html) // 1024, 'Ko ->', out)
