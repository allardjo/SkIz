"""Génère src/carte-secteurs.html : carte SVG des secteurs desservis.
Données : © contributeurs OpenStreetMap (ODbL), via Nominatim. Voir data/osm-*.json."""
import json,math,os
HERE=os.path.dirname(os.path.abspath(__file__)); D=os.path.join(HERE,'..','data')
W0,E0,S0,N0=-74.6,-72.5,45.52,46.8
K=math.cos(math.radians(46.1))
W=1000; H=round(W*(N0-S0)/((E0-W0)*K))
def pr(lon,lat): return ((lon-W0)*K/((E0-W0)*K)*W,(N0-lat)/(N0-S0)*H)
def dp(pts,t):
    if len(pts)<3: return pts
    a,b=pts[0],pts[-1]; dx,dy=b[0]-a[0],b[1]-a[1]; L=math.hypot(dx,dy) or 1e-9
    m,i=0,0
    for k in range(1,len(pts)-1):
        d=abs(dy*(pts[k][0]-a[0])-dx*(pts[k][1]-a[1]))/L
        if d>m: m,i=d,k
    if m>t: return dp(pts[:i+1],t)[:-1]+dp(pts[i:],t)
    return [a,b]
def path(geo,t):
    polys=[geo['coordinates']] if geo['type']=='Polygon' else geo['coordinates']
    s=''
    for poly in polys:
        for ring in poly:
            p=[pr(*c[:2]) for c in ring]
            if max(x for x,_ in p)<-50 or min(x for x,_ in p)>W+50 or max(y for _,y in p)<-50 or min(y for _,y in p)>H+50: continue
            p=p[:-1] if p[0]==p[-1] else p
            k=max(range(len(p)),key=lambda i:math.hypot(p[i][0]-p[0][0],p[i][1]-p[0][1]))
            p=dp(p[:k+1],t)[:-1]+dp(p[k:]+[p[0]],t)[:-1]
            if len(p)<4: continue
            s+='M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in p)+'Z'
    return s
munis=json.load(open(os.path.join(D,'osm-municipalites.json'),encoding='utf-8'))
mrcs=json.load(open(os.path.join(D,'osm-mrc.json'),encoding='utf-8'))
BG=["Matawinie","Montcalm","Les Moulins","L'Assomption (MRC)","D'Autray","Joliette (MRC)","Maskinongé (MRC)","Mékinac","Les Chenaux","Trois-Rivières","Les Laurentides","Les Pays-d'en-Haut","Thérèse-De Blainville","Mirabel","Laval","Agglomération de Montréal"]
bg=''.join(f'<path d="{path(mrcs[n]["geojson"],1.1)}"/>' for n in BG if n in mrcs)
cov=''.join(f'<path d="{path(g["geojson"],.45)}"><title>{n}</title></path>' for n,g in munis.items())
def c(n):
    g=munis[n]; return pr(float(g['lon']),float(g['lat']))
LAB=[('Joliette',1,'m'),('Saint-Michel-des-Saints',0,'r'),('Louiseville',0,'l'),('Berthierville',0,'r'),('Rawdon',0,'l'),('Repentigny',0,'r'),('Terrebonne',0,'l'),('Montréal-Est',0,'r'),('Saint-Jean-de-Matha',0,'l'),('Lavaltrie',0,'r')]
SEC={'Saint-Jean-de-Matha','Rawdon','Berthierville','Lavaltrie','Repentigny'}
lab=''
for n,big,al in LAB:
    x,y=c(n); dx={'m':0,'l':-18,'r':18}[al]; anc={'m':'middle','l':'end','r':'start'}[al]
    lab+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{9 if big else 6}" class="{'pt pt-j' if big else 'pt'}"/><text x="{x+dx:.1f}" y="{y+(-22 if al=="m" else 9):.1f}" text-anchor="{anc}" class="{'lb-j' if big else 'lb'+(' lb-sec' if n in SEC else '')}">{n}</text>'
ctx=[('Montréal',-73.57,45.57,'r'),('Laval',-73.80,45.67,'m'),('Mont-Tremblant',-74.58,46.12,'r')]
cx=''.join(f'<text x="{pr(a,b)[0]:.1f}" y="{pr(a,b)[1]:.1f}" class="lb-c" text-anchor="{"end" if al=="l" else "start" if al=="r" else "middle"}">{n}</text>' for n,a,b,al in ctx)
svg=f'''<svg class="carte-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="carte-t carte-d" xmlns="http://www.w3.org/2000/svg">
<title id="carte-t">Carte des secteurs desservis par Bédard</title><desc id="carte-d">Les municipalités desservies, entre Joliette, Saint-Michel-des-Saints, Louiseville, Montréal-Est et Terrebonne, apparaissent en bleu foncé; le reste du territoire est en teinte pâle.</desc>
<defs><clipPath id="cadre"><rect width="{W}" height="{H}" rx="0"/></clipPath></defs>
<rect class="eau" width="{W}" height="{H}"/>
<g clip-path="url(#cadre)"><g class="fond">{bg}</g><g class="couvert">{cov}</g>{cx}{lab}</g>
</svg>'''
open(os.path.join(HERE,'carte-secteurs.html'),'w',encoding='utf-8').write(svg)
print(len(svg)//1024,'Ko',W,H)
