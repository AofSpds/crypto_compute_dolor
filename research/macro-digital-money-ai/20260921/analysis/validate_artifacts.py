"""Check provenance, references and selected substantive numeric identities; no network."""
from pathlib import Path
import json,hashlib,re,datetime
ROOT=Path(__file__).resolve().parents[1]
def read(name): return json.loads((ROOT/name).read_text(encoding='utf-8'))
src=[json.loads(x) for x in (ROOT/'SOURCES.jsonl').read_text(encoding='utf-8').splitlines()]
claims=[json.loads(x) for x in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
checks=[]
def ck(name,value):
 checks.append(dict(check=name,passed=bool(value)))
 if not value: raise AssertionError(name)
required=['REPORT.md','SOURCES.jsonl','CLAIMS.jsonl','ANALYSIS_AND_REVIEW.md','CHECKPOINT.md','RESEARCH_RETURN_PACKET.md']
ck('six_nonempty_deliverables',all((ROOT/p).stat().st_size>500 for p in required))
ck('32_original_questions_assessed',len(claims)==32 and {c['claim_id'] for c in claims}=={f'H{i:02}' for i in range(1,33)} and all(c['assessment']!='UNASSESSED' for c in claims))
ids={x['source_id'] for x in src};ck('unique_source_ids',len(ids)==len(src))
ck('claim_references_resolve',all(set(c['supporting_source_ids']+c['challenging_source_ids'])<=ids for c in claims))
ck('no_unread_source_as_support',all(next(x for x in src if x['source_id']==s)['read_depth']!='DISCOVERED' for c in claims for s in c['supporting_source_ids']))
ck('all_registered_local_sources_match_SHA',all(hashlib.sha256((ROOT/x['local_path']).read_bytes()).hexdigest()==x['sha256'] for x in src if 'local_path'in x))
ck('raw_downloads_match_SHA',all(hashlib.sha256((ROOT/x['local_path']).read_bytes()).hexdigest()==x['sha256'] for x in read('data/raw/DOWNLOAD_MANIFEST.json') if 'local_path'in x))
ck('gold_challenge_not_data',next(x for x in read('data/raw/DOWNLOAD_MANIFEST.json') if x['filename']=='gold_gld_stooq.csv')['access_status']=='INVALID_CONTENT_ACCESS_LIMITED')
ck('24_executed_analytic_checks',len(read('data/derived/CHECKS.json')['checks'])==24 and all(x['passed'] for x in read('data/derived/CHECKS.json')['checks']))
r=read('data/derived/RESULTS.json')
ck('T01_to_T08_actual_results',set(r)=={f'T{i:02}' for i in range(1,9)})
ck('2022_real_return_independent_identity',abs((1+r['T04']['annual_2022']['BTC_USD'])/(1+r['T04']['annual_2022']['CPI'])-1-r['T04']['annual_2022']['BTC_real_USD'])<1e-12)
ck('claim_counts_agree',read('data/derived/REGISTER_SUMMARY.json')['claim_count']==len(claims))
ck('return_timestamp_recorded','FINALIZE_TIMESTAMP' not in (ROOT/'RESEARCH_RETURN_PACKET.md').read_text(encoding='utf-8'))
broken=[]
for file in required:
 if not file.endswith('.md'):continue
 for target in re.findall(r'\]\(([^)]+)\)',(ROOT/file).read_text(encoding='utf-8')):
  if target.startswith(('https://','http://','#')):continue
  if not (ROOT/target).exists(): broken.append([file,target])
broken=[x for x in broken if x[1]!='data/derived/ARTIFACT_CHECKS.json']
ck('relative_artifact_links_exist',not broken)
result={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'review_status':'AUTHOR_SELF_REVIEW_ONLY','checks':checks,'broken_links':broken,'files':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in required},'scope':'Local references, byte identity and selected arithmetic; not independent research validation.'}
(ROOT/'data/derived/ARTIFACT_CHECKS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'artifact_checks_passed':len(checks),'source_records':len(src),'claims':len(claims)},ensure_ascii=False))
