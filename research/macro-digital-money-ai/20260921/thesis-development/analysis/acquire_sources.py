"""Public primary-source snapshots; failures retained, no login or bypass."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen
from datetime import datetime, timezone
import json, hashlib, sys
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
SOURCES={
'N01_coase.html':'https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x',
'N02_williamson.pdf':'https://www.nobelprize.org/uploads/2018/06/williamson_lecture.pdf',
'N03_holmstrom.pdf':'https://web.stanford.edu/~milgrom/publishedarticles/Multitask%20Principal%20Agent.pdf',
'N04_jcurve.pdf':'https://conference.nber.org/confer/2020/YSAIf20/EB2.pdf',
'N05_baumol.pdf':'https://karlshell.com/wp-content/uploads/2016/02/The-Transactions-Demand-for-Cash-An-Inventory-Theoretic-Approach.pdf',
'N06_teece.pdf':'https://www.edegan.com/pdfs/Teece%20%281986%29%20-%20Profiting%20From%20Technological%20Innovation%20Implications%20For%20Integration%20Collaboration%20Licensing%20And%20Public%20Policy.pdf',
'N07_invoicing.pdf':'https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025178-source-pdf.pdf',
'N08_bis170.pdf':'https://www.bis.org/publications/paper-170-impact-stablecoins-international-monetary-and-financial-system.pdf',
'N09_fed_payments.html':'https://www.federalreserve.gov/econres/notes/feds-notes/payment-stablecoins-and-cross-border-payments-benefits-and-implications-for-monetary-policy-20260330.html',
'N10_fed_dollar.html':'https://www.federalreserve.gov/econres/notes/feds-notes/fifth-conference-on-the-international-roles-of-the-u-s-dollar-stablecoins-digital-payments-and-the-ir-of-the-usd-20260716.html',
'N11_jagged.pdf':'https://www.hbs.edu/ris/Publication%20Files/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf',
'N12_treasurydirect.html':'https://www.treasurydirect.gov/marketable-securities/understanding-pricing/',
'S08_bis2025.html':'https://www.bis.org/publications/aer-2025/next-generation-monetary-financial-system',
'N13_fastpayments.html':'https://www.bis.org/publications/quest-speed-payments',
'N14_baumol_tobin.pdf':'https://pages.stern.nyu.edu/~wbaumol/CommunicationTheOptimalCash.pdf',
}
raw=ROOT/'evidence/raw'; raw.mkdir(parents=True,exist_ok=True)
def fetch(item):
    name,url=item; record={'id':name.split('_')[0],'url':url,'accessed_utc':datetime.now(timezone.utc).isoformat()}
    try:
        with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 (public academic research)'}),timeout=35) as r:
            data=r.read(); record.update(final_url=r.url,content_type=r.headers.get('Content-Type'))
        if name.endswith('.pdf') and not data.startswith(b'%PDF'): raise ValueError('Not a PDF; not saved as source')
        target=raw/name; target.write_bytes(data)
        record.update(status='SNAPSHOT_ACQUIRED_NOT_AUTOMATICALLY_READ',path=str(target.relative_to(ROOT)).replace('\\','/'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        if name.endswith('.pdf'):
            pdf=PdfReader(target); pages=[f'\n=== PDF PAGE {i+1} ===\n'+p.extract_text() for i,p in enumerate(pdf.pages)]
            target.with_suffix('.txt').write_text('\n'.join(pages),encoding='utf-8',newline='\n'); record['pages']=len(pages)
    except Exception as e: record.update(status='ACCESS_FAILED',error=str(e))
    return record
if __name__=='__main__':
    selected={k:v for k,v in SOURCES.items() if not sys.argv[1:] or k.split('_')[0] in sys.argv[1:]}
    prior=ROOT/'evidence/DOWNLOAD_MANIFEST.json'
    records=json.loads(prior.read_text(encoding='utf-8')) if prior.exists() and sys.argv[1:] else []
    new_records=list(ThreadPoolExecutor(max_workers=6).map(fetch,selected.items()))
    records=[r for r in records if r['id'] not in {n['id'] for n in new_records}]+new_records
    (ROOT/'evidence/DOWNLOAD_MANIFEST.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    for r in new_records: print(r['id'],r['status'],r.get('pages'),r.get('error',''))
