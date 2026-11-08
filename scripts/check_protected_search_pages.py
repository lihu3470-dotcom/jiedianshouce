"""Fail when a prepared site changes a proven search landing page's core identity."""

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.h1 = ''
        self.canonical = []
        self.in_title = False
        self.in_h1 = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'title':
            self.in_title = True
        elif tag == 'h1':
            self.in_h1 = True
        elif tag == 'link' and values.get('rel') == 'canonical':
            self.canonical.append(values.get('href', ''))

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        elif tag == 'h1':
            self.in_h1 = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_h1:
            self.h1 += data


parser = argparse.ArgumentParser()
parser.add_argument('site_root', type=Path)
args = parser.parse_args()
root = args.site_root.resolve(strict=True)
manifest = json.loads((Path(__file__).resolve().parents[1] / 'docs/PROTECTED-SEARCH-PAGES.json').read_text(encoding='utf-8'))
issues = []
for item in manifest:
    path = item['path']
    if not path.startswith('/') or not path.endswith('/') or urlsplit(path).netloc:
        raise SystemExit(f'invalid protected path: {path}')
    file = root / path.lstrip('/') / 'index.html'
    if not file.is_file():
        issues.append(f'{path}: missing page')
        continue
    page = Page()
    page.feed(file.read_text(encoding='utf-8', errors='replace'))
    h1 = re.sub(r'\s+', ' ', page.h1).strip()
    if page.title.strip() != item['title']:
        issues.append(f'{path}: title changed')
    if h1 != item['h1']:
        issues.append(f'{path}: H1 changed')
    if page.canonical != ['https://jiedianshouce.com' + path]:
        issues.append(f'{path}: canonical changed')

print(json.dumps({'checked': len(manifest), 'issues': issues}, ensure_ascii=False))
if issues:
    raise SystemExit(1)
