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
extra = open(ROOT + 'src/service-extra.css', encoding='utf-8').read()
body = open(ROOT + 'src/service-installation-thermopompe.body.html', encoding='utf-8').read()

css = re.sub(r'url\(\{\{IMG_[A-Z]+\}\}\)', 'none', css)  # images de l'accueil, inutiles ici
title = 'Installation de thermopompe à Joliette | Bédard'
desc = "Installation de thermopompe murale ou centrale à Joliette et dans Lanaudière : évaluation, soumission détaillée et installation propre. Urgence 24 h."
assert len(title) <= 60 and len(desc) <= 160, (len(title), len(desc))

ld = '''{"@context":"https://schema.org","@graph":[
{"@type":"Service","@id":"https://cbedard.com/services/installation-thermopompe-joliette/#service","name":"Installation de thermopompe à Joliette","serviceType":"Installation de thermopompe murale et centrale","provider":{"@type":["HVACBusiness","LocalBusiness"],"@id":"https://cbedard.com/#entreprise","name":"Bédard — Performance thermique","legalName":"Entreprise De Réfrigération & Climatisation Claude Bédard (1995) Inc.","telephone":"+1-450-753-9426","address":{"@type":"PostalAddress","streetAddress":"304, boulevard de l'Industrie","addressLocality":"Joliette","addressRegion":"QC","postalCode":"J6E 8V2","addressCountry":"CA"}},"areaServed":["Joliette","Lanaudière"],"url":"https://cbedard.com/services/installation-thermopompe-joliette/"},
{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://cbedard.com/"},{"@type":"ListItem","position":2,"name":"Services","item":"https://cbedard.com/services/"},{"@type":"ListItem","position":3,"name":"Installation de thermopompe"}]},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Quelle est la différence entre une thermopompe murale et centrale?","acceptedAnswer":{"@type":"Answer","text":"La thermopompe murale chauffe et climatise une zone sans conduits. La thermopompe centrale se raccorde aux conduits de la maison pour desservir tout le bâtiment."}},
{"@type":"Question","name":"Une thermopompe peut-elle remplacer ma fournaise?","acceptedAnswer":{"@type":"Answer","text":"Selon l'appareil et la maison, une thermopompe peut assurer une grande partie du chauffage. Au Québec, on la jumelle souvent à un chauffage d'appoint pour les grands froids (système bi-énergie). Nous évaluons votre situation avant de recommander."}},
{"@type":"Question","name":"Combien de temps prend l'installation?","acceptedAnswer":{"@type":"Answer","text":"Cela dépend du type d'appareil et de votre maison. Nous précisons l'échéancier dans la soumission, et nous respectons les dates convenues."}},
{"@type":"Question","name":"Faites-vous l'entretien après l'installation?","acceptedAnswer":{"@type":"Answer","text":"Oui, nous offrons un service d'entretien périodique personnalisé."}}]}
]}'''

head = f'''<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://cbedard.com/services/installation-thermopompe-joliette/">
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
out = ROOT + 'service-installation-thermopompe.html'
open(out, 'w', encoding='utf-8').write(html)
print(len(html) // 1024, 'Ko ->', out)
