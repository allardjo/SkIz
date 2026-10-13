"""Génère les corps HTML des pages Contact et Soumission (sources de maquettes/src/)."""
ARROW='<svg class="ico fl" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK='<svg class="ico" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'
I={
'phone':'<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
'mail':'<path d="M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/><polyline points="22,6 12,13 2,6"/>',
'pin':'<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
'clock':'<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
'star':'<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/>',
'fb':'<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
'in':'<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zM4 6a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"/>',
}
def ic(n): return f'<svg class="ico" viewBox="0 0 24 24">{I[n]}</svg>'
TEL='<a href="tel:+14507539426" data-track="call_tracking">450-753-9426</a>'

zones=['Joliette','Notre-Dame-des-Prairies','Saint-Charles-Borromée','Crabtree','Saint-Paul','Saint-Thomas','Lavaltrie','Berthierville','Saint-Félix-de-Valois','Saint-Jean-de-Matha','Rawdon','Repentigny']
zh=''.join(f'<span>{z}</span>' for z in zones)

contact=f'''<main>
<!-- ================= HERO CONTACT ================= -->
<div class="hero hero-service hero-court hero-contact">
  <div class="bg"></div>
  <div class="wrap">
    <div>
      <nav class="fil" aria-label="Fil d'Ariane"><a href="#">Accueil</a><span>›</span><b>Contact</b></nav>
      <div class="pastille reveal"><b>{CHECK}</b>Réponse rapide · Urgence 24 h</div>
      <h1 class="reveal d1">Parlons de votre <em>projet</em></h1>
      <p class="lead reveal d2"><b>Une équipe de plus de 65 professionnels à Joliette.</b> Appelez-nous, écrivez-nous ou passez nous voir : un spécialiste vous répond pour le chauffage, la climatisation, la ventilation et la réfrigération.</p>
    </div>
  </div>
</div>

<!-- ================= 4 FAÇONS DE JOINDRE ================= -->
<div class="faits"><div class="wrap"><div class="cartes-contact">
  <a class="cc reveal" href="tel:+14507539426" data-track="call_tracking">{ic('phone')}<small>Téléphone</small><b>450-753-9426</b><span>Lundi au vendredi, 8 h à 17 h</span></a>
  <a class="cc cc-urgence reveal d1" href="tel:+14507539426" data-track="call_tracking">{ic('clock')}<small>Urgence 24 h</small><b>450-753-9426</b><span>Une panne? Une équipe est disponible jour et nuit.</span></a>
  <a class="cc reveal d2" href="tel:+18009530153" data-track="call_tracking">{ic('phone')}<small>Sans frais</small><b>1-800-953-0153</b><span>Partout au Québec</span></a>
  <a class="cc reveal d3" href="mailto:info@cbedard.com">{ic('mail')}<small>Courriel</small><b>info@cbedard.com</b><span>Nous répondons rapidement</span></a>
</div></div></div>

<!-- ================= FORMULAIRE + INFOS ================= -->
<section><div class="wrap contact-lay">
  <form class="form-contact reveal" action="#" onsubmit="return false" data-form="contact">
    <h2>Joindre un spécialiste</h2>
    <p class="sous">Laissez-nous vos coordonnées et votre question : on vous rappelle.</p>
    <div class="grille2">
      <div class="champ"><label for="k-nom">Prénom et nom*</label><input id="k-nom" autocomplete="name" placeholder="Votre nom"></div>
      <div class="champ"><label for="k-tel">Téléphone*</label><input id="k-tel" type="tel" autocomplete="tel" placeholder="450 000-0000"></div>
      <div class="champ plein"><label for="k-mail">Courriel*</label><input id="k-mail" type="email" autocomplete="email" placeholder="vous@exemple.com"></div>
      <div class="champ plein"><label for="k-msg">Votre message</label><textarea id="k-msg" placeholder="Décrivez brièvement votre besoin…"></textarea></div>
    </div>
    <button class="btn btn-r" type="submit">Envoyer le message {ARROW}</button>
    <p class="legal">Pour une demande de prix, utilisez plutôt la <a href="#" style="color:var(--bleu);font-weight:700">soumission gratuite</a>. <em>[Mention Loi 25 à valider]</em></p>
  </form>

  <div>
    <span class="eyebrow">Coordonnées</span>
    <h2 class="reveal">Venez nous voir à Joliette</h2>
    <address class="adresse reveal d1"><b>Bédard — Performance thermique</b><br>304, boulevard de l'Industrie<br>Joliette (Québec) J6E 8V2</address>
    <div class="heures reveal d2">
      <div><b>Lundi au vendredi</b><span>8 h à 17 h (fermé de 12 h à 13 h)</span></div>
      <div><b>Samedi et dimanche</b><span>Sur rendez-vous avec un représentant</span></div>
      <div class="urg"><b>Service d'urgence</b><span>24 heures sur 24, 7 jours sur 7</span></div>
    </div>
    <a class="btn btn-m reveal d3" href="https://www.google.com/maps/dir/?api=1&destination=304+boulevard+de+l%27Industrie+Joliette+QC" target="_blank" rel="noopener">Obtenir l'itinéraire {ARROW}</a>
    <div class="reseaux reveal d3">
      <a href="#">{ic('fb')}Facebook</a>
      <a href="#">{ic('in')}LinkedIn</a>
      <a href="#">{ic('star')}Laissez-nous un avis Google</a>
    </div>
  </div>
</div></section>

<!-- ================= CARTE ================= -->
<section style="padding-top:0"><div class="wrap">
  <div class="carte-map reveal">
    <iframe title="Carte : 304, boulevard de l'Industrie, Joliette" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=304+boulevard+de+l%27Industrie+Joliette+QC&amp;output=embed"></iframe>
    <div class="bas"><span>304, boulevard de l'Industrie, Joliette</span><a class="lien" href="https://www.google.com/maps/search/?api=1&query=304+boulevard+de+l%27Industrie+Joliette+QC" target="_blank" rel="noopener">Ouvrir dans Google Maps {ARROW}</a></div>
  </div>
</div></section>

<!-- ================= TEXTE LOCAL ================= -->
<section class="fond-beige"><div class="wrap seo-bloc">
  <div>
    <span class="eyebrow">Notre secteur</span>
    <h2 class="reveal">Chauffage et climatisation à Joliette et dans Lanaudière</h2>
  </div>
  <div>
    <p class="reveal">Depuis plus de 40 ans, Bédard conseille, installe et entretient des systèmes de chauffage, de ventilation, de climatisation et de réfrigération pour les résidences, les commerces et les institutions de la région.</p>
    <p class="reveal d1">Nos spécialistes vous guident dans le choix du bon appareil et vous informent des programmes gouvernementaux qui peuvent s'appliquer à votre projet : climatisation, chauffage, ventilation, géothermie ou plancher chauffant. L'estimation à votre domicile ou à nos bureaux est gratuite.</p>
    <div class="zones reveal d2">{zh}</div>
    <p class="placeholder reveal">[Liste des municipalités desservies à valider]</p>
  </div>
</div></section>

<!-- ================= APPEL FINAL ================= -->
<div class="final"><div class="wrap">
  <h2 class="reveal">Un projet? Une panne? On est là.</h2>
  <p class="reveal d1">Soumission gratuite pour votre maison ou votre commerce, service d'urgence 24 h.</p>
  <div class="cta reveal d2"><a class="btn btn-b" href="#">Demander une soumission gratuite {ARROW}</a></div>
  <a class="grosphone reveal d3" href="tel:+14507539426" data-track="call_tracking">450-753-9426</a>
</div></div>
</main>
'''

def cr(name, val, label, i, cls=''):
    idd=f'{name}-{i}'
    return f'<div class="cr"><input type="radio" id="{idd}" name="{name}" value="{val}"><label for="{idd}">{label}</label></div>'
def grp(name, opts, cls=''):
    return f'<div class="choix-rapide {cls}">'+''.join(cr(name,o,o,i) for i,o in enumerate(opts))+'</div>'

produits=['Système mural (thermopompe et climatiseur)','Système de ventilation centralisé','Échangeur d\'air','Fournaise électrique','Fournaise au bois','Géothermie','Plancher radiant','Commercial']
entendu=['Déjà client','Référence d\'un proche','Référence d\'un employé','Moteur de recherche','Facebook','Camion sur la route','Salon habitation','CAA Habitation','Pages Jaunes']
opt=''.join(f'<option>{e}</option>' for e in entendu)

soum=f'''<main>
<!-- ================= HERO SOUMISSION ================= -->
<div class="hero hero-service hero-court hero-soum">
  <div class="bg"></div>
  <div class="wrap">
    <div>
      <nav class="fil" aria-label="Fil d'Ariane"><a href="#">Accueil</a><span>›</span><b>Soumission</b></nav>
      <div class="pastille reveal"><b>{CHECK}</b>Gratuit · Sans engagement</div>
      <h1 class="reveal d1">Votre soumission gratuite, <em>en 2 minutes</em></h1>
      <p class="lead reveal d2"><b>Dites-nous ce qu'il vous faut.</b> Un spécialiste Bédard vous rappelle pour évaluer votre projet et vous remettre une soumission détaillée. Chauffage, climatisation, ventilation, géothermie, commercial.</p>
    </div>
  </div>
</div>

<!-- ================= FORMULAIRE EN 3 ÉTAPES ================= -->
<section style="padding-top:clamp(3rem,6vw,5rem)"><div class="wrap soum-lay">
  <form class="soum-form reveal" id="soum" action="#" onsubmit="return false" data-form="soumission" novalidate>
    <div class="progres" aria-hidden="true">
      <div class="actif" data-p="1">1. Projet<small>Quoi et où</small></div>
      <div data-p="2">2. Coordonnées<small>Pour vous rappeler</small></div>
      <div data-p="3">3. Détails<small>Facultatif</small></div>
    </div>

    <div class="etape-f actif" data-e="1">
      <h2>Quel est votre projet?</h2>
      <p class="sous">Choisissez le produit qui vous intéresse.</p>
      <p class="q">Pour quel produit aimeriez-vous de l'information?*</p>
      {grp('produit',produits)}
      <div class="grille2">
        <div class="champ"><label for="s-ville">Ville du projet*</label><input id="s-ville" name="ville" autocomplete="address-level2" placeholder="Joliette"></div>
        <div class="champ"><label>Êtes-vous client chez nous?</label>
          <div class="choix-rapide" style="margin:0;grid-template-columns:1fr 1fr;gap:.5rem">{cr('client','Nouveau client','Nouveau',0)}{cr('client','Client existant','Existant',1)}</div></div>
      </div>
      <p class="erreur" id="err1" role="alert" style="color:var(--rouille);font-weight:600;display:none;margin-top:1rem">Choisissez un produit et indiquez la ville du projet.</p>
      <div class="soum-nav"><span></span><button class="btn btn-r" type="button" data-next="2">Continuer {ARROW}</button></div>
    </div>

    <div class="etape-f" data-e="2">
      <h2>Comment vous joindre?</h2>
      <p class="sous">Un spécialiste vous rappelle pour évaluer votre projet.</p>
      <div class="grille2">
        <div class="champ plein"><label for="s-nom">Prénom et nom*</label><input id="s-nom" name="nom" autocomplete="name" placeholder="Votre nom"></div>
        <div class="champ"><label for="s-tel">Téléphone*</label><input id="s-tel" name="tel" type="tel" autocomplete="tel" placeholder="450 000-0000"></div>
        <div class="champ"><label for="s-mail">Courriel*</label><input id="s-mail" name="courriel" type="email" autocomplete="email" placeholder="vous@exemple.com"></div>
      </div>
      <p class="erreur" id="err2" role="alert" style="color:var(--rouille);font-weight:600;display:none">Entrez votre nom, un téléphone et un courriel valides.</p>
      <div class="soum-nav"><button class="btn-retour" type="button" data-next="1">← Retour</button><button class="btn btn-r" type="button" data-next="3">Continuer {ARROW}</button></div>
      <p class="legal">Vous pouvez aussi <a href="#" data-envoyer style="color:var(--bleu);font-weight:700">envoyer votre demande maintenant</a>, sans ajouter de détails.</p>
    </div>

    <div class="etape-f" data-e="3">
      <h2>Précisez votre projet</h2>
      <p class="sous">Facultatif, mais ça nous aide à vous donner un prix plus juste.</p>
      <p class="q">Construction existante ou nouvelle construction?</p>
      {grp('construction',['Construction existante','Nouvelle construction'])}
      <p class="q">Remplacement ou nouvelle installation?</p>
      {grp('remplacement',['Remplacement d\'un équipement','Nouvelle installation'])}
      <div class="grille2">
        <div class="champ plein"><label for="s-entendu">Où avez-vous entendu parler de nous?</label><select id="s-entendu" name="entendu"><option value="">Choisir</option>{opt}</select></div>
        <div class="champ plein"><label for="s-com">Commentaires</label><textarea id="s-com" name="commentaires" placeholder="Superficie, équipement actuel, échéancier…"></textarea></div>
        <div class="champ plein"><label for="s-file">Photos ou plans (facultatif)</label><div class="fichier"><input id="s-file" name="fichier" type="file" accept=".jpg,.jpeg,.png,.gif,.tiff,.bmp,.pdf" multiple></div></div>
      </div>
      <div class="soum-nav"><button class="btn-retour" type="button" data-next="2">← Retour</button><button class="btn btn-r" type="submit">Envoyer ma demande {ARROW}</button></div>
      <p class="legal">Photos (JPG, PNG, PDF…) acceptées. Vos renseignements servent seulement à traiter votre demande. <em>[Mention Loi 25 à valider]</em></p>
    </div>

    <div class="merci" id="merci" role="status">
      <div class="rond">{CHECK}</div>
      <h2>Merci, votre demande est envoyée!</h2>
      <p class="sous" style="max-width:30em;margin:.6rem auto 1.6rem">Un spécialiste Bédard vous rappelle sous peu. Une urgence? Appelez-nous tout de suite.</p>
      <a class="btn btn-m" href="tel:+14507539426" data-track="call_tracking">450-753-9426</a>
    </div>
  </form>

  <aside class="aide-soum">
    <div class="aide-carte reveal d1">
      <h3>Et après votre demande?</h3>
      <ol class="suite">
        <li><b>On vous rappelle</b>Un spécialiste valide votre besoin. <em>[Délai à confirmer]</em></li>
        <li><b>Évaluation</b>À votre domicile ou à nos bureaux, sans frais.</li>
        <li><b>Soumission détaillée</b>Vous savez exactement ce qui est inclus.</li>
      </ol>
    </div>
    <div class="aide-tel reveal d2">
      <small>Vous préférez parler à quelqu'un?</small>
      <a class="gros" href="tel:+14507539426" data-track="call_tracking">450-753-9426</a>
      <p>Lundi au vendredi, 8 h à 17 h. Service d'urgence 24 h.</p>
    </div>
  </aside>
</div></section>

<!-- ================= PREUVES ================= -->
<section class="fond-ciel"><div class="wrap">
  <div class="tete">
    <div><span class="eyebrow">Pourquoi Bédard</span><h2 class="reveal">Une équipe qui livre</h2></div>
    <p class="reveal d1">4,9 sur 5, selon plus de 180 avis clients. <em style="opacity:.7">[à valider sur la fiche Google]</em></p>
  </div>
  <div class="avis3">
    <figure class="carte-avis carte-avis-fonce reveal"><div class="etoiles">{{{{ETOILES}}}}</div><blockquote>« Une entreprise qui a à cœur sa clientèle. Tout a été effectué dans les règles de l'art. »</blockquote><cite><span class="av">ML</span><div>Mat L.<span>Client, Google</span></div></cite></figure>
    <figure class="carte-avis reveal d1"><div class="etoiles">{{{{ETOILES}}}}</div><blockquote>« Service très courtois et efficace. À partir du premier appel pour soumission jusqu'à la fin de l'installation. »</blockquote><cite><span class="av">ML</span><div>Martin Loyer<span>Client, Google</span></div></cite></figure>
    <figure class="carte-avis reveal d2"><div class="etoiles">{{{{ETOILES}}}}</div><blockquote>« Travail très propre. Respect des dates d'échéance. Personnel très courtois et professionnel. »</blockquote><cite><span class="av">KG</span><div>K. Gianna<span>Cliente, Google</span></div></cite></figure>
  </div>
</div></section>

<script>
(function(){{
  var f=document.getElementById('soum');if(!f)return;
  var etapes=f.querySelectorAll('.etape-f'),prog=f.querySelectorAll('.progres div');
  function va(n){{etapes.forEach(function(e){{e.classList.toggle('actif',e.dataset.e==n)}});prog.forEach(function(p){{var k=+p.dataset.p;p.classList.toggle('actif',k==n);p.classList.toggle('fait-p',k<n)}});f.scrollIntoView({{behavior:'smooth',block:'start'}})}}
  function ok1(){{return f.querySelector('[name=produit]:checked')&&f.ville.value.trim()}}
  function ok2(){{return f.nom.value.trim()&&f.tel.value.replace(/\\D/g,'').length>=10&&/.+@.+\\..+/.test(f.courriel.value)}}
  function envoi(){{if(!ok1()){{va(1);document.getElementById('err1').style.display='block';return}}if(!ok2()){{va(2);document.getElementById('err2').style.display='block';return}}
    window.dataLayer=window.dataLayer||[];window.dataLayer.push({{event:'form_submit',form_name:'soumission'}});
    etapes.forEach(function(e){{e.classList.remove('actif')}});f.querySelector('.progres').style.display='none';document.getElementById('merci').classList.add('actif')}}
  f.addEventListener('click',function(ev){{var b=ev.target.closest('[data-next]');if(b){{var n=+b.dataset.next;
    if(n==2&&!ok1()){{document.getElementById('err1').style.display='block';return}}
    if(n==3&&!ok2()){{document.getElementById('err2').style.display='block';return}}
    va(n)}}
    if(ev.target.closest('[data-envoyer]')){{ev.preventDefault();envoi()}}}});
  f.addEventListener('submit',envoi);
}})();
</script>
<!-- ================= APPEL FINAL ================= -->
</main>
'''
open('src/contact.body.html','w',encoding='utf-8').write(contact)
open('src/soumission.body.html','w',encoding='utf-8').write(soum)
print(len(contact),len(soum))
