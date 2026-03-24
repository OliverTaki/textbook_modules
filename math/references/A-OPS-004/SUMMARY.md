# 司書報告（Librarian Report）

## 現状報告

収集資料がありませんので、要点をまとめることはできません。

## 必要な処理

1. `web_search.collect_references()` を呼び出して：
   - 日本語 Wikipedia の「割合」「百分率」「歩合」関連記事
   - DuckDuckGo で「数学 割合 解説 教材」を DuckDuckGo で検索して上位ページを収集

2. `references/A-OPS-004/` を作成し：
   - `INDEX.md`（収集資料一覧）
   - `wikipedia.txt`（日本語 Wikipedia 記事）
   - `ref_NN.txt`（DDG 検索ページ）

3. 収集後、以下を Editor に提供：
   - 収集資料の要約（どの資料をどう使うか）

## 待機

収集作業が完了するまで待機します。ネットワークエラーで取得不能な場合は ERROR_LOG に記録して、Editor にもう一度収集を依頼します。