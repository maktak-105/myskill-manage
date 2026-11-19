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

## 更新手順（2026-11-19 時点の運用メモ）

- 公開用に `curate_stack.py` などの `base_dir` は伏せ字（`~\source\project`）になっています。実行時は **実パスへ書き換えた複製をリポジトリ外で実行**し、実パス版をコミットしないでください。
- スクリプトの出力は `name / start_month / start_date / commit_count / languages / frontend / backend / database / tools_infra / desc` のみです。公開用の `latest_date / display_month / desc_ja / desc_en` は手キュレーション項目なので、**既存の `curated_analysis.json` にマージ**して更新します（技術スタックの自動判定は先頭40ファイルのキーワード一致のため判定がぶれます。既存プロジェクトでは `commit_count` と `latest_date`（新しくなる場合のみ）を更新し、スタック欄は手キュレーション値を維持）。
- 新規プロジェクトの着手日は、ファイル時刻ではなく **Git 初回コミット日** を採用します（コピーでファイル時刻が実態より古くなるため）。
- 説明文は READMEの転記ではなく **中立表現で書き起こします**（社内サーバー名・DB名・アカウントID・個人ハンドル・社内組織名を含めない）。
- `index.html` の `rawProjects` は `json.dumps(curated_analysis.json, ensure_ascii=False)` と完全一致する埋め込みです。更新時は丸ごと再生成し、`skill_capability_map.html` は `index.html` と同一内容に保ちます。
