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
