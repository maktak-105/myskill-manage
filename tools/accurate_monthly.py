import os
import json
import subprocess
from datetime import datetime

base_dir = r'c:\Users\0120025-Z100\source\project'

projects = []

for item in os.listdir(base_dir):
    p_path = os.path.join(base_dir, item)
    if not os.path.isdir(p_path) or item in ['.vscode', '_rules', '___appli-template']:
        continue
    
    # Git初回コミット取得
    first_commit = None
    last_commit = None
    commit_count = 0
    if os.path.exists(os.path.join(p_path, '.git')):
        res = subprocess.run(['git', '-C', p_path, 'log', '--reverse', '--format=%ad', '--date=format:%Y-%m-%d'], capture_output=True, text=True, errors='ignore')
        commits = res.stdout.strip().splitlines()
        if commits:
            first_commit = commits[0]
            last_commit = commits[-1]
            commit_count = len(commits)

    dir_stat = os.stat(p_path)
    dir_c_date = datetime.fromtimestamp(dir_stat.st_ctime).strftime('%Y-%m-%d')
    dir_m_date = datetime.fromtimestamp(dir_stat.st_mtime).strftime('%Y-%m-%d')

    # 最も信頼できる着手日
    actual_date = first_commit if first_commit else dir_c_date
    actual_month = actual_date[:7]

    projects.append({
        'name': item,
        'actual_date': actual_date,
        'actual_month': actual_month,
        'last_date': last_commit if last_commit else dir_m_date,
        'commits': commit_count
    })

projects.sort(key=lambda x: (x['actual_month'], x['actual_date']))

for p in projects:
    print(f"{p['actual_month']} | {p['actual_date']} | {p['name']:<22} | commits: {p['commits']}")
