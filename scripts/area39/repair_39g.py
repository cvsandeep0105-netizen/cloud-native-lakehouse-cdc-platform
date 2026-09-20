from pathlib import Path

p = Path(r".\scripts\area39\run_area39_final.py")
s = p.read_text(encoding="utf-8")

old = """r=run(['aws','s3api','list-objects-v2','--bucket',BUCKET,'--prefix','raw/olist/','--query','KeyCount','--output','text']);
    if r.returncode or int(r.stdout.strip() or 0)!=9:return False
    r=run(['aws','s3api','list-objects-v2','--bucket',BUCKET,'--prefix','bronze/olist/','--query','KeyCount','--output','text']);
    if r.returncode or int(r.stdout.strip() or 0)!=9:return False"""

new = """r=run(['aws','s3','ls',f's3://{BUCKET}/raw/olist/']);
    if r.returncode or len([x for x in r.stdout.splitlines() if x.strip()])!=9:return False
    r=run(['aws','s3','ls',f's3://{BUCKET}/bronze/olist/','--recursive']);
    if r.returncode or len([x for x in r.stdout.splitlines() if x.strip()])!=9:return False"""

if old not in s:
    raise SystemExit("TARGET BLOCK NOT FOUND - NO CHANGE MADE")

p.write_text(s.replace(old, new), encoding="utf-8")
print("39-G validator repair: PASS")
