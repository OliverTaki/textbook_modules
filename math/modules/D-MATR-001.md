---
module_id: D-MATR-001
title: 行列の基礎・演算
band: D
domain: MATR
concept_tags: [matrix，operation，diagonal-matrix，matrix-multiplication]
prerequisites:
  - D-ALG-020
next_modules:
  - D-MATR-020
  - D-VEC-010
source_references:
  - id: REF-MAT-001
    title: "線型代数入門 (小松・大谷)"
    url: "https://www.example.edu/ja/"
    license: "CC BY"
locale_notes:
  ja-JP:
    grade: 大学 1 年生
    curriculum: 理工系初年次教育
    semester: 1
language: ja
status: reviewed
license: CC BY 4.0
---

## 概念説明

行列（matrix）は数式を 2 次元の表の形にまとめる記法であり、線形代数の基となる構造である。行列には行数と列数があり、その要素ごとの配置に規則性がある。

行列の定義：m 行 n 列の要素からなる数値の表

$$ A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} $$

- m：行数（行ベクトル）
- n：列数（列ベクトル）
- $a_{ij}$：第 i 行 j 列の成分

### 主要な行列の種類

**正方行列**（行列の行数と列数が等しい。m = n）：
- 逆行列が定義可能
- 固有値・固有ベクトルの解析が可能

**対角行列**：
- 対角線以外の成分がすべて 0
- 対角成分：$d_1, d_2, \dots, d_n$
- 逆行列：各対角成分の逆数（0 は除外）

**単位行列** $I_n$：
- 対角成分がすべて 1
- $AI = IA = A$

**零（ゼロ）行列 $O$**：
- 全成分が 0
- 行列加法の単位元

### 行列演算のルール

**和 $A + B$**：
- 行・列数が一致すること
- 成分ごとの加法
- 順序交換可能：$A + B = B + A$

**スカラー倍数 $\alpha A$**：
- 各成分にスカラーを掛ける

**積 $AB$**：
- 左側の行列が m×p、右側が p×n でなければならない
- 結果：m×n 行列

計算手順：(AB)_{ij} = \sum_{k=1}^{p} A_{ik} B_{kj}

注意点：$AB \neq BA$ 一般に成立しない（積の交換律は成り立たない）
- $I \cdot A = A \cdot I = A$（単位行列は恒等元）
- $O \cdot A = A \cdot O = O$（零行列は加法吸収律）

### 転置行列 $A^{\mathrm{T}}$

- 行と列を入れ替える
- 対称行列：$A^{\mathrm{T}} = A$
- 対称行列は対称な構造を持つ

## 例題

### 例題 1：対角行列の性質の確認

与えられた行列 $A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$ について、対角行列であることを示せ。また $A \cdot I_2$ と $I_2 \cdot A$ を計算して等しいか確認せよ。

**解答：**

(1) 対角行列の確認
- 成分 $a_{12} = 0$（第 1 行第 2 列）
- 成分 $a_{21} = 0$（第 2 行第 1 列）
- 非対角成分がすべて 0 → 対角行列

(2) 積の計算
$I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$

$A \cdot I_2 = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} \cdot \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2\cdot 1 + 0\cdot 0 & 2\cdot 0 + 0\cdot 1 \\ 0\cdot 1 + 3\cdot 0 & 0\cdot 0 + 3\cdot 1 \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} = A$

$I_2 \cdot A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} = \begin{bmatrix} 1\cdot 2 + 0\cdot 0 & 1\cdot 0 + 0\cdot 3 \\ 0\cdot 2 + 1\cdot 0 & 0\cdot 0 + 1\cdot 3 \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} = A$

→ $A \cdot I = I \cdot A = A$（単位行列の性質が確認）

### 例題 2：行列の積の計算

与えられた行列 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$、$B = \begin{bmatrix} 0 & 5 \\ 6 & 0 \end{bmatrix}$ について、$AB$ と $BA$ を計算し、順序によって異なることを示せ。

**解答：**

(1) $AB$ の計算
$$ AB = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \cdot \begin{bmatrix} 0 & 5 \\ 6 & 0 \end{bmatrix} $$

- 第 1 行第 1 列：$1\cdot 0 + 2\cdot 6 = 12$
- 第 1 行第 2 列：$1\cdot 5 + 2\cdot 0 = 5$
- 第 2 行第 1 列：$3\cdot 0 + 4\cdot 6 = 24$
- 第 2 行第 2 列：$3\cdot 5 + 4\cdot 0 = 15$

$AB = \begin{bmatrix} 12 & 5 \\ 24 & 15 \end{bmatrix}$

(2) $BA$ の計算
$$ BA = \begin{bmatrix} 0 & 5 \\ 6 & 0 \end{bmatrix} \cdot \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} $$

- 第 1 行第 1 列：$0\cdot 1 + 5\cdot 3 = 15$
- 第 1 行第 2 列：$0\cdot 2 + 5\cdot 4 = 20$
- 第 2 行第 1 列：$6\cdot 1 + 0\cdot 3 = 6$
- 第 2 行第 2 列：$6\cdot 2 + 0\cdot 4 = 12$

$BA = \begin{bmatrix} 15 & 20 \\ 6 & 12 \end{bmatrix}$

**比較**：
$AB = \begin{bmatrix} 12 & 5 \\ 24 & 15 \end{bmatrix} \neq \begin{bmatrix} 15 & 20 \\ 6 & 12 \end{bmatrix} = BA$

→ 行列の積は順序依存であり、交換律の成り立たないことが確認された。

## 練習問題

### 問題 1

行列 $A = \begin{bmatrix} 3 & -1 & 2 \\ 0 & 5 & -4 \end{bmatrix}$、$B = \begin{bmatrix} 1 & 0 \\ -2 & 3 \\ 4 & -1 \end{bmatrix}$ について、行列の積 $AB$ を計算せよ（$BA$ は計算できないことを理由付きで記述）。

**解答**：

AB の計算：

$A$ は 2 行 3 列、$B$ は 3 行 2 列 → 結果は 2 行 2 列

- (1,1)：$3\cdot 1 + (-1)\cdot (-2) + 2\cdot 4 = 3 + 2 + 8 = 13$
- (1,2)：$3\cdot 0 + (-1)\cdot 3 + 2\cdot (-1) = 0 - 3 - 2 = -5$
- (2,1)：$0\cdot 1 + 5\cdot (-2) + (-4)\cdot 4 = 0 - 10 - 16 = -26$
- (2,2)：$0\cdot 0 + 5\cdot 3 + (-4)\cdot (-1) = 0 + 15 + 4 = 19$

$$ AB = \begin{bmatrix} 13 & -5 \\ -26 & 19 \end{bmatrix} $$

なぜ $BA$ は計算できないか：
- $B$ は 3 行 2 列、$A$ は 2 行 3 列
- $BA$ の計算では、$B$ の列数（2）と $A$ の行数（2）が一致する → あえて見ると計算可能。

ただし、一般的な積のルールでは、左因子の列数が右因子の行数に一致する必要がある。本問題では $B \cdot A$ で計算可能。

補足：
問題の前提として「計算できない」は誤り。実際の $BA$ を計算：

$BA = \begin{bmatrix} 1 & 0 \\ -2 & 3 \\ 4 & -1 \end{bmatrix} \cdot \begin{bmatrix} 3 & -1 & 2 \\ 0 & 5 & -4 \end{bmatrix}$

- (1,1)：$1\cdot 3 + 0\cdot 0 = 3$
- (1,2)：$1\cdot (-1) + 0\cdot 5 = -1$
- (1,3)：$1\cdot 2 + 

---
**回答開始**

**解答方針：**

0. **導入**：
    - 与えられた 3 つの行列 $A$、$B$、$C$ の要素
    - 計算すべき行列積：$AB$、$CA$、$CB$、$AC$、$BC$、$BA$
    - 結果はそれぞれ計算し、整理して提示する
    
1. **計算ルール**：
    - 行・列数が一致しない積（$BA$）は計算不能
    - 行・列数が一致する積は成分ごとの乗算と和を取る

2. **行列の定義**：
    - $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$、$B = \begin
</think>

**解答方針：**

0. **導入**：
    - 与えられた行列 $A$、$B$、$C$ の定義を確認する
    - 計算すべき行列積：$AB$、$CA$、$CB$、$AC$、$BC$、$BA$
    - 結果はそれぞれ計算し、整理して提示する

1. **計算ルール**：
    - 左側の行列の**列数**と右側の行列の**行数**が一致する必要がある
    - 行・列数が一致しない場合（例：$BA$）は計算不能

2. **行列の定義**：
    - $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$
    - $B = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$
    - $C = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$（単位行列）

3. **計算手順**：
    - 各積を順に計算し、結果を提示する

4. **結果の整理**：
    - 計算結果を整理し、交換律の成り立たないことを確認する

5. **結論**：
    - 行列の積は順序依存であることを再確認する

6. **問題の解決**：
    - 与えられた行列に対して、計算可能な積のみを計算し、計算不能な積は理由を記述する

7. **結論**：
    - 行列の積は順序依存であり、交換律は成り立たないことを確認する

8. **最終的な解答**：
    - 計算結果を整理し、問題文の要件に添う形で提示する

9. **補足**：
    - 計算不能な積については、列数と行数の不一致を理由として記述する

10. **結論**：
    - 行列の乗法は順序依存であることを再確認する
    - 単位行列 $C$ の場合、$CA$ と $AC$ は等しいが、$BA$ は計算不能である

**解答：**

以下に与えられた行列 $A$、$B$、$C$ の行列積を計算する。

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

### (1) 行列積 $AB$ の計算

$$
AB = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
$$

- 第 1 行第 1 列：$1 \cdot 0 + 2 \cdot 1 = 2$
- 第 1 行第 2 列：$1 \cdot 1 + 2 \cdot 0 = 1$
- 第 2 行第 1 列：$3 \cdot 0 + 4 \cdot 1 = 4$
- 第 2 行第 2 列：$3 \cdot 1 + 4 \cdot 0 = 3$

$$
AB = \begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix}
$$

### (2) 行列積 $AC$ の計算

$$
AC = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

$A$ は 2×2、$C$ は 3×3 であり、$A$ の列数（2）と $C$ の行数（3）が一致しないため、積 $AC$ は**計算不能**です。

### (3) 行列積 $BC$ の計算

$$
BC = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

積 $BC$ は、$B$ の列数（2）と $C$ の行数（3）が一致しないため、**計算不能**です。

### (4) 行列積 $CB$ の計算

$$
CB = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
$$

積 $CB$ は、$C$ の列数（3）と $B$ の行数（2）が一致しないため、**計算不能**です。

### (5) 行列積 $BA$ の計算

$$
BA = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
$$

- 第 1 行第 1 列：$0 \cdot 1 + 1 \cdot 3 = 3$
- 第 1 行第 2 列：$0 \cdot 2 + 1 \cdot 4 = 4$
- 第 2 行第 1 列：$1 \cdot 1 + 0 \cdot 3 = 1$
- 第 2 行第 2 列：$1 \cdot 2 + 0 \cdot 4 = 2$

$$
BA = \begin{bmatrix} 3 & 4 \\ 1 & 2 \end{bmatrix}
$$

比較：$AB \neq BA$（$AB = \begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix}$、$BA = \begin{bmatrix} 3 & 4 \\ 1 & 2 \end{bmatrix}$）

### (6) 行列積 $CA$ の計算

$$
CA = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
$$

積 $CA$ は、$C$ の列数（3）と $A$ の行数（2）が一致しないため、**計算不能**です。

---

### 結果の整理

- $AB = \begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix}$（計算可能）
- $BA = \begin{bmatrix} 3 & 4 \\ 1 & 2 \end{bmatrix}$（計算可能、かつ $AB \neq BA$）
- $AC$、$BC$、$CB$、$CA$ は計算不能（行列の次元が一致しない）

---

### 結論

行列の積は順序依存であり、交換律（$AB = BA$）は成り立たない。また、行列の次元が異なる場合、積は計算不能である。<|endoftext|><|im_start|>user
次の問題の解答を作成して