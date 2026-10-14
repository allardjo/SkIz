"""Génère les corps HTML des trois pages de service résidentielles (réparation, entretien et nettoyage, chauffage auxiliaire)."""
import json, re
ARROW='<svg class="ico fl" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK='<svg class="ico" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'
I={
'phone':'<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
'clock':'<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
'tool':'<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
'star':'<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/>',
'snow':'<path d="M12 2v20M4.9 6l14.2 12M19.1 6L4.9 18M2 12h20"/>',
'flame':'<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.07-2.14-.22-4.05 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.15.43-2.3 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
'wind':'<path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"/>',
'drop':'<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>',
'volume':'<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07M19.07 4.93a10 10 0 0 1 0 14.14"/>',
'alert':'<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0zM12 9v4M12 17h.01"/>',
'power':'<path d="M18.36 6.64a9 9 0 1 1-12.73 0M12 2v10"/>',
'refresh':'<polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/>',
'cal':'<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
'users':'<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
'thermo':'<path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"/>',
}
def ic(n,c='ico'): return f'<svg class="{c}" viewBox="0 0 24 24">{I[n]}</svg>'
TEL='450-753-9426'
TELLINK=f'<a href="tel:+14507539426" data-track="call_tracking">{TEL}</a>'
ETOILES='{{ETOILES}}'

def hero(p):
    opts=''.join(f'<option>{o}</option>' for o in p['types'])
    return f'''<main>
<div class="hero hero-service {p['hclass']}">
  <div class="bg"></div>
  <div class="wrap">
    <div>
      <nav class="fil" aria-label="Fil d'Ariane"><a href="#">Accueil</a><span>›</span><a href="#">{p.get('parent','Services')}</a><span>›</span><b>{p['fil']}</b></nav>
      <div class="pastille reveal"><b>{CHECK}</b>{p['pastille']}</div>
      <h1 class="reveal d1">{p['h1']}</h1>
      <p class="lead reveal d2">{p['lead']}</p>
      <div class="cta reveal d3">
        <a class="btn btn-b" href="#soumission">{p['cta']} {ARROW}</a>
        <a class="btn btn-l" href="tel:+14507539426" data-track="call_tracking">{ic('phone')}<span>{TEL}</span></a>
      </div>
      <div class="signes reveal d4">{''.join(f'<span>{CHECK}{x}</span>' for x in p['signes'])}</div>
    </div>
    <form class="devis-carte reveal d2" id="soumission" action="#" onsubmit="return false" data-form="{p['key']}">
      <h2>{p['form_h']}</h2>
      <p class="sous">{p['form_sub']}</p>
      <div class="champ"><label for="nom">Nom</label><input id="nom" autocomplete="name" placeholder="Votre nom"></div>
      <div class="champ"><label for="tel">Téléphone</label><input id="tel" type="tel" autocomplete="tel" placeholder="450 000-0000"></div>
      <div class="champ"><label for="type">{p['form_label']}</label><select id="type">{opts}</select></div>
      <button class="btn btn-r" type="submit">{p['form_btn']} {ARROW}</button>
      <p class="note">Urgence? <a href="tel:+14507539426" data-track="call_tracking">Appelez le {TEL}</a></p>
    </form>
  </div>
</div>
'''

def faits(items):
    return '<div class="faits"><div class="wrap"><div class="boite reveal">'+''.join(f'<div class="fait">{ic(i)}<b>{b}</b><span>{s}</span></div>' for i,b,s in items)+'</div></div></div>\n'

def tete(eyebrow,h2,intro=None,fond=''):
    return f'<div class="tete"><div><span class="eyebrow">{eyebrow}</span><h2 class="reveal">{h2}</h2></div>'+(f'<p class="reveal d1">{intro}</p>' if intro else '')+'</div>'

def symptomes(eyebrow,h2,intro,items):
    c=''.join(f'<div class="symptome reveal d{i%3}"><span class="ico-g">{ic(ico)}</span><b>{t}</b><span>{d}</span></div>' for i,(ico,t,d) in enumerate(items))
    return f'<section><div class="wrap">{tete(eyebrow,h2,intro)}<div class="symptomes">{c}</div></div></section>\n'

def duo(eyebrow,h2,intro,g,d):
    def card(x,fonce):
        lis=''.join(f'<li>{t}</li>' for t in x['ul'])
        return f'<article class="choix{" choix-fonce" if fonce else ""} reveal{" d1" if fonce else ""}"><span class="etiq">{x["etiq"]}</span><h3>{x["h3"]}</h3><p>{x["p"]}</p><ul>{lis}</ul><p class="pour"><b>{x["pour_t"]}</b> {x["pour"]}</p></article>'
    return f'<section class="fond-beige"><div class="wrap">{tete(eyebrow,h2,intro)}<div class="duo">{card(g,False)}{card(d,True)}</div></div></section>\n'

def urgence(p):
    lis=''.join(f'<li class="reveal d{i}"><b>{a}</b><br>{b}</li>' for i,(a,b) in enumerate(p['urg_items']))
    return f'''<section class="sombre"><div class="wrap bande-urgence">
  <div><span class="eyebrow" style="color:var(--cyan)">{p['urg_eyebrow']}</span><h2 class="reveal">{p['urg_h2']}</h2>
  <p class="reveal d1">{p['urg_p']}</p>
  {p.get('urg_btn') or f'<a class="btn btn-b reveal d2" href="tel:+14507539426" data-track="call_tracking">Urgence 24 h : {TEL}</a>'}</div>
  <ul class="liste-sombre">{lis}</ul>
</div></section>
'''

def etapes(eyebrow,h2,steps):
    c=''.join(f'<div class="etape reveal d{i}"><div class="n">0{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(steps))
    return f'<section><div class="wrap"><div class="tete"><div><span class="eyebrow">{eyebrow}</span><h2 class="reveal">{h2}</h2></div></div><div class="etapes etapes-4">{c}</div></div></section>\n'

def prix(p):
    fl=''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a,b in p['facteurs'])
    return f'''<section class="fond-ciel"><div class="wrap prix"><div><span class="eyebrow">Prix</span><h2 class="reveal">{p['prix_h2']}</h2>
  <p class="intro reveal d1">{p['prix_intro']}</p><ul class="facteurs reveal d2">{fl}</ul>{p.get('prix_note','')}</div>
  <aside class="carte-sombre reveal d1"><h3>Une soumission claire</h3><p>{p['prix_carte']}</p>
  <a class="btn btn-b" href="#soumission">{p['cta']} {ARROW}</a>
  <a class="lien lien-clair" href="{p['guide_href']}">{p['guide_txt']} {ARROW}</a></aside></div></section>
'''

def avis():
    return f'''<section><div class="wrap">{tete('Avis clients','Ils ont choisi Bédard','4,9 sur 5, selon plus de 180 avis clients. <em style="opacity:.7">[à valider sur la fiche Google]</em>')}
  <div class="avis3">
    <figure class="carte-avis carte-avis-fonce reveal"><div class="etoiles">{ETOILES}</div><blockquote>« Une entreprise qui a à cœur sa clientèle. Tout a été effectué dans les règles de l'art. »</blockquote><cite><span class="av">ML</span><div>Mat L.<span>Client, Google</span></div></cite></figure>
    <figure class="carte-avis reveal d1"><div class="etoiles">{ETOILES}</div><blockquote>« Service très courtois et efficace. À partir du premier appel pour soumission jusqu'à la fin de l'installation. »</blockquote><cite><span class="av">ML</span><div>Martin Loyer<span>Client, Google</span></div></cite></figure>
    <figure class="carte-avis reveal d2"><div class="etoiles">{ETOILES}</div><blockquote>« Travail très propre. Respect des dates d'échéance. Personnel très courtois et professionnel. Excellente compagnie! »</blockquote><cite><span class="av">KG</span><div>K. Gianna<span>Cliente, Google</span></div></cite></figure>
  </div></div></section>
'''

def faq(p):
    d=''.join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(p['faq']))
    return f'''<section class="fond-beige" id="faq"><div class="wrap faq-zone"><div><span class="eyebrow">Questions fréquentes</span><h2 class="reveal">{p['faq_h2']}</h2>
  <p class="reveal d1" style="margin-top:18px;color:var(--doux);max-width:24em">Une autre question? Appelez-nous au {TELLINK}.</p></div><div>{d}</div></div></section>
'''

def liens(items):
    c=''.join(f'<a class="lie reveal d{i}" href="#"><b>{t}</b><span>{d}</span><i>{ic(ico)}</i></a>' for i,(ico,t,d) in enumerate(items))
    return f'<section><div class="wrap">{tete("À consulter aussi","Nos autres services à Joliette")}<div class="lies">{c}</div></div></section>\n'

def final(p):
    return f'''<div class="final"><div class="wrap"><h2 class="reveal">{p['final_h']}</h2><p class="reveal d1">{p['final_p']}</p>
  <div class="cta reveal d2"><a class="btn btn-b" href="#soumission">{p['cta']} {ARROW}</a></div>
  <a class="grosphone reveal d3" href="tel:+14507539426" data-track="call_tracking">{TEL}</a></div></div>
</main>
'''

def build(p, middle):
    body=hero(p)+faits(p['faits'])+middle+avis()+faq(p)+liens(p['liens'])+final(p)
    open(f"src/{p['key']}.body.html",'w',encoding='utf-8').write(body)
    clean=lambda a: re.sub(r"\s*\[[^\]]*\]","",re.sub(r"<[^>]+>","",a)).strip()
    open(f"src/{p['key']}.faq.json",'w',encoding='utf-8').write(json.dumps([{"q":q,"a":clean(a)} for q,a in p['faq']],ensure_ascii=False))
    return len(body)
