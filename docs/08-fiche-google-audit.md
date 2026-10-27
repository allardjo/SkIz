# Audit de la fiche Google (Google Business Profile) et de la cohérence NAP

**Statut : audit partiel.** La fiche Google elle-même (Maps, tableau de bord) n'est pas accessible depuis mon environnement, et les pages des annuaires (Carrier, CAA-Québec) ne s'ouvrent pas non plus; je n'ai que les résultats de recherche. Ce document donne (1) ce que j'ai pu établir, (2) la grille à remplir en 15 minutes avec la fiche ouverte, (3) les valeurs cibles à y mettre. Avec une capture d'écran ou l'export de la fiche, je complète la colonne « Constaté ».

## 1. Ce que j'ai pu établir

**Noms différents selon la source (risque de cohérence NAP)**

| Source | Nom affiché |
|---|---|
| CAA-Québec (entreprises recommandées) | Entreprise de Réfrigération & Climatisation Claude Bedard (1995) inc. (RBQ 2163-6048-78 selon la fiche), 304, boulevard de l'Industrie, Joliette |
| Carrier (détaillant) | « Climatisation C.Bedard », même adresse |
| Site actuel / futur site | Bédard, Performance thermique |
| Fiche Google (d'après le lien de partage fourni) | « Réfrigération Claude Bédard 1995 Inc. » (identifiant d'entité Google `/g/1tdkrdrw`) : un quatrième nom, sans « Entreprise de » ni « & Climatisation » |

Quatre noms pour une même adresse : Google rapproche les citations par nom + adresse + téléphone. Plus les variantes sont nombreuses, plus le signal local se dilue.

**Données de la fiche déjà en main (Search Console / tableau de bord, mai à octobre 2026)**
- 2 109 interactions, 875 appels, 613 clics vers le site; environ 145 appels par mois, donc plus d'appels que de clics.
- Baisse de juin à septembre : interactions -38 %, appels -48 %, clics vers le site -51 % (en partie saisonnière).
- Aucune activité de publication connue : le contrat de l'ancienne agence ne couvrait pas la fiche.

## 2. Grille à comparer avec la fiche (colonne « Constaté » à remplir)

| Champ | Cible recommandée | Constaté |
|---|---|---|
| Nom | Le nom de l'enseigne réelle (celle de la façade, des camions et du logo). Pas de mots-clés ajoutés. Si la façade dit « Bédard Performance thermique », c'est ce nom. | |
| Adresse | 304, boulevard de l'Industrie, Joliette (Québec) J6E 8V2, identique au site, à Carrier et à CAA | |
| Téléphone principal | 450-753-9426 (le même qu'au site); sans frais 1-800-953-0153 en secondaire | |
| Site Web | https://cbedard.com/ avec UTM (`?utm_source=google&utm_medium=gbp`), pour isoler les clics de la fiche dans GA4 | |
| Lien « Rendez-vous / Soumission » | Page de soumission du site (avec UTM) | |
| Catégorie principale | Celle qui correspond à la demande la plus forte (thermopompe et climatisation résidentielles) : une catégorie de type « Entrepreneur en climatisation ». À vérifier dans l'interface, les libellés exacts varient. | |
| Catégories secondaires | Chauffage, ventilation, réfrigération (entrepreneur), selon ce que l'interface propose; 3 à 5 maximum, que des catégories réellement offertes | |
| Heures | Lundi au vendredi 8 h à 17 h; ajouter le service d'urgence 24 h sur 24 en note ou en « heures spéciales »; jours fériés à jour | |
| Zone de service | 20 maximum. Proposition : Joliette, Notre-Dame-des-Prairies, Saint-Charles-Borromée, Saint-Paul, Saint-Thomas, Crabtree, Saint-Félix-de-Valois, Saint-Jean-de-Matha, Rawdon, Saint-Michel-des-Saints, Lavaltrie, Lanoraie, Berthierville, Louiseville, L'Assomption, Saint-Sulpice, Repentigny, Mascouche, Terrebonne, Montréal-Est | |
| Services | Un service par ligne avec courte description : installation, réparation, entretien et nettoyage de thermopompe et climatiseur, chauffage d'appoint, ventilation commerciale, réfrigération commerciale, ferblanterie | |
| Description (750 caractères max.) | Voir proposition ci-dessous | |
| Photos | 25 à 50 vraies photos : façade, équipe, camions, installations avant/après, chantiers commerciaux. Ajout régulier (2 à 4 par mois). Pas de photos d'archive. | |
| Logo et photo de couverture | Nouveau logo (marque Bédard), format carré, fond propre | |
| Avis | Note actuelle vs 4,9 affiché sur le site (« 180+ avis » : 176 Google + 12 Facebook au dernier relevé). Réponse à tous les avis, surtout aux plus récents. Demande d'avis systématique après chaque chantier (lien court + code QR). | |
| Questions et réponses | Remplir les 6 à 8 questions les plus fréquentes (zones, prix, urgence, subventions, garanties, délai de soumission) | |
| Publications | 1 à 2 par mois : projet réalisé, rappel d'entretien avant l'été, offre saisonnière. Dernière publication : ? | |
| Messagerie, appels manqués | Réponse rapide; désactiver si personne ne répond | |
| Attributs | Services d'urgence, soumission gratuite, bilingue (si applicable), accessible en fauteuil | |
| Propriétaires et gestionnaires | Au moins 2 personnes de l'entreprise, plus un accès pour l'agence seulement si nécessaire; retirer les accès de l'ancienne agence | |
| Doublons et fiches fermées | Rechercher « Bédard Joliette », « Claude Bédard », « Climatisation C. Bédard » : fusionner ou faire supprimer tout doublon | |

## 3. Proposition de description (à valider, 489 caractères sur 750 permis)

« Bédard, c'est plus de 40 ans d'expertise en chauffage, climatisation, ventilation et réfrigération à Joliette et dans Lanaudière. Notre équipe de plus de 65 professionnels installe, répare et entretient thermopompes, climatiseurs muraux, fournaises et systèmes de ventilation, pour les maisons comme pour les commerces et les institutions. Soumission gratuite. Service d'urgence 24 h sur 24, 7 jours sur 7. Anciennement Entreprise de Réfrigération & Climatisation Claude Bédard (1995) inc. »

À valider : « 40 ans », « 65 professionnels », mention de l'ancien nom (utile pour relier les citations existantes). Le numéro RBQ peut être ajouté seulement s'il est confirmé.

## 4. Actions de cohérence hors Google (à faire au lancement)

1. **Un seul nom, une seule adresse, un seul téléphone** sur : site, fiche Google, Facebook, LinkedIn, Carrier (et autres marques représentées), CAA-Québec, RBQ, Pages Jaunes, Yelp, Canada 411, Chambre de commerce.
2. **Carrier** : demander la mise à jour du nom (« Climatisation C.Bedard » → nom actuel), du site Web (cbedard.com) et des services; ces pages de détaillant sont des citations à forte autorité.
3. **CAA-Québec** : mettre à jour le nom commercial et le lien vers le nouveau site.
4. **Site** : nom légal (`legalName`) dans le pied de page et les données structurées, `sameAs` vers la fiche Google, Facebook et LinkedIn, même adresse et même téléphone partout (déjà prévu dans les maquettes).
5. **Lien de la fiche vers le site** : page d'accueil pour le lien principal; pages « Soumission » et « Réparation et dépannage » pour les boutons rendez-vous et appel d'urgence.

## 5. Où la fiche peut le plus rapporter

- Fiche = ~145 appels par mois : c'est le canal à protéger en premier. Le site seul génère moins de leads directs.
- Le classement local se joue sur la proximité, la pertinence (catégories, services, description) et la notoriété (avis, citations). Les deux leviers que l'entreprise contrôle le plus vite : **catégories/services complets** et **avis récents avec réponses**.
- Les requêtes avec ville (Mascouche, Lanoraie, Lavaltrie, Terrebonne) montrent de la demande sans clics : la zone de service élargie de la fiche et, plus tard, des pages locales avec projets réels sont les deux leviers.

## 6. Ce que j'ai besoin de toi pour finir l'audit

Une de ces trois options : capture d'écran de la fiche (vue publique et tableau de bord), lien de la fiche Maps, ou export des informations. Je remplis alors la colonne « Constaté » et je te donne la liste des écarts classés par priorité.

## 7. Complément : lien de partage de la fiche (2026-10-27)

- Lien fourni : https://share.google/YKjmWuKXecckxKHwZ. Il mène à la fiche « Réfrigération Claude Bédard 1995 Inc. » (identifiant d'entité Google `/g/1tdkrdrw`). Seule la redirection a pu être lue; le contenu de la fiche (catégories, heures, services, avis) reste à vérifier avec une capture d'écran.
- Le nom affiché sur Google est donc **différent** de la marque (« Bédard Performance thermique ») et du nom légal complet. À corriger après le lancement de l'enseigne (voir `docs/04-marque.md`).
- Liens utilisés sur la page Avis : « Voir tous les avis sur Google » = lien de partage de la fiche; « Laisser un avis » et code QR = lien d'avis direct https://g.page/r/Ceb7Vf7wbTIAEBM/review (fourni le 2026-10-27). Le code QR (`maquettes/src/qr-avis.svg`) est généré pour ce lien; à imprimer sur les factures, cartes de visite et camions.
- Où trouver ces liens : en étant connecté au compte propriétaire, rechercher le nom de l'entreprise sur Google ou ouvrir Google Maps > fiche > « Partager » > copier le lien (profil); « Demander des avis » ou « Obtenir plus d'avis » > copier le lien (avis).
- Pour les données structurées, `sameAs` devra pointer vers la fiche (URL Google Maps de la fiche ou identifiant d'entité), Facebook et LinkedIn.

## 8. Relevé de la fiche (captures du 2026-10-27)

| Élément | Constaté | Verdict |
|---|---|---|
| Nom saisi dans le tableau de bord | Entreprise de Réfrigération & Climatisation Claude Bédard 1995 Inc. | = nom légal (à changer au lancement de l'enseigne) |
| Nom affiché dans Google (recherche / Maps) | « Réfrigération Claude Bédard 1995 Inc. » (diminutif choisi par Google) | Écart : Google affiche autre chose que ce qui est saisi |
| Note et avis | 4,7 sur 5, 202 avis Google | Le site disait 4,9 et « 180+ » (moyenne de l'ancien site, plus ancienne) : **corrigé partout** (« 4,7 sur 5, plus de 200 avis Google ») |
| Catégorie principale | Fournisseur de systèmes de climatisation | Catégorie de vente; à remplacer par une catégorie d'entrepreneur (installation, réparation) |
| Catégorie secondaire | Entrepreneur spécialisé dans le chauffage | OK; ajouter ventilation, réfrigération, thermopompe si l'interface les propose |
| Adresse | 304 Bd de l'Industrie, Joliette, QC J6E 8V2 | Conforme au site |
| Téléphone | (450) 753-9426 | Conforme au site |
| Heures | Lundi à vendredi 8 h à 17 h; samedi et dimanche fermé | Conforme au site; urgence 24 h non indiquée (à ajouter en heures spéciales ou en attribut) |
| Date d'ouverture | Mai 1983 | Confirme « plus de 40 ans » (43 ans) |
| Description | « Entreprise de ventilation, chauffage et climatisation établie depuis plus de 40 ans… contrats de services… design de systèmes de ventilation… » | Correcte mais sans « thermopompe » (la demande la plus forte), sans villes desservies, sans urgence 24 h, et avec une coquille (« Oeuvrant »). Remplacer par la version du §3. |
| Gestion | « Vous gérez ce profil » | OK |
| Bouton Site Web | Présent | Ajouter les paramètres UTM |
| Zone de service, services, produits, publications | Non visibles sur les captures | À vérifier dans le tableau de bord |

## 9. Harmoniser les noms (plan)

**Pourquoi Google affiche un diminutif.** Le nom public d'une fiche vient du graphe de connaissances de Google, pas seulement du champ « Nom de l'entreprise ». Quand le nom saisi, le site, les annuaires et le registre ne concordent pas (ici : nom légal long, « Claude Bedard (1995) inc. » chez CAA-Québec, « Climatisation C.Bedard » chez Carrier, « Bédard Performance thermique » sur le futur site), Google raccourcit ou choisit lui-même la variante. La seule solution durable : faire concorder toutes les sources.

**Nom cible partout : « Bédard Performance thermique »** (nom public), nom légal seulement là où il est exigé.

Ordre des opérations :
1. Registraire des entreprises du Québec : déclarer le nom d'usage.
2. Enseigne, camions, factures, soumissions, signature de courriel, site : changer d'abord (Google veut que le nom de la fiche corresponde au nom réel affiché).
3. Site : `name` = Bédard Performance thermique, `legalName` = nom légal exact du REQ, `alternateName` = Bédard, Réfrigération Claude Bédard, `sameAs` = fiche Google, Facebook, LinkedIn; titre de la page d'accueil et du pied de page cohérents.
4. Fiche Google : modifier « Nom de l'entreprise » pour « Bédard Performance thermique » (garder une photo de la nouvelle façade ou d'un camion sous la main si Google demande une vérification). Mettre « Anciennement Entreprise de Réfrigération & Climatisation Claude Bédard 1995 Inc. » dans la description pendant 12 à 24 mois.
5. Mises à jour des autres plateformes, au même moment :

| Plateforme | Nom à y mettre |
|---|---|
| Facebook (page climatisationbedard), LinkedIn, Instagram | Bédard Performance thermique |
| Carrier (détaillant), autres marques (Mitsubishi, Harnois, Ventech, Fabro) | Bédard Performance thermique, site cbedard.com |
| CAA-Québec (entreprises recommandées) | Bédard Performance thermique, avec le nom légal en complément |
| Pages Jaunes, Yelp, Canada 411, Chambre de commerce, Apple Maps (Business Connect), Bing Places, Waze | Bédard Performance thermique |
| RBQ, REQ, contrats, factures | Nom légal (ne change pas) + nom d'usage déclaré |

6. Si le diminutif persiste après 4 à 6 semaines : demander la correction du nom à l'assistance du Profil d'entreprise Google (formulaire de modification du nom) en joignant la preuve (enseigne, REQ, site).
7. Ne jamais ajouter de mots-clés dans le nom de la fiche (risque de suspension).

**Catégories à demander.** Principale : une catégorie d'entrepreneur en climatisation (au lieu de « Fournisseur de systèmes de climatisation »); secondaires : chauffage (déjà là), ventilation, réfrigération commerciale, selon les libellés proposés par l'interface.
