---
module_id: C-MEAS-011
title: 円の面積の微積分による導出
band: C
domain: CALC
concept_tags: [circle-area, integral-calculus, limit-process, geometric-summation]
prerequisites:
  - C-CALC-001 # 定積分の基礎
  - C-CALC-002 # 円関数と半径方向座標変換
  - C-CALC-004 # 極限の厳密な記述法
next_modules:
  - C-CALC-015 # 極座標での面積の一般化
source_references:
  - id: SRC-001
    title: "高等数学（積分学）入門"
    url: "https://www.jstage.jst.go.jp/article/ijmeij/1/0/1_1_130"
    license: "CC BY-NC-SA"
  - id: SRC-002
    title: "数学I・II・III 学習指導要領"
    url: "https://www.mext.go.jp/a_menu/shotou/nenkou/gakushu_yourei_kourin/2.htm"
    license: "CC BY"
license: CC BY 4.0
---

## 概念説明

円の面積を定積分を用いて厳密に導出する手法は、積分学の基礎理論（面積関数の性質、極限の定義、被積分関数の対称性）を理解した上で必要とされる概念である。

本モジュールでは、円面積の導出を以下の 3 段階で扱う。

1. **放射状のスライス**: 円の中心から半径方向に分割し、各微小領域を極座標で表現する
2. **積分の適用**: カルテン（直角座標）または極座標を適切に設定した上で面積関数を積分する
3. **極限の厳密性**: 分割の幅が 0 に近づく過程を「近似」ではなく「極限値として扱う」ことを明確にする

## 例題

### 例題 1: 直角座標による導出（上半円の関数）

半径 \( R \) の円において、上半円の面積を \( y = \sqrt{R^2 - x^2} \) を使って積分することで求める。

**解答**:

圆的上半分方程式：
\[
y = \sqrt{R^2 - x^2}
\]

円の面積は上下対称なので、上半円の面積の 2 倍として計算する：

\[
A = 2 \int_{-R}^{R} \sqrt{R^2 - x^2} \, dx
\]

三角関数の置換 \( x = R \sin \theta \)，\( dx = R \cos \theta \, d\theta \) を適用する：

\[
\begin{aligned}
\int \sqrt{R^2 - x^2} \, dx &= \int \sqrt{R^2 - R^2 \sin^2 \theta} \cdot R \cos \theta \, d\theta \\
&= \int R \cos \theta \cdot R \cos \theta \, d\theta \\
&= R^2 \int \cos^2 \theta \, d\theta \\
&= R^2 \int \frac{1 + \cos 2\theta}{2} \, d\theta \\
&= \frac{R^2}{2} \left( \theta + \frac{1}{2} \sin 2\theta \right)
\end{aligned}
\]

積分範囲：\( x = -R \Leftrightarrow \sin \theta = -1 \Leftrightarrow \theta = -\frac{\pi}{2} \)

\[
x = R \Leftrightarrow \sin \theta = 1 \Leftrightarrow \theta = \frac{\pi}{2}
\]

\[
\begin{aligned}
A &= 2 \left[ \frac{R^2}{2} \left( \theta + \frac{1}{2} \sin 2\theta \right) \right]_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \\
&= R^2 \left[ \frac{\pi}{2} + \frac{1}{2} \sin \pi - \left( -\frac{\pi}{2} + \frac{1}{2} \sin (-\pi) \right) \right] \\
&= R^2 (\frac{\pi}{2} + \frac{\pi}{2}) \\
&= \pi R^2
\end{aligned}
\]

**採点基準**:

- 公式設定で三角関数置換を記載
- 積分の上下限と結果に矛盾がないこと
- 最終結果が \( \pi R^2 \) と一致すること

---

### 例題 2: 極座標による導出

極座標では、円の面積を放射方向 \( r \) と角度 \( \theta \) の微小要素の積分として求める。

**解答**:

極座標の微小面積要素：
\[
dA = r \, dr \, d\theta
\]

半径 \( R \) の領域全体を積分：

\[
A = \int_{0}^{2\pi} \int_{0}^{R} r \, dr \, d\theta
\]

内側積分（\( r \) について）：
\[
\int_{0}^{R} r \, dr = \left[ \frac{r^2}{2} \right]_0^R = \frac{R^2}{2}
\]

外側積分（\( \theta \) について）：
\[
A = \int_{0}^{2\pi} \frac{R^2}{2} \, d\theta = \frac{R^2}{2} \left[ \theta \right]_0^{2\pi} = \pi R^2
\]

この結果は直角座標の結果と一致する。微積分の厳密な適用により「近似」ではなく正確な導出が可能である。

**採点基準**:

- 極座標変換の微分要素 \( r \, dr \, d\theta \) の根拠が明記
- 積分変数の区間の正当性があるか
- 内外の積分順序が正しく適用されているか

---

## 練習問題

### 問題 1

半径 \( 3 \) の円の面積を微積分で求めなさい。被積分関数の設定を明示し、\( R = 3 \) の代入過程を示すこと。

**解答**:

\[
A = 2 \int_{-3}^{3} \sqrt{9 - x^2} \, dx
\]

定積分の値を計算すると：

\[
\begin{aligned}
A &= 2 \cdot \frac{1}{2} \cdot \pi \cdot 3^2 \\
&= 9\pi \\
&\approx 28.27
\end{aligned}
\]

**採点基準**:

- 積分設定に \( R = 3 \) を正しく代入しているか
- 結果が \( \pi R^2 \) に一致しているか

---

### 問題 2

極座標での微小要素 \( dA \, = \, r \, dr \, d\theta \) が何に基づいて導出されるかを説明し、半径 \( 5 \) の円の面積を導出せよ。

**解答**:

極座標において微小領域は「放射方向の長さ \( r \, dr \)」と「角度 \( d\theta \)」で近似される。この領域は半径 \( r \) の円において直角三角形の面積として \( \frac{1}{2} r^2 d\theta \) と表せるが、積分を \( r \) について行うと微小長方形 \( r \, dr \, d\theta \) として扱える。

積分式：
\[
A = \int_{0}^{2\pi} \int_{0}^{5} r \, dr \, d\theta
\]

\[
\begin{aligned}
A &= \int_{0}^{2\pi} \left[ \frac{r^2}{2} \right]_0^5 \, d\theta \\
&= \int_{0}^{2\pi} \frac{25}{2} \, d\theta \\
&= \frac{25}{2} \cdot 2\pi = 25\pi
\end{aligned}
\]

**採点基準**:

- 微小面積要素の導出根拠が明確に記されているか
- \( \frac{1}{2} r^2 d\theta \) と \( r dr d\theta \) の区別が正しいか
- 最終結果が \( \pi R^2 \) に一致しているか

---

### 問題 3

半径 \( R \) の円において、面積 \( A \) を \( r \)，\( \theta \) 関数の積分として表し、\( R \neq 0 \) の場合に \( A = \pi R^2 \) となることを示せ。さらに、\( f(r) = r^2 \) の関数 \( A = \int_{0}^{R} f(r) \, dr \) の場合、面積 \( A \) がどのように変化するかを説明せよ。

**解答**:

極座標における面積要素は \( r \, dr \, d\theta \) で表される。\( \theta \) について \( 0 \) から \( 2\pi \)，\( r \) について \( 0 \) から \( R \) までの積分として表される：

\[
A = \int_{0}^{2\pi} \int_{0}^{R} r \, dr \, d\theta
\]

積分の順序を変えて計算する：

\[
\begin{aligned}
A &= \int_{0}^{2\pi} d\theta \cdot \int_{0}^{R} r \, dr \\
&= \left( \theta \big|_{0}^{2\pi} \right) \cdot \left( \frac{r^2}{2} \big|_{0}^{R} \right) \\
&= 2\pi \cdot \frac{R^2}{2} \\
&= \pi R^2
\end{aligned}
\]

\( f(r) = r^2 \) の場合：

\[
\begin{aligned}
A_{\text{sub}} &= \int_{0}^{R} r^2 \, dr \\
&= \frac{R^3}{3}
\end{aligned}
\]

これは円の面積ではなく、被積分関数そのものが \( r^2 \) に変化した新しい面積関数である。つまり、関数の指数が \( 1 \) から \( 2 \) に変化した場合、面積の計算方法自体が変化し、\( \pi R^2 \) の公式は失われる。

**採点基準**:

- 積分変数の範囲が「角度 \( 0 \sim 2\pi \) 」「半径 \( 0 \sim R \)」で明示されているか
- 積分順序の交換が正当に記述されているか
- \( f(r) = r^2 \) の場合の変化が積分結果で明確に表されているか

---

## 問題生成ルール

以下のルールにより問題を作成する：

- 問題の難易度：C レベル（定積分の基礎から極限の厳密な扱いくらい）
- 被積分関数：\( \sqrt{R^2 - x^2} \) または \( r \, dr \, d\theta \) の基本形を使用
- 積分変数：\( x \) または \( r \)，\( \theta \)
- 結果の型：\( \pi R^2 \) または \( \frac{R^3}{3} \)
- 問題文は日本語に限定し、数式は LaTeX で表現

---

## 学習上の差異

日本における数学科目において、円の面積の積分による導出は主に以下の観点で扱われることが多いため意識すること：

- 高校数学では通常「図形積分」として扱い、極限の意味合いは深掘りされにくい
- 大学では極座標変換の厳密性を重視し、\( r \, dr \, d\theta \) の導出に焦点を当てる
- 本モジュールでは「近似」ではなく「極限」として扱う厳密さを維持する

---

## 補足ノート

- 積分の厳密な極限処理において「\( \lim_{\Delta \to 0} \)」の記述は必要不可欠
- 極座標変換におけるヤコビアンの意義は、微小要素の面積計算において \( r \) 因子が現れる理由を説明する
- 近似式から極限へ移行する際、被積分関数の連続性や一様収束の概念を念頭に置く
- 三角関数の置換や積分計算の正確さは C レベルでの必須スキルとして定着させる

---
#endofdoc
---
module_id: C-MEAS-011
title: 圆的面积通过微积分导出
band: C
domain: CALC
concept_tags: [circle-area, 积分微积分, 极限过程, 几何求和]
prerequisites:
  - C-CALC-001 # 定积分基础
  - C-CALC-002 # 圆函数与极坐标变换
  - C-CALC-004 # 极限的严格描述方法
next_modules:
  - C-CALC-015 # 极坐标中的面积推广
source_references:
  - id: SRC-001
    title: "高等数学（积分学）入门"
    url: "https://www.jstage.jst.go.jp/article/ijmeij/1/0/1_1_130"
    license: "CC BY-NC-SA"
  - id: SRC-002
    title: "数学I・II・III 学习指导要领"
    url: "https://www.mext.go.jp/a_menu/shotou/nenkou/gakushu_yourei_kourin/2.htm"
    license: "CC BY"
license: CC BY 4.0
---

## 概念说明

通过定积分严格导出圆面积的这种方法，需要理解面积函数的性质、极限定义以及被积函数的对称性等微积分基本概念才能掌握。

本模块将按以下 3 个阶段推导圆面积：

1. **径向切片**：将圆按从中心向外的方向分割，并用极坐标表示每个微小区域。
2. **积分应用**：在直角坐标系或极坐标系中 appropriately 设置面积函数进行积分。
3. **严格性极限**：将分割宽度趋近于 0 的过程明确为“极限值”而非“近似”。

## 例题

### 例题 1：直角坐标推导（上半圆函数）

在半径 \( R \) 的圆中，使用 \( y = \sqrt{R^2 - x^2} \) 对上圆面积进行积分：

**解答**:

圆的上半圆方程：
\[
y = \sqrt{R^2 - x^2}
\]

圆面积由于上下对称，计算上半圆面积再乘以 2：

\[
A = 2 \int_{-R}^{R} \sqrt{R^2 - x^2} \, dx
\]

使用三角代换 \( x = R \sin \theta \)，\( dx = R \cos \theta \, d\theta \)：

\[
\begin{aligned}
\int \sqrt{R^2 - x^2} \, dx &= \int \sqrt{R^2 - R^2 \sin^2 \theta} \cdot R \cos \theta \, d\theta \\
&= \int R \cos \theta \cdot R \cos \theta \, d\theta \\
&= R^2 \int \cos^2 \theta \, d\theta \\
&= R^2 \int \frac{1 + \cos 2\theta}{2} \, d\theta \\
&= \frac{R^2}{2} \left( \theta + \frac{1}{2} \sin 2\theta \right)
\end{aligned}
\]

积分范围：\( x = -R \Leftrightarrow \theta = -\frac{\pi}{2} \)

\[
x = R \Leftrightarrow \theta = \frac{\pi}{2}
\]

\[
\begin{aligned}
A &= 2 \left[ \frac{R^2}{2} \left( \theta + \frac{1}{2} \sin 2\theta \right) \right]_{-\frac{\pi}{2}}^{\frac{\二}{}
\frac{2 \pi}{2} - (-\frac{2 \pi}{2})
} }^{ \frac{ \pi}{2}}
\]

\[
&= 2 \left[ \frac{R^2}{2} \left( \frac{\pi}{2} - (-\frac{\pi}{2}) + \frac{