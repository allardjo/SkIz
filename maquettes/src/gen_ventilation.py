"""Génère le corps HTML de la sous-page Ventilation commerciale (maquettes/src/ventilation.body.html)."""
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
'drop':'<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>',
'refresh':'<polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/>',
}
def ic(n,c='ico'): return f'<svg class="{c}" viewBox="0 0 24 24">{I[n]}</svg>'
TEL='450-753-9426'
def carte(n,i,t,p,ul,fonce=False):
    return f'<div class="metier{" metier-fonce" if fonce else ""} reveal d{n%3}"><span class="num">0{n+1}</span><span class="ico-g">{ic(i)}</span><h3>{t}</h3><p>{p}</p><ul>'+''.join(f'<li>{x}</li>' for x in ul)+'</ul></div>'
cartes=''.join([
 carte(0,'pen','Conception et dessins','Dessins d\'intégration et analyse des dessins d\'atelier, en collaboration avec les chargés de projet.',['Relevés sur le chantier','Dessins d\'intégration','Documents de chantier']),
 carte(1,'layers','Ferblanterie sur mesure','Des ferblantiers spécialisés en ventilation fabriquent les conduits et les pièces adaptés à votre bâtiment.',['Fabrication sur mesure','Installation sur chantier','Conduits et accessoires'],True),
 carte(2,'wind','Installation de systèmes','Design, conception et installation de systèmes de ventilation personnalisés pour votre bâtiment.',['Commercial, industriel, institutionnel','Mise en service','Respect de l\'échéancier']),
 carte(3,'refresh','Échangeurs d\'air','Choix, installation et entretien d\'échangeurs d\'air pour renouveler l\'air du bâtiment.',['Installation et remplacement','Entretien et filtres','Nettoyage des unités']),
 carte(4,'drop','Nettoyage des systèmes','Nettoyage des systèmes de ventilation, des unités, des échangeurs d\'air et des conduits.',['Systèmes de ventilation','Unités murales','Conduits'],True),
 carte(5,'tool','Entretien et dépannage','Un entretien périodique personnalisé et un service d\'urgence disponible 24 heures sur 24.',['Entretien périodique','Dépannage 24 h','Suivi de vos équipements']),
])
facteurs=[('La taille et l\'usage du bâtiment','Superficie, nombre de zones, occupation et type d\'activité.'),('Le niveau de conception','Un système neuf à concevoir, ou un réseau existant à modifier.'),('Les équipements choisis','Unités, échangeurs, conduits et accessoires adaptés à vos besoins.'),('L\'accès au chantier','Hauteurs, espaces restreints, travaux en bâtiment occupé.'),('L\'échéancier','Phases de travaux et coordination avec les autres corps de métier.')]
fl=''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a,b in facteurs)
faq=[
 ("Qu'est-ce que la ventilation commerciale?","La ventilation commerciale regroupe les systèmes qui renouvellent l'air d'un bâtiment, évacuent l'humidité, les odeurs et les polluants, et distribuent l'air là où il faut. Elle s'adapte à l'usage du bâtiment : commerce, industrie ou institution."),
 ("Faites-vous la conception et l'installation?","Oui. Nos professionnels réalisent le design, la conception et l'installation de systèmes de ventilation personnalisés, y compris les dessins d'intégration et les dessins d'atelier."),
 ("Fabriquez-vous les conduits sur mesure?","Oui. Nos ferblantiers, spécialisés en ventilation, fabriquent et installent les conduits et les pièces adaptés à votre bâtiment."),
 ("Offrez-vous le nettoyage et l'entretien des systèmes?","Oui. Nous nettoyons les systèmes de ventilation, les unités, les échangeurs d'air et les conduits, et nous offrons un entretien périodique personnalisé."),
 ("Combien coûte un projet de ventilation commerciale?","Chaque bâtiment est différent : le prix dépend de la taille, de l'usage, des équipements et de l'accès au chantier. Nous évaluons votre projet, puis nous vous remettons une soumission détaillée."),
 ("Quels secteurs desservez-vous?","Nos travaux se font en grande majorité dans Lanaudière et ses environs. Contactez-nous pour un projet situé ailleurs."),
 ("Avez-vous un service d'urgence?",f"Oui, un service d'urgence est offert 24 heures sur 24. Appelez le {TEL}."),
]
faqh=''.join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(faq))
import json
open('src/ventilation.faq.json','w',encoding='utf-8').write(json.dumps([{"q":q,"a":a} for q,a in faq],ensure_ascii=False))

body=f'''<main>
<!-- ================= HERO ================= -->
<div class="hero hero-service hero-comm hero-vent">
  <div class="bg"></div>
  <div class="wrap">
    <div>
      <nav class="fil" aria-label="Fil d'Ariane"><a href="#">Accueil</a><span>›</span><a href="#">Commercial</a><span>›</span><b>Ventilation commerciale</b></nav>
      <div class="pastille reveal"><b>{CHECK}</b>Joliette et Lanaudière</div>
      <h1 class="reveal d1">Ventilation commerciale à <em>Joliette</em></h1>
      <p class="lead reveal d2"><b>De la conception à l'entretien, une seule équipe.</b> Conception, ferblanterie sur mesure, installation et nettoyage de systèmes de ventilation pour les commerces, les industries et les institutions de Lanaudière.</p>
      <div class="cta reveal d3">
        <a class="btn btn-b" href="#soumission">Demander une soumission {ARROW}</a>
        <a class="btn btn-l" href="tel:+14507539426" data-track="call_tracking">{ic('clock')}<span>Urgence 24 h : {TEL}</span></a>
      </div>
    </div>
    <form class="devis-carte reveal d2" id="soumission" action="#" onsubmit="return false" data-form="commercial-ventilation">
      <h2>Soumission en ventilation</h2>
      <p class="sous">Décrivez votre projet : un spécialiste vous rappelle sous 24 heures ouvrables.</p>
      <div class="champ"><label for="v-nom">Nom et entreprise</label><input id="v-nom" autocomplete="organization" placeholder="Votre nom, votre entreprise"></div>
      <div class="champ"><label for="v-tel">Téléphone</label><input id="v-tel" type="tel" autocomplete="tel" placeholder="450 000-0000"></div>
      <div class="champ"><label for="v-type">Type de projet</label>
        <select id="v-type"><option>Nouvelle installation</option><option>Remplacement ou modification</option><option>Conception et dessins</option><option>Ferblanterie sur mesure</option><option>Nettoyage ou entretien</option><option>Dépannage / urgence</option></select></div>
      <button class="btn btn-r" type="submit">Être rappelé {ARROW}</button>
      <p class="note">Urgence? <a href="tel:+14507539426" data-track="call_tracking">Appelez le {TEL}</a></p>
    </form>
  </div>
</div>

<!-- ================= POINTS FORTS ================= -->
<div class="faits"><div class="wrap">
  <div class="boite reveal">
    <div class="fait">{ic('pen')}<b>Conception interne</b><span>Dessins d'intégration et d'atelier</span></div>
    <div class="fait">{ic('layers')}<b>Ferblanterie sur mesure</b><span>Conduits fabriqués pour votre bâtiment</span></div>
    <div class="fait">{ic('users')}<b>65+ professionnels</b><span>Une équipe de plus de 40 ans d'expérience</span></div>
    <div class="fait">{ic('clock')}<b>Urgence 24 h</b><span>Entretien périodique personnalisé</span></div>
  </div>
</div></div>

<!-- ================= SERVICES ================= -->
<section><div class="wrap">
  <div class="tete">
    <div><span class="eyebrow">Nos services</span><h2 class="reveal">Tout pour la ventilation de votre bâtiment</h2></div>
    <p class="reveal d1">Nos experts, qualifiés et diplômés en ventilation, réalisent des projets commerciaux, industriels et institutionnels.</p>
  </div>
  <div class="metiers metiers-6">{cartes}</div>
</div></section>

<!-- ================= PUBLICS ================= -->
<section class="fond-beige"><div class="wrap">
  <div class="tete">
    <div><span class="eyebrow">Types de bâtiments</span><h2 class="reveal">Un système adapté à votre usage</h2></div>
    <p class="reveal d1">Chaque bâtiment a ses propres besoins en air, en débit et en confort.</p>
  </div>
  <div class="publics">
    <div class="public reveal"><b>Commerces</b><span>Boutiques, bureaux et espaces de service à la clientèle. <em>[exemples à valider]</em></span></div>
    <div class="public reveal d1"><b>Industries</b><span>Ateliers et bâtiments industriels : renouvellement d'air et évacuation. <em>[exemples à valider]</em></span></div>
    <div class="public reveal d2"><b>Institutions</b><span>Bâtiments institutionnels : systèmes adaptés à leurs exigences. <em>[exemples à valider]</em></span></div>
  </div>
</div></section>

<!-- ================= DÉROULEMENT ================= -->
<section><div class="wrap">
  <div class="tete"><div><span class="eyebrow">Déroulement</span><h2 class="reveal">Comment se déroule votre projet</h2></div></div>
  <div class="etapes etapes-4">
    <div class="etape reveal"><div class="n">01</div><h3>Visite et relevés</h3><p>Nous visitons le bâtiment et prenons les relevés nécessaires sur le chantier.</p></div>
    <div class="etape reveal d1"><div class="n">02</div><h3>Conception et dessins</h3><p>Dessins d'intégration et dessins d'atelier, en collaboration avec les chargés de projet.</p></div>
    <div class="etape reveal d2"><div class="n">03</div><h3>Fabrication et installation</h3><p>Nos ferblantiers fabriquent les conduits sur mesure et l'équipe installe le système.</p></div>
    <div class="etape reveal d3"><div class="n">04</div><h3>Mise en service et entretien</h3><p>Nous vérifions le fonctionnement, puis proposons un entretien périodique personnalisé.</p></div>
  </div>
</div></section>

<!-- ================= PRIX ================= -->
<section class="fond-ciel"><div class="wrap prix">
  <div>
    <span class="eyebrow">Prix</span>
    <h2 class="reveal">Combien coûte un projet de ventilation commerciale?</h2>
    <p class="intro reveal d1">Chaque bâtiment est différent, donc chaque projet est sur mesure. Voici ce qui fait varier le prix.</p>
    <ul class="facteurs reveal d2">{fl}</ul>
  </div>
  <aside class="carte-sombre reveal d1">
    <h3>Une soumission détaillée</h3>
    <p>Nous évaluons votre bâtiment avant de vous donner un prix. Vous savez exactement ce qui est inclus.</p>
    <a class="btn btn-b" href="#soumission">Demander une soumission {ARROW}</a>
    <a class="lien lien-clair" href="tel:+14507539426" data-track="call_tracking">Ou appelez le {TEL} {ARROW}</a>
  </aside>
</div></section>

<!-- ================= POURQUOI BÉDARD ================= -->
<section class="sombre"><div class="wrap bande-urgence">
  <div>
    <span class="eyebrow" style="color:var(--cyan)">Pourquoi Bédard</span>
    <h2 class="reveal">Une expertise en ventilation de longue date</h2>
    <p class="reveal d1">Depuis plus de 40 ans à Joliette, et avec Ventilation Fabro (acquise en 2012) et Solution Ventech (2010), Bédard a bâti une équipe spécialisée en ventilation commerciale et institutionnelle, en nettoyage de systèmes et en ferblanterie.</p>
    <a class="btn btn-b reveal d2" href="#soumission">Parler à un spécialiste {ARROW}</a>
  </div>
  <ul class="liste-sombre">
    <li class="reveal"><b>Un seul interlocuteur</b><br>Conception, fabrication, installation et entretien.</li>
    <li class="reveal d1"><b>Ferblantiers spécialisés</b><br>Des conduits adaptés à votre bâtiment.</li>
    <li class="reveal d2"><b>Une équipe de plus de 65 professionnels</b><br>Disponible aussi en urgence, 24 h sur 24.</li>
  </ul>
</div></section>

<!-- ================= RÉALISATIONS ================= -->
<section><div class="wrap">
  <div class="programmes reveal">
    <span class="eyebrow">Réalisations</span>
    <h2>Projets de ventilation récents</h2>
    <p>Projets commerciaux, industriels et institutionnels livrés par Bédard, avec photos, type de bâtiment, ville et travaux réalisés. <em>[À fournir : 3 à 6 projets avec l'autorisation des clients]</em></p>
  </div>
</div></section>

<!-- ================= FAQ ================= -->
<section class="fond-ciel" id="faq"><div class="wrap faq-zone">
  <div>
    <span class="eyebrow">Questions fréquentes</span>
    <h2 class="reveal">Ventilation commerciale : vos questions</h2>
    <p class="reveal d1" style="margin-top:18px;color:var(--doux);max-width:24em">Une autre question? Appelez-nous au <a href="tel:+14507539426" data-track="call_tracking" style="color:var(--bleu);font-weight:700;text-decoration:none">{TEL}</a>.</p>
  </div>
  <div>{faqh}</div>
</div></section>

<!-- ================= LIENS LIÉS ================= -->
<section class="fond-beige"><div class="wrap">
  <div class="tete"><div><span class="eyebrow">À consulter aussi</span><h2 class="reveal">Nos autres services commerciaux</h2></div></div>
  <div class="lies">
    <a class="lie reveal" href="#"><b>Services commerciaux</b><span>Tous nos services pour les bâtiments commerciaux.</span><i>{ic('layers')}</i></a>
    <a class="lie reveal d1" href="#"><b>Réfrigération commerciale</b><span>Installation, service et entretien de vos systèmes.</span><i>{ic('wind')}</i></a>
    <a class="lie reveal d2" href="#"><b>Ferblanterie</b><span>Conduits et pièces sur mesure.</span><i>{ic('tool')}</i></a>
    <a class="lie reveal d3" href="#"><b>Échangeurs d'air</b><span>Pour les maisons : choix, installation et entretien.</span><i>{ic('refresh')}</i></a>
  </div>
</div></section>

<!-- ================= APPEL FINAL ================= -->
<div class="final"><div class="wrap">
  <h2 class="reveal">Un projet de ventilation?</h2>
  <p class="reveal d1">Parlez à un spécialiste Bédard : relevés, conception, ferblanterie sur mesure et installation.</p>
  <div class="cta reveal d2"><a class="btn btn-b" href="#soumission">Demander une soumission {ARROW}</a></div>
  <a class="grosphone reveal d3" href="tel:+14507539426" data-track="call_tracking">{TEL}</a>
</div></div>
</main>
'''
open('src/ventilation.body.html','w',encoding='utf-8').write(body)
print(len(body))
