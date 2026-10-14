# Image de marque Bédard (reçue le 2026-10-12)

Sources : `assets/brand/Bedard-Normes.pdf` (normes) et le LogoKit (PNG transparents dans `assets/brand/png/`, SVG dérivés dans `assets/brand/svg/`). Les jetons CSS sont dans `assets/brand/tokens.css`.

## Identité
- Nom visuel : **Bédard**. Signature : **Performance thermique**.
- Variantes : logo seul, logo + signature (vertical ou horizontal), symbole (deux paires d'arcs) avec ou sans nom, pastille « Bédard ».
- Versions : marine (fond clair), beige/blanc (fond marine ou foncé), noir.
- Le kit ne contient pas de SVG. Je les ai générés à partir des fichiers vectoriels Illustrator (`Bedard-LG-RBG.ai`), fond retiré : marine, beige et blanc.

## Couleurs
| Nom | HEX | Rôle proposé |
|---|---|---|
| Marine | `#003650` | Couleur principale, fonds foncés, titres |
| Bleu | `#006492` | Liens, boutons secondaires |
| Cyan | `#28B0D8` | Accents sur fond foncé, illustrations |
| Ciel | `#BBE4EB` | Fonds doux, zones d'information |
| Beige | `#E5E4D9` | Fond de page, sections alternées |
| Nuit | `#000014` | Texte très foncé, pied de page |
| Rouille | `#8A4D3A` | Accent chaud : boutons d'appel (soumission, urgence) |
| Dégradé | marine → bleu → cyan → ciel → beige | Bandeaux, héros |

Règle d'accessibilité : le cyan sur blanc ne passe pas (contraste 2,53). Cyan seulement sur marine ou nuit.

## Typographies
- **Mona Sans** (gratuite, Google Fonts) : texte courant.
- **Ballinger** (condensée grasse) : titres. Le client détient une licence achetée séparément (2026-10-12), donc auto-hébergement. À vérifier dans le contrat : droits d'usage web (@font-face), formats fournis (WOFF2 attendu), nombre de domaines et de pages vues. Une licence « poste de travail » seule (OTF/TTF) ne couvre généralement pas le web. Les fichiers de police ne vont jamais dans le dépôt (`.gitignore` en place) ; ils sont déposés sur le serveur du site. La maquette v2 contient un bloc `@font-face` commenté et `--font-titre` avec repli sur Mona Sans.
- Pour la vitesse et la conformité à la Loi 25, j'hébergerais Mona Sans sur le site plutôt que de passer par Google Fonts.

## Attention SEO : le changement de nom
Le site, Google et les annuaires connaissent l'entreprise comme « Entreprise De Réfrigération & Climatisation Claude Bédard (1995) Inc ». La marque devient « Bédard — Performance thermique ». Pour ne pas perdre en référencement local :
- Garder le nom légal dans le pied de page, la page de contact et les données structurées (`legalName`), et utiliser « Bédard » comme nom commercial (`name`).
- Mettre à jour la fiche Google Business Profile, Facebook, LinkedIn et les annuaires avec le même nom, la même adresse et le même numéro (cohérence NAP).
- Garder « Réfrigération & Climatisation » dans les titres de pages et les textes, parce que les gens cherchent ces mots, pas la signature.
- Mettre à jour le logo dans l'image de partage (og:image) et le favicon.

## Décision de nommage (recommandation, à confirmer avec le comptable ou l'avocat)

- **Nom public partout (Google, site, réseaux sociaux, annuaires, publicité, camions, soumissions) : « Bédard Performance thermique »**, écrit toujours de la même façon (sans tiret) pour garder le NAP cohérent.
- **Nom légal seulement là où l'identité juridique est requise** : ligne dans le pied de page et sur la page Contact (« Bédard Performance thermique est une marque de [nom légal exact du REQ] »), `legalName` dans les données structurées, contrats, factures, licence RBQ.
- **« Climatisation C. Bédard »** : ancien nom d'usage (visible chez Carrier). Pas de nom public; conservé comme `alternateName` et dans « anciennement » pendant 12 à 24 mois.
- **Données structurées** : `name` = « Bédard Performance thermique », `legalName` = nom légal copié exactement du Registraire des entreprises, `alternateName` = « Bédard », « Climatisation C. Bédard ».
- **Conditions** : déclarer le nom d'usage au Registraire des entreprises du Québec; vérifier l'obligation d'afficher le numéro de licence RBQ dans la publicité; changer d'abord enseigne, camions, factures, signature de courriel et site; puis le nom de la fiche Google (qui doit correspondre au nom réel affiché); puis les annuaires (Carrier, CAA-Québec, Pages Jaunes).
- Ne jamais ajouter de mots-clés dans le nom de la fiche Google (risque de suspension); les mots « climatisation », « chauffage » vont dans les catégories, services, titres de pages et description.
