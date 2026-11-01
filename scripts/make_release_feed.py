"""Verify one already-published APK and generate in-app update metadata."""
import argparse,hashlib,json,re,subprocess
from pathlib import Path
from urllib.parse import urlparse
PACKAGE='com.merzel.sealcluster'
CERT='7ea9f4081ba15186da97bc4db150d2b0719a3895970864fc5978ac6de1e9b289'
p=argparse.ArgumentParser();p.add_argument('--release',type=Path,required=True);p.add_argument('--directory',type=Path,required=True);p.add_argument('--aapt',required=True);p.add_argument('--apksigner',required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
r=json.loads(a.release.read_text());apks=list(a.directory.glob('*.apk'))
if r.get('isDraft') or r.get('isPrerelease') or len(apks)!=1:raise SystemExit('Exactly one APK in a published stable-channel release is required')
f=apks[0]
if not 0<f.stat().st_size<=100*1024*1024:raise SystemExit('APK size outside allowed range')
badging=subprocess.check_output([a.aapt,'dump','badging',str(f)],text=True)
m=re.search(r"package: name='([^']+)' versionCode='(\d+)' versionName='([^']+)'",badging)
if not m or m[1]!=PACKAGE:raise SystemExit('Wrong package or unreadable APK metadata')
code=int(m[2]);name=m[3]
minimum=re.search(r"sdkVersion:'(\d+)'",badging)
if not minimum:raise SystemExit('Missing minimum SDK')
verification=subprocess.check_output([a.apksigner,'verify','--print-certs',str(f)],text=True)
certs=re.findall(r'Signer #\d+ certificate SHA-256 digest: ([a-fA-F0-9]+)',verification)
if [c.lower() for c in certs]!=[CERT]:raise SystemExit('APK signing certificate differs from the distributed application')
assets=[x for x in r.get('assets',[]) if x.get('name')==f.name]
if len(assets)!=1:raise SystemExit('Published APK asset not found')
url=assets[0].get('url','');u=urlparse(url)
if u.scheme!='https' or u.hostname!='github.com' or u.username:raise SystemExit('Unexpected asset URL')
notes=r.get('body','') or ''
if code<=0 or len(name)>100 or len(notes)>16000:raise SystemExit('Release metadata too long or invalid')
feed=dict(packageName=PACKAGE,versionCode=code,versionName=name,minSdk=int(minimum[1]),apkUrl=url,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),notes=notes)
a.output.write_text(json.dumps(feed,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Verified package, version, APK signature and SHA-256:',code,name)
