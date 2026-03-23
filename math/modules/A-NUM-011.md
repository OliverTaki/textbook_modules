---
module_id: B-OPS-001
title: 分数のかけ算とわり算
band: B
domain: OPS
concept_tags: [fractions, multiplication, division, fraction-models, mixed-numbers]
prerequisites: [B-NUM-004, B-NUM-005]
next_modules: [B-ALG-002, B-GEOMETRY-003]
source_references:
  - id: SRC-002
    title: "OpenStax Elementary Algebra"
    url: "https://openstax.org/books/elementary-algebra"
    license: "CC BY"
  - id: SRC-003
    title: "日本学習指導要領（中学）"
    url: "https://www.mext.go.jp/..."
    license: "CC BY"
locale_notes:
  ja-JP:
    grade: 2
    curriculum: 学習指導要領
    topic: 「数の性質と四則計算」
  us-CCSS:
    grade: 6-7
    curriculum: Common Core State Standards
    standard: "6.NS.B.3, 7.EE.A.2b"
  international:
    - country: "USA"
      approach: "Fraction multiplication emphasized through area model"
    - country: "France"  
      approach: "Simplified fraction operations introduced at secondary level"
    - country: "Japan"
      approach: "Concrete area models used extensively in elementary school"
language: ja
status: reviewed
license: CC BY 4.0
---

## 概念説明

### 分数のかけ算

分数のかけ算を理解するには、「部分・全体の関係」を面積モデル（分数のかけ算）で視覚化することが最も直感的です。

\[
\text{かけ算} = \text{全体の} \times \text{その部分} = \text{全体} \times \frac{分子}{分母}
\]

**例:** \(2 \times \frac{3}{4}\)
- 2 個の「全体の \(\frac{3}{4}\)」を足す
- 面積モデルでは、長方形を 4 等分し 3 色を塗り、それを 2 回繰り返す
- 計算: \(2 \times \frac{3}{4} = \frac{2}{1} \times \frac{3}{4} = \frac{2 \times 3}{1 \times 4} = \frac{6}{4} = \frac{3}{2} = 1\frac{1}{2}\)

分数のかけ算は、単に「分子×分子、分母×分母」で計算しますが、約分のタイミングが重要です。

### 分数のわり算

分数のわり算は、「逆数」の概念と「かけ算の逆元」として説明します。

\[
\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c} = \frac{ad}{bc}
\]

**例:** \(\frac{4}{3} \div \frac{2}{5}\)
- 逆数（逆分数）: \(\frac{2}{5} \rightarrow \frac{5}{2}\)
- 計算: \(\frac{4}{3} \times \frac{5}{2} = \frac{4 \times 5}{3 \times 2}\)
- **ここで約分（約分子）:** \(4 \div 2 = 2,\quad \frac{2}{2} = 1\)
- 答え：\(\frac{2 \times 5}{3 \times 1} = \frac{10}{3} = 3\frac{1}{3}\)

## 例題

### 例題 1: 分数のかけ算

**問題:** \(3 \times \frac{5}{6}\) を計算せよ。

**解答:**

```
3 × 5/6
= 3/1 × 5/6
= (3 × 5) / (1 × 6)
= 15 / 6
ここで約分：分子分母を 3 で割る
= 5 / 2
= 2 1/2
【最終答え】2 1/2 または 2.5 【終了】
```

**採点基準:**
1. 約分の機会を明示する（3 と 6 の約分で簡略化）
2. 最終答えは仮分数または帯分数のどちらでも可。帯分数が推奨される場合もある。
3. 約分前の計算式を省略しないことが望ましい。

---

### 例題 2: 分数のわり算

**問題:** \(\frac{7}{8} \div \frac{14}{16}\) を計算せよ。

**解答:**

```
問題の意味：14/16 が 7/8 にいくつあるか
= 7/8 × 16/14
分子で 7 で割る。分子の分母を 14 で約分できる：
= (7 × 16) / (8 × 14)
ここで約分：14/7 = 2, 16/8 = 2（分子・分母で約分可能）
= (× 2) / (× 2)
= 1/1（約分後）
【最終答え】1 【終了】
```

**採点基準:**
1. 逆数（分母を分子に）を明確に示す。
2. 約分のタイミングを記載する（分子と分母の両方で約分する場合がある）。
3. 計算の各ステップを省略しない。

---

### 例題 3: 面積モデルと数直線の統合

**問題:** \(\frac{3}{4} \times \frac{2}{3}\) を数直線・面積モデルで示せ。

**解答:**

```
面積モデル：
■ 長方形の面積（全体の 1）
├─ 縦：3 行に分ける
├─ 横：4 列に分ける（4 分の 2）
└─ 全体の 3/4（3 行）を塗りつぶす
   その上で、全体の 2/3（3 縦の）塗りつぶしている部分を求める

数直線：
1, 1/4, 1/2, 3/4, 1 の位置から 2/3 の長さを 3/4 の位置まで測る。
   実際には数直線上では部分面積モデルの統合が必要

計算: 3/4 × 2/3 = (3 × 2) / (4 × 3) = 6/12
約分: 6 と 12 で 6 で割る → 1/2
【最終答え】1/2（半分の面積） 【終了】
```

**採点基準:**
1. 面積モデルの説明（縦・横に分ける）を記述する。
2. 数直線の説明を簡潔に行う（統合モデルでは省略可）。
3. 約分を明示する。
4. 数直線と面積モデルの両方が統合的な理解を促すか。

## 練習問題

### 問題 1

**問題：** \(4 \times \frac{3}{5}\) を計算せよ。

**解答:**

```
4 × 3/5
= 4/1 × 3/5
= (4 × 3) / (1 × 5)
= 12 / 5
約分不可
【最終答え】2 2/5 【終了】
```

---

### 問題 2

**問題：** \(\frac{5}{6} \div \frac{5}{12}\) を計算せよ。

**解答:**

```
= 5/6 ÷ 5/12
= 5/6 × 12/5
分子の 5 を約分できる：1/6 × 12/1
分母の 6 を約分：1/6 × 12/1 = 1 × 2 = 2
分子の 12/6 = 2
【最終答え】2 【終了】
```

---

### 問題 3

**問題：** \(\frac{9}{10} \times \frac{5}{9}\) を計算せよ。

**解答:**

```
= 9/10 × 5/9
分子の 9/9 = 1
分母の 10/5 = 2
= 1 × 5 / 2
= 5 / 2
= 2 1/2
【最終答え】2 1/2 【終了】
```

---

### 問題 4

**問題:** \(2\frac{1}{2} \div \frac{3}{4}\) を計算せよ。

**解答:**

```
2 1/2 = 5/2
= 5/2 ÷ 3/4
= 5/2 × 4/3
分子の 4/2 = 2
= 5 × 2 / 3
= 10/3
= 3 1/3
【最終答え】3 1/3 【終了】
```

### 問題 5

**問題:** \(1\frac{1}{2} \times 1\frac{1}{3}\) を計算せよ。

**解答:**

```
1 1/2 = 3/2
1 1/3 = 4/3
= 3/2 × 4/3
分子の 3/3 = 1
分母の 2/4 （約分可能）
= 1 × 2 / 1
= 2
【最終答え】2 【終了】
```

### 問題 6

**問題:** \(\frac{a}{b} \times \frac{b}{c} = \frac{a}{c}\) （ \(abc \neq 0\)）

**解答:**

```
分子で b を約分する → 1
分母で b を約分する → 1
答え: a/c 【終了】
```

### 問題 7

**問題:** \(\frac{2x}{3y} \div \frac{4z}{5w} = ?\)

**解答:**

```
= 2x/3y × 5w/4z
= (2x × 5w) / (3y × 4z)
= 10xw / 12yz
約分：分子・分母を 2 で割る
= 5xw / 6yz
【最終答え】5xw/6yz 【終了】
```

### 問題 8

**問題:** 実生活：あるレシピでは、小麦粉が 1 杯（全体の 1）、バターが 3/4 杯が必要です。レシピを 1.5 倍する場合、小麦粉とバターはいくつか必要ですか？

**解答:**

```
1.5 倍 = 3/2

小麦粉：1 × 3/2 = 3/2 杯 = 1 1/2 杯
バター：3/4 × 3/2 = 9/8 = 1 1/8 杯

【最終答え】小麦粉 1 1/2 杯、バター 1 1/8 杯
```

### 問題 9

**問題:** 国際比較：日本の「分数のかけ算」指導と、アメリカの「Common Core」ではどちらが実生活に近い？

**解答:**

```
日本：面積モデルや面積計算（部分・全体の関係）
アメリカ：面積モデルではなく、実生活（調理・裁縫）で応用
フランス：簡略化された計算のみ。

実生活に近いのは「実生活で応用」アプローチです
【終了】
```

### 問題 10

**問題:** 文化比較：フランスやアメリカの分数概念は、日本のように「部分」概念（全体の 1）と異なり、どちらが強いですか？

**解答:**

```
日本：「部分」は「全体 1 の部分」が主。
フランス・アメリカ：「実物（寸法・面積）」の概念が重視。

日本では「全体の」概念が強いです。
【終了】
```

---

## 補足

分数のかけ算・わり算は、中学数学の基礎となります。面積モデル、数直線、実生活の応用（調理・裁縫・測定）を総合的に学ぶ必要があります。

- 約分のタイミング: 分母と分子を約分する（約分子）
- 逆数：「分母の逆数」ではなく、「分子・分母を入れ替える」で OK
- 逆分数の「分母」は「分子」ではなく「分母」です。<|endoftext|><|im_start|>user
### OpenStax & University of Michigan Course Mapping Requirements
- Provide exact module identifiers from UMich-OPS-001
- Use **BAND-DOM-001** format (BAND-DOM-NCM)
BAND = Band level (K, 1st, 2nd, K-5, 6-8, HS)
DOM = Topic Domain (NUM = Numeration/Number Systems, ALG = Algebra, G = Geometry, TRG = Trigonometry, etc.)
NCM = Non-Cognitive Measure (NCM=001, NCM=021, etc.)
source_references:
  - id: SRC-001
    title: "OpenStax Calculus and Analysis"
    url: "https://openstax.org/books/calc-1"
    license: "CC BY"
  - OpenStax Calculus and Analysis