# Analyse Search Console (propriété https://cbedard.com/)

Données : `data/search-console/` (exports du 2026-10-12). Période de performance : 2025-06-11 au 2026-10-10 (16 mois).
Limite : Google ne donne que les 1 000 premières requêtes (environ 40 % des clics) ; le reste est anonymisé.

## 1. Vue d'ensemble
- 4 861 clics, 546 216 impressions, CTR 0,89 %.
- Appareils : mobile 2 375 clics (position moyenne 9,9), ordinateur 2 087 clics (position moyenne 34).
- Pays : Canada 91 % des clics ; France 304 clics (37 000 impressions) venant surtout des articles de blogue (peu de valeur pour les leads).
- Extraits de produits : 289 clics (filtres Aldes et autres).

## 2. Alerte : baisse de trafic depuis la fin juillet 2026
| Période | Clics / semaine | Impressions / semaine |
|---|---|---|
| Juin 2026 (pic) | 77 à 119 | 7 000 à 11 000 |
| Depuis le 20 juillet | 26 à 48 | 2 000 à 5 700 |

Comparaison d'une année à l'autre (pas seulement saisonnier) : août 2025 = 451 clics, août 2026 = 148 (-67 %) ; septembre 2025 = 240 clics, septembre 2026 = 161 (-33 %), impressions 32 251 → 14 138 (-56 %).
La cause est inconnue. À élucider avant la migration : changement de plugin, de cache, de thème, de configuration SEO, mise à jour de WordPress, ou mise à jour de l'algorithme de Google en juillet 2026.

## 3. Indexation (Google Search Console, 2026-10-08)
- 68 pages indexées, 69 non indexées.
- Raisons : 24 exclues par `noindex`, 16 « autre page avec canonique correcte », 12 redirections, 1 introuvable (404), 1 bloquée par robots.txt, 9 « détectées, non indexées », 6 « explorées, non indexées ».
- À vérifier URL par URL dans Search Console (rapport Pages) : quelles 24 pages sont en `noindex`, et si ce sont bien des pages techniques (panier, compte, etc.).
- Mon crawl du sitemap (corrigé après une première lecture fautive des balises) trouve 6 pages `noindex` parmi les 77 URL : panier, commande, mon-compte et leurs versions `/en/`. Les 18 autres pages `noindex` vues par Google sont hors sitemap : à identifier dans Search Console.

## 4. Les vraies pages qui rapportent (URL à protéger en priorité)
| Page | Clics | Impressions | Position | Note |
|---|---|---|---|---|
| `/air-climatise-mural-a-quel-prix-sattendre/` | 1 340 (28 %) | 144 731 | 10,2 | Article de blogue |
| `/` | 1 317 (27 %) | 143 454 | 36,1 | Marque + 135 liens externes |
| `/remplacer-thermopompe-a-quel-prix/` | 487 | 48 840 | 10,6 | Article de blogue |
| `/quel-est-meilleur-humidificateur-pour-maison/` | 305 | 27 648 | 14,6 | Article de blogue |
| `/produits/chauffage/thermopompes-murales/` | 173 | 42 454 | 31,9 | |
| `/contact-climatisation-joliette/` | 138 | 39 206 | 17,4 | |
| `/produit/paquet-2-filtres-haute-efficacite-aldes-h95-h150-h110/` | 135 | 6 981 | 8,0 | Fiche produit |
| `/avis/` | 123 | 10 988 | 11,3 | |
| `/climatiseur-mural-air-climatise-thermopompe-joliette/` | 106 | 64 293 | 23,6 | « À propos » dans le menu ; 10 liens externes |
| `/produits/chauffage/thermopompes-centrales/` | 87 | 60 204 | 24,8 | |
| `/carrieres/` | 48 | 367 | 5,4 | CTR 13 % |

Constat : **trois articles de blogue génèrent 44 % de tous les clics**, devant les pages de services. Ils ne doivent pas être touchés ni redirigés sans équivalent. Ce sont aussi les meilleures portes d'entrée pour capter des demandes de soumission (aujourd'hui rien ne le prévoit).
Règle : les 11 URL ci-dessus gardent exactement la même adresse (ou 301 direct vers un équivalent).

## 5. Requêtes
- Marque : 29 requêtes, 665 clics, position moyenne environ 2 (« bedard climatisation », « climatisation bédard », « claude bédard », etc.). La marque est forte.
- Hors marque : 971 requêtes, 1 280 clics, 380 000 impressions.
- **Les gens cherchent « bédard » + « climatisation ».** Le nouveau nom visuel « Bédard — Performance thermique » ne doit pas faire disparaître le mot « climatisation » à côté de « Bédard » dans les titres, descriptions et textes.

Meilleures requêtes hors marque (clics) : climatiseur mural (82), climatiseur mural prix avec installation (75), air climatisé mural prix (70), air climatisé mural (66), prix air climatisé mural (54), thermopompe joliette (42), remplacement thermopompe centrale (40), climatisation joliette (34).

## 6. Occasions de leads : beaucoup d'impressions, presque aucun clic
| Requête | Impressions | Clics | Position |
|---|---|---|---|
| installation thermopompe joliette | 14 379 | 3 | 7,2 |
| air climatisé mural | 11 640 | 66 | 11,4 |
| climatiseur mural | 10 174 | 82 | 9,9 |
| réparation thermopompe joliette | 7 491 | 1 | 7,8 |
| thermopompe joliette | 7 441 | 42 | 6,9 |
| thermopompe prix | 3 454 | 3 | 12,4 |
| air climatisé joliette | 3 188 | 3 | 4,8 |
| chauffage auxiliaire joliette | 2 970 | 0 | 11,0 |
| ventilation commerciale joliette | 2 943 | 0 | 6,9 |
| nettoyage climatiseur joliette | 2 733 | 0 | 13,9 |
| nettoyage thermopompe joliette | 2 688 | 0 | 16,5 |
| installation climatiseur joliette | 2 436 | 0 | 7,0 |

Pistes : le site est vu des milliers de fois pour des services précis à Joliette, mais n'a probablement pas de page dédiée pour chacun, et les titres et descriptions actuels n'attirent pas le clic. Il y a un levier direct : une page de service par ville et par besoin (installation, réparation, entretien/nettoyage, ventilation commerciale, chauffage auxiliaire) avec formulaire de soumission. Seulement 62 requêtes locales hors marque génèrent 116 clics.

## 7. Liens externes (192 au total)
- 135 liens vers l'accueil (66 sites), 10 vers la page « climatiseur mural… joliette », 6 vers climatisation Lanaudière, 6 vers climatiseur mural, 4 vers thermopompes centrales, 3 vers « remplacer thermopompe à quel prix ».
- Sources (échantillon de 160 URL, 92 domaines) : environ 35 Aldes (`old.aldes-na.com`, un ancien sous-domaine, risque de disparaître), environ 59 annuaires et profils d'entreprise (Reseau411, Cylex, MapQuest, Canpages, Infobel, Profil Canada, ZoomInfo, Crunchbase, etc.), environ 52 médias locaux et régionaux (réseau Info du Nord, journaux régionaux, souvent des publireportages), et une quinzaine d'autres (CETAF, CCGJ, articles de sites français et de blogues).
- Plusieurs sites de contenu général, surtout français, semblent être du contenu placé : à évaluer avant de s'en préoccuper.
- Textes d'ancrage : surtout de marque (« climatisation c bédard », « cbedard com ») et de sujets (« climatiseur mural », « thermopompe murale »). Profil naturel.

## 8. Liens internes (1 643)
Presque toutes les pages principales reçoivent 71-72 liens : ce sont le menu et le pied de page. La page « Conditions d'utilisation » reçoit autant de poids que les services. Le nouveau site doit concentrer le poids interne sur les pages qui rapportent et ajouter des liens dans le contenu (blogue vers services, services vers soumission).

## 9. À faire à cause de la marque
- Mettre à jour le nom, le logo et les coordonnées dans les annuaires listés ci-dessus et sur Google Business Profile (cohérence NAP).
- Demander à Aldes de vérifier que le lien fonctionne encore (leur ancien sous-domaine).
- Demander la mise à jour du nom dans les médias régionaux quand c'est possible.

## 10. Enquête sur la baisse de trafic (état au 2026-10-12)
Réponse du client : une mise à jour ou un plugin a été modifié (détails inconnus).

Vérifié, sans anomalie :
- Googlebot et un navigateur reçoivent la même réponse (200, même poids) sur l'accueil et l'article phare : pas de blocage selon le visiteur.
- Les dates de modification du sitemap n'indiquent aucune page modifiée depuis mars 2026 : la baisse ne vient pas d'une modification de contenu.
- `robots.txt` ne bloque rien d'important. 71 pages sont en `index, follow`, 6 pages techniques en `noindex` (normal).
- Les 3 anciennes URL connues de Google qui répondent en 404 ont un trafic négligeable (0 à 2 impressions) : pas la cause.
- `robots.txt` mentionne encore des dossiers NitroPack et LiteSpeed alors que seul LiteSpeed Cache est détecté sur les pages : un ancien plugin d'optimisation a peut-être été retiré.

Non vérifiable d'ici : Wayback Machine (connexion coupée), PageSpeed (quota de l'API dépassé), rapport par page dans le temps.

Pistes à confirmer (par ordre de probabilité) :
1. Mise à jour d'un plugin de cache ou d'optimisation (LiteSpeed, ancien NitroPack) qui aurait changé le rendu pour Google (JavaScript, images chargées en différé, CSS critique).
2. Changement chez Google (mise à jour de l'algorithme ou réponses de l'IA dans les résultats), qui toucherait surtout les articles « prix ». Position moyenne stable mais impressions en baisse = moins de visibilité.
3. Problème de vitesse ou de Core Web Vitals.

Vérifications à faire dans Search Console : Comparer les 28 derniers jours à la même période de l'an passé (par pages et par requêtes), puis les rapports « Actions manuelles », « Problèmes de sécurité » et « Core Web Vitals ».
Vérification dans le cPanel : trier `wp-content/plugins` par date de modification pour voir quel plugin a été mis à jour et quand.
