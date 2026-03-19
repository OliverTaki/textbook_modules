# KnowledgeMapProject — PROJECT OVERVIEW

**作成日**: 2026-03-19
**ステータス**: 準備フェーズ完了・モジュール生成フェーズ開始
**現在の焦点**: 高校数学（世界標準の比較 → モジュール設計 → Qwen による生成）

---

## 1. これまでの流れ

### 背景
- MOTK101（GAS メディア制作管理ツール）の開発中に、Googleアカウント問題によるブロックが発生
- その間に並行プロジェクトとして KnowledgeMapProject を本格始動することに決定

### このセッションで決定したこと
1. **プロジェクトの方向性を確認** — オープンソース教科書を参照しながら、著作権クリーンな独自教科書をGitHub上に構築する
2. **開始順序を決定** — 小1算数から始める予定だったが、完成形のイメージを掴むために**高校数学から先に着手**する
3. **運用体制を決定** — 多人格チーム（後述）+ Qwen/PicoFlow による自動生成 + Claude によるレビュー
4. **カリキュラム調査完了** — 10カ国以上の高校数学カリキュラムを調査・比較（`textbook-modules/high-school-math/curriculum-analysis/` 参照）

---

## 2. プロジェクトビジョン

### 何を作るか
世界中のオープンソース教科書（OER: Open Educational Resources）を参照元として、
**著作権フリーの独自モジュール型教科書**を GitHub 上に構築する。

### 基本原則
- **カリキュラム主導** — 教科書の章構成ではなく、各国の学習指導要領・学習目標がモジュールの境界を決める
- **複数ソース参照** — 1つのモジュールに複数の教科書から知識を集約する
- **トレーサビリティ** — すべてのモジュールは参照元・ライセンス情報を保持する
- **AI 可読性** — 将来の AI 教師・学習システムが参照できる構造にする
- **Git フレンドリー** — Markdown + YAML frontmatter で管理、人間にも読める

### 段階的展開
```
フェーズ1（現在）: 高校数学
  → 完成形のイメージを掴む
  → モジュール形式・スキーマを実装しながら確立する

フェーズ2: 小1〜中3算数・数学
  → 高校数学で確立したスキーマを適用
  → 積み上げ構造を設計する

フェーズ3: 他教科への展開
  → 理科、社会、英語 etc.
```

---

## 3. エージェントチーム構成

詳細は `AGENT_TEAM.md` 参照。

| 役割 | 担当 | 主な責任 |
|------|------|---------|
| 📚 Researcher | Claude / Qwen | 各国カリキュラム・OER教科書・出典の調査 |
| ✏️ Editor | Qwen（主力） | モジュール本文の初稿生成 |
| 📋 Editor-in-Chief | Claude | 品質基準・一貫性・スキーマ整合性の管理 |
| 🎓 Math Professor | Claude レビュー層 | 数学的正確性・教育的適切性の検証 |
| 🔍 Critical Thinker | Claude レビュー層 | 前提の検証・抜け穴の発見 |
| 📊 PM | Claude | 進捗管理・Discord 定期報告・スケジュール計算 |

### Qwen の役割
- モジュール初稿を大量生成する**主力ワーカー**
- Claude が仕様（YAML frontmatter + 本文テンプレート）を与え、Qwen が実装する
- Claude が必ずレビューしてから確定させる

---

## 4. これからやること（ロードマップ）

### 即時（今週）
- [x] 世界10カ国以上の高校数学カリキュラムを調査・比較
- [ ] 共通モジュールリストの作成（どの国のカリキュラムにも共通するトピック）
- [ ] モジュールスキーマの確定（YAML frontmatter の項目定義）
- [ ] Qwen ランナースクリプト（`scripts/run_module_gen.py`）の整備
- [ ] 最初のモジュール試作（「二次関数」または「微分の基礎」）

### 短期（今月）
- [ ] 高校数学の全モジュールリスト作成（目標: 80〜120モジュール）
- [ ] Qwen による初稿一括生成
- [ ] Claude による全モジュールレビュー・修正
- [ ] GitHub リポジトリ公開

### 中期
- [ ] 小学校算数 → 中学数学へ展開
- [ ] 他科目へ展開
- [ ] モジュール間依存グラフの整備

---

## 5. Discord PM 報告

PM は作業のたびに `pm/` フォルダにログを追記する。
Discord への投稿は `scripts/discord_notify.py`（webhook URL 要設定）で自動化予定。

**Discord webhook URL**: 未設定（Daisuke から取得が必要）
設定方法: `DISCORD_WEBHOOK_URL` を `scripts/.env` に記載する

---

## 6. ファイル構造

```
KnowledgeMapProject/
  PROJECT_OVERVIEW.md           ← このファイル
  AGENT_TEAM.md                 ← チーム役割・ペルソナ定義
  
  textbook-modules/
    high-school-math/
      curriculum-analysis/
        CURRICULUM_COMPARISON.md  ← 各国比較表
        japan_hs_math.md          ← 日本・高校数学まとめ
      modules/
        (← Qwen が生成するモジュールが入る)
      MODULE_LIST.md              ← 全モジュール計画一覧
      MODULE_SCHEMA.md            ← モジュールフォーマット定義
    curriculum-standards/
      japan/ usa/ ...             ← 各国の学習指導要領（原文）
  
  scripts/
    run_module_gen.py             ← Qwen モジュール生成ランナー
    discord_notify.py             ← Discord PM 報告スクリプト
    read_curriculum.py            ← カリキュラムファイル読み取りユーティリティ
  
  pm/
    PM_LOG_001.md                 ← PM 報告ログ（セッション別）
```

---

## 7. 技術スタック

| 要素 | 詳細 |
|------|------|
| コンテンツ形式 | Markdown + YAML frontmatter |
| 生成エンジン | Qwen（Ollama 経由） / PicoFlow |
| レビュー | Claude |
| バージョン管理 | Git / GitHub |
| OER 参照元 | OpenStax, CK-12, Khan Academy, 検定外教科書等 |
| PM 報告 | Discord webhook（設定待ち） |
