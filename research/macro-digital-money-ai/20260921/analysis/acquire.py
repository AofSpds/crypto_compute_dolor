"""Bounded public-source download, no keys/accounts/payments; run explicitly to refresh."""
import urllib.request, urllib.parse, json, hashlib, datetime, pathlib, concurrent.futures
ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / 'data' / 'raw'
SERIES = ['CBBTCUSD','SP500','NASDAQCOM','CPIAUCSL','DEXKOUS','DTWEXBGS','DGS3MO','DGS10','DFF','GOLDAMGBD228NLBM','KORCPIALLMINMEI']
URLS = {f'fred_{s}.csv':'https://fred.stlouisfed.org/graph/fredgraph.csv?'+urllib.parse.urlencode({'id':s,'cosd':'2015-01-01','coed':'2026-09-18'}) for s in SERIES}
def fetch(item):
    name,url=item
    record={'filename':name,'requested_url':url,'accessed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Public academic research (local analysis only)'})
        with urllib.request.urlopen(req,timeout=35) as response:
            blob=response.read(15000000)
            record.update(status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'))
        if len(blob)>=15000000: raise ValueError('15 MB bounded download limit reached')
        (RAW/name).write_bytes(blob)
        record.update(bytes=len(blob),sha256=hashlib.sha256(blob).hexdigest(),local_path='data/raw/'+name,access_status='DATA_ACQUIRED')
        if name.endswith('.csv') and (b'<html' in blob[:1000].lower() or b'<!doctype' in blob[:1000].lower()):
            record.update(access_status='INVALID_CONTENT_ACCESS_LIMITED',error='HTML challenge instead of CSV; not used in analysis')
    except Exception as exc: record.update(access_status='ACCESS_LIMITED',error=str(exc))
    return record
if __name__=='__main__':
    RAW.mkdir(parents=True,exist_ok=True)
    extra=ROOT/'analysis'/'download_urls.json'
    if extra.exists(): URLS.update(json.loads(extra.read_text(encoding='utf-8')))
    prior=RAW/'DOWNLOAD_MANIFEST.json'
    old=json.loads(prior.read_text(encoding='utf-8')) if prior.exists() else []
    done={r['filename'] for r in old}
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool: results=list(pool.map(fetch,[(k,v) for k,v in URLS.items() if k not in done]))
    results=old+results
    (RAW/'DOWNLOAD_MANIFEST.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    for r in results: print(r['filename'],r['access_status'],r.get('bytes',r.get('error')))
