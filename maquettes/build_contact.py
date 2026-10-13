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
extra_base = open(ROOT + 'src/service-extra.css', encoding='utf-8').read() + open(ROOT + 'src/contact-extra.css', encoding='utf-8').read()

import json
bc = lambda n, item: '{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://cbedard.com/"},{"@type":"ListItem","position":2,"name":"%s"}]}' % n
ent = '"@id":"https://cbedard.com/#entreprise"'
LB = ('{"@type":["LocalBusiness","HVACBusiness"],"@id":"https://cbedard.com/#entreprise","name":"Bédard — Performance thermique","legalName":"Entreprise De Réfrigération & Climatisation Claude Bédard (1995) Inc.",'
      '"url":"https://cbedard.com/","telephone":"+1-450-753-9426","email":"info@cbedard.com",'
      '"address":{"@type":"PostalAddress","streetAddress":"304, boulevard de l\'Industrie","addressLocality":"Joliette","addressRegion":"QC","postalCode":"J6E 8V2","addressCountry":"CA"},'
      '"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"17:00"}],'
      '"contactPoint":[{"@type":"ContactPoint","contactType":"customer service","telephone":"+1-450-753-9426","availableLanguage":"fr"},{"@type":"ContactPoint","contactType":"toll free","telephone":"+1-800-953-0153","availableLanguage":"fr"}]}')
PAGES = {
 'contact': dict(BODY='contact.body.html', OUT='contact-climatisation-joliette.html', CANON='https://cbedard.com/contact-climatisation-joliette/',
   title='Nous joindre : chauffage et climatisation Joliette | Bédard',
   desc="Joignez Bédard à Joliette : 450-753-9426, courriel, adresse et heures. Service d'urgence 24 h pour chauffage, climatisation et réfrigération.",
   ld='{"@context":"https://schema.org","@graph":[{"@type":"ContactPage","@id":"https://cbedard.com/contact-climatisation-joliette/#page","url":"https://cbedard.com/contact-climatisation-joliette/","name":"Nous joindre","about":{"@id":"https://cbedard.com/#entreprise"}},' + LB + ',' + bc('Contact','') + ']}'),
 'commercial': dict(BODY='commercial.body.html', OUT='commercial.html', CANON='https://cbedard.com/commercial/',
   title='Services commerciaux CVAC-R à Joliette | Bédard',
   desc="Ventilation, réfrigération et ferblanterie pour commerces, industries et institutions à Joliette et Lanaudière. Conception, entretien, urgence 24 h.",
   ld='{"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://cbedard.com/commercial/#page","url":"https://cbedard.com/commercial/","name":"Services commerciaux","about":{"@id":"https://cbedard.com/#entreprise"}},{"@type":"Service","@id":"https://cbedard.com/commercial/#service","name":"Ventilation, réfrigération et ferblanterie commerciales","serviceType":"CVAC-R commercial, industriel et institutionnel","provider":{"@id":"https://cbedard.com/#entreprise"},"areaServed":{"@type":"AdministrativeArea","name":"Lanaudière"}},' + bc('Commercial','') + ',{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Pour quels types de bâtiments travaillez-vous?","acceptedAnswer":{"@type":"Answer","text":"Nous réalisons des projets résidentiels, commerciaux, industriels et institutionnels."}},{"@type":"Question","name":"Faites-vous la conception des systèmes de ventilation?","acceptedAnswer":{"@type":"Answer","text":"Oui. Nos professionnels réalisent le design, la conception et l\'installation de systèmes de ventilation personnalisés, y compris les dessins d\'intégration et les dessins d\'atelier."}},{"@type":"Question","name":"Offrez-vous un entretien périodique?","acceptedAnswer":{"@type":"Answer","text":"Oui, nous offrons un service d\'entretien périodique personnalisé pour vos équipements de ventilation, de réfrigération et de climatisation."}},{"@type":"Question","name":"Avez-vous un service d\'urgence?","acceptedAnswer":{"@type":"Answer","text":"Oui, un service d\'urgence est offert 24 heures sur 24."}}]}]}'),
 'ventilation': dict(BODY='ventilation.body.html', OUT='ventilation-commerciale-joliette.html', CANON='https://cbedard.com/commercial/ventilation-commerciale-joliette/',
   title='Ventilation commerciale à Joliette | Bédard',
   desc="Conception, ferblanterie sur mesure, installation et nettoyage de ventilation commerciale à Joliette et Lanaudière. Soumission détaillée, urgence 24 h.",
   ld=json.dumps({"@context":"https://schema.org","@graph":[
     {"@type":"WebPage","@id":"https://cbedard.com/commercial/ventilation-commerciale-joliette/#page","url":"https://cbedard.com/commercial/ventilation-commerciale-joliette/","name":"Ventilation commerciale à Joliette","about":{"@id":"https://cbedard.com/#entreprise"}},
     {"@type":"Service","@id":"https://cbedard.com/commercial/ventilation-commerciale-joliette/#service","name":"Ventilation commerciale","serviceType":"Conception, fabrication, installation et nettoyage de systèmes de ventilation","provider":{"@id":"https://cbedard.com/#entreprise"},"areaServed":{"@type":"AdministrativeArea","name":"Lanaudière"}},
     {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://cbedard.com/"},{"@type":"ListItem","position":2,"name":"Commercial","item":"https://cbedard.com/commercial/"},{"@type":"ListItem","position":3,"name":"Ventilation commerciale"}]},
     {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":x["q"],"acceptedAnswer":{"@type":"Answer","text":x["a"]}} for x in json.load(open('/home/user/SkIz/maquettes/src/ventilation.faq.json',encoding='utf-8'))]}]}, ensure_ascii=False)),
 'refrigeration': dict(BODY='refrigeration.body.html', OUT='refrigeration-commerciale-joliette.html', CANON='https://cbedard.com/commercial/refrigeration-commerciale/',
   title='Réfrigération commerciale à Joliette | Bédard',
   desc="Frigoristes à Joliette : installation, entretien préventif et dépannage 24 h de systèmes de réfrigération commerciale. Soumission détaillée.",
   ld=json.dumps({"@context":"https://schema.org","@graph":[
     {"@type":"WebPage","@id":"https://cbedard.com/commercial/refrigeration-commerciale/#page","url":"https://cbedard.com/commercial/refrigeration-commerciale/","name":"Réfrigération commerciale à Joliette","about":{"@id":"https://cbedard.com/#entreprise"}},
     {"@type":"Service","@id":"https://cbedard.com/commercial/refrigeration-commerciale/#service","name":"Réfrigération commerciale","serviceType":"Installation, entretien et dépannage de systèmes de réfrigération commerciale","provider":{"@id":"https://cbedard.com/#entreprise"},"areaServed":{"@type":"AdministrativeArea","name":"Lanaudière"}},
     {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://cbedard.com/"},{"@type":"ListItem","position":2,"name":"Commercial","item":"https://cbedard.com/commercial/"},{"@type":"ListItem","position":3,"name":"Réfrigération commerciale"}]},
     {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":x["q"],"acceptedAnswer":{"@type":"Answer","text":x["a"]}} for x in json.load(open('/home/user/SkIz/maquettes/src/refrigeration.faq.json',encoding='utf-8'))]}]}, ensure_ascii=False)),
 'soumission': dict(BODY='soumission.body.html', OUT='soumission.html', CANON='https://cbedard.com/soumission/',
   title='Soumission gratuite chauffage et climatisation | Bédard',
   desc="Demandez une soumission gratuite en 2 minutes : thermopompe, climatisation, ventilation, géothermie ou projet commercial à Joliette et Lanaudière.",
   ld='{"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://cbedard.com/soumission/#page","url":"https://cbedard.com/soumission/","name":"Soumission gratuite","about":{"@id":"https://cbedard.com/#entreprise"}},' + bc('Soumission','') + ']}'),
}
for key, P in PAGES.items():
    BODY, OUT, CANON, title, desc, ld = P['BODY'], P['OUT'], P['CANON'], P['title'], P['desc'], P['ld']
    json.loads(ld)
    extra = extra_base + (open(ROOT + 'src/commercial-extra.css', encoding='utf-8').read() if key in ('commercial', 'ventilation', 'refrigeration') else '') + (open(ROOT + 'src/refrigeration-extra.css', encoding='utf-8').read() if key == 'refrigeration' else '')
    body = open(ROOT + 'src/' + BODY, encoding='utf-8').read()
    css2 = re.sub(r'url\(\{\{IMG_[A-Z]+\}\}\)', 'none', css)
    assert len(title) <= 60 and len(desc) <= 160, (key, len(title), len(desc))
    head = f'''<!doctype html>
    <html lang="fr-CA">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{CANON}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Mona+Sans:ital,wdth,wght@0,75..125,200..900&display=swap" rel="stylesheet">
    <style>{css2}
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
    files = {'thermo': 'thermopompe', 'hero': 'hero', 'equipe': 'equipe', 'residentiel': 'residentiel', 'commercial': 'commercial', 'entretien': 'entretien', 'chauffage': 'chauffage', 'guide': 'guide-thermopompe', 'refrig': 'refrigeration'}
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
    out = ROOT + OUT
    open(out, 'w', encoding='utf-8').write(html)
    print(len(html) // 1024, 'Ko ->', out)
