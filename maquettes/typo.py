"""Typographie française : espaces insécables avant : ; ? ! et dans les guillemets, numéros de téléphone insécables.
S'applique seulement au texte visible (pas aux balises, scripts ni feuilles de style)."""
import re
_SPLIT = re.compile(r'(<script.*?</script>|<style.*?</style>|<!--.*?-->|<[^>]+>)', re.S)
_PHONE = re.compile(r'(?<![\d-])(1-\d{3}-\d{3}-\d{4}|\d{3}-\d{3}-\d{4})(?![\d-])')

def _txt(s):
    s = re.sub(r' ([:;?!])', ' \\1', s)
    s = s.replace('« ', '« ').replace(' »', ' »')
    s = _PHONE.sub(r'<span class="nw">\1</span>', s)
    return s

def typo(html):
    parts = _SPLIT.split(html)
    return ''.join(p if (i % 2) else _txt(p) for i, p in enumerate(parts))

def add_css(html):
    return html.replace('\n<style>', '\n<style>.nw{white-space:nowrap}', 1)
