"""Pages produits générées à partir de data/catalogue-produits.json (extrait du Portail vendeur).
Sorties : produits-thermopompes-murales.html, produits-thermopompes-multizones.html, produits-climatiseur-mural.html,
produits-thermopompes-centrales.html, produits-echangeurs-air.html.  Usage : python3 -I build_produits.py"""
import base64, collections, json, re, sys
sys.path.insert(0, '/home/user/SkIz/maquettes')
from typo import typo, add_css
ROOT = '/home/user/SkIz/maquettes/'
B = '/home/user/SkIz/assets/brand/svg/'
def svg(n): return 'data:image/svg+xml;base64,' + base64.b64encode(open(B + n, 'rb').read()).decode()
CAT = json.load(open('/home/user/SkIz/data/catalogue-produits.json', encoding='utf-8'))
ARROW = '<svg class="ico fl" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARROW_I = '<svg class="ico" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<svg class="ico" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'
NB = ' '

# ---------- outils ----------
def num(s):
    m = re.search(r'\d+(?:\.\d+)?', str(s or '').replace(',', '.')); return float(m.group()) if m else None
def fr(v, dec=None):
    s = (f'{v:.{dec}f}' if dec is not None else (f'{v:.1f}'.rstrip('0').rstrip('.'))); return s.replace('.', ',')
def btu(entries):
    return sorted({int(num(x['cap'].replace(' ', '')) ) for x in entries if x.get('cap') and 'BTU' in x['cap']})
def btu_txt(vals): return ' · '.join(f'{v:,}'.replace(',', NB) for v in vals) + f'{NB}BTU'
def by_type(*types, marque=None):
    return [x for x in CAT if x['type'] in types and (marque is None or x['marque'] == marque)]
def common(vals):
    vals = [v for v in vals if v]; return collections.Counter(vals).most_common(1)[0][0] if vals else ''
def fiche(entries):
    urls = [x['ficheUrl'] for x in entries if x.get('ficheUrl') and 'supabase.co' not in x['ficheUrl']]
    return common(urls)
def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;').replace('"', '&quot;')

# Écarts constatés entre le portail et les fiches : valeurs retenues (voir docs/11-pages-produits.md)
EFF_OVERRIDE = {('Carrier', 'Thermopompe simple zone — Série Performance'): ("35", "15,6")}
def efficacite(entries, marque, type0):
    if (marque, type0) in EFF_OVERRIDE:
        s, h = EFF_OVERRIDE[(marque, type0)]; return f'SEER2{NB}jusqu’à{NB}{s} · HSPF2{NB}jusqu’à{NB}{h}'
    s = [num(x.get('seer')) for x in entries if x.get('seer') and '%' not in str(x['seer'])]
    h = [num(x.get('hspf')) for x in entries if x.get('hspf')]
    p = []
    if any(s): p.append(f'SEER2{NB}jusqu’à{NB}{fr(max(v for v in s if v))}')
    if any(h): p.append(f'HSPF2{NB}jusqu’à{NB}{fr(max(v for v in h if v))}')
    return ' · '.join(p) if p else 'Voir la fiche technique'

def serie_card(nom, sous_titre, types, marque, froid=None, extra=None, E=None, eff_key=None):
    E = E if E is not None else by_type(*types, marque=marque)
    assert E, (marque, types)
    froid = froid or common([x.get('froid') for x in E if x.get('froid') and x['froid'] not in ('—', 'n.d.')])
    rows = [('Capacités', btu_txt(btu(E)))]
    if any(x.get('seer') or x.get('hspf') for x in E): rows.append(('Efficacité', efficacite(E, marque, eff_key or types[0])))
    rows.append(('Garantie', esc(common([x['gar'] for x in E]))))
    v = [x for x in E if x.get('volt')]
    if (v and len(v) == len(E)) or '115' in nom + sous_titre: rows.append(('Alimentation', f'115{NB}V'))
    elif v: rows.append(('Alimentation', f'115{NB}V offert en {btu_txt(btu(v))}'))
    for k, v in (extra or []): rows.append((k, v))
    f = fiche(E)
    lien = f'<a class="lien-fiche" href="{esc(f)}" target="_blank" rel="noopener">Fiche technique du fabricant (PDF) {ARROW_I}</a>' if f else ''
    badge = f'<span class="badge-froid">{froid}</span>' if froid else ''
    dl = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows)
    return f'<article class="serie reveal"><header><h4>{nom}<span class="type">{sous_titre}</span></h4>{badge}</header><dl>{dl}</dl>{lien}</article>', E, froid

# ---------- gabarit de page ----------
def hero(fil, pastille, h1, lead, facts, note_facts, titre_carte):
    li = ''.join(f'<li><span>{a}</span><b>{b}</b></li>' for a, b in facts)
    return f'''<main>
<div class="hero hero-service hero-prod">
  <div class="bg"></div>
  <div class="wrap">
    <div>
      <nav class="fil" aria-label="Fil d'Ariane"><a href="#">Accueil</a><span>›</span><a href="#">Résidentiel</a><span>›</span><b>{fil}</b></nav>
      <div class="pastille reveal"><b>{CHECK}</b>{pastille}</div>
      <h1 class="reveal d1">{h1}</h1>
      <p class="lead reveal d2">{lead}</p>
      <div class="cta reveal d3">
        <a class="btn btn-b" href="#soumission">Demander une soumission {ARROW}</a>
        <a class="btn btn-l" href="tel:+14507539426" data-track="call_tracking">450-753-9426</a>
      </div>
    </div>
    <aside class="carte-chiffres reveal d2"><h2>{titre_carte}</h2><ul>{li}</ul><p class="note">{note_facts}</p></aside>
  </div>
</div>
'''
def section(eyebrow, h2, intro, corps, cls=''):
    p = f'<p class="reveal d1">{intro}</p>' if intro else ''
    return f'<section{(" class=" + chr(34) + cls + chr(34)) if cls else ""}><div class="wrap"><div class="tete"><div><span class="eyebrow">{eyebrow}</span><h2 class="reveal">{h2}</h2></div>{p}</div>{corps}</div></section>\n'
def faq(titre, qa):
    det = ''.join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(qa))
    return f'''<section id="faq"><div class="wrap faq-zone">
  <div><span class="eyebrow">Questions fréquentes</span><h2 class="reveal">{titre}</h2>
  <p class="reveal d1" style="margin-top:18px;color:var(--doux);max-width:24em">Une autre question? Appelez-nous au <a href="tel:+14507539426" style="color:var(--bleu);font-weight:700;text-decoration:none">450-753-9426</a>.</p></div>
  <div class="reveal d1">{det}</div>
</div></section>
'''
def lies(items):
    c = ''.join(f'<a class="lie reveal d{i}" href="#"><b>{t}</b><span>{d}</span><i>{ARROW_I}</i></a>' for i, (t, d) in enumerate(items))
    return f'<section class="fond-beige"><div class="wrap"><div class="tete"><div><span class="eyebrow">À consulter aussi</span><h2 class="reveal">Pour aller plus loin</h2></div></div><div class="lies">{c}</div></div></section>\n'
FINAL = f'''<div class="final"><div class="wrap">
  <h2 class="reveal">Le bon appareil, installé comme il faut.</h2>
  <p class="reveal d1">Un spécialiste Bédard évalue votre maison et vous remet une soumission détaillée gratuite.</p>
  <div class="cta reveal d2"><a class="btn btn-b" href="#soumission">Demander une soumission gratuite {ARROW}</a></div>
  <a class="grosphone reveal d3" href="tel:+14507539426" data-track="call_tracking">450-753-9426</a>
</div></div>
</main>
'''
NOTE_VALIDER = '<p class="note-valider reveal">Capacités, températures d’utilisation et garanties tirées de notre catalogue; cotes d’efficacité maximales publiées par les fabricants, selon le modèle. Les fiches techniques font foi. <em>[À valider contre les fiches avant publication]</em></p>'
NOTE_ALDES = '<p class="note-valider reveal">Débits et efficacités de récupération tirés de notre catalogue; les fiches techniques des modèles font foi. <em>[À valider contre les fiches avant publication]</em></p>'
def brand_block(marque, resume, cartes):
    return f'<div class="marque-bloc"><div class="marque-titre"><h3>{marque}</h3><span>{resume}</span></div><div class="series">{"".join(cartes)}</div></div>'
def jsonld(url, nom, desc, fil_nom, qa, series_noms):
    j = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": nom, "description": desc, "inLanguage": "fr-CA", "about": {"@id": "https://cbedard.com/#entreprise"}},
        {"@type": "ItemList", "name": nom, "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n} for i, n in enumerate(series_noms)]},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://cbedard.com/"}, {"@type": "ListItem", "position": 2, "name": "Résidentiel", "item": "https://cbedard.com/residentiel/"}, {"@type": "ListItem", "position": 3, "name": fil_nom}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": re.sub('<[^>]+>', '', q), "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in qa]}]}
    return json.dumps(j, ensure_ascii=False)

# ---------- assemblage ----------
base = open(ROOT + 'source-accueil-v21.template.html', encoding='utf-8').read()
s0 = base.index('\n<style>') + 8
css = re.sub(r'url\(\{\{IMG_[A-Z]+\}\}\)', 'none', base[s0: base.index('</style>')])
header = base[base.index('<header class="site"'): base.index('</header>') + 9]
tail = base[base.index('<footer class="pied">'):]
extra = open(ROOT + 'src/service-extra.css', encoding='utf-8').read() + open(ROOT + 'src/produits-extra.css', encoding='utf-8').read()
star = '<svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/></svg>'
def build(out, title, desc, canon, body, ld):
    assert len(title) <= 60 and len(desc) <= 160, (out, len(title), len(desc))
    html = f'''<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
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

''' + header + '\n\n' + body + '\n' + tail
    html = (html.replace('{{SYMBOLE_BEIGE}}', svg('symbole-beige.svg')).replace('{{LOGO_HORIZ_BEIGE}}', svg('logo-enonce-horizontal-beige.svg'))
            .replace('{{LOGO_HORIZ_MARINE}}', svg('logo-enonce-horizontal-marine.svg')).replace('{{LOGO_ENONCE_BEIGE}}', svg('logo-enonce-horizontal-beige.svg')).replace('{{ETOILES}}', star * 5))
    html = typo(add_css(html))
    left = re.findall(r'\{\{[A-Z_0-9]+\}\}', html)
    open(ROOT + out, 'w', encoding='utf-8').write(html)
    print(f'{out}: {len(html) // 1024} Ko | titre {len(title)} | desc {len(desc)} | restants {left}')

# =====================================================================
# 1. THERMOPOMPES MURALES (simple zone)
# =====================================================================
M = lambda *a, **k: serie_card(*a, **k)
mur = {}
mur['Mitsubishi'] = [
    M('Série FX', 'Thermopompe murale simple zone', ['Thermopompe simple zone — Série FX (-37°C)'], 'Mitsubishi'),
    M('Série GX', 'Grand froid, -37 °C', ['Thermopompe simple zone — Série GX (-37°C)'], 'Mitsubishi'),
    M('Série GX', 'Climat québécois, -25 °C', ['Thermopompe simple zone — Série GX (-25°C)'], 'Mitsubishi'),
    M('Série HX', 'Thermopompe murale simple zone', ['Thermopompe simple zone — Série HX'], 'Mitsubishi'),
    M('Série JX', 'Modèle 115 V', ['Thermopompe simple zone 115V — Série JX'], 'Mitsubishi'),
]
mur['Carrier'] = [
    M('Série Performance', 'Thermopompe murale simple zone', ['Thermopompe simple zone — Série Performance'], 'Carrier'),
    M('Série Confort MH', 'Thermopompe murale simple zone', ['Thermopompe simple zone — Série Confort MH'], 'Carrier'),
]
mur['Daikin'] = [
    M('Aurora', 'Thermopompe murale simple zone', ['Mural simple zone — Aurora'], 'Daikin'),
    M('Atmosphera', 'Thermopompe murale simple zone', ['Mural simple zone — Atmosphera'], 'Daikin'),
    M('Entra', 'Thermopompe murale simple zone', ['Mural simple zone — Entra'], 'Daikin'),
    M('Oterra', 'Thermopompe murale simple zone', ['Mural simple zone — Oterra'], 'Daikin'),
    M('Oterra 110 V', 'Modèle 110 V', ['Mural simple zone — Oterra 110 V'], 'Daikin'),
]
all_mur = [x for m in mur.values() for (_, E, _) in m for x in E]
n_series = sum(len(v) for v in mur.values())
caps = btu(all_mur)
froids = sorted({int(num(f)) for m in mur.values() for (_, _, f) in m if f}, reverse=True)   # valeurs positives (|-37| etc.)
bandes = collections.OrderedDict((t, []) for t in (15, 25, 37))
for m, lst in mur.items():
    for (html_c, E, f) in lst:
        nom = re.search(r'<h4>(.*?)<span class="type">(.*?)</span>', html_c)
        bandes[int(num(f))].append(f'{m} {nom.group(1)}' + (f' ({re.sub("&nbsp;| ", " ", nom.group(2))})' if '115' in nom.group(2) or '110' in nom.group(2) else ''))
band_html = ''
txt = {15: ('Jusqu’à -15 °C', 'Pour les journées froides d’automne et de printemps, ou comme appareil d’appoint de confort.'),
       25: ('Jusqu’à -25 °C', 'Le choix courant pour chauffer une grande partie de l’hiver québécois.'),
       37: ('Jusqu’à -37 °C', 'Pour les maisons plus exposées ou quand on veut compter le plus possible sur la thermopompe.')}
for t, noms in bandes.items():
    cls = ' fonce' if t == 37 else ''
    band_html += f'<div class="bande reveal{cls}"><span class="temp">-{t} °C</span><h3>{txt[t][0]}</h3><p>{txt[t][1]}</p><ul>{"".join(f"<li>{n}</li>" for n in noms)}</ul></div>'
corps_series = ''.join(brand_block(m, resume, [c for (c, _, _) in mur[m]]) for m, resume in [
    ('Mitsubishi', 'Cinq séries, de -25 °C à -37 °C'), ('Carrier', 'Deux séries'), ('Daikin', 'Cinq séries')])
garanties = [('Mitsubishi', common([x['gar'] for x in all_mur if x['marque'] == 'Mitsubishi'])), ('Carrier', common([x['gar'] for x in all_mur if x['marque'] == 'Carrier'])), ('Daikin', common([x['gar'] for x in all_mur if x['marque'] == 'Daikin']))]
qa_mur = [
    ('Quelle est la différence entre une thermopompe murale et un climatiseur mural?', 'Dans la pratique, aucune : on dit « climatiseur mural » par habitude, mais pratiquement tous les appareils muraux que nous installons sont des thermopompes. Elles climatisent l’été et chauffent le reste de l’année, sans conduits.'),
    ('Une thermopompe murale peut-elle chauffer par grand froid?', f'Oui, selon le modèle. Chaque série annonce une température minimale d’utilisation en chauffage, de -15 °C à -37 °C dans notre gamme. Le rendement baisse avec le froid, comme pour toute thermopompe; nous évaluons chez vous si un chauffage d’appoint est utile.'),
    ('Mitsubishi, Carrier ou Daikin : quelle marque choisir?', 'Les trois marques sont offertes et le bon choix dépend du froid à affronter, de la superficie à desservir, du budget et de la garantie. Nous recommandons un modèle après avoir évalué votre maison, pas avant.'),
    ('Quelle capacité (BTU) me faut-il?', 'À titre indicatif, une unité de 12 000 BTU convient à environ 1 000 pi² selon l’isolation, les fenêtres et l’aménagement. Nous calculons la capacité qui convient à votre maison; une unité trop grosse ou trop petite fonctionne moins bien.'),
    ('Combien coûte une thermopompe murale installée?', 'Pour une unité simple zone, comptez environ 3 500 $ à 5 300 $ avant taxes, installation comprise. Le prix varie selon la puissance, la série et l’installation. <em>[À valider avant publication]</em>'),
    ('Quelles sont les garanties?', f'Elles varient selon la marque et la série : {garanties[0][0]}, {garanties[0][1].lower()}; {garanties[1][0]}, {garanties[1][1].lower()}; {garanties[2][0]}, {garanties[2][1].lower()} (selon la série). <em>[À valider selon les conditions des fabricants]</em>'),
]
corps_cap = '''<div class="deux-col">
  <article class="bande reveal"><h3>Quelle capacité?</h3><p>À titre indicatif, une unité de 12&nbsp;000&nbsp;BTU convient à environ 1&nbsp;000 pi² selon l’isolation, les fenêtres et l’aménagement. Nous calculons la capacité qui convient à votre maison.</p><p><a class="lien" href="#" style="color:var(--bleu);font-weight:700">Voir le guide des prix</a></p></article>
  <article class="bande reveal d1"><h3>Simple zone ou multizone?</h3><p>Une unité simple zone dessert une zone ouverte. Un système multizone relie plusieurs unités intérieures à une seule unité extérieure.</p><p><a class="lien" href="#" style="color:var(--bleu);font-weight:700">Voir les thermopompes multizones</a></p></article>
</div>'''
body = (hero('Thermopompes murales', 'Mitsubishi · Carrier · Daikin', 'Thermopompes murales à <em>Joliette</em>',
             '<b>Aussi appelées climatiseurs muraux, elles chauffent et climatisent sans conduits.</b> Nous installons trois marques et plusieurs séries, du modèle courant à la thermopompe pour grand froid.',
             [('Séries offertes', str(n_series)), ('Marques', '3'), ('Capacités', f'{caps[0]:,}'.replace(',', NB) + f'{NB}à{NB}' + f'{caps[-1]:,}'.replace(',', NB) + f'{NB}BTU'), ('Froid supporté', f'jusqu’à -{froids[0]}{NB}°C')],
             'Gamme simple zone de notre catalogue, relevé de novembre 2026.', 'Notre gamme en bref')
        + section('Choisir selon le froid', 'Quelle température d’utilisation vous faut-il?', 'Température minimale d’utilisation en chauffage annoncée par le fabricant.', f'<div class="bandes-froid">{band_html}</div>')
        + section('Notre gamme', 'Les séries de thermopompes murales que nous installons', 'Chaque série existe en plusieurs capacités. Nous choisissons avec vous le modèle qui convient.', corps_series + NOTE_VALIDER, cls='fond-beige')
        + section('Bien choisir', 'Capacité et nombre de zones', '', corps_cap)
        + faq('Thermopompes murales : vos questions', qa_mur)
        + lies([('Installation de thermopompe', 'Déroulement, évaluation et soumission détaillée.'), ('Climatiseur mural ou thermopompe', 'Le guide pour comprendre la différence.'), ('Prix d’une thermopompe murale', 'Ce qui fait varier le prix installé.')])
        + FINAL)
build('produits-thermopompes-murales.html', 'Thermopompes murales à Joliette : nos séries | Bédard', 'Thermopompes murales (climatiseurs muraux) à Joliette : séries Mitsubishi, Carrier et Daikin, de -15 °C à -37 °C. Soumission gratuite.', 'https://cbedard.com/produits/chauffage/thermopompes-murales/', body,
      jsonld('https://cbedard.com/produits/chauffage/thermopompes-murales/', 'Thermopompes murales', 'Séries de thermopompes murales offertes par Bédard', 'Thermopompes murales', qa_mur,
             [f'{m} {re.search(r"<h4>(.*?)<span", c).group(1)}' for m, lst in mur.items() for (c, _, _) in lst]))

# =====================================================================
# 2. THERMOPOMPES MULTIZONES ET AUTRES UNITÉS INTÉRIEURES
# =====================================================================
def zones(E):
    z = sorted({int(m.group(1)) for x in E for m in [re.search(r'(\d) zones', x['type'])] if m}); return z
E_mxz = [x for x in CAT if x['marque'] == 'Mitsubishi' and x['type'].startswith('Multizone — Série MXZ')]
E_dai = [x for x in CAT if x['marque'] == 'Daikin' and x['type'].startswith('Mural multizone — Aurora')]
E_car = by_type('Thermopompe murale multizone — Série Performance MG', marque='Carrier')
zm, zd = zones(E_mxz), zones(E_dai)
mz = {
 'Mitsubishi': [serie_card('Série MXZ', f'Multizone, {zm[0]} à {zm[-1]} zones', [], 'Mitsubishi', froid='-20 °C ou -30 °C', E=E_mxz, eff_key='MXZ', extra=[('Zones', f'{zm[0]} à {zm[-1]}')])],
 'Carrier': [serie_card('Série Performance MG', 'Multizone', [], 'Carrier', E=E_car, eff_key='MG')],
 'Daikin': [serie_card('Aurora multizone', f'Multizone, {zd[0]} à {zd[-1]} zones', [], 'Daikin', froid='-20 °C ou -25 °C', E=E_dai, eff_key='AUR', extra=[('Zones', f'{zd[0]} à {zd[-1]}')])],
}
corps_mz = ''.join(brand_block(m, r, [c for (c, _, _) in mz[m]]) for m, r in [('Mitsubishi', 'Série MXZ'), ('Carrier', 'Série Performance MG'), ('Daikin', 'Aurora multizone')])
tbl = '''<table class="tableau-types reveal"><thead><tr><th>Type d’unité intérieure</th><th>Pour quoi faire</th><th>Séries offertes</th></tr></thead><tbody>
<tr><th>Murale</th><td>La plus courante : fixée en haut du mur.</td><td>Mitsubishi (FX, GX, HX, JX), Carrier (Performance, Confort MH), Daikin (Aurora, Atmosphera, Entra, Oterra), Stelpro (Élite-B, Pro-B)</td></tr>
<tr><th>Console au sol</th><td>Installée près du plancher, là où le haut du mur n’est pas disponible.</td><td>Mitsubishi (SUZ-AA, SUZ-CA), Carrier (Performance), Daikin (Aurora)</td></tr>
<tr><th>Cassette</th><td>Encastrée dans le plafond, à une ou quatre directions de soufflage.</td><td>Mitsubishi (1 voie et 4 voies), Carrier (Performance), Stelpro (SICB1)</td></tr>
<tr><th>Gainable</th><td>Cachée dans le plafond, avec de courtes conduites vers les pièces.</td><td>Stelpro (SFCB1)</td></tr>
</tbody></table>'''
qa_mz = [
    ('Qu’est-ce qu’un système multizone?', f'Une seule unité extérieure relie plusieurs unités intérieures ({zm[0]} à {zm[-1]} selon la série). Chaque pièce ou zone se règle séparément.'),
    ('Multizone ou plusieurs unités simple zone?', 'Les deux approches se valent selon la maison. Le multizone limite le nombre d’unités extérieures sur la façade; plusieurs unités simple zone donnent plus d’indépendance entre les zones. Nous comparons les deux pour votre plan.'),
    ('Peut-on combiner une murale, une console et une cassette?', 'Souvent oui, selon la série et la capacité de l’unité extérieure. Nous validons la compatibilité avant de vous remettre la soumission.'),
    ('Combien coûte un système multizone?', 'Le prix augmente avec le nombre de zones et le type d’unités. Nous ne publions pas de prix sans avoir évalué votre maison : la soumission est gratuite et détaillée.'),
]
body = (hero('Thermopompes multizones', 'Mitsubishi · Carrier · Daikin', 'Thermopompes <em>multizones</em> et unités intérieures au choix',
             '<b>Une seule unité extérieure, plusieurs zones à régler séparément.</b> Murales, consoles, cassettes ou gainables : on choisit le bon type d’unité pour chaque pièce.',
             [('Zones par système', f'{zm[0]} à {zm[-1]}'), ('Marques', '3'), ('Types d’unités', '4'), ('Froid supporté', f'jusqu’à -{max(int(num(x.get("froid"))) for x in E_mxz)}{NB}°C')],
             'Gamme multizone de notre catalogue, relevé de novembre 2026.', 'Multizone en bref')
        + section('Nos systèmes', 'Les séries multizones que nous installons', 'Une unité extérieure, plusieurs unités intérieures.', corps_mz + NOTE_VALIDER, cls='fond-beige')
        + section('Choisir le bon type', 'Quelle unité intérieure pour chaque pièce?', 'Les types d’unités intérieures de notre catalogue.', tbl)
        + faq('Multizone : vos questions', qa_mz)
        + lies([('Thermopompes murales', 'Les séries simple zone, par marque.'), ('Installation de thermopompe', 'Déroulement, évaluation et soumission détaillée.'), ('Thermopompes centrales', 'Pour une maison avec conduits.')])
        + FINAL)
build('produits-thermopompes-multizones.html', 'Thermopompes multizones à Joliette | Bédard', 'Thermopompes multizones à Joliette : Mitsubishi, Carrier, Daikin. Murales, consoles, cassettes et gainables. Soumission gratuite.', 'https://cbedard.com/produits/chauffage/thermopompes-multizones/', body,
      jsonld('https://cbedard.com/produits/chauffage/thermopompes-multizones/', 'Thermopompes multizones', 'Systèmes multizones et unités intérieures offerts par Bédard', 'Thermopompes multizones', qa_mz, ['Mitsubishi Série MXZ', 'Carrier Série Performance MG', 'Daikin Aurora multizone']))

# =====================================================================
# 3. CLIMATISEUR MURAL (refroidissement seulement)
# =====================================================================
cl = {
 'Mitsubishi': [serie_card('Série GX', 'Climatiseur mural simple zone', ['Climatiseur simple zone — Série GX'], 'Mitsubishi', froid='Refroidissement seul')],
 'Daikin': [serie_card('Oterra', 'Climatiseur mural simple zone', ['Climatiseur simple zone — Oterra'], 'Daikin', froid='Refroidissement seul')],
}
caps_cl = btu([x for m in cl.values() for (_, E, _) in m for x in E])
corps_cl = ''.join(brand_block(m, r, [c for (c, _, _) in cl[m]]) for m, r in [('Mitsubishi', 'Série GX'), ('Daikin', 'Oterra')])
comp = f'''<div class="deux-col">
  <article class="bande reveal"><h3>Climatiseur mural seul</h3><p>Il rafraîchit et déshumidifie l’air, sans conduits. Il ne chauffe pas.</p><ul><li>Refroidissement seulement</li><li>Sans conduits</li><li>{btu_txt(caps_cl[:1])} à {btu_txt(caps_cl[-1:])}</li></ul></article>
  <article class="bande fonce reveal d1"><h3>Thermopompe murale</h3><p>Elle climatise de la même façon et chauffe en plus, de l’automne au printemps. C’est ce que nous installons le plus souvent.</p><ul><li>Climatise et chauffe</li><li>Sans conduits</li><li>De -15 °C à -37 °C en chauffage</li></ul><p><a class="lien" href="#" style="color:var(--cyan);font-weight:700">Voir les thermopompes murales</a></p></article>
</div>'''
qa_cl = [
    ('Un climatiseur mural chauffe-t-il?', 'Non. Un climatiseur seul rafraîchit seulement. Pratiquement tous les appareils muraux que nous installons sont des thermopompes, qui chauffent aussi.'),
    ('Quand choisir un climatiseur seul plutôt qu’une thermopompe?', 'Quand on veut seulement rafraîchir et déshumidifier. Nous comparons les deux pour votre cas avant de recommander un modèle.'),
    ('Combien coûte un climatiseur mural installé?', 'Le prix dépend de la puissance, de la série et de l’installation. Notre guide des prix explique ce qui le fait varier.'),
]
body = (hero('Climatiseur mural', 'Refroidissement seulement', 'Climatiseur mural à <em>Joliette</em>',
             '<b>Un climatiseur mural rafraîchit et déshumidifie sans conduits. Il ne chauffe pas.</b> Pour la plupart des maisons, nous recommandons plutôt une thermopompe murale, qui climatise de la même façon et chauffe en plus.',
             [('Séries offertes', str(sum(len(v) for v in cl.values()))), ('Marques', '2'), ('Capacités', f'{caps_cl[0]:,}'.replace(',', NB) + f'{NB}à{NB}' + f'{caps_cl[-1]:,}'.replace(',', NB) + f'{NB}BTU'), ('Chauffage', 'Non')],
             'Climatiseurs seuls de notre catalogue, relevé de novembre 2026.', 'Notre gamme en bref')
        + section('Bien choisir', 'Climatiseur seul ou thermopompe murale?', 'La différence tient au chauffage.', comp)
        + section('Notre gamme', 'Les climatiseurs muraux que nous installons', 'Chaque série existe en plusieurs capacités.', corps_cl + NOTE_VALIDER, cls='fond-beige')
        + faq('Climatiseur mural : vos questions', qa_cl)
        + lies([('Thermopompes murales', 'Les séries qui chauffent et climatisent.'), ('Climatiseur mural ou thermopompe', 'Le guide pour comprendre la différence.'), ('Prix d’un climatiseur mural installé', 'Ce qui fait varier le prix.')])
        + FINAL)
build('produits-climatiseur-mural.html', 'Climatiseur mural à Joliette : modèles et choix | Bédard', 'Climatiseur mural (refroidissement seulement) à Joliette : séries Mitsubishi et Daikin. Comparez avec la thermopompe murale. Soumission gratuite.', 'https://cbedard.com/produits/climatisation-lanaudiere/climatiseur-mural/', body,
      jsonld('https://cbedard.com/produits/climatisation-lanaudiere/climatiseur-mural/', 'Climatiseur mural', 'Climatiseurs muraux (refroidissement seulement) offerts par Bédard', 'Climatiseur mural', qa_cl, ['Mitsubishi Série GX', 'Daikin Oterra']))

# =====================================================================
# 4. THERMOPOMPES CENTRALES
# =====================================================================
ce = {
 'Carrier': [serie_card('Crossover Performance', 'Thermopompe centrale', ['Thermopompe centrale — Crossover Performance'], 'Carrier')],
 'Daikin': [serie_card('Daikin Fit DH7', 'Thermopompe centrale', ['Thermopompe centrale — Daikin Fit DH7'], 'Daikin'), serie_card('Daikin Fit DH9', 'Thermopompe centrale', ['Thermopompe centrale — Daikin Fit DH9'], 'Daikin')],
 'Mitsubishi': [serie_card('SVZ-AP / SUZ-AK', 'Thermopompe centrale', ['Thermopompe centrale — SVZ-AP / SUZ-AK (-30°C)'], 'Mitsubishi'), serie_card('ZUBA Central', 'PVA-AA / PUZ-AK', ['ZUBA Central — PVA-AA / PUZ-AK (-30°C)'], 'Mitsubishi')],
}
all_ce = [x for m in ce.values() for (_, E, _) in m for x in E]
caps_ce = btu(all_ce)
corps_ce = ''.join(brand_block(m, r, [c for (c, _, _) in ce[m]]) for m, r in [('Carrier', 'Une série'), ('Daikin', 'Deux séries'), ('Mitsubishi', 'Deux séries, jusqu’à -30 °C')])
def kw(entries):
    v = [int(num(x['cap'])) for x in entries if x.get('cap') and 'KW' in x['cap'].upper()]; return (min(v), max(v)) if v else None
el = [x for x in CAT if x['type'].startswith('Élément électrique')]
kmin, kmax = kw(el)
acc = f'''<div class="acc-grille">
  <article class="acc reveal"><h4>Cabinets souffleurs</h4><p>Le ventilateur intérieur raccordé aux conduits.</p><ul><li>Carrier Crossover Performance</li><li>Daikin Fit (2 positions et multi-positions)</li><li>Mitsubishi PVA-AA et SVZ-AP</li><li>Stelpro Slim-B (SAHB1)</li></ul></article>
  <article class="acc reveal d1"><h4>Serpentins</h4><p>L’échangeur de chaleur installé avec le cabinet.</p><ul><li>Carrier Crossover Performance</li><li>Daikin Fit (A-coil et horizontal)</li></ul></article>
  <article class="acc reveal d2"><h4>Éléments électriques</h4><p>Une résistance électrique prend le relais par grand froid : de {kmin} à {kmax}{NB}kW selon le modèle.</p><ul><li>Carrier (EHKMC)</li><li>Stelpro (EAH)</li><li>Thermolec (pour Mitsubishi SVZ-AP et PVA-AA)</li></ul><p><a class="lien" href="#" style="color:var(--bleu);font-weight:700">Voir le chauffage d’appoint</a></p></article>
  <article class="acc reveal d3"><h4>Thermostats</h4><p>Pour régler et programmer le système.</p><ul><li>Carrier Côr (Wi-Fi)</li><li>Daikin One+ et One Touch</li><li>Sinopé TH6500WF</li><li>Mitsubishi PAR-42MAA (filaire)</li></ul></article>
</div>'''
qa_ce = [
    ('Thermopompe centrale ou thermopompe murale?', 'La centrale utilise les conduits de la maison pour desservir tous les espaces; la murale chauffe et climatise une zone sans conduits. Le bon choix dépend de la maison : nous évaluons chez vous.'),
    ('Faut-il changer mes conduits?', 'Pas nécessairement. Nous vérifions l’état et la capacité des conduits existants avant de recommander un système.'),
    ('Peut-on la combiner avec une fournaise ou un élément électrique?', 'Oui, selon la configuration. Un élément électrique dans le cabinet, ou un chauffage d’appoint, prend le relais par grand froid. Nous évaluons la meilleure combinaison pour votre maison.'),
    ('Quelle marque choisir?', 'Carrier, Daikin et Mitsubishi sont offertes. Le choix dépend de la maison, du froid à affronter, du budget et de la garantie; nous le faisons avec vous après l’évaluation.'),
]
body = (hero('Thermopompes centrales', 'Carrier · Daikin · Mitsubishi', 'Thermopompes centrales à <em>Joliette</em>',
             '<b>Une thermopompe qui utilise les conduits de votre maison.</b> Elle climatise l’été et chauffe le reste de l’année, pour toutes les pièces avec un seul système.',
             [('Séries offertes', str(sum(len(v) for v in ce.values()))), ('Marques', '3'), ('Capacités', f'{caps_ce[0]:,}'.replace(',', NB) + f'{NB}à{NB}' + f'{caps_ce[-1]:,}'.replace(',', NB) + f'{NB}BTU'), ('Froid supporté', f'jusqu’à -30{NB}°C')],
             'Gamme centrale de notre catalogue, relevé de novembre 2026.', 'Notre gamme en bref')
        + section('Notre gamme', 'Les thermopompes centrales que nous installons', 'Chaque série existe en plusieurs capacités.', corps_ce + NOTE_VALIDER, cls='fond-beige')
        + section('Accessoires', 'Ce qui complète une thermopompe centrale', 'Cabinets, serpentins, éléments électriques et thermostats de notre catalogue.', acc)
        + faq('Thermopompes centrales : vos questions', qa_ce)
        + lies([('Chauffage d’appoint', 'Le relais de votre thermopompe quand il fait très froid.'), ('Thermopompes murales', 'Pour chauffer et climatiser sans conduits.'), ('Installation de thermopompe', 'Déroulement, évaluation et soumission détaillée.')])
        + FINAL)
build('produits-thermopompes-centrales.html', 'Thermopompes centrales à Joliette : Carrier, Daikin | Bédard', 'Thermopompes centrales à Joliette : Carrier, Daikin et Mitsubishi, avec cabinets, éléments électriques et thermostats. Soumission gratuite.', 'https://cbedard.com/produits/chauffage/thermopompes-centrales/', body,
      jsonld('https://cbedard.com/produits/chauffage/thermopompes-centrales/', 'Thermopompes centrales', 'Thermopompes centrales offertes par Bédard', 'Thermopompes centrales', qa_ce, ['Carrier Crossover Performance', 'Daikin Fit DH7', 'Daikin Fit DH9', 'Mitsubishi SVZ-AP / SUZ-AK', 'Mitsubishi ZUBA Central']))

# =====================================================================
# 5. ÉCHANGEURS D'AIR (Aldes)
# =====================================================================
ald = [x for x in CAT if x['marque'] == 'Aldes' and x['type'].startswith('Échangeur')]
ctl = [x for x in CAT if x['marque'] == 'Aldes' and not x['type'].startswith('Échangeur')]
rows = ''.join(f'<tr><th>{x["modele"]}</th><td>{"VRC" if "VRC" in x["type"] else "VRE"}</td><td>{x["cap"].replace(" PCM", NB + "pi³/min")}</td><td>{x["seer"].replace(" SRE", NB + "%").replace(" %", NB + "%") if False else x["seer"].replace(" % SRE", NB + "%")}</td></tr>' for x in ald)
tab_al = f'<table class="tableau-types reveal"><thead><tr><th>Modèle Aldes</th><th>Type</th><th>Débit</th><th>Efficacité de récupération (SRE)</th></tr></thead><tbody>{rows}</tbody></table>'
vv = f'''<div class="deux-col">
  <article class="bande reveal"><h3>VRC : récupérateur de chaleur</h3><p>Il récupère la chaleur de l’air extrait pour préchauffer l’air neuf qui entre. Il évacue aussi l’humidité de la maison.</p></article>
  <article class="bande fonce reveal d1"><h3>VRE : récupérateur d’énergie</h3><p>Il récupère la chaleur et une partie de l’humidité. Utile quand l’air intérieur devient trop sec l’hiver.</p></article>
</div>'''
ctls = ''.join(f'<article class="acc reveal d{i}"><h4>{n}</h4><p>{esc(x["desc"])}</p></article>' for i, (n, x) in enumerate(zip(['Contrôle mural multifonction', 'Hygromètre-thermostat LCD', 'Minuterie de salle de bain'], ctl)))
acc_al = f'<div class="acc-grille acc-3">{ctls}</div>'
qa_al = [
    ('VRC ou VRE : lequel choisir?', 'Le VRC récupère la chaleur; le VRE récupère la chaleur et une partie de l’humidité. Nous recommandons selon l’humidité de la maison, le nombre d’occupants et le système de chauffage.'),
    ('Quelle capacité (pi³/min) me faut-il?', f'Nos modèles vont de {min(int(num(x["cap"])) for x in ald)} à {max(int(num(x["cap"])) for x in ald)}{NB}pi³/min. La bonne capacité dépend de la superficie, du nombre de pièces et de chambres : nous la calculons chez vous.'),
    ('Les échangeurs Aldes sont-ils homologués Energy Star?', 'Notre catalogue les indique comme homologués Energy Star. <em>[À valider contre les fiches des modèles]</em>'),
    ('Comment entretenir un échangeur d’air?', 'Les filtres se nettoient ou se remplacent régulièrement, et le noyau s’entretient une à deux fois par an. Nous offrons l’entretien et vendons des filtres Aldes dans notre boutique. <em>[Fréquence à valider]</em>'),
]
body = (hero('Échangeurs d’air', 'Aldes · VRC et VRE', 'Échangeurs d’air à <em>Joliette</em>',
             '<b>Un air neuf et sain dans toute la maison, sans perdre la chaleur.</b> Nous installons les échangeurs d’air Aldes, avec récupération de chaleur (VRC) ou d’énergie (VRE).',
             [('Modèles Aldes', str(len(ald))), ('Débits', f'{min(int(num(x["cap"])) for x in ald)} à {max(int(num(x["cap"])) for x in ald)}{NB}pi³/min'), ('Récupération', f'jusqu’à {max(int(num(x["seer"])) for x in ald)}{NB}%'), ('Contrôles', str(len(ctl)))],
             'Gamme Aldes de notre catalogue, relevé de novembre 2026.', 'Notre gamme en bref')
        + section('Bien choisir', 'VRC ou VRE?', 'Deux types d’échangeurs d’air.', vv)
        + section('Notre gamme', 'Les échangeurs d’air Aldes', 'Débit et efficacité de récupération selon le modèle.', tab_al + NOTE_ALDES, cls='fond-beige')
        + section('Contrôles', 'Les commandes qui vont avec', 'Pour régler et automatiser la ventilation.', acc_al)
        + faq('Échangeurs d’air : vos questions', qa_al)
        + lies([('Filtres Aldes', 'Nos filtres de remplacement et haute efficacité.'), ('Entretien et nettoyage', 'Un entretien périodique personnalisé.'), ('Quel est le meilleur système de ventilation résidentiel?', 'Le guide pour comprendre et choisir.')])
        + FINAL)
build('produits-echangeurs-air.html', 'Échangeurs d’air à Joliette : VRC et VRE Aldes | Bédard', 'Échangeurs d’air Aldes à Joliette : VRC et VRE, débits de 88 à 218 pi³/min, contrôles. Installation et entretien. Soumission gratuite.', 'https://cbedard.com/produits/qualite-de-lair/echangeurs-dair/', body,
      jsonld('https://cbedard.com/produits/qualite-de-lair/echangeurs-dair/', 'Échangeurs d’air', 'Échangeurs d’air Aldes offerts par Bédard', 'Échangeurs d’air', qa_al, [x['modele'] for x in ald]))
