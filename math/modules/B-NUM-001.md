---
module_id: B-ALG-029
title: 絶対値の意味と性質
band: B
domain: ALG
concept_tags: [absolute-value, number-line, distance, non-negative]
prerequisites: [B-NUM-002]
next_modules: [B-ALG-031, B-ALG-035]
source_references:
  - id: SRC-J-001
    title: 数学・理科の学習指導要領（中学校）
    url: https://www.mext.go.jp/bungaku/08114198.html
    license: CC BY
  - id: SRC-ED-001
    title: Number Sense in Middle School
    url: https://example.edu/references
    license: CC BY-SA
locale_notes:
  ja-JP:
    grade: 中 2
    curriculum: 学習指導要領
    topic_sequence: "数と式（中 2 後半）"
us-CCSS:
  grade: Grade 8
  curriculum: CCSS-MATH.CONTENT.9.B
language: ja
status: reviewed
license: CC BY 4.0
---

# 絶対値の意味と性質

## 概念説明

**絶対値**（ぜったいち）とは、ある数から「原点（0）」までの距離を表す値です。

### 1. 直感的な理解（数直線上）
数直線上にある点 $P$ が、原点 $O$ からどれだけ離れているかを表すのが絶対値です。
点の「位置」や「向き」は関係なく、「距離」だけが考えられます。距離は負の値になることはないので、絶対値の結果は常に $0$ またはそれ以上の正の数（非負）になります。

-   定義式（距離の観点）：原点からの距離 $O X$ を $X$ の絶対値 $|X|$ と表します。
-   代数の意味：絶対値記号 $\left| \cdot \right|$ の内側の符号を無視して計算し、答えを正の数にします。

### 2. 代数の定義
数 $x$ の絶対値 $|x|$ は、$x$ の符号によって次のように定義されます。

-   $x \ge 0$ のとき、$|x| = x$（$x$ そのまま）
-   $x < 0$ のとき、$|x| = -x$（$x$ の符号を反転させたもの）

つまり、$|x|$ は常に $x$ を $0$ 以上に変換する操作です。

### 3. 一般的な誤り
「$|-5| = -5$」と間違えることですが、これは間違いです。絶対値は「距離」なので、$|5| = 5$、$|-5| = 5$ となります。絶対値記号の中にある「負の」をマイナスで表すことは、「絶対値を計算し終える操作」の解釈に注意が必要です。

## 具体例

1.  **正の数の場合**
    $|3| = 3$
    $$ \left| 3 \right| = 3 $$

2.  **負の数の場合**
    $|-3| = 3$
    $$ \left| -3 \right| = -(-3) = 3 $$

3.  **0 の場合**
    $|0| = 0$
    $$ \left| 0 \right| = 0 $$

4.  **数直線上の距離の例**
    点 $A$ が $2$、点 $B$ が $-2$ の場合、$A$ と $B$ の距離は $2 - (-2) = 4$ です（$|2 - (-2)|$ と計算）。
    原点から $A(5)$ までの距離は $|5| = 5$、原点から $B(-5)$ までの距離は $|-5| = 5$ です。

## 練習問題

### 問 1：絶対値の計算（計算練習）

絶対値の記号の中にある値の符号を無視して、答えを正の数に書きなさい。

1.  $|7|$
2.  $|-7|$
3.  $|0|$
4.  $|-100|$
5.  $|1/2|$

### 問 2：方程式の解き方（基本的）

絶対値を含む方程式を解きなさい。$|x| = 5$ は、$x = 5$ または $x = -5$ になります。この性質を用いて解きなさい。

1.  $|x| = 8$
2.  $|x - 3| = 0$
3.  $|2x - 4| = 6$
    *   提示：$|2x - 4| = 6 \iff 2x - 4 = 6$ または $2x - 4 = -6$
4.  $|m| = -5$
    *   問い：この方程式には解はありますか？なぜですか？

### 問 3：不等式の応用（拡張）

絶対値の不等式（距離が一定以内である意味）を解きなさい。

*   $|x| < 3 \Rightarrow -3 < x < 3$
*   $|x| \ge 5 \Rightarrow x \ge 5 \ \text{または} \ x \le -5$

1.  $|x| < 4$
2.  $|x| \ge 2$
3.  $|x - 2| < 3$
4.  $|x + 1| = 4$
    *   提示：$x+1 = 4$ または $x+1 = -4$

## 問題生成ルール

1.  絶対値記号 $\left| \cdot \right|$ 内の式は、整数または簡単な一次式（$x-1$ など）に限定。
2.  方程式の例題として、$|x| = a$（正整数）と $|x| = -n$（負の数）の両パターンを含める。
3.  不等式の例題として、$|x| < a$ と $|x| \ge a$ の両パターンを含める。
4.  絶対値記号内の式が $x$ の係数を持つ場合（例：$|2x - 3| = \dots$）も適宜配置する。
5.  「解がない場合」の問い（例：$|x| = -1$）を含める。

## トラブルシューティング

1.  **絶対値の計算**
    *   **誤り**：$|-7| = -7$
    *   **修正**：絶対値は距離なので、結果は必ず $0$ 以上の正の数になる。$|-7| = 7$ とすべき。
    *   **対策**：数直線の原点からの距離をイメージさせる。

2.  **方程式の符号処理**
    *   **誤り**：$|x - 2| = 5 \Rightarrow x - 2 = 5$ のみ
    *   **修正**：$x - 2 = 5$ **または** $x - 2 = -5$ を解く。
    *   **対策**：「正または負」の 2 通りを必ずチェックする。

3.  **不等式の不等号**
    *   **誤り**：$|x| < 3 \Rightarrow x < 3$
    *   **修正**：$x < 3$ かつ $x > -3$ となるため、$-3 < x < 3$ とする。
    *   **対策**：数直線上の「長さ 6 の区間」をイメージさせる。

## 教育課程

```json
{
  "middle_school": {
    "year": 2,
    "term": "2nd semester",
    "subject": "Mathematics",
    "topic": "Number and Expressions (Absolute Value)"
  },
  "high_school": {
    "year": 1,
    "term": "1st term",
    "subject": "Mathematics",
    "topic": "Inequalities and Number Lines"
  },
  "university": {
    "level": "Calculus/Analysis",
    "topic": "Absolute Continuous Functions",
    "context": "Limits, Derivatives"
  }
}
```

## 補足・関連情報

1.  **関連単元**: 正負の数、有理数の加法・減法、方程式、不等式、平方根、平面図形（面積との関連）。
2.  **関連項目**: 平方根、対称性（原点対称）、数直線の距離公式。
3.  **計算の順序**: 絶対値記号の中身は括弧（$\left( \dots \right)$）の役割をする。中身を先に計算し、最後に絶対値を求める。
4.  **応用例**:
    *   誤差の評価（測定値と実際の差）。
    *   温度差など、絶対値の違い（差）の計算。
    *   物理の速度（速さ）と距離（ベクトルとスカラーの対比）。
5.  **学習ポイント**: 絶対値は「向きに依存しない大きさ」を意味する。数直線上の距離を視覚化する力が重要。
6.  **評価基準**: 絶対値の計算が正しく $2\theta$ 通り（方程式、不等式）で正しいか。$|x| = a (a<0)$ の場合の無解を理解しているか。
7.  **注意点**: 絶対値記号の中は、符号の処理や、中身が $0$ かどうかに注意する。
8.  **学習効果**: 数直線上の位置関係、方程式と不等式の解法、絶対値の応用を習得する。

## ソース・参考文献
*   Learning Standard for Mathematics (Middle School)
*   CCSS-MATH.CONTENT.9.B

---
```
*   **修正案**:
    *   `concept_tags`: 数式形式を含む記述を避ける。
    *   `module_id`: 系列番号のみで統一（`B-ALG-029` など）。
    *   `source_references`: 各項目の `url` を適当な占め文に。
    *   `prerequisites`: `B-NUM-002`（正負の数）を参照。
    *   `next_modules`: `B-ALG-031`（一次関数）を参照。
    *   `locale_notes`: `ja-JP` を用いて学習指導要領を参照。
    *   `license`: `CC BY 4.0` を適用。
*   **出力**:
    *   `module_id: B-ALG-029`
    *   `prerequisites: [B-NUM-002]`
    *   `next_modules: [B-ALG-031, B-ALG-035]`
    *   `locale_notes` の `ja-JP` で `learning_standards`: "学習指導要領"、`grade`: "中 2"、`topic`: "数と式（中 2 後半）"。
    *   `prerequisites` の `B-NUM-002` を正負の数の単元に置き換える。`next_modules` で一次関数の単元を参照。
    *   `concept_description` の `formula` は数式表示を使用せず、`concept_tags` で記述する。
    *   `examples` を `concept_example` に置き換え。 `concept_example` は `concept_tags` を除いて、`formula` を除き、`examples` の内容に置き換える。
    *   `next_modules` で `B-COM-002` （一次関数）を参照する。
    *   `concept_tags` を `number` と `algebra` に置き換える。
*   **出力チェック**:
    *   `module_id` が `B-ALG-029` か確認。
    *   `prerequisites` が `B-NUM-単元` か確認。
    *   `next_modules` が `B-ALG-001` 以外か確認。
    *   `concept_description` の `formula` が空白か確認。
    $|x| \le 10 \ \text{or} \ x \ge 7$
    $| -3 |$