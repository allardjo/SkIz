# Plan de migration SEO : ne rien perdre, gagner du terrain

Base de départ : `inventaire-urls.csv` (77 URL du sitemap, crawl du 2026-10-12 : statut, title, meta description, H1, canonical, mots, schémas, poids).

## Règle d'or
Aucune URL qui rapporte du trafic ne disparaît ou ne change sans une redirection 301 vers son équivalent direct. On garde les mêmes adresses quand c'est possible.

## Ce qu'on sait du site actuel (vérifié)
- 77 URL : 38 pages, 39 produits (filtres à air), 6 articles de blogue.
- Les 39 fiches produit sont des filtres Maxi-Pleat avec un texte presque identique (~528 mots chacune).
- La page nommée « À propos » dans le menu a l'URL `/climatiseur-mural-air-climatise-thermopompe-joliette/` : c'est vraisemblablement une page qui se positionne sur un mot-clé fort. À garder telle quelle (ou 301 si on la déplace).
- 48 pages sur 77 n'ont pas de meta description.
- 71 pages ont un title de plus de 70 caractères (l'accueil en fait 170).
- 6 pages sans H1 (panier, commande, mon-compte, versions /en/ du panier et du compte).
- 99 images sans texte alternatif.
- Pages techniques dans le sitemap qui ne devraient pas y être : `/404-2/`, `/panier/`, `/commande/`, `/mon-compte/`, `/shop/` et les 4 pages `/en/...`. Deux d'entre elles ont un canonical qui pointe ailleurs.
- Schéma `Organization` seulement ; aucune fiche d'entreprise locale. Pas de FAQ, pas d'avis structurés.
- Seulement 6 articles de blogue.

## Avant la migration (références à figer)
1. Exporter de Google Search Console (16 derniers mois) : requêtes, pages, clics, impressions, position.
2. Exporter de Google Analytics : pages d'entrée, conversions, sources.
3. Relever les positions actuelles des 20 à 30 mots-clés clés (service + ville).
4. Test PageSpeed Insights (mobile et ordinateur) de l'accueil, d'une page service, de la soumission.
5. Relever le profil de liens entrants (pour savoir quelles URL ont des liens externes).
6. Sauvegarde complète du site actuel (fichiers + base de données).

Sans les points 1 à 3, on ne peut pas prouver que le nouveau site fait mieux. Ce sont les données que j'ai besoin que tu me fournisses.

## Pendant la construction
- Nouveau site construit sur un environnement de préproduction, protégé par mot de passe et en `noindex`.
- Carte de redirections 301 (ancienne URL → nouvelle URL) pour 100 % des URL du sitemap et celles qui ont des liens ou du trafic.
- Titles à 60 caractères ou moins, descriptions uniques sur 100 % des pages indexables, un seul H1 par page.
- Données structurées : `HVACBusiness` / `LocalBusiness` (adresse, heures, zone desservie, téléphone), `Service`, `FAQPage`, `Review`/`AggregateRating` si les règles de Google le permettent, `BreadcrumbList`.
- Pages techniques (panier, compte, 404) en `noindex` et retirées du sitemap.
- Décision sur les 39 fiches de filtres : selon les données de Search Console, soit on les garde avec un contenu unique, soit on les regroupe sous une page catégorie avec des 301.
- Maillage interne : chaque page service liée à ses produits, à ses articles et à la soumission.
- Performance : visées mesurables (mobile) : LCP < 2,5 s, CLS < 0,1, INP < 200 ms, score PageSpeed 90+.
- Accessibilité : contrastes et texte alternatif sur toutes les images.

## Lancement
1. Gel du contenu sur l'ancien site.
2. Test complet de la préproduction : liens brisés, redirections, formulaires, suivi des conversions, schémas valides.
3. Mise en ligne en dehors des heures de pointe.
4. Retirer le `noindex`, soumettre le nouveau sitemap dans Search Console, valider les redirections par crawl.
5. Vérifier le suivi des conversions (appels, formulaires, clic sur le téléphone) avec un vrai test.
6. Plan de retour arrière : sauvegarde prête à être restaurée.

## Après le lancement (90 jours)
- Surveillance quotidienne la première semaine : erreurs 404, couverture de l'index, positions, leads.
- Rapport à 30, 60 et 90 jours comparé à la référence d'avant migration.
- Nouveaux articles de blogue et pages locales (par ville) pour pousser le référencement.

## Ce que je peux garantir et ce que je ne peux pas
- Je peux garantir la méthode : redirections complètes, aucune URL oubliée, balises et schémas corrects, site plus rapide, suivi mesuré.
- Je ne peux pas promettre un classement précis. Google décide, et une migration cause souvent de petites fluctuations temporaires. Notre plan vise à les réduire au minimum et à améliorer les facteurs sur lesquels on a le contrôle.
