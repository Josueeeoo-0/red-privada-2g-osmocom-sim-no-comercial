"""Check generated local links without network access or extra dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
BASE = '/red-privada-2g-osmocom-sim-no-comercial/'

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('src', 'href') and value:
                self.links.append(value)

errors = []
pages = list(SITE.rglob('*.html'))
if not pages:
    sys.exit('ERROR: primero ejecutar python -m mkdocs build --strict')
checked = 0
for page in pages:
    parser = Links()
    parser.feed(page.read_text(encoding='utf-8'))
    for value in parser.links:
        url = urlsplit(value)
        if url.scheme or url.netloc or not url.path:
            continue
        path = unquote(url.path)
        if path.startswith(BASE):
            dest = SITE / path[len(BASE):]
        elif path.startswith('/'):
            dest = SITE / path.lstrip('/')
        else:
            dest = page.parent / path
        if dest.is_dir():
            dest = dest / 'index.html'
        if not dest.exists():
            errors.append(f'{page.relative_to(SITE)} -> {value}')
        checked += 1
for error in errors:
    print('ERROR:', error)
if errors:
    sys.exit(1)
print(f'OK: {len(pages)} HTML, {checked} enlaces locales comprobados.')
