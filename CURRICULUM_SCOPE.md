# Curriculum Scope — textbook_modules

このドキュメントは、データベースに収録する全モジュールのスコープ（予定含む）を定義します。

- **ID形式**: `{BAND}-{DOMAIN}-{NNN}` (BAND-DOMAIN-NNN方式)
- **ステータス**: `available`（利用可能）/ `quarantine`（修復待ち）/ `planned`（未作成）
- **言語**: 日本語優先（`language: ja`）。英語版は将来拡充予定

## BANDの定義

| BAND | 対象 |
|------|------|
| A | 小学校（elementary） |
| B | 中学校（middle school） |
| C | 高校基礎（high school standard） |
| D | 高校発展・理系（high school advanced） |
| E | 大学教養（undergraduate） |

---

## BAND A — 小学校算数

### A-NUM（数の概念・数の体系）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| A-NUM-001 | 1 | 数の概念と数え方（1〜10） | — | available |
| A-NUM-002 | 2 | 10より大きい数（10〜100） | A-NUM-001 | available |
| A-NUM-003 | 2 | 大きい数（〜1000） | A-NUM-002 | planned |
| A-NUM-004 | 3 | 大きい数（〜10000） | A-NUM-003 | planned |
| A-NUM-005 | 4 | 大きい数（億・兆） | A-NUM-004 | planned |
| A-NUM-006 | 3 | 小数の入門 | A-NUM-002 | planned |
| A-NUM-007 | 4 | 小数の計算 | A-NUM-006 | planned |
| A-NUM-008 | 3 | 分数の入門 | A-OPS-003 | planned |
| A-NUM-009 | 4 | 分数の計算（同分母） | A-NUM-008 | planned |
| A-NUM-010 | 5 | 分数の計算（異分母・通分） | A-NUM-009 | planned |
| A-NUM-011 | 6 | 分数の乗除 | A-NUM-010 | planned |
| A-NUM-012 | 5 | 整数の性質（倍数・約数） | A-OPS-002 | planned |

### A-OPS（計算操作）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| A-OPS-001 | 1 | ひき算の基礎 | A-NUM-001 | available |
| A-OPS-002 | 2 | かけ算・九九 | A-OPS-001 | available |
| A-OPS-003 | 3 | わり算の基礎 | A-OPS-002 | planned |
| A-OPS-004 | 4 | 割合（百分率・歩合） | A-OPS-003 | planned |
| A-OPS-005 | 5 | 小数の乗除 | A-NUM-007 | planned |
| A-OPS-006 | 6 | 比と比の値 | A-OPS-004 | planned |
| A-OPS-007 | 6 | 速さ（距離・時間・速さ） | A-OPS-006 | planned |
| A-OPS-008 | 6 | 比例と反比例 | A-OPS-006 | planned |

### A-MEAS（測定・単位）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| A-MEAS-001 | 1 | 長さ・かさ・重さの基礎 | A-NUM-001 | available |
| A-MEAS-002 | 1 | 時刻と時間の基礎 | A-NUM-001 | available |
| A-MEAS-003 | 2 | 長さの単位（cm・m） | A-MEAS-001 | planned |
| A-MEAS-004 | 2 | かさの単位（dL・L） | A-MEAS-001 | planned |
| A-MEAS-005 | 2 | 時刻と時間の計算 | A-MEAS-002 | planned |
| A-MEAS-006 | 3 | 長さ・重さの単位換算 | A-MEAS-003 | planned |
| A-MEAS-007 | 4 | 面積の基礎（正方形・長方形） | A-GEO-001 | planned |
| A-MEAS-008 | 5 | 面積（三角形・平行四辺形・台形） | A-MEAS-007 | planned |
| A-MEAS-009 | 5 | 体積の基礎 | A-MEAS-007 | planned |
| A-MEAS-010 | 5 | 平均・単位量あたり | A-OPS-004 | planned |
| A-MEAS-011 | 6 | 円の面積 | A-GEO-003 | planned |
| A-MEAS-012 | 6 | 立体図形（角柱・円柱・体積） | A-MEAS-009 | planned |

### A-GEO（図形）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| A-GEO-001 | 2 | 三角形と四角形 | — | planned |
| A-GEO-002 | 3 | 三角形の種類・性質 | A-GEO-001 | planned |
| A-GEO-003 | 4 | 角度と分度器 | A-GEO-002 | planned |
| A-GEO-004 | 4 | 垂直・平行と四角形の種類 | A-GEO-002 | planned |
| A-GEO-005 | 5 | 正多角形と円周 | A-GEO-004 | planned |
| A-GEO-006 | 6 | 立体図形の性質 | A-GEO-005 | planned |

### A-STAT（データ・統計）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| A-STAT-001 | 3 | 表とグラフ（棒グラフ） | A-NUM-001 | planned |
| A-STAT-002 | 4 | 折れ線グラフ | A-STAT-001 | planned |
| A-STAT-003 | 5 | 平均と代表値 | A-MEAS-010 | planned |
| A-STAT-004 | 6 | データの整理・場合の数入門 | A-STAT-003 | planned |

---

## BAND B — 中学校数学

### B-NUM（数と式）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| B-NUM-001 | 7 | 正負の数・絶対値 | A-NUM-005 | planned |
| B-NUM-002 | 7 | 正負の数の四則計算 | B-NUM-001 | planned |
| B-NUM-003 | 9 | 平方根・無理数 | B-ALG-001 | planned |

### B-ALG（文字式・方程式）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| B-ALG-001 | 7 | 文字と式・代入 | B-NUM-002 | planned |
| B-ALG-002 | 7 | 一次方程式 | B-ALG-001 | planned |
| B-ALG-003 | 8 | 式の展開と因数分解 | B-ALG-001 | planned |
| B-ALG-004 | 8 | 連立方程式 | B-ALG-002 | planned |
| B-ALG-005 | 9 | 二次方程式 | B-NUM-003 | planned |

### B-FUNC（関数）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| B-FUNC-001 | 7 | 比例と反比例（関数の入門） | A-OPS-008 | planned |
| B-FUNC-002 | 8 | 一次関数 | B-FUNC-001 | planned |
| B-FUNC-003 | 9 | 二次関数（y=ax²） | B-FUNC-002 | planned |

### B-GEO（図形・証明）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| B-GEO-001 | 7 | 平面図形の基礎・合同と相似 | A-GEO-005 | available |
| B-GEO-002 | 7 | 空間図形（立体の性質） | A-MEAS-012 | planned |
| B-GEO-003 | 8 | 平行と合同・証明の基礎 | B-GEO-001 | planned |
| B-GEO-004 | 8 | 三角形の合同条件 | B-GEO-003 | planned |
| B-GEO-005 | 8 | 平行四辺形の性質と証明 | B-GEO-004 | planned |
| B-GEO-006 | 9 | 相似な図形・相似比 | B-GEO-005 | planned |
| B-GEO-007 | 9 | 三平方の定理（ピタゴラス） | B-GEO-006 | planned |
| B-GEO-008 | 9 | 円の性質（円周角・接線） | B-GEO-001 | planned |

### B-STAT（確率・統計）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| B-STAT-001 | 7 | データの分析（度数分布・ヒストグラム） | A-STAT-004 | planned |
| B-STAT-002 | 8 | 確率の基礎 | A-STAT-004 | planned |
| B-STAT-003 | 9 | 標本調査と統計 | B-STAT-001 | planned |

---

## BAND C — 高校数学（基礎）

### C-ALG（代数・式と証明）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| C-ALG-001 | 10 | 多項式の展開と因数分解 | B-ALG-003 | available |
| C-ALG-002 | 10 | 方程式と不等式 | B-ALG-005 | planned |
| C-ALG-003 | 11 | 複素数と方程式 | C-ALG-002 | planned |

### C-FUNC（関数）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| C-FUNC-001 | 10 | 関数の概念・定義域・値域 | B-FUNC-003 | planned |
| C-FUNC-002 | 10 | 二次関数 | C-FUNC-001 | planned |
| C-FUNC-003 | 11 | 指数関数 | C-FUNC-001 | planned |
| C-FUNC-004 | 11 | 対数関数 | C-FUNC-003 | planned |

### C-TRIG（三角関数）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| C-TRIG-001 | 10 | 三角比 sin/cos/tan の定義 | B-GEO-007 | available |
| C-TRIG-002 | 10 | 三角比の応用（正弦定理・余弦定理） | C-TRIG-001 | planned |
| C-TRIG-003 | 11 | 三角関数（一般角・弧度法） | C-TRIG-001 | planned |
| C-TRIG-004 | 11 | 三角関数の加法定理と応用 | C-TRIG-003 | planned |

### C-GEO（図形と方程式）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| C-GEO-001 | 10 | 平面図形・合同と相似（高校版） | B-GEO-006 | planned |
| C-GEO-002 | 11 | 図形と方程式（直線・円） | C-FUNC-002 | planned |
| C-GEO-003 | 11 | 軌跡と領域 | C-GEO-002 | planned |

### C-CALC（微積分基礎）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| C-CALC-001 | 11 | 微分の基礎・導関数 | C-FUNC-002 | available |
| C-CALC-002 | 11 | 積分の基礎・面積計算 | C-CALC-001 | available |

### C-VEC（ベクトル）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| C-VEC-001 | 11 | ベクトルの基礎・演算 | C-TRIG-001 | available |
| C-VEC-002 | 11 | ベクトルの内積・成分計算 | C-VEC-001 | planned |

### C-SEQ（数列）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| C-SEQ-001 | 11 | 数列の基礎・等差数列 | C-ALG-001 | planned |
| C-SEQ-002 | 11 | 等比数列・漸化式 | C-SEQ-001 | planned |
| C-SEQ-003 | 11 | 数学的帰納法 | C-SEQ-002 | planned |

### C-PROB（確率・組み合わせ）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| C-PROB-001 | 10 | 場合の数・順列・組み合わせ | A-STAT-004 | planned |
| C-PROB-002 | 10 | 確率の基礎・事象と確率 | C-PROB-001 | planned |
| C-PROB-003 | 10 | 条件付き確率・独立と従属 | C-PROB-002 | planned |
| C-PROB-004 | 11 | 確率分布・期待値・分散 | C-PROB-002 | planned |

### C-STAT（統計）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| C-STAT-001 | 10 | データの分析・統計の基礎 | B-STAT-001 | planned |
| C-STAT-002 | 11 | 正規分布・統計的推測 | C-PROB-004 | planned |

### C-NUM（整数の性質）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| C-NUM-001 | 10 | 整数の性質・約数と倍数 | A-NUM-012 | planned |
| C-NUM-002 | 10 | 素数・素因数分解・互除法 | C-NUM-001 | planned |

---

## BAND D — 高校数学（発展・理系）

### D-CALC（微積分発展）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| D-CALC-001 | 12 | 極限（数列の極限・関数の極限） | C-SEQ-002 | planned |
| D-CALC-002 | 12 | 微分の発展（合成関数・逆関数） | C-CALC-001 | planned |
| D-CALC-003 | 12 | 積分の発展（置換積分・部分積分） | C-CALC-002 | planned |
| D-CALC-004 | 12 | 体積・曲線の長さ・積分応用 | D-CALC-003 | planned |

### D-ALG（複素数平面・代数発展）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| D-ALG-001 | 12 | 複素数平面 | C-ALG-003 | planned |

### D-FUNC（関数発展）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| D-FUNC-001 | 12 | 分数関数・無理関数 | C-FUNC-001 | planned |
| D-FUNC-002 | 12 | 逆関数・合成関数 | D-FUNC-001 | planned |

### D-VEC（空間ベクトル）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| D-VEC-001 | 12 | 空間ベクトル | C-VEC-002 | planned |

### D-MATR（行列）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| D-MATR-001 | 12 | 行列の基礎・演算 | C-VEC-001 | planned |
| D-MATR-002 | 12 | 行列の応用（連立方程式・変換） | D-MATR-001 | planned |

### D-GEO（2次曲線・極座標）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| D-GEO-001 | 12 | 2次曲線（放物線・楕円・双曲線） | C-GEO-002 | planned |
| D-GEO-002 | 12 | 極座標と極方程式 | C-TRIG-003 | planned |

### D-STAT（統計発展）

| module_id | grade | title | prerequisites | status |
|-----------|-------|-------|---------------|--------|
| D-STAT-001 | 12 | 統計的推定・検定の基礎 | C-STAT-002 | planned |

---

## Summary

| BAND | Total | available | quarantine | planned |
|------|-------|-----------|------------|---------|
| A（小学校） | 34 | 4 | 0 | 30 |
| B（中学校） | 22 | 1 | 0 | 21 |
| C（高校基礎） | 32 | 7 | 0 | 25 |
| D（高校発展） | 11 | 0 | 0 | 11 |
| **合計** | **99** | **12** | **0** | **87** |

### 修復待ちモジュール（quarantine）

以下のモジュールはフォーマット問題のため `tm-work/staging/quarantine/` に隔離中です。
修復後に公開リポジトリへ再追加予定です。

| 旧ID | 問題 | 対応予定ID |
|------|------|-----------|
| ELM-002 | 要確認 | A-OPS-ADD-001 ※ |
| ALG-002 | frontmatter が code block 内に記載 | C-ALG-002 |
| ELM-008 | frontmatter なし | A-NUM-003 |
| ELM-009 | pseudo-metadata（bold記法） | A-GEO-001 |
| ELM-010 | module_id が ELM-001 と重複 | A-MEAS-003 |
| ELM-011 | CT review ドキュメントを誤収録 | — |
| ELM-012 | 要確認 | A-MEAS-005 ※ |
| FUNC-001 | 要確認 | C-FUNC-001 ※ |
| FUNC-002 | 要確認 | C-FUNC-002 ※ |
| STAT-001 | 要確認 | C-STAT-001 ※ |

※ 修復後に内容を確認してから確定ID割り当て

---

*最終更新: 2026-03-23*
