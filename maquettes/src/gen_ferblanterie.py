"""Génère le corps HTML de la sous-page Ventilation commerciale (maquettes/src/refrigeration.body.html)."""
ARROW='<svg class="ico fl" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK='<svg class="ico" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'
I={
'users':'<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
'cal':'<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
'clock':'<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
'tool':'<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
'wind':'<path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"/>',
'layers':'<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
'pen':'<path d="M12 20h9M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4z"/>',
'snow':'<path d="M12 2v20M4.9 6l14.2 12M19.1 6L4.9 18M2 12h20"/>',
'drop':'<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>',
'refresh':'<polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/>',
}
def ic(n,c='ico'): return f'<svg class="{c}" viewBox="0 0 24 24">{I[n]}</svg>'
TEL='450-753-9426'
def carte(n,i,t,p,ul,fonce=False):
    return f'<div class="metier{" metier-fonce" if fonce else ""} reveal d{n%3}"><span class="num">0{n+1}</span><span class="ico-g">{ic(i)}</span><h3>{t}</h3><p>{p}</p><ul>'+''.join(f'<li>{x}</li>' for x in ul)+'</ul></div>'
def carte(n,i,t,p,ul,fonce=False):
    return f'<div class="metier{" metier-fonce" if fonce else ""} reveal d{n%3}"><span class="num">0{n+1}</span><span class="ico-g">{ic(i)}</span><h3>{t}</h3><p>{p}</p><ul>'+''.join(f'<li>{x}</li>' for x in ul)+'</ul></div>'
cartes=''.join([
 carte(0,'layers','Conduits sur mesure','Des ferblantiers spécialisés en ventilation fabriquent les conduits et les pièces adaptés à votre bâtiment. <em>[fabrication en atelier à valider]</em>',['Sections droites et transitions','Raccords et accessoires','Selon les dessins d\'atelier']),
 carte(1,'tool','Installation sur chantier','Une équipe qualifiée installe vos conduits et vos pièces de ferblanterie, selon l\'échéancier convenu.',['Commercial et institutionnel','Industriel et résidentiel','Coordination avec les autres métiers'],True),
 carte(2,'refresh','Modification et remplacement','Ajout, réparation ou remplacement de conduits dans un réseau de ventilation existant.',['Modification de réseaux','Réparation de conduits','Remplacement de pièces']),
])
faq=[
 ("Qu'est-ce qu'un ferblantier en ventilation?","Le ferblantier en ventilation fabrique et installe les conduits et les pièces de tôle qui distribuent l'air dans un bâtiment. Il travaille à partir des dessins d'atelier et en coordination avec les autres métiers du chantier."),
 ("Fabriquez-vous les conduits sur mesure?","Oui, nos ferblantiers spécialisés en ventilation fabriquent et installent des conduits adaptés à votre bâtiment. [À valider : fabrication en atelier]"),
 ("Faites-vous seulement la ferblanterie, ou aussi la ventilation complète?","Les deux. Vous pouvez nous confier uniquement la ferblanterie, ou l'ensemble du projet : conception, ferblanterie, installation et entretien du système de ventilation."),
 ("Travaillez-vous avec des entrepreneurs et des concepteurs?","Oui. Nous collaborons avec les chargés de projet et préparons des dessins d'intégration et des dessins d'atelier pour coordonner le chantier."),
 ("Dans quels secteurs travaillez-vous?","Nos travaux se font en grande majorité dans Lanaudière et ses environs. Contactez-nous pour un projet situé ailleurs."),
 ("Comment obtenir une soumission?","Décrivez votre projet dans le formulaire ou appelez-nous. Un spécialiste vous rappelle sous 24 heures ouvrables et vous remet une soumission détaillée."),
 ("Recrutez-vous des ferblantiers?","Oui. Nous cherchons des ferblantiers et des apprentis ferblantiers (2e année et plus) dans la région de Lanaudière : salaire CCQ commercial, véhicule de service et travail à l'année."),
]
faqh=''.join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(faq))
import json, re
open('src/ferblanterie.faq.json','w',encoding='utf-8').write(json.dumps([{"q":q,"a":re.sub(r"\s*\[[^\]]*\]","",a)} for q,a in faq],ensure_ascii=False))

body=f'''<main>
<!-- ================= HERO ================= -->
<div class="hero hero-service hero-comm hero-fer">
  <div class="bg"></div>
  <div class="wrap">
    <div>
      <nav class="fil" aria-label="Fil d'Ariane"><a href="#">Accueil</a><span>›</span><a href="#">Commercial</a><span>›</span><b>Ferblanterie</b></nav>
      <div class="pastille reveal"><b>{CHECK}</b>Ferblantiers · Joliette et Lanaudière</div>
      <h1 class="reveal d1">Ferblantier en ventilation à <em>Joliette</em></h1>
      <p class="lead reveal d2"><b>Des experts qualifiés et diplômés en ventilation.</b> Conduits et pièces de ferblanterie sur mesure, installation sur chantier et modification de réseaux pour vos projets commerciaux, industriels, institutionnels et résidentiels.</p>
      <div class="cta reveal d3">
        <a class="btn btn-b" href="#soumission">Demander une soumission {ARROW}</a>
        <a class="btn btn-l" href="tel:+14507539426" data-track="call_tracking">{ic('clock')}<span>Parler à un spécialiste : {TEL}</span></a>
      </div>
    </div>
    <form class="devis-carte reveal d2" id="soumission" action="#" onsubmit="return false" data-form="commercial-ferblanterie">
      <h2>Soumission en ferblanterie</h2>
      <p class="sous">Décrivez votre projet : un spécialiste vous rappelle sous 24 heures ouvrables.</p>
      <div class="champ"><label for="f-nom">Nom et entreprise</label><input id="f-nom" autocomplete="organization" placeholder="Votre nom, votre entreprise"></div>
      <div class="champ"><label for="f-tel">Téléphone</label><input id="f-tel" type="tel" autocomplete="tel" placeholder="450 000-0000"></div>
      <div class="champ"><label for="f-type">Type de projet</label>
        <select id="f-type"><option>Conduits sur mesure</option><option>Installation sur chantier</option><option>Modification d'un réseau existant</option><option>Projet complet de ventilation</option><option>Autre</option></select></div>
      <button class="btn btn-r" type="submit">Être rappelé {ARROW}</button>
      <p class="note">Une question? <a href="tel:+14507539426" data-track="call_tracking">Appelez le {TEL}</a></p>
    </form>
  </div>
</div>

<!-- ================= POINTS FORTS ================= -->
<div class="faits"><div class="wrap">
  <div class="boite reveal">
    <div class="fait">{ic('layers')}<b>Sur mesure</b><span>Conduits adaptés à votre bâtiment</span></div>
    <div class="fait">{ic('users')}<b>Qualifiés et diplômés</b><span>Experts en ventilation</span></div>
    <div class="fait">{ic('wind')}<b>Un seul interlocuteur</b><span>Conception, ferblanterie, installation</span></div>
    <div class="fait">{ic('cal')}<b>40+ ans</b><span>D'expérience dans Lanaudière</span></div>
  </div>
</div></div>

<!-- ================= SERVICES ================= -->
<section><div class="wrap">
  <div class="tete">
    <div><span class="eyebrow">Nos services</span><h2 class="reveal">De la tôle au système en marche</h2></div>
    <p class="reveal d1">Nous réalisons des projets dans le domaine résidentiel, commercial, industriel et institutionnel.</p>
  </div>
  <div class="metiers">{cartes}</div>
</div></section>

<!-- ================= PIÈCES ================= -->
<section class="fond-beige"><div class="wrap duo-fer">
  <div class="illu-fer reveal"></div>
  <div>
    <span class="eyebrow">Pièces et conduits</span>
    <h2 class="reveal">Des pièces adaptées à chaque réseau</h2>
    <p class="reveal d1" style="color:var(--doux);font-size:1.12rem;margin:1.2rem 0 1.6rem;max-width:34em">Chaque bâtiment a son parcours d'air. Nos ferblantiers préparent les sections droites, les transitions et les raccords nécessaires pour que le réseau s'installe proprement. <em>[liste des pièces à valider]</em></p>
    <ul class="liste-check reveal d2">
      <li>Sections droites de conduits</li>
      <li>Transitions et changements de dimension</li>
      <li>Raccords et brides d'assemblage</li>
      <li>Pièces spéciales selon les dessins d'atelier</li>
    </ul>
  </div>
</div></section>

<!-- ================= RÉALISATION ================= -->
<section><div class="wrap duo-fer duo-fer-inv">
  <div>
    <span class="eyebrow">Réalisation</span>
    <h2 class="reveal">Des conduits installés avec précision</h2>
    <p class="reveal d1" style="color:var(--doux);font-size:1.12rem;margin:1.2rem 0 1.6rem;max-width:34em">Conduits galvanisés installés dans un bâtiment : le résultat du travail de nos ferblantiers, de la fabrication à la pose. <em>[À compléter : nom ou type du projet, ville, travaux réalisés]</em></p>
    <a class="btn btn-m reveal d2" href="#soumission">Discuter de votre projet {ARROW}</a>
  </div>
  <div class="photo-fer reveal"></div>
</div></section>

<!-- ================= DÉROULEMENT ================= -->
<section class="fond-beige"><div class="wrap">
  <div class="tete"><div><span class="eyebrow">Déroulement</span><h2 class="reveal">Comment se déroule votre projet</h2></div></div>
  <div class="etapes etapes-4">
    <div class="etape reveal"><div class="n">01</div><h3>Plans et relevés</h3><p>Nous analysons les plans et prenons les relevés nécessaires sur le chantier.</p></div>
    <div class="etape reveal d1"><div class="n">02</div><h3>Dessins d'atelier</h3><p>Nous préparons les dessins d'atelier, en collaboration avec les chargés de projet.</p></div>
    <div class="etape reveal d2"><div class="n">03</div><h3>Fabrication</h3><p>Les conduits et les pièces sont préparés selon les dessins. <em>[atelier à valider]</em></p></div>
    <div class="etape reveal d3"><div class="n">04</div><h3>Installation</h3><p>Une équipe qualifiée installe le tout, selon l'échéancier convenu.</p></div>
  </div>
</div></section>

<!-- ================= RECRUTEMENT ================= -->
<section class="sombre"><div class="wrap bande-urgence">
  <div>
    <span class="eyebrow" style="color:var(--cyan)">Carrières</span>
    <h2 class="reveal">Vous êtes ferblantier(ère)? Rejoignez l'équipe.</h2>
    <p class="reveal d1">Nous cherchons des ferblantiers et des apprentis (2<sup>e</sup> année et plus) dans la région de Lanaudière, pour soutenir notre croissance.</p>
    <a class="btn btn-b reveal d2" href="#">Voir le poste de ferblantier {ARROW}</a>
  </div>
  <ul class="liste-sombre">
    <li class="reveal"><b>Salaire CCQ commercial</b><br>En tout temps.</li>
    <li class="reveal d1"><b>Véhicule de service</b><br>Fourni, selon le poste.</li>
    <li class="reveal d2"><b>Travail à l'année, chantiers locaux</b><br>Fini les heures perdues dans le trafic.</li>
  </ul>
</div></section>

<!-- ================= FAQ ================= -->
<section class="fond-ciel" id="faq"><div class="wrap faq-zone">
  <div>
    <span class="eyebrow">Questions fréquentes</span>
    <h2 class="reveal">Ferblanterie : vos questions</h2>
    <p class="reveal d1" style="margin-top:18px;color:var(--doux);max-width:24em">Une autre question? Appelez-nous au <a href="tel:+14507539426" data-track="call_tracking" style="color:var(--bleu);font-weight:700;text-decoration:none">{TEL}</a>.</p>
  </div>
  <div>{faqh}</div>
</div></section>

<!-- ================= LIENS LIÉS ================= -->
<section class="fond-beige"><div class="wrap">
  <div class="tete"><div><span class="eyebrow">À consulter aussi</span><h2 class="reveal">Nos autres services commerciaux</h2></div></div>
  <div class="lies">
    <a class="lie reveal" href="#"><b>Services commerciaux</b><span>Tous nos services pour les bâtiments commerciaux.</span><i>{ic('layers')}</i></a>
    <a class="lie reveal d1" href="#"><b>Ventilation commerciale</b><span>Conception, ferblanterie et installation.</span><i>{ic('wind')}</i></a>
    <a class="lie reveal d2" href="#"><b>Réfrigération commerciale</b><span>Frigoristes, entretien et urgence 24 h.</span><i>{ic('snow')}</i></a>
    <a class="lie reveal d3" href="#"><b>Carrières</b><span>Rejoignez une équipe de plus de 65 professionnels.</span><i>{ic('users')}</i></a>
  </div>
</div></section>

<!-- ================= APPEL FINAL ================= -->
<div class="final"><div class="wrap">
  <h2 class="reveal">Un projet de ferblanterie?</h2>
  <p class="reveal d1">Parlez à un spécialiste Bédard : plans, dessins d'atelier, fabrication et installation.</p>
  <div class="cta reveal d2"><a class="btn btn-b" href="#soumission">Demander une soumission {ARROW}</a></div>
  <a class="grosphone reveal d3" href="tel:+14507539426" data-track="call_tracking">{TEL}</a>
</div></div>
</main>
'''
open('src/ferblanterie.body.html','w',encoding='utf-8').write(body)
print(len(body))
