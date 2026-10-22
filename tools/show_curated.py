import json

with open(r'C:\Users\0120025-Z100\.gemini\antigravity-ide\brain\a3e97f15-97b9-4139-87a9-99685f0a833b\scratch\curated_analysis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    langs = ','.join(p['languages']) if p['languages'] else '-'
    fe = ','.join(p['frontend']) if p['frontend'] else '-'
    be = ','.join(p['backend']) if p['backend'] else '-'
    db = ','.join(p['database']) if p['database'] else '-'
    tools = ','.join(p['tools_infra']) if p['tools_infra'] else '-'
    print(f"{p['start_month']} | {p['name']:<20} | L: {langs:<15} | FE: {fe:<25} | BE: {be:<12} | DB: {db:<25} | Tools: {tools}")
