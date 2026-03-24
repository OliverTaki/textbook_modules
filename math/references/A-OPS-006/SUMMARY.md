# ❌ 役割の範囲外

ご提示いただいたタスクは、**私の役割（Librarian）を超えています**。私は「一次資料を収集するだけ」で、以下は行いません：

- 📝 教材本文や要約の執筆
- 📊 資料のまとめ
- ✍️ コンテンツ作成のサポート

## 私の実際の役割

| 許可 | 禁止 |
|-----|------|
| `web_search.collect_references()` を呼び出す | 教材本文を書く |
| `references/{module_id}/` に保存する | 資料要約を作成する |
| `INDEX.md` を生成する | ライセンス確認や品質レビュー |
| 収集結果の報告 | git commit |

## 今回の状況

提供された資料には収集データがありません。そのため：

```
references/A-OPS-006/INDEX.md ← ここで INDEX を生成
references/A-OPS-006/wikipedia.txt ← 空
references/A-OPS-006/ref_*.txt ← 空
```

資料がないため、INDEX.md は空またはエラーログを記録した形になります。

## 適切な役割分け

- 🔍 **Librarian（私）**：資料収集のみ
- 🎓 **Editor**：教材作成（要約を含む）
- ✅ **Professor**：品質レビュー
- 🔎 **Critical Thinker**：事実確認

資料収集が完了したら、Editor 様へ `references/A-OPS-006/` をお渡しします。