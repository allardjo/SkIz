import base64,re,sys
sys.path.insert(0,'/home/user/SkIz/maquettes')
from typo import typo, add_css
B='/home/user/SkIz/assets/brand/svg/'; I='/home/user/SkIz/maquettes/img/'
def svg(n): return 'data:image/svg+xml;base64,'+base64.b64encode(open(B+n,'rb').read()).decode()
def jpg(n): return 'data:image/jpeg;base64,'+base64.b64encode(open(I+n+'.jpg','rb').read()).decode()
t=open(sys.argv[1],encoding='utf-8').read()
imgs={'HERO':'hero','EQUIPE':'equipe','RESIDENTIEL':'residentiel','COMMERCIAL':'commercial','THERMO':'thermopompe','ENTRETIEN':'entretien','CHAUFFAGE':'chauffage','GUIDE':'guide-thermopompe'}
decl=''
for k,f in imgs.items():
    decl+=f'--img-{k.lower()}:url({jpg(f)});'
    t=t.replace('url({{IMG_%s}})'%k,'var(--img-%s)'%k.lower())
t=t.replace(':root{',':root{'+decl,1)
star='<svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/></svg>'
t=(t.replace('{{SYMBOLE_BEIGE}}',svg('symbole-beige.svg'))
    .replace('{{LOGO_HORIZ_BEIGE}}',svg('logo-enonce-horizontal-beige.svg'))
    .replace('{{LOGO_HORIZ_MARINE}}',svg('logo-enonce-horizontal-marine.svg'))
    .replace('{{LOGO_ENONCE_BEIGE}}',svg('logo-enonce-horizontal-beige.svg'))
    .replace('{{ETOILES}}',star*5).replace('{{ETOILE1}}',star))
t=typo(add_css(t))
left=re.findall(r'\{\{[A-Z_]+\}\}',t)
print('placeholders restants:',left)
open(sys.argv[2],'w',encoding='utf-8').write(t); print(len(t)//1024,'Ko ->',sys.argv[2])
