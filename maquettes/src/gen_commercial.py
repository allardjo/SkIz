"""Génère le corps HTML du hub Commercial (maquettes/src/commercial.body.html)."""
ARROW='<svg class="ico fl" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK='<svg class="ico" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'
I={
'users':'<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
'cal':'<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
'clock':'<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
'tool':'<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
'snow':'<path d="M12 2v20M4.9 6l14.2 12M19.1 6L4.9 18M2 12h20"/>',
'wind':'<path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"/>',
'layers':'<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
}
def ic(n,c='ico'): return f'<svg class="{c}" viewBox="0 0 24 24">{I[n]}</svg>'
TEL='450-753-9426'
body=f'''<main>
<!-- ================= HERO COMMERCIAL ================= -->
<div class="hero hero-service hero-comm">
  <div class="bg"></div>
  <div class="wrap">
    <div>
      <nav class="fil" aria-label="Fil d'Ariane"><a href="#">Accueil</a><span>›</span><b>Commercial</b></nav>
      <div class="pastille reveal"><b>{CHECK}</b>Commercial · Industriel · Institutionnel</div>
      <h1 class="reveal d1">Ventilation, réfrigération et ferblanterie pour <em>votre bâtiment</em></h1>
      <p class="lead reveal d2"><b>Une seule équipe, de la conception à l'entretien.</b> Plus de 40 ans d'expertise dans Lanaudière, une équipe de plus de 65 professionnels et un service d'urgence 24 h pour les commerces, les industries et les institutions.</p>
      <div class="cta reveal d3">
        <a class="btn btn-b" href="#soumission">Demander une soumission {ARROW}</a>
        <a class="btn btn-l" href="tel:+14507539426" data-track="call_tracking">{ic('clock')}<span>Urgence 24 h : {TEL}</span></a>
      </div>
    </div>
    <form class="devis-carte reveal d2" id="soumission" action="#" onsubmit="return false" data-form="commercial">
      <h2>Soumission commerciale</h2>
      <p class="sous">Décrivez votre projet : un spécialiste vous rappelle sous 24 heures ouvrables.</p>
      <div class="champ"><label for="cm-nom">Nom et entreprise</label><input id="cm-nom" autocomplete="organization" placeholder="Votre nom, votre entreprise"></div>
      <div class="champ"><label for="cm-tel">Téléphone</label><input id="cm-tel" type="tel" autocomplete="tel" placeholder="450 000-0000"></div>
      <div class="champ"><label for="cm-type">Type de projet</label>
        <select id="cm-type"><option>Réfrigération commerciale</option><option>Ventilation</option><option>Ferblanterie sur mesure</option><option>Entretien périodique</option><option>Dépannage / urgence</option><option>Je ne sais pas encore</option></select></div>
      <button class="btn btn-r" type="submit">Être rappelé {ARROW}</button>
      <p class="note">Urgence? <a href="tel:+14507539426" data-track="call_tracking">Appelez le {TEL}</a></p>
    </form>
  </div>
</div>

<!-- ================= POINTS FORTS ================= -->
<div class="faits"><div class="wrap">
  <div class="boite reveal">
    <div class="fait">{ic('users')}<b>65+ professionnels</b><span>Conception, installation, service</span></div>
    <div class="fait">{ic('cal')}<b>40+ ans</b><span>D'expérience dans Lanaudière</span></div>
    <div class="fait">{ic('clock')}<b>Urgence 24 h</b><span>Une équipe disponible jour et nuit</span></div>
    <div class="fait">{ic('tool')}<b>Entretien périodique</b><span>Personnalisé, pour votre bâtiment</span></div>
  </div>
</div></div>

<!-- ================= LES TROIS MÉTIERS ================= -->
<section><div class="wrap">
  <div class="tete">
    <div><span class="eyebrow">Nos expertises</span><h2 class="reveal">Trois métiers, une seule équipe</h2></div>
    <p class="reveal d1">Ventilation, réfrigération et ferblanterie sous le même toit : un seul interlocuteur pour coordonner votre projet.</p>
  </div>
  <div class="metiers">
    <a class="metier reveal" href="#"><span class="num">01</span><span class="ico-g">{ic('snow')}</span>
      <h3>Réfrigération commerciale</h3>
      <p>Des techniciens spécialisés installent et entretiennent vos systèmes de réfrigération avec minutie, efficacité et professionnalisme.</p>
      <ul><li>Installation de systèmes</li><li>Service et dépannage</li><li>Climatisation et contrôle</li></ul>
      <span class="go">Découvrir la réfrigération {ARROW}</span></a>
    <a class="metier metier-fonce reveal d1" href="#"><span class="num">02</span><span class="ico-g">{ic('wind')}</span>
      <h3>Ventilation commerciale et institutionnelle</h3>
      <p>Design, conception et installation de systèmes de ventilation personnalisés, par des experts qualifiés. Ventilation Fabro, acquise en 2012, renforce notre expertise.</p>
      <ul><li>Conception et dessins d'atelier</li><li>Installation et mise en service</li><li>Nettoyage et entretien des systèmes</li></ul>
      <span class="go">Découvrir la ventilation {ARROW}</span></a>
    <a class="metier reveal d2" href="#"><span class="num">03</span><span class="ico-g">{ic('layers')}</span>
      <h3>Ferblanterie sur mesure</h3>
      <p>Des ferblantiers spécialisés en ventilation fabriquent et installent les conduits et les pièces adaptés à votre bâtiment.</p>
      <ul><li>Fabrication sur mesure</li><li>Installation sur chantier</li><li>Résidentiel, commercial, industriel et institutionnel</li></ul>
      <span class="go">Découvrir la ferblanterie {ARROW}</span></a>
  </div>
</div></section>

<!-- ================= POUR QUI ================= -->
<section class="fond-beige"><div class="wrap">
  <div class="tete">
    <div><span class="eyebrow">Pour qui</span><h2 class="reveal">Des projets de toutes tailles</h2></div>
    <p class="reveal d1">Nous travaillons surtout dans Lanaudière et ses environs, avec les propriétaires, les gestionnaires et les entrepreneurs.</p>
  </div>
  <div class="publics">
    <div class="public reveal"><b>Commerces et industries</b><span>Bâtiments commerciaux et industriels : réfrigération, ventilation, climatisation et entretien.</span></div>
    <div class="public reveal d1"><b>Institutions</b><span>Bâtiments institutionnels : systèmes de ventilation et de confort adaptés à leurs exigences.</span></div>
    <div class="public reveal d2"><b>Entrepreneurs et gestionnaires</b><span>Un partenaire pour la conception, la coordination avec les chargés de projet et l'installation. <em>[à valider]</em></span></div>
  </div>
</div></section>

<!-- ================= DÉROULEMENT ================= -->
<section><div class="wrap">
  <div class="tete"><div><span class="eyebrow">Déroulement</span><h2 class="reveal">De la conception à l'entretien</h2></div></div>
  <div class="etapes etapes-4">
    <div class="etape reveal"><div class="n">01</div><h3>Relevés et conception</h3><p>Nous visitons le chantier, prenons les relevés et préparons les dessins d'intégration.</p></div>
    <div class="etape reveal d1"><div class="n">02</div><h3>Dessins et coordination</h3><p>Dessins d'atelier et documents de chantier, en collaboration avec les chargés de projet.</p></div>
    <div class="etape reveal d2"><div class="n">03</div><h3>Installation</h3><p>Une équipe qualifiée fabrique et installe, selon l'échéancier convenu.</p></div>
    <div class="etape reveal d3"><div class="n">04</div><h3>Mise en service et entretien</h3><p>Nous vérifions le fonctionnement, puis proposons un entretien périodique personnalisé.</p></div>
  </div>
</div></section>

<!-- ================= ENTRETIEN ET URGENCE ================= -->
<section class="sombre"><div class="wrap bande-urgence">
  <div>
    <span class="eyebrow" style="color:var(--cyan)">Entretien et urgence</span>
    <h2 class="reveal">Votre bâtiment ne s'arrête pas. Nous non plus.</h2>
    <p class="reveal d1">Un entretien périodique personnalisé prolonge la durée de vie de vos équipements. En cas de panne, une équipe est disponible 24 heures sur 24.</p>
    <a class="btn btn-b reveal d2" href="tel:+14507539426" data-track="call_tracking">Urgence 24 h : {TEL}</a>
  </div>
  <ul class="liste-sombre">
    <li class="reveal"><b>Entretien périodique</b><br>Un programme adapté à votre bâtiment et à vos équipements.</li>
    <li class="reveal d1"><b>Dépannage 24 h</b><br>Ventilation, réfrigération, climatisation et chauffage.</li>
    <li class="reveal d2"><b>Nettoyage des systèmes</b><br>Ventilation, unités, échangeurs d'air et conduits.</li>
  </ul>
</div></section>

<!-- ================= RÉALISATIONS ================= -->
<section><div class="wrap">
  <div class="programmes reveal">
    <span class="eyebrow">Réalisations</span>
    <h2>Quelques projets de référence</h2>
    <p>Section réservée aux projets commerciaux, industriels et institutionnels livrés par Bédard, avec photos, type de bâtiment, ville et travaux réalisés. <em>[À fournir : 3 à 6 projets, avec l'autorisation des clients; licences et certifications (RBQ, CCQ) à afficher ici]</em></p>
  </div>
</div></section>

<!-- ================= FAQ ================= -->
<section class="fond-ciel" id="faq"><div class="wrap faq-zone">
  <div>
    <span class="eyebrow">Questions fréquentes</span>
    <h2 class="reveal">Services commerciaux : vos questions</h2>
    <p class="reveal d1" style="margin-top:18px;color:var(--doux);max-width:24em">Une autre question? Appelez-nous au <a href="tel:+14507539426" data-track="call_tracking" style="color:var(--bleu);font-weight:700;text-decoration:none">{TEL}</a>.</p>
  </div>
  <div>
    <details open><summary>Pour quels types de bâtiments travaillez-vous?</summary><p>Nous réalisons des projets résidentiels, commerciaux, industriels et institutionnels. Le secteur commercial et institutionnel représente une grande part de nos travaux de ventilation.</p></details>
    <details><summary>Faites-vous la conception des systèmes de ventilation?</summary><p>Oui. Nos professionnels réalisent le design, la conception et l'installation de systèmes de ventilation personnalisés, y compris les dessins d'intégration et les dessins d'atelier.</p></details>
    <details><summary>Offrez-vous un entretien périodique?</summary><p>Oui, nous offrons un service d'entretien périodique personnalisé pour vos équipements de ventilation, de réfrigération et de climatisation.</p></details>
    <details><summary>Avez-vous un service d'urgence?</summary><p>Oui, un service d'urgence est offert 24 heures sur 24. Appelez le {TEL}.</p></details>
    <details><summary>Dans quels secteurs travaillez-vous?</summary><p>Nos travaux se font en grande majorité dans Lanaudière et ses environs. Contactez-nous pour un projet situé ailleurs.</p></details>
    <details><summary>Comment obtenir une soumission?</summary><p>Décrivez votre projet dans le formulaire ou appelez-nous. Un spécialiste vous rappelle sous 24 heures ouvrables, évalue vos besoins et vous remet une soumission détaillée.</p></details>
  </div>
</div></section>

<!-- ================= LIENS LIÉS ================= -->
<section class="fond-beige"><div class="wrap">
  <div class="tete"><div><span class="eyebrow">À consulter aussi</span><h2 class="reveal">Nos autres services</h2></div></div>
  <div class="lies">
    <a class="lie reveal" href="#"><b>Résidentiel</b><span>Thermopompes, climatisation, chauffage et qualité de l'air.</span><i>{ic('wind').replace('class="ico"','class="ico"')}</i></a>
    <a class="lie reveal d1" href="#"><b>Réparation et dépannage</b><span>Urgence 24 h pour tous vos systèmes.</span><i>{ic('tool')}</i></a>
    <a class="lie reveal d2" href="#"><b>Entretien et nettoyage</b><span>Un entretien périodique personnalisé.</span><i>{ic('cal')}</i></a>
    <a class="lie reveal d3" href="#"><b>Carrières</b><span>Rejoignez une équipe de plus de 65 professionnels.</span><i>{ic('users')}</i></a>
  </div>
</div></section>

<!-- ================= APPEL FINAL ================= -->
<div class="final"><div class="wrap">
  <h2 class="reveal">Un projet commercial?</h2>
  <p class="reveal d1">Parlez à un spécialiste Bédard : relevés, conception, installation et entretien.</p>
  <div class="cta reveal d2"><a class="btn btn-b" href="#soumission">Demander une soumission {ARROW}</a></div>
  <a class="grosphone reveal d3" href="tel:+14507539426" data-track="call_tracking">{TEL}</a>
</div></div>
</main>
'''
open('src/commercial.body.html','w',encoding='utf-8').write(body)
print(len(body))
