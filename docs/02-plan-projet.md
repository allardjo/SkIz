# Plan de refonte cbedard.com

Objectifs : (1) générer plus de leads, (2) optimiser le SEO, (3) design moderne, (4) refléter la nouvelle image de marque (logos, couleurs).

## Entrées requises du client
- Nouveaux logos (SVG si possible, versions couleur / blanc / noir)
- Couleurs (codes HEX) et polices, ou le guide de marque
- Photos de projets et d'équipe de qualité
- Accès à Google Analytics / Search Console (ou export des données clés)
- Liste des offres et zones desservies prioritaires

## Phases

### Phase 1 : Fondations (sans dépendre de la marque)
- Diagnostic (fait, voir `01-diagnostic.md`)
- Nouvelle arborescence et menu simplifié
- Plan de redirections 301 (ancien URL → nouvel URL) pour protéger le SEO
- Stratégie de mots-clés (service + ville : Joliette, Lanaudière, etc.)
- Parcours de conversion : appel, soumission, urgence 24 h

### Phase 2 : Contenu
- Message d'accueil et propositions de valeur
- Pages services et produits réécrites, orientées besoin du client
- Titres, méta-descriptions, FAQ, preuve sociale (avis)

### Phase 3 : Design (dépend des éléments de marque)
- Système de design : couleurs, typographie, composants
- Maquette HTML cliquable : accueil, page service, soumission, contact
- Validation mobile en premier

### Phase 4 : Développement WordPress
- Thème sur mesure (léger, sans page builder)
- Un seul formulaire de soumission, suivi des conversions
- Données structurées LocalBusiness, performance (Core Web Vitals), accessibilité
- Nettoyage des plugins

### Phase 5 : Migration et lancement
- Test sur site de préproduction
- Redirections 301, sitemap, Search Console
- Suivi des positions et des leads après lancement

## Décisions ouvertes
- Édition du contenu : blocs Gutenberg modifiables vs. mise en page figée
- Avenir de la boutique WooCommerce (filtres)
- Bilinguisme (WPML) : nécessaire ou non
