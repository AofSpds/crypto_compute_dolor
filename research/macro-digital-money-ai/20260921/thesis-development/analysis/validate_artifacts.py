"""Scope/hash/link/unit artifact checks; not independent scientific review."""
from pathlib import Path
import hashlib, json, re, subprocess
ROOT=Path(__file__).resolve().parents[1]; OLD=ROOT.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def check(name,passed,detail=None):
    checks.append({'name':name,'passed':bool(passed),'detail':detail})
receipt=json.loads((ROOT/'INGEST_RECEIPT.json').read_text(encoding='utf-8'))
changed=[r['path'] for r in receipt['files'] if sha(ROOT/r['path'])!=r['sha256']]
check('all_14_received_inputs_unchanged',not changed,changed)
external=json.loads((ROOT/'inputs/external-review/MANIFEST.json').read_text(encoding='utf-8'))
external_diff=[r['path'] for r in external['files'] if sha(ROOT/'inputs/external-review'/r['path'])!=r['sha256']]
check('six_external_payloads_match_supplied_manifest',not external_diff,external_diff)
repo='C:/Users/ms1pk/dev/rsch/crypto_compute_dolor'
prefix='research/macro-digital-money-ai/20260921/thesis-development/'
git=['git','-c','safe.directory='+repo,'-C',repo]
blob=subprocess.check_output(git+['show','3cb224a839fcb3cd393a463824762fcdf0769eda:'+prefix+'THESIS_BASELINE_v1.0_20260921.md'])
check('baseline_git_commit_A_equals_attachment',hashlib.sha256(blob).hexdigest()==sha(ROOT/'THESIS_BASELINE_v1.0_20260921.md'))
local_missing=[]
docs=['THESIS_v1.1.md','ARGUMENT_EVIDENCE.md','RESEARCH_RETURN_PACKET.md']
for name in docs:
    p=ROOT/name
    if not p.exists(): local_missing.append(name);continue
    for link in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        if re.match(r'\w+://',link):continue
        if not (p.parent/link.split('#')[0]).exists():local_missing.append(name+':'+link)
check('required_documents_and_local_links_exist',not local_missing,local_missing)
text=(ROOT/'ARGUMENT_EVIDENCE.md').read_text(encoding='utf-8')
check('P01_to_P10_mapping_present',all(f'### P{i:02}' in text for i in range(1,11)))
thesis=(ROOT/'THESIS_v1.1.md').read_text(encoding='utf-8')
check('original_hold_ids_preserved',all(i in thesis for i in ['H10','H18','H23']))
calc=json.loads((ROOT/'analysis/results/RESULTS.json').read_text(encoding='utf-8'))
check('fifteen_calculation_checks_pass',calc['passed']==15 and all(c['passed'] for c in calc['checks']))
check('analysis_input_hash_matches',calc['input_sha256']==sha(ROOT/'analysis/inputs.json'))
patterns=[r'quarter cent',r'\$0\.25 per',r'\$1[–-]1\.25',r'\$2\.5 per',r'\$1[–-]1\.25 per']
hits=[]; searched=0
for p in OLD.rglob('*'):
    if not p.is_file() or p.is_relative_to(ROOT) or 'raw' in p.parts or p.suffix not in ('.md','.py','.json','.jsonl','.csv'):continue
    body=p.read_text(encoding='utf-8',errors='replace');searched+=1
    for pattern in patterns:
        if re.search(pattern,body,re.I):hits.append({'path':str(p.relative_to(OLD)).replace('\\','/'),'pattern':pattern})
check('no_footnote_dollar_phrasing_in_prior_outputs',not hits,{'searched_files':searched,'patterns':patterns,'hits':hits,'limit':'Exact/near-text search, not proof against all paraphrases. Raw source PDF/text excluded; thesis subtree excluded.'})
report={'review_status':'AUTHOR_SELF_REVIEW_ONLY','checks':checks,'passed':sum(c['passed'] for c in checks),'total':len(checks),'scope':'Artifact consistency; not independent review, causal identification or full regression reproduction.'}
(ROOT/'analysis/results/ARTIFACT_CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(report,ensure_ascii=False))
if not all(c['passed'] for c in checks):raise SystemExit(1)
