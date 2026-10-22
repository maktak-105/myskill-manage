# スキル・習得技術スタック 月別履歴＆層別マトリクス レポート

本レポートは、`\project` フォルダ内に存在する全43プロジェクトのソースコード、設定ファイル（`package.json`, `requirements.txt`, `Cargo.toml`, `*.csproj`, `CMakeLists.txt` 等）、Gitコミット履歴、ファイルタイムスタンプを詳細にスキャン・解析し、**2026年3月〜10月（本格開始の5月以降を中心とする約半年間）のスキル習得・開発履歴** を層別（言語、フロントエンド、バックエンド、データベース、AI/RPA/低レイヤ）に体系化したものです。

---

## 1. エグゼクティブ・サマリー（半年間の進化総括）

```mermaid
timeline
    title 2026年 スキル＆技術スタック習得タイムライン
    2026-03〜04 : 黎明期 : Python/FastAPI : 数理最適化 : Next.js/React : Supabase
    2026-05 : 本格始動期 : Qt/C++(Win32) : Vite/React : Gemini API : Quickシリーズ始動
    2026-06 : Web＆ネイティブ展開 : Next.jsフルスタック : Streamlit : PDF高速処理(C++)
    2026-07 : 業務DX＆大規模自動化 : 試作部内製化 : 大規模RPA(Auto-X) : MCPツール開発
    2026-08 : ネイティブ高速化深化 : C++ユーティリティ連作 : Qt6/QML画像処理 : 7-Zip連携
    2026-09 : 多様化＆先端スタック : C#(.NET10/WPF/WinForms) : pywinauto/Playwright : Gleam/Rust : ローカルLLM
    2026-10 : 基幹DX＆部内サーバー : 得意先固有EDI解析 : 部内PostgreSQLサーバー構築 : AD連携人事DB
```

> [!NOTE]
> **驚異的な成長スピードと技術的守備範囲**
> - **フロントエンド**: Next.js/ReactのモダンWebから、Streamlit、Qt 6 (QML)、C# (WPF/WinForms)、pywebview まで、Web・デスクトップ双方のGUIを網羅。
> - **低レイヤ・ネイティブ**: C++ による Win32 API 制御、NTFS MFT/ファイル走査の超高速化、PDFレンダリング移植、Rust によるバックエンド最適化。
> - **データ＆業務基盤**: Excel/VBAレガシー資産の脱却、PostgreSQL（クラウドSupabaseおよび部内オンプレサーバー）、EDI固定長電文パーサー、Active Directory連携。
> - **AI & RPA**: 単なるプロンプト利用にとどまらず、Gemini/OpenAI API連携、MCP (Model Context Protocol) ツール開発、pywinauto/Playwrightによるハイブリッド自動化、Ollama/Continue等のローカルLLM環境ハックまで到達。

---

## 2. 技術スタック層別マトリクス (Layered Tech Stack)

| レイヤ | 技術スタック・要素技術 | 該当プロジェクト / 主な用途 |
| :--- | :--- | :--- |
| **主要言語** | **Python** | [myerp](file:///c:/Users/0120025-Z100/source/project/myerp), [Auto-X](file:///c:/Users/0120025-Z100/source/project/Auto-X), [shisaku-system](file:///c:/Users/0120025-Z100/source/project/shisaku-system), [jinji-db](file:///c:/Users/0120025-Z100/source/project/jinji-db), [udon-db](file:///c:/Users/0120025-Z100/source/project/udon-db) など（バックエンド・データ処理・自動化の基幹） |
| | **C++** | [QuickImageView](file:///c:/Users/0120025-Z100/source/project/QuickImageView) (Qt 6), [QuickMarkPDF](file:///c:/Users/0120025-Z100/source/project/QuickMarkPDF), [QuickFolderSize](file:///c:/Users/0120025-Z100/source/project/QuickFolderSize), [QuickFileCopy](file:///c:/Users/0120025-Z100/source/project/QuickFileCopy), [QuickDiskRescue](file:///c:/Users/0120025-Z100/source/project/QuickDiskRescue)（高速I/O、Win32、メモリ・ポインタ制御） |
| | **C# (.NET 10)** | [QuickDock](file:///c:/Users/0120025-Z100/source/project/QuickDock)（Windowsデスクトップ常駐型ドッキングランチャー、WinForms / WPF） |
| | **TypeScript / JavaScript** | [myDB](file:///c:/Users/0120025-Z100/source/project/myDB), [suuri-chat](file:///c:/Users/0120025-Z100/source/project/suuri-chat), [SNS Management](file:///c:/Users/0120025-Z100/source/project/SNS%20Management), [FieldStyle2026](file:///c:/Users/0120025-Z100/source/project/FieldStyle2026) |
| | **Rust** | [myerp/erp-backend-rs](file:///c:/Users/0120025-Z100/source/project/myerp/erp-backend-rs)（数理最適化・計算集中型バックエンド） |
| | **Gleam** | [gleam](file:///c:/Users/0120025-Z100/source/project/gleam)（BEAM/Erlang仮想マシン上で動作する新世代型安全言語の検証） |
| | **PowerShell / Bash** | [bunai-server](file:///c:/Users/0120025-Z100/source/project/bunai-server), [project-LLM](file:///c:/Users/0120025-Z100/source/project/project-LLM)（サーバー自動構築・環境パッチ・プロビジョニング） |
| | **SQL** | PostgreSQL / SQLite 向け DDL, DML, パフォーマンスクエリ |
| **フロントエンド** | **React / Next.js (App Router)** | [myDB](file:///c:/Users/0120025-Z100/source/project/myDB), [suuri-chat](file:///c:/Users/0120025-Z100/source/project/suuri-chat), [SNS Management](file:///c:/Users/0120025-Z100/source/project/SNS%20Management)（Tailwind CSS, Lucide Icons, モダンUI） |
| | **Vite + React** | [FieldStyle2026](file:///c:/Users/0120025-Z100/source/project/FieldStyle2026), [jinji-db](file:///c:/Users/0120025-Z100/source/project/jinji-db)（高速ビルド・軽量SPA） |
| | **Qt 6 / QML** | [QuickImageView](file:///c:/Users/0120025-Z100/source/project/QuickImageView), [QuickFolderSize](file:///c:/Users/0120025-Z100/source/project/QuickFolderSize)（モダンデスクトップGUI、ハードウェアアクセラレーション） |
| | **WPF / WinForms** | [QuickDock](file:///c:/Users/0120025-Z100/source/project/QuickDock)（Windowsネイティブ枠なし半透明ドックUI、ドラッグ＆ドロップ） |
| | **pywebview / WebUI** | [auto-window](file:///c:/Users/0120025-Z100/source/project/auto-window), [QuickDiskBench](file:///c:/Users/0120025-Z100/source/project/QuickDiskBench)（HTML/CSS/JSを用いた軽量デスクトップUI） |
| | **Streamlit** | [udon-db](file:///c:/Users/0120025-Z100/source/project/udon-db)（データ探索・管理ダッシュボード） |
| **バックエンド** | **FastAPI** | [myerp](file:///c:/Users/0120025-Z100/source/project/myerp), [shisaku-system](file:///c:/Users/0120025-Z100/source/project/shisaku-system), [ap-drill](file:///c:/Users/0120025-Z100/source/project/ap-drill), [shadowing-lab](file:///c:/Users/0120025-Z100/source/project/shadowing-lab), [chumonsho-2seikan](file:///c:/Users/0120025-Z100/source/project/chumonsho-2seikan), [jinji-db](file:///c:/Users/0120025-Z100/source/project/jinji-db) |
| | **Rust Backend** | [myerp/erp-backend-rs](file:///c:/Users/0120025-Z100/source/project/myerp/erp-backend-rs) (Cargoベース) |
| | **Express (Node.js)** | [QuickDiskBench](file:///c:/Users/0120025-Z100/source/project/QuickDiskBench), [seikan_2](file:///c:/Users/0120025-Z100/source/project/seikan_2) 等のローカルAPIサーバー |
| **データベース** | **PostgreSQL** | [bunai-server](file:///c:/Users/0120025-Z100/source/project/bunai-server) (部内オンプレサーバー構築・運用), [jinji-db](file:///c:/Users/0120025-Z100/source/project/jinji-db), [chumonsho-2seikan](file:///c:/Users/0120025-Z100/source/project/chumonsho-2seikan), [shisaku-system](file:///c:/Users/0120025-Z100/source/project/shisaku-system) |
| | **Supabase (PostgreSQL BaaS)** | [myDB](file:///c:/Users/0120025-Z100/source/project/myDB), [udon-db](file:///c:/Users/0120025-Z100/source/project/udon-db), [ap-drill](file:///c:/Users/0120025-Z100/source/project/ap-drill), [shadowing-lab](file:///c:/Users/0120025-Z100/source/project/shadowing-lab)（Auth/RLS/クラウドDB連携） |
| | **SQLite** | [myerp](file:///c:/Users/0120025-Z100/source/project/myerp), [shadowing-lab](file:///c:/Users/0120025-Z100/source/project/shadowing-lab), 各種デスクトップツールローカルキャッシュ |
| | **Active Directory / LDAP** | [jinji-db](file:///c:/Users/0120025-Z100/source/project/jinji-db)（組織・人事・社員情報の自動取得・同期） |
| | **Excel / EDI電文** | [chumonsho-2seikan](file:///c:/Users/0120025-Z100/source/project/chumonsho-2seikan) (固定長バイナリ/S-JISパース), openpyxl/xlwings |
| **AI / RPA / 低レイヤ** | **LLM API & Agent** | Gemini API, OpenAI API, Claude API, Ollama, [suuri-chat](file:///c:/Users/0120025-Z100/source/project/suuri-chat), [shadowing-lab](file:///c:/Users/0120025-Z100/source/project/shadowing-lab) |
| | **MCP (Model Context Protocol)** | [fabric](file:///c:/Users/0120025-Z100/source/project/fabric) (Microsoft Fabric / OneLake Lakehouse連携MCPサーバー), [note](file:///c:/Users/0120025-Z100/source/project/note) |
| | **デスクトップ / Web RPA** | [auto-window](file:///c:/Users/0120025-Z100/source/project/auto-window) (pywinauto + Playwright), [Auto-X](file:///c:/Users/0120025-Z100/source/project/Auto-X) (170コミットの大規模自動化) |
| | **Windows Native / 低レイヤ** | Win32 API, NTFS走査, 非マウントドライブ直接アクセス ([QuickDiskRescue](file:///c:/Users/0120025-Z100/source/project/QuickDiskRescue)), 7-Zip DLL/CLI連携 ([Quick7Zip](file:///c:/Users/0120025-Z100/source/project/Quick7Zip)) |

---

## 3. 月別 習得技術・プロジェクト詳細履歴 (Monthly Timeline)

### 【2026年3月〜4月】黎明期：Webフルスタックと数理最適化の基礎確立
- **習得・活用技術**: Python, FastAPI, SQLite, 数理最適化（MILP / 設備負荷平準化）, Next.js, React, Tailwind CSS, Supabase, Google Gemini API
- **主要プロジェクト**:
  - [myerp](file:///c:/Users/0120025-Z100/source/project/myerp): 多階層BOM管理、設備負荷平準化、AIアシスタント搭載ERP。バックエンドにRust（`erp-backend-rs`）も導入。
  - [myDB](file:///c:/Users/0120025-Z100/source/project/myDB): Supabase + Next.js + Gemini AIチャットアシスタントによる自律型データベース管理。

---

### 【2026年5月】本格始動期：C++ネイティブ開発 ＆ Webツールの展開
- **習得・活用技術**: C++, Win32 API, Vite, React, Lucide Icons, メール自動化
- **主要プロジェクト**:
  - [FieldStyle2026](file:///c:/Users/0120025-Z100/source/project/FieldStyle2026): Vite + React によるイベント向けUI構築。
  - [QuickFolderSize](file:///c:/Users/0120025-Z100/source/project/QuickFolderSize): C++によるWindowsファイルシステム/フォルダサイズ高速算出ユーティリティ（「Quickシリーズ」の第1弾）。
  - [map_maker_cl](file:///c:/Users/0120025-Z100/source/project/map_maker_cl): Pythonによる地図・マップデータ生成。
  - [mail_manage](file:///c:/Users/0120025-Z100/source/project/mail_manage): FastAPI + Win32/Outlook連携によるメール管理・自動化。

---

### 【2026年6月】Web＆ネイティブ双方の本格展開とC++高速化
- **習得・活用技術**: C++（PythonからのC++高速化移植）, Streamlit, Next.js, PostgreSQL, AIエージェント設計
- **主要プロジェクト**:
  - [QuickMarkPDF](file:///c:/Users/0120025-Z100/source/project/QuickMarkPDF) (122コミット): PDF透かし・印影高速捺印ツール。PythonプロトタイプからC++へのポーティングを行い、ボトルネック解消と劇的な高速化を達成（`CPP_PORT_POSTMORTEM.md` に詳細記録）。
  - [suuri-chat](file:///c:/Users/0120025-Z100/source/project/suuri-chat): 数理的思考と詩的感性を併せ持つAI相談チャット（Next.js + Tailwind + LLM）。
  - [udon-db](file:///c:/Users/0120025-Z100/source/project/udon-db) (145コミット): Streamlit + Supabaseによる香川うどん店舗・記録データベース。
  - [SNS Management](file:///c:/Users/0120025-Z100/source/project/SNS%20Management): Next.js + PostgreSQL によるSNS運用管理システム。
  - [note](file:///c:/Users/0120025-Z100/source/project/note): note執筆・自動投稿ワークフロー。

---

### 【2026年7月】基幹業務DX化 ＆ 大規模RPA・MCPプロトコル
- **習得・活用技術**: Playwright, Microsoft Fabric / OneLake Lakehouse, MCP (Model Context Protocol), 大規模業務自動化
- **主要プロジェクト**:
  - [Auto-X](file:///c:/Users/0120025-Z100/source/project/Auto-X) (170コミット): 業務プロセスのフルオートメーションを実現する大規模自動化基盤。
  - [shisaku-system](file:///c:/Users/0120025-Z100/source/project/shisaku-system): 従来の「Excel＋VBAマクロ」による原価見積業務を、FastAPI + PostgreSQL + Web内製システムへ移行するDX基盤。
  - [fabric](file:///c:/Users/0120025-Z100/source/project/fabric): Microsoft Fabric / OneLake LakehouseをAIエージェントから操作するためのMCPツール開発。
  - [seikan_2](file:///c:/Users/0120025-Z100/source/project/seikan_2): 製缶・受発注業務DXシステム。

---

### 【2026年8月】「Quick」シリーズ（C++ / Qt 6 / 高速ネイティブGUI）の爆発期
- **習得・活用技術**: Qt 6, QML, CMake, C++, 7-Zip内部連携, Win32 I/O
- **主要プロジェクト**:
  - [QuickImageView](file:///c:/Users/0120025-Z100/source/project/QuickImageView): Qt 6 + QML + CMake + C++ による超軽量・高速画像ビューア＆編集ソフト。
  - [QuickFileCopy](file:///c:/Users/0120025-Z100/source/project/QuickFileCopy): Windows 10/11ネイティブ高速ファイルコピーツール（Win32バッファリング制御）。
  - [QuickDiskBench](file:///c:/Users/0120025-Z100/source/project/QuickDiskBench): ディスク速度ベンチマークツール（CrystalDiskMark風）。
  - [Quick7Zip](file:///c:/Users/0120025-Z100/source/project/Quick7Zip): 7-Zipエンジンを活用したモダンフロントエンド。

---

### 【2026年9月】多様化・先端スタック・C#デスクトップ・Windows RPA
- **習得・活用技術**: C# (.NET 10 / WPF / WinForms), pywebview, pywinauto, 音声・言語学習, Gleam言語, ローカルLLM環境ハック (Ollama/ComfyUI/Continue)
- **主要プロジェクト**:
  - [QuickDock](file:///c:/Users/0120025-Z100/source/project/QuickDock): **C# (.NET 10 / WinForms / WPF)** によるWindows枠なしフローティングドックランチャー。
  - [auto-window](file:///c:/Users/0120025-Z100/source/project/auto-window): pywinauto（Win32/UIAアプリ操作）＋ Playwright（Web自動化）＋ pywebview（デスクトップUI）による完全脱商用RPAの内製基盤。
  - [shadowing-lab](file:///c:/Users/0120025-Z100/source/project/shadowing-lab): 英語音声のリンキング・弱形学習Webアプリ（FastAPI + Supabase + LLM）。
  - [ap-drill](file:///c:/Users/0120025-Z100/source/project/ap-drill): 応用情報技術者（AP）試験対策ドリルシステム。
  - [mont-simu](file:///c:/Users/0120025-Z100/source/project/mont-simu) (205コミット): モンテカルロシミュレーション / 数理解析GUI。
  - [QuickDiskRescue](file:///c:/Users/0120025-Z100/source/project/QuickDiskRescue): Windowsがマウントできない破損ドライブからデータを直接抽出するC++レスキューツール。
  - [gleam](file:///c:/Users/0120025-Z100/source/project/gleam): 型安全な関数型言語Gleamの環境構築と検証。
  - [project-LLM](file:///c:/Users/0120025-Z100/source/project/project-LLM) / [LLM-manage](file:///c:/Users/0120025-Z100/source/project/LLM-manage): ローカルLLM（Ollama, ComfyUI, Continue VSCode拡張のCSS修正パッチ）環境の最適化・調査。

---

### 【2026年10月（現在）】実務EDI解析・社内PostgreSQLサーバー構築・本格基幹DX
- **習得・活用技術**: 得意先ユニーク調達EDI電文パース, オンプレPostgreSQLサーバー構築・運用（PowerShell）, Active Directory (AD) 連携, 人材育成体系
- **主要プロジェクト**:
  - [chumonsho-2seikan](file:///c:/Users/0120025-Z100/source/project/chumonsho-2seikan): 得意先ユニーク次世代調達EDI形式の固定長Shift_JIS電文を自動解析し、PostgreSQLへ正規化格納するミッションクリティカルなバッチ/Webシステム。
  - [bunai-server](file:///c:/Users/0120025-Z100/source/project/bunai-server): 部内専用PostgreSQLデータベースサーバーの自動構築スクリプト（PowerShell）、ロール/権限管理、Power Automate連携、IT部門向け申請手順の確立。
  - [jinji-db](file:///c:/Users/0120025-Z100/source/project/jinji-db): 従来のExcel VBA人事リストから脱却し、Active Directory (AD) から自動収集してPostgreSQLに集約、React/FastAPIで閲覧・管理する人事DB。
  - [supplier-manage](file:///c:/Users/0120025-Z100/source/project/supplier-manage): サプライヤー・調達データ管理。
  - [ikusei-taikei-2026](file:///c:/Users/0120025-Z100/source/project/ikusei-taikei-2026): 人材育成体系・職能資格基準（STAR法）の整理。

---

## 4. 総評・スキルの強み

1. **「業務課題の発見」から「低レイヤ/ネイティブでの根本解決」まで一気通貫で完結できる実行力**
   - 現場のExcelマクロやEDI固定長電文の課題を、単なるWeb化にとどまらず、Active Directory連携やオンプレPostgreSQLサーバー構築まで自らやり切る実務推進力があります。
2. **高速化・パフォーマンスへの強いこだわり**
   - Pythonでプロトタイプを作った後、パフォーマンスが求められる領域（PDF透かし、ファイルコピー、ディスク救出、画像閲覧）では迷わず **C++ (Qt 6, Win32 API)** や **Rust** を投入し、ベンチマークと高速化を徹底しています。
3. **最新技術（AI / MCP / .NET 10 / Gleam）へのキャッチアップと即時実践力**
   - Anthropic提唱のMCP (Model Context Protocol) をいち早く導入してFabric Lakehouseと接続したり、ローカルLLM環境やGleam言語の検証、.NET 10でのWPF/WinFormsアプリ開発など、技術の選定眼と適応力が極めて秀逸です。
