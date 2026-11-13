import os
import json
import glob
from collections import defaultdict

with open(r'~\.gemini\antigravity-ide\brain\a3e97f15-97b9-4139-87a9-99685f0a833b\scratch\scan_summary.json', 'r', encoding='utf-8') as f:
    projects = json.load(f)

base_dir = r'~\source\project'

details = []

for p in projects:
    name = p['Name']
    p_path = os.path.join(base_dir, name)
    if not os.path.isdir(p_path):
        continue

    # 決定的な日付の選定
    dates = []
    if p.get('GitFirst'):
        dates.append(p['GitFirst'])
    if p.get('MinFileDate'):
        dates.append(p['MinFileDate'])
    if p.get('DirCreation'):
        dates.append(p['DirCreation'])
    
    dates = [d for d in dates if d and d.startswith('20')]
    earliest_date = min(dates) if dates else 'Unknown'
    start_month = earliest_date[:7] if earliest_date != 'Unknown' else 'Unknown'

    last_dates = []
    if p.get('GitLast'):
        last_dates.append(p['GitLast'])
    if p.get('MaxFileDate'):
        last_dates.append(p['MaxFileDate'])
    if p.get('DirLastWrite'):
        last_dates.append(p['DirLastWrite'])
    last_dates = [d for d in last_dates if d and d.startswith('20')]
    latest_date = max(last_dates) if last_dates else 'Unknown'
    last_month = latest_date[:7] if latest_date != 'Unknown' else 'Unknown'

    # ファイル走査してより詳細な技術スタックを特定
    found_langs = set()
    frontend = set()
    backend = set()
    database = set()
    tools_infra = set()

    # パッケージJSON
    pkg_file = os.path.join(p_path, 'package.json')
    if os.path.exists(pkg_file):
        try:
            with open(pkg_file, 'r', encoding='utf-8') as pf:
                pkg_data = json.load(pf)
                deps = {**pkg_data.get('dependencies', {}), **pkg_data.get('devDependencies', {})}
                for k in deps:
                    if 'react' in k: frontend.add('React')
                    if 'vue' in k: frontend.add('Vue')
                    if 'next' in k: frontend.add('Next.js')
                    if 'vite' in k: frontend.add('Vite')
                    if 'tailwind' in k: frontend.add('Tailwind CSS')
                    if 'electron' in k: frontend.add('Electron')
                    if 'express' in k: backend.add('Express')
                    if 'prisma' in k: database.add('Prisma')
                    if 'supabase' in k: database.add('Supabase')
                    if 'sqlite' in k: database.add('SQLite')
                    if 'mysql' in k: database.add('MySQL')
                    if 'pg' in k or 'postgres' in k: database.add('PostgreSQL')
                    if 'lucide' in k: frontend.add('Lucide Icons')
                    if 'radix' in k or 'shadcn' in k: frontend.add('Radix UI / shadcn')
                if any(k.endswith('.ts') or k.endswith('.tsx') for k in glob.glob(os.path.join(p_path, '**/*'), recursive=True)[:100]):
                    found_langs.add('TypeScript')
                else:
                    found_langs.add('JavaScript')
        except:
            pass

    # Python
    py_files = glob.glob(os.path.join(p_path, '**/*.py'), recursive=True)
    if py_files:
        found_langs.add('Python')
        # requirements or scan imports
        req_file = os.path.join(p_path, 'requirements.txt')
        req_text = ''
        if os.path.exists(req_file):
            try:
                with open(req_file, 'r', encoding='utf-8', errors='ignore') as rf:
                    req_text = rf.read().lower()
            except:
                pass
        
        # sample some py files
        for pyf in py_files[:15]:
            try:
                with open(pyf, 'r', encoding='utf-8', errors='ignore') as f_in:
                    req_text += ' ' + f_in.read(2000).lower()
            except:
                pass

        if 'fastapi' in req_text: backend.add('FastAPI')
        if 'flask' in req_text: backend.add('Flask')
        if 'django' in req_text: backend.add('Django')
        if 'streamlit' in req_text: frontend.add('Streamlit')
        if 'gradio' in req_text: frontend.add('Gradio')
        if 'playwright' in req_text: tools_infra.add('Playwright')
        if 'pywinauto' in req_text: tools_infra.add('pywinauto')
        if 'pywebview' in req_text: frontend.add('pywebview')
        if 'sqlite' in req_text or 'sqlite3' in req_text: database.add('SQLite')
        if 'supabase' in req_text: database.add('Supabase')
        if 'pandas' in req_text: tools_infra.add('Pandas')
        if 'openpyxl' in req_text or 'xlwings' in req_text: tools_infra.add('Excel操作(openpyxl/xlwings)')
        if 'openai' in req_text or 'anthropic' in req_text or 'google.genai' in req_text or 'gemini' in req_text:
            backend.add('LLM API (OpenAI/Claude/Gemini)')

    # C#
    cs_files = glob.glob(os.path.join(p_path, '**/*.cs'), recursive=True)
    if cs_files or p.get('HasCSharp') or p.get('Csprojs'):
        found_langs.add('C#')
        # check csproj
        for csproj in glob.glob(os.path.join(p_path, '**/*.csproj'), recursive=True):
            try:
                with open(csproj, 'r', encoding='utf-8', errors='ignore') as cf:
                    c_text = cf.read()
                    if 'UseWPF' in c_text or 'PresentationCore' in c_text:
                        frontend.add('WPF (Desktop)')
                    if 'UseWindowsForms' in c_text or 'System.Windows.Forms' in c_text:
                        frontend.add('WinForms (Desktop)')
                    if 'Microsoft.AspNetCore' in c_text:
                        backend.add('ASP.NET Core')
                    if 'Microsoft.Data.Sqlite' in c_text or 'System.Data.SQLite' in c_text:
                        database.add('SQLite')
                    if 'EntityFrameworkCore' in c_text:
                        database.add('Entity Framework Core')
                    if 'Dapper' in c_text:
                        database.add('Dapper')
            except:
                pass

    # C++
    cpp_files = glob.glob(os.path.join(p_path, '**/*.cpp'), recursive=True) + glob.glob(os.path.join(p_path, '**/*.hpp'), recursive=True)
    if cpp_files or p.get('HasCpp'):
        found_langs.add('C++')

    # DB files
    db_files = glob.glob(os.path.join(p_path, '**/*.db'), recursive=True) + glob.glob(os.path.join(p_path, '**/*.sqlite*'), recursive=True)
    if db_files:
        database.add('SQLite (ローカルDBファイル)')

    # HTML/CSS/JS native
    if glob.glob(os.path.join(p_path, '**/*.html'), recursive=True) and not frontend:
        frontend.add('HTML/CSS/Vanilla JS')

    # README or summary check for description
    readme_snippet = ''
    for r_name in ['README.md', 'readme.md', 'Readme.md', 'memo.md', 'spec.md']:
        rf = os.path.join(p_path, r_name)
        if os.path.exists(rf):
            try:
                with open(rf, 'r', encoding='utf-8', errors='ignore') as r_in:
                    readme_snippet = r_in.read(500).strip().replace('\n', ' ')
                    break
            except:
                pass

    details.append({
        'name': name,
        'start_month': start_month,
        'earliest_date': earliest_date,
        'last_month': last_month,
        'latest_date': latest_date,
        'commit_count': p.get('CommitCount', 0),
        'languages': sorted(list(found_langs)),
        'frontend': sorted(list(frontend)),
        'backend': sorted(list(backend)),
        'database': sorted(list(database)),
        'tools_infra': sorted(list(tools_infra)),
        'readme': readme_snippet[:200]
    })

details.sort(key=lambda x: (x['start_month'], x['earliest_date']))

with open(r'~\.gemini\antigravity-ide\brain\a3e97f15-97b9-4139-87a9-99685f0a833b\scratch\detailed_analysis.json', 'w', encoding='utf-8') as f_out:
    json.dump(details, f_out, ensure_ascii=False, indent=2)

print(f"Parsed {len(details)} projects successfully.")
