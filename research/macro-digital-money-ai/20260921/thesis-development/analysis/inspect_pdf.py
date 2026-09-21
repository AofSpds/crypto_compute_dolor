from pathlib import Path
import sys
from pypdf import PdfReader
import pypdfium2 as pdfium

# Run: python inspect_pdf.py PATH text|image 1,2,3 (one-based PDF pages).
path=Path(sys.argv[1]); mode=sys.argv[2]; pages=[int(p)-1 for p in sys.argv[3].split(',')]
if mode=='text':
    pdf=PdfReader(path)
    for i in pages: print(f'=== PDF PAGE {i+1} ===\n'+pdf.pages[i].extract_text())
elif mode=='image':
    pdf=pdfium.PdfDocument(str(path))
    out=Path(__file__).resolve().parents[1]/'evidence/raw/inspection'; out.mkdir(parents=True,exist_ok=True)
    for i in pages:
        target=out/f'{path.stem}_p{i+1}.png'
        pdf[i].render(scale=1.6).to_pil().save(target)
        print(target)
else: raise ValueError(mode)
