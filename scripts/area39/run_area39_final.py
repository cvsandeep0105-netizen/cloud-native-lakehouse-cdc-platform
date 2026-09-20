import json,subprocess,sys,datetime
from pathlib import Path
ROOT=Path.cwd(); E=ROOT/'evidence'/'area-39'; E.mkdir(parents=True,exist_ok=True)
ACCOUNT='326130805409'; REGION='ap-south-1'; BUCKET='project02-lakehouse-cdc-dev-data-lake'; DB='project02-lakehouse-cdc-dev_catalog'; WG='project02-lakehouse-cdc-dev-athena'
def run(cmd):
    print('> '+' '.join(cmd)); r=subprocess.run(cmd,text=True,capture_output=True); print(r.stdout); print(r.stderr); return r
results={}
def stage(name,fn):
    print('\n===== '+name+' ====='); ok=fn(); results[name]=ok; print(name+': '+('PASS' if ok else 'FAIL')); return ok

def g():
    r=run(['aws','sts','get-caller-identity','--query','Account','--output','text']);
    if r.returncode or r.stdout.strip()!=ACCOUNT:return False
    r=run(['aws','s3api','head-bucket','--bucket',BUCKET]);
    if r.returncode:return False
    r=run(['aws','glue','get-database','--name',DB]);
    if r.returncode:return False
    r=run(['aws','athena','get-work-group','--work-group',WG]);
    if r.returncode:return False
    r=run(['aws','s3','ls',f's3://{BUCKET}/raw/olist/']);
    if r.returncode or len([x for x in r.stdout.splitlines() if x.strip()])!=9:return False
    r=run(['aws','s3','ls',f's3://{BUCKET}/bronze/olist/','--recursive']);
    if r.returncode or len([x for x in r.stdout.splitlines() if x.strip()])!=9:return False
    return True

def h():
    r=run(['terraform','-chdir=./infrastructure/terraform','plan','-no-color']);
    if r.returncode or 'No changes' not in r.stdout:return False
    r=run(['aws','kms','get-key-rotation-status','--key-id','a89963ae-348b-486b-aa26-71fd4ccee1d0','--query','KeyRotationEnabled','--output','text']);
    if r.returncode or r.stdout.strip().lower()!='true':return False
    r=run(['aws','s3api','get-public-access-block','--bucket',BUCKET]);
    return r.returncode==0

def i():
    inv={'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'account':ACCOUNT,'region':REGION,'bucket':BUCKET,'catalog_database':DB,'athena_workgroup':WG,'stages':results}
    (E/'area-39-deployment-evidence.json').write_text(json.dumps(inv,indent=2))
    return (E/'area-39-deployment-evidence.json').exists()

def j():
    ok=all(results.get(x,False) for x in ['39-G','39-H','39-I'])
    final={'area':'39','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'results':results,'status':'PASS / FROZEN' if ok else 'FAIL / NOT FROZEN'}
    (E/'area-39-final-integration.json').write_text(json.dumps(final,indent=2))
    (E/'area-39-acceptance-and-freeze.md').write_text('# Area 39 Acceptance\n\nStatus: '+final['status']+'\n\nAWS deployment validation, operational evidence and deployment evidence were executed by the controlled Area 39 runner.\n')
    return ok

if not stage('39-G',g):sys.exit(1)
if not stage('39-H',h):sys.exit(1)
if not stage('39-I',i):sys.exit(1)
if not stage('39-J',j):sys.exit(1)
print('\n===== AREA 39: PASS / FROZEN =====')
