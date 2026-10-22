import os
import shutil

src_dir = r'C:\Users\0120025-Z100\.gemini\antigravity-ide\brain\a3e97f15-97b9-4139-87a9-99685f0a833b'
scratch_dir = os.path.join(src_dir, 'scratch')
dest_dir = r'c:\Users\0120025-Z100\source\manage'
tools_dir = os.path.join(dest_dir, 'tools')

os.makedirs(tools_dir, exist_ok=True)

# 1. ドキュメント類のコピー
docs = [
    'skill_and_tech_stack_history.md',
    'skill_and_capability_map.md',
    'skill_capability_map.html'
]

for d in docs:
    s_path = os.path.join(src_dir, d)
    d_path = os.path.join(dest_dir, d)
    if os.path.exists(s_path):
        shutil.copy2(s_path, d_path)
        print(f"Copied Doc: {d} -> {d_path}")

# 2. ツール・スクリプト・データファイルのコピー
for item in os.listdir(scratch_dir):
    if item.endswith('.ps1') or item.endswith('.py') or item.endswith('.json'):
        s_item = os.path.join(scratch_dir, item)
        d_item = os.path.join(tools_dir, item)
        shutil.copy2(s_item, d_item)
        print(f"Copied Tool: {item} -> {d_item}")

# 3. tools用のREADME作成
readme_path = os.path.join(tools_dir, 'README.md')
readme_text = """# プロジェクト解析・スキルマッピング ツール集

このフォルダには、`\\project` フォルダ内の全プロジェクトを自動走査・解析し、月別技術スタックおよびケイパビリティマップを生成した各種スクリプトとデータが格納されています。

## 含まれるツール一覧

- **`analyze_projects.ps1`**: PowerShellによる各プロジェクトの作成日・更新日・Gitコミット履歴および設定ファイル走査スクリプト
- **`curate_stack.py`**: 自作ソースコード（node_modulesやvenv等を除く）を精査し、言語・フロントエンド・バックエンド・DB・AI/RPAスタックを判定するスクリプト
- **`accurate_monthly.py`**: Git初回コミット日および実ディレクトリ作成日に基づく着手月の精密判定スクリプト
- **`inspect_quick_and_core.py`**: Quickシリーズおよび主要プロジェクトのREADME・拡張子別ファイル数を詳細調査するスクリプト
- **`print_summary.py`**: 月別サマリーと新規習得技術をコマンドライン上に整形表示するスクリプト
- **`scan_summary.json` / `curated_analysis.json`**: 解析結果のスキャンデータ（JSON形式）

## 実行方法例
```powershell
# 月別サマリーの再表示
python print_summary.py

# プロジェクト再スキャン
python curate_stack.py
```
"""

with open(readme_path, 'w', encoding='utf-8') as rf:
    rf.write(readme_text)
print("Created README.md in tools")

print("\n=== Contents of manage ===")
for root, dirs, files in os.walk(dest_dir):
    level = root.replace(dest_dir, '').count(os.sep)
    indent = ' ' * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        print(f"{subindent}{f}")
