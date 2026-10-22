import os
import json
import glob
from collections import defaultdict
from datetime import datetime

base_dir = r'c:\Users\0120025-Z100\source\project'

def analyze_all():
    projects_data = []
    
    for item in os.listdir(base_dir):
        p_path = os.path.join(base_dir, item)
        if not os.path.isdir(p_path) or item in ['.vscode', '_rules', '___appli-template']:
            continue
        
        # 1. 日付取得 (Git最優先、次にコンテンツファイルの最古日時)
        git_first = None
        git_last = None
        commit_count = 0
        git_dir = os.path.join(p_path, '.git')
        if os.path.exists(git_dir):
            try:
                import subprocess
                cmd1 = ['git', '-C', p_path, 'log', '--reverse', '--format=%ad', '--date=format:%Y-%m-%d']
                res1 = subprocess.run(cmd1, capture_output=True, text=True, errors='ignore')
                lines = res1.stdout.strip().splitlines()
                if lines:
                    git_first = lines[0]
                    git_last = lines[-1]
                    commit_count = len(lines)
            except:
                pass
        
        # ファイルスキャン (除外: node_modules, .git, .venv, bin, obj, target)
        src_files = []
        ext_count = defaultdict(int)
        min_file_time = None
        max_file_time = None
        
        for root, dirs, files in os.walk(p_path):
            dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '.venv', 'venv', 'bin', 'obj', 'target', '.next', 'dist']]
            for f in files:
                full_f = os.path.join(root, f)
                ext = os.path.splitext(f)[1].lower()
                ext_count[ext] += 1
                src_files.append((f, full_f, ext))
                try:
                    c_time = os.path.getctime(full_f)
                    m_time = os.path.getmtime(full_f)
                    t = min(c_time, m_time)
                    if min_file_time is None or t < min_file_time:
                        min_file_time = t
                    t_max = max(c_time, m_time)
                    if max_file_time is None or t_max > max_file_time:
                        max_file_time = t_max
                except:
                    pass

        # 日付判定
        dates = []
        if git_first: dates.append(git_first)
        if min_file_time: dates.append(datetime.fromtimestamp(min_file_time).strftime('%Y-%m-%d'))
        
        start_date = min(dates) if dates else 'Unknown'
        start_month = start_date[:7] if start_date != 'Unknown' else 'Unknown'

        # 言語判定
        langs = set()
        if ext_count['.py'] > 0: langs.add('Python')
        if ext_count['.cpp'] > 0 or ext_count['.cxx'] > 0 or ext_count['.cc'] > 0 or ext_count['.hpp'] > 0 or ext_count['.h'] > 0:
            # 純粋なC/C++ソースがあるか
            if any(ext in ['.cpp', '.cxx', '.cc'] for _, _, ext in src_files):
                langs.add('C++')
        if ext_count['.cs'] > 0: langs.add('C#')
        if ext_count['.rs'] > 0 or os.path.exists(os.path.join(p_path, 'Cargo.toml')) or any('Cargo.toml' in f for f, _, _ in src_files):
            langs.add('Rust')
        if ext_count['.ts'] > 0 or ext_count['.tsx'] > 0: langs.add('TypeScript')
        if ext_count['.js'] > 0 or ext_count['.jsx'] > 0 or ext_count['.mjs'] > 0:
            if 'TypeScript' not in langs: langs.add('JavaScript')
        if ext_count['.gleam'] > 0 or os.path.exists(os.path.join(p_path, 'gleam.toml')): langs.add('Gleam')
        if ext_count['.ps1'] > 0 and len(langs) == 0: langs.add('PowerShell')
        if ext_count['.sql'] > 0: langs.add('SQL')

        # 技術スタック判定
        fe = set()
        be = set()
        db = set()
        tools = set()

        # パッケージやソースコード解析
        all_text_sample = ''
        for fname, fpath, ext in src_files[:40]:
            if ext in ['.json', '.toml', '.txt', '.py', '.cs', '.ts', '.tsx', '.cpp', '.h', '.qml', '.sql', '.md']:
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='ignore') as rf:
                        all_text_sample += ' ' + rf.read(1500)
                except:
                    pass

        # フロントエンド
        if 'react' in all_text_sample.lower(): fe.add('React')
        if 'next' in all_text_sample.lower() and ('next.config' in all_text_sample or '"next"' in all_text_sample): fe.add('Next.js')
        if 'vite' in all_text_sample.lower(): fe.add('Vite')
        if 'tailwind' in all_text_sample.lower(): fe.add('Tailwind CSS')
        if 'streamlit' in all_text_sample.lower(): fe.add('Streamlit')
        if 'pywebview' in all_text_sample.lower(): fe.add('pywebview (Desktop GUI)')
        if ext_count['.qml'] > 0 or 'Qt' in all_text_sample: fe.add('Qt 6 / QML (Desktop GUI)')
        if ext_count['.cs'] > 0:
            if 'winforms' in all_text_sample.lower() or 'system.windows.forms' in all_text_sample.lower(): fe.add('WinForms (Desktop)')
            if 'wpf' in all_text_sample.lower() or 'presentationcore' in all_text_sample.lower(): fe.add('WPF (Desktop)')
        if ext_count['.html'] > 0 and not fe:
            fe.add('HTML5/CSS3/Vanilla JS')

        # バックエンド
        if 'fastapi' in all_text_sample.lower(): be.add('FastAPI')
        if 'express' in all_text_sample.lower(): be.add('Express')
        if 'Rust' in langs: be.add('Rust Backend (Cargo)')
        if 'win32' in all_text_sample.lower() or 'windows.h' in all_text_sample.lower(): tools.add('Win32 API / Windows Native')

        # データベース
        if 'postgres' in all_text_sample.lower() or 'psycopg' in all_text_sample.lower(): db.add('PostgreSQL')
        if 'supabase' in all_text_sample.lower(): db.add('Supabase (PostgreSQL BaaS)')
        if 'sqlite' in all_text_sample.lower() or ext_count['.db'] > 0 or ext_count['.sqlite'] > 0 or ext_count['.sqlite3'] > 0: db.add('SQLite')
        if 'openpyxl' in all_text_sample.lower() or 'xlwings' in all_text_sample.lower() or ext_count['.xlsx'] > 0 or ext_count['.xlsm'] > 0:
            tools.add('Excel/VBA連携')

        # AI/LLM / 自動化
        if any(w in all_text_sample.lower() for w in ['openai', 'claude', 'gemini', 'google.genai', 'ollama', 'anthropic']):
            tools.add('LLM API (OpenAI/Claude/Gemini/Ollama)')
        if 'playwright' in all_text_sample.lower(): tools.add('Playwright (Web RPA)')
        if 'pywinauto' in all_text_sample.lower(): tools.add('pywinauto (Windows RPA)')
        if 'mcp' in all_text_sample.lower() or 'modelcontextprotocol' in all_text_sample.lower(): tools.add('MCP (Model Context Protocol)')

        # README description
        desc = ''
        for r_name in ['README_jp.md', 'README.md', 'readme.md']:
            rf = os.path.join(p_path, r_name)
            if os.path.exists(rf):
                try:
                    with open(rf, 'r', encoding='utf-8', errors='ignore') as r_in:
                        for line in r_in:
                            line = line.strip()
                            if line and not line.startswith('#') and not line.startswith('!') and not line.startswith('['):
                                desc = line[:100]
                                break
                    if desc: break
                except:
                    pass

        projects_data.append({
            'name': item,
            'start_month': start_month,
            'start_date': start_date,
            'commit_count': commit_count,
            'languages': sorted(list(langs)),
            'frontend': sorted(list(fe)),
            'backend': sorted(list(be)),
            'database': sorted(list(db)),
            'tools_infra': sorted(list(tools)),
            'desc': desc
        })

    projects_data.sort(key=lambda x: (x['start_month'], x['start_date']))
    with open(r'C:\Users\0120025-Z100\.gemini\antigravity-ide\brain\a3e97f15-97b9-4139-87a9-99685f0a833b\scratch\curated_analysis.json', 'w', encoding='utf-8') as cf:
        json.dump(projects_data, cf, ensure_ascii=False, indent=2)

analyze_all()
print("Curated analysis completed.")
