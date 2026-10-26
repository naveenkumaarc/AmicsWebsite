"""Check the deployable site for broken local links, assets and HTML landmarks."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import re,sys
ROOT=Path(__file__).parent/'dist'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.h1=0;self.missing_alt=0;self.main=0;self.categories=0;self.gallery=0
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if t=='h1':self.h1+=1
  if t=='main':self.main+=1
  if t=='img' and not a.get('alt'):self.missing_alt+=1
  if t=='img' and 'category-image' in a.get('class',''):self.categories+=1
  if t=='button' and 'gallery-item' in a.get('class',''):self.gallery+=1
  for k in ['href','src','data-image']:
   if k in a:self.refs.append(a[k])
errors=[];pages={}
for path in ROOT.rglob('*.html'):
 p=Page();p.feed(path.read_text());pages[path.resolve()]=p
 if path.name=='404.html':continue
 if p.h1!=1:errors.append(f'{path}: expected one h1, found {p.h1}')
 if p.main!=1:errors.append(f'{path}: expected one main')
 # The initially empty lightbox alt is set by showPhoto() before the dialog opens.
 allowed_empty=1 if path==ROOT/'index.html' else 0
 if p.missing_alt>allowed_empty:errors.append(f'{path}: missing alt text')
 if len(p.ids)!=len(set(p.ids)):errors.append(f'{path}: duplicate HTML ids')
for path,p in pages.items():
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  target=(path.parent/unquote(u.path)).resolve() if u.path else path
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{path.relative_to(ROOT)}: missing {ref}')
  elif u.fragment and target.suffix=='.html' and unquote(u.fragment) not in pages[target].ids:errors.append(f'{path.relative_to(ROOT)}: broken anchor {ref}')
for css in ROOT.glob('*.css'):
 for ref in re.findall(r'url\([\"\']?([^\)\"\']+)',css.read_text()):
  if not urlsplit(ref).scheme and not (css.parent/ref).exists():errors.append(f'{css.name}: missing {ref}')
for slug in ['', 'about-us','services','solutions','products','contact-us']:
 path=ROOT/slug/'index.html'
 if not path.exists():errors.append(f'Missing page {slug}')
for slug in ['products','solutions']:
 path=(ROOT/slug/'index.html').resolve()
 if pages[path].categories!=7:errors.append(f'{slug}: expected seven category images')
if pages[(ROOT/'index.html').resolve()].gallery!=33:errors.append('Expected all 33 original gallery photographs')
if errors:print('\n'.join(errors));sys.exit(1)
print('PASS: six main pages, 14 category images, 33 gallery photos, local assets, navigation links and anchors.')
