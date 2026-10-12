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

## 11. Comparaison : 28 derniers jours (13 sept. au 10 oct. 2026) contre la même période de 2025
Données : `data/search-console/comparaison-28j-vs-an-passe/`.

| Mesure | 2025 | 2026 | Écart |
|---|---|---|---|
| Clics (tous appareils) | 204 | 168 | -18 % |
| Impressions | 25 750 | 11 160 | -57 % |
| CTR | 0,82 % (Canada) | 1,61 % (Canada) | doublé |
| Position moyenne (Canada) | 34,5 | 24,1 | meilleure |
| Clics de marque (requêtes exportées) | 26 | 53 | doublés |

Évolution mensuelle des clics d'une année à l'autre : juin -3 %, juillet -47 %, août -67 %, septembre -33 %, 28 derniers jours -18 %. La perte est concentrée sur juillet et août 2026, en pleine saison de la climatisation.

Constats :
1. **Ce n'est pas un effondrement global.** Les positions moyennes s'améliorent et la marque progresse. La baisse d'impressions vient en grande partie de requêtes sans valeur (« ferblantier ventilation brossard », « chauffage et climatisation beauport », « installation climatisation québec »…) où le site était classé 55 à 85 et qui ont disparu.
2. **Les requêtes locales à forte valeur ont perdu des rangs :**
   - thermopompe joliette : position 2,9 → 22,1
   - installation climatiseur joliette : 2,8 → 18,6
   - ventilation commerciale joliette : 2,9 → 15,4
   - air climatisé joliette : 3,0 → 11,1
   - chauffage auxiliaire joliette : 9,0 → 20,7
   - nettoyage thermopompe joliette : 10,2 → 42,2
   Les requêtes contenant « joliette » : clics 8 → 3, impressions 2 994 → 1 660.
3. **Pages locales en recul :** `/contact-climatisation-joliette/` position 7,1 → 17,2 ; `/climatiseur-mural-air-climatise-thermopompe-joliette/` 18,4 → 35,2 ; `/produits/chauffage/thermopompes-centrales/` 16,9 → 24,4.
4. **Article phare :** `/air-climatise-mural-a-quel-prix-sattendre/` clics 34 → 3 (-91 %), impressions -83 %, alors que sa position moyenne s'améliore (15,6 → 7,1). La requête « air climatisé mural » passe de 524 à 17 impressions presque sans changer de rang (14,7 → 13,5). Un changement dans l'affichage des résultats de Google (réponses IA, autres blocs) est plus probable qu'un problème technique du site.
5. **Contenu vieilli :** l'article phare date de 2022 (modifié le 2022-08-30), celui sur le remplacement de thermopompe de 2023 (modifié le 2023-05-18). Les prix cités (2 500 $ à 4 200 $) sont probablement dépassés pour des requêtes « prix ».
6. Appareils : ordinateur 102 clics (position 31,4), mobile 58 clics (position 8,7), tablette 8.
7. Aucun des éléments mesurés n'incrimine directement un plugin ou un problème technique. L'hypothèse du plugin reste à tester avec les dates de modification des dossiers (`wp-content/plugins`).

## 12. Conséquences pour la refonte
- Pages locales dédiées pour chaque service à Joliette (installation, réparation, entretien et nettoyage, ventilation commerciale, chauffage auxiliaire), avec titres précis, contenu récent, preuve locale (avis, projets, adresse) et formulaire.
- Rafraîchir les trois articles « prix » : prix à jour, date de mise à jour visible, FAQ structurée, calculateur ou formulaire de soumission, liens vers les pages de services.
- Données structurées d'entreprise locale, avis, FAQ.
- Suivre les mêmes indicateurs après le lancement : requêtes « joliette », position des pages locales, clics de marque, soumissions.

## 13. Fin du contrat de link building et dates de mise à jour des plugins

### Contexte fourni par le client
Un forfait de link building, avec l'entreprise qui rédigeait aussi les articles de blogue, n'a pas été renouvelé à partir de l'été 2026. La date exacte de fin est à confirmer. Le dossier `nitropack` n'existe pas dans `wp-content`.

### Vérification des pages qui nous lient (2026-10-12, `data/search-console/liens/verification-liens-2026-10-12.csv`)
Sur 163 URL de l'échantillon « autres exemples de liens » :
- 131 pages sont en ligne, 0 retournent 404/410.
- 88 contiennent encore un lien vers cbedard.com.
- 42 sont accessibles sans lien visible dans le HTML : 35 sont des fiches de l'ancien site `old.aldes-na.com` (le lien est peut-être chargé par script ou retiré ; le site actuel d'Aldes n'en montre aucun dans sa page d'accueil), 7 autres (lemeilleurduquebec.ca, stayonpro.com, canpages, cetaf.qc.ca).
- 32 ne peuvent pas être vérifiées (blocage anti-robots : Cylex, Datanyze, etc.).
Limite : Search Console ne garde pas l'historique des liens perdus. Les liens déjà retirés avant l'export n'apparaissent pas.
Conclusion provisoire : aucune preuve que les liens aient été retirés à la fin du contrat, mais l'historique complet manque.

### Dates de modification des plugins (cPanel, `wp-content/plugins`)
| Date | Plugins |
|---|---|
| 29 sept. 2026, 22 h 58-59 | wordpress-seo (Yoast), wpforms-lite, redirection, really-simple-ssl, post-smtp, advanced-custom-fields (mise à jour groupée) |
| 28 sept. 2026 | mainwp-child |
| 7 sept. 2026 | litespeed-cache, contact-form-7 et son module de téléversement |
| 27 juil. 2026 | gdpr-cookie-compliance |
| 6 juil. 2026 | duplicate-post |
| 14 mai 2026 | wp-review-slider-pro, post-smtp-pro |
| 1er mai 2026 | WPML (sitepress, string-translation, seo-multilingual) |
| 25 mars 2026 | woocommerce-gateway-stripe, woocommerce-multilingual, pdf-invoices |

Lecture : aucune mise à jour de plugin important (cache, SEO, thème, constructeur de pages) ne coïncide avec la baisse, qui débute entre le 13 et le 20 juillet. La mise à jour la plus proche avant est duplicate-post (6 juillet), sans impact SEO connu ; la plus proche après est le bandeau de cookies (27 juillet). L'hypothèse « plugin » est donc peu soutenue par ces données.

**`mainwp-child` est installé.** C'est l'extension qui permet à un tableau de bord MainWP (souvent d'une agence ou d'un webmestre) de gérer le site à distance. À identifier : qui contrôle ce tableau de bord, et est-ce toujours souhaité après la fin du contrat.

### Hypothèses liées au link building (ni confirmées ni écartées)
1. Arrêt de l'acquisition de nouveaux liens et de contenu pendant que les concurrents continuent : l'érosion des rangs locaux se manifeste en 1 à 3 mois, ce qui est compatible avec juillet-août.
2. Liens temporaires (loués) retirés à la fin du contrat : non soutenu par la vérification, mais l'historique manque.
3. Liens de faible qualité neutralisés par Google (articles génériques sur des sites français, annuaires automatiques) : indépendant de la fin du contrat, possible.
4. L'ancienne agence conserve un accès au site (MainWP ou autre) : risque de sécurité et de dépendance.

### À obtenir
- Date exacte de fin du contrat et rapports mensuels de l'agence (liste des liens et articles placés).
- Inventaire des comptes que l'agence contrôle : hébergement, WordPress, MainWP, Google Tag Manager, Analytics, Search Console, fiche Google Business Profile, droits d'auteur des articles.
- Historique des liens perdus avec dates : Ahrefs Webmaster Tools (gratuit pour son propre site) après validation du domaine.

## 14. Ahrefs Webmaster Tools (plan gratuit) : premières observations, 2026-10-12
Limites du plan gratuit : l'historique (onglet « Lost », périodes) et l'export CSV sont verrouillés ; l'analyse se fait par captures d'écran.

- Ahrefs recense 1 332 backlinks et 1 046 domaines référents (contre 192 liens et environ 92 domaines dans Google). Une grande partie est du bruit automatique.
- Les domaines apparus le 29 septembre 2026 (37486168.xyz, ailinkbuildingtool.website, mertio.shop, strongestbacklinks.shop, competitorlinkanalysis.online, s-tribe.net, etc.) sont étiquetés SPAM par Ahrefs : sites de vente de « link building » qui lient des millions de domaines. Ils ne sont pas ciblés sur cbedard.com et sont postérieurs à la baisse de juillet. Pas de désaveu recommandé.
- Liens de contenu dofollow les plus récents (503 au total) : annonces d'emploi `jobcqc.ca` (4 octobre) pointant vers `/carrieres` (redirigé vers `/carrieres/`), anciens PDF du journal APQ de 2010 (publicités avec le téléphone et `www.cbedard.com`, découverts fin septembre), fiches d'annuaires (`quebec-annuaire.com`, `unitedstatescompanies.org`). La date « First seen » est la date de découverte par Ahrefs, pas de création du lien.
- Chaîne de redirections inutile : `http://www.cbedard.com/` → `https://www.cbedard.com/` → `https://cbedard.com/` (deux sauts). Cible : un seul saut.
- Les liens vers `/carrieres` montrent que cette URL doit être conservée (CTR de 13 % dans Google).
- Les publireportages (Les Versants, La Nouvelle Union, etc.) sont toujours en ligne.

Prochaine étape : filtrer les backlinks sur « publireportage » dans l'URL de la page référente et trier par « First seen » pour dater les placements de l'ancienne agence.

## 15. Publireportages de l'ancienne agence (Ahrefs : dofollow, dans le contenu, URL contenant « publireportage »)
Résultat : 32 liens, tous considérés comme actifs par Ahrefs (le rapport « sans historique » n'affiche que les liens vivants).

Premières détections (« First seen »), du plus récent au plus ancien :
| Date | Site |
|---|---|
| 16 avril 2026 | infodunordvalleedelarouge.ca (chauffage : erreurs à éviter) |
| 15 avril 2026 | infodunordmontlaurier.ca (climatisation de la maison) |
| 30 octobre 2025 | infodunordtremblant.ca (puissance d'une climatisation murale) |
| 20 septembre 2025 | infodunordvalleedelarouge.ca (climatisation économique) |
| 2 septembre 2025 | infodunordsainteagathe.ca (choisir sa fournaise) |
| 1er septembre 2025 | laction.com (durée de vie d'un climatiseur mural) |
| 21 mai 2025 | lanouvelle.net (4 raisons de choisir une thermopompe) |
| 15 mars 2025 | leprogres.net (efficacité énergétique) |
| 14 mars 2025 | lerefletdulac.com, lechodemaskinonge.com, lechodelatuque.com |

Lecture :
- Le dernier placement détecté date de mi-avril 2026, soit trois mois avant le début de la baisse (13 au 20 juillet).
- Le rythme est faible : une trentaine de liens répartis sur 14 mois, surtout sur des sites régionaux de faible autorité (DR 27 à 64).
- Ces liens sont toujours actifs. Il n'y a pas de preuve de retrait à la fin du contrat.
- Ils pointent surtout vers les pages qui ont perdu des rangs (thermopompes centrales, climatiseur mural, climatisation Lanaudière, page « climatiseur mural… joliette »).
- Ce sont des articles commandités avec lien dofollow. Selon les consignes de Google, les liens payants devraient porter `rel="sponsored"` ou `nofollow`. Risque faible mais réel de neutralisation.

Conclusion provisoire : l'arrêt du link building seul explique mal une baisse de 47 à 67 % des clics. Il reste un facteur possible parmi d'autres (contenu et fiche d'entreprise Google non entretenus, concurrents plus actifs, changements dans les résultats de Google).

À vérifier ensuite : la fiche Google Business Profile (vues, appels, clics vers le site, par mois) et le contenu exact du contrat de l'ancienne agence (fiche d'entreprise, avis, citations, publications).

## 16. Google Business Profile (mai à octobre 2026, lecture des graphiques, valeurs approximatives)
Totaux de la période : 2 109 interactions, 875 appels, 613 clics vers le site Web.

| Mois | Interactions | Appels | Clics vers le site |
|---|---|---|---|
| Mai 2026 | 370 | 140 | 125 |
| Juin 2026 | 530 | 240 | 168 |
| Juillet 2026 | 405 | 185 | 120 |
| Août 2026 | 390 | 155 | 105 |
| Septembre 2026 | 330 | 125 | 83 |
| Octobre 2026 (partiel) | 90 | 40 | 20 |

Lecture :
- Pic en juin, puis baisse régulière : de juin à septembre, interactions -38 %, appels -48 %, clics vers le site -51 %.
- La fiche génère environ 145 appels par mois, plus que les clics vers le site. C'est une source de leads majeure à protéger et à exploiter dans la refonte (lien vers une page d'atterrissage avec UTM, services, photos, avis, publications).
- La baisse de la fiche est progressive, sans cassure en juillet, et plus modérée que celle du site dans Google (clics Search Console : juin 430, juillet 293, août 148, septembre 161). Une partie de la baisse est saisonnière (pic de climatisation en juin).
- Il manque la comparaison avec mai à octobre 2025 pour isoler la part saisonnière.

## 17. Périmètre du contrat avec l'ancienne agence et production visible
Réponse du client : le contrat portait principalement sur des liens et des articles de blogue (pas la fiche Google, pas l'entretien technique, pas la gestion du site).

Production visible (API WordPress et Ahrefs) :
- Blogue du site : 6 articles seulement, publiés le 2022-05-31, 2022-08-30, 2022-11-15, 2023-03-29, 2023-07-20 et 2024-01-18. Aucun depuis janvier 2024. Les trois articles « prix » qui génèrent 44 % des clics datent de 2022 et 2023 (dernières modifications 2022-08-30, 2023-05-18, 2023-12-21).
- Articles commandités sur des médias régionaux : environ 32, de mars 2025 à avril 2026.
- Pages du site modifiées en 2026 : accueil (25 mars), avis (4 mars), carrières (27 février).

Conclusion : la production sur le site s'est arrêtée 21 mois avant la baisse, et la dernière publication externe date d'avril 2026. La fin du contrat n'explique donc pas à elle seule la chute de juillet. Le vrai problème : personne n'entretenait le référencement (contenu vieillissant, fiche Google, technique) pendant que les concurrents continuaient.

À demander à l'agence : liste complète des articles et liens livrés (URL, date, cible), clause sur la durée de maintien des liens, propriété et droit de réutilisation des textes, retrait de ses accès (dont MainWP).

## 18. Suivi déjà installé sur le site (lu dans le conteneur Google Tag Manager `GTM-WBRNDF7`)
- Deux identifiants Google Analytics 4 : `G-W6VHEMGHS1` (avec les événements `call_tracking` et `form_submit`) et `G-Z8DXJE4D6X` (avec `call_tracking`).
- Suivi de conversions Google Ads : compte `868743737`, deux étiquettes de conversion.
- Aucun GA4 directement dans le code de la page : tout passe par GTM.
- Le bandeau de cookies précise que Google Analytics est un cookie « tiers » soumis au consentement : les données sont donc incomplètes (visiteurs qui refusent).

Conséquence : une propriété Analytics existe probablement déjà, sous un autre compte Google (ancienne agence ou ancien webmestre). Récupérer l'accès administrateur vaut mieux que d'en créer une nouvelle (on garde l'historique des appels et des formulaires).
Question ouverte : y a-t-il, ou y avait-il, des campagnes Google Ads ? Une pause estivale aurait réduit les leads sans toucher au référencement naturel.
