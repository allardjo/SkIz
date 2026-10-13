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
