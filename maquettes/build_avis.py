"""Assemble la page de service modèle à partir du gabarit v2 (CSS, en-tête, pied) et des fichiers de maquettes/src/."""
import base64, re, sys
sys.path.insert(0, '/home/user/SkIz/maquettes')
from typo import typo, add_css
ROOT = '/home/user/SkIz/maquettes/'
B = '/home/user/SkIz/assets/brand/svg/'
def svg(n): return 'data:image/svg+xml;base64,' + base64.b64encode(open(B + n, 'rb').read()).decode()
def jpg(n): return 'data:image/webp;base64,' + base64.b64encode(open(ROOT + 'img/' + n + '.webp', 'rb').read()).decode()

base = open(ROOT + 'source-accueil-v21.template.html', encoding='utf-8').read()
s0 = base.index('\n<style>') + 8  # le commentaire Ballinger contient aussi le mot <style>
css = base[s0: base.index('</style>')]
header = base[base.index('<header class="site"'): base.index('</header>') + 9]
tail = base[base.index('<footer class="pied">'):]
extra = open(ROOT + 'src/service-extra.css', encoding='utf-8').read() + open(ROOT + 'src/avis-extra.css', encoding='utf-8').read()
body = open(ROOT + 'src/avis.body.html', encoding='utf-8').read()

css = re.sub(r'url\(\{\{IMG_[A-Z]+\}\}\)', 'none', css)  # images de l'accueil, inutiles ici
title = 'Avis clients : ce que disent nos clients | Bédard'
desc = "4,9 sur 5 selon plus de 180 avis Google et Facebook. Lisez les témoignages de clients de Bédard à Joliette et en Lanaudière."
assert len(title) <= 60 and len(desc) <= 160, (len(title), len(desc))

ld = '''{"@context":"https://schema.org","@graph":[
{"@type":"CollectionPage","@id":"https://cbedard.com/avis/#page","url":"https://cbedard.com/avis/","name":"Avis clients","about":{"@id":"https://cbedard.com/#entreprise"},"inLanguage":"fr-CA"},
{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://cbedard.com/"},{"@type":"ListItem","position":2,"name":"Avis clients"}]},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Où puis-je lire tous vos avis?","acceptedAnswer":{"@type":"Answer","text":"Tous nos avis sont publiés sur notre fiche Google et sur notre page Facebook, avec le texte complet et la date. Nous n'en modifions aucun."}},
{"@type":"Question","name":"Comment laisser un avis sur Bédard?","acceptedAnswer":{"@type":"Answer","text":"Ouvrez notre fiche Google, donnez une note et décrivez votre expérience. Il suffit d'un compte Google, et cela prend environ deux minutes."}},
{"@type":"Question","name":"Que faire si mon expérience n'a pas été à la hauteur?","acceptedAnswer":{"@type":"Answer","text":"Appelez-nous au 450-753-9426 ou écrivez-nous : nous voulons le savoir et corriger la situation. Vous pouvez aussi publier votre avis; nous y répondons."}},
{"@type":"Question","name":"Les avis sont-ils vérifiés?","acceptedAnswer":{"@type":"Answer","text":"Les avis sont publiés directement par Google et Facebook, pas par Bédard. Nous ne payons pas pour obtenir des avis."}}]}
]}'''

head = f'''<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://cbedard.com/avis/">
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
out = ROOT + 'avis.html'
open(out, 'w', encoding='utf-8').write(html)
print(len(html) // 1024, 'Ko ->', out)
