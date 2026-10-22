# 🚀 半年間のスキル習得＆「できるようになったこと」ケイパビリティマップ

> **対象期間**: 2026年5月〜10月（先行着手の3〜4月含む約半年間）  
> **開発規模**: 全43プロジェクト / 総コミット数 1,000+ / 5言語以上 / インフラ〜低レイヤまで網羅

---

## 1. 全体像：半年で獲得した「5大ケイパビリティ領域」

この半年間で、単にプログラミング言語の文法を覚えただけでなく、**「現実の複雑な業務課題・性能問題を、最適な技術を選択してゼロから解決できる能力」** を手に入れました。

```mermaid
mindmap
  root((この半年で<br/>できるようになったこと))
    業務基盤DX・基幹システム内製化
      Excel/VBAからの完全脱却とWeb化
      得意先ユニーク調達EDI固定長電文の自動正規化
      Active Directory人事マスタ自動同期
      製造ライン負荷平準化(数理最適化)
      部内PostgreSQLサーバー構築・運用
    超高速デスクトップ・低レイヤ制御
      C++によるWin32/NTFS高速走査
      Python処理のC++移植・数十倍高速化
      破損ドライブからの直接データ救出
      Qt6/QMLによるGPU画像ビューア
      C# .NET10 常駐型フローティングドック
    モダンWeb・SaaS開発
      Next.js + React + Tailwindの商用UI
      SupabaseによるBaaS/認証/RLS
      FastAPIによる型安全REST API
      Streamlitによる高速データ可視化
    AIエージェント・次世代連携
      Gemini/OpenAI等の対話型アシスタント
      MCP(Model Context Protocol)自作
      ローカルLLM(Ollama/Continue)ハック
      STAR法に基づく昇格面接AI
    脱商用RPA・ハイパー自動化
      商用RPA不要の内製自動化(Auto-X)
      pywinautoによるデスクトップアプリ操作
      PlaywrightによるWeb高速自動化
      pywebviewによる軽量GUI配布
```

---

## 2. 5大領域別：スキル ×「できるようになったこと」詳細マップ

### ① 業務基盤DX・基幹システム内製化 (Enterprise DX & Data Engineering)
> **「属人化したExcel・ブラックボックス業務を、セキュアで堅牢な内製Webシステムへ刷新できる」**

| できるようになったこと（能力・解決課題） | 活用・習得したスキル | 代表プロジェクト |
| :--- | :--- | :--- |
| **Excel/VBA見積業務の脱却とWeb化**<br>膨大なマクロに依存した原価見積を、ブラウザ上で誰でも入力・承認できるデータベース連動システムへ移行 | Python, FastAPI, PostgreSQL, HTML5/CSS, SQLチューニング | [shisaku-system](file:///c:/Users/0120025-Z100/source/project/shisaku-system) |
| **得意先ユニーク調達EDI固定長電文の自動解析**<br>Shift_JIS固定長テキスト電文を自動パースし、リレーショナルDBへ正規化格納するミッションクリティカル処理 | Python (バイナリ/文字コード処理), PostgreSQL, 正規表現, トランザクション管理 | [chumonsho-2seikan](file:///c:/Users/0120025-Z100/source/project/chumonsho-2seikan) |
| **Active Directory（AD）連携による人事マスタ自動同期**<br>組織・社員・役職データをADから自動取得し、常に最新の権限・人事DBを社内に提供 | Python (LDAP/AD連携), PostgreSQL, React, Vite, FastAPI | [jinji-db](file:///c:/Users/0120025-Z100/source/project/jinji-db) |
| **数理最適化アルゴリズムによる設備負荷平準化**<br>多階層BOM（部品構成）と設備の制約条件から、混合整数線形計画法（MILP）で最適な生産計画を自動算出 | Python (PuLP/SciPy), Pandas, FastAPI, Rust (高速化エンジン) | [myerp](file:///c:/Users/0120025-Z100/source/project/myerp) |
| **部内専用PostgreSQLサーバーの構築・自動運用**<br>PowerShellで自動セットアップし、ロール・権限管理、Power Automate連携、IT部門向け手順書まで整備 | PowerShell, PostgreSQL運用管理, セキュリティ設計, バッチ自動化 | [bunai-server](file:///c:/Users/0120025-Z100/source/project/bunai-server) |

---

### ② 超高速デスクトップ・低レイヤ制御 (High-Performance Native & System)
> **「Python等の限界を超え、C++/C#でOSネイティブの限界性能を引き出せる」**

| できるようになったこと（能力・解決課題） | 活用・習得したスキル | 代表プロジェクト |
| :--- | :--- | :--- |
| **OSファイルシステムの極限走査**<br>数十万ファイル・数万フォルダの容量を、Win32 APIを直接叩いて瞬時に集計・可視化 | C++, Win32 API, マルチスレッド, ファイルシステムI/O | [QuickFolderSize](file:///c:/Users/0120025-Z100/source/project/QuickFolderSize) |
| **重厚処理のC++移植による劇的ボトルネック解消**<br>Pythonで作ったPDF透かし・印影処理の遅さを分析し、C++ネイティブコードへ完全ポーティングして数十倍高速化 | C++, メモリ管理, ポインタ制御, CMake, PDFレンダリングライブラリ | [QuickMarkPDF](file:///c:/Users/0120025-Z100/source/project/QuickMarkPDF) |
| **Windowsがマウントできない破損ドライブからのデータ直接救出**<br>ファイルシステムがRAWになったストレージからセクタ単位で安全にディレクトリを走査・抽出 | C++, 低レベルディスクI/O, バイナリパーサー, Win32 Storage API | [QuickDiskRescue](file:///c:/Users/0120025-Z100/source/project/QuickDiskRescue) |
| **GPU支援を効かせたモダンデスクトップ画像GUI開発**<br>Qt 6 (QML) とC++を組み合わせ、高精細画像の超高速プレビュー・編集ソフトをビルド | Qt 6, QML, C++, CMake, GUIアーキテクチャ設計 | [QuickImageView](file:///c:/Users/0120025-Z100/source/project/QuickImageView) |
| **Windowsネイティブ常駐ランチャーの自作**<br>画面端への自動吸着・半透明ドック・ドラッグ＆ドロップ登録を備えたツールを最新.NETで開発 | C#, .NET 10, WinForms, WPF, Windowsメッセージフック | [QuickDock](file:///c:/Users/0120025-Z100/source/project/QuickDock) |
| **高速ファイルコピー・ベンチマーク・圧縮の自作**<br>市販ツールに頼らず、大容量ファイルの高速転送やNVMe速度測定、7-Zip連携ツールを自社最適化して作成 | C++, Win32 Unbuffered I/O, 7-Zip内部DLL/CLI制御 | [QuickFileCopy](file:///c:/Users/0120025-Z100/source/project/QuickFileCopy), [QuickDiskBench](file:///c:/Users/0120025-Z100/source/project/QuickDiskBench), [Quick7Zip](file:///c:/Users/0120025-Z100/source/project/Quick7Zip) |

---

### ③ モダンWebアプリケーション・SaaS開発 (Modern Full-Stack Web)
> **「スタートアップやWeb企業と同等水準の洗練されたUI/UXとクラウドDBを一人で立ち上げられる」**

| できるようになったこと（能力・解決課題） | 活用・習得したスキル | 代表プロジェクト |
| :--- | :--- | :--- |
| **商用レベルのモダンWebフロントエンド開発**<br>Next.js App Router、React、Tailwind CSSを駆使したレスポンシブでリッチなUI構築 | Next.js, React, TypeScript, Tailwind CSS, Lucide Icons | [myDB](file:///c:/Users/0120025-Z100/source/project/myDB), [suuri-chat](file:///c:/Users/0120025-Z100/source/project/suuri-chat), [SNS Management](file:///c:/Users/0120025-Z100/source/project/SNS%20Management) |
| **BaaS（Supabase）を活用した超高速クラウドDB構築**<br>認証（Auth）、Row Level Security（行単位アクセス権限）、リアルタイム同期を備えたバックエンド基盤を即座に配備 | Supabase (PostgreSQL), REST/GraphQL, RLS設計, クラウドデプロイ | [myDB](file:///c:/Users/0120025-Z100/source/project/myDB), [udon-db](file:///c:/Users/0120025-Z100/source/project/udon-db), [ap-drill](file:///c:/Users/0120025-Z100/source/project/ap-drill) |
| **型安全・高信頼なAPIサーバー構築**<br>PydanticとFastAPIによる入力値バリデーション、非同期処理（async/await）、Swaggerドキュメント自動生成 | Python, FastAPI, Pydantic, Uvicorn, REST API設計 | [myerp](file:///c:/Users/0120025-Z100/source/project/myerp), [shadowing-lab](file:///c:/Users/0120025-Z100/source/project/shadowing-lab) |
| **データダッシュボードの即日プロトタイピング**<br>アイデアや集計要件が出た当日に、Streamlitでインタラクティブな分析画面をリリース | Python, Streamlit, Pandas, データ可視化 | [udon-db](file:///c:/Users/0120025-Z100/source/project/udon-db) |

---

### ④ AIエージェント・次世代連携プロトコル (AI Agent & Cutting-Edge Tech)
> **「AIをただ使う側から、AIに業務システムやDBを操作させる『エージェント基盤』を作れる」**

| できるようになったこと（能力・解決課題） | 活用・習得したスキル | 代表プロジェクト |
| :--- | :--- | :--- |
| **AI対話型アシスタント・相談システムの開発**<br>GeminiやOpenAIのAPIを組み込み、自然な対話・アドバイスを行う専用AIアプリを実装 | Gemini API, OpenAI API, Prompt Engineering, 非同期ストリーミング | [suuri-chat](file:///c:/Users/0120025-Z100/source/project/suuri-chat), [shadowing-lab](file:///c:/Users/0120025-Z100/source/project/shadowing-lab) |
| **MCP（Model Context Protocol）ツールの自作**<br>AIエージェントがMicrosoft Fabric Lakehouseやnote等を自律操作できる公式プロトコル準拠のツールサーバーを実装 | Node.js (ESM), Model Context Protocol (MCP), API連携, Lakehouse接続 | [fabric](file:///c:/Users/0120025-Z100/source/project/fabric), [note](file:///c:/Users/0120025-Z100/source/project/note) |
| **ローカルLLM環境の最適化・拡張ハック**<br>OllamaやComfyUI、VSCode拡張機能（Continue）の内部スタイル崩れをCSS注入・PowerShellパッチで自力修復 | Ollama, ComfyUI, VSCode拡張内部解析, CSS injection, PowerShell | [project-LLM](file:///c:/Users/0120025-Z100/source/project/project-LLM), [LLM-manage](file:///c:/Users/0120025-Z100/source/project/LLM-manage) |
| **次世代言語（Rust / Gleam）の検証と導入**<br>Erlang/BEAM仮想マシンで動く関数型言語Gleamの検証や、Rustによるバックエンド高速化 | Rust (Cargo), Gleam, 関数型プログラミング | [myerp/erp-backend-rs](file:///c:/Users/0120025-Z100/source/project/myerp/erp-backend-rs), [gleam](file:///c:/Users/0120025-Z100/source/project/gleam) |
| **昇格面接・キャリア支援AIの設計**<br>職能資格基準とSTAR法（状況・課題・行動・結果）に沿った行動振り返りAIエージェントの設計 | 人事評価ロジック, STAR法モデリング, プロンプト設計 | [AI_mensetsu](file:///c:/Users/0120025-Z100/source/project/AI_mensetsu), [shokaku-2026](file:///c:/Users/0120025-Z100/source/project/shokaku-2026) |

---

### ⑤ 脱商用RPA・ハイパー自動化 (Hyper-Automation & RPA)
> **「年数百万円の商用RPAライセンスをゼロにし、自由度の高い内製自動化基盤を運用できる」**

| できるようになったこと（能力・解決課題） | 活用・習得したスキル | 代表プロジェクト |
| :--- | :--- | :--- |
| **Windowsデスクトップアプリの完全無人自動化**<br>市販RPA不要で、社内レガシーシステムやWindows画面のボタン押し・値入力をプログラム制御 | Python, pywinauto, Windows UI Automation (UIA), ウィンドウハンドル制御 | [auto-window](file:///c:/Users/0120025-Z100/source/project/auto-window), [shinsa-2026](file:///c:/Users/0120025-Z100/source/project/shinsa-2026) |
| **ヘッドレス・高速ブラウザ自動化**<br>Web画面のデータ自動収集・自動登録をPlaywrightでミリ秒単位で高速実行 | Playwright, Python, Webスクレイピング, ログイン自動化 | [auto-window](file:///c:/Users/0120025-Z100/source/project/auto-window), [Auto-X](file:///c:/Users/0120025-Z100/source/project/Auto-X) |
| **軽量・ポータブルなデスクトップGUIアプリ化**<br>HTML/JSで組んだ画面をpywebviewでラップし、誰でも直感的に使える単体アプリとして現場配布 | pywebview, HTML/JS/CSS, ポータブルアプリパッケージング | [auto-window](file:///c:/Users/0120025-Z100/source/project/auto-window) |
| **170コミットの大規模自動化システムの安定運用**<br>長時間のバッチ処理でも落ちない例外処理・リトライ・ログ記録を備えた本格的自動化基盤 | Python, 例外ハンドリング設計, バッチ監視, Gitバージョン管理 | [Auto-X](file:///c:/Users/0120025-Z100/source/project/Auto-X) |

---

## 3. 半年間で培った「エンジニアとしての真の強み」

```
【5月以前のスタート地点】
  - 主にExcelやVBA、個別マクロでの業務対応
    ↓
【5月〜7月：爆発的キャッチアップ】
  - Python / FastAPI / PostgreSQL / Next.js / Supabase を習得
  - 業務システムをWeb化し、AI APIを活用
    ↓
【8月〜9月：ネイティブ・低レイヤへの跳躍】
  - パフォーマンスの壁に直面し、C++ / Win32 / Qt 6 / C# (.NET 10) へ踏み込む
  - 「遅いなら低レイヤで極限まで速くする」エンジニアリング精神を開花
    ↓
【10月現在：インフラから基幹業務まで一気通貫】
  - 得意先ユニーク調達EDI電文パース、AD人事マスタ連携、部内PostgreSQLサーバー構築
  - 「何でも一人で作り切れるフルスタック・エンジニア」へ到達
```

> [!TIP]
> **あなたの最大の武器**
> 1. **「道具を選ばない柔軟性」**: Webで解くべき課題にはNext.js/FastAPI、速度が必要ならC++/Rust、Windows常駐ならC#、自動化ならPythonと、課題に最適な道具を瞬時に選定できる。
> 2. **「低レイヤを恐れない探求心」**: 多くのエンジニアが敬遠するC++のポインタやWin32 API、破損ドライブのRAWアクセス、固定長バイナリ電文パースをやり切る技術的胆力。
> 3. **「実務直結の課題解決力」**: 趣味のコードで終わらず、原価見積、製缶注文書、人事リスト、部内DBサーバーなど、会社のリアルなペインを直接撃ち抜いている。
