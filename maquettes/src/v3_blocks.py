"""Blocs réutilisables de la version sobre : avis (carrousel) et compteurs."""
ARR = '<svg class="ico fl" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
STAR = '<svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/></svg>'
REVIEWS = [
 ("Une entreprise qui a à cœur sa clientèle. Tout a été effectué dans les règles de l'art. Si quelqu'un me pose la question où acheter une thermopompe… c'est vous que je recommanderai.", 'Mat L.', 'ML'),
 ("Service très courtois et efficace. À partir du premier appel pour soumission jusqu'à la fin de l'installation.", 'Martin Loyer', 'ML'),
 ("J'ai fait installer deux climatiseurs muraux. Travail très propre. Respect des dates d'échéance. Personnel très courtois et professionnel. Excellente compagnie!", 'K. Gianna', 'KG'),
]
def avis_block():
    slides = ''.join(f'<figure class="av-slide{" on" if i == 0 else ""}"><blockquote>{q}</blockquote><figcaption><span class="av">{ini}</span><div><b>{nom}</b><small>Client, avis Google</small></div></figcaption></figure>' for i, (q, nom, ini) in enumerate(REVIEWS))
    dots = ''.join(f'<button type="button" class="av-dot{" on" if i == 0 else ""}" aria-label="Avis {i+1}"></button>' for i in range(len(REVIEWS)))
    return f'''<section class="avis-wow" id="avis"><div class="wrap avis-grille">
  <div class="av-gauche">
    <div class="av-note reveal"><span class="gros"><span data-count="4.7" data-dec="1">4,7</span></span><span class="sur">/5</span></div>
    <div class="av-etoiles reveal d1" aria-label="5 étoiles sur 5">{STAR * 5}</div>
    <p class="av-txt reveal d2"><b>200+ avis Google</b></p>
    <a class="btn btn-b reveal d3" href="#">Lire les avis {ARR}</a>
  </div>
  <div class="av-droite reveal d1">
    <div class="av-car" data-car>
      <span class="guil" aria-hidden="true">«</span>
      <div class="av-slides">{slides}</div>
      <div class="av-nav"><div class="av-dots">{dots}</div><div class="av-fleches"><button type="button" class="av-prev" aria-label="Avis précédent">{ARR}</button><button type="button" class="av-next" aria-label="Avis suivant">{ARR}</button></div></div>
    </div>
    <div class="av-puces"><span>Travail propre</span><span>Échéances respectées</span><span>Service courtois</span></div>
  </div>
</div></section>'''
