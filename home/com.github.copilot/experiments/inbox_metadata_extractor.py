import os
import datetime
import yaml

INBOX = '/workspaces/21JUN25-research/inbox/'

def summarize_file(fpath):
    ext = os.path.splitext(fpath)[1].lower()
    try:
        if ext in ['.pdf']:
            return 'PDF file (no text summary)'
        elif ext in ['.sh', '.py', '.js', '.rb']:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and not line.startswith('"""') and not line.startswith("'''") and not line.startswith('//!') and not line.startswith('/*') and not line.startswith('//') and not line.startswith('/*') and not line.startswith('*/') and not line.startswith('#!'):
                        return f'Code: {line[:120]}'
            return 'Script file (no code summary found)'
        elif ext in ['.txt', '.md']:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        return line[:200]
            return 'Text/Markdown file (no summary found)'
        else:
            return f'File type {ext} (no summary logic)'
    except Exception as e:
        return f'Could not summarize: {e}'

for root, dirs, files in os.walk(INBOX):
    for fname in files:
        if fname.endswith('.metadata.yaml'):
            continue  # Skip already processed
        fpath = os.path.join(root, fname)
        meta = {
            'filename': fname,
            'path': fpath,
            'date_processed': str(datetime.datetime.now()),
            'type': fname.split('.')[-1],
            'summary': summarize_file(fpath)
        }
        with open(fpath + '.metadata.yaml', 'w') as f:
            yaml.dump(meta, f, allow_unicode=True)
