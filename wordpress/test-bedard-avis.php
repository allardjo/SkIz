<?php
ini_set('error_log', '/dev/null');
// Test hors WordPress : php test-bedard-avis.php  (simule les fonctions de WordPress et la réponse de Google)
define('ABSPATH', __DIR__); define('DAY_IN_SECONDS', 86400); define('HOUR_IN_SECONDS', 3600);
$T = []; $O = []; $SC = []; $APPELS = 0; $MODE = 'ok'; $VU = null;
function get_transient($k) { global $T; return $T[$k] ?? false; }
function set_transient($k, $v, $t) { global $T; $T[$k] = $v; return true; }
function delete_all() { global $T; $T = []; }
function get_option($k) { global $O; return $O[$k] ?? false; }
function update_option($k, $v, $a = null) { global $O; $O[$k] = $v; return true; }
function add_shortcode($n, $f) { global $SC; $SC[$n] = $f; }
function shortcode_atts($d, $a, $n = '') { return array_merge($d, (array) $a); }
function esc_html($s) { return htmlspecialchars($s, ENT_QUOTES, 'UTF-8'); }
function esc_url($s) { return $s; }
function wp_strip_all_tags($s) { return strip_tags($s); }
function is_wp_error($r) { return $r === 'ERR'; }

function wp_remote_get($url, $args) {
    global $APPELS, $MODE, $VU; $APPELS++; $VU = [$url, $args];
    if ($MODE === 'echec') { return ['code' => 403, 'body' => '{"error":{}}']; }
    return ['code' => 200, 'body' => json_encode(['rating' => 4.7, 'userRatingCount' => 202, 'googleMapsUri' => 'https://maps.google.com/?cid=1',
        'reviews' => [
            ['rating' => 5, 'text' => ['text' => 'Service <b>très</b> courtois.'], 'authorAttribution' => ['displayName' => 'Martin Loyer'], 'relativePublishTimeDescription' => 'il y a 2 mois'],
            ['rating' => 2, 'text' => ['text' => 'Moyen.'], 'authorAttribution' => ['displayName' => 'A B'], 'relativePublishTimeDescription' => 'il y a 1 an'],
            ['rating' => 5, 'text' => ['text' => ''], 'authorAttribution' => ['displayName' => 'Sans Texte'], 'relativePublishTimeDescription' => 'hier'],
        ]])];
}
function wp_remote_retrieve_response_code($r) { return $r['code']; }
function wp_remote_retrieve_body($r) { return $r['body']; }
define('BEDARD_PLACES_API_KEY', 'CLE-DE-TEST'); define('BEDARD_PLACE_ID', 'PLACE123'); define('BEDARD_AVIS_MAX_APPELS_JOUR', 3);
require __DIR__ . '/bedard-avis-google.php';
function ok($c, $m) { echo ($c ? '  OK  ' : ' ÉCHEC') . ' ' . $m . "\n"; if (!$c) { $GLOBALS['ECHECS'] = ($GLOBALS['ECHECS'] ?? 0) + 1; } }

ok($SC['bedard_note']() === '4,7', 'note = 4,7');
ok($SC['bedard_nb_avis']() === '202', 'nombre d\'avis = 202');
ok($SC['bedard_note_texte']() === '4,7 sur 5, 202 avis Google', 'texte de la note');
ok($APPELS === 1, 'un seul appel à Google pour trois codes courts (cache) : ' . $APPELS);
ok(strpos($VU[0], 'places.googleapis.com/v1/places/PLACE123') !== false, 'URL de la nouvelle API Places');
ok(($VU[1]['headers']['X-Goog-FieldMask'] ?? '') !== '' && strpos($VU[1]['headers']['X-Goog-FieldMask'], 'rating') !== false, 'masque de champs envoyé (limite la facturation)');
$h = $SC['bedard_avis'](['limite' => 6, 'min_etoiles' => 4]);
ok(substr_count($h, '<figure class="carte-avis">') === 1, 'un seul avis affiché (2 étoiles et avis sans texte exclus)');
ok(strpos($h, '<b>') === false && strpos($h, 'Service très courtois.') !== false, 'HTML des avis retiré');
ok(strpos($h, 'MARTIN') === false && strpos($h, '>ML<') !== false, 'initiales ML');
ok(strpos($h, 'AggregateRating') === false, 'aucun balisage d\'avis');
// échec de l'API : valeur de secours (note et nombre seulement)
delete_all(); $MODE = 'echec'; $APPELS = 0;
ok($SC['bedard_note']() === '4,7' && $SC['bedard_nb_avis']() === '202', 'API en échec : valeur de secours (4,7 / 202)');
ok($SC['bedard_avis']([]) === '', 'API en échec : pas de texte d\'avis périmé');
$SC['bedard_note'](); $SC['bedard_note']();
ok($APPELS === 1, 'après un échec, pas de nouvel essai pendant 1 h : ' . $APPELS);
// plafond quotidien
delete_all(); $MODE = 'ok'; $APPELS = 0;
for ($i = 0; $i < 6; $i++) { global $T; unset($T[BEDARD_AVIS_CACHE]); $SC['bedard_note'](); }
ok($APPELS === 3, 'plafond de sécurité de 3 appels par jour respecté : ' . $APPELS);
echo ($GLOBALS['ECHECS'] ?? 0) ? "\n" . $GLOBALS['ECHECS'] . " échec(s)\n" : "\nTous les tests passent\n";
