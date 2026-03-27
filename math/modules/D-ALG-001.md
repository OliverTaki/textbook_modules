---
module_id: D-ALG-001
title: 複素数平面
band: D
domain: ALG
concept_tags: [complex-numbers, complex-plane, real-imaginary-plane, geometric-interpretation]
prerequisites: [C-ALG-011, C-ALG-023]
next_modules: [D-ALG-022]
source_references:
  - id: SRC-001
    title: "複素数入門"
    url: "https://ja.wikipedia.org/wiki/複素数"
    license: "CC BY-SA"
locale_notes:
  ja-JP:
    grade: 3
    curriculum: 高校数学 III
  us-CCSS:
    grade: High School AP Precalc
    curriculum: Complex Numbers Unit
language: ja
status: reviewed
license: CC BY 4.0
---

## 概念説明

複素数 $z = a + bi$（ここで $a, b$ は実数、$i^2 = -1$）は、単なる代数計算の対象を超えて、幾何学的な解釈を持つ。

複素数集合は実平面上の点を表すことができ、これを**複素数平面**（またはガウス平面）と呼ぶ。実軸を実数部 $a$、虚軸を虚数部 $b$ として、点 $(a, b)$ を複素数 $z = a + bi$ に対応させるのが定義である。

複素数平面上で、原点 $O(0,0)$ から点 $z$ を結んだ線分の長さを**絶対値**（または大きさ）$|z|$、$Oz$ が実軸から受ける角度（単位円方向に回転）を**辐角** $\theta$ と定義する。このとき、極形式は
$$z = |z|(\cos\theta + i\sin\theta)$$
または欧拉の公式を用いると
$$z = |z|e^{i\theta}$$
と表せる。

複素数平面は、関数論や制御理論、電気工学、物理学などで不可欠なツールであり、幾何的解釈と代数的操作を結びつける架け橋として機能する。

## 例題

### 例題 1：複素数平面での位置の表示
複素数 $z_1 = 3 + 2i$ および $z_2 = -1 + 4i$ が複素数平面上に与えられている。

（1）$z_1$、$z_2$ を複素数平面で表せ。

（2）$z_1$、$z_2$ の絶対値を計算せよ。

（3）$z_1$ の辐角 $\theta_1$ を弧度数、ラジアン単位で近似せよ。

**解答:**
（1）$z_1 = 3 + 2i$ は複素数平面の点 $(3, 2)$、$z_2 = -1 + 4i$ は点 $(-1, 4)$ で表される。実軸上に 3、虚軸上に 2 を取った点、実軸上に -1、虚軸上に 4 を取った点である。

（2）
$$|z_1| = \sqrt{3^2 + 2^2} = \sqrt{9 + 4} = \sqrt{13}$$
$$|z_2| = \sqrt{(-1)^2 + 4^2} = \sqrt{1 + 16} = \sqrt{17}$$

（3）$z_1$ の辐角 $\theta_1$ は、点 $(3, 2)$ を原点から見た角度である。
$$\tan\theta_1 = \frac{2}{3}$$
$$\theta_1 = \arctan\left(\frac{2}{3}\right) \approx 0.588 \text{ (ラジアン)}$$

### 例題 2：極形式の計算と乗法
複素数 $z_1 = 2(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3})$ および $z_2 = 3(\cos\frac{\pi}{6} + i\sin\frac{\pi}{6})$ とする。

（1）極形式で積 $z_1 z_2$ を計算せよ。

（2）極形式で商 $z_1 / z_2$ を計算せよ。

（3）アルゴリズムとして、乗法・除法の一般的な規則を述べよ。

**解答:**
（1）極形式の乗法：絶対値を掛け、辐角を加える。
$$z_1 z_2 = 2 \cdot 3 \left[\cos\left(\frac{\pi}{3} + \frac{\pi}{6}\right) + i\sin\left(\frac{\pi}{3} + \frac{\pi}{6}\right)\right] = 6\left(\cos\frac{\pi}{2} + i\sin\frac{\pi}{2}\right) = 6i$$

（2）極形式の除法：絶対値を割り、辐角を引く。
$$\frac{z_1}{z_2} = \frac{2}{3} \left[\cos\left(\frac{\pi}{3} - \frac{\pi}{6}\right) + i\sin\left(\frac{\pi}{3} - \frac{\pi}{6}\right)\right] = \frac{2}{3}\left(\cos\frac{\pi}{6} + i\sin\frac{\pi}{6}\right) = \frac{2}{3}\left(\frac{\sqrt{3}}{2} + \frac{1}{2}i\right) = \frac{\sqrt{3}}{3} + \frac{1}{3}i$$

（3）複素数 $z_1 = r_1(\cos\theta_1 + i\sin\theta_1)$、$z_2 = r_2(\cos\theta_2 + i\sin\theta_2)$ に対し、
$$z_1 z_2 = r_1 r_2 (\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2))$$
$$\frac{z_1}{z_2} = \frac{r_1}{r_2} (\cos(\theta_1 - \theta_2) + i\sin(\theta_1 - \theta_2))$$
と表せる。これは極形式による計算の基本ルールである。

## 練習問題

### 問題 1：複素数の加減法の幾何的意味
複素数 $z_1 = 2 + 3i$、$z_2 = 1 - 2i$ とする。

複素数平面で、$z_1 + z_2$ を幾何的な方法（平行四辺形の法則）で説明せよ。また、$z_1 - z_2$ も説明せよ。

**解答:**
複素数 $z_1$ と $z_2$ をベクトルと見做すと、$z_1 + z_2$ はこれら 2 本のベクトルを頭を合わせてつなげた場合の合成ベクトルであり、平行四辺形の法則で表せる。具体例では、$z_1$ のベクトル $(2, 3)$ と $z_2$ のベクトル $(1, -2)$ を足すと $(3, 1)$ となり、$z_1 + z_2 = 3 + i$ である。

$z_1 - z_2$ は $z_1$ から $z_2$ へのベクトルを意味し、$-(1-2i)$ を $z_1$ に加えたものと同値。具体的には、$z_1 - z_2 = 2+3i - (1-2i) = 1+5i$ となり、複素数平面上では $(3, 1)$ から $(1, -2)$ へ向かうベクトルの長さと方向に相当する。

**採点基準:**
- 複素数 $z_1+Z_2$ を複素数平面上で幾何的に説明できる（平行四辺形の法則または三角形の法則を用いる）
- $z_1 - z_2$ を $z_1$ から $z_2$ へのベクトルとして説明できる
- 計算結果が正しい（$z_1 + z_2 = 3+i$、$z_1 - z_2 = 1+5i$）
- 複素数平面の点を座標で表せる

### 問題 2：辐角の範囲について
複素数 $z = -1 + i\sqrt{3}$ の辐角 $\theta$ を、辐角主値の範囲（$-\pi < \theta \le \pi$）で求めよ。

（1）まず、$\tan\theta = \frac{\sqrt{3}}{-1} = -\sqrt{3}$ とする。このとき、$\theta$ の候補を求めよ。

（2）$z$ が第 2 象限の点であることを用いて、辐角の正解を定式せよ。

（3）辐角の一般化（辐角の共通部分 $+\theta_{主} + 2k\pi$）について簡潔に説明せよ。

**解答:**
（1）$\tan\theta = -\sqrt{3}$ となる場合、$\theta = \frac{\pi}{3}$ または $\theta = \frac{4\pi}{3}$ のとき、但し $\tan\theta$ は周期 $\pi$ である。

（2）$z = -1 + i\sqrt{3}$ は実部 $-1$、虚部 $\sqrt{3}$ であり、第 2 象限の点である。第 2 象限での辐角主値の正解は $\theta = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$ である。

（2）辐角は周期 $\pi$ ではなく $\pi$ ではなく $2\pi$ であるため、辐角の一般化 $\theta = \frac{2\pi}{3} + 2k\pi$ ($k$ は整数) であり、辐角主値の定義では $-\pi < \theta \le \pi$ 範囲内に収まる唯一の解は $\frac{2\p