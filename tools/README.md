# プロジェクト解析・スキルマッピング ツール集

このフォルダには、`\project` フォルダ内の全プロジェクトを自動走査・解析し、月別技術スタックおよびケイパビリティマップを生成した各種スクリプトとデータが格納されています。

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
