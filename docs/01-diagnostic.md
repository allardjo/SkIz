# Diagnostic du site cbedard.com

Date : 2026-10-12. Analyse faite à partir du code des pages publiques (accueil, soumission, services, contact, avis, blogue). Aucune mesure de vitesse réelle ni rendu visuel à ce stade.

## Entreprise
Entreprise de Réfrigération & Climatisation Claude Bédard (1995) Inc, Joliette (Lanaudière). Chauffage, climatisation, géothermie, qualité de l'air, planchers radiants, réfrigération commerciale, ferblanterie. Plus de 40 ans d'expérience, service d'urgence 24 h.

## Techno actuelle
- WordPress 7.0.7, PHP 8.3, LiteSpeed (cache)
- Thème Jupiter X + Elementor
- WooCommerce (boutique de filtres), WPML, Contact Form 7 + formulaires Elementor
- WP Review Slider Pro (avis), GDPR Cookie Compliance, Google Tag Manager
- SEO : Yoast (balises et sitemap de type Yoast)

## Constats vérifiés
1. Deux systèmes de formulaires : Contact Form 7 (page Soumission) et Elementor (page Contact).
2. Pages lourdes : accueil 400 Ko de HTML, pages de contenu ~200 Ko, Avis 680 Ko. WooCommerce, Elementor et le plugin d'avis chargent sur toutes les pages.
3. Titre SEO de l'accueil beaucoup trop long (nom légal + liste de services).
4. Données structurées : `Organization` générique seulement, pas de fiche locale (adresse, heures, zone desservie, téléphone).
5. Deux H1 sur l'accueil.
6. Message d'accueil générique ; urgence 24 h visible seulement dans le pied de page.
7. Menu d'environ 20 liens, répétés dans trois blocs de navigation.
8. Dates des avis au format américain (9/17/2026).
9. WPML installé, mais aucune balise hreflang trouvée (probablement inutilisé).

## À confirmer
- Vitesse mobile réelle (PageSpeed Insights / Core Web Vitals)
- Suivi des soumissions (courriels, Google Analytics / GTM)
- Rendu visuel et mobile (captures du propriétaire)

## Recommandation provisoire
Rester sur WordPress. Remplacer Jupiter X + Elementor par un thème sur mesure léger. Un seul tunnel de soumission. Ménage des plugins. Édition du contenu par blocs Gutenberg si l'équipe veut garder de l'autonomie.
