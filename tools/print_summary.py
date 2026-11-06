import json
import os
from collections import defaultdict

curated_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'curated_analysis.json')
with open(curated_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"{'Month':<7} | {'Project Name':<22} | {'Languages':<20} | {'Frontend':<25} | {'Backend':<25} | {'DB':<20}")
print("-" * 130)

monthly_projects = defaultdict(list)
for p in data:
    m = p['start_month']
    monthly_projects[m].append(p)
    langs = ', '.join(p['languages']) if p['languages'] else '-'
    fe = ', '.join(p['frontend']) if p['frontend'] else '-'
    be = ', '.join(p['backend']) if p['backend'] else '-'
    db = ', '.join(p['database']) if p['database'] else '-'
    print(f"{m:<7} | {p['name']:<22} | {langs:<20} | {fe:<25} | {be:<25} | {db:<20}")

print("\n=== 月別プロジェクト数・新規導入技術 ===")
seen_tech = set()
for m in sorted(monthly_projects.keys()):
    projs = monthly_projects[m]
    new_tech = set()
    for p in projs:
        for t in p['languages'] + p['frontend'] + p['backend'] + p['database'] + p['tools_infra']:
            if t not in seen_tech:
                new_tech.add(t)
                seen_tech.add(t)
    proj_names = [p['name'] for p in projs]
    print(f"\n【{m}】({len(projs)}件): {', '.join(proj_names)}")
    if new_tech:
        print(f"  ★ 新規登場/習得スタック: {', '.join(sorted(new_tech))}")
