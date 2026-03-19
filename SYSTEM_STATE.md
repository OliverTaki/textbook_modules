# SYSTEM_STATE
<!-- Qwen・Claude 両方が参照。Qwen がループ起動時に最初に読む。 -->

status: idle
<!-- 有効値: running / idle / hold / error / stop -->

last_updated: 2026-03-19T00:00:00Z
updated_by: init

current_task: none
current_role: none
current_module: none

## ステータス定義
| status  | 意味                                 | 次の行動           |
|---------|--------------------------------------|--------------------|
| running | Qwen がリレー実行中                  | 干渉しない         |
| idle    | 全タスク完了・待機中                 | 新タスク追加待ち   |
| hold    | 稟議待ち・差し戻し・要人間判断       | 人間が HOLD_QUEUE を確認 |
| error   | エラー検知（3回連続など）            | ERROR_LOG を確認   |
| stop    | 停止対象操作検知・即時停止           | 人間のみ再起動可   |
