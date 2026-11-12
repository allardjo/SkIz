<?php
/**
 * Plugin Name: Bédard – Avis Google
 * Description: Affiche la note, le nombre d'avis et des avis de la fiche Google de Bédard (API Google Places, nouvelle version), avec cache de 24 h. À placer dans wp-content/mu-plugins/.
 * Version: 1.0.0
 *
 * Configuration (wp-config.php, JAMAIS dans le code d'une page ni dans le thème) :
 *   define('BEDARD_PLACES_API_KEY', '...');   // clé restreinte à l'adresse IP du serveur et à « Places API (New) »
 *   define('BEDARD_PLACE_ID', '...');         // identifiant de la fiche (Place ID)
 *   define('BEDARD_AVIS_MAX_APPELS_JOUR', 10); // facultatif : plafond de sécurité (10 par défaut)
 *
 * Codes courts : [bedard_note]  [bedard_nb_avis]  [bedard_note_texte]  [bedard_avis limite="6"]  (min_etoiles="1" par défaut : on affiche ce que Google retourne, sans trier)
 * Aucun balisage d'avis (AggregateRating / Review) n'est généré : volontaire (avis auto-déclarés).
 */
if (!defined('ABSPATH')) { exit; }

const BEDARD_AVIS_CACHE = 'bedard_avis_google';
const BEDARD_AVIS_SECOURS = 'bedard_avis_google_secours';

/** Retourne ['note'=>float, 'nb'=>int, 'avis'=>array, 'lien'=>string, 'secours'=>bool] ou null. */
function bedard_avis_donnees() {
    $cache = get_transient(BEDARD_AVIS_CACHE);
    if (is_array($cache)) { return $cache; }
    if (get_transient(BEDARD_AVIS_CACHE . '_echec')) { return bedard_avis_secours(); }

    if (!defined('BEDARD_PLACES_API_KEY') || !defined('BEDARD_PLACE_ID') || !BEDARD_PLACES_API_KEY || !BEDARD_PLACE_ID) {
        return bedard_avis_secours();
    }
    // plafond de sécurité : jamais plus de N appels par jour, quoi qu'il arrive (boucle, bogue, robot)
    $max = defined('BEDARD_AVIS_MAX_APPELS_JOUR') ? (int) BEDARD_AVIS_MAX_APPELS_JOUR : 10;
    $cle_jour = 'bedard_avis_appels_' . gmdate('Ymd');
    $n = (int) get_transient($cle_jour);
    if ($n >= $max) { return bedard_avis_secours(); }
    set_transient($cle_jour, $n + 1, DAY_IN_SECONDS);

    $url = 'https://places.googleapis.com/v1/places/' . rawurlencode(BEDARD_PLACE_ID) . '?languageCode=fr';
    $rep = wp_remote_get($url, [
        'timeout' => 8,
        'headers' => [
            'X-Goog-Api-Key'   => BEDARD_PLACES_API_KEY,
            'X-Goog-FieldMask' => 'rating,userRatingCount,googleMapsUri,reviews.rating,reviews.text,reviews.authorAttribution.displayName,reviews.relativePublishTimeDescription,reviews.publishTime',
        ],
    ]);
    $code = is_wp_error($rep) ? 0 : (int) wp_remote_retrieve_response_code($rep);
    $json = $code === 200 ? json_decode(wp_remote_retrieve_body($rep), true) : null;
    if (!is_array($json) || !isset($json['rating'])) {
        error_log('[Bédard avis Google] échec de l\'appel (code ' . $code . ')');   // la clé n'est jamais journalisée
        set_transient(BEDARD_AVIS_CACHE . '_echec', 1, HOUR_IN_SECONDS);              // pas de nouvel essai avant 1 h
        return bedard_avis_secours();
    }
    $avis = [];
    foreach ((array) ($json['reviews'] ?? []) as $r) {
        $avis[] = [
            'etoiles' => (int) ($r['rating'] ?? 0),
            'texte'   => (string) ($r['text']['text'] ?? ''),
            'auteur'  => (string) ($r['authorAttribution']['displayName'] ?? ''),
            'quand'   => (string) ($r['relativePublishTimeDescription'] ?? ''),
        ];
    }
    $data = [
        'note'    => (float) $json['rating'],
        'nb'      => (int) ($json['userRatingCount'] ?? 0),
        'avis'    => $avis,
        'lien'    => (string) ($json['googleMapsUri'] ?? ''),
        'secours' => false,
        'date'    => time(),
    ];
    set_transient(BEDARD_AVIS_CACHE, $data, DAY_IN_SECONDS);
    // valeur de secours : seulement la note et le nombre d'avis (jamais le texte des avis)
    update_option(BEDARD_AVIS_SECOURS, ['note' => $data['note'], 'nb' => $data['nb'], 'lien' => $data['lien'], 'date' => $data['date']], false);
    return $data;
}

function bedard_avis_secours() {
    $s = get_option(BEDARD_AVIS_SECOURS);
    return is_array($s) ? ['note' => (float) $s['note'], 'nb' => (int) $s['nb'], 'avis' => [], 'lien' => (string) ($s['lien'] ?? ''), 'secours' => true, 'date' => (int) ($s['date'] ?? 0)] : null;
}

function bedard_avis_fr($note) { return str_replace('.', ',', rtrim(rtrim(number_format((float) $note, 1, '.', ''), '0'), '.')); }

add_shortcode('bedard_note', function () {
    $d = bedard_avis_donnees(); return $d ? esc_html(bedard_avis_fr($d['note'])) : '';
});
add_shortcode('bedard_nb_avis', function () {
    $d = bedard_avis_donnees(); return $d ? esc_html((string) $d['nb']) : '';
});
add_shortcode('bedard_note_texte', function () {
    $d = bedard_avis_donnees();
    return $d ? esc_html(bedard_avis_fr($d['note']) . ' sur 5, ' . $d['nb'] . ' avis Google') : '';
});

const BEDARD_AVIS_ETOILE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/></svg>';

/** Mur d'avis, dans le design du site (classes .carte-avis et .etoiles des maquettes). */
add_shortcode('bedard_avis', function ($atts) {
    $a = shortcode_atts(['limite' => 6, 'min_etoiles' => 1], $atts, 'bedard_avis');
    $d = bedard_avis_donnees();
    if (!$d || empty($d['avis'])) { return ''; }
    $sortie = ''; $n = 0;
    foreach ($d['avis'] as $r) {
        if ($r['etoiles'] < (int) $a['min_etoiles'] || trim($r['texte']) === '') { continue; }
        if ($n++ >= (int) $a['limite']) { break; }
        $init = '';
        foreach (preg_split('/\s+/', trim($r['auteur'])) as $mot) { $init .= mb_strtoupper(mb_substr($mot, 0, 1)); }
        $init = mb_substr($init, 0, 2);
        $sortie .= '<figure class="carte-avis"><div class="etoiles" aria-label="' . (int) $r['etoiles'] . ' étoiles sur 5">'
                 . str_repeat(BEDARD_AVIS_ETOILE, max(0, min(5, (int) $r['etoiles']))) . '</div>'
                 . '<blockquote>« ' . esc_html(wp_strip_all_tags($r['texte'])) . ' »</blockquote>'
                 . '<cite><span class="av">' . esc_html($init) . '</span><div>' . esc_html($r['auteur'])
                 . '<span>Client, Google · ' . esc_html($r['quand']) . '</span></div></cite></figure>';
    }
    if ($sortie === '') { return ''; }
    $attrib = $d['lien'] ? '<p class="note-import">Avis publiés sur <a href="' . esc_url($d['lien']) . '" target="_blank" rel="noopener">Google</a>. Les cinq avis affichés sont choisis par Google.</p>' : '';
    return '<div class="mur-avis">' . $sortie . '</div>' . $attrib;
});
