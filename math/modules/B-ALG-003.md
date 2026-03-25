module_id: "C-ALG-042"
title: "二次関数と二次方程式：解と因数分解"
band: "C"
domain: "ALG"
concept_tags:
  - "quadratic_equations"
  - "discriminant"
  - "factorization"
  - "vertex_form"
prerequisites:
  - "basic_algebraic_operations"
  - "roots_of_linear_equations"
next_modules:
  - "polynomial_equations"
source_references:
  - "Japanese_Mathematics_Curriculum"
  - "Algebra_2_Standards"
locale_notes:
  ja-JP: "高水準の数学教育カリキュラムに準拠します。平方数でない Discriminant の場合の扱いに注意が必要です。"
language: "ja-JP"
status: "reviewed"
content: "module_id: C-ALG-042
title: 二次関数と二次方程式：解と因数分解
band: C
domain: ALG
concept_tags:
  - quadratic_equations
  - discriminant
  - factorization
  - vertex_form
prerequisites:
  - basic_arithmetic
  - linear_equations
next_modules:
  - polynomial_equations
source_references:
  - Japanese_Curriculum_Mathematics
  - Algebra_2_Standards
locale_notes:
  ja-JP: 日本および米国の数学教育カリキュラムに基づいた解説をします。平方完成や因数分解の正確な使い分けが重要です。
language: ja-JP
status: reviewed
content:|
  # 二次関数と二次方程式：解と因数分解

  このモジュールでは、二次方程式の解法、判別式（Discriminant）の計算、平方完成を用いた頂点座標の求め方について詳しく解説します。

  ## 1. 判別式 D と因数分解

  二次方程式 $ax^2 + bx + c = 0$ の解は、公式
  $$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$
  で求められます。ここで、$D = b^2 - 4ac$ は「判別式」と呼ばれます。

  判別式 $D$ の値によって、方程式の解の性質が変化します。

  ### 定理（因数分解と判別式の関係）
  係数が有理数のとき、方程式 $ax^2 + bx + c = 0$ が有理数の根（因数分解可能な形）を持つためには、$D$ が完全平方数でなければなりません。

  - **$D > 0$ で完全平方数**: 2 つの有理数の解があり、因数分解できます。
  - **$D > 0$ で不完全平方数**: 2 つの異なる実数の解がありますが、無理数解のため因数分解（整数・分数の範囲）はできません。
  - **$D = 0$**: 1 つの実数の解（重解）があり、$(x - r)^2 = 0$ の形になります。
  - **$D < 0$**: 実数の解は存在しません。

  ## 2. 例題 A：因数分解可能な方程式

  **問題**: $x^2 - 5x + 6 = 0$ を解なさい。

  **解答**:
  まず、$a=1, b=-5, c=6$ です。
  判別式を計算します。
  $$ D = b^2 - 4ac = (-5)^2 - 4(1)(6) = 25 - 24 = 1 $$
  $D=1$ は完全平方数です。**したがって、因数分解できます。**

  $$x^2 - 5x + 6$$
  2 つの整数 $m, n$ を見つけ、$(x-m)(x-n)$ のような形にします。
  ※ $m+n = -(-5) = 5$、$mn = 6$ を満たす整数は $2, 3$ です。
  $$x^2 - 5x + 6 = (x-2)(x-3) = 0$$

  よって、解は $x=2$ または $x=3$ です。

  ## 3. 例題 B：因数分解の限界（解の公式を使います）

  **問題**: $x^2 - 4x - 9 = 0$ を解なさい。

  **解答**:
  まず、$a=1, b=-4, c=-9$ です。
  判別式を計算します。
  $$ D = (-4)^2 - 4(1)(-9) = 16 + 36 = 52 $$
  $D=52$ は完全平方数ではありません（$7^2=49, 8^2=64$）。**したがって、整数や分数の範囲では因数分解はできません。**
  （※実際には無理数解を持ちます）

  解の公式を用いる必要があります。
  $$ x = \frac{-(-4) \pm \sqrt{52}}{2(1)} = \frac{4 \pm 2\sqrt{13}}{2} = 2 \pm \sqrt{13} $$

  ## 4. 平方完成

  放物線の頂点座標を求めるには、平方完成が効果的です。
  $$y = ax^2 + bx + c$$
 を
  $$ y = a(x + \frac{b}{2a})^2 + (c - \frac{b^2}{4a}) $$
 の形に変形します。

  **例題**: 放物線 $y = x^2 - 6x + 7$ の頂点を求めなさい。

  **解答**:
  $a=1, b=-6$ なので、軸（対称軸）は $x = -\frac{-6}{2} = 3$ です。

  平方完成：
  $$y = 1(x^2 - 6x + 9) - 9 + 7$$
  $$ y = 1(x-3)^2 - 2 $$
  よって、頂点は $(3, -2)$ となります。

  ## 5. 学習のポイントと注意点

  1. **因数分解が失敗する場合**: 判別式 $D$ が完全平方数でない場合（無理数解を持つ場合）、因数分解の公式を使おうとすると正しく求められません。そのときは必ず解の公式 $x = \frac{-b \pm \sqrt{D}}{2a}$ を使いましょう。
  2. **展開と因数分解の逆過程**:
     - $(x+m)(x+n) = x^2 + (m+n)x + mn$ は成り立ちます。
     - $(x+m)^2 \neq x^2 + m^2$ 注意が必要です。$(x+m)^2 = x^2 + 2mx + m^2$ です。
     - 符号の間違いに注意（特に $b$ の符号）してください。

  ## 6. 参考文献と歴史的背景

  - **参考文献**:
    - 教育課程における数学（日本）および Algebra（米国）の基準。
  - **歴史的背景**:
    - 判別式という概念は 1679 年に数学者 Euler によって導入されたと言われています。
    - 平方数以外の値を持つ Discriminant によって、二次方程式が有理数で解を持つことができないことを示しています。

  ## 7. 練習問題

  以下の練習問題を解いてご自身の理解を確認してください。

  1. **因数分解**: $x^2 - 6x + 8 = 0$ を因数分解し、解を求めなさい。
     *解*: $D = 36 - 32 = 4$ （完全平方数）。解は $x=2, x=4$。*
  2. **解の公式の利用**: $x^2 - 2x - 1 = 0$ を解なさい。
     *解*: $D = 4 + 4 = 8$。$D$ が完全平方数でないため解は無理数。$x = 1 \pm \sqrt{2}$。*
  3. **平方完成**: 放物線 $y = 2x^2 + 8x + 10$ の頂点を求めなさい（$y = a(x-h)^2 + k$ にしなさい）。
     *解*: 軸は $x = -4/4 = -2$。$y = 2(x+2)^2 + 2$。*（頂点は $(-2, 2)$*）
  4. **誤解の排除**: $(x+2)^2$ を展開しなさい。
     *解*: $x^2 + 4x + 4$ です。これと $x^2+4$ を混同しないでください。

  解答を求め、間違えた部分の解説は以下の通りです：
  - 因数分解は整数の範囲で考える場合、$D$ が完全平方数でなければ因数分解（乗法要素に整数を持つ）は成立しません。
  - 平方完成で頂点の $y$ 座標を求める際は、括弧外に係数がある場合、計算を慎重に行う必要があります。

  ---

  **結論**:
  二次方程式を解く際、因数分解が効いているかどうかを確認するためには、常に判別式 $D=b^2-4ac$ を計算して、それが完全平方数であるかどうかを確認する慣習がおすすめです。有理数解を持たない方程式（$D$ が平方数でない）については、無理数を含む解の形で表すのが一般的です。

  ```html
  <article itemscope itemtype="http://schema.org/EducationalOccupationalProgram">
    <h1 itemprop="name" lang="ja-JP">二次関数と二次方程式：解と因数分解</h1>
    <section itemprop="about" itemscope itemtype="http://schema.org/Course">
      <h2 itemprop="name">1. 判別式 D と因数分解</h2>
      <img itemprop="image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Parabola.svg/1200px-Parabola.svg.png" alt="放物線グラフ">
      <p itemprop="description">二次方程式の解の性質を判別式 D で理解します。</p>
      <details></details>
      <p>二次方程式
      $$ ax^2 + bx + c = 0 $$
      を因数分解可能な形 $a(x-r_1)(x-r_2)$ にするには、$D = b^2 - 4ac$ が有理数の平方数である必要があります。</p>
    </section>
    <section itemprop="about" itemscope itemtype="
```