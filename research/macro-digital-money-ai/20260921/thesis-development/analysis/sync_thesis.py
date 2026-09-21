"""Copy only this thesis subtree; refuse changes to preserved input bytes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

SOURCE=Path(__file__).resolve().parents[1]
REPO=Path('C:/Users/ms1pk/dev/rsch/crypto_compute_dolor').resolve()
DEST=(REPO/'research/macro-digital-money-ai/20260921/thesis-development').resolve()
assert DEST.is_relative_to(REPO) and SOURCE!=DEST
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
receipt=json.loads((SOURCE/'INGEST_RECEIPT.json').read_text(encoding='utf-8'))
for r in receipt['files']:
    assert sha(SOURCE/r['path'])==r['sha256'],r['path']
    assert (DEST/r['path']).exists() and sha(DEST/r['path'])==r['sha256'],r['path']
records=[]
for p in sorted(SOURCE.rglob('*')):
    if not p.is_file() or p.name=='SYNC_RECEIPT.json' or '__pycache__' in p.parts:continue
    assert not p.is_symlink()
    rel=p.relative_to(SOURCE);target=(DEST/rel).resolve();assert target.is_relative_to(DEST)
    target.parent.mkdir(parents=True,exist_ok=True)
    if not target.exists() or sha(target)!=sha(p):shutil.copyfile(p,target)
    assert sha(target)==sha(p)
    records.append({'path':str(rel).replace('\\','/'),'sha256':sha(p),'bytes':p.stat().st_size,'git_raw_excluded':rel.parts[:2]==('evidence','raw')})
report={'completed_utc':datetime.now(timezone.utc).isoformat(),'source':str(SOURCE),'destination':str(DEST),'protected_inputs_unchanged':True,'files':records}
for root in (SOURCE,DEST):
    (root/'analysis/SYNC_RECEIPT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'files_verified':len(records),'raw_files':sum(r['git_raw_excluded'] for r in records),'destination':str(DEST)},ensure_ascii=False))
