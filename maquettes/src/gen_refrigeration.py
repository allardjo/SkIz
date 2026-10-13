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
cartes=''.join([
 carte(0,'tool','Installation de systèmes','Installation de systèmes de réfrigération commerciale avec minutie, efficacité et professionnalisme.',['Évaluation de vos besoins','Installation sur chantier','Mise en service']),
 carte(1,'clock','Service et dépannage 24 h','Une panne de réfrigération menace votre marchandise : une équipe est disponible jour et nuit.',['Diagnostic et réparation','Urgence 24 h sur 24','Suivi après intervention'],True),
 carte(2,'refresh','Entretien préventif','Un entretien périodique personnalisé garde vos équipements performants et réduit les risques de panne.',['Inspection régulière','Programme sur mesure','Dossier de vos équipements']),
 carte(3,'snow','Climatisation commerciale','Nos techniciens interviennent aussi en climatisation pour les commerces, les industries et les institutions.',['Installation et remplacement','Entretien et service','Commercial et institutionnel']),
 carte(4,'wind','Contrôle et régulation','Du contrôle, de la réfrigération et de la climatisation, avec des techniciens à l\'affût des nouvelles technologies.',['Contrôle des systèmes','Optimisation de la performance','Formation continue de l\'équipe'],True),
 carte(5,'users','Une équipe de frigoristes','Apprentis et compagnons qui travaillent en service, en installation, en commercial, en industriel et en institutionnel.',['Techniciens qualifiés','Formation continue','Plus de 65 professionnels chez Bédard']),
])
facteurs=[('Le type d\'équipement','Chambre froide, comptoir, système centralisé ou autre équipement de réfrigération.'),('La taille et la charge','Volume à refroidir, température visée et usage du local.'),('L\'état de l\'installation existante','Nouveau système à installer, ou remplacement et modification d\'un système en place.'),('L\'accès au chantier','Espaces restreints, travaux en commerce ouvert, contraintes d\'horaire.'),('L\'entretien prévu','Un programme périodique après l\'installation, adapté à vos équipements.')]
fl=''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a,b in facteurs)
faq=[
 ("Qu'est-ce que la réfrigération commerciale?","La réfrigération commerciale regroupe les systèmes qui conservent au froid la marchandise, les aliments ou les produits d'un commerce, d'une industrie ou d'une institution. Elle demande des équipements fiables et un entretien régulier."),
 ("Intervenez-vous en cas de panne?",f"Oui, un service d'urgence est offert 24 heures sur 24. Appelez le {TEL}. Une panne de réfrigération peut mettre votre marchandise à risque : appelez dès que vous la constatez."),
 ("Offrez-vous un entretien préventif?","Oui, nous offrons un service d'entretien périodique personnalisé pour vos équipements de réfrigération et de climatisation."),
 ("Installez-vous de nouveaux systèmes de réfrigération?","Oui. Nos techniciens spécialisés et qualifiés installent des systèmes de réfrigération commerciale. Nous évaluons d'abord vos besoins, puis nous vous remettons une soumission détaillée."),
 ("Faites-vous aussi la climatisation commerciale?","Oui. Nos techniciens interviennent en réfrigération, en climatisation et en contrôle, pour des bâtiments commerciaux, industriels et institutionnels."),
 ("Combien coûte un projet de réfrigération commerciale?","Le prix dépend du type d'équipement, de la taille du projet, de l'état de l'installation existante et de l'accès au chantier. Nous évaluons votre projet, puis nous vous remettons une soumission détaillée."),
 ("Quels secteurs desservez-vous?","Nos travaux se font en grande majorité dans Lanaudière et ses environs. Contactez-nous pour un projet situé ailleurs."),
]
faqh=''.join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(faq))
import json
open('src/refrigeration.faq.json','w',encoding='utf-8').write(json.dumps([{"q":q,"a":a} for q,a in faq],ensure_ascii=False))

body=f'''<main>
<!-- ================= HERO ================= -->
<div class="hero hero-service hero-comm hero-refrig">
  <div class="bg"></div>
  <div class="wrap">
    <div>
      <nav class="fil" aria-label="Fil d'Ariane"><a href="#">Accueil</a><span>›</span><a href="#">Commercial</a><span>›</span><b>Réfrigération commerciale</b></nav>
      <div class="pastille reveal"><b>{CHECK}</b>Frigoristes · Joliette et Lanaudière</div>
      <h1 class="reveal d1">Réfrigération commerciale à <em>Joliette</em></h1>
      <p class="lead reveal d2"><b>Des frigoristes qualifiés, du service d'urgence 24 h à l'installation.</b> Installation, entretien et dépannage de systèmes de réfrigération et de climatisation pour les commerces, les industries et les institutions.</p>
      <div class="cta reveal d3">
        <a class="btn btn-b" href="#soumission">Demander une soumission {ARROW}</a>
        <a class="btn btn-l" href="tel:+14507539426" data-track="call_tracking">{ic('clock')}<span>Urgence 24 h : {TEL}</span></a>
      </div>
    </div>
    <form class="devis-carte reveal d2" id="soumission" action="#" onsubmit="return false" data-form="commercial-refrigeration">
      <h2>Soumission en réfrigération</h2>
      <p class="sous">Décrivez votre besoin : un spécialiste vous rappelle sous 24 heures ouvrables.</p>
      <div class="champ"><label for="r-nom">Nom et entreprise</label><input id="r-nom" autocomplete="organization" placeholder="Votre nom, votre entreprise"></div>
      <div class="champ"><label for="r-tel">Téléphone</label><input id="r-tel" type="tel" autocomplete="tel" placeholder="450 000-0000"></div>
      <div class="champ"><label for="r-type">Type de besoin</label>
        <select id="r-type"><option>Nouvelle installation</option><option>Remplacement ou modification</option><option>Entretien préventif</option><option>Climatisation commerciale</option><option>Dépannage / urgence</option></select></div>
      <button class="btn btn-r" type="submit">Être rappelé {ARROW}</button>
      <p class="note">Panne? <a href="tel:+14507539426" data-track="call_tracking">Appelez le {TEL}</a></p>
    </form>
  </div>
</div>

<!-- ================= POINTS FORTS ================= -->
<div class="faits"><div class="wrap">
  <div class="boite reveal">
    <div class="fait">{ic('clock')}<b>Urgence 24 h</b><span>Une équipe disponible jour et nuit</span></div>
    <div class="fait">{ic('users')}<b>Frigoristes qualifiés</b><span>Apprentis et compagnons</span></div>
    <div class="fait">{ic('refresh')}<b>Entretien préventif</b><span>Personnalisé, pour moins de pannes</span></div>
    <div class="fait">{ic('cal')}<b>40+ ans</b><span>D'expérience dans Lanaudière</span></div>
  </div>
</div></div>

<!-- ================= SERVICES ================= -->
<section><div class="wrap">
  <div class="tete">
    <div><span class="eyebrow">Nos services</span><h2 class="reveal">Vos frigoristes à Joliette</h2></div>
    <p class="reveal d1">Des techniciens spécialisés et qualifiés, toujours à l'affût des nouvelles technologies pour mieux vous servir.</p>
  </div>
  <div class="metiers metiers-6">{cartes}</div>
  <p class="placeholder reveal">[Types d'équipements à confirmer pour la liste détaillée : chambres froides, comptoirs réfrigérés, systèmes centralisés, etc.]</p>
</div></section>

<!-- ================= URGENCE ================= -->
<section class="sombre"><div class="wrap bande-urgence">
  <div>
    <span class="eyebrow" style="color:var(--cyan)">Urgence 24 h</span>
    <h2 class="reveal">Une panne de froid? N'attendez pas.</h2>
    <p class="reveal d1">Pour un commerce, une panne de réfrigération met la marchandise à risque. Notre équipe de service est disponible 24 heures sur 24 pour intervenir rapidement.</p>
    <a class="btn btn-b reveal d2" href="tel:+14507539426" data-track="call_tracking">Urgence 24 h : {TEL}</a>
  </div>
  <ul class="liste-sombre">
    <li class="reveal"><b>1. Vous appelez</b><br>Un technicien prend votre appel, jour et nuit.</li>
    <li class="reveal d1"><b>2. Nous diagnostiquons</b><br>Un frigoriste qualifié identifie la cause de la panne.</li>
    <li class="reveal d2"><b>3. Nous réparons</b><br>Puis nous vous proposons un entretien préventif pour éviter la récidive.</li>
  </ul>
</div></section>

<!-- ================= PUBLICS ================= -->
<section class="fond-beige"><div class="wrap">
  <div class="tete">
    <div><span class="eyebrow">Types de clients</span><h2 class="reveal">Du commerce à l'institution</h2></div>
    <p class="reveal d1">Nos frigoristes travaillent en commercial, en industriel, en institutionnel et en résidentiel.</p>
  </div>
  <div class="publics">
    <div class="public reveal"><b>Commerces</b><span>Magasins, restaurants et commerces d'alimentation. <em>[exemples à valider]</em></span></div>
    <div class="public reveal d1"><b>Industries</b><span>Entreprises dont les produits exigent un froid contrôlé. <em>[exemples à valider]</em></span></div>
    <div class="public reveal d2"><b>Institutions</b><span>Bâtiments institutionnels et leurs cuisines ou entrepôts. <em>[exemples à valider]</em></span></div>
  </div>
</div></section>

<!-- ================= DÉROULEMENT ================= -->
<section><div class="wrap">
  <div class="tete"><div><span class="eyebrow">Déroulement</span><h2 class="reveal">Comment se déroule votre projet</h2></div></div>
  <div class="etapes etapes-4">
    <div class="etape reveal"><div class="n">01</div><h3>Évaluation</h3><p>Nous évaluons vos besoins, votre local et vos équipements existants.</p></div>
    <div class="etape reveal d1"><div class="n">02</div><h3>Soumission détaillée</h3><p>Vous recevez une soumission claire, avec les équipements et les travaux prévus.</p></div>
    <div class="etape reveal d2"><div class="n">03</div><h3>Installation</h3><p>Des frigoristes qualifiés installent le système selon l'échéancier convenu.</p></div>
    <div class="etape reveal d3"><div class="n">04</div><h3>Mise en service et entretien</h3><p>Nous vérifions le fonctionnement, puis proposons un entretien préventif personnalisé.</p></div>
  </div>
</div></section>

<!-- ================= PRIX ================= -->
<section class="fond-ciel"><div class="wrap prix">
  <div>
    <span class="eyebrow">Prix</span>
    <h2 class="reveal">Combien coûte un système de réfrigération commerciale?</h2>
    <p class="intro reveal d1">Chaque projet est différent. Voici ce qui fait varier le prix.</p>
    <ul class="facteurs reveal d2">{fl}</ul>
  </div>
  <aside class="carte-sombre reveal d1">
    <h3>Une soumission détaillée</h3>
    <p>Nous évaluons votre projet avant de vous donner un prix. Vous savez exactement ce qui est inclus.</p>
    <a class="btn btn-b" href="#soumission">Demander une soumission {ARROW}</a>
    <a class="lien lien-clair" href="tel:+14507539426" data-track="call_tracking">Ou appelez le {TEL} {ARROW}</a>
  </aside>
</div></section>

<!-- ================= RÉALISATIONS ================= -->
<section><div class="wrap">
  <div class="programmes reveal">
    <span class="eyebrow">Réalisations</span>
    <h2>Projets de réfrigération récents</h2>
    <p>Projets commerciaux, industriels et institutionnels livrés par Bédard, avec photos, type d'équipement, ville et travaux réalisés. <em>[À fournir : 3 à 6 projets avec l'autorisation des clients; licences et certifications (RBQ, CCQ, certificat de frigoriste) à afficher ici]</em></p>
  </div>
</div></section>

<!-- ================= FAQ ================= -->
<section class="fond-ciel" id="faq"><div class="wrap faq-zone">
  <div>
    <span class="eyebrow">Questions fréquentes</span>
    <h2 class="reveal">Réfrigération commerciale : vos questions</h2>
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
    <a class="lie reveal d2" href="#"><b>Ferblanterie</b><span>Conduits et pièces sur mesure.</span><i>{ic('tool')}</i></a>
    <a class="lie reveal d3" href="#"><b>Carrières</b><span>Devenez frigoriste chez Bédard.</span><i>{ic('users')}</i></a>
  </div>
</div></section>

<!-- ================= APPEL FINAL ================= -->
<div class="final"><div class="wrap">
  <h2 class="reveal">Du froid fiable, jour et nuit.</h2>
  <p class="reveal d1">Parlez à un spécialiste Bédard : installation, entretien préventif et dépannage 24 h.</p>
  <div class="cta reveal d2"><a class="btn btn-b" href="#soumission">Demander une soumission {ARROW}</a></div>
  <a class="grosphone reveal d3" href="tel:+14507539426" data-track="call_tracking">{TEL}</a>
</div></div>
</main>
'''
open('src/refrigeration.body.html','w',encoding='utf-8').write(body)
print(len(body))
