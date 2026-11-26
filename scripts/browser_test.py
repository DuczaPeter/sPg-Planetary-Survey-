"""Exercise the unchanged application and capture actual browser screenshots."""
import os, sys, json, shutil
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
APP=ROOT/'sPg_Nyx_I_V10_dokumentalt.html'
OUT=ROOT/'docs/images'; OUT.mkdir(exist_ok=True)
R={}; errors=[]; requests=[]
known={'Savrilium':'balanced_01','Laranite':'semi_arid_01','Titanium':'semi_arid_01','Agricium':'semi_arid_01','Tin':'balanced_01','Copper':'arid_01','Aluminum':'arid_01'}
order=['Savrilium','Gold','Bexalite','Laranite','Aslarite','Titanium','Agricium','Torite','Hephaestanite','Tin','Quartz','Copper','Aluminum']
def record(k,v):
 R[k]=v; print(k,v,flush=True); (ROOT/'docs/browser-results.json').write_text(json.dumps(R,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
with sync_playwright() as pw:
 exe=os.environ.get('CHROME_PATH') or shutil.which('google-chrome') or shutil.which('chromium')
 b=pw.chromium.launch(executable_path=exe,headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 def fresh():
  p=b.new_page(viewport={'width':1820,'height':1050}); p.on('pageerror',lambda e:errors.append(str(e)));p.on('console',lambda e:errors.append(e.text[:180]) if e.type=='error' else None);p.on('request',lambda r:requests.append(r.url[:100]) if r.url.startswith(('http:','https:')) else None);return p
 p=fresh()
 try:
  p.goto(APP.as_uri(),wait_until='load',timeout=15000);p.wait_for_function("document.querySelector('#base')?.naturalWidth===8192",timeout=8000);record('local_file','PASS');method='file URI'
 except Exception as exc:
  record('local_file','BLOCKED/FAIL: '+str(exc).splitlines()[0][:220]);p.close();errors.clear();p=fresh();p.set_content(APP.read_text(encoding='utf-8'),wait_until='load',timeout=60000);method='set_content (unchanged full HTML)'
 record('browser',f'{Path(exe).name if exe else "Playwright Chromium"} {b.version}; {method}')
 def test(k,fn):
  try:fn();record(k,'PASS')
  except Exception as e:record(k,'FAIL: '+(str(e).splitlines() or [type(e).__name__])[0][:200])
 def check(f,e,src='surface',layer=None):
  p.wait_for_function("""([f,e])=>{let b=document.querySelector('#base'),a=[...document.querySelectorAll('#overlay img')],c=[...document.querySelectorAll('#outlines img')];return b.complete&&b.naturalWidth===8192&&b.naturalHeight===4096&&a.length===f&&c.length===e&&[...a,...c].every(i=>i.complete&&i.naturalWidth>0)}""",arg=[f,e],timeout=10000)
  assert p.evaluate(f'document.querySelector("#base").src==={src}');assert not p.locator('#status').inner_text().startswith('HIBA')
  if layer:assert p.locator('#overlay img').get_attribute('data-layer')==layer and p.locator('#outlines img').get_attribute('data-layer')==layer
  pixels=p.evaluate("""()=>[...document.querySelectorAll('#stage img')].map(i=>{let c=document.createElement('canvas');c.width=256;c.height=128;let x=c.getContext('2d');x.drawImage(i,0,0,256,128);let a=x.getImageData(0,0,256,128).data;let n=0;for(let j=3;j<a.length;j+=4)if(a[j])n++;return n})""");assert pixels[0]==32768 and all(n>0 for n in pixels[1:]),pixels
 def pick(n):p.locator(f'#picker button[data-ore="{n}"]').click(timeout=5000)
 def initial():
  check(3,0);assert p.locator('#picker button').count()==14 and p.locator('#layers .layer').count()==6
 def one(n):
  pick(n);f=int(n in known);check(f,f,layer=known.get(n));assert p.locator(f'#picker button[data-ore="{n}"]').get_attribute('aria-pressed')=='true'
 def shot(name):
  p.evaluate('window.scrollTo(0,0)');p.screenshot(path=str(OUT/(name+'.jpg')),type='jpeg',quality=85,timeout=15000)
 test('initial',initial)
 if R['initial']=='PASS':test('screenshot_initial',lambda:shot('initial'))
 for n in order:
  test('ore_'+n,lambda n=n:one(n))
  if n in ['Savrilium','Gold'] and R['ore_'+n]=='PASS':test('screenshot_'+n,lambda n=n:shot(n.lower()))
 def view(m,src):
  p.select_option('#mode',m);check(int(m=='estimate'),int(m=='estimate'),src,'arid_01' if m=='estimate' else None)
 for m,src in [('surface','surface'),('biome','biome'),('estimate','surface')]:
  test('view_'+m,lambda m=m,src=src:view(m,src))
  if R['view_'+m]=='PASS':test('screenshot_'+m,lambda m=m:shot(m))
 def switch():one('Savrilium');one('Gold');one('Copper');p.select_option('#mode','biome');one('Gold');assert p.locator('#mode').input_value()=='estimate'
 test('clear_and_gold',switch)
 def allpick():pick('');initial();p.locator('#layers button[data-ore="Copper"]').click();check(1,1,layer='arid_01')
 test('all_and_layer_button',allpick)
 def zoom(z):
  pick('Copper');p.eval_on_selector('#zoom',f"e=>{{e.value={z};e.dispatchEvent(new Event('input'))}}");check(1,1,layer='arid_01');assert p.locator('#stage').evaluate('e=>e.style.width')==f'{100*z}%'
 for z in [2,4,8,1]:
  test(f'zoom_{z}',lambda z=z:zoom(z))
  if z==2 and R['zoom_2']=='PASS':test('screenshot_zoom',lambda:shot('zoom'))
 def opacity():
  for v in [0,45,100]:
   p.eval_on_selector('#opacity',f"e=>{{e.value={v};e.dispatchEvent(new Event('input'))}}");assert float(p.locator('#overlay').evaluate('e=>getComputedStyle(e).opacity'))==v/100;assert p.locator('#outlines').evaluate('e=>getComputedStyle(e).opacity')=='1'
 test('opacity',opacity)
 def grid():
  p.locator('#gridon').uncheck();assert p.locator('#grid').evaluate('e=>getComputedStyle(e).display')=='none';p.locator('#gridon').check();assert p.locator('#grid').evaluate('e=>getComputedStyle(e).display')!='none'
 test('grid',grid)
 def drag():
  zoom(2);p.locator('#viewport').scroll_into_view_if_needed();r=p.locator('#viewport').bounding_box();x=r['x']+400;y=max(0,r['y'])+200;p.mouse.move(x,y);p.mouse.down();p.mouse.move(x-200,y-100,steps=5);p.mouse.up();assert p.locator('#viewport').evaluate('e=>e.scrollLeft')>0
 test('drag',drag)
 def coord():
  r=p.locator('#viewport').bounding_box();x=r['x']+400;y=max(0,r['y'])+200;p.mouse.move(x,y);before=p.locator('#coord').inner_text();p.mouse.move(x+100,y+50);assert p.locator('#coord').inner_text()!=before
 test('coordinates',coord)
 def regions():
  p.locator('details summary').click();assert p.locator('#regions p').count()==8 and p.locator('#regions').is_visible();p.locator('details summary').click();assert not p.locator('#regions').is_visible()
 test('regions',regions)
 def reset():
  p.locator('#reset').click();initial();assert p.locator('#viewport').evaluate('e=>e.scrollLeft===0&&e.scrollTop===0');assert p.locator('#mode').input_value()=='estimate' and p.locator('#zoom').input_value()=='1' and p.locator('#opacity').input_value()=='45' and p.locator('#gridon').is_checked()
 test('reset',reset)
 def mobile():
  p.set_viewport_size({'width':700,'height':950});assert p.locator('aside.panel').bounding_box()['y']<p.locator('section.panel').bounding_box()['y'];assert p.locator('main').evaluate('e=>getComputedStyle(e).gridTemplateColumns').count('px')==1
 test('mobile',mobile)
 record('console_errors',errors);record('external_requests',requests);b.close()
if any(str(v).startswith('FAIL') for v in R.values()) or errors or requests:sys.exit(1)
