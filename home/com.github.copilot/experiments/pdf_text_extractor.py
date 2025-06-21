import os
from pathlib import Path
try:
    from PyPDF2 import PdfReader
except ImportError:
    print('Please install PyPDF2: pip install PyPDF2')
    exit(1)

INBOX = '/workspaces/21JUN25-research/inbox/'

def extract_pdf_text(pdf_path, out_txt_path):
    try:
        reader = PdfReader(pdf_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        with open(out_txt_path, 'w', encoding='utf-8') as f:
            f.write(text.strip())
        return True
    except Exception as e:
        print(f'Failed to extract {pdf_path}: {e}')
        return False

for root, dirs, files in os.walk(INBOX):
    for fname in files:
        if fname.lower().endswith('.pdf'):
            pdf_path = os.path.join(root, fname)
            out_txt_path = pdf_path + '.extracted.txt'
            if not Path(out_txt_path).exists():
                extract_pdf_text(pdf_path, out_txt_path)
