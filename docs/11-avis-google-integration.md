# Brancher la fiche Google au site : note et avis à jour automatiquement

## Ce qui est possible
| Besoin | Faisable? | Comment |
|---|---|---|
| Note moyenne (ex. 4,7) et nombre d'avis (ex. 202) à jour partout sur le site | Oui | API Google Places (nouvelle version), champs `rating` et `userRatingCount` |
| Afficher quelques avis récents avec nom, étoiles, texte | Oui, mais limité à 5 avis | Même API (champ `reviews` : les 5 avis jugés les plus pertinents) |
| Afficher les 202 avis | Oui, avec un accès propriétaire | API du Profil d'entreprise (Business Profile API) : demande d'accès à Google, autorisation OAuth par le propriétaire de la fiche; ou service tiers qui s'en charge |
| « Temps réel » strict (chaque visite) | Non recommandé | Mise à jour une fois par jour (cache) suffit : un avis ajouté apparaît le lendemain; limite aussi les coûts et respecte les conditions de Google |

## Trois façons de le faire
1. **Plugin tout fait** (Trustindex, Elfsight, EmbedSocial, WP Review Slider Pro, etc.). Rapide : on colle l'identifiant de la fiche, le widget affiche note et avis. Inconvénients : abonnement mensuel pour la version complète, design peu personnalisable, scripts de tiers chargés chez le visiteur (poids, témoins, consentement Loi 25), et certains plugins ajoutent un balisage d'avis que Google n'accepte pas pour l'entreprise elle-même : le désactiver.
2. **Intégration sur mesure par l'agence (recommandée)** : un petit module WordPress appelle l'API Google côté serveur, garde le résultat en cache 24 h et le sert au site avec notre design (page Avis, accueil, pages de services). Aucun script de tiers chez le visiteur, donc plus rapide et plus simple pour la Loi 25.
3. **Mélange** : note et nombre d'avis par l'API (partout sur le site), mur d'avis par un plugin, jusqu'à ce que l'accès au Profil d'entreprise soit approuvé.

## Étapes (option 2)
1. **Identifiant de la fiche (Place ID)** : le trouver avec l'outil « Place ID Finder » de Google (la fiche est « Réfrigération Claude Bédard 1995 Inc. », Joliette). Le lien d'avis `g.page/r/…/review` ne contient pas le Place ID tel quel.
2. **Projet Google Cloud** : créer un projet au nom de l'entreprise (compte du propriétaire, pas celui de l'agence), activer la facturation (carte de crédit requise), activer « Places API (New) ».
3. **Clé d'API** : la créer et la restreindre (adresse IP du serveur ou domaine du site). Ne jamais la mettre dans le code visible de la page; elle reste côté serveur (WordPress).
4. **Module WordPress** : appel de « Place Details » avec seulement les champs voulus (`rating`, `userRatingCount`, `reviews`), mise en cache 24 h, valeur de secours (la dernière valeur connue) si l'appel échoue.
5. **Affichage** : codes courts (shortcodes) utilisables partout, par exemple `[bedard_note]` (4,7), `[bedard_nb_avis]` (202), `[bedard_avis limite=6]` (mur d'avis dans le design du site). Les maquettes affichent aujourd'hui « 4,7 sur 5 » et « plus de 200 avis Google » en texte fixe : ces valeurs deviennent les codes courts.
6. **Attribution** : afficher « Avis Google » avec un lien vers la fiche, comme l'exigent les conditions de Google.
7. **Option, pour tous les avis** : demander l'accès à l'API du Profil d'entreprise (formulaire de Google, quelques jours) et l'autorisation du propriétaire de la fiche.

## Règles à respecter
- Pas de balisage `AggregateRating` ni `Review` sur le site pour l'entreprise elle-même (avis « auto-déclarés » : pas d'étoiles dans Google, risque de balisage ignoré). Voir `07-arborescence.md`, section Page Avis.
- Ne pas modifier ni trier les avis pour mettre les meilleurs en haut sans le dire; afficher la vraie note de Google.
- Coût : l'appel Place Details (champs avis et note) est facturé par Google à l'usage; avec 1 à 2 appels par jour, le coût est négligeable. À confirmer sur la grille tarifaire de Google Maps Platform au moment de l'activation.
- Loi 25 : en appelant l'API côté serveur, rien n'est envoyé à Google depuis le navigateur du visiteur; avec un plugin à script, le bandeau de consentement doit le couvrir.

## Ce que j'ai besoin de toi
1. Qui est le propriétaire du compte Google de la fiche (pour le projet Google Cloud et l'accès au Profil d'entreprise)?
2. Une carte de crédit pour la facturation de Google Cloud (coût prévu très faible).
3. Choix : plugin tout fait (rapide) ou intégration sur mesure (recommandée).
