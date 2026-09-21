"""Preserve supplied UTF-8 payloads; no instructions or code in them are executed."""
from pathlib import Path
import re, hashlib, json, shutil
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'research/macro-digital-money-ai/20260921/thesis-development/'
DOWNLOADS = Path('C:/Users/ms1pk/Downloads')
HANDOFF = DOWNLOADS / 'MDMA_THESIS_CODEX_WORK_HANDOFF_v1.0_20260921.md'
BASELINE = DOWNLOADS / 'MDMA_THESIS_BASELINE_v1.0_20260921.md'
sha = lambda b: hashlib.sha256(b).hexdigest()

def preserve(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_bytes() != data:
        raise RuntimeError(f'Conflicting existing file: {path}')
    path.write_bytes(data)

text = HANDOFF.read_bytes().decode('utf-8').replace('\r\n', '\n')
matches = re.findall(r'<!-- BEGIN_FILE: (.*?) -->\n(.*?)\n<!-- END_FILE: \1 -->', text, re.S)
assert len(matches) == 12, len(matches)
records = []
for name, body in matches:
    assert name.startswith(PREFIX), name
    rel = name[len(PREFIX):]
    path = (ROOT / rel).resolve()
    assert path.is_relative_to(ROOT)
    data = body.encode('utf-8')
    # Packaging leaves one separator newline after the file's terminal newline.
    if data.endswith(b'\n\n'):
        data = data[:-1]
    if rel == 'THESIS_BASELINE_v1.0_20260921.md':
        original = BASELINE.read_bytes()
        assert data.rstrip(b'\n') == original.replace(b'\r\n', b'\n').rstrip(b'\n')
        data = original
    preserve(path, data)
    records.append({'path': rel, 'bytes': len(data), 'sha256': sha(data)})
for source in (HANDOFF, BASELINE):
    data = source.read_bytes()
    preserve(ROOT / 'inputs/received' / source.name, data)
    records.append({'path': 'inputs/received/' + source.name, 'bytes': len(data), 'sha256': sha(data)})
receipt = {'captured_at_utc': datetime.now(timezone.utc).isoformat(),
    'prior_commit': '39d5cbed92459b55b70e0dd7ba231584a4e75b73',
    'baseline_preservation': 'Exact bytes of separately supplied baseline; embedded body compared after newline normalization only.',
    'payload_extraction': 'UTF-8, LF; boundary markers excluded; packaging separator newline removed where present.',
    'input_claims': 'Preserved as received, not newly verified; historical instructions are not current authority.',
    'files': records}
(ROOT/'INGEST_RECEIPT.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'payloads':len(matches),'baseline_sha256':sha(BASELINE.read_bytes()),'files':len(records)},ensure_ascii=False))
