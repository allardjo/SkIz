# Maquette de la page d'accueil (v1)

Fichier : `maquettes/accueil.html` (page autonome, ouvrable dans un navigateur ; logos intégrés ; polices Mona Sans via Google Fonts, à héberger sur le site final).

## Intentions
- **Leads :** téléphone cliquable en permanence (barre du haut, en-tête, barre fixe sur mobile), formulaire de soumission dans l'écran d'accueil, appel final à l'action, urgence 24 h visible dès le haut.
- **SEO local :** H1 « Thermopompe, climatisation et chauffage à Joliette », une grille de 8 services qui devient 8 pages locales, guides de prix (les trois articles qui génèrent 44 % des clics), FAQ avec données structurées `FAQPage`, `HVACBusiness`/`LocalBusiness` avec nom légal, adresse, heures et zone desservie (JSON-LD dans la page).
- **Marque :** marine pour les fonds forts, beige pour les sections alternées, rouille réservé aux boutons d'action (contraste 6,6 sur blanc), cyan seulement sur fond foncé (règle de contraste), symbole en filigrane, Mona Sans partout. Les titres utilisent Mona Sans en graisse forte tant que la licence web de Ballinger n'est pas confirmée.
- **Mobile d'abord :** une colonne, barre fixe « Appeler / Soumission ».

## Contenu réel repris du site actuel
Adresse, téléphones, heures, urgence 24 h, « plus de 40 ans d'expérience », entretien périodique personnalisé, trois avis clients (initiales telles qu'affichées), services.

## À confirmer ou à fournir avant publication
- Fourchettes de prix (FAQ) et mise à jour 2026 des trois guides de prix.
- Secteurs desservis (liste des villes), « appareils en inventaire ».
- Note moyenne et nombre d'avis (non inventés dans la maquette).
- Photos réelles de projets et de l'équipe.
- Adresses des 8 pages de services (proposition : `/thermopompe-joliette/`, `/climatiseur-mural-joliette/`, etc.) et redirections vers les URL existantes.
- Maintien des URL à forte valeur : `/`, `/carrieres/`, `/climatiseur-mural-air-climatise-thermopompe-joliette/` et les trois articles « prix ».
- Suivi : conserver les événements `call_tracking` et `form_submit` et les conversions Google Ads dans Google Tag Manager.
