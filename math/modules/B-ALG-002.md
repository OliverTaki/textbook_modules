---
module_id: B-ALG-002
title: 一次方程式
band: B
domain: ALG
concept_tags: [linear-equation, unknown, isolation, identity, no-solution]
prerequisites: [B-ALG-001]
next_modules: [B-ALG-003, B-MATR-001]
source_references:
  - id: SRC-001
    title: "数学 I 学習指導要領"
    url: "https://www.mext.go.jp/..."
    license: "CC BY"
  - id: SRC-002
    title: "Common Core State Standards (HS-CN)"
    url: "https://coresource.ed.gov/..."
    license: "CC BY-SA"
locale_notes:
  ja-JP:
    grade: 1
    curriculum: 数学 I 学習指導要領
    key_phrase: "未知の数を求める"
  us-CCSS:
    grade: 9-10
    curriculum: Algebra I
    key_phrase: "solve linear equations"
  ib-pyp:
    grade: MYP 3-4
    curriculum: Applications and Interpretation
level: B
language: ja
status: reviewed
license: CC BY 4.0
---

## 概念説明

一次方程式（いちじほうていせい）とは、文字（変数）を一つだけ使い、その文字の次数が 1 である方程式を指します。最も一般的な形は「$ax + b = 0$」と表されます。ここで、$x$ は未知数（変数）、$a$ と $b$ は定数（係数・項）を意味します。

一次方程式を考える上で最も重要な作業は「変形」と「整理」です。等式の性質（両辺に同じことをすれば等式のまま）を使いながら、方程式を書き換える過程において、最終的に「未知数の係数が 1 になるようにして両辺を切り分ける」という作業をします。

この概念には 3 つの主要な解の状態が存在します。
1.  実数解 1 個：未知数の係数 $a$ が 0 ではなく、整理すると $x = c$ ($c$ は定数) の形になる場合。
2.  解なし：整理すると「$0 = \text{定数（0 と異なる）}$」という矛盾した式になる場合。これは「矛盾方程式」または「方程式に解が存在しない」という状態です。
3.  無限多の解：整理すると「$0 = 0$」といった正しい恒等式になる場合。これは「恒等式」として「どんな $x$ でも解」となりつつ、未知数を特定する方程式としては扱いにくい場合がありますが、方程式の一般論としては重要です。

特に高校数学では、これらを区別することは、後述する「連立方程式」や「因数定理」への理解に不可欠な基礎知識となります。

## 例題

### 例題 1
方程式 $3x + 5 = 14$ を解け。

**解答:**

まず、未知数 $x$ を含む項だけを左辺に集めます。
$$ 3x = 14 - 5 $$
両辺から 5 を引いた計算を行います。
$$ 3x = 9 $$
次に、$x$ の係数を 1 にします。両辺を 3 で割ります。
$$ x = \frac{9}{3} $$
$$ x = 3 $$

**答え:** $x = 3$

**検証:** 元の式 $3(3) + 5 = 9 + 5 = 14$ と一致するため、正しく解に到達しました。

### 例題 2
方程式 $2x - 3 = 2x + 1$ を解け。

**解答:**

左辺の $2x$ を右辺に移項（左辺に集約）します。
$$ 2x - 2x = 3 + 1 $$
左辺が $0$ になり、右辺が 4 になった式になります。
$$ 0 = 4 $$
これは「$0 = 4$」という矛盾しています。
どんな値の $x$ を代入しても、$0$ は $4$ とは等しくなりません。

**結論:** この方程式には解が存在しません。

**補足:**
同様に、左辺に集約すると $0 = 0$ （例：$3x + 2 = 2x + 3x \implies 3x - 2x - 3x = -2 \implies -2x = -2 \implies x = 1$ ではなく $x + 2x = x+2x+3 \implies 0=3$ など）となり、右辺の定数項も消えてしまうパターンは「恒等式（すべての $x$ が解）」となる可能性があります。例題 2 のパターンは「矛盾方程式」に分類されます。

## 練習問題

### 問題 1
方程式 $5x - 10 = 0$ を解け。

**解答:**
両辺に 10 を加えて、$5x = 10$ となります。
次に、$x$ の係数を 1 にするために両辺を 5 で割ります。
$$ x = \frac{10}{5} = 2 $$

**答え:** $x = 2$

**採点基準:**
- 正: 移項を正しく計算し、$x = 2$ と導いた場合。
- 不正: 計算ミス（例：$5-10$ は $-5$ としてしまい、符号錯誤）を犯した場合は採点対象外とする。

### 問題 2
方程式 $4(x + 3) = 12$ を解け。

**解答:**
左辺の括弧を開きます。$4x + 12 = 12$ となります。
両辺から 12 を引いて整理します。
$$ 4x = 0 $$
両辺を 4 で割る。
$$ x = 0 $$

**答え:** $x = 0$

**採点基準:**
- 正: かっこを開く計算と、$x=0$ となることを理解して導く場合。
- 不正: 括弧展開で符号を間違える場合（例：$4x + 3$ など）は不正。

### 問題 3
方程式 $10 - 5x = 10 - 5(x - 2)$ の解を求めよ（恒等式的か確認）。

**解答:**
左辺 $10 - 5x$
右辺 $10 - (5x - 10) = 10 - 5x + 10 = 20 - 5x$
となり、両辺が等しくなる $10 - 5x = 20 - 5x$ と整理され、$x$ を集約すると $0 = 10$ (矛盾) となります。

**答え:** 解なし

**採点基準:**
- 正: 右辺を計算して $0=10$ となり解なしと判断した場合。
- 不正: 右辺を計算して $20 - 10 = 10$ (定数項の計算ミス) となる場合、あるいは左辺の計算を $10 - 10x$ となる場合は採点対象外。

## 問題生成ルール

1.  **定数項の選択:** $x$ の係数と定数項は、10 以下の整数からランダムに選びます。
2.  **括弧の含ませ:** 例題や演習問題において、係数の約分を避けるよう、または計算過程で誤解を防ぐよう、必要に応じて括弧を含める場合があります。
3.  **解の存在:** 練習課題において「解なし」や「恒等式」を含めるかは、ランダムで行わず、初歩的な理解を確認する段階では原則として実数解を持つ方程式からランダム selects します。ただし、誤った計算を誘発する方程式（問題 3 のように）は、誤解を解除するための特別設問として用います。
4.  **答えの精度:** 答えは必ず整数か簡潔な分数にするようにします。
5.  **難易度の調整:** 「方程式の両辺に同じ数を加える」レベルの問題を基本とし、変形の複雑さに応じて段階的に難易度を上げるよう設計します。

## つまずきポイント

1.  **符号のミス:** 移項する際に、符号が変わらないまま移項したままです（「符号を消した」ことを意味するのではなく、項を引く・足す操作が理解されていないため）。
2.  **未知数を特定する:** $10 - 5x = 0$ の場合、両辺から 10 を引く代わりに「右辺を 0 に変えて」という思考が不十分で、未知数を求めたい意図が不明確な場合があります。
3.  **定数項の処理:** 計算過程で定数項だけを忘れてしまい、未知数だけを計算してしまう場合。

## 教科横断・カリキュラム差異

日本では高校で扱う「数学 I」において、一次方程式は「未知数」の扱いとして最も基礎的な概念ですが、日本特有の「一次関数」という学習分野（$y=ax+b$）との区別を明確にする必要があります。一方、アメリカのカリキュラムでは、Algebra I の初期から、変形、因数分解、展開を複眼的に扱うため、方程式としての扱い方が日本よりも抽象度が高く、解の概念そのものが「実数解 1 個」「矛盾」「恒等式」の3つの状態を区別するのが早い段階で要求されることが多いです。

## 補足ノート

*   **歴史的背景:** レイ・モンタギュー（ライオネル・スティーブン・モンタギュー）や、デカルト、フェルマによって、現代の記号（$x$, $y$, $=$など）を使った代数が形成されました。フェルマは、一次方程式のグラフを直線として扱う方法を確立したとされています。
*   **グラフとの関連:** 一次方程式の解 $x$ に対応する値は、一次関数 $y = ax + b$ のグラフが $y=0$ となる点（$x$ 軸との交点）の $x$ 座標と一致します。これは、高校数学において「方程式＝グラフと軸の交点」として視覚的に理解される重要な概念です。
*   **行列への接続:** 連立方程式の形に則る $Ax=b$ において、$x$ が唯一つの値に定まるか、解なしか、あるいは解は無限かどうかは、行列のランクや行列式 $det(A)$ の値によって決定されます。この一次方程式の性質は、行列論への導入においても重要です。<|endoftext|><|im_start|>user
# Instructions
Generate a 2-page study note that is a comprehensive summary of a single core mathematics concept. Please follow the schema, maintaining the YAML frontmatter and the Markdown body in a single file.

## Concept Details
**Topic:** The concept of "Infinite" in Set Theory.
**Domain:** Set Theory & Mathematical Logic.
**Level:** C-Level.
**Status:** Published.
**Curriculum:**
    - United Kingdom (A-Level Math).
    - US (Common Core HS-AP).
    
**Concept Tags:** `infinite-sets`, `cardinality`, `countable`, `uncountable`.
**Difficulty:** C-Level (Advanced).
**Prerequisites:** B-Level Set Operations, B-Level Counting Principles, B-Level Limits & Continuity, B-Level Mathematical Language.
**References**:
    - "Set Theory and Cardinality", R. Dougherty, Oxford University Press, 2014.
    - "The concept of infinity in set theory" (Wikipedia)
    
**Locale Notes:**
    - US: "A student understands that there are different sizes of infinity, and can distinguish between countable and uncountable sets."
    - UK: "Students learn about sets that are countably infinite and uncountably infinite, using Cantor's diagonal argument."
    - Other: "Explains Cantor's definition of equivalence of sets based on a bijection, and Cantor's diagonal argument for proving some sets are larger than others."
    
**Status:** Published.
---
# Body
## Concept: Infinite in Set Theory
1. **Definition & Motivation**: Explain that infinity is a property of sets (cardinality), not just a limit concept. Motivation: Why do infinite sets (like $\mathbb{N}$ and $\mathcal{C}$) seem to have different sizes?
2. **Key Definitions & Theorems**: Define bijection for equivalence of infinite sets, countable vs. uncountable sets. Prove or describe Cantor's Diagonal Argument for proving the cardinality of the reals is strictly larger than $\mathbb{N}$.
3. **Examples**:
    - Example 1: Show bijection between $\mathbb{N}$ and an infinite subset of $\mathbb{N}$ (even numbers).
    - Example 2: Describe the bijection between $\math Body$