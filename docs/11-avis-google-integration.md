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

## Sans Google Cloud : solutions gratuites ou presque (ajout du 2026-11-14)

Le propriétaire de la fiche a accès au tableau de bord, mais l'accès **automatique** aux avis par code passe toujours par un projet Google Cloud (Places API ou Business Profile API). Sans Cloud :

| Solution | Coût | Mise à jour | Limites |
|---|---|---|---|
| **A. Valeurs centralisées, mises à jour à la main** : un champ « Note Google » et « Nombre d'avis » dans les réglages de WordPress, repris partout par des codes courts | Gratuit | Manuelle (5 minutes par mois, ou après un nouvel avis marquant) | Peut être en retard de quelques semaines; aucune dépendance externe, aucun consentement à ajouter |
| **B. Carte Google intégrée** (« Partager > Intégrer une carte » depuis Google Maps, sans clé) sur la page Contact | Gratuit | Automatique : la fiche s'affiche avec la note et le nombre d'avis | Ce n'est pas notre design; charge des ressources de Google (couvrir dans le bandeau de consentement Loi 25) |
| **C. Plugin avec version gratuite** (Trustindex, Elfsight, etc.) | Gratuit avec limites, payant pour la version complète | Automatique, avec une fréquence limitée dans la version gratuite | Nombre d'avis affichés, fréquence de mise à jour, mention du fournisseur et design limités selon l'offre du moment : vérifier les conditions avant de choisir; scripts de tiers (Loi 25) |
| **D. Places API dans le quota gratuit de Google** | Gratuit en pratique (le volume prévu est très inférieur au quota gratuit mensuel; à confirmer sur la grille de Google) | Automatique, 1 à 2 fois par jour | Exige quand même un compte Google Cloud avec une carte de crédit enregistrée; on peut plafonner le quota quotidien (ex. 5 appels) pour qu'aucun frais ne soit possible |

À éviter : extraire les avis de Google Maps par programme (« scraping »), contraire aux conditions de Google et fragile.

**Recommandation sans Cloud** : A + B maintenant (gratuit, sans risque, prêt au lancement), mur d'avis avec des citations choisies (avec l'accord du client ou en citant brièvement avec le lien vers la fiche), et passage à D si l'automatisation devient souhaitable.

## Vérification des offres gratuites (2026-11-14)

Besoin : gratuit + automatique + aucune mise à jour mensuelle.

- **Trustindex (plugin WordPress gratuit)** : limité à 10 avis par widget; importe les avis à la connexion, mais la synchronisation automatique est réservée à l'abonnement payant (le bouton « Télécharger les nouveaux avis » est manuel). Ne répond pas au besoin. Source : centre d'aide de Trustindex.
- **Elfsight (plan gratuit)** : 200 affichages du widget par mois, soit quelques jours de trafic. Inutilisable pour un site d'entreprise.
- **API Google Places** : chaque SKU « Enterprise » a 1 000 requêtes gratuites par mois (grille de Google Maps Platform). Avec 1 appel par jour (environ 30 par mois), la facture attendue est de 0 $. Exige un compte Google Cloud avec une carte enregistrée. Vérifier sur la grille officielle quels champs (note, nombre d'avis, texte des avis) relèvent de quel SKU avant l'activation.

**Conclusion** : la seule solution à la fois gratuite en pratique, automatique et sans entretien est l'API Places dans le quota gratuit. Il faut un compte Cloud (au nom de l'entreprise), mais on peut rendre tout frais impossible :
1. quota quotidien de l'API plafonné à 10 requêtes;
2. alerte de budget à 1 $;
3. clé restreinte au serveur du site;
4. module avec cache de 24 h et valeur de secours.

Variante sans compte Cloud pour l'entreprise : l'agence utilise son propre projet Google Cloud et sa clé pour le site de Bédard. Gratuit pour Bédard, mais dépendance envers l'agence (si le contrat prend fin, la clé disparaît) : à éviter sauf entente écrite.
