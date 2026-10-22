$srcDir = 'C:\Users\0120025-Z100\.gemini\antigravity-ide\brain\a3e97f15-97b9-4139-87a9-99685f0a833b'
$scratchDir = Join-Path $srcDir 'scratch'
$destDir = 'c:\Users\0120025-Z100\source\manage'
$toolsDir = Join-Path $destDir 'tools'

if (-not (Test-Path $toolsDir)) {
    New-Item -ItemType Directory -Path $toolsDir -Force | Out-Null
}

# 1. 文書ファイルのコピー
$docFiles = @(
    'skill_and_tech_stack_history.md',
    'skill_and_capability_map.md',
    'skill_capability_map.html'
)

foreach ($f in $docFiles) {
    $srcPath = Join-Path $srcDir $f
    $destPath = Join-Path $destDir $f
    if (Test-Path $srcPath) {
        Copy-Item -Path $srcPath -Destination $destPath -Force
        Write-Output "Copied Doc: $f -> $destPath"
    }
}

# 2. ツール・スクリプト・データファイルのコピー
$toolFiles = Get-ChildItem -Path $scratchDir -File | Where-Object { $_.Name -ne 'copy_to_manage.ps1' }

foreach ($tf in $toolFiles) {
    $destPath = Join-Path $toolsDir $tf.Name
    Copy-Item -Path $tf.FullName -Destination $destPath -Force
    Write-Output "Copied Tool: $($tf.Name) -> $destPath"
}

# 3. toolsディレクトリ用のREADME作成
$readmeContent = @"
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
"@

$readmePath = Join-Path $toolsDir 'README.md'
$readmeContent | Out-File -FilePath $readmePath -Encoding utf8

Write-Output "`n=== manageフォルダの配置状況 ==="
Get-ChildItem -Path $destDir | Select-Object Name, Length, LastWriteTime
Write-Output "`n=== toolsフォルダの配置状況 ==="
Get-ChildItem -Path $toolsDir | Select-Object Name, Length, LastWriteTime
