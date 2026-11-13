# 🚀 Engineering Capability & Tech Stack Portfolio (`skill-manage`)

[🇯🇵 日本語](#-概要-japanese) | [🇺🇸 English](#-overview-english)

---

## 🌐 Live Interactive Dashboard / 公開ダッシュボード
👉 **[https://maktak-105.github.io/manage/](https://maktak-105.github.io/manage/)**  
*(A responsive, interactive single-page dashboard featuring instant search across all 47 projects, category filtering, chronological tech matrices, and bilingual support.)*

---

## 🇯🇵 概要 (Japanese)

本リポジトリは、開発者が約8ヶ月間（2026年3月〜11月）で手掛けた**全47プロジェクト**を自動走査・解析し、月別の技術スタック習得履歴、6大中核ケイパビリティ領域、および成果物マトリクスを一元管理・可視化するためのポートフォリオ基盤です。

### 📊 全体サマリー
- **総開発プロジェクト数**: 47+ プロジェクト
- **駆使・習得言語**: 6+ 言語（Python, TypeScript, JavaScript, C++, C#, Rust, Gleam, PowerShell, SQL 等）
- **総 Git コミット数**: 1,400+ コミット
- **6大中核ケイパビリティ領域**:
  1. 🏢 **業務基盤DX・基幹内製化** (Excel脱却、大手自動車調達EDI固定長パース、原価実績Fastify API、AD人事同期)
  2. 🌐 **自宅NAS・クラウド・公開Web** (QNAP NAS Docker、PostgreSQL 16、Cloudflare Tunnel/Access、Vercel/PWA)
  3. ⚡ **超高速C++/C#・低レイヤ** (Win32高速走査、Qt6/QML GPU描画、.NET 10 常駐ドック、C++高速移植)
  4. 💻 **モダンWeb・SaaS開発** (Next.js App Router、React、Tailwind CSS、Supabase BaaS)
  5. 🤖 **AIエージェント・先端技術** (自律AIループ Ralph Loop、Gemini/OpenAI API、MCPツール、Obsidian+Claude)
  6. 🚀 **脱商用RPA・ハイパー自動化** (Auto-X、pywinauto × Playwright ハイブリッド自動化)

### 📁 ドキュメント一覧
- **[`index.html`](file:///c:/Users/0120025-Z100/source/manage/index.html)**: 統合Webダッシュボード（スマホ対応・日英切り替え・リアルタイム検索付き）
- **[`tech_acquisition_matrix.md`](file:///c:/Users/0120025-Z100/source/manage/tech_acquisition_matrix.md)**: 技術視点・時系列習得マップ（いつ何を初めて導入したかの体系表）
- **[`monthly_tech_matrix.md`](file:///c:/Users/0120025-Z100/source/manage/monthly_tech_matrix.md)**: 月別×カテゴリ別成果物（プロジェクト）マトリクス
- **[`skill_and_capability_map.md`](file:///c:/Users/0120025-Z100/source/manage/skill_and_capability_map.md)**: 6大ケイパビリティ領域・課題解決実績レポート
- **[`skill_and_tech_stack_history.md`](file:///c:/Users/0120025-Z100/source/manage/skill_and_tech_stack_history.md)**: 技術スタック層別マトリクス＆進化タイムライン

---

## 🇺🇸 Overview (English)

This repository serves as a unified engineering portfolio and capability tracking platform, automatically analyzing **47 projects** developed over an 8-month period (March — November 2026). It visualizes technology adoption timelines, core capability domains, and project metrics.

### 📊 Overall Highlights
- **Total Projects**: 47+ Production & R&D projects
- **Core Languages**: 6+ Languages (Python, TypeScript, JavaScript, C++, C#, Rust, Gleam, PowerShell, SQL)
- **Total Commits**: 1,400+ Git commits
- **6 Core Engineering Capability Domains**:
  1. 🏢 **Enterprise DX & Core Systems**: Legacy Excel migration, Automotive EDI parser, Read-only cost API (Fastify), Active Directory sync.
  2. 🌐 **Self-Hosted Cloud & Public Web**: 24/7 QNAP NAS Docker, PostgreSQL 16, Cloudflare Access Zero Trust, Vercel PWA.
  3. ⚡ **High-Performance Native & Low-Level**: Direct Win32 API NTFS scan, Qt 6 / QML GPU rendering, .NET 10 desktop dock, Python-to-C++ porting (30x speedup).
  4. 💻 **Modern Web & Fullstack SaaS**: Next.js (App Router), React, Tailwind CSS, Supabase BaaS with RLS.
  5. 🤖 **AI Agents & Autonomous Tech**: Self-healing test loops (Ralph Loop), Gemini/OpenAI streaming, Custom MCP tools, Claude Second Brain.
  6. 🚀 **Hyper-Automation & RPA**: License-free in-house RPA combining pywinauto (Windows UIA) & Playwright (Web).

---

## 🖥️ Usage / 使い方

### 1. View the Live Dashboard / ダッシュボードの閲覧
Open [`index.html`](file:///c:/Users/0120025-Z100/source/manage/index.html) in any web browser, or visit the [GitHub Pages](https://maktak-105.github.io/manage/) site.

### 2. Rescan & Update Projects / プロジェクトの再解析
```powershell
# Run codebase analyzer
python tools/curate_stack.py

# Display summary in CLI
python tools/print_summary.py
```
