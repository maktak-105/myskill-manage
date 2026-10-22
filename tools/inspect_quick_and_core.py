import os
import glob

base_dir = r'c:\Users\0120025-Z100\source\project'
quick_projects = [d for d in os.listdir(base_dir) if d.startswith('Quick') or d in ['auto-window', 'Auto-X', 'seikan_2', 'chumonsho-2seikan', 'shisaku-system', 'shokaku-2026', 'ap-drill', 'shadowing-lab', 'jinji-db', 'myerp', 'myDB', 'udon-db', 'suuri-chat', 'SNS Management']]

for q in quick_projects:
    p_path = os.path.join(base_dir, q)
    # look for cpp, cs, py, ts, js, cmake, vcxproj, sln
    exts = {}
    for root, dirs, files in os.walk(p_path):
        if any(ignore in root for ignore in ['.git', 'node_modules', '.venv', 'bin', 'obj']):
            continue
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            exts[ext] = exts.get(ext, 0) + 1
    
    # Check README for 1 line description
    desc = ''
    for rm in ['README.md', 'README_jp.md', 'HISTORY_jp.md']:
        rf = os.path.join(p_path, rm)
        if os.path.exists(rf):
            try:
                with open(rf, 'r', encoding='utf-8', errors='ignore') as f_in:
                    for line in f_in:
                        line = line.strip()
                        if line and not line.startswith('#') and not line.startswith('[') and not line.startswith('!'):
                            desc = line[:80]
                            break
                    if desc: break
            except:
                pass

    top_exts = sorted(exts.items(), key=lambda x: x[1], reverse=True)[:6]
    top_ext_str = ', '.join([f"{k}:{v}" for k, v in top_exts if k])
    print(f"[{q}]")
    print(f"  Desc: {desc}")
    print(f"  Files: {top_ext_str}")
