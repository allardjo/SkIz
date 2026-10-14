"""Fabrique source-accueil-v3.template.html (version sobre) à partir du gabarit v2 :
nouvel en-tête (menus déroulants), nouveau pied de page, nouvelle accueil à 6 blocs, CSS de calme."""
import re, sys
sys.path.insert(0, 'src')
from v3_blocks import avis_block
t = open('source-accueil-v2.template.html', encoding='utf-8').read()

ARR = '<svg class="ico fl" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
TELSVG = '<svg class="ico" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
CHEV = '<svg class="ico chev" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>'

MENUS = [
 ('Résidentiel', 'Voir tout le résidentiel', ['Installation de thermopompe', 'Climatiseur mural et thermopompe', "Chauffage d'appoint", 'Climatiseurs centraux', 'Fournaises électriques', "Qualité de l'air", 'Géothermie et planchers radiants']),
 ('Commercial', 'Voir tout le commercial', ['Ventilation commerciale', 'Réfrigération commerciale', 'Ferblanterie']),
 ('Services', 'Voir tous les services', ['Réparation et dépannage', 'Entretien et nettoyage', 'Urgence 24 h']),
]
nav = ''
for top, allt, items in MENUS:
    nav += f'<div class="m-item"><a class="m-top" href="#">{top}{CHEV}</a><div class="m-drop">' + ''.join(f'<a href="#">{i}</a>' for i in items) + f'<a class="m-all" href="#">{allt} {ARR}</a></div></div>'
nav += '<a class="m-top" href="#">Blogue</a><a class="m-top" href="#">Carrières</a>'
mob = ''
for top, allt, items in MENUS:
    mob += f'<details><summary>{top}</summary>' + ''.join(f'<a href="#">{i}</a>' for i in items) + f'<a href="#">{allt}</a></details>'
mob += '<a class="m-simple" href="#">Blogue</a><a class="m-simple" href="#">Carrières</a><a class="m-simple" href="#">Contact</a>'

HEADER = f'''<header class="site" id="entete">
  <div class="wrap barre">
    <a class="logo" href="#" aria-label="Bédard — Performance thermique"><img class="on-dark" src="{{{{LOGO_HORIZ_BEIGE}}}}" alt="Bédard, performance thermique"><img class="on-light" src="{{{{LOGO_HORIZ_MARINE}}}}" alt=""></a>
    <nav class="principal" aria-label="Navigation principale">{nav}</nav>
    <div class="actions">
      <a class="tel" href="tel:+14507539426">{TELSVG}<span><small>Urgence 24 h</small>450-753-9426</span></a>
      <a class="btn btn-r" href="#soumission">Demander une soumission</a>
      <button class="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="menu-mobile"><svg class="ico ouvre" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></svg><svg class="ico ferme" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
    </div>
  </div>
  <div class="m-mobile" id="menu-mobile">{mob}<a class="btn btn-r" href="#soumission">Demander une soumission</a></div>
</header>'''

MAIN = f'''<main>
<!-- ================= 1. HERO ================= -->
<div class="hero hero3">
  <div class="wrap">
    <h1 class="reveal">Chauffage, climatisation et ventilation à <em>Joliette</em></h1>
    <p class="lead reveal d1"><b>Le chef de file régional du confort thermique.</b> Plus de 40 ans d'expertise, pour votre maison comme pour votre commerce.</p>
    <div class="cta reveal d2">
      <a class="btn btn-b" href="#soumission">Demander une soumission {ARR}</a>
      <a class="lien-tel" href="tel:+14507539426">{TELSVG}Urgence 24 h : 450-753-9426</a>
    </div>
  </div>
</div>

<div class="devis-zone"><div class="wrap">
  <form class="devis reveal" id="soumission" action="#" onsubmit="return false">
    <div class="tt"><h2>Soumission rapide</h2><p>Trois informations, un spécialiste vous rappelle.</p></div>
    <div class="champ"><label for="nom">Nom</label><input id="nom" name="nom" autocomplete="name" placeholder="Votre nom"></div>
    <div class="champ"><label for="tel">Téléphone</label><input id="tel" name="tel" type="tel" autocomplete="tel" placeholder="450 000-0000"></div>
    <div class="champ"><label for="svc">Je cherche</label>
      <select id="svc" name="svc"><option>Une thermopompe</option><option>Un climatiseur mural</option><option>Une réparation ou un dépannage</option><option>Un entretien ou un nettoyage</option><option>De la ventilation</option><option>Du chauffage</option><option>Un projet commercial</option><option>Autre</option></select></div>
    <button class="btn btn-r" type="submit">Être rappelé {ARR}</button>
  </form>
</div></div>


<!-- ================= CHIFFRES ================= -->
<section class="chiffres3"><div class="wrap">
  <div class="c3 reveal"><b><span data-count="65">65</span><i>+</i></b><span>professionnels<br>à votre service</span></div>
  <div class="c3 reveal d1"><b><span data-count="40">40</span><i>+</i></b><span>ans d'expertise<br>en confort thermique</span></div>
  <div class="c3 reveal d2"><b><span data-count="24">24</span><i>h</i></b><span>service d'urgence<br>jour et nuit</span></div>
</div></section>

<!-- ================= 2. DEUX UNIVERS ================= -->
<section id="univers" class="sec3"><div class="wrap">
  <h2 class="titre3 reveal">Pour la maison ou pour le bâtiment</h2>
  <div class="deux3">
    <a class="pan reveal" href="#"><div class="photo" style="background-image:url({{{{IMG_RESIDENTIEL}}}})"></div><div class="txt"><h3>Résidentiel</h3><p>Thermopompes, climatisation, chauffage et qualité de l'air pour votre maison.</p><span class="go">Découvrir {ARR}</span></div></a>
    <a class="pan reveal d1" href="#"><div class="photo" style="background-image:url({{{{IMG_COMMERCIAL}}}})"></div><div class="txt"><h3>Commercial</h3><p>Ventilation, réfrigération et ferblanterie pour les commerces, les industries et les institutions.</p><span class="go">Découvrir {ARR}</span></div></a>
  </div>
</div></section>

<!-- ================= 3. SERVICES ================= -->
<section id="services" class="svc3"><div class="wrap">
  <div class="svc3-tete reveal"><h2>Nos services</h2><span>Un seul interlocuteur, de l'installation à l'entretien.</span></div>
  <div class="svc3-grille">
    <a class="svc reveal" href="#"><span class="ico-g"><svg class="ico" viewBox="0 0 24 24"><path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"/></svg></span><b>Installation</b><small>Thermopompe, climatisation</small>{ARR}</a>
    <a class="svc reveal d1" href="#"><span class="ico-g"><svg class="ico" viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg></span><b>Réparation</b><small>Dépannage, urgence 24 h</small>{ARR}</a>
    <a class="svc reveal d2" href="#"><span class="ico-g"><svg class="ico" viewBox="0 0 24 24"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg></span><b>Entretien</b><small>Nettoyage, programme périodique</small>{ARR}</a>
    <a class="svc reveal d3" href="tel:+14507539426"><span class="ico-g"><svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></span><b>Urgence 24 h</b><small>450-753-9426</small>{ARR}</a>
  </div>
</div></section>

<!-- ================= 4. AVIS ================= -->
{{AVIS}}

<!-- ================= 5. CARRIÈRES ================= -->
<section class="carr3"><div class="wrap">
  <div class="reveal"><b>Rejoignez une équipe de plus de 65 professionnels.</b><span>3 postes ouverts : ferblantier, frigoriste, magasinier.</span></div>
  <a class="btn btn-m reveal d1" href="#">Voir les postes {ARR}</a>
</div></section>

<!-- ================= 6. APPEL FINAL ================= -->
<div class="final"><div class="wrap">
  <h2 class="reveal">Parlons de votre projet.</h2>
  <p class="reveal d1">Un spécialiste Bédard vous répond, que ce soit pour une soumission ou pour une urgence.</p>
  <div class="cta reveal d2"><a class="btn btn-b" href="#soumission">Demander une soumission {ARR}</a></div>
  <a class="grosphone reveal d3" href="tel:+14507539426">450-753-9426</a>
</div></div>
</main>'''

FOOTER = f'''<footer class="pied"><div class="wrap">
  <div class="grille grille3">
    <div><img class="logo" src="{{{{LOGO_ENONCE_BEIGE}}}}" alt="Bédard, performance thermique"><p>304, boulevard de l'Industrie<br>Joliette (Québec) J6E 8V2</p><p><a href="tel:+14507539426">450-753-9426</a><br><a href="mailto:info@cbedard.com">info@cbedard.com</a></p></div>
    <div><h4>Résidentiel</h4><ul><li><a href="#">Installation de thermopompe</a></li><li><a href="#">Climatiseur mural</a></li><li><a href="#">Chauffage d'appoint</a></li><li><a href="#">Réparation et dépannage</a></li><li><a href="#">Entretien et nettoyage</a></li></ul></div>
    <div><h4>Commercial</h4><ul><li><a href="#">Ventilation commerciale</a></li><li><a href="#">Réfrigération commerciale</a></li><li><a href="#">Ferblanterie</a></li></ul></div>
    <div><h4>Entreprise</h4><ul><li><a href="#">Blogue</a></li><li><a href="#">Avis clients</a></li><li><a href="#">Carrières</a></li><li><a href="#">Contact</a></li></ul></div>
  </div>
  <div class="legal"><span>© 2026 Entreprise De Réfrigération &amp; Climatisation Claude Bédard (1995) Inc. Tous droits réservés.</span><span>Confidentialité · Conditions d'utilisation</span></div>
</div></footer>'''

MAIN = MAIN.replace('{AVIS}', avis_block())
# --- remplacements ---
a, b = t.index('<header class="site"'), t.index('</header>') + 9
t = t[:a] + HEADER + t[b:]
a, b = t.index('<main>'), t.index('</main>') + 7
t = t[:a] + MAIN + t[b:]
a, b = t.index('<footer class="pied">'), t.index('</footer>') + 9
t = t[:a] + FOOTER + t[b:]
# JSON-LD : plus de FAQ visible sur l'accueil
t = re.sub(r',\n\{"@type":"FAQPage".*?\]\}\n(?=\]\})', '\n', t, flags=re.S)

V3CSS = r'''
/* ===================== VERSION SOBRE (v3) ===================== */
section{padding:clamp(5.5rem,10vw,10rem) 0}
.sec3{padding:clamp(5.5rem,10vw,10rem) 0}
.sec3-ciel{background:#f3f8f9}
.titre3{font-size:clamp(2.2rem,4.2vw,3.6rem);letter-spacing:-.03em;font-stretch:86%;max-width:14em;margin-bottom:3rem}
.intro3{color:var(--doux);font-size:1.2rem;max-width:22em}
/* en-tête : une seule barre, menus déroulants */
header.site .barre{height:5.5rem}
nav.principal{align-items:center;gap:.25rem}
nav.principal .m-top{display:inline-flex;align-items:center;gap:.35rem}
nav.principal .chev{width:.9rem;height:.9rem;stroke-width:2.5;transition:transform .2s}
.m-item{position:relative}
.m-item:hover .chev,.m-item:focus-within .chev{transform:rotate(180deg)}
.m-drop{position:absolute;top:100%;left:-.6rem;min-width:19.5rem;padding:.9rem .6rem .6rem;background:#fff;border-radius:1.2rem;box-shadow:0 1.6rem 3.6rem rgba(0,30,50,.22);opacity:0;visibility:hidden;transform:translateY(.5rem);transition:opacity .2s,transform .2s,visibility .2s;z-index:5}
.m-item:hover .m-drop,.m-item:focus-within .m-drop{opacity:1;visibility:visible;transform:none}
nav.principal .m-drop a{display:flex;color:var(--marine)!important;background:none;border-radius:.8rem;padding:.7rem .9rem;font-weight:500}
nav.principal .m-drop a:hover{background:#eef3f4}
nav.principal .m-drop .m-all{margin-top:.3rem;border-top:1px solid #e1e8ea;border-radius:0 0 .8rem .8rem;color:var(--bleu)!important;font-weight:700;gap:.5rem;align-items:center}
.tel small{display:block;font-size:.7rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;opacity:.75;line-height:1.1}
.tel>span{line-height:1.15}
.burger{border:0;cursor:pointer}
.burger .ferme{display:none}
header.site.open .burger .ouvre{display:none}header.site.open .burger .ferme{display:block}
.m-mobile{display:none}
/* hero sobre */
.hero3{padding:clamp(9.5rem,19vh,13.5rem) 0 clamp(8rem,15vh,11rem);background:linear-gradient(160deg,#00263b 0%,#003650 55%,#00496b 100%)}
.hero3::before{content:"";display:block;position:absolute;inset:0;left:0;top:0;right:0;bottom:0;width:auto;height:auto;background:var(--img-hero) 100% 40%/cover no-repeat;transform:scaleX(-1);opacity:.8}
.hero3::after{content:"";display:block;position:absolute;inset:0;left:0;top:0;right:0;bottom:0;width:auto;height:auto;border-radius:0;background:linear-gradient(95deg,rgba(0,24,40,.97) 0%,rgba(0,38,58,.86) 40%,rgba(0,54,80,.2) 100%)}
.hero3 .wrap{display:block}
.hero3 h1{max-width:12.5em;font-size:clamp(3rem,6.2vw,5.6rem)}
.hero3 p.lead{max-width:30em;margin-bottom:2.6rem}
.hero3 .cta{align-items:center;gap:1.8rem}
.lien-tel{display:inline-flex;gap:.6rem;align-items:center;color:#fff;font-weight:600;text-decoration:none;padding:.4rem 0;border-bottom:1px solid rgba(255,255,255,.4)}
.lien-tel:hover{border-color:#fff}.lien-tel .ico{color:var(--cyan)}
.stats3{display:flex;gap:clamp(2rem,5vw,5rem);flex-wrap:wrap;margin-top:clamp(3.5rem,8vh,5.5rem);padding-top:2rem;border-top:1px solid rgba(255,255,255,.22);max-width:44rem}
.stats3 b{display:block;font-family:var(--font-titre);font-size:clamp(2.2rem,3.6vw,3.2rem);font-weight:800;line-height:1;letter-spacing:-.03em;font-stretch:84%;color:#fff}
.stats3>div>span{display:block;margin-top:.45rem;font-size:.92rem;color:#c3d6dc}
.stats3 b span{display:inline;margin:0;font:inherit;color:inherit;letter-spacing:inherit}
/* deux univers */
.deux3{display:grid;grid-template-columns:1fr 1fr;gap:1.6rem}
.pan{position:relative;min-height:clamp(26rem,48vw,36rem);border-radius:1.9rem;overflow:hidden;color:#fff;display:flex;align-items:flex-end;text-decoration:none;isolation:isolate}
.pan .photo{position:absolute;inset:0;z-index:-2;background-size:cover;background-position:center;transition:transform 1.1s cubic-bezier(.2,.7,.2,1)}
.pan::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(0,20,40,0) 30%,rgba(0,30,50,.94) 100%)}
.pan:hover .photo{transform:scale(1.05)}
.pan .txt{padding:clamp(1.8rem,3.4vw,3rem)}
.pan h3{color:#fff;font-size:clamp(2.2rem,3.6vw,3.2rem);font-stretch:86%;margin-bottom:.8rem}
.pan p{color:#d7e6ea;max-width:26em;margin-bottom:1.4rem}
.pan .go{display:inline-flex;gap:.7rem;align-items:center;font-weight:700}
.pan:hover .go .fl{transform:translateX(.35rem)}
/* services en liste */
.duo3{display:grid;grid-template-columns:.8fr 1.2fr;gap:clamp(2rem,6vw,6rem);align-items:start}
.duo3 .titre3{margin-bottom:1.2rem}
.rangs{border-top:1px solid #cfdadd}
.rang{display:grid;grid-template-columns:1fr auto;grid-template-areas:"t i" "d i";gap:.2rem 1.5rem;align-items:center;padding:1.7rem .2rem;border-bottom:1px solid #cfdadd;text-decoration:none;transition:padding .25s,background .25s}
.rang b{grid-area:t;font-size:clamp(1.3rem,2vw,1.7rem);color:var(--marine);letter-spacing:-.02em;font-family:var(--font-titre);font-weight:800;font-stretch:90%}
.rang span{grid-area:d;color:var(--doux)}
.rang i{grid-area:i;width:3rem;height:3rem;border-radius:50%;display:grid;place-items:center;background:var(--beige);color:var(--marine);transition:transform .3s}
.rang:hover{padding-left:1rem;background:rgba(255,255,255,.7)}
.rang:hover i{transform:translateX(.3rem)}
/* preuve */
.preuve3{background:var(--marine);color:#fff;padding:clamp(5rem,9vw,8.5rem) 0;position:relative;overflow:hidden}
.preuve3::before{content:"";position:absolute;left:-12rem;top:-8rem;width:40rem;height:48rem;background:url({{SYMBOLE_BEIGE}}) no-repeat center/contain;opacity:.05}
.preuve3 .wrap{position:relative;max-width:62rem}
.note3{display:flex;gap:1.2rem;align-items:center;margin-bottom:2rem;color:#c3d6dc}
.note3 b{font-family:var(--font-titre);font-size:3.2rem;color:#fff;font-weight:800;letter-spacing:-.03em;font-stretch:84%}.note3 small{font-size:1.4rem;opacity:.7}
.preuve3 blockquote{font-size:clamp(1.6rem,3vw,2.5rem);line-height:1.25;font-weight:500;letter-spacing:-.015em;color:#fff}
.cite3{display:flex;gap:.9rem;align-items:center;margin-top:2rem;color:#c3d6dc;flex-wrap:wrap}
.cite3 .av{width:2.75rem;height:2.75rem;border-radius:50%;background:var(--cyan);color:var(--marine);display:grid;place-items:center;font-weight:800}
.cite3 .lien{margin-left:auto;color:var(--ciel);font-weight:700}
.voir-aussi{margin-top:2.4rem;color:var(--doux);font-size:1rem;display:flex;flex-wrap:wrap;gap:.5rem 1.4rem}
.voir-aussi a{color:var(--bleu);font-weight:600;text-decoration:none}
.voir-aussi a:hover{text-decoration:underline}
.sec3.fond-beige{background:var(--beige)}
/* carrières */
.carr3{background:var(--beige);padding:2.6rem 0}
.carr3 .wrap{display:flex;gap:2rem;align-items:center;justify-content:space-between;flex-wrap:wrap}
.carr3 b{display:block;font-size:clamp(1.3rem,2vw,1.7rem);color:var(--marine);letter-spacing:-.02em}
.carr3 span{color:var(--doux)}
/* pied de page sobre */
footer.pied .grille3{grid-template-columns:1.3fr 1fr 1fr 1fr}
footer.pied p{margin-bottom:1rem;line-height:1.6}
'''+open('src/v31.css',encoding='utf-8').read()+r'''
@media (max-width:1100px){
  .deux3,.duo3{grid-template-columns:1fr}
  header.site .m-mobile{display:none;position:absolute;left:0;right:0;top:100%;background:#fff;box-shadow:0 1.6rem 2.6rem rgba(0,30,50,.18);padding:1rem var(--gut) 1.6rem;max-height:calc(100vh - 5.5rem);overflow:auto}
  header.site.open .m-mobile{display:block}
  .m-mobile summary{cursor:pointer;font-weight:700;color:var(--marine);padding:1rem 0;border-bottom:1px solid #e1e8ea;font-size:1.1rem;list-style:none;display:flex;justify-content:space-between;font-stretch:100%}
  .m-mobile summary::-webkit-details-marker{display:none}.m-mobile summary::after{content:"+";font-weight:400;color:var(--bleu)}
  .m-mobile details[open] summary::after{content:"–"}
  .m-mobile details a{display:block;padding:.75rem 0 .75rem .8rem;color:var(--texte);text-decoration:none}
  .m-mobile .m-simple{display:block;padding:1rem 0;border-bottom:1px solid #e1e8ea;font-weight:700;color:var(--marine);text-decoration:none;font-size:1.1rem}
  .m-mobile .btn{margin-top:1.2rem;width:100%}
  header.site.open{background:#fff}header.site.open .logo .on-light{opacity:1}header.site.open .logo .on-dark{opacity:0}
  header.site.open .burger{background:#eef3f4;color:var(--marine)}
  .actions .tel,.actions>.btn{display:none}
  footer.pied .grille3{grid-template-columns:1fr 1fr}
}
@media (max-width:720px){
  .hero3 .cta{flex-direction:column;align-items:flex-start;gap:1.2rem}
  .stats3{gap:1.6rem 2.4rem}
  .cite3 .lien{margin-left:0}
  footer.pied .grille3{grid-template-columns:1fr}
}
'''
i = t.index('</style>')
t = t[:i] + V3CSS + t[i:]
# JS : menu mobile
t = t.replace("var h=document.getElementById('entete');", "var h=document.getElementById('entete');var bg=h.querySelector('.burger');if(bg)bg.addEventListener('click',function(){var o=h.classList.toggle('open');bg.setAttribute('aria-expanded',o)});",1)
t = t.replace('  // compteurs\n', open('src/v31.js', encoding='utf-8').read(), 1)
t = t.replace('{threshold:.6});\n    cs.forEach', '{threshold:.35});\n    cs.forEach')
open('source-accueil-v3.template.html', 'w', encoding='utf-8').write(t)
print(len(t) // 1024, 'Ko')
