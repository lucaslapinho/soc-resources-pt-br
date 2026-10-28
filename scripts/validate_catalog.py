"""Validação local, sem dependências externas ou acesso à rede."""
import csv
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parents[1]
resources = json.loads((root/'data/recursos.json').read_text(encoding='utf-8'))['recursos']
readme = (root/'README.md').read_text(encoding='utf-8')
assert len({r['id'] for r in resources}) == len(resources), 'IDs duplicados'
urls = set()
for resource in resources:
    for key in ['id','nome','categoria','tipo','fontes','finalidade','aplicacao','origem']:
        assert resource.get(key), (resource['id'],key)
    assert readme.count(f'**{resource["id"]}**') == 1, f'{resource["id"]} ausente ou repetido no README'
    for url in resource['fontes']:
        parsed = urlsplit(url)
        assert parsed.scheme == 'https' and parsed.hostname, url
        assert not parsed.username and not parsed.password, 'URL com credenciais'
        urls.add(url)
with (root/'data/recursos.csv').open(encoding='utf-8',newline='') as stream:
    rows = list(csv.DictReader(stream))
assert [r['id'] for r in rows] == [r['id'] for r in resources], 'CSV divergente'
checks = json.loads((root/'data/verificacao-links.json').read_text(encoding='utf-8'))
assert {r['url'] for r in checks} == urls, 'Registro de links divergente'
for document in root.rglob('*.md'):
    text = document.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)',text):
        if '://' in target or target.startswith('#'): continue
        path = unquote(target.split('#')[0])
        assert (document.parent/path).exists(), f'Link local quebrado: {document}: {target}'
    for soc_id in re.findall(r'SOC-\d{3}',text):
        assert soc_id in {r['id'] for r in resources}, f'ID desconhecido: {soc_id}'
print(f'OK: {len(resources)} entradas, {len(urls)} URLs, CSV e links locais consistentes.')
