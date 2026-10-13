"""Corps de la page « Installation de thermopompe » en version sobre (hero + 5 blocs + appel final)."""
ARR = '<svg class="ico fl" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
TELSVG = '<svg class="ico" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
body = f'''<main>
<!-- ================= HERO ================= -->
<div class="hero hero-service">
  <div class="bg"></div>
  <div class="wrap">
    <div>
      <nav class="fil" aria-label="Fil d'Ariane"><a href="#">Accueil</a><span>›</span><a href="#">Services</a><span>›</span><b>Installation de thermopompe</b></nav>
      <h1 class="reveal">Installation de thermopompe à <em>Joliette</em></h1>
      <p class="lead reveal d1"><b>Une thermopompe bien choisie et bien installée, du premier appel à la mise en service.</b> Murale ou centrale, pour votre maison ou votre commerce.</p>
      <div class="cta reveal d2">
        <a class="btn btn-b" href="#soumission">Demander une soumission {ARR}</a>
        <a class="lien-tel" href="tel:+14507539426" data-track="call_tracking">{TELSVG}450-753-9426</a>
      </div>
    </div>
    <form class="devis-carte reveal d2" id="soumission" action="#" onsubmit="return false">
      <h2>Soumission pour votre thermopompe</h2>
      <p class="sous">Un spécialiste vous rappelle sous 24 heures ouvrables.</p>
      <div class="champ"><label for="nom">Nom</label><input id="nom" autocomplete="name" placeholder="Votre nom"></div>
      <div class="champ"><label for="tel">Téléphone</label><input id="tel" type="tel" autocomplete="tel" placeholder="450 000-0000"></div>
      <div class="champ"><label for="type">Type de projet</label>
        <select id="type"><option>Je ne sais pas encore (conseillez-moi)</option><option>Thermopompe murale</option><option>Thermopompe centrale</option><option>Remplacement d'un système existant</option><option>Projet commercial</option></select></div>
      <button class="btn btn-r" type="submit">Être rappelé {ARR}</button>
      <p class="note">Urgence? <a href="tel:+14507539426" data-track="call_tracking">Appelez le 450-753-9426</a></p>
    </form>
  </div>
</div>

<!-- ================= 1. MURALE OU CENTRALE ================= -->
<section class="sec3"><div class="wrap">
  <h2 class="titre3 reveal">Murale ou centrale : laquelle choisir?</h2>
  <div class="duo">
    <article class="choix reveal">
      <span class="etiq">Thermopompe murale</span>
      <h3>Souple, sans conduits</h3>
      <p>Une unité intérieure fixée au mur, reliée à une unité extérieure. Elle chauffe et climatise une zone ou plusieurs pièces.</p>
      <ul><li>Aucun conduit requis</li><li>Plusieurs zones possibles</li></ul>
      <a class="lien" href="#">Voir les thermopompes murales {ARR}</a>
    </article>
    <article class="choix choix-fonce reveal d1">
      <span class="etiq">Thermopompe centrale</span>
      <h3>Une solution pour toute la maison</h3>
      <p>Raccordée à vos conduits, elle distribue la chaleur et la fraîcheur dans tout le bâtiment, en remplacement ou en complément d'un système existant.</p>
      <ul><li>Utilise vos conduits existants</li><li>Peut être jumelée à un appoint (bi-énergie)</li></ul>
      <a class="lien" href="#">Voir les thermopompes centrales {ARR}</a>
    </article>
  </div>
</div></section>

<!-- ================= 2. DÉROULEMENT ================= -->
<section class="sec3 fond-beige"><div class="wrap">
  <h2 class="titre3 reveal">Votre installation, étape par étape</h2>
  <div class="etapes">
    <div class="etape reveal"><div class="n">01</div><h3>Évaluation</h3><p>Nous analysons votre maison ou votre commerce : superficie, conduits, électricité, usage.</p></div>
    <div class="etape reveal d1"><div class="n">02</div><h3>Soumission détaillée</h3><p>Une soumission claire, avec l'appareil recommandé et les travaux prévus.</p></div>
    <div class="etape reveal d2"><div class="n">03</div><h3>Installation propre</h3><p>Une équipe qualifiée installe votre thermopompe à la date convenue.</p></div>
    <div class="etape reveal d3"><div class="n">04</div><h3>Mise en service</h3><p>Nous vérifions le fonctionnement et vous proposons un entretien périodique.</p></div>
  </div>
</div></section>

<!-- ================= 3. PRIX ================= -->
<section class="sec3"><div class="wrap prix">
  <div>
    <h2 class="titre3 reveal" style="margin-bottom:1.4rem">Combien coûte l'installation?</h2>
    <p class="intro reveal d1">Le prix varie d'un projet à l'autre. Voici ce qui le fait changer, pour comparer des soumissions en connaissance de cause. <em>[Fourchettes de prix et programmes d'aide à valider avant publication]</em></p>
    <ul class="facteurs reveal d2">
      <li><b>Le type d'appareil</b><span>Murale (une ou plusieurs unités) ou centrale.</span></li>
      <li><b>La puissance nécessaire</b><span>Selon la superficie, l'isolation et l'usage.</span></li>
      <li><b>Le nombre de zones</b><span>Plus il y a de zones à desservir, plus il faut d'unités ou de conduits.</span></li>
      <li><b>L'installation existante</b><span>Conduits, panneau électrique, accès à l'extérieur.</span></li>
    </ul>
  </div>
  <aside class="carte-sombre reveal d1">
    <h3>Une soumission précise, sans surprise</h3>
    <p>Nous évaluons votre projet avant de vous donner un prix. Vous savez exactement ce qui est inclus.</p>
    <a class="btn btn-b" href="#soumission">Demander une soumission {ARR}</a>
    <a class="lien lien-clair" href="#">Guide : remplacer une thermopompe, à quel prix? {ARR}</a>
  </aside>
</div></section>

<!-- ================= 4. PREUVE ================= -->
<section class="preuve3"><div class="wrap">
  <div class="note3 reveal"><b>4,9<small>/5</small></b><span>180+ avis clients <em>[à valider sur la fiche Google]</em></span></div>
  <blockquote class="reveal d1">« Service très courtois et efficace. À partir du premier appel pour soumission jusqu'à la fin de l'installation. Travail très propre, respect des dates d'échéance. »</blockquote>
  <div class="reveal d2 cite3"><span class="av">ML</span>Martin Loyer, client<a class="lien lien-clair" href="#">Lire les avis clients {ARR}</a></div>
</div></section>

<!-- ================= 5. FAQ ================= -->
<section class="sec3 fond-beige" id="faq"><div class="wrap faq-zone">
  <div>
    <h2 class="titre3 reveal" style="margin-bottom:1.2rem">Vos questions</h2>
    <p class="reveal d1" style="color:var(--doux);max-width:24em">Une autre question? Appelez-nous au <a href="tel:+14507539426" data-track="call_tracking" style="color:var(--bleu);font-weight:700;text-decoration:none">450-753-9426</a>.</p>
    <p class="voir-aussi reveal d2">Voir aussi : <a href="#">Réparation et dépannage</a><a href="#">Entretien et nettoyage</a><a href="#">Chauffage auxiliaire</a></p>
  </div>
  <div>
    <details open><summary>Quelle est la différence entre une thermopompe murale et centrale?</summary><p>La thermopompe murale chauffe et climatise une zone sans conduits. La thermopompe centrale se raccorde aux conduits de la maison pour desservir tout le bâtiment.</p></details>
    <details><summary>Une thermopompe peut-elle remplacer ma fournaise?</summary><p>Selon l'appareil et la maison, une thermopompe peut assurer une grande partie du chauffage. Au Québec, on la jumelle souvent à un chauffage d'appoint pour les grands froids (système bi-énergie). Nous évaluons votre situation avant de recommander.</p></details>
    <details><summary>Combien de temps prend l'installation?</summary><p>Cela dépend du type d'appareil et de votre maison. Nous précisons l'échéancier dans la soumission, et nous respectons les dates convenues.</p></details>
    <details><summary>Faites-vous l'entretien après l'installation?</summary><p>Oui, nous offrons un service d'entretien périodique personnalisé.</p></details>
    <details><summary>Existe-t-il des subventions pour une thermopompe?</summary><p>Des programmes d'aide peuvent exister. Nous vous indiquons ceux qui s'appliquent à votre projet. <em>[À valider avant publication]</em></p></details>
  </div>
</div></section>

<!-- ================= APPEL FINAL ================= -->
<div class="final"><div class="wrap">
  <h2 class="reveal">Installez la bonne thermopompe.</h2>
  <p class="reveal d1">Parlez à un spécialiste Bédard : évaluation, soumission détaillée, installation propre.</p>
  <div class="cta reveal d2"><a class="btn btn-b" href="#soumission">Demander une soumission {ARR}</a></div>
  <a class="grosphone reveal d3" href="tel:+14507539426" data-track="call_tracking">450-753-9426</a>
</div></div>
</main>
'''
open('src/service-installation-v3.body.html', 'w', encoding='utf-8').write(body)
print(len(body))
