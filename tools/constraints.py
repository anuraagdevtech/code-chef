#!/usr/bin/env python3
"""
Recover a problem's constraints.

Modern problems expose them as problemComponents.constraints. Older ones only
have them inside the statement body (HTML or markdown) under a "Constraints"
heading, and a handful never publish them at all - those are listed by hand in
data/constraints_overrides.json.
"""
import html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_OV = None

# Headings that end the constraints block. Plurals matter: a bare "Subtask"
# will not match "###Subtasks", because \b fails before the trailing "s".
STOP = (r'Examples?|Inputs?|Outputs?|Samples?|Explanations?|Subtasks?|'
        r'Scoring|Notes?|Authors?|Testers?|Editorial|Clarification')


def overrides():
    global _OV
    if _OV is None:
        with open(os.path.join(ROOT, 'data', 'constraints_overrides.json')) as f:
            _OV = {k: v for k, v in json.load(f).items() if not k.startswith('_')}
    return _OV


def _text(h):
    """HTML -> rough markdown, keeping bare < and > that are comparisons."""
    h = re.sub(r'<aside.*?</aside>', '', h, flags=re.S | re.I)
    # Superscripts carry the magnitude: 10<sup>5</sup> must not flatten to 105.
    h = re.sub(r'<sup\b[^>]*>(.*?)</sup>', r'^\1', h, flags=re.S | re.I)
    h = re.sub(r'<sub\b[^>]*>(.*?)</sub>', r'_\1', h, flags=re.S | re.I)
    h = re.sub(r'<br\s*/?>', '\n', h, flags=re.I)
    h = re.sub(r'<li\b[^>]*>', '- ', h, flags=re.I)
    h = re.sub(r'</(?:p|li|ul|ol|h[1-6]|div|pre)>', '\n', h, flags=re.I)
    h = re.sub(r'</?(?:p|b|i|u|ul|ol|li|h[1-6]|pre|div|span|a|strong|em|code|'
               r'sub|sup|center|font|table|tr|td|th|tbody|img)\b[^>]*>', '', h, flags=re.I)
    return re.sub(r'\n{3,}', '\n\n', html.unescape(h))


def from_body(body):
    """Pull the Constraints section out of a statement body."""
    if not body:
        return ''
    t = _text(body.replace('\r\n', '\n'))
    m = re.search(rf'^\s*#*\s*\**\s*Constraints?\s*\**\s*$\n(.*?)(?=^\s*#*\s*\**\s*(?:{STOP})\b|\Z)',
                  t, flags=re.S | re.I | re.M)
    if not m:
        m = re.search(rf'Constraints?\s*:?\s*\n(.*?)(?=\n\s*(?:{STOP})\b|\Z)',
                      t, flags=re.S | re.I)
    if not m:
        return ''
    out = m.group(1).strip()
    out = re.sub(r'\n{2,}', '\n', out)          # the lists come out double spaced
    out = '\n'.join(ln.rstrip() for ln in out.splitlines() if ln.strip())
    return out.strip()


def resolve(raw, code):
    """Best available constraints text for a problem payload."""
    pc = raw.get('problemComponents') or {}
    direct = (pc.get('constraints') or '').strip()
    if direct:
        return direct.replace('\r\n', '\n')
    found = from_body(raw.get('body') or '')
    if found:
        return found
    return overrides().get(code, '')


if __name__ == '__main__':
    codes = open(os.path.join(ROOT, 'data', 'all_solved.txt')).read().split()
    missing = []
    for c in codes:
        raw = json.load(open(os.path.join(ROOT, 'data', 'raw', f'{c}.json')))
        if not resolve(raw, c):
            missing.append(c)
    print(f'constraints resolved for {len(codes) - len(missing)} / {len(codes)}')
    if missing:
        print('still missing:', ' '.join(missing))
