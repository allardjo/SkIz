"""Assemble la page de service modèle à partir du gabarit v2 (CSS, en-tête, pied) et des fichiers de maquettes/src/."""
import base64, re, sys
sys.path.insert(0, '/home/user/SkIz/maquettes')
from typo import typo, add_css
ROOT = '/home/user/SkIz/maquettes/'
B = '/home/user/SkIz/assets/brand/svg/'
def svg(n): return 'data:image/svg+xml;base64,' + base64.b64encode(open(B + n, 'rb').read()).decode()
def jpg(n): return 'data:image/jpeg;base64,' + base64.b64encode(open(ROOT + 'img/' + n + '.jpg', 'rb').read()).decode()

base = open(ROOT + 'source-accueil-v3.template.html', encoding='utf-8').read()
s0 = base.index('\n<style>') + 8  # le commentaire Ballinger contient aussi le mot <style>
css = base[s0: base.index('</style>')]
header = base[base.index('<header class="site"'): base.index('</header>') + 9]
tail = base[base.index('<footer class="pied">'):]
extra = open(ROOT + 'src/service-extra.css', encoding='utf-8').read()
body = open(ROOT + 'src/pilier-climatiseur-thermopompe.body.html', encoding='utf-8').read()

css = re.sub(r'url\(\{\{IMG_[A-Z]+\}\}\)', 'none', css)  # images de l'accueil, inutiles ici
title = 'Climatiseur mural et thermopompe à Joliette | Bédard'
desc = "Climatiseur mural, thermopompe et climatisation à Joliette et Lanaudière : conseil, installation propre et entretien par plus de 65 professionnels."
assert len(title) <= 60 and len(desc) <= 160, (len(title), len(desc))

ld = '''{"@context":"https://schema.org","@graph":[
{"@type":"Service","@id":"https://cbedard.com/climatiseur-mural-air-climatise-thermopompe-joliette/#service","name":"Climatiseur mural et thermopompe à Joliette","serviceType":"Vente, installation et entretien de climatiseurs muraux et de thermopompes","provider":{"@type":["HVACBusiness","LocalBusiness"],"@id":"https://cbedard.com/#entreprise","name":"Bédard — Performance thermique","legalName":"Entreprise De Réfrigération & Climatisation Claude Bédard (1995) Inc.","telephone":"+1-450-753-9426","address":{"@type":"PostalAddress","streetAddress":"304, boulevard de l'Industrie","addressLocality":"Joliette","addressRegion":"QC","postalCode":"J6E 8V2","addressCountry":"CA"}},"areaServed":["Joliette","Lanaudière"],"url":"https://cbedard.com/climatiseur-mural-air-climatise-thermopompe-joliette/"},
{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://cbedard.com/"},{"@type":"ListItem","position":2,"name":"Climatiseur mural et thermopompe"}]},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Quelle est la différence entre un climatiseur mural et une thermopompe murale?","acceptedAnswer":{"@type":"Answer","text":"Le climatiseur mural rafraîchit. La thermopompe murale climatise aussi, et peut en plus chauffer, ce qui permet d'utiliser un seul appareil toute l'année. Dans les deux cas, aucun conduit n'est nécessaire."}},
{"@type":"Question","name":"Peut-on climatiser plusieurs pièces avec un seul climatiseur mural?","acceptedAnswer":{"@type":"Answer","text":"Oui, dans bien des cas. Une unité simple zone peut couvrir un plein pied complet avec plusieurs pièces, selon l'aménagement, l'isolation et la circulation de l'air. Pour des espaces plus éloignés ou fermés, on ajoute des unités (système multizone). Nous évaluons votre maison avant de recommander."}},
{"@type":"Question","name":"Faites-vous l'entretien et le nettoyage des climatiseurs muraux?","acceptedAnswer":{"@type":"Answer","text":"Oui, nous offrons un service d'entretien périodique personnalisé."}},
{"@type":"Question","name":"Offrez-vous un service d'urgence?","acceptedAnswer":{"@type":"Answer","text":"Oui, un service d'urgence est offert 24 heures sur 24. Appelez le 450-753-9426."}}]}
]}'''

head = f'''<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://cbedard.com/climatiseur-mural-air-climatise-thermopompe-joliette/">
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
out = ROOT + 'pilier-climatiseur-mural-thermopompe.html'
open(out, 'w', encoding='utf-8').write(html)
print(len(html) // 1024, 'Ko ->', out)
