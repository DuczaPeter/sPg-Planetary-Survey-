#!/usr/bin/env python3
"""Verify every image occurrence, JS syntax and lossless reconstruction of V10.
Requires Python 3 and Node.js. No third-party Python packages or network access.
"""
import argparse, base64, hashlib, re, struct, subprocess, tempfile, zlib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / 'sPg_Nyx_I_V10_dokumentalt.html'
V10 = '068b865c6327ab3000e3db41aad2fa5a286b5494bb434e0a78d5249277b5bd04'
V9 = 'e83152dd788a4aa5dd0505a3a3463fe8d37f245f0d0be13b7675bf0f6b67c55f'
START = b'<script type="text/plain" id="ai-ujraepitesi-dokumentacio">'
END = b'</script>'
URI = re.compile(rb'data:image/png;base64,[A-Za-z0-9+/=]+')

def require(condition, message):
    if not condition: raise ValueError(message)

def sha(data): return hashlib.sha256(data).hexdigest()

def validate_png(data):
    require(data.startswith(b'\x89PNG\r\n\x1a\n'), 'Invalid PNG signature')
    i=8; dimensions=None; idat=[]; done=False
    while i<len(data):
        require(i+12<=len(data), 'Truncated PNG chunk')
        n=struct.unpack_from('>I',data,i)[0]; tag=data[i+4:i+8]; end=i+12+n
        require(end<=len(data), 'Truncated PNG payload')
        payload=data[i+8:i+8+n]
        require(zlib.crc32(tag+payload)&0xffffffff==struct.unpack_from('>I',data,i+8+n)[0], 'Invalid PNG CRC')
        if tag==b'IHDR': dimensions=struct.unpack_from('>II',payload)
        if tag==b'IDAT': idat.append(payload)
        i=end
        if tag==b'IEND': done=True;break
    require(done and i==len(data) and dimensions and idat, 'Invalid PNG structure')
    zlib.decompress(b''.join(idat))
    return dimensions

def manifest(text):
    rows=re.findall(r'^IMG_(\d{2}) \| (.*?) \| (\d+)×(\d+) \| (.*?) \| (\d+) bájt \| SHA-256 ([0-9a-f]{64})$',text,re.M)
    require(len(rows)==18,'Embedded manifest must contain 18 occurrences')
    return rows

def external_manifest(path):
    rows=re.findall(r'^\| IMG_(\d{2}) \| `([^`]+)` \| (\d+)×(\d+) \| ([^|]+?) \| (\d+) \| `([0-9a-f]{64})` \|$',path.read_text(encoding='utf-8'),re.M)
    return rows

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,help='Write reconstructed V10 to a NEW file');args=ap.parse_args()
    raw=APP.read_bytes();require(sha(raw)==V10,'V10 baseline hash mismatch; do not overwrite the expected value to silence this check')
    require(raw.count(START)==1,'Documentation wrapper must be unique')
    a=raw.index(START);b=raw.index(END,a)+len(END);block=raw[a:b];doc=block[len(START):-len(END)].decode('utf-8');live=raw[:a]+raw[b:]
    require(sha(live)==V9,'Removing the exact documentation block did not restore V9')
    rows=manifest(doc)
    for language in ('en','hu'):
        require(external_manifest(ROOT/f'docs/IMAGES.{language}.md')==rows,f'{language} image manifest differs from embedded documentation')
    uris=URI.findall(live);require(len(uris)==len(rows),'Image occurrence count differs')
    # The exact original URI is retained, not regenerated from a possibly altered encoding.
    for i,(uri,row) in enumerate(zip(uris,rows),1):
        idx,name,w,h,fmt,size,digest=row
        require(int(idx)==i,'Image ordering changed');data=base64.b64decode(uri.split(b',',1)[1],validate=True)
        require(len(data)==int(size) and sha(data)==digest,f'IMG_{idx}: byte length/hash mismatch')
        require(validate_png(data)==(int(w),int(h)),f'IMG_{idx}: invalid PNG dimensions')
        print(f'PASS IMG_{idx} {name} {size} {digest}')
    begin=b'\nBEGIN_V9_TEMPLATE\n';end=b'\nEND_V9_TEMPLATE\n';require(block.count(begin)==block.count(end)==1,'Template delimiters invalid')
    template=block.split(begin,1)[1].split(end,1)[0]
    # Match only exact placeholders in the template, NEVER global replacement of the HTML or Base64.
    require(sorted(re.findall(rb'@@IMG_(\d{2})@@',template))==[f'{i:02}'.encode() for i in range(1,19)],'Template image placeholders invalid')
    require(template.count(b'@@SCRIPT_END@@')==1,'Script end placeholder invalid')
    rebuilt9=re.sub(rb'@@IMG_(\d{2})@@|@@SCRIPT_END@@',lambda m:uris[int(m.group(1))-1] if m.group(1) else END,template)
    require(rebuilt9==live and sha(rebuilt9)==V9,'V9 reconstruction mismatch')
    anchor=b'<meta charset="utf-8">';require(rebuilt9.count(anchor)==1,'Charset anchor not unique');pos=rebuilt9.index(anchor)+len(anchor)
    rebuilt10=rebuilt9[:pos]+block+rebuilt9[pos:];require(rebuilt10==raw and sha(rebuilt10)==V10,'V10 reconstruction mismatch')
    print('PASS exact V9 and V10 reconstruction; V10 SHA-256',V10)
    # Documentation is text/plain and has been removed. Only executable script is checked.
    scripts=re.findall(rb'<script>(.*?)</script>',live,re.S);require(len(scripts)==1,'Expected one executable script')
    with tempfile.TemporaryDirectory() as tmp:
        js=Path(tmp)/'app.js';js.write_bytes(scripts[0]);subprocess.run(['node','--check',str(js)],check=True)
    print('PASS JavaScript syntax')
    if args.output:
        with args.output.open('xb') as f:f.write(rebuilt10)
        print('Wrote reconstructed V10:',args.output)

if __name__=='__main__':main()
