# 🚀 Engineering Capability & Project Portfolio (manage)

本リポジトリは、ローカル環境（`c:\Users\0120025-Z100\source\` 等）における全開発プロジェクト（47+件）を自動走査・解析し、月別の技術スタック習得履歴、6大ケイパビリティ領域、および成果物マトリクスを一元管理・可視化するためのポートフォリオ基盤です。

---

## 📊 全体サマリー（2026年3月〜11月現在）

- **総開発プロジェクト数**: 47+ プロジェクト
- **駆使・習得言語**: 6+ 言語（Python, TypeScript, JavaScript, C++, C#, Rust, Gleam, PowerShell, SQL 等）
- **総 Git コミット数**: 1,400+ コミット
- **6大中核ケイパビリティ領域**:
  1. 🏢 **業務基盤DX・基幹内製化** (Excel脱却、EDI固定長パース、原価実績Fastify API、AD人事同期)
  2. 🌐 **自宅NAS・クラウド・公開Web** (QNAP NAS Docker、PostgreSQL 16、Cloudflare Tunnel/Access、Vercel/PWA)
  3. ⚡ **超高速C++/C#・低レイヤ** (Win32高速走査、Qt6/QML GPU描画、.NET 10 常駐ドック、C++高速移植)
  4. 💻 **モダンWeb・SaaS開発** (Next.js App Router、React、Tailwind CSS、Supabase BaaS)
  5. 🤖 **AIエージェント・先端技術** (自律AIループ Ralph Loop、Gemini/OpenAI API、MCPツール、Obsidian+Claude)
  6. 🚀 **脱商用RPA・ハイパー自動化** (Auto-X、pywinauto × Playwright ハイブリッド自動化)

---

## 📁 主要ファイル構成

| ファイル / フォルダ | 説明 |
| :--- | :--- |
| **[`skill_capability_map.html`](file:///c:/Users/0120025-Z100/source/manage/skill_capability_map.html)** | **統合Webダッシュボード**。全47プロジェクトの検索・ソート、月別成果物・技術マトリクス、ケイパビリティカード、時系列タイムラインを1画面で閲覧可能。 |
| **[`tech_acquisition_matrix.md`](file:///c:/Users/0120025-Z100/source/manage/tech_acquisition_matrix.md)** | **🛠️ 技術視点・時系列習得マップ**。言語・FW・ライブラリ・DB・インフラ・AIをいつ初めて導入したかの技術別進化表。 |
| **[`monthly_tech_matrix.md`](file:///c:/Users/0120025-Z100/source/manage/monthly_tech_matrix.md)** | **月別×カテゴリ別成果物マトリクス**。2026年3月〜11月の時系列で成果物（プロジェクト）と要素技術を整理。 |
| **[`skill_and_capability_map.md`](file:///c:/Users/0120025-Z100/source/manage/skill_and_capability_map.md)** | **6大ケイパビリティ領域レポート**。「できるようになったこと」と課題解決実績の体系表。 |
| **[`skill_and_tech_stack_history.md`](file:///c:/Users/0120025-Z100/source/manage/skill_and_tech_stack_history.md)** | **技術スタック層別マトリクス**。インフラ・言語・フロント・バックエンド・DBごとの詳細履歴。 |
| **[`tools/`](file:///c:/Users/0120025-Z100/source/manage/tools)** | 各プロジェクトのソースコード・Git履歴を解析するスクリプト＆スキャンデータ群。 |

---

## 🖥️ 使い方

### 1. 統合ダッシュボードの閲覧
ブラウザ（EdgeやChrome等）で直接 [`skill_capability_map.html`](file:///c:/Users/0120025-Z100/source/manage/skill_capability_map.html) を開くことで、すべての実績・マトリクス・全プロジェクト一覧をグラフィカルに検索・閲覧できます。

### 2. プロジェクトの再スキャン・最新化
新しいプロジェクトを追加した際や、コミットが進んだ際は以下のコマンドで最新状態を再集計できます：
```powershell
# プロジェクトの最新スキャン実行
python tools/curate_stack.py

# コマンドライン上での月別サマリー表示
python tools/print_summary.py
```

