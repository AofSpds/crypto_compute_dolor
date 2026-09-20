"""Copy this research only to the user-connected repo; no deletion and no Git mutation."""
from pathlib import Path
import hashlib,json,shutil,datetime
SRC=Path(__file__).resolve().parents[1]
DEST=Path('C:/Users/ms1pk/dev/rsch/crypto_compute_dolor/research/macro-digital-money-ai/20260921')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
if __name__=='__main__':
    receipt=SRC/'analysis'/'SYNC_RECEIPT.json'
    old=json.loads(receipt.read_text(encoding='utf-8')) if receipt.exists() else {'files':{}}
    records={}; copied=0
    for p in SRC.rglob('*'):
        if not p.is_file() or p==receipt or '__pycache__' in p.parts: continue
        rel=p.relative_to(SRC).as_posix(); target=DEST/rel; h=sha(p)
        if target.exists() and sha(target) not in [h,old['files'].get(rel)]:
            raise RuntimeError('Destination changed outside this research writer: '+str(target))
        if not target.exists() or sha(target)!=h:
            target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,target); copied+=1
        assert sha(target)==h; records[rel]=h
    result={'synced_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':str(SRC),'destination':str(DEST),'files':records,'git_scope':'COPY_ONLY; see Git history and RESEARCH_RETURN_PACKET.md for commit state','remote_status':'NOT_CHECKED_BY_COPY_TOOL'}
    receipt.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    shutil.copy2(receipt,DEST/'analysis'/'SYNC_RECEIPT.json')
    print(json.dumps({'verified_files':len(records),'copied_or_updated':copied,'destination':str(DEST)},ensure_ascii=False))
