# MODULE_SCHEMA.md — モジュールフォーマット定義

**バージョン**: 0.1（暫定 — 実装後に簡略化予定）
**原則**: OPEN_QUESTIONS.md 通り、最初は情報量多めで作り、実装経験後に削減する

---

## ファイル名規則

```
{MODULE_ID}.md
例: HS-FUNC-002_quadratic-functions.md
```

---

## YAML Frontmatter

```yaml
---
module_id: HS-FUNC-002
title: "二次関数 / Quadratic Functions"
subject: mathematics
domain: functions
level: high-school
grade_range: "10-11"  # 相当学年（国際基準）

learning_objective: >
  二次関数の性質を理解し、グラフの描画・方程式の解法・最大最小問題を
  解くことができる。

prerequisites:
  - HS-FUNC-001  # 関数の基礎概念
  - HS-ALG-001   # 一次式・方程式

next_modules:
  - HS-FUNC-003  # 多項式関数
  - HS-CALC-001  # 微分の基礎

core_concepts:
  - 放物線とその性質
  - 頂点形式・標準形・因数分解形
  - 判別式
  - 最大値・最小値

key_terms:
  - quadratic function / 二次関数
  - parabola / 放物線
  - vertex / 頂点
  - discriminant / 判別式
  - axis of symmetry / 対称軸

common_misunderstandings:
  - "y = ax² + bx + c の a が符号を決めるが、向きが逆になると混乱する"
  - "判別式 D=0 が「解が存在する」ではなく「重解」だと気づきにくい"

curriculum_coverage:
  japan: ["数学I"]
  uk: ["A-Level Pure Math"]
  singapore: ["H2 Math"]
  ib: ["AA SL/HL", "AI SL/HL"]
  usa_common_core: ["HSF-IF", "HSF-BF"]
  australia: ["Mathematical Methods"]

source_references:
  - title: "OpenStax Algebra and Trigonometry"
    url: "https://openstax.org/books/algebra-and-trigonometry/pages/1-introduction-to-prerequisites"
    license: "CC BY 4.0"
    sections: ["5.1", "5.2", "5.3"]
  - title: "CK-12 Algebra II"
    url: "https://www.ck12.org/book/ck-12-algebra-ii-with-trigonometry/"
    license: "CC BY-NC 3.0"
    sections: ["Quadratic Functions"]

license: "CC BY 4.0"
version: "0.1"
created: "2026-03-19"
reviewed_by: ""
status: draft  # draft | reviewed | final
---
```

---

## 本文構造

```markdown
# {title}

## 学習目標

{learning_objective の展開 — 箇条書きで具体的に}

---

## 概念説明

### 定義
{核心的な定義を数式付きで記述}

### 性質
{主要な性質を列挙。証明の概略を含む}

### 直感的理解
{図・比喩・具体例による直感的説明}

---

## 標準形と変換

{各形式（標準形・頂点形式・因数分解形）の変換方法}

---

## 例題

### 例題 1（基礎）
**問題**: {問題文}
**解答**: {ステップごとの解答}

### 例題 2（応用）
**問題**: {問題文}
**解答**: {ステップごとの解答}

---

## よくある間違い

{common_misunderstandings の具体的な説明と正しい理解}

---

## 練習問題

1. {問題} （答え: {答え}）
2. {問題} （答え: {答え}）
3. {問題} （答え: {答え}）

---

## 参照元

{source_references の自然言語での記述}

---

## 次のステップ

- `{next_modules[0]}` — {次モジュールの簡単な説明}
- `{next_modules[1]}` — {次モジュールの簡単な説明}
```

---

## 数式記法

- インライン数式: `$...$`
- ブロック数式: `$$...$$`
- 例: 二次方程式の解の公式 `$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$`

---

## Qwen へのタスク指示テンプレート

```
以下のスキーマに従って、数学モジュールの初稿を生成してください。

MODULE_ID: {module_id}
TITLE: {title}
LEVEL: 高校数学
OBJECTIVE: {learning_objective}
PREREQUISITES: {prerequisites}
KEY_CONCEPTS: {core_concepts}
COMMON_ERRORS: {common_misunderstandings}
REFERENCE: {source_references[0]} （内容を参照・参考にするが、文章は独自に書く）

要件:
- YAML frontmatter を含む完全なモジュールファイルを生成する
- 数式は LaTeX 記法 ($..$ / $$..$$) を使用する
- 例題は2問以上（基礎1問・応用1問）
- 練習問題は3問以上（答え付き）
- 著作権クリーンな独自文章で書く（参照元の直接コピーは禁止）
- 日本語で記述する（数学用語は英語も括弧書きで併記）
```
