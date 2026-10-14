"""Fabrique source-accueil-v21.template.html : l'ancien design (v2) intact + bandeau de menu agrandi,
« Blogue » à la place de « Guides de prix », « chauffage d'appoint » et menu mobile fonctionnel."""
t = open('source-accueil-v2.template.html', encoding='utf-8').read()
def rep(a, b, count=1):
    global t
    assert a in t, a[:70]
    t = t.replace(a, b, count)

# --- vocabulaire
rep('<a href="#guides">Guides</a>', '<a href="#guides">Blogue</a>')
rep('<span class="eyebrow">Guides de prix</span><h2 class="reveal">Combien ça coûte? Les réponses, avant même de nous appeler</h2>',
    '<span class="eyebrow">Blogue</span><h2 class="reveal">Des conseils clairs pour décider, avant même de nous appeler</h2>')
rep('<p class="reveal d1">Des guides clairs et à jour, rédigés par notre équipe.</p>', '<p class="reveal d1">Des articles et des guides à jour, rédigés par notre équipe.</p>')
rep('<li><a href="#">Guides de prix</a></li>', '<li><a href="#">Blogue</a></li>')
rep('chauffage auxiliaire', "chauffage d'appoint")

# --- menu mobile fonctionnel (le burger de v2 ne faisait rien)
MOB = ('<div class="m-mobile" id="menu-mobile">'
  '<a class="m-simple" href="#univers">Résidentiel</a><a class="m-simple" href="#univers">Commercial</a><a class="m-simple" href="#services">Services</a>'
  '<a class="m-simple" href="#guides">Blogue</a><a class="m-simple" href="#avis">Avis</a><a class="m-simple" href="#carrieres">Carrières</a><a class="m-simple" href="#">Contact</a>'
  '<a class="btn btn-r" href="#soumission">Demander une soumission</a></div>')
rep('</header>', MOB + '\n</header>')
rep('<span class="burger" aria-label="Menu"><svg class="ico" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></svg></span>',
    '<button class="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="menu-mobile"><svg class="ico ouvre" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></svg><svg class="ico ferme" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></button>')
rep("var h=document.getElementById('entete');", "var h=document.getElementById('entete');var bg=h.querySelector('.burger');if(bg)bg.addEventListener('click',function(){var o=h.classList.toggle('open');bg.setAttribute('aria-expanded',o)});")

CSS = r'''
/* ===== v2.1 : bandeau de menu agrandi ===== */
.urgence{font-size:.9rem}
header.site .barre,header.site.solid .barre{height:6.5rem;gap:1.2rem;width:calc(100% - 2*clamp(1rem,2.2vw,3.2rem))}
.barre .logo{height:3.8rem;width:15.4rem}
.barre .logo img{height:3.8rem}
nav.principal{gap:0;font-size:1.1rem;font-weight:600}
nav.principal a{padding:.8rem .85rem}
.tel{font-size:1.08rem}
.actions{gap:1rem}
.actions .btn{padding:.95rem 1.45rem;font-size:1rem}
.hero{padding-top:clamp(11rem,18vh,13.5rem)}
footer.pied .logo{height:4.4rem}
.burger{border:0;cursor:pointer}
.burger .ferme{display:none}
header.site.open .burger .ouvre{display:none}header.site.open .burger .ferme{display:block}
.m-mobile{display:none}

/* aspect identique en haut de page et au défilement : même bleu, mêmes couleurs, même taille. Seul le fond devient opaque. */
header.site,header.site.solid{background:rgba(0,32,50,calc(.97*var(--p,0)));box-shadow:0 .4rem 1.9rem rgba(0,10,25,calc(.38*var(--p,0)));backdrop-filter:blur(calc(10px*var(--p,0)));transform:translateY(calc(-1px*var(--s,0)));transition:none;will-change:transform}
header.site.solid .urgence{max-height:2.9rem;opacity:1}
header.site.solid .logo .on-light{opacity:0}header.site.solid .logo .on-dark{opacity:1}
header.site.solid nav.principal a{color:#fff}header.site.solid nav.principal a:hover{background:rgba(255,255,255,.14)}
header.site.solid .tel{color:#fff}header.site.solid .tel .ico{color:var(--cyan)}
header.site.solid .burger{background:rgba(255,255,255,.14);color:#fff}
@media (max-width:1400px){.barre .logo{height:3.5rem;width:14.2rem}.barre .logo img{height:3.5rem}nav.principal{font-size:1.04rem}nav.principal a{padding:.7rem .62rem}.tel{font-size:1.02rem}.actions{gap:.8rem}.actions .btn{padding:.85rem 1.2rem;font-size:.95rem}header.site .barre{gap:.8rem}}
@media (max-width:1240px){nav.principal{font-size:1rem}nav.principal a{padding:.65rem .5rem}.barre .logo{height:3.2rem;width:13rem}.barre .logo img{height:3.2rem}.tel span{display:none}.actions .btn{padding:.8rem 1.05rem;font-size:.92rem}}
@media (max-width:1100px){
  header.site .barre,header.site.solid .barre{height:5.2rem}
  .barre .logo{height:3.3rem;width:13.4rem}.barre .logo img{height:3.3rem}
  header.site .m-mobile{display:none;position:absolute;left:0;right:0;top:100%;background:#fff;box-shadow:0 1.6rem 2.6rem rgba(0,30,50,.18);padding:1rem var(--gut) 1.6rem;max-height:calc(100vh - 5.4rem);overflow:auto}
  header.site.open .m-mobile{display:block}
  .m-mobile .m-simple{display:block;padding:1rem 0;border-bottom:1px solid #e1e8ea;font-weight:700;color:var(--marine);text-decoration:none;font-size:1.1rem}
  .m-mobile .btn{margin-top:1.2rem;width:100%}
  header.site.open{background:#fff}
  header.site.open .logo .on-light{opacity:1}header.site.open .logo .on-dark{opacity:0}
  header.site.open .burger{background:#eef3f4;color:var(--marine)}
  .actions .tel,.actions>.btn{display:none}
}
'''
i = t.index('</style>')
t = t[:i] + CSS + t[i:]
# le numéro de téléphone reste visible (icône + numéro); classe pour le masquer à l'étroit
rep('<a class="tel" href="tel:+14507539426">', '<a class="tel" href="tel:+14507539426">')

# --- Carrières : le poste de dessinateur est comblé, celui de magasinier est ouvert
rep('Frigoristes, ferblantiers, dessinateurs : des métiers qualifiés', 'Frigoristes, ferblantiers, magasiniers : des métiers qualifiés')
rep('<span>Dessinateur(trice) en ventilation<small>Lanaudière</small></span>', '<span>Magasinier(ère)<small>Joliette</small></span>')

# --- Secteurs desservis et bureau : deux blocs distincts, bien étiquetés
_a = t.index('<div id="contact">'); _b = t.index('  <div>\n    <span class="eyebrow">Questions fréquentes</span>')
_mrc = ['Joliette','Notre-Dame-des-Prairies','Saint-Charles-Borromée','Crabtree','Saint-Paul','Saint-Thomas','Notre-Dame-de-Lourdes','Saint-Ambroise-de-Kildare','Sainte-Mélanie','Saint-Pierre']
_chips = ''.join('<span>%s</span>' % m for m in _mrc)
_new = ('<div id="contact">\n'
 '    <span class="eyebrow">Secteurs desservis</span>\n'
 '    <h2 class="reveal">Nous desservons Joliette et Lanaudière</h2>\n'
 '    <p class="sect-plus reveal">Toute la MRC de Joliette et plusieurs secteurs voisins de Lanaudière. <a class="lien" href="#">Voir la liste complète des secteurs desservis</a></p>\n'
 '    <span class="eyebrow eyebrow-bureau">Où nous trouver</span>\n'
 '    <div class="carte-adresse reveal">\n'
 '      <h3>Notre bureau à Joliette</h3>\n'
 '      <dl>\n'
 '        <dt>Adresse</dt><dd>304, boulevard de l\'Industrie<br>Joliette (Québec) J6E 8V2</dd>\n'
 '        <dt>Téléphone</dt><dd><a href="tel:+14507539426">450-753-9426</a></dd>\n'
 '        <dt>Sans frais</dt><dd><a href="tel:+18009530153">1-800-953-0153</a></dd>\n'
 '        <dt>Heures</dt><dd>Lundi au vendredi, 8 h à 17 h<br>(fermé de 12 h à 13 h)</dd>\n'
 '        <dt>Fin de semaine</dt><dd>Sur rendez-vous avec un représentant</dd>\n'
 '        <dt>Urgence</dt><dd>24 h sur 24, 7 jours sur 7<br><a href="tel:+14507539426">450-753-9426</a></dd>\n'
 '      </dl>\n'
 '      <a class="lien" href="https://www.google.com/maps/dir/?api=1&destination=304+boulevard+de+l%27Industrie+Joliette+QC" target="_blank" rel="noopener">Obtenir l\'itinéraire <svg class="ico fl" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>\n'
 '    </div>\n'
 '  </div>\n')
t = t[:_a] + _new + t[_b:]
CSS_ZONE = """
/* secteurs desservis / bureau */
.sect-plus{color:var(--doux);margin:1.2rem 0 0;max-width:34em;font-size:1rem}
.eyebrow-bureau{margin-top:2.8rem}
.carte-adresse .lien{display:inline-flex;margin-top:1.4rem;color:var(--bleu);font-weight:700}
"""
_i = t.index('</style>'); t = t[:_i] + CSS_ZONE + t[_i:]

# --- bandeau du haut : l'urgence 24 h et les heures du bureau ne doivent pas se confondre
rep('<span class="pt"><i></i>Service d\'urgence 24 h<span class="hrs"> · Lundi au vendredi, 8 h à 17 h</span></span>', '<span class="pt"><i></i>Service d\'urgence 24 h sur 24, 7 jours sur 7</span>')
_a = t.index('<span class="adr">'); _b = t.index('</span>', _a) + 7
t = t[:_a] + '<span class="adr"><svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>Bureau ouvert du lundi au vendredi, 8 h à 17 h</span>' + t[_b:]

# --- défilement continu
rep("function onScroll(){h.classList.toggle('solid',window.scrollY>40)}",
    "var urg=h.querySelector('.urgence');function onScroll(){var y=window.scrollY,uh=urg?urg.offsetHeight:0;h.classList.toggle('solid',y>40);h.style.setProperty('--p',Math.max(0,Math.min(1,y/90)).toFixed(3));h.style.setProperty('--s',Math.max(0,Math.min(y,uh)))}")
open('source-accueil-v21.template.html', 'w', encoding='utf-8').write(t)
print(len(t) // 1024, 'Ko')
