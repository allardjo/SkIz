"""Construit le site de test hors ligne (dossier + zip) à partir des maquettes.

- relie toutes les pages entre elles (les liens « # » des maquettes deviennent de vrais liens);
- crée les pages manquantes (hubs simples et pages « à venir »);
- extrait les images en fichiers, télécharge la police Mona Sans (licence OFL) pour l'affichage hors ligne;
- ajoute un plan du site, un README et fabrique le zip.
Usage : python3 -I build_offline.py [dossier_de_sortie]
"""
import base64, hashlib, os, re, shutil, sys, unicodedata, urllib.request, zipfile
sys.path.insert(0, '/home/user/SkIz/maquettes')
from typo import typo, add_css

ROOT = '/home/user/SkIz/maquettes/'
OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/user/SkIz/dist/site-bedard-offline'
ZIP = OUT + '.zip'

# ---------- pages existantes ----------
SRC = {
 'index.html': ('accueil-v21.html', 'Accueil'),
 'thermopompe-installation.html': ('service-installation-thermopompe.html', 'Installation de thermopompe'),
 'climatiseur-mural-thermopompe.html': ('pilier-climatiseur-mural-thermopompe.html', 'Climatiseur mural et thermopompe (page pilier)'),
 'prix-climatiseur-mural.html': ('article-prix-climatiseur-mural.html', 'Article : prix d\'un climatiseur mural'),
 'reparation-thermopompe-climatiseur-joliette.html': ('reparation-thermopompe-climatiseur-joliette.html', 'Réparation et dépannage'),
 'entretien-nettoyage-thermopompe-climatiseur-joliette.html': ('entretien-nettoyage-thermopompe-climatiseur-joliette.html', 'Entretien et nettoyage'),
 'chauffage-auxiliaire-joliette.html': ('chauffage-auxiliaire-joliette.html', "Chauffage d'appoint"),
 'commercial.html': ('commercial.html', 'Commercial (hub)'),
 'ventilation-commerciale-joliette.html': ('ventilation-commerciale-joliette.html', 'Ventilation commerciale'),
 'refrigeration-commerciale-joliette.html': ('refrigeration-commerciale-joliette.html', 'Réfrigération commerciale'),
 'ferblanterie-joliette.html': ('ferblanterie-joliette.html', 'Ferblanterie'),
 'carrieres.html': ('carrieres.html', 'Carrières'),
 'contact-climatisation-joliette.html': ('contact-climatisation-joliette.html', 'Contact'),
 'soumission.html': ('soumission.html', 'Soumission'),
}
# ---------- pages générées ----------
HUBS = {
 'residentiel.html': ('Résidentiel', "Votre maison, tout confort, toute l'année.", 'Chauffage, climatisation, qualité de l\'air et services pour votre maison.',
   [('thermopompe-installation.html', 'Installation de thermopompe', 'Murale ou centrale, avec soumission détaillée.'),
    ('climatiseur-mural-thermopompe.html', 'Climatiseur mural et thermopompe', 'Comparer les deux et choisir.'),
    ('climatiseurs-centraux.html', 'Climatiseurs centraux', 'Climatiser toute la maison par les conduits.'),
    ('fournaises-electriques.html', 'Fournaises électriques', 'Vente et installation.'),
    ('chauffage-auxiliaire-joliette.html', "Chauffage d'appoint", 'Compléter votre thermopompe par grand froid.'),
    ('qualite-de-l-air.html', "Qualité de l'air", "Échangeurs d'air, humidificateurs, purificateurs."),
    ('geothermie-planchers-radiants.html', 'Géothermie et planchers radiants', 'Conception et installation.'),
    ('services.html', 'Services', 'Réparation, entretien et nettoyage.')]),
 'services.html': ('Services', "Des services complets d'installation et d'entretien.", 'Réparation, entretien, installation et chauffage : pour la maison comme pour le commerce.',
   [('reparation-thermopompe-climatiseur-joliette.html', 'Réparation et dépannage', 'Thermopompe, climatiseur. Urgence 24 h.'),
    ('entretien-nettoyage-thermopompe-climatiseur-joliette.html', 'Entretien et nettoyage', 'Un entretien périodique personnalisé.'),
    ('thermopompe-installation.html', 'Installation de thermopompe', 'Murale ou centrale.'),
    ('commercial.html', 'Services commerciaux', 'Ventilation, réfrigération et ferblanterie.'),
    ('residentiel.html', 'Résidentiel', 'Tout pour la maison.')]),
 'blogue.html': ('Blogue', 'Conseils et guides de nos experts.', 'Articles informatifs et guides de prix pour comprendre, comparer et bien choisir.',
   [('prix-climatiseur-mural.html', "Climatiseur mural : à quel prix s'attendre?", 'Article phare, mis à jour en 2026.'),
    ('guide-remplacer-thermopompe.html', 'Remplacer sa thermopompe : à quel prix?', '(à venir)'),
    ('guide-humidificateur.html', 'Quel est le meilleur humidificateur?', '(à venir)'),
    ('climatiseur-mural-thermopompe.html', 'Climatiseur mural et thermopompe', 'Comparer les deux et choisir.')]),
}
STUBS = {
 'avis.html': ('Avis clients', "Page des avis : à maquetter (4,9 sur 5, plus de 180 avis, à valider sur la fiche Google)."),
 'boutique.html': ('Boutique de filtres', 'Boutique WooCommerce existante (filtres, produits). Pas encore maquettée.'),
 'thermopompes-murales.html': ('Thermopompes murales', 'Page produit : chauffer et climatiser sans conduits.'),
 'thermopompes-centrales.html': ('Thermopompes centrales', 'Page produit : une solution pour tout le bâtiment.'),
 'fournaises-electriques.html': ('Fournaises électriques', 'Page produit : vente et installation de fournaises électriques.'),
 'climatiseurs-centraux.html': ('Climatiseurs centraux', 'Page produit : climatiser toute la maison par les conduits.'),
 'geothermie-planchers-radiants.html': ('Géothermie et planchers radiants', 'Conception et installation de systèmes géothermiques et radiants.'),
 'qualite-de-l-air.html': ("Qualité de l'air", "Échangeurs d'air, humidificateurs, déshumidificateurs et purificateurs."),
 'guide-remplacer-thermopompe.html': ('Remplacer sa thermopompe : à quel prix?', 'Guide de prix à rafraîchir (article de 2023).'),
 'guide-humidificateur.html': ('Quel est le meilleur humidificateur?', 'Guide à rafraîchir (système de ventilation résidentiel : 5 378 impressions).'),
 'conditions-utilisation.html': ('Conditions d\'utilisation', 'Page légale existante du site actuel, à reprendre (hors menu principal).'),
 'politique-de-confidentialite.html': ('Politique de confidentialité', 'À rédiger (Loi 25) : responsable de la protection des renseignements personnels, finalités, conservation.'),
}

# ---------- gabarit commun ----------
base = open(ROOT + 'source-accueil-v21.template.html', encoding='utf-8').read()
s0 = base.index('\n<style>') + 8
CSS = re.sub(r'url\(\{\{IMG_[A-Z]+\}\}\)', 'none', base[s0: base.index('</style>')])
HEADER = base[base.index('<header class="site"'): base.index('</header>') + 9]
TAIL = base[base.index('<footer class="pied">'):]
EXTRA = open(ROOT + 'src/service-extra.css', encoding='utf-8').read() + open(ROOT + 'src/contact-extra.css', encoding='utf-8').read()
B = '/home/user/SkIz/assets/brand/svg/'
def svg(n): return 'data:image/svg+xml;base64,' + base64.b64encode(open(B + n, 'rb').read()).decode()
def jpg(n): return 'data:image/jpeg;base64,' + base64.b64encode(open(ROOT + 'img/' + n + '.jpg', 'rb').read()).decode()
IMGS = {'thermo': 'thermopompe', 'hero': 'hero', 'equipe': 'equipe', 'residentiel': 'residentiel', 'commercial': 'commercial', 'entretien': 'entretien', 'chauffage': 'chauffage', 'guide': 'guide-thermopompe'}
ARROW = '<svg class="ico fl" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<svg class="ico" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'

def shell(title, desc, body):
    head = f'''<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Bédard</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<link href="https://fonts.googleapis.com/css2?family=Mona+Sans:ital,wdth,wght@0,75..125,200..900&display=swap" rel="stylesheet">
<style>{CSS}
{EXTRA}
.hero-stub .bg{{display:none}}
</style>
</head>
<body>

'''
    html = head + HEADER + '\n\n' + body + '\n' + TAIL
    used = sorted(set(re.findall(r'var\(--img-([a-z]+)\)', html)))
    html = html.replace(':root{', ':root{' + ''.join(f'--img-{k}:url({jpg(IMGS[k])});' for k in used if k in IMGS), 1)
    star = '<svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/></svg>'
    html = (html.replace('{{SYMBOLE_BEIGE}}', svg('symbole-beige.svg')).replace('{{LOGO_HORIZ_BEIGE}}', svg('logo-enonce-horizontal-beige.svg'))
                .replace('{{LOGO_HORIZ_MARINE}}', svg('logo-enonce-horizontal-marine.svg')).replace('{{LOGO_ENONCE_BEIGE}}', svg('logo-enonce-horizontal-beige.svg')).replace('{{ETOILES}}', star * 5))
    return typo(add_css(html))

ICO = '<svg class="ico" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
def cards(items):
    return '<div class="lies">' + ''.join(f'<a class="lie reveal d{i%4}" href="{h}"><b>{t}</b><span>{d}</span><i>{ICO}</i></a>' for i, (h, t, d) in enumerate(items)) + '</div>'
def hero(h1, lead, badge, fil):
    return f'''<main>
<div class="hero hero-service hero-court hero-stub">
  <div class="bg"></div>
  <div class="wrap"><div>
    <nav class="fil" aria-label="Fil d'Ariane"><a href="#">Accueil</a><span>›</span><b>{fil}</b></nav>
    <div class="pastille reveal"><b>{CHECK}</b>{badge}</div>
    <h1 class="reveal d1">{h1}</h1>
    <p class="lead reveal d2">{lead}</p>
  </div></div>
</div>
'''
FINAL = f'''<div class="final"><div class="wrap">
  <h2 class="reveal">Un projet? Parlons-en.</h2>
  <p class="reveal d1">Un spécialiste Bédard vous rappelle sous 24 heures ouvrables.</p>
  <div class="cta reveal d2"><a class="btn btn-b" href="#">Demander une soumission {ARROW}</a></div>
  <a class="grosphone reveal d3" href="tel:+14507539426">450-753-9426</a>
</div></div>
</main>
'''
PAGES = {}   # nom -> html
for name, (h1, lead, intro, items) in HUBS.items():
    body = hero(h1, lead, 'Page hub (maquette)', h1) + f'<section><div class="wrap"><div class="tete"><div><span class="eyebrow">Explorer</span><h2 class="reveal">{h1}</h2></div><p class="reveal d1">{intro}</p></div>{cards(items)}</div></section>\n' + FINAL
    PAGES[name] = shell(h1, intro, body)
RELATED = [('thermopompe-installation.html', 'Installation de thermopompe', 'Une page déjà maquettée.'), ('climatiseur-mural-thermopompe.html', 'Climatiseur mural et thermopompe', 'La page pilier.'), ('commercial.html', 'Services commerciaux', 'Ventilation, réfrigération, ferblanterie.'), ('plan-du-site.html', 'Plan du site', 'Toutes les pages de la maquette.')]
for name, (h1, note) in STUBS.items():
    body = hero(h1, 'Cette page sera maquettée dans une prochaine étape, sur le même modèle que les autres.', 'Page à venir', h1) + f'<section><div class="wrap"><div class="programmes reveal"><span class="eyebrow">Maquette à venir</span><h2>{h1}</h2><p>{note}</p></div></div></section>\n<section class="fond-beige"><div class="wrap"><div class="tete"><div><span class="eyebrow">En attendant</span><h2 class="reveal">Voir les pages déjà maquettées</h2></div></div>{cards(RELATED)}</div></section>\n' + FINAL
    PAGES[name] = shell(h1, note, body)

# ---------- lecture des pages existantes ----------
for name, (src, _) in SRC.items():
    PAGES[name] = open(ROOT + src, encoding='utf-8').read()

# ---------- plan du site ----------
groups = [
 ('Pages entièrement maquettées', [(n, SRC[n][1]) for n in SRC]),
 ('Pages hub (simples, générées)', [(n, HUBS[n][0]) for n in HUBS]),
 ('Pages « à venir » (gabarit vide)', [(n, STUBS[n][0]) for n in STUBS]),
]
plan = ''.join(f'<h3 style="margin:2.2rem 0 1rem">{g}</h3>' + cards([(n, t, n) for n, t in items]) for g, items in groups)
PAGES['plan-du-site.html'] = shell('Plan du site', 'Toutes les pages de la maquette hors ligne.',
    hero('Plan du site', "Toutes les pages de la maquette, pour tester la navigation hors ligne.", 'Outil de test', 'Plan du site') + f'<section><div class="wrap">{plan}</div></section>\n' + FINAL)

# ---------- réécriture des liens ----------
def norm(t):
    t = re.sub(r'<[^>]+>', '', t)
    t = unicodedata.normalize('NFD', t)
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.sub(r'\s+', ' ', t.replace('’', "'")).strip().lower()
CONTACT = 'contact-climatisation-joliette.html'
RULES = [
 (r'^$', 'index.html'), (r'^accueil', 'index.html'),
 (r'voir tout le residentiel', 'residentiel.html'), (r'voir tout le commercial', 'commercial.html'), (r'voir tous les services', 'services.html'),
 (r'^urgence', 'reparation-thermopompe-climatiseur-joliette.html'),
 (r'politique de confidentialite', 'politique-de-confidentialite.html'),
 (r'^(avis|lire tous les avis|lire les avis)', 'avis.html'), (r'boutique', 'boutique.html'), (r'^blogue', 'blogue.html'),
 (r'^ferblantier\(ere\)', 'carrieres.html#ferblantier'), (r'voir le poste de ferblantier', 'carrieres.html#ferblantier'),
 (r'^frigoriste', 'carrieres.html#frigoriste'), (r'^magasinier', 'carrieres.html#magasinier'),
 (r'^dessinateur|voir les postes|^carrieres', 'carrieres.html'),
 (r'^contact', CONTACT), (r'^guides', 'blogue.html'),
 (r'remplacer (sa|une) thermopompe|guide : remplacer', 'guide-remplacer-thermopompe.html'),
 (r'humidificateur', 'guide-humidificateur.html'),
 (r"a quel prix s'attendre|lire le guide : climatiseur mural", 'prix-climatiseur-mural.html'),
 (r'climatiseur mural et thermopompe', 'climatiseur-mural-thermopompe.html'),
 (r'^climatiseurs? muraux?|^climatiseur mural|voir les climatiseurs muraux', 'climatiseur-mural-thermopompe.html'),
 (r'climatiseurs centraux|voir les climatiseurs centraux', 'climatiseurs-centraux.html'),
 (r'^(commercial|services commerciaux)', 'commercial.html'),
 (r'^01 refrigeration|refrigeration commerciale', 'refrigeration-commerciale-joliette.html'),
 (r'^02 ventilation|ventilation commerciale', 'ventilation-commerciale-joliette.html'),
 (r'^03 ferblanterie|^ferblanterie', 'ferblanterie-joliette.html'),
 (r"installation d'?(e|une) thermopompe|le plus demande|^thermopompe(?!s)", 'thermopompe-installation.html'),
 (r'thermopompes? centrales?|voir les thermopompes centrales', 'thermopompes-centrales.html'),
 (r'thermopompes? murales?|voir les thermopompes murales', 'thermopompes-murales.html'),
 (r'^chauffage', 'chauffage-auxiliaire-joliette.html'),
 (r'fournaises? electriques?', 'fournaises-electriques.html'),
 (r'geothermie', 'geothermie-planchers-radiants.html'),
 (r"qualite de l'air|ventilation et qualite|echangeurs? d'air|^ventilation$", 'qualite-de-l-air.html'),
 (r'^services', 'services.html'),
 (r'^residentiel', 'residentiel.html'),
 (r'entretien et nettoyage', 'entretien-nettoyage-thermopompe-climatiseur-joliette.html'),
 (r'reparation et depannage', 'reparation-thermopompe-climatiseur-joliette.html'),
 (r'^installation', 'thermopompe-installation.html'), (r'^reparation', 'reparation-thermopompe-climatiseur-joliette.html'), (r'^entretien', 'entretien-nettoyage-thermopompe-climatiseur-joliette.html'),
 (r'soumission|evaluation|parler a un specialiste|discuter de votre|demander', 'soumission.html'),
]
HASH_FALLBACK = {'#soumission': 'soumission.html', '#services': 'services.html', '#guides': 'blogue.html', '#avis': 'avis.html', '#carrieres': 'carrieres.html'}
unmapped = []
def rewrite(name, html):
    i = html.index('<body')
    head, body = html[:i], html[i:]
    ids = set(re.findall(r'\bid="([^"]+)"', body))
    def sub(m):
        attrs1, href, attrs2, inner = m.group(1), m.group(2), m.group(3), m.group(4)
        if href.startswith(('tel:', 'mailto:', 'http')) or 'data-envoyer' in attrs1 + attrs2 or 'data-poste' in attrs1 + attrs2 and href == '#postuler':
            return m.group(0)
        text = norm(inner)
        if href.startswith('#') and len(href) > 1 and href[1:] in ids:
            return m.group(0)
        if href == '#' or href.startswith('#'):
            target = None
            if href == '#univers':
                target = 'commercial.html' if text.startswith('commercial') else 'residentiel.html'
            elif href in HASH_FALLBACK:
                target = HASH_FALLBACK[href]
            else:
                for pat, tgt in RULES:
                    if re.search(pat, text): target = tgt; break
            if target is None:
                unmapped.append((name, href, text[:50])); return m.group(0)
            if target == name: target = '#'
            return f'<a{attrs1}href="{target}"{attrs2}>{inner}</a>'
        return m.group(0)
    body = re.sub(r'<a\b([^>]*?)href="([^"]*)"([^>]*)>(.*?)</a>', sub, body, flags=re.S)
    # menu principal : sur l'accueil aussi, les entrées ouvrent les pages au lieu de faire défiler la page
    if '<header class="site"' in body and name == 'index.html':
        k = body.index('</header>')
        hdr = body[:k]
        def nav(m):
            h = m.group(2); t = norm(m.group(4))
            tgt = {'#univers': 'commercial.html' if t.startswith('commercial') else 'residentiel.html', '#services': 'services.html', '#guides': 'blogue.html', '#avis': 'avis.html', '#carrieres': 'carrieres.html'}.get(h)
            return f'<a{m.group(1)}href="{tgt}"{m.group(3)}>{m.group(4)}</a>' if tgt else m.group(0)
        hdr = re.sub(r'<a\b([^>]*?)href="(#[a-z]+)"([^>]*)>(.*?)</a>', nav, hdr, flags=re.S)
        body = hdr + body[k:]
    return head + body
LEGAL_OLD = "<span>Confidentialité · Conditions d'utilisation</span>"
LEGAL_NEW = '<span><a href="politique-de-confidentialite.html">Confidentialité</a> · <a href="conditions-utilisation.html">Conditions d\'utilisation</a></span>'
for n in list(PAGES): PAGES[n] = rewrite(n, PAGES[n].replace(LEGAL_OLD, LEGAL_NEW))

# ---------- bouton « plan du site » (test seulement) ----------
PLAN_BTN = '''<style>.offline-plan{position:fixed;left:14px;bottom:14px;z-index:99999;background:#000014;color:#fff;font:600 13px/1 system-ui,sans-serif;padding:10px 14px;border-radius:999px;text-decoration:none;opacity:.85;box-shadow:0 4px 16px rgba(0,0,0,.3)}.offline-plan:hover{opacity:1}@media(max-width:720px){.offline-plan{bottom:70px}}</style><a class="offline-plan" href="plan-du-site.html">☰ Plan du site (test)</a>'''
for n in PAGES:
    if n != 'plan-du-site.html': PAGES[n] = PAGES[n].replace('</body>', PLAN_BTN + '\n</body>', 1)

# ---------- écriture : dossier, images, police ----------
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT + '/img'); os.makedirs(OUT + '/fonts')
def save_asset(kind, data):
    h = hashlib.sha1(data).hexdigest()[:10]
    fn = f'img/{kind}-{h}.{"jpg" if kind=="photo" else "svg"}'
    if not os.path.exists(OUT + '/' + fn): open(OUT + '/' + fn, 'wb').write(data)
    return fn
def externalize(html):
    html = re.sub(r'url\(data:image/jpeg;base64,([A-Za-z0-9+/=]+)\)', lambda m: f'url({save_asset("photo", base64.b64decode(m.group(1)))})', html)
    html = re.sub(r'data:image/svg\+xml;base64,([A-Za-z0-9+/=]+)', lambda m: save_asset('logo', base64.b64decode(m.group(1))), html)
    return html
# police Mona Sans (OFL), téléchargée une seule fois
css = urllib.request.urlopen(urllib.request.Request('https://fonts.googleapis.com/css2?family=Mona+Sans:ital,wdth,wght@0,75..125,200..900&display=swap', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'})).read().decode()
for u in sorted(set(re.findall(r'https://fonts\.gstatic\.com/[^)]+\.woff2', css))):
    fn = 'fonts/' + u.rsplit('/', 1)[1]
    open(OUT + '/' + fn, 'wb').write(urllib.request.urlopen(u).read())
    css = css.replace(u, fn.split('/', 1)[1])
open(OUT + '/fonts/mona-sans.css', 'w', encoding='utf-8').write(css)
for n, html in PAGES.items():
    html = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', html)
    html = re.sub(r'<link href="https://fonts\.googleapis\.com[^>]*>', '<link rel="stylesheet" href="fonts/mona-sans.css">', html)
    open(OUT + '/' + n, 'w', encoding='utf-8').write(externalize(html))

readme = open(ROOT + 'offline-LISEZ-MOI.txt', encoding='utf-8').read() if os.path.exists(ROOT + 'offline-LISEZ-MOI.txt') else ''
open(OUT + '/LISEZ-MOI.txt', 'w', encoding='utf-8').write(readme)
# ---------- zip ----------
if os.path.exists(ZIP): os.remove(ZIP)
folder = os.path.basename(OUT)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for dp, _, fs in os.walk(OUT):
        for f in sorted(fs):
            p = os.path.join(dp, f); z.write(p, os.path.join(folder, os.path.relpath(p, OUT)))
print(len(PAGES), 'pages |', len(os.listdir(OUT + '/img')), 'images |', round(os.path.getsize(ZIP) / 1048576, 1), 'Mo ->', ZIP)
print('liens non branchés:', len(unmapped))
for u in unmapped: print('  ', u)
