---
module_id: D-CALC-004
title: 体積と回転体の弧の長さ
band: D
domain: CALC
concept_tags:
  - volume-of-revolution
  - arc-length
  - integration
  - paraboloid
  - solids-in-calculus
prerequisites:
  - C-CALC-001
next_modules:
  - D-CALC-005
source_references:
  - id: SRC-A-001
    title: University Calculus Textbook
    license: CC BY-NC-ND
locale_notes:
  ja-JP:
    grade: 大学数学
    curriculum: 微積基礎
language: ja
status: reviewed
license: CC BY
---
## 概念説明

本モジュールでは、二重積分や積分の応用として、回転体の体積と曲線の弧の長さの積分計算を解説する。主な焦点は、回転軸を $x$ 軸とし、関数 $y=(x-1)^2$ を領域 $0 \leq x \leq 1$ で回転させた体積、およびその曲線の長さを求めることである。

### 体積の計算原理

回転体の体積は、円盤法（disk method）または輪法（washer method）を用いて計算する。$y=f(x)$ と $x$ 軸で囲まれた領域を $x$ 軸の周りに回転させた体積 $V$ は、公式
\[ V = \pi \int_{a}^{b} [f(x)]^2 \, dx \]
によって求められる。ここで、$f(x)=y$ であり、被積分関数は円の面積 $\pi r^2$ （$r=y$）の積分である。

### 弧の長さの計算原理

曲線 $y=f(x)$ の $a \leq x \leq b$ での弧の長さ $L$ は、勾配公式から以下の積分である。
\[ L = \int_{a}^{b} \sqrt{1 + [f'(x)]^2} \, dx \]
この式は $dx$（$x$ に関する微分）を含み、$dy$ ではなく $x$ を独立変数として表現することを示している。

## 例題

### 例題 1: 放物線による回転体の体積

**問題:** 関数 $y=(x-1)^2$ と $x$ 軸で囲まれた領域 $0 \leq x \leq 1$ を $x$ 軸の周りに 1 回転させたときできる体積を求めよ。

**【解説】**

被積分関数は $f(x)=(x-1)^2$ であり、積分範囲は $a=0, b=1$ である。

1.  $f(x)$ を 2 乗する
    \[ [f(x)]^2 = [(x-1)^2]^2 = (x-1)^4 \]
2.  積分定数 $\pi$ を係数として積分式に代入
    \[ V = \pi \int_{0}^{1} (x-1)^4 \, dx \]
3.  置換積分または展開で計算する
    \[ \int (x-1)^4 \, dx = \frac{1}{5}(x-1)^5 + C \]
4.  上下限を代入し計算
    \[ V = \pi \left[ \frac{1}{5}(x-1)^5 \right]_{0}^{1} \]
    \[ V = \pi \left\{ \frac{1}{5}(1-1)^5 - \frac{1}{5}(0-1)^5 \right\} \]
    \[ V = \pi \left\{ 0 - \frac{1}{5}(-1) \right\} = \pi \left( \frac{1}{5} \right) \]
5.  最後に式を整理
    \[ V = \frac{\pi}{5} \]

**【解答】**

体積は $\frac{\pi}{5}$ 立方単位である。

**【注意点】**

- 「$1 \leq x$」のときに体積が計算不能であると主張するのは誤りである。定義域は $x$ 軸周りの回転領域 $0 \leq x \leq 1$ であり、積分範囲内では常に正の体積を定義する。
- 積分の微分要素として $x\,dx$ を用いる表現ではなく、定積分の標準的な形式として $\pi \int [f(x)]^2 \, dx$ と書くことが重要である。

### 例題 2: 放物線の弧の長さ

**問題:** 関数 $y=(x-1)^2$ およびその導関数を考慮し、$0 \leq x \leq 1$ における曲線の長さ $L$ を計算せよ。

**【解説】**

1.  導関数を求める
    \[ f'(x) = \frac{d}{dx}[(x-1)^2] = 2(x-1) \]
2.  勾配公式に代入し、$L$ を定義する
    \[ L = \int_{0}^{1} \sqrt{1 + [f'(x)]^2} \, dx = \int_{0}^{1} \sqrt{1 + [2(x-1)]^2} \, dx \]
    \[ L = \int_{0}^{1} \sqrt{1 + 4(x-1)^2} \, dx \]
3.  この積分は部分積分または三項式分解（または置換）で可能であるが、標準的な公式 $ \int \sqrt{a^2+u^2} \, du $ を活用する。
    置換 $u = 2(x-1)$ とする（$du = 2\,dx$）。
    積分範囲は $x=0 \Rightarrow u=-2$, $x=1 \Rightarrow u=0$ となる。
    \[ L = \frac{1}{2} \int_{-2}^{0} \sqrt{1 + u^2} \, du \]
    標準積分公式を使うと、$ \int \sqrt{1+u^2} \, du = \frac{1}{2} \left[ u \sqrt{1+u^2} + \ln(u+\sqrt{1+u^2}) \right] $
4.  上下限を代入
    \[ L = \frac{1}{4} \left[ \left( 0 \cdot 1 + \ln(0+1) \right) - \left( (-2)\sqrt{1+(-2)^2} + \ln(-2+\sqrt{1+(-2)^2}) \right) \right] \]
    \[ L = \frac{1}{4} \left[ 0 - \left( -2\sqrt{5} + \ln(\sqrt{5}-2) \right) \right] \]
    \[ L = \frac{1}{4} \left( 2\sqrt{5} - \ln(\sqrt{5}-2) \right) \]
    さらに $\ln(\sqrt{5}-2) = -\ln(\frac{\sqrt{5}+2}{1}) = -\ln(\sqrt{5}+2)$ 変形も可能。
    \[ L = \frac{1}{2} \sqrt{5} + \frac{1}{4} \ln(7.5) \]

**【解答】**

長さ $L = \frac{1}{2} \sqrt{5} - \frac{1}{4} \ln(\sqrt{5}-2)$ である。

**【解釈】**

この値は放物線が弧形状を持つため、直線距離（$1+1=2$）よりも長いが、楕円や円弧に比べて短い。

## 練習問題

### 問題 1

**問題文:**
関数 $y=x^2$ で囲まれた領域 $0 \leq x \leq 1$ を $x$ 軸の周りに 1 回転させた回転体の体積を求めなさい。

**解答:**
\[
\begin{aligned}
V &= \pi \int_{0}^{1} (x^2)^2 \, dx \\
&= \pi \int_{0}^{1} x^4 \, dx \\
&= \pi \left[ \frac{1}{5}x^5 \right]_{0}^{1} \\
&= \frac{\pi}{5}
\end{aligned}
\]

**採点基準:**
- 積分式が $y^2$ を用いて正しいか確認（$y=(x^2)^2$）。
- 係数 $\pi$ の位置が適切か確認。
- 上限 1、下限 0 の計算結果が $\pi/5$ であるか確認。

### 問題 2

**問題文:**
放物線 $y=x^2$ 上の点 $(1,1)$ から点 $(0,0)$ までの弧の長さを求めよ。

**问题文**
関数 $y=x^2$ で囲まれた領域 $0 \ problems
 problems
 problems
 problems
 problems