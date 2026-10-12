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
- **Ballinger** (Adobe Fonts, condensée grasse) : titres. Il faut une licence Adobe Fonts qui couvre le web. À confirmer avec toi. Sinon, on utilise Mona Sans en graisse forte pour les titres.
- Pour la vitesse et la conformité à la Loi 25, j'hébergerais Mona Sans sur le site plutôt que de passer par Google Fonts.

## Attention SEO : le changement de nom
Le site, Google et les annuaires connaissent l'entreprise comme « Entreprise De Réfrigération & Climatisation Claude Bédard (1995) Inc ». La marque devient « Bédard — Performance thermique ». Pour ne pas perdre en référencement local :
- Garder le nom légal dans le pied de page, la page de contact et les données structurées (`legalName`), et utiliser « Bédard » comme nom commercial (`name`).
- Mettre à jour la fiche Google Business Profile, Facebook, LinkedIn et les annuaires avec le même nom, la même adresse et le même numéro (cohérence NAP).
- Garder « Réfrigération & Climatisation » dans les titres de pages et les textes, parce que les gens cherchent ces mots, pas la signature.
- Mettre à jour le logo dans l'image de partage (og:image) et le favicon.
