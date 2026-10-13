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
