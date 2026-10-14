# Arborescence cible et plan de redirections

Table complète, une ligne par URL : `data/redirections-et-arborescence.csv` (81 URL : les 77 du sitemap, 3 anciennes adresses vues par Google et le nouvel article du 2026-10-12). Elle contient les clics et impressions de 16 mois, les liens externes, la décision, l'adresse cible et la priorité.

## Principe : ne rien déplacer sans raison
Aucune adresse qui rapporte du trafic ou des liens ne change. La refonte change le design, le contenu et le menu, pas les URL. Résultat :
- 58 URL gardées telles quelles, plus 11 fiches de filtres gardées en attendant une décision.
- 4 pages techniques traitées par `noindex` et sitemap (panier, commande, compte, page 404 personnalisée) et la boutique `/shop/` clarifiée.
- Seulement **7 redirections 301**, toutes simples :
  - 3 anciennes variantes d'articles qui répondent en 404 vers l'article actuel ;
  - 4 pages anglaises WPML (`/en/...`) vers leur équivalent français.
- 20 URL de priorité P1 (page d'accueil, articles « prix », page pilier, services, contact, soumission, avis, carrières, catégories qui ont des liens), à tester en premier au lancement.

Règles d'infrastructure à appliquer à la migration :
1. `http://` et `www.` vers `https://cbedard.com/` **en un seul saut** (aujourd'hui, deux sauts pour certains liens).
2. `/index.php` vers `/`.
3. Un canonical propre sur chaque page ; `/commande/` ne doit plus pointer vers `/panier/` sans raison.
4. Les pages techniques et la 404 ne sont ni dans le sitemap ni indexées.
5. Les paramètres comme `?gQT=` ne créent pas de pages indexables.

## Arborescence cible

```
/                                         Accueil (garder)
├── /residentiel/                         NOUVEAU : hub résidentiel
│   ├── /climatiseur-mural-air-climatise-thermopompe-joliette/   PILIER (garder l'URL)
│   ├── /produits/chauffage/              (garder) + thermopompes-murales, thermopompes-centrales, fournaises-electriques
│   ├── /produits/climatisation-lanaudiere/   (garder) + climatiseur-mural, climatiseur-central
│   ├── /produits/qualite-de-lair/        (garder) + échangeurs d'air, humidificateurs, purificateurs
│   ├── /produits/geothermie/             (garder)
│   └── /produits/planchers-radiants/     (garder)
├── /commercial/                          NOUVEAU : hub commercial
│   ├── /commercial/refrigeration-commerciale/      NOUVEAU
│   ├── /commercial/ventilation-commerciale-joliette/   NOUVEAU (2 943 impressions)
│   └── /commercial/ferblanterie/         NOUVEAU
├── /services/                            Hub des services (garder l'URL)
│   ├── /services/installation-thermopompe-joliette/   NOUVEAU (14 379 impressions)
│   ├── /services/reparation-thermopompe-climatiseur-joliette/   NOUVEAU (7 491 + 1 166)
│   ├── /services/entretien-nettoyage-thermopompe-climatiseur-joliette/   NOUVEAU (2 733 + 2 688)
│   └── /services/chauffage-auxiliaire-joliette/   NOUVEAU (2 970)
├── /blogue/                              (garder) 7 articles, URL inchangées, à rafraîchir
├── /avis/  /carrieres/  /soumission/  /contact-climatisation-joliette/   (garder)
├── /boutique-web/                        (garder) + 39 fiches /produit/... et /shop/ (archive)
└── pages légales, panier, commande, compte  (noindex, hors sitemap)
```
Les chiffres d'impressions sont ceux de 16 mois de Search Console pour les requêtes visées.

À évaluer plus tard (risque de concurrence entre pages) : une page « installation de climatiseur à Joliette » séparée (2 436 impressions) ou une section dans la page pilier. Tant qu'on n'a pas vu la page pilier se repositionner, on la traite dans la page pilier.
Pages par ville (Repentigny, etc.) : seulement quand la liste des secteurs desservis sera confirmée.

## Menu proposé (de 20 liens à 6)
1. Résidentiel (menu déroulant : thermopompes, climatiseurs muraux, chauffage, ventilation et air, géothermie et planchers radiants)
2. Commercial (réfrigération, ventilation, ferblanterie)
3. Services (installation, réparation 24 h, entretien)
4. Guides de prix
5. Avis
6. Carrières
À droite : téléphone cliquable et bouton « Demander une soumission ». Le pied de page reprend les liens détaillés. La page « Conditions d'utilisation » sort du menu principal (elle recevait autant de poids interne que les services).

## Maillage interne à ajouter
- Chaque guide de prix pointe vers sa page de service et vers la soumission (aujourd'hui, aucun lien dans le contenu).
- Chaque page de service pointe vers sa catégorie de produits, son guide, la FAQ et le formulaire.
- La page pilier et l'accueil reçoivent des liens contextuels depuis les articles et les services.

## Mise en œuvre sur WordPress
- Le plugin **Redirection** est déjà installé sur le site : on y entre les 7 redirections. Les règles `http` / `www` / `index.php` se mettent au niveau du serveur (`.htaccess`, LiteSpeed).
- Les nouvelles pages sont créées sur le site de préproduction, non indexé.

## Protocole de test (avant et après le lancement)
1. Avant : exporter l'état de référence (déjà dans `data/` et `docs/inventaire-urls.csv`).
2. Sur la préproduction : parcourir les 81 anciennes adresses ; chacune doit répondre 200 (même URL) ou 301 en un saut vers l'adresse cible du tableau.
3. Tester les 20 pages P1 une par une : titre, description, H1, canonical, données structurées, formulaire, suivi des appels et des soumissions.
4. Après le lancement : refaire le parcours le jour même, puis à 7, 30 et 90 jours ; surveiller Search Console (couverture, erreurs 404, positions des requêtes « Joliette »).

## Observation à noter
Un nouvel article, « Échangeur d'air au Québec : utilisation et entretien », a été publié le 2026-10-12 (absent des données Search Console). Quelqu'un publie donc du contenu en ce moment. À savoir qui, pour coordonner avec la refonte.

## Page de service modèle : `maquettes/service-installation-thermopompe.html`
Gabarit des pages de services locales (même design que l'accueil, adapté aux grands écrans, mobile validé). Sources : `maquettes/src/` et `maquettes/build_service.py`.

Contenu et SEO :
- Adresse cible : `/services/installation-thermopompe-joliette/` ; titre de 47 caractères, description de 149 caractères, un seul H1 (« Installation de thermopompe à Joliette »), canonical, fil d'Ariane.
- Données structurées : `Service` (rattaché à l'entreprise locale), `BreadcrumbList`, `FAQPage` (4 réponses validées).
- Structure : héros avec formulaire de soumission, bande de points forts, comparatif murale / centrale, déroulement en 4 étapes, facteurs de prix (sans chiffres inventés), bloc subventions, avis, FAQ, liens vers les services voisins, appel final.
- Liens internes prévus : catégories thermopompes murales / centrales, guide « Remplacer une thermopompe : à quel prix? », réparation, entretien, chauffage auxiliaire, climatiseur mural.
- Typographie française (espaces insécables, téléphones sur une ligne) appliquée aux deux maquettes (`maquettes/typo.py`).

À confirmer avant publication (marqué dans la page) : fourchettes de prix, programmes d'aide, durée d'installation, note et nombre d'avis.
Chaque autre page de service reprend ce gabarit : réparation, entretien et nettoyage, chauffage auxiliaire, ventilation commerciale, réfrigération commerciale, ferblanterie.

## Page pilier : `maquettes/pilier-climatiseur-mural-thermopompe.html`
Refonte de la page qui a 10 liens externes et 64 000 impressions, **à la même adresse** : `/climatiseur-mural-air-climatise-thermopompe-joliette/` (appelée « À propos » dans le menu actuel). Sources : `maquettes/src/pilier-climatiseur-thermopompe.body.html`, `maquettes/build_pilier.py`.

Ce que la page actuelle disait (et que la refonte conserve) : titre générique « Votre entreprise de chauffage, ventilation et climatisation », H1 « L'entreprise de chauffage, ventilation et climatisation par excellence », 886 mots, et surtout l'histoire de l'entreprise. La refonte garde les mots-clés (chauffage, ventilation, climatisation, climatiseur mural, thermopompe, air climatisé) et reprend l'histoire sous forme de frise.

Nouveau positionnement SEO :
- Titre : « Climatiseur mural et thermopompe à Joliette | Bédard » (52 caractères). H1 : « Climatiseur mural et thermopompe à Joliette ».
- Requêtes visées : climatiseur mural Joliette, air climatisé Joliette, thermopompe Joliette, installation de climatiseur Joliette.
- Structure : héros avec formulaire, faits (depuis 1983, 65+ professionnels, urgence 24 h, 4,9/5), climatiseur mural contre thermopompe (cartes et tableau comparatif), installation à Joliette, gamme de produits (liens vers les 4 catégories), histoire de l'entreprise, prix, avis, FAQ (6 questions), services liés.
- Données structurées : `Service`, `BreadcrumbList`, `FAQPage` (4 réponses validées).

Faits tirés de la page actuelle (à confirmer, parce que le site actuel peut être dépassé) : 1983 concessionnaire exclusif Carrier pour Lanaudière ; 2005 recommandée par CAA habitation (cote de satisfaction supérieure à 95 %) ; 2006 acquisition de Service de chauffage Harnois ; 2009 concessionnaire agréé Mitsubishi ; 2010-2011 Solution Ventech (nettoyage de ventilation, unités murales, échangeurs d'air, conduits de sécheuse) ; 2012 déménagement au 304, boulevard de l'Industrie et acquisition de Ventilation Fabro (ventilation commerciale et institutionnelle).
Contradiction à régler : la page actuelle parle de « 35 ans d'expérience », l'accueil de « plus de 40 ans », et la frise part de 1983 (43 ans en 2026). Choisir un seul énoncé, vérifiable, partout.
Attention au référencement : changer le titre et le H1 d'une page qui se classe peut bouger ses positions. La page conserve son adresse, ses mots-clés et son contenu historique ; on surveille ses positions pendant 90 jours après le lancement.

## Article phare : `maquettes/article-prix-climatiseur-mural.html`
Refonte de « Air climatisé mural : à quel prix s'attendre? » (`/air-climatise-mural-a-quel-prix-sattendre/`, 1 340 clics, 28 % du trafic, 144 731 impressions, position moyenne 10,2), **même adresse**. Sources : `maquettes/src/article-prix-climatiseur-mural.body.html`, `maquettes/build_article.py`.

Ce que l'article actuel contient et que la refonte garde : les facteurs du prix (installation, puissance en BTU de 9 000 à 36 000, niveau sonore, efficacité SEER et Energy Star, options, saison d'achat) et les prix de 2022 (moyenne de 3 500 $ avant taxes, installation incluse ; de 2 500 $ à 4 200 $). Il se classe déjà entre les positions 4 et 5 sur « air climatisé mural prix », « prix air climatisé mural » et « climatiseur mural prix avec installation » : on conserve ces mots-clés dans le titre, le H1 et les sous-titres.

Ce qui s'ajoute : réponse courte en haut de page (« En bref »), tableau par situation (une pièce, deux zones, multizone), comparatif climatiseur mural et thermopompe murale, liste de ce que doit contenir une bonne soumission, section « installation à Joliette », FAQ de 6 questions, sommaire fixe, formulaire de soumission dans la colonne latérale, appels à l'action au milieu et à la fin, bloc auteur, liens vers la page pilier et les services. Environ 1 060 mots dans la nouvelle version (l'ancienne page comptait 1 035 mots, menus et pied de page compris : le corps de l'article était nettement plus court). Données structurées : `Article` (publié le 2022-05-31), `BreadcrumbList`, `FAQPage`.

Requêtes ciblées (Search Console) : air climatisé mural prix (6 547 impressions), climatiseur mural prix (3 530), climatiseur mural prix avec installation (3 341), installation climatiseur joliette (2 436), installation climatiseur mural (1 986), prix air climatisé mural (1 677), prix climatiseur mural (1 489), air climatisé mural 12 000 BTU prix (environ 1 600), combien coûte un climatiseur mural (761).

**À fournir avant publication (bloquant)** :
1. Les prix 2026 par situation (une pièce, deux zones, multizone, et 12 000 BTU). Les chiffres de 2022 sont affichés tels quels et marqués [à mettre à jour]. Un guide de prix avec des prix périmés nuit à la confiance et au référencement.
2. La cote SEER typique des modèles vendus aujourd'hui.
3. Le nom et le titre du conseiller qui valide l'article (signature, crédibilité).
4. La date de mise à jour à afficher (la date de publication d'origine, 2022-05-31, est conservée dans les données structurées).
Risque : l'article génère 28 % des clics. Publier la version rafraîchie à la même adresse, avec le même sujet, et surveiller la page 90 jours.

## Page Carrières (maquette)

Fichier : `maquettes/carrieres.html` (source : `maquettes/src/carrieres.body.html`, `carrieres-extra.css`, `build_carrieres.py`). URL conservée : `/carrieres/` (CTR de 13 %, liens depuis jobcqc.ca).

- Contenu repris de la page actuelle (valeurs, vision, mission, 4 postes, salaire du magasinier, exigences, avantages). Rien d'inventé, sauf les éléments marqués ci-dessous.
- Structure : héros avec liste des postes ouverts, 4 faits, culture et valeurs, avantages (fond marine), 4 postes en accordéon avec bouton « Postuler à ce poste » qui présélectionne le poste dans le formulaire, déroulement en 3 étapes, formulaire de candidature (CV, lettre), appel final.
- SEO : title de 59 caractères (« Emplois en CVAC à Joliette et Lanaudière | Carrières Bédard »), description de 143 caractères, canonical, JSON-LD `JobPosting` pour chaque poste + fil d'Ariane.
- Titre actuel du site : « Emplois en CVAC à Joliette — C.Bédard » (le mot-clé « emplois CVAC Joliette » est conservé).

À valider avant publication :
1. `datePosted` des 4 JobPosting est fixée au 2026-10-13 par défaut : mettre la vraie date de chaque annonce, et retirer un poste dès qu'il est comblé (sinon Google peut ignorer ou pénaliser le balisage).
2. Les 4 postes sont-ils tous encore ouverts? (compte affiché : « 4 postes ouverts »).
3. Étape « On vous rappelle » : délai de réponse à confirmer par les RH.
4. Avantages du magasinier (assurance, retraite) : confirmer; le dessinateur n'a pas de régime de retraite listé.
5. Mention de protection des renseignements (Loi 25) du formulaire.
6. Le formulaire doit envoyer à info@cbedard.com ou à une adresse RH, avec suivi GTM (événement `form_submit`, distinct des soumissions clients).
7. Image du héros : photo de la bibliothèque du site, licence à confirmer; idéalement remplacer par une vraie photo d'équipe.

## Pages Contact et Soumission (maquettes)

Fichiers : `maquettes/contact-climatisation-joliette.html` et `maquettes/soumission.html` (sources : `src/contact.body.html`, `src/soumission.body.html`, `src/contact-extra.css`, générées par `src/gen_contact.py`, assemblées par `build_contact.py`). URL conservées : `/contact-climatisation-joliette/` et `/soumission/`.

**Contact** : 4 cartes (téléphone, urgence 24 h, sans frais, courriel), mini-formulaire, adresse, heures, itinéraire, carte Google, réseaux, lien vers l'avis Google, texte local réécrit (« plus de 40 ans » à la place de « plus de 30 ans » sur le site actuel) et liste de municipalités. JSON-LD : ContactPage + LocalBusiness/HVACBusiness (adresse, heures, deux numéros) + fil d'Ariane.

**Soumission** : formulaire en 3 étapes qui reprend tous les champs du formulaire actuel (client existant ou non, ville, produit, construction, remplacement, provenance, commentaires, photos) :
1. Projet : produit (cartes cliquables) et ville.
2. Coordonnées : nom, téléphone, courriel. Lien « envoyer maintenant » pour ne pas perdre un prospect pressé.
3. Détails facultatifs : construction, remplacement, provenance, commentaires, photos ou plans.
Les champs obligatoires passent de 6 (formulaire actuel) à 5, et seuls produit, ville, nom, téléphone et courriel bloquent l'envoi. Message de remerciement avec poussée `form_submit` dans le dataLayer (démo).

À faire à l'implémentation :
1. Remplacer le formulaire par un Contact Form 7 (ou Elementor) équivalent en gardant les noms de champs actuels (`your-produit`, `your-ville`, etc.) pour ne pas casser les automatisations en aval (monday.com, courriels).
2. Conserver les événements GTM `form_submit` et `call_tracking` et la conversion Google Ads : les liens `tel:` portent `data-track="call_tracking"` dans la maquette comme repère.
3. Enregistrer aussi la demande partielle à l'étape 2 (nom + téléphone) pour ne pas perdre les abandons : à valider avec l'équipe des ventes.
4. Valider : municipalités desservies, délai de rappel, mention Loi 25, URL Facebook et LinkedIn, lien direct d'avis Google, textes d'avis (reprise de la page de service).
5. Carte Google : prévoir un chargement après consentement (Loi 25).

## Validations faites avec le client (13 octobre 2026)

| Point | Décision |
|---|---|
| Délai de rappel (soumission et contact) | Sous 24 heures ouvrables. Appliqué aux pages Contact et Soumission. |
| Municipalités desservies | Les 10 municipalités de la MRC de Joliette (Crabtree, Joliette, Notre-Dame-de-Lourdes, Notre-Dame-des-Prairies, Saint-Ambroise-de-Kildare, Saint-Charles-Borromée, Sainte-Mélanie, Saint-Paul, Saint-Pierre, Saint-Thomas) + Lavaltrie, Berthierville, Saint-Félix-de-Valois, Saint-Jean-de-Matha, Rawdon, Repentigny. La liste de la MRC vient de sources de 2001 et 2011 : à confirmer sur le site de la MRC de Joliette. |
| Postes ouverts (Carrières) | Ferblantier, frigoriste, magasinier. Le poste de dessinateur en ventilation est retiré de la maquette (compté « 3 postes ouverts », 3 JobPosting). |
| Adresse des candidatures | info@cbedard.com |
| Facebook, LinkedIn, avis Google | Liens repris du site actuel : facebook.com/climatisationbedard, linkedin.com/company/climatisation-claude-bedard, g.page/r/Ceb7Vf7wbTIAEB0/review. |
| Mention de confidentialité (Loi 25) | Texte court sous chaque formulaire, avec lien vers une politique de confidentialité qui reste à publier. |

Encore ouvert :
1. Prix 2026 (ventes) pour l'article phare, SEER typique, nom du conseiller, date de mise à jour.
2. `datePosted` réelles des 3 JobPosting. Le poste « dessinateur » reste visible sur le site actuel tant que la page n'est pas remplacée : à retirer au lancement.
3. Page « politique de confidentialité » à rédiger et publier (nom du responsable de la protection des renseignements personnels requis par la Loi 25).
4. Chiffres « 4,9 sur 5 » et « plus de 180 avis » à comparer avec la fiche Google.
5. Techniques : noms de champs CF7, tracking GTM, enregistrement de la demande partielle à l'étape 2.

## Prix 2026 reçus des ventes (13 octobre 2026)

- Climatiseur mural, 1 pièce, 1 appareil : **3 500 $ à 5 300 $ avant taxes, installation comprise**. Publié dans la boîte « En bref », la ligne « Une pièce » du tableau, la FAQ et le balisage FAQPage de l'article.
- Les anciens prix de 2022 (2 500 $ à 4 200 $, moyenne 3 500 $) sont retirés.
- Encore à obtenir : prix « multizone » (ligne du tableau; prévoir par exemple le prix pour 2 unités et pour chaque unité supplémentaire), SEER typique, nom du conseiller. La mention « mis à jour en octobre 2026 » est inscrite.
- Remarque : la fourchette est large (écart de 1 800 $). L'article explique déjà les facteurs (puissance, bruit, efficacité, options). Reformuler pour 2 zones et multizone dès que les ventes répondent.

## Vocabulaire : « simple zone » plutôt que « une pièce » (13 octobre 2026)

Une unité murale simple zone peut couvrir un plein pied complet avec plusieurs pièces. Le vocabulaire est donc par zone, pas par pièce :
- Article « prix » : « climatiseur mural simple zone (une unité intérieure) » dans « En bref », la FAQ et le balisage; tableau en deux lignes : « Simple zone » et « Multizone » (1 unité extérieure, 2 unités intérieures ou plus). Pas de ligne « Deux zones » : un système à deux unités intérieures est déjà un multizone.
- Page pilier : puce « Une unité simple zone peut couvrir un plein pied complet, selon l'aménagement », tableau comparatif (« une zone ou un étage complet ») et réponse de la FAQ « Peut-on climatiser plusieurs pièces avec un seul climatiseur mural? » réécrite (« Oui, dans bien des cas… »).
- À faire valider par un conseiller : la limite de couverture d'une unité simple zone (superficie, circulation de l'air, chambres fermées) avant publication de la FAQ.

Correction (13 octobre 2026) : le client précise qu'il n'y a que des systèmes simple zone et multizone. La ligne « Deux zones » est retirée de l'article, la page pilier parle de « système multizone ».

## SEER et conseiller (13 octobre 2026)

- SEER : « les appareils muraux que nous proposons aujourd'hui affichent une cote SEER de 17 à 28 » (remplace « 13 ou 14 » de l'ancien guide).
- Conseiller : Jonathan Allard, conseiller. Bloc auteur de l'article (« Guide rédigé par l'équipe Bédard et validé par Jonathan Allard, conseiller ») et balisage Article (author Person, jobTitle « Conseiller »). Titre exact à confirmer s'il diffère de « Conseiller ».
- FAQ « secteurs » de l'article et de la page pilier : liste des municipalités (MRC de Joliette + secteurs voisins) inscrite.
- Restent à confirmer : prix multizone, format 12 000 BTU « très courant pour une zone moyenne », vérification de la liste de la MRC sur le site de la MRC.

## Efficacité : SEER, HSPF et COP (13 octobre 2026)

Le conseiller précise qu'au Québec le HSPF (performance en chauffage) et le COP (coefficient de performance) comptent davantage que le SEER seul, car ils indiquent la performance en chauffage. L'article « prix » :
- section 4 devient « L'efficacité énergétique : SEER, HSPF et COP », avec les trois définitions et un conseil (demander le COP à basse température, un climatiseur seul n'a pas de HSPF ni de COP de chauffage);
- la liste « bonne soumission » demande les cotes SEER et HSPF et le COP à basse température;
- nouvelle question FAQ « C'est quoi le SEER, le HSPF et le COP? » (visible + balisage FAQPage, 5 questions).

À compléter par Jonathan Allard : plage de HSPF et de COP (à 8 °C et à basse température) des modèles vendus. Aucun chiffre de HSPF ou de COP n'est inventé dans la maquette. Idée : ajouter une ligne « Efficacité » (SEER / HSPF + COP) au tableau comparatif de la page pilier une fois les chiffres connus.

## Titre de l'auteur : copropriétaire (13 octobre 2026)

Jonathan Allard est copropriétaire de l'entreprise, pas « conseiller » : titre corrigé dans le bloc auteur, sous le titre de l'article et dans le balisage Article (`jobTitle` « Copropriétaire »). Un guide validé par un propriétaire renforce les signaux d'expérience et de confiance (E-E-A-T), sans être un facteur de classement direct. Lien LinkedIn personnel (https://ca.linkedin.com/in/joallard) ajouté dans `sameAs` de la Person.

## Puissance en pieds carrés (13 octobre 2026)

Le client propose de remplacer « zone moyenne » par des pieds carrés approximatifs. Le texte dit maintenant : « Un format de 12 000 BTU, très courant, convient généralement à un espace d'environ 400 à 600 pieds carrés [approximation à valider] ». L'estimation de départ (règle générale de l'industrie, non vérifiée par Bédard) est à confirmer par le client. Idée : petit tableau BTU / superficie approximative (9 000, 12 000, 18 000, 24 000 BTU) avec les chiffres de l'équipe des ventes, qui répond directement à la recherche « quelle puissance BTU choisir ».

Validé par le client (copropriétaire) : un format de 12 000 BTU convient jusqu'à environ 1 000 pi², selon les circonstances et les autres données. Texte publié : « peut convenir jusqu'à environ 1 000 pieds carrés ». L'estimation de 400 à 600 pi² est abandonnée. Le tableau BTU / superficie reste à faire avec les chiffres du client pour 9 000, 18 000 et 24 000 BTU.

## COP de près de 5 (13 octobre 2026)

Le client indique que certains modèles ont un COP qui atteint tout près de 5. Ajouté à la section efficacité : « certains modèles atteignent un COP de près de 5 [température de mesure à préciser] ». À préciser avant publication : la température à laquelle ce COP est mesuré (en général à une température extérieure douce, autour de 8 °C; le COP baisse par grand froid), et le modèle exact. Une allégation chiffrée de performance doit pouvoir être appuyée par la fiche technique du fabricant (publicité non trompeuse). Garder aussi le COP à basse température : c'est celui qui compte en hiver.

## Correction : cotes SEER2 et HSPF2 (13 octobre 2026)

Le copropriétaire corrige les données d'efficacité : HSPF2 jusqu'à 15,6 et SEER2 jusqu'à 35. L'article publie « jusqu'à 15,6 en HSPF2 » et « jusqu'à 35 en SEER2 » (remplace « SEER de 17 à 28 »), et le vocabulaire passe à SEER2 et HSPF2 (titre de section, liste, FAQ visible et balisage FAQPage, liste de contrôle de la soumission). Une phrase explique que le « 2 » indique la norme d'essai actuelle et que les nouvelles cotes ne se comparent pas directement aux anciennes.

Le COP de « près de 5 » est retiré en attendant confirmation (l'encadré « À compléter » le dit). À obtenir : COP à basse température (par exemple à -15 °C). Si le COP de près de 5 est confirmé avec sa température de mesure, on le remet.

## COP confirmé : 4,95 à 47 °F (13 octobre 2026)

COP de 4,95 à 47 °F (8,3 °C) pour certains modèles, confirmé par le copropriétaire. Publié avec sa température de mesure : « certains modèles atteignent un COP de 4,95 à 8,3 °C (47 °F) ». À garder : la fiche technique du fabricant qui appuie ce chiffre (publicité non trompeuse). Reste à obtenir le COP à basse température (par exemple à -15 °C), l'encadré « À compléter » le demande toujours.

## COP à basse température : 2,38 à 17 °F (13 octobre 2026)

COP de 2,38 à 17 °F (-8,3 °C) confirmé par le copropriétaire. Publié à côté du COP de 4,95 à 47 °F, avec la comparaison au chauffage électrique ordinaire (COP de 1). L'encadré « À compléter » est retiré. Le conseil de l'article cite maintenant les deux points de mesure (47 °F et 17 °F). Optionnel : COP à -15 °C (5 °F), utile pour les grands froids de janvier. L'article n'attend plus que le prix multizone.

## Hub Commercial (maquette)

Fichier : `maquettes/commercial.html` (sources : `src/gen_commercial.py`, `src/commercial.body.html`, `src/commercial-extra.css`, assemblé par `build_contact.py`). URL cible : `/commercial/` (nouvelle page, hub parent de `/commercial/refrigeration-commerciale/`, `/commercial/ventilation-commerciale-joliette/` et `/commercial/ferblanterie/`).

- Titre « Services commerciaux CVAC-R à Joliette | Bédard » (47 caractères), description de 154 caractères. JSON-LD : WebPage + Service (zone Lanaudière) + FAQPage (4 questions) + fil d'Ariane.
- Structure : héros avec formulaire de soumission commerciale (nom et entreprise, téléphone, type de projet), 4 points forts, 3 métiers (réfrigération, ventilation, ferblanterie) qui renvoient aux sous-pages, publics visés, déroulement en 4 étapes (relevés et conception, dessins et coordination, installation, mise en service et entretien), bande entretien et urgence 24 h, section réalisations, FAQ de 6 questions, liens vers les autres services, appel final.
- Contenu repris de ton site et de la page Carrières : conception et installation de ventilation personnalisée, réfrigération commerciale, ferblanterie spécialisée en ventilation, dessins d'intégration et d'atelier, collaboration avec les chargés de projet, travaux surtout dans Lanaudière, Ventilation Fabro (2012), entretien périodique, urgence 24 h.

À fournir ou valider :
1. Projets de référence (3 à 6) avec photos, type de bâtiment, ville, travaux, et l'autorisation des clients.
2. Licences et certifications à afficher (RBQ, CCQ), numéros de licence.
3. La phrase « entrepreneurs et gestionnaires » comme public visé.
4. Les trois sous-pages (réfrigération, ventilation, ferblanterie) restent à construire, sur le modèle de la page de service. Ventilation commerciale : 2 943 impressions sur 16 mois, la plus prometteuse.
5. Photo du héros : image de la bibliothèque du site (intérieur industriel), licence à confirmer.
6. Le formulaire envoie à l'équipe commerciale (adresse à préciser), avec suivi `form_submit` distinct de la soumission résidentielle (`data-form="commercial"`).

## Sous-page Ventilation commerciale (maquette)

Fichier : `maquettes/ventilation-commerciale-joliette.html` (sources : `src/gen_ventilation.py`, `src/ventilation.body.html`, assemblé par `build_contact.py`). URL cible : `/commercial/ventilation-commerciale-joliette/`. Titre « Ventilation commerciale à Joliette | Bédard » (43 caractères), description de 151 caractères, JSON-LD WebPage + Service + FAQPage (7 questions) + fil d'Ariane (Accueil > Commercial > Ventilation).

**Pourquoi cette page** : dans Search Console, « ventilation commerciale joliette » compte 2 943 impressions en position moyenne 6,9, avec 0 clic (16 mois). Aucune page dédiée n'y répond aujourd'hui : c'est la page générique `/services/` qui ressort. D'autres requêtes de ventilation ont beaucoup d'impressions (« ferblantier ventilation brossard » 3 089, « échangeur d'air québec » 1 949) mais portent sur des villes hors secteur : on ne les vise pas.

Contenu : héros avec formulaire de soumission, 4 points forts, 6 services (conception et dessins, ferblanterie sur mesure, installation, échangeurs d'air, nettoyage des systèmes, entretien et dépannage), types de bâtiments, déroulement en 4 étapes, facteurs du prix (aucun prix publié, projets sur mesure), pourquoi Bédard (Ventilation Fabro 2012, Solution Ventech 2010), réalisations, FAQ, liens liés.

Attention à la concurrence entre pages : au lancement, `/services/` doit pointer vers cette page (lien contextuel « ventilation commerciale ») et ne pas viser la même requête. Le hub `/commercial/` envoie aussi vers elle.

À fournir ou valider : exemples de bâtiments pour chaque type (marqués « à valider »), 3 à 6 projets de référence, délais typiques d'un projet, licences RBQ et CCQ, photo du héros (la photo du hub, licence à confirmer).

Correction transversale : les numéros de téléphone ne se coupent plus en deux lignes (`a[href^="tel:"]{white-space:nowrap}`), sur toutes les pages construites avec `build_contact.py` et `build_carrieres.py`.

## Sous-page Réfrigération commerciale (maquette)

Fichier : `maquettes/refrigeration-commerciale-joliette.html` (sources : `src/gen_refrigeration.py`, `src/refrigeration.body.html`, `src/refrigeration-extra.css`, assemblé par `build_contact.py`). URL cible : `/commercial/refrigeration-commerciale/`. Titre « Réfrigération commerciale à Joliette | Bédard » (45 caractères), description de 138 caractères, JSON-LD WebPage + Service + FAQPage (7 questions) + fil d'Ariane.

**Données de recherche** : volume plus modeste que la ventilation (environ 1 500 impressions utiles en 16 mois) : « frigoriste joliette » 205 impressions (position 6,6), « réfrigération notre-dame-des-prairies » 214, « compagnie de réfrigération » 110 (position 7,3), « entreprise frigoriste » 169, « refrigeration climatisation » 198 (position 15), « climatisation commerciale » 146 (position 73), « bedard refrigeration » 97 (position 2,5). Les requêtes hors secteur (Brossard, Rimouski, Baie-Saint-Paul, Beloeil) ne sont pas visées. L'angle retenu : « Vos frigoristes à Joliette » et l'urgence 24 h, un vrai besoin quand de la marchandise est à risque.

Contenu : héros avec formulaire, 4 points forts, 6 services (installation, service et dépannage 24 h, entretien préventif, climatisation commerciale, contrôle et régulation, équipe de frigoristes), bande urgence en 3 gestes (appel, diagnostic, réparation), types de clients, déroulement en 4 étapes, facteurs du prix (aucun chiffre), réalisations, FAQ, liens liés (dont Carrières : « Devenez frigoriste »).

Photo du héros : image « refrigeration-commerciale-opt.jpg » de la bibliothèque médias de ton site (chambre froide avec évaporateur), assombrie pour garder le contraste. À confirmer : licence (photo d'archive ou photo de Bédard) et, idéalement, la remplacer par une photo d'un chantier réel.

À fournir ou valider : liste des équipements qu'on installe et entretient (chambres froides, comptoirs, systèmes centralisés : l'encadré de la page le demande), exemples de clients par type, 3 à 6 projets de référence, licences et certificats de frigoriste, délai d'intervention en urgence (aucune promesse de délai écrite pour l'instant).

## Correctif visuel : chiffres des étapes (13 octobre 2026)

Les gros chiffres en contour (01 à 04 des déroulements, 01 à 06 des cartes commerciales, chiffres de l'accueil) montraient des traits parasites à l'intérieur du « 4 » : la police variable Mona Sans a des tracés qui se chevauchent, et un contour (`-webkit-text-stroke`) les dessine tous. Remplacé par des chiffres pleins en teinte pâle, sans contour. Toutes les pages ont été reconstruites. Quand Ballinger (police statique) sera installée, on pourra reconsidérer un contour, à tester sur chaque chiffre.

## Sous-page Ferblanterie (maquette)

Fichier : `maquettes/ferblanterie-joliette.html` (sources : `src/gen_ferblanterie.py`, `src/ferblanterie.body.html`, `src/ferblanterie-extra.css`, assemblé par `build_contact.py`). URL cible : `/commercial/ferblanterie/`. Titre « Ferblantier en ventilation à Joliette | Bédard » (45 caractères), description de 142 caractères, JSON-LD WebPage + Service + FAQPage (7 questions, mentions « à valider » retirées du balisage) + fil d'Ariane.

**Demande de recherche : faible.** Une seule requête de ferblanterie dans 16 mois de Search Console : « ferblantier ventilation brossard » (3 089 impressions, position 53), hors secteur et sans clic. « Ferblantier Joliette » n'apparaît pas. Cette page sert donc surtout de **page de soutien** : elle complète le hub commercial et la ventilation, rassure les entrepreneurs et les concepteurs, et alimente le **recrutement** (bloc « Vous êtes ferblantier(ère)? » avec salaire CCQ commercial, véhicule de service, travail à l'année, chantiers locaux, repris de ta page Carrières). Aucune promesse de classement.

Contenu : héros avec formulaire, 4 points forts, 3 services (conduits sur mesure, installation sur chantier, modification et remplacement), pièces et conduits (illustration de ton site), réalisation (photo de chantier de ton site), déroulement en 4 étapes (plans et relevés, dessins d'atelier, fabrication, installation), recrutement, FAQ, liens liés.

Photos : « Ferblanterie-min » (conduits galvanisés installés dans un bâtiment) en héros et en réalisation; « ferblanterie-opt-realopt » (illustration de sections de conduits) dans « Pièces et conduits ». Licences et nom du projet à confirmer.

**À valider (important)** : la **fabrication en atelier**. Ton site dit « ferblantier spécialisé en ventilation… design, conception et installation » et ta page Carrières parle de ferblantiers, mais rien n'affirme que Bédard fabrique ses conduits dans son propre atelier. Les mentions « fabriquent », « fabrication sur mesure » et « atelier » (page ferblanterie, page ventilation, hub commercial) sont des suppositions marquées « à valider » sur cette page : à confirmer ou à retirer. Valider aussi la liste des pièces, les types de projets et le projet de la photo.

## Ferblanterie : pas de fabrication en atelier (13 octobre 2026)

Le copropriétaire précise : Bédard ne fabrique pas de conduits dans ses ateliers. L'entreprise peut toutefois se déplacer chez le client et faire fabriquer des pièces sur mesure lorsque des besoins spécifiques le demandent. Toutes les mentions de fabrication interne sont retirées :
- Page ferblanterie : service « Conduits sur mesure » devient « Pièces sur mesure » (relevés sur place, pièces fabriquées selon les mesures, installation par nos ferblantiers); étape « Fabrication » devient « Pièces sur mesure »; question FAQ « Fabriquez-vous… » devient « Pouvez-vous fournir des pièces sur mesure? » (réponse : on se déplace, on prend les mesures, on fait fabriquer, nos ferblantiers installent); « le ferblantier installe et ajuste » à la place de « fabrique et installe »; description et balisage Service corrigés.
- Page ventilation et hub commercial : carte « Ferblanterie » (installation sur chantier, pièces sur mesure au besoin), étape « Installation », FAQ reformulée, « Conception, ferblanterie, installation et entretien » à la place de « fabrication ».
- Accueil : « ferblanterie sur mesure » devient « ferblanterie ».
Les mots « atelier » qui restent désignent les **dessins d'atelier** (shop drawings), pas un atelier de fabrication.

## Pages de service résidentielles (maquettes)

Générées par `maquettes/src/gen_services.py` (blocs communs) et `gen_services_pages.py` (contenu des trois pages), avec `src/services-extra.css`, assemblées par `build_contact.py`. Même structure que la page d'installation de thermopompe (héros avec formulaire, points forts, contenu, déroulement, prix, avis, FAQ, liens, appel final).

| Page | URL cible | Requêtes visées (16 mois, Search Console) |
|---|---|---|
| `reparation-thermopompe-climatiseur-joliette.html` | `/services/reparation-thermopompe-climatiseur-joliette/` | « réparation thermopompe joliette » 7 491 impressions (position 7,8, 1 clic), « réparation air climatisé joliette » 1 276 (6,9), « réparation climatiseur joliette » 1 166 (8,8) |
| `entretien-nettoyage-thermopompe-climatiseur-joliette.html` | `/services/entretien-nettoyage-thermopompe-climatiseur-joliette/` | « nettoyage climatiseur joliette » 2 733 (position 13,9), « nettoyage thermopompe joliette » 2 688 (16,5) |
| `chauffage-auxiliaire-joliette.html` | `/services/chauffage-auxiliaire-joliette/` | « chauffage auxiliaire joliette » 2 970 (position 11) |

Les trois affichent actuellement la page générique `/services/` (ou aucune page) : le potentiel de clics est élevé, la position moyenne est déjà proche de la première page. Aucune promesse de classement.

Contenu :
- **Réparation** : 6 symptômes courants (ne chauffe pas, ne refroidit pas, fuite, givre, bruit, démarrages aléatoires), bande urgence 24 h en 3 gestes, « réparer ou remplacer? », déroulement, facteurs du prix (aucun chiffre), FAQ de 8 questions (secteurs inclus).
- **Entretien et nettoyage** : bénéfices de l'entretien, thermopompe murale ou climatiseur, entretien périodique planifié, déroulement, facteurs du prix, FAQ (nettoyage des échangeurs d'air et conduits, filtres, urgence).
- **Chauffage auxiliaire** : « pourquoi un appoint » avec les deux COP du copropriétaire (4,95 à 8,3 °C et 2,38 à -8,3 °C), deux options (thermopompe + fournaise bi-énergie; thermopompe murale + chauffage existant), ce que nous évaluons, déroulement, FAQ.

À valider avant publication : marques réparées, frais de diagnostic et de déplacement, fréquence d'entretien recommandée, liste détaillée du nettoyage, forfaits et tarifs, disponibilité des filtres en boutique, rapport d'intervention, description des options bi-énergie (avec le conseiller), fourchettes de prix du chauffage auxiliaire, subventions, mention « garantie du fabricant » (entretien exigé), liens vers les pages produit (fournaises électriques) et vers le guide de remplacement.

Maillage : chaque page renvoie aux trois autres services, à l'installation de thermopompe et au formulaire. Au lancement, `/services/` devra pointer vers ces trois pages (liens contextuels) sans viser les mêmes requêtes.

## Correction : options du chauffage auxiliaire (13 octobre 2026)

Le copropriétaire relève une erreur de logique : pour compléter une thermopompe, on n'installe pas une thermopompe murale. La section « Les options » de `/services/chauffage-auxiliaire-joliette/` présentait « Thermopompe murale : conserver votre chauffage actuel ». Reformulée en **deux types de chauffage auxiliaire** : (1) **fournaise électrique** (jumelée à une thermopompe centrale, système bi-énergie) et (2) **chauffage existant gardé en appoint** (types de chauffage à valider). La FAQ « bi-énergie ou appoint existant » ne mentionne plus de thermopompe murale. À faire valider par le conseiller : types de chauffage existants compatibles (plinthes électriques, etc.) et la compatibilité avec une maison sans conduits.

## Site de test hors ligne (13 octobre 2026)

`maquettes/build_offline.py` construit un dossier et un zip (`dist/site-bedard-offline.zip`, 2,4 Mo) qu'on ouvre sans Internet : double-clic sur `index.html`.
- 31 pages : 14 maquettées (accueil, installation de thermopompe, pilier, guide de prix, réparation, entretien, chauffage auxiliaire, commercial, ventilation, réfrigération, ferblanterie, carrières, contact, soumission), 4 hubs simples (Résidentiel, Services, Guides de prix, Blogue), 12 pages « à venir » (avis, boutique, pages produits, deux guides, politique de confidentialité, conditions d'utilisation) et un plan du site.
- Les liens `#` des maquettes sont remplacés par de vrais liens (règles de correspondance par texte du lien). Le menu principal de l'accueil ouvre les pages.
- Images extraites en fichiers (`img/`), police Mona Sans (licence OFL) incluse (`fonts/`). Ballinger non incluse. La carte Google de la page Contact demande Internet. Les formulaires sont des démonstrations.
- Test automatisé sur le zip décompressé : 1 000 liens internes valides (fichiers et ancres), les 31 pages atteignables depuis l'accueil, police chargée, aucune image cassée, aucune erreur JavaScript.

Bug trouvé et corrigé grâce à ce test : en ajoutant la section SEER2 / HSPF2 / COP de l'article « prix », un remplacement trop large avait supprimé les sections « Les options », « La saison d'achat », le bloc d'appel à l'action et **le tableau des prix par situation** (simple zone 3 500 $ à 5 300 $, multizone). Tout est restauré depuis l'historique git; l'article a maintenant les 6 facteurs, le tableau et la section efficacité.

## Version sobre (v3) : accueil et page de service pilote (13 octobre 2026)

**Retour du copropriétaire :** le site est très chargé, difficile à naviguer, et donne l'impression d'une entreprise de taille moyenne plutôt que d'un leader. Décisions : version sobre (5 à 6 blocs par page), pas de vraies photos pour l'instant, points « [à valider] » gardés dans les pages.

**Mesure de départ (v2) :** 10 à 11 sections par page, 740 à 1 635 mots, 17 à 23 cartes et vignettes, 5 à 6 boutons d'action, 3 à 7 « [à valider] », même gabarit répété partout, 4 cartes « À consulter aussi » au bas de chaque page, 12 pages « à venir » vides dans le test hors ligne.

**Ce qui a changé** (`maquettes/make_v3_template.py` fabrique `source-accueil-v3.template.html`; tous les générateurs utilisent maintenant ce gabarit) :
- **En-tête** : plus de bandeau du haut (adresse, heures, sans frais déplacés au pied de page et à la page Contact). Une seule barre : logo, menu à trois déroulants (Résidentiel, Commercial, Services) + Guides de prix et Carrières, numéro d'urgence 24 h bien visible, bouton de soumission. Menu mobile en accordéon.
- **Pied de page** : de 19 à 14 liens, sans paragraphe de description.
- **Accueil** : 12 blocs deviennent 6 : hero (titre, une phrase, un bouton, le téléphone, trois chiffres) + barre de soumission rapide; deux grands panneaux Résidentiel et Commercial; services en liste de 5 lignes; une seule citation client avec la note 4,9 sur 5; bandeau Carrières; appel final. Retirés de l'accueil : étapes, FAQ, guides en cartes, « pourquoi nous », zone desservie et la FAQ du balisage. Hauteur : ~4 800 px au lieu d'environ 9 000.
- **Page de service pilote (installation de thermopompe)** : hero + 5 blocs + appel final (murale ou centrale, déroulement, prix avec carte de soumission, une citation, FAQ de 5 questions). Retirés : bandeau de 4 faits, pastille, signes, trois cartes d'avis, encadré « programmes » (fondu dans l'intro du prix), 4 cartes « À consulter aussi » (remplacées par trois liens texte). Hauteur : ~5 700 px au lieu d'environ 8 400.
- Règles de style : un titre fort par bloc, plus d'espace vertical, pas d'étiquettes ni de badges répétés, un seul bouton principal par écran.

**À décider après évaluation :** si la direction convient, appliquer le modèle sobre aux autres pages (pilier, services résidentiels, commercial et ses 3 sous-pages, carrières, contact, soumission, article). Les photos de chantiers, d'équipe et de camions sont le plus gros levier pour avoir l'air d'un leader : des emplacements sont prévus (panneaux de l'accueil, hero).

## Version sobre v3.1 : retours du copropriétaire (14 octobre 2026)

Retours sur la première version sobre : certaines choses bien (les deux panneaux Résidentiel et Commercial), d'autres ordinaires.
- **Chiffres (65+, 40+)** : trop petits, à gauche, sans animation. Remplacés par une bande pleine largeur de trois très grands chiffres (65+ professionnels, 40+ ans d'expertise, 24 h service d'urgence) avec compteur animé qui monte à l'arrivée dans l'écran (vérifié : valeurs finales 65, 40 et 24).
- **Avis** : refaits en section marquante : « 4,9 » géant à dégradé qui monte en compteur, cinq étoiles dorées qui apparaissent une à une, et un carrousel de trois citations réelles (Mat L., Martin Loyer, K. Gianna) avec flèches, points et défilement automatique toutes les 7 secondes (arrêt au survol). Trois puces tirées des avis : travail propre, échéances respectées, service courtois. Même bloc sur la page de service pilote.
- **Logo** : de 46 px à 70 px de haut dans l'en-tête (60 px une fois la page défilée), et 80 px dans le pied de page.
- **Nos services** : une rangée compacte de 4 tuiles (installation, réparation, entretien, urgence 24 h) au lieu d'un grand bloc de 5 lignes.
- **Panneaux Résidentiel / Commercial** : conservés tels quels.
- **« Guides de prix » rétabli en « Blogue »** : le blogue contient aussi des articles informatifs, pas seulement des prix. Menu, pied de page, hubs et site hors ligne mis à jour. La page-hub « Guides » est supprimée; l'article sur le prix du climatiseur mural reste un guide de prix dans le blogue.
- **« Chauffage auxiliaire » n'est plus présenté comme un service** : ce n'est pas un service distinct, c'est un complément à la thermopompe. Retiré des tuiles de services, de la liste Services et des cartes « à consulter aussi » des pages de service. Il reste une page (la demande de recherche existe : « chauffage auxiliaire joliette », 2 970 impressions) classée sous **Résidentiel** (fil d'Ariane, balisage, URL cible `/residentiel/chauffage-auxiliaire-joliette/`) et appelée « Chauffage d'appoint » dans les menus.

## Retour à la « version 1 » avec un bandeau de menu agrandi (14 octobre 2026)

Après évaluation, le copropriétaire préfère la version 1 (design complet d'avant la version sobre) et demande un bandeau de menu plus gros : logo plus gros, titres de section plus gros.
- **Gabarit v2.1** (`maquettes/make_v21_template.py` fabrique `source-accueil-v21.template.html` à partir du gabarit v2 intact) : toutes les pages et le site hors ligne l'utilisent. Les gabarits v2 et v3 (version sobre) restent dans le dépôt, sans être utilisés.
- **Bandeau agrandi** : barre de 7 rem au lieu de 5,75 rem (5,9 rem défilée); logo de 62 px de haut à 1440 px de large (46 px avant), 94 px sur écran de 2560 px; titres du menu à 1,1 rem et en semi-gras (0,98 rem avant); numéro de téléphone et bouton de soumission plus gros. Marges latérales du bandeau resserrées pour que le tout tienne.
- **Test de largeur** : aucune sortie de cadre ni chevauchement à 1180, 1280, 1366, 1440, 1536, 1728, 1920 et 2560 px (page d'accueil et page de service). En dessous de 1100 px, menu burger.
- **Menu mobile** : le bouton burger de la version 1 ne faisait rien; il ouvre maintenant un menu complet (7 entrées + bouton de soumission).
- **Corrections conservées** : « Blogue » remplace « Guides de prix » (menu, titre de la section de l'accueil, pied de page); « chauffage d'appoint » remplace « chauffage auxiliaire » dans les textes de l'accueil; la carte « Chauffage auxiliaire » est retirée des « autres services » de la page d'installation; la page chauffage reste classée sous Résidentiel.
- **Entrées de menu** : Résidentiel, Commercial, Services, Blogue, Avis, Carrières (6, comme avant). Les menus déroulants de la version sobre ne sont pas repris.

## Bandeau de menu : fini le « saut » au défilement (14 octobre 2026)

Retour du copropriétaire : la bande bleue (haut de page) et la bande blanche (page défilée) s'affichaient différemment, ce qui « bogue pour l'œil » au passage de l'une à l'autre.

**Causes mesurées** : au défilement, le logo rapetissait (62 px à 54 px de haut), le menu se décalait d'environ 20 px vers la gauche, la barre perdait de la hauteur, le bandeau du haut (urgence, adresse, sans frais) disparaissait d'un coup et le fond passait de bleu à blanc avec le texte du menu de blanc à bleu.

**Correction** :
- Même hauteur de barre (6,5 rem), même logo, mêmes positions et mêmes tailles dans les deux états, à toutes les largeurs testées (1180, 1280, 1440, 1920, 2560 px) : x, largeur et hauteur du logo, du menu et du bouton identiques à 0, 20, 46, 70, 90, 200 et 600 px de défilement.
- **Même apparence tout le temps** : le bandeau reste bleu marine (comme le hero) avec texte blanc, logo beige et bouton rouille. Il devient seulement opaque et reçoit une ombre quand on défile (progressif sur 90 px), au lieu de basculer au blanc.
- Le bandeau du haut glisse vers le haut en suivant le défilement (46 px), au lieu de disparaître d'un coup.

Alternative écartée : un bandeau blanc défilé exige de changer de logo, de couleur de texte et de fond, donc le même saut visuel; sur le hero sombre, un bandeau blanc en haut de page est impossible sans logo foncé.

## Accueil : postes ouverts et section « secteurs / bureau » (14 octobre 2026)

- **Postes ouverts de l'accueil** : la section Carrières listait encore Frigoriste, Ferblantier(ère) et Dessinateur(trice), alors que le dessinateur est comblé et que le magasinier est ouvert. Corrigé : Frigoriste (Lanaudière), Ferblantier(ère) (Lanaudière), **Magasinier(ère) (Joliette)**, avec le texte « Frigoristes, ferblantiers, magasiniers ». Les liens mènent aux postes de la page Carrières. Plus aucune mention du poste de dessinateur comme poste ouvert sur le site.
- **« Où nous trouver » : deux informations différentes mélangées.** Le titre « Joliette et Lanaudière » et les pastilles parlaient des secteurs desservis, la carte en dessous de l'adresse physique du bureau. Séparées en deux blocs étiquetés : **« Secteurs desservis »** (titre « Nous desservons Joliette et Lanaudière », pastilles des 10 municipalités de la MRC de Joliette, phrase sur les secteurs voisins : Lavaltrie, Berthierville, Saint-Félix-de-Valois, Saint-Jean-de-Matha, Rawdon, Repentigny; la pastille « Autres secteurs : à confirmer » est retirée) puis **« Où nous trouver »** (carte « Notre bureau à Joliette » : adresse, téléphones, heures, fin de semaine, lien d'itinéraire). Même logique que la page Contact.

## Secteurs desservis : SEO et emplacement (14 octobre 2026)

**Question du client** : est-ce utile, au SEO, de mentionner tous les endroits desservis sur l'accueil? **Décision : non, la liste complète va sur la page Contact; l'accueil garde une phrase courte.**

Raisons (à confirmer par les résultats après le lancement) :
- Données Search Console (16 mois, 392 043 impressions au total) : les requêtes avec « Joliette » représentent environ 58 000 impressions et 135 clics; toutes les autres villes de la zone confirmée ensemble (Notre-Dame-des-Prairies 2 582, Lavaltrie 1 644, Saint-Félix-de-Valois 655, Repentigny 272, Saint-Charles-Borromée 166, Saint-Paul 87, Berthierville 72) font environ 5 500 impressions et 0 clic, soit environ 9 % de Joliette.
- Une liste de noms de villes sur l'accueil ne suffit pas à se classer pour « réparation thermopompe Lavaltrie » : il faudrait une page dédiée avec un contenu réellement propre à la ville. Une liste trop longue risque de passer pour du bourrage de mots-clés.
- Le classement local dépend surtout de la fiche Google (proximité, catégories, avis, zone de service) et du balisage `areaServed`, déjà dans le code de la page.

Réalisé : l'accueil dit « Nous desservons Joliette et Lanaudière. Toute la MRC de Joliette et plusieurs secteurs voisins de Lanaudière. » avec un lien « Voir la liste complète des secteurs desservis » vers la page Contact, qui garde les 16 municipalités. Le bloc « Où nous trouver » (carte du bureau) reste distinct.
À faire au lancement : régler les zones de service de la fiche Google. Pages par ville (Notre-Dame-des-Prairies, Lavaltrie) : à reconsidérer après 90 jours si le trafic le justifie, avec du contenu local réel.

## Bandeau du haut : urgence 24 h et heures du bureau (14 octobre 2026)

Le bandeau disait « Service d'urgence 24 h · Lundi au vendredi, 8 h à 17 h », ce qui laissait croire que l'urgence 24 h n'était offerte que pendant ces heures. Séparé : « Service d'urgence 24 h sur 24, 7 jours sur 7 » (à gauche) et « Bureau ouvert du lundi au vendredi, 8 h à 17 h » (au centre, avec une icône d'horloge). L'adresse, retirée du bandeau, reste dans le bloc « Où nous trouver », la page Contact et le pied de page. Dans la carte du bureau de l'accueil, la ligne « Fin de semaine : sur rendez-vous · Urgence 24 h » est remplacée par deux lignes distinctes : « Fin de semaine : sur rendez-vous avec un représentant » et « Urgence : 24 h sur 24, 7 jours sur 7, 450-753-9426 ».

## Secteurs desservis élargis (page Contact)

Demande : ajouter toutes les municipalités entre Joliette et Saint-Michel-des-Saints, Louiseville, Montréal-Est et Terrebonne.

- La liste de la page Contact passe de 16 à 34 municipalités, regroupées en 5 blocs : Joliette et la MRC de Joliette / Vers Saint-Michel-des-Saints / Vers Louiseville / Vers Montréal-Est / Vers Terrebonne (source : `src/gen_contact.py`, `GROUPES`).
- Accueil inchangé : phrase courte + lien vers Contact (décision SEO déjà prise).
- Note sous la liste : « Votre municipalité n'est pas dans la liste? Appelez-nous pour confirmer le service dans votre secteur. »
- **À valider par l'équipe** : la liste est établie selon les axes routiers (131/347, 158/138, A31/A40/343) — jugement à confirmer; les municipalités d'une seule MRC officielle ne sont pas toutes incluses (ex. Saint-Damien, Saint-Côme, Sainte-Béatrix, Saint-Alphonse-Rodriguez, Sainte-Marcelline-de-Kildare en Matawinie; Saint-Esprit, Saint-Jacques, Saint-Liguori en Montcalm).
- Correctif au passage : débordement horizontal mobile (390 px) sur Contact, causé par `white-space:nowrap` appliqué aux cartes `a[href^="tel:"]`.

## Secteurs desservis : 44 municipalités + carte

- Ajout des municipalités qui avaient été laissées de côté : Matawinie (Saint-Damien, Saint-Côme, Sainte-Béatrix, Saint-Alphonse-Rodriguez, Sainte-Marcelline-de-Kildare), Montcalm (Saint-Esprit, Saint-Jacques, Saint-Liguori; Saint-Roch-de-l'Achigan déplacée dans ce groupe) et Maskinongé / Yamachiche (groupe « Vers Louiseville et Yamachiche »). Total : 44 municipalités en 6 groupes.
- Nouvelle carte SVG des secteurs desservis sur la page Contact (colonne gauche, sticky sur bureau) : municipalités desservies en bleu foncé, reste du territoire en teinte pâle, bureau de Joliette en point rouille, légende et mention « © contributeurs OpenStreetMap » (licence ODbL, mention obligatoire).
- Données : frontières OSM via Nominatim, enregistrées dans `maquettes/data/osm-municipalites.json` (44 municipalités) et `maquettes/data/osm-mrc.json` (fonds MRC). Génération : `src/gen_carte.py` → `src/carte-secteurs.html`, injectée par `src/gen_contact.py`. Garde-fou : `gen_contact.py` refuse de générer si la liste de municipalités et les polygones de la carte ne correspondent pas exactement.
- Pour ajouter une municipalité : l'ajouter dans `GROUPES` (gen_contact.py) ET récupérer son polygone (même méthode que `data/osm-municipalites.json`).
- Carte entièrement hors-ligne (aucun appel externe, aucune tuile); étiquettes secondaires masquées sur mobile.
- Les frontières proviennent d'OSM (simplifiées); elles sont indicatives, pas une référence officielle.

## Secteurs desservis : carte retirée, liste courte + repliable

- Carte SVG retirée (jugée inutile). Fichiers `gen_carte.py`, `carte-secteurs.html` et `data/osm-*.json` supprimés (récupérables dans l'historique git, commit dbf849c).
- Page Contact : 15 villes clés visibles (Joliette, Notre-Dame-des-Prairies, Saint-Charles-Borromée, Saint-Félix-de-Valois, Saint-Jean-de-Matha, Rawdon, Saint-Michel-des-Saints, Lavaltrie, Lanoraie, Berthierville, Louiseville, Repentigny, Mascouche, Terrebonne, Montréal-Est), choisies d'après la demande réelle (Search Console) et les corridors. Bouton « Voir les 44 municipalités desservies » déplie la liste complète par groupes (`<details>`, tout reste dans le HTML).
- Analyse Search Console (392 k impressions) : hors Joliette, on affiche déjà pour « thermopompe/air climatisé » + Mascouche (~3 000 impr.), Lanoraie (~1 700), Lavaltrie (~1 600), Terrebonne (~1 600), Notre-Dame-des-Prairies (~670), Saint-Félix-de-Valois (~650), Saint-Sulpice (~360), Repentigny (~270) — mais 0 clic. Conclusion : une liste de villes ne suffit pas à capter ces requêtes; il faudra, après le lancement, des pages locales dédiées pour les 3-4 meilleures (Mascouche, Lavaltrie/Lanoraie, Terrebonne, Notre-Dame-des-Prairies) + fiche Google Business Profile avec zone de service.

## Bandeau du haut supprimé

- Le bandeau (urgence 24 h / heures du bureau / sans frais) est retiré de toutes les pages (`make_v21_template.py`). L'en-tête garde le logo, le menu, le 450-753-9426 et « Demander une soumission ».
- Impact SEO : nul. Un bandeau n'a pas de valeur en soi; ce qui compte, c'est la présence du nom, de l'adresse, du téléphone et des heures (NAP) dans du texte indexable et dans les données structurées. Ils restent dans le pied de page de toutes les pages, la page Contact (cartes et fiche du bureau), le JSON-LD LocalBusiness (heures, téléphones, 24 h/24 pour l'urgence) et, au lancement, la fiche Google Business Profile.
- L'urgence 24 h reste visible : puce du hero d'accueil, pastille du hero Contact, appel final, barre « Appeler » mobile.
