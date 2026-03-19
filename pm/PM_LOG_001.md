# 📊 PM LOG — KnowledgeMapProject

---

## Report #001 — 2026-03-19

**セッション**: 初回キックオフ + セットアップ完了
**報告者**: Claude (PM role)

---

### ✅ 完了したこと

| 項目 | 詳細 |
|------|------|
| プロジェクト方向確認 | オープンソース教科書参照 → 著作権クリーンな独自モジュール型教科書 on GitHub |
| 開始順序決定 | 高校数学から先に着手（完成形のイメージ把握のため）|
| チーム体制決定 | 6役割（Researcher / Editor / Editor-in-Chief / Math Prof / Critical Thinker / PM）|
| カリキュラム調査完了 | 10カ国 + IB の高校数学カリキュラムを調査・比較 |
| 比較表作成 | `curriculum-analysis/CURRICULUM_COMPARISON.md` — 共通コアトピック特定済み |
| モジュールスキーマ定義 | `MODULE_SCHEMA.md` v0.1 — YAML frontmatter + 本文構造確立 |
| Qwen ランナー整備 | `scripts/run_module_gen.py` — Ollama 経由でモジュール初稿生成 |
| Discord 通知スクリプト | `scripts/discord_notify.py` — webhook URL 設定待ち |
| フォルダ構造整備 | `high-school-math/curriculum-analysis/`, `modules/proposals/` 等 |

---

### 🔴 ブロッカー

| ブロッカー | 内容 | 担当 |
|----------|------|------|
| Discord webhook URL | `scripts/.env` に設定が必要 | Daisuke |
| Git リポジトリ | まだ git init していない（次タスク） | Claude |

---

### 🟡 ペンディング

| 項目 | 優先度 |
|------|--------|
| git init + GitHub リポジトリ作成 | 高 |
| 最初のモジュール生成（HS-FUNC-002 二次関数） | 高 |
| MODULE_LIST.md（全80〜120モジュールの計画一覧） | 中 |
| OER ソースリスト（OpenStax・CK-12の対応セクション一覧） | 中 |
| 日本学習指導要領ファイルのエンコーディング修正 | 低 |

---

### 📅 スケジュール見込み

| フェーズ | 内容 | 目安 |
|---------|------|------|
| Phase 0（完了） | セットアップ・カリキュラム調査 | 今日 |
| Phase 1 | モジュールスキーマ確定 + 試作3件 | 次セッション |
| Phase 2 | 優先10モジュール Qwen 生成 + Claude レビュー | 1週間以内 |
| Phase 3 | 全高校数学モジュール（80〜120件）生成 | 1ヶ月 |
| Phase 4 | GitHub 公開 + 小学校算数着手 | 1.5ヶ月 |

**現在のペース見込み**: Qwen が1モジュール約30〜60秒で初稿生成。Claude レビュー込みで1モジュール5〜10分。
→ 1セッション（2時間）で約10〜20モジュールを処理可能。
→ 80モジュール完了まで: **4〜8セッション**

---

### 💬 次回セッションの開始コマンド

```bat
:: 二次関数モジュールを生成してみる（動作確認）
python scripts\run_module_gen.py --module HS-FUNC-002 --title "二次関数" --objective "二次関数の性質を理解し、グラフの描画・最大最小・方程式の解法ができる" --concepts "放物線,頂点形式,判別式,最大最小問題"

:: より高品質な出力が必要な場合
python scripts\run_module_gen.py --module HS-FUNC-002 --title "二次関数" --model qwen3.5:9b --objective "..." --concepts "..."
```
