import sys
sys.path.insert(0,'src')
from gen_services import *

BTN_SOUM=f'<a class="btn btn-b reveal d2" href="#soumission">Demander une soumission {ARROW}</a>'
SECTEURS="Nous desservons toutes les municipalités de la MRC de Joliette (Joliette, Notre-Dame-des-Prairies, Saint-Charles-Borromée, Crabtree, Saint-Paul, Saint-Thomas, Notre-Dame-de-Lourdes, Saint-Ambroise-de-Kildare, Sainte-Mélanie et Saint-Pierre), ainsi que plusieurs secteurs voisins de Lanaudière."

# ===================== RÉPARATION =====================
P1=dict(key='reparation',hclass='hero-repar',fil='Réparation et dépannage',pastille='Thermopompe et climatiseur · Urgence 24 h',
 h1="Réparation de thermopompe et de climatiseur à <em>Joliette</em>",
 lead="<b>Un appareil en panne? Un diagnostic précis, une réparation claire.</b> Nos techniciens interviennent sur les thermopompes et les climatiseurs, avec un service d'urgence disponible 24 heures sur 24.",
 cta='Demander un dépannage',signes=['Diagnostic précis','Soumission claire avant les travaux','Urgence 24 h'],
 form_h='Dépannage ou réparation',form_sub='Décrivez le problème : un technicien vous rappelle rapidement.',form_label='Problème',
 types=['Ma thermopompe ne chauffe pas','Mon climatiseur ne refroidit pas','Bruit, fuite ou givre',"L'appareil ne démarre pas",'Autre problème / je ne sais pas'],form_btn='Être rappelé',
 faits=[('clock','Urgence 24 h','Une équipe disponible jour et nuit'),('tool','Diagnostic précis','Cause identifiée avant de réparer'),('users','65+ professionnels','Des techniciens qualifiés'),('star','4,9 sur 5','Plus de 180 avis clients')],
 urg_eyebrow='Urgence 24 h',urg_h2="Une panne en plein hiver? On s'en occupe.",
 urg_p="Une thermopompe ou un climatiseur qui lâche au pire moment : appelez-nous, une équipe est disponible 24 heures sur 24.",
 urg_items=[('1. Vous appelez','Un technicien prend votre appel, jour et nuit.'),('2. Nous diagnostiquons','Nous identifions la cause de la panne.'),('3. Nous réparons','Avec votre accord, après une soumission claire.')],
 prix_h2='Combien coûte une réparation de thermopompe?',prix_intro="Le coût dépend de la panne, de la pièce à remplacer et de l'appareil. Nous vous donnons le prix avant d'intervenir.",
 facteurs=[('La nature de la panne','Une pièce simple ou un composant majeur.'),("L'âge et la marque de l'appareil",'Disponibilité des pièces et état général.'),("Le moment de l'intervention",'Heures normales ou urgence 24 h. <em>[frais à valider]</em>'),("L'accès à l'appareil",'Distance, déplacement et accessibilité des unités.')],
 prix_note='<p class="placeholder reveal">[Frais de diagnostic et de déplacement à confirmer avant publication]</p>',
 prix_carte="Un technicien évalue la panne avant d'intervenir. Vous connaissez le coût avant les travaux.",guide_href='#',guide_txt='Guide : remplacer sa thermopompe, à quel prix?',
 faq_h2='Réparation de thermopompe : vos questions',
 faq=[("Faites-vous la réparation de thermopompes et de climatiseurs à Joliette?","Oui, à Joliette et dans la région de Lanaudière. Nos techniciens interviennent sur les thermopompes et les climatiseurs."),
  ("Avez-vous un service d'urgence?",f"Oui, un service d'urgence est offert 24 heures sur 24. Appelez le {TEL}."),
  ("Ma thermopompe ne chauffe plus : que faire?","Vérifiez d'abord que l'appareil est alimenté et que le mode de chauffage est bien réglé, puis appelez-nous : un technicien identifiera la cause. Ne tentez pas de démonter l'appareil."),
  ("Réparer ou remplacer mon appareil?","Cela dépend de l'âge de l'appareil, de la nature de la panne et du coût de la réparation. Nous vous remettons une soumission pour comparer les deux options."),
  ("Réparez-vous les appareils que vous n'avez pas installés?","Nous évaluons chaque demande : appelez-nous avec la marque et le modèle de votre appareil. <em>[À valider : marques réparées]</em>"),
  ("Combien coûte une réparation?","Le coût dépend de la panne, de la pièce à remplacer et de l'appareil. Nous vous donnons le prix avant d'intervenir."),
  ("Faites-vous aussi l'entretien?","Oui, nous offrons un service d'entretien et de nettoyage périodique personnalisé pour thermopompes et climatiseurs."),
  ("Quels secteurs desservez-vous?",SECTEURS)],
 liens=[('refresh','Entretien et nettoyage','Un entretien périodique personnalisé.'),('thermo','Installation de thermopompe','Murale ou centrale, avec soumission détaillée.'),('wind','Thermopompe murale','Aussi appelée climatiseur mural.')],
 final_h='Un appareil en panne? Appelez-nous.',final_p="Un technicien Bédard diagnostique, vous remet une soumission claire et répare. Urgence 24 h.")
mid1=(symptomes('Symptômes courants',"Quel est le problème de votre appareil?","Voici les situations les plus fréquentes. Dans tous les cas, un technicien identifie la cause avant d'intervenir.",
 [('thermo','Ne chauffe pas assez','La thermopompe tourne, mais la maison reste froide.'),('snow','Ne refroidit pas',"Le climatiseur souffle de l'air tiède ou ne rafraîchit plus."),('drop',"Fuite d'eau","De l'eau coule de l'unité intérieure ou extérieure."),('alert','Givre ou glace',"Du givre se forme sur l'unité, surtout par temps froid."),('volume','Bruit inhabituel','Claquement, vibration ou sifflement anormal.'),('power','Démarrages aléatoires',"L'appareil s'allume ou s'éteint de lui-même, ou ne démarre plus.")])
 + urgence(P1)
 + duo('Réparer ou remplacer?','Faut-il réparer ou remplacer votre appareil?',"Nous vous disons franchement ce qui est le plus avantageux pour vous.",
   dict(etiq='Réparation',h3='Quand une réparation suffit',p="Si l'appareil est relativement récent et que la panne est bien ciblée, une réparation est souvent la meilleure option.",ul=['Panne ciblée et appareil en bon état','Pièce disponible','Coût de réparation raisonnable'],pour_t='Notre approche :',pour="nous vous disons franchement si la réparation vaut la peine."),
   dict(etiq='Remplacement',h3='Quand il vaut mieux remplacer',p="Si l'appareil est âgé, tombe souvent en panne ou n'est plus efficace, le remplacement coûte souvent moins cher à long terme.",ul=['Pannes répétées',"Appareil ancien ou peu efficace","Réparation presque aussi chère qu'un appareil neuf"],pour_t='Bon à savoir :',pour="nous vous remettons une soumission pour comparer les deux options."))
 + etapes('Déroulement','Comment se passe une réparation',[('Vous appelez',"Vous décrivez le problème et l'appareil concerné."),('Diagnostic','Un technicien se déplace et identifie la cause.'),('Soumission claire','Vous connaissez le coût avant les travaux.'),('Réparation et suivi','Nous réparons et vérifions le fonctionnement.')])
 + prix(P1))
build(P1,mid1)

# ===================== ENTRETIEN =====================
P2=dict(key='entretien',hclass='hero-entretien',fil='Entretien et nettoyage',pastille='Thermopompe et climatiseur · Joliette',
 h1="Nettoyage et entretien de thermopompe et de climatiseur à <em>Joliette</em>",
 lead="<b>Un appareil bien entretenu dure plus longtemps et performe mieux.</b> Nos techniciens nettoient les thermopompes murales et entretiennent les climatiseurs, avec un service périodique et personnalisé.",
 cta='Demander un entretien',signes=['Service périodique personnalisé','Thermopompes murales et climatiseurs','Techniciens qualifiés'],
 form_h='Entretien ou nettoyage',form_sub='Dites-nous ce qu\'il vous faut : on vous rappelle rapidement.',form_label="Type d'entretien",
 types=['Nettoyage de thermopompe murale','Entretien de climatiseur','Entretien périodique (programme)','Je ne sais pas encore'],form_btn='Être rappelé',
 faits=[('refresh','Périodique et personnalisé','Un programme adapté à vos appareils'),('tool','Techniciens qualifiés','Plus de 65 professionnels chez Bédard'),('clock','Urgence 24 h','En cas de panne entre deux entretiens'),('star','4,9 sur 5','Plus de 180 avis clients')],
 urg_eyebrow='Entretien périodique',urg_h2='Un entretien qui se planifie tout seul',
 urg_p="Avec un programme d'entretien périodique personnalisé, nous planifions les visites pour vous : votre appareil reste performant, sans que vous y pensiez.",
 urg_btn=BTN_SOUM,
 urg_items=[('Calendrier de visites','Nous planifions le bon moment pour chaque appareil. <em>[à valider]</em>'),("Rapport d'intervention",'Vous savez ce qui a été fait. <em>[à valider]</em>'),('Priorité en cas de panne','Une équipe disponible 24 heures sur 24.')],
 prix_h2='Combien coûte un nettoyage de thermopompe?',prix_intro="Le coût dépend du nombre d'appareils et de leur état. Nous vous le précisons avant d'intervenir.",
 facteurs=[("Le nombre d'appareils",'Une seule unité ou plusieurs unités intérieures.'),("Le type d'appareil",'Thermopompe murale ou climatiseur.'),("L'état de l'appareil",'Date du dernier entretien et niveau d\'encrassement.'),('La fréquence',"Une visite ponctuelle ou un programme périodique.")],
 prix_note='<p class="placeholder reveal">[Tarifs ou forfaits à confirmer avant publication]</p>',
 prix_carte="Nous vous précisons le coût de l'entretien avant d'intervenir, pour un appareil ou pour tout votre parc.",guide_href='#',guide_txt='Besoin de filtres? Voir la boutique',
 faq_h2='Entretien et nettoyage : vos questions',
 faq=[("À quelle fréquence faut-il nettoyer une thermopompe?","Cela dépend de l'appareil et de l'usage. Nous recommandons un entretien périodique personnalisé. <em>[À valider : fréquence recommandée]</em>"),
  ("Puis-je nettoyer les filtres moi-même?","Oui, le nettoyage des filtres est généralement à la portée du propriétaire : consultez le manuel de votre appareil. Pour un nettoyage complet, faites appel à un technicien."),
  ("Que comprend le nettoyage d'une thermopompe murale?","Nos techniciens assurent le nettoyage de la thermopompe murale pour prolonger sa longévité et ses performances. <em>[Liste détaillée des étapes à valider]</em>"),
  ("Nettoyez-vous aussi les échangeurs d'air et les conduits?","Oui. Nous nettoyons les systèmes de ventilation, les unités murales, les échangeurs d'air et les conduits."),
  ("Où trouver des filtres?","Consultez notre boutique en ligne. <em>[À valider : filtres offerts]</em>"),
  ("Avez-vous un service d'urgence?",f"Oui, un service d'urgence est offert 24 heures sur 24. Appelez le {TEL}."),
  ("Quels secteurs desservez-vous?",SECTEURS)],
 liens=[('tool','Réparation et dépannage','Thermopompe, climatiseur. Urgence 24 h.'),('thermo','Installation de thermopompe','Murale ou centrale.'),('wind','Échangeurs d\'air','Choix, installation et entretien.')],
 final_h='Un appareil propre, un confort durable.',final_p="Planifiez votre entretien avec un technicien Bédard : thermopompe, climatiseur, échangeur d'air.")
mid2=(symptomes('Pourquoi entretenir','Les bénéfices d\'un entretien régulier',"Un entretien périodique garde votre appareil performant et vous évite des surprises.",
 [('thermo','Une meilleure performance',"Un appareil propre chauffe et refroidit plus efficacement."),('refresh','Une durée de vie prolongée',"Un entretien régulier prolonge la longévité de l'appareil."),('wind','Moins de poussière','Filtres et unités propres : moins de poussière et de mauvaises odeurs dans la maison.'),('alert','Moins de pannes','Un entretien régulier aide à repérer les problèmes avant la panne.'),('drop','Un drainage qui fonctionne','Drainage et filtres vérifiés pour éviter fuites et humidité.'),('tool','Une garantie respectée',"Un entretien régulier peut être exigé par le fabricant. <em>[à valider]</em>")])
 + duo('Ce que comprend l\'entretien','Thermopompe murale ou climatiseur',"Deux services, un même objectif : un appareil performant, plus longtemps.",
   dict(etiq='Thermopompe murale',h3='Nettoyage de thermopompe',p="Un nettoyage périodique et personnalisé de votre thermopompe murale, pour prolonger sa longévité et ses performances.",ul=["Nettoyage de l'unité intérieure","Vérification de l'unité extérieure",'Contrôle du fonctionnement'],pour_t='Fréquence :',pour="<em>[à valider : fréquence recommandée]</em>"),
   dict(etiq='Climatiseur',h3="Entretien d'air climatisé",p="Un entretien régulier de votre climatiseur pour qu'il soit prêt quand la chaleur arrive.",ul=['Nettoyage et vérification','Contrôle du drainage','Remise en route avant la saison chaude'],pour_t='Idéal :',pour="au printemps, avant les premières chaleurs. <em>[à valider]</em>"))
 + urgence(P2)
 + etapes('Déroulement','Comment se passe un entretien',[('Vous appelez','Vous décrivez vos appareils et vos besoins.'),('Évaluation','Nous évaluons vos appareils et leur état.'),('Nettoyage et entretien','Un technicien qualifié intervient.'),('Suivi','Nous planifions la prochaine visite.')])
 + prix(P2))
build(P2,mid2)

# ===================== CHAUFFAGE AUXILIAIRE =====================
P3=dict(key='chauffage',hclass='hero-chauff',parent='Résidentiel',fil="Chauffage d'appoint",pastille='Thermopompe et grands froids · Joliette',
 h1="Chauffage auxiliaire à <em>Joliette</em>",
 lead="<b>Gardez la maison confortable, même par grand froid.</b> Un chauffage auxiliaire prend le relais de votre thermopompe quand les températures chutent. Nous évaluons votre maison et recommandons la bonne combinaison.",
 cta="Demander une évaluation",signes=['Évaluation de votre maison','Combinaison adaptée','Soumission détaillée'],
 form_h='Évaluation de votre chauffage',form_sub='Un spécialiste vous rappelle rapidement.',form_label='Votre situation',
 types=["J'ai une thermopompe et je veux un appoint",'Je veux ajouter une thermopompe à ma fournaise','Je remplace mon chauffage','Je ne sais pas encore (conseillez-moi)'],form_btn='Être rappelé',
 faits=[('thermo','Par grand froid','Un relais quand le rendement baisse'),('tool','Évaluation de la maison','Avant toute recommandation'),('flame','Fournaises électriques','Vente et installation chez Bédard'),('star','4,9 sur 5','Plus de 180 avis clients')],
 urg_eyebrow='Notre évaluation',urg_h2='Ce que nous évaluons chez vous',
 urg_p="Chaque maison réagit différemment au froid. Avant de recommander, nous regardons ce qui compte.",urg_btn=BTN_SOUM,
 urg_items=[('Votre chauffage actuel','Fournaise, plinthes, chaudière : ce qui est déjà en place.'),("L'isolation et les conduits","L'état de l'enveloppe et du réseau de distribution."),('Vos besoins et votre budget','Le confort visé et ce que vous souhaitez investir.')],
 prix_h2='Combien coûte un chauffage auxiliaire?',prix_intro="Le prix dépend du système choisi et de votre maison. Voici ce qui le fait varier.",
 facteurs=[("Le type d'appoint",'Fournaise électrique ou autre système en complément.'),("L'état des conduits",'Conduits existants ou à adapter.'),('Le panneau électrique',"Capacité et travaux électriques à prévoir."),('La taille de la maison','Superficie, isolation et nombre de zones.')],
 prix_note='<p class="placeholder reveal">[Fourchettes de prix à valider avant publication]</p>',
 prix_carte="Nous évaluons votre maison avant de vous donner un prix. Vous savez exactement ce qui est inclus.",guide_href='#',guide_txt="Voir les fournaises électriques",
 faq_h2='Chauffage auxiliaire : vos questions',
 faq=[("Qu'est-ce qu'un chauffage auxiliaire?","C'est un système de chauffage qui prend le relais de la thermopompe quand les températures chutent et que son rendement baisse."),
  ("Une thermopompe peut-elle chauffer seule au Québec?","Selon le modèle et la maison, elle peut assurer une grande partie du chauffage : certains modèles conservent un COP de 2,38 à -8,3 °C. Pour les très grands froids, un chauffage d'appoint assure le confort. Nous évaluons votre situation avant de recommander."),
  ("Ai-je besoin d'un chauffage auxiliaire?","Cela dépend de votre maison, de son isolation, de la thermopompe choisie et du confort souhaité. Nous évaluons avant de recommander."),
  ("Quelle est la différence entre un système bi-énergie et un appoint existant?","Un système bi-énergie jumelle la thermopompe à une fournaise qui prend le relais par grand froid. Dans une maison déjà équipée d'un chauffage, celui-ci peut simplement servir d'appoint. <em>[À valider avec le conseiller]</em>"),
  ("Offrez-vous des fournaises électriques?","Oui, nous vendons et installons des fournaises électriques. <em>[Lien vers la page des fournaises à ajouter]</em>"),
  ("Existe-t-il des subventions?","Des programmes d'aide peuvent exister. Nous vous indiquons ceux qui s'appliquent à votre projet. <em>[À valider avant publication]</em>"),
  ("Quels secteurs desservez-vous?",SECTEURS)],
 liens=[('thermo','Installation de thermopompe','Murale ou centrale, avec soumission détaillée.'),('tool','Réparation et dépannage','Urgence 24 h pour votre chauffage.'),('refresh','Entretien et nettoyage','Un entretien périodique personnalisé.'),('flame','Fournaises électriques','Vente et installation.')],
 final_h='Un confort constant, même par -20 °C.',final_p="Parlez à un spécialiste Bédard : évaluation de votre maison et soumission détaillée.")
P3['final_h']='Un confort constant, même en plein hiver.'
cop=f'''<section><div class="wrap">{tete('Pourquoi un appoint',"Pourquoi un chauffage d'appoint?","Une thermopompe performe moins quand il fait très froid, et c'est normal. Voici ce que montrent certains de nos modèles.")}
  <div class="cop">
    <div class="cop-carte reveal"><span class="temp">À 8,3 °C (47 °F)</span><div class="gros">4,95</div><p>COP de certains modèles : près de 5 kWh de chaleur produite pour 1 kWh d'électricité consommé.</p></div>
    <div class="cop-carte cop-froid reveal d1"><span class="temp">À -8,3 °C (17 °F)</span><div class="gros">2,38</div><p>Le rendement baisse par grand froid, mais il reste plus de deux fois supérieur à celui d'un chauffage électrique ordinaire (COP de 1).</p></div>
  </div>
  <p class="reveal" style="margin-top:1.6rem;color:var(--doux);max-width:46em">Le chauffage auxiliaire entre en jeu quand la thermopompe ne suffit plus à elle seule : il garantit un confort constant, sans surprise sur la facture.</p>
</div></section>
'''
mid3=(cop
 + duo('Les options',"Deux types de chauffage auxiliaire","Le chauffage auxiliaire prend le relais de votre thermopompe par grand froid. La bonne solution dépend de votre maison et de votre chauffage actuel.",
   dict(etiq='Fournaise électrique',h3='Une fournaise qui prend le relais',p="Jumelée à une thermopompe centrale, la fournaise électrique prend le relais quand il fait très froid : c'est le système bi-énergie.",ul=['Confort constant toute la saison',"Appoint intégré au système central",'Fournaises électriques offertes chez Bédard'],pour_t='Idéal pour :',pour="une maison munie de conduits. <em>[à valider]</em>"),
   dict(etiq='Chauffage existant',h3='Garder votre chauffage actuel en appoint',p="Votre chauffage actuel reste en place et prend le relais de la thermopompe quand le froid s'intensifie. <em>[types de chauffage à valider]</em>",ul=['Aucun nouvel équipement de chauffage à acheter','Moins de travail à l\'installation',"Le chauffage actuel sert d'appoint"],pour_t='Idéal pour :',pour="une maison déjà équipée d'un chauffage fonctionnel. <em>[à valider]</em>"))
 + urgence(P3)
 + etapes('Déroulement','Comment se déroule votre projet',[('Évaluation','Nous évaluons votre maison et votre chauffage actuel.'),('Recommandation','Nous vous proposons la bonne combinaison.'),('Installation','Une équipe qualifiée installe le système.'),('Mise en service','Nous vérifions le fonctionnement et vous expliquons les réglages.')])
 + prix(P3))
build(P3,mid3)
print('ok')
