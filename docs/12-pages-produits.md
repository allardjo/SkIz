# Pages de produits (à partir du Portail vendeur)

## Source
- « Portail vendeur — Bédard » (https://www.cbedard.com/portail-cbedard/) : une seule page HTML qui contient tout le catalogue (tableaux `CATALOGUE`, `EXTRAS`, `GARANTIES`, `CAPACITES`, marques). Relevé du 2026-11-12 : 288 entrées (Mitsubishi 104, Carrier 83, Daikin 58, Stelpro 25, Aldes 10, Thermolec 7, Sinopé 1). La copie du dépôt `bedard-crm` (30 octobre) est identique, sauf 9 entrées Daikin renommées.
- Hors de la page, le portail n'a que deux tables en base de données (`soumissions`, `profiles`) : soumissions de clients et utilisateurs, privées et inutiles pour les pages de produits. Aucun accès au portail n'est donc nécessaire d'un autre ordinateur.
- Extrait public (sans prix ni photos des fabricants) : `data/catalogue-produits.json`. Générateur : `maquettes/build_produits.py` (styles : `maquettes/src/produits-extra.css`).

## Pages produites (site de test)
| Page | Adresse prévue | Contenu |
|---|---|---|
| Thermopompes murales | `/produits/chauffage/thermopompes-murales/` (existante, 173 clics) | 12 séries Mitsubishi, Carrier, Daikin; choix selon le froid (-15, -25, -37 °C); capacité; FAQ |
| Thermopompes multizones | `/produits/chauffage/thermopompes-multizones/` (**nouvelle**) | 3 séries multizones (2 à 5 zones); types d'unités intérieures (murale, console, cassette, gainable) |
| Climatiseur mural (refroidissement seul) | `/produits/climatisation-lanaudiere/climatiseur-mural/` (existante, 45 clics) | 2 séries; comparaison avec la thermopompe murale |
| Thermopompes centrales | `/produits/chauffage/thermopompes-centrales/` (existante, 87 clics) | 5 séries; cabinets, serpentins, éléments électriques, thermostats |
| Échangeurs d'air | `/produits/qualite-de-lair/echangeurs-dair/` (existante, 52 clics) | 7 modèles Aldes (VRC et VRE), 3 contrôles |

Les chiffres (nombre de séries, capacités, froid, débits) sont **calculés à partir du catalogue** : une mise à jour du portail met les pages à jour au prochain assemblage.

## Règles appliquées
- Pages par série (environ 25), pas par modèle (288) : pas de pages minces.
- Aucun prix. Les prix du portail sont à 0 sauf 20 entrées, jamais publiés.
- Photos : aucune photo de fabricant (liées à leurs serveurs, droits à confirmer). Pas de photo d'unité extérieure pour illustrer une murale.
- Séries R-410A exclues des pages (Carrier Performance R-410A, Infinity, multizone R-410A, etc.) : à confirmer si elles sont encore offertes.
- Textes rédigés par nous, pas copiés des fabricants.
- Pas de balisage de produit avec prix ou avis : `CollectionPage`, `ItemList`, `BreadcrumbList` et `FAQPage` seulement.

## Divergences constatées (à corriger dans le portail ou à valider)
- **Carrier Performance (simple zone et multizone)** : le portail indique SEER2 jusqu'à 27,5 et HSPF2 jusqu'à 14,8; la fiche du fabricant dit « SEER2 jusqu'à 35,1 et HSPF2 jusqu'à 15,6 ». Les pages et l'article utilisent 35 et 15,6 (comme déclaré par le copropriétaire).
- Autres séries : la lecture automatique des fiches n'a pas permis de confirmer tous les chiffres (fiches de combinaisons, plusieurs cotes par PDF, certaines fiches Daikin inaccessibles). Les chiffres d'efficacité des autres séries viennent du portail et sont marqués **[À valider contre les fiches avant publication]**.
- Le COP du portail (ex. 4,95 pour la série FX) n'indique pas la température de mesure : il n'est pas publié sur les pages, sauf dans l'article (4,95 à 8,3 °C et 2,38 à -8,3 °C, déclarés par le client).

## À valider avant publication
1. Séries R-410A (offertes ou non).
2. Chiffres d'efficacité par série contre les fiches (liste ci-dessus).
3. Garanties (conditions des fabricants : enregistrement, durée, main-d'œuvre).
4. Permission d'utiliser les noms de marques dans les titres et les textes (ententes de concessionnaire Mitsubishi, Carrier, Daikin).
5. Homologation Energy Star des échangeurs Aldes.
6. Fréquence d'entretien d'un échangeur d'air.
7. Prix indicatif d'un simple zone (3 500 $ à 5 300 $ avant taxes) repris de l'article.

## Pas dans le portail (autre source nécessaire)
Fournaises électriques, humidificateurs et déshumidificateurs, purificateurs, géothermie, planchers radiants, filtres (boutique en ligne).

## Migration
L'adresse `/produits/chauffage/thermopompes-multizones/` est nouvelle : l'ajouter au sitemap et à la liste des nouvelles pages de `09-plan-migration-lancement.md` (section 2B). Les autres adresses sont celles du site actuel (section 2A) : même URL, contenu remplacé.

## Couverture du catalogue (relevé du 2026-11-14)
Sur 288 entrées du portail : **122** sont décrites par une carte de série ou un tableau (unités extérieures, échangeurs d'air et contrôles Aldes); **60** accessoires (cabinets souffleurs, serpentins, éléments électriques, thermostats) sont cités dans les listes de la page des thermopompes centrales; **106** entrées n'étaient pas représentées individuellement (unités intérieures murales, consoles, cassettes, gainables, et séries R-410A exclues).

**Ajout (choix du client : « liste des modèles dans chaque série »)** : chaque carte de série a maintenant un bouton repliable « Voir les modèles (N) » : numéro de l'unité extérieure, capacité en BTU et unité intérieure associée de même capacité (murales Mitsubishi et Carrier; cabinets souffleurs et serpentins pour les centrales). La page des multizones a une liste repliable des consoles, cassettes et gainables (Mitsubishi, Carrier, Daikin, Stelpro). Les modèles Daikin n'ont pas d'unité intérieure distincte dans le catalogue; les séries R-410A restent exclues (à confirmer).

**Hub Résidentiel** : le groupe « Air et ventilation » devient « Qualité de l'air » avec deux cartes séparées : « Échangeur d'air » (page produit) et « Purificateur d'air » (page à venir, URL actuelle `/produits/qualite-de-lair/purificateurs-dair/`). Les humidificateurs et déshumidificateurs (URL actuelle `/produits/qualite-de-lair/humidificateurs-deshumidificateurs/`, 27 clics) ne sont plus dans le hub : à décider (carte ou page).

## Photos des produits (2026-11-14)
- Source : les photos listées dans le catalogue du portail (serveurs des fabricants : Mitsubishi, Carrier, Daikin, Stelpro, Aldes, etc.), 61 images distinctes, une par série ou par modèle. Téléchargées, détourées (fond transparent), réduites à 640 px et converties en WebP (1,3 Mo en tout, 78 Ko au maximum). Elles sont **hébergées avec le site** (pas de lien direct vers les serveurs des fabricants).
- Utilisation : photo de l'unité intérieure en tête de chaque carte de série murale (ou de l'unité extérieure si la série n'a pas de photo d'unité intérieure), miniatures dans le tableau des échangeurs d'air, photos des contrôles Aldes. Texte alternatif descriptif sur chaque image.
- **Droits à confirmer avant publication** : ces images appartiennent aux fabricants. Vérifier dans les ententes de concessionnaire (et les portails de marque Carrier, Mitsubishi, Daikin) l'usage permis et les consignes (mention de marque, retouche, détourage). En cas de doute, demander les fichiers officiels aux représentants.
- **Pas dans le dépôt public** : les images (`maquettes/img/produits/`), la correspondance modèle-photo (`data/photos-fabricants.json`) et les pages produits qui les intègrent (`maquettes/produits-*.html`) sont exclues de git. Pour les régénérer : placer les images et la correspondance, puis `python3 -I maquettes/build_produits.py` et `python3 -I maquettes/build_offline.py`. Le zip de test les contient.
- Une photo de la série (ex. « Série GX ») est partagée par les variantes -25 °C et -37 °C : le catalogue n'a qu'une image pour ces deux séries.
