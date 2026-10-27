# Plan de migration et de lancement

Mis à jour le 2026-10-27. Complète `03-migration-seo.md` (principes) avec les chiffres réels, la carte des URL du nouveau site, le protocole de test, la surveillance et le retour arrière.

## 1. Ce qu'on protège

Données Search Console (16 mois, 392 000 impressions, 1 945 clics) :
- **Recherches de marque : environ 24 % des clics.** « bedard climatisation » (186 clics), « climatisation bédard » (115), « bédard climatisation » (54), « climatisation bedard » (39), « climatisation claude bédard » (38), « claude bédard » (37). Les gens cherchent « Bédard » + « climatisation » et « Claude Bédard ». **Conséquence pour le nom** : « Bédard » reste l'ancre du nom public; garder « climatisation » dans les titres de la page d'accueil et de la page Contact, et « Claude Bédard » dans le nom légal, le pied de page et `alternateName`.
- **Pages qui rapportent** : article prix du climatiseur mural (1 340 clics, 28 % du site), accueil (1 317 clics, 66 sites référents, 70 % des liens externes), remplacer une thermopompe (487), meilleur humidificateur (305), catégorie thermopompes murales (173), contact (138), avis (123), page pilier climatiseur mural/thermopompe (106, 10 liens), thermopompes centrales (87), services (68).
- **Fiche Google** : environ 145 appels par mois, plus que le site.
- **Tendance** : clics du site en baisse depuis juillet 2026 (juin 430, septembre 161). La comparaison d'après-lancement doit se faire contre la **même période de l'an dernier** et contre la tendance, pas contre un seul mois.

## 2. Carte des URL

### A. Adresses identiques, à ne pas changer (priorité 1)
`/`, `/air-climatise-mural-a-quel-prix-sattendre/`, `/remplacer-thermopompe-a-quel-prix/`, `/quel-est-meilleur-humidificateur-pour-maison/`, `/climatiseur-mural-air-climatise-thermopompe-joliette/` (page pilier), `/contact-climatisation-joliette/`, `/avis/`, `/soumission/`, `/carrieres/`, `/services/`, `/blogue/`, ainsi que les catégories de produits : `/produits/chauffage/`, `/produits/chauffage/thermopompes-murales/`, `/produits/chauffage/thermopompes-centrales/`, `/produits/chauffage/fournaises-electriques/`, `/produits/climatisation-lanaudiere/` (+ `climatiseur-mural`, `climatiseur-central`), `/produits/qualite-de-lair/` (+ échangeurs d'air, humidificateurs, purificateurs), `/produits/planchers-radiants/`, `/produits/geothermie/`.

**Conséquence pour les maquettes** : les tuiles « Thermopompe murale », « Thermopompe centrale », « Géothermie », « Planchers radiants », « Fournaises électriques » et « Qualité de l'air » doivent pointer vers ces adresses existantes, pas vers de nouvelles. Les pages « à venir » du site de test (thermopompes-murales, thermopompes-centrales, geothermie, planchers-radiants…) prennent ces URL.

### B. Nouvelles pages (aucune ancienne URL, donc aucune redirection)
- `/services/installation-thermopompe-joliette/`
- `/services/reparation-thermopompe-climatiseur-joliette/`
- `/services/entretien-nettoyage-thermopompe-climatiseur-joliette/`
- `/residentiel/chauffage-auxiliaire-joliette/`
- `/commercial/`, `/commercial/ventilation-commerciale-joliette/`, `/commercial/refrigeration-commerciale/`, `/commercial/ferblanterie/`

À faire pour chacune : title et description uniques, balisage, présence dans le sitemap, au moins 3 liens internes entrants (accueil, menu, pages liées).

### C. Redirections 301 (7)
| Ancienne adresse | Nouvelle adresse |
|---|---|
| `/air-climatise-a-quel-prix-sattendre/` | `/air-climatise-mural-a-quel-prix-sattendre/` |
| `/air-climatise-mural-a-quel-poids-sattendre/` | `/air-climatise-mural-a-quel-prix-sattendre/` |
| `/quel-est-meilleur-humidificateur-maison-quebec/` | `/quel-est-meilleur-humidificateur-pour-maison/` |
| `/en/shop/` | `/shop/` |
| `/en/cart/` | `/panier/` |
| `/en/checkout/` | `/commande/` |
| `/en/my-account/` | `/mon-compte/` |

Autres décisions déjà prises : `/404-2/`, `/panier/`, `/commande/`, `/mon-compte/`, `/shop/` en `noindex` et hors sitemap; `/shop/` avec canonical vers `/boutique-web/`. Source : `data/redirections-et-arborescence.csv` (81 lignes).

### D. Risque de cannibalisation (à surveiller, ne pas régler avant le lancement)
« Thermopompe murale / climatiseur mural » sera visée par 3 pages : la catégorie de produits (173 clics), la page pilier (106) et la page d'installation (nouvelle). Règle : chacune garde son rôle (catalogue, information et comparaison, service et soumission), avec des liens croisés. Décision à 90 jours selon les positions.

## 3. Calendrier (lancement visé : janvier 2027)

**Décisions du 2026-10-27** : lancement visé en janvier 2027; **responsable du retour arrière : le propriétaire de l'entreprise** (à nommer aussi un suppléant joignable pendant les 7 premiers jours).

**Date cible : mardi 12 janvier 2027**, début de matinée. Date de repli : mardi 19 janvier. Cette fenêtre laisse 90 jours de stabilisation avant la haute saison (mars à juillet) et évite les fêtes (20 décembre au 5 janvier).

| Période | Étape | Responsable |
|---|---|---|
| 27 oct. à 13 nov. | Valider les textes « [à valider] »; fournir : vraies photos, avis réels de la fiche Google, licence web de la police Ballinger, accès à l'hébergement et au domaine, ventes de filtres (voir `10-fiches-filtres.md`) | Client |
| 27 oct. à 13 nov. | Terminer les pages manquantes (produits aux URL actuelles, politique de confidentialité) | Agence |
| 16 nov. à 4 déc. | Intégration WordPress en préproduction (gabarits, URL, redirections, données structurées) | Agence |
| 16 nov. à 4 déc. | Fiche Google : catégorie principale, services, description (avant le lancement) | Client |
| 7 à 18 déc. | Protocole de test complet (§5) et corrections; **11 déc. : exports de référence** (Search Console, GA4, positions, PageSpeed) | Agence |
| 18 déc. | **Gel du développement** | Agence |
| 21 déc. à 4 janv. | Pause. Seulement les validations finales de contenu | Client |
| 5 à 8 janv. | Sauvegarde finale, répétition de la restauration, **décision go / no-go le vendredi 8 janvier** | Agence + responsable |
| **12 janv.** | **Lancement** (§6) | Agence; responsable du retour arrière disponible toute la journée |
| 19 janv. | Contrôle à 7 jours | Agence |
| 19 à 26 janv. | Changement du nom de la fiche Google, si l'enseigne, les camions et les factures sont prêts (jamais le jour du lancement) | Client |
| 11 fév. | Contrôle à 30 jours | Agence |
| 13 mars | Contrôle à 60 jours | Agence |
| 12 avril | Contrôle à 90 jours; décisions sur les filtres, la cannibalisation et les pages locales | Agence + client |

**Risques de calendrier** : les éléments qui dépendent du client (photos, avis, licence de police, accès hébergement, nom d'usage) sont le chemin critique. Si un élément n'est pas livré le 4 décembre, on le remplace par une solution temporaire (photos d'archive, police de remplacement) plutôt que de reporter la date.

## 4. Avant le lancement (T-30 à T-1)

| # | Tâche | Qui | Critère |
|---|---|---|---|
| 1 | Exports Search Console (16 mois : requêtes, pages) et GA4 (pages d'entrée, conversions) archivés dans le dépôt | Agence | Fichiers datés |
| 2 | Relevé des positions des 25 requêtes suivies (§7) | Agence | Tableau initial |
| 3 | PageSpeed mobile et ordinateur : accueil, service, soumission | Agence | Scores de départ |
| 4 | Sauvegarde complète du site actuel (fichiers + base de données), restauration testée | Hébergeur / agence | Restauration réussie sur un site de test |
| 5 | Exploration de l'ancien site (liste complète des URL, y compris produits) | Agence | Comparée à la carte du §2 |
| 6 | Fichier de redirections 301 chargé en préproduction | Agence | 100 % des anciennes URL répondent 200 ou 301 |
| 7 | Préproduction protégée par mot de passe, en `noindex` | Agence | Vérifié |
| 8 | Contenus [à valider] résolus ou retirés | Client | Aucune mention « [à valider] » restante |
| 9 | Police Ballinger (licence web, WOFF2) et photos (licence) confirmées | Client | Documents au dossier |
| 10 | Politique de confidentialité (Loi 25) publiée, bandeau de consentement testé | Client + agence | Page en ligne |
| 11 | Accès : retrait des accès de l'ancienne agence, mots de passe changés | Client | Liste d'accès signée |

## 5. Protocole de test en préproduction

| Test | Comment | Réussite |
|---|---|---|
| Liens | Exploration complète | 0 lien brisé interne |
| Redirections | Chaque ancienne URL de la carte | 301 en un seul saut vers la bonne cible |
| Titres et descriptions | Exploration | 100 % uniques; titres ≤ 60 caractères |
| H1 | Exploration | Un seul par page |
| Canonical | Exploration | Chaque page indexable pointe vers elle-même |
| `noindex` | Pages techniques | Présent; absent des pages publiques |
| Sitemap et robots | Fichiers | Sitemap sans pages `noindex`; robots n'interdit pas le site |
| Données structurées | Test des résultats enrichis (par type) | Aucune erreur : HVACBusiness, Service, FAQPage, BreadcrumbList, JobPosting, Article |
| Formulaires | Soumission réelle et appel de test | Courriel reçu; événements `form_submit` et `call_tracking` visibles dans GA4 (GTM-WBRNDF7) |
| Vitesse | PageSpeed mobile | LCP < 2,5 s, CLS < 0,1, INP < 200 ms, score 90+ |
| Images | Exploration | Alt sur toutes les images de contenu; WebP |
| Accessibilité | Contrastes et clavier | Pas d'erreur critique |
| Appareils | Téléphone, tablette, ordinateur | Aucun défilement horizontal; menu mobile fonctionnel |
| Boutique | Panier, commande, filtres | Achat test réussi |

## 6. Jour J

1. Geler le contenu de l'ancien site (veille).
2. Sauvegarde finale.
3. Déployer le nouveau site et les redirections; retirer le `noindex`.
4. Vérifier tout de suite : accueil, 10 pages clés, 5 redirections, formulaire, appel.
5. Soumettre le nouveau sitemap dans Search Console; demander l'indexation de l'accueil et des 5 pages clés.
6. Mise à jour des liens vers le nouveau site : fiche Google (site web avec UTM), Facebook, LinkedIn, signatures de courriel.
7. Garder l'ancien serveur ou la sauvegarde accessible 30 jours.

## 7. Requêtes à suivre (25)

Marque : bedard climatisation; climatisation bédard; claude bédard; climatisation claude bédard.
Service + ville : thermopompe joliette; installation thermopompe joliette; réparation thermopompe joliette; climatisation joliette; air climatisé joliette; chauffage auxiliaire joliette; ventilation commerciale joliette; nettoyage thermopompe joliette; chauffage joliette.
Produit : climatiseur mural; air climatisé mural; climatiseur mural prix; air climatisé mural prix; climatiseur mural prix avec installation; thermopompe murale prix; thermopompe prix; remplacement thermopompe centrale; meilleur humidificateur.
Autres : fournaise électrique joliette; géothermie joliette; plancher radiant lanaudière.

## 8. Surveillance et seuils

| Quand | Quoi | Seuil d'alerte |
|---|---|---|
| Jour 1 à 7, chaque jour | Erreurs 404 et couverture de l'index, appels et formulaires, positions des requêtes de marque | Toute 404 sur une URL de la carte; formulaire ou appel non reçu |
| Semaine 1 | Pages indexées vs attendues | Moins de 90 % des pages attendues |
| Jour 7 | Clics et impressions vs 7 jours précédents | Baisse de plus de 30 % |
| Jour 30 | Clics, positions des 25 requêtes, appels de la fiche, conversions | Baisse de plus de 20 % vs même période de l'an dernier et vs tendance |
| Jour 60 | Même rapport + vitesse réelle (Core Web Vitals) | Aucune page clé sous sa position de départ de plus de 3 rangs |
| Jour 90 | Rapport complet; décision sur cannibalisation, pages locales, blogue | Rapport comparé à la référence |

Les fluctuations de 2 à 4 semaines après une migration sont normales; un seuil dépassé déclenche une enquête (redirections, balises, indexation), pas un retour arrière automatique.

## 9. Retour arrière

**Déclencheurs** (un seul suffit) : formulaires ou appels non fonctionnels depuis plus de 4 heures; plus de 5 pages clés en erreur 404 ou 500; site entier en `noindex` après correction tentée; baisse de plus de 50 % des clics pendant 3 jours consécutifs sans cause identifiée.

**Procédure** : décision du responsable désigné (le propriétaire) sur avis de l'agence; restaurer la sauvegarde finale (fichiers et base de données); rétablir le DNS et les redirections de l'ancien site; vérifier les 10 pages clés; informer l'équipe; analyser la cause avant une nouvelle tentative. Durée visée : moins de 2 heures.

## 10. Décisions et informations à obtenir

1. ~~Date de lancement~~ : janvier 2027, cible le 12 janvier (décidé le 2026-10-27).
2. ~~Responsable du retour arrière~~ : le propriétaire (décidé le 2026-10-27). Reste à nommer un suppléant.
3. Hébergement : accès, procédure de sauvegarde et de restauration, DNS.
4. Confirmer que les URL de la section A sont toutes conservées (surtout les catégories de produits).
5. Les 39 fiches de filtres : garder tel quel ou regrouper (voir `03-migration-seo.md`).
6. Nom d'usage déclaré au Registraire; enseigne et camions prêts avant le changement de nom de la fiche Google.
7. Avis réels à importer (page Avis) et lien d'avis (déjà fourni).
