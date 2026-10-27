# Maquette de la page d'accueil

## Version 2 : `maquettes/accueil-v2.html`
Page autonome (images, logos et styles intégrés ; seule la police Mona Sans est chargée depuis Google Fonts, à héberger sur le site final). Source modifiable : `maquettes/source-accueil-v2.template.html`, images dans `maquettes/img/`, assemblage avec `maquettes/build_v2.py`.

### Positionnement
Retour du client sur la v1 : « site trop générique, on dirait une petite entreprise ». Or l'entreprise compte plus de 65 employés et se présente comme un chef de file régional. La v2 reprend ce positionnement : grande échelle typographique, photographie, chiffres de preuve, deux univers (résidentiel / commercial), section carrières.

### Structure
1. En-tête fixe transparent puis blanc au défilement, barre d'urgence 24 h, téléphone cliquable, bouton de soumission.
2. Hero : H1 SEO « Chauffage, climatisation et ventilation à Joliette », photo avec pastilles (urgence 24 h, note 4,9/5).
3. Barre de soumission rapide (3 champs) qui chevauche le hero.
4. Bande de chiffres animée : 65+ professionnels, 40+ ans, 4,9/5 (180+ avis), 24 h.
5. Deux univers : résidentiel et commercial.
6. Services en grille asymétrique (8 tuiles, dont l'urgence 24 h en rouille).
7. « Pourquoi Bédard » : la taille d'une grande entreprise, le soin d'une équipe locale.
8. Avis : note globale et trois avis réels du site.
9. Guides de prix (les trois articles qui génèrent 44 % des clics).
10. Carrières : « Rejoignez une équipe de plus de 65 professionnels » (postes réels vus sur jobcqc.ca).
11. Étapes, zone desservie, FAQ (données structurées `FAQPage`), appel final, pied de page.
Mobile : une colonne, barre fixe « Appeler / Soumission ».

### Grands écrans (correctif du 2026-10-13)
Retour du client (Mac, grand écran) : la mise en page était plafonnée à environ 1 240 px et flottait au centre. Correctif : conteneur fluide (largeur de l'écran moins des marges de 4 % à 5,5 rem, plafond à 120 rem), toutes les mesures converties de px en rem, et taille de base qui grandit de 16 px (écran de 1 440 px) à 24 px (écran de 2 560 px). La hauteur du hero s'adapte à la hauteur de la fenêtre pour que la barre de soumission reste visible. Testé à 1 440, 1 728 et 2 560 px de largeur.

### Marque
Marine, beige, rouille (boutons d'action uniquement), cyan sur fond foncé seulement, dégradé de marque en pied de page, symbole en filigrane, Mona Sans avec axe de largeur pour les titres (en attendant la licence web de Ballinger).

### Origine des chiffres
- 65+ professionnels et « chef de file régional » : déclarés par le client, à pouvoir justifier publiquement.
- 40+ ans : tiré du site actuel.
- Note et avis : la fiche Google affiche 4,7 sur 5 et 202 avis (relevé du 2026-10-27). Le site et les maquettes utilisent maintenant « 4,7 sur 5 » et « plus de 200 avis Google » (l'ancien « 4,9 / 180+ » venait de la page Avis du site actuel : 176 Google + 12 Facebook, moyenne 4,93).
- Postes : annonces réelles trouvées sur jobcqc.ca (frigoriste apprenti, ferblantier, dessinateur en ventilation).

### Images
Photos tirées de la médiathèque du site actuel (banque d'images : à confirmer que la licence couvre le nouveau site). À remplacer, quand possible, par de vraies photos de l'équipe, des camions, des installations et du bâtiment.

### À confirmer avant publication
- Fourchettes de prix (FAQ) et mise à jour 2026 des trois guides.
- Secteurs desservis, rôles de l'équipe, « appareils en inventaire ».
- Licence Adobe Fonts (Ballinger), hébergement local de Mona Sans.
- Suivi : conserver `call_tracking`, `form_submit` et les conversions Google Ads dans Google Tag Manager ; ajouter le consentement aux cookies (Loi 25).
- URL à conserver : `/`, `/carrieres/`, `/climatiseur-mural-air-climatise-thermopompe-joliette/` et les trois articles « prix ».

## Version 1 : `maquettes/accueil.html`
Première proposition, jugée trop générique. Conservée pour référence.
