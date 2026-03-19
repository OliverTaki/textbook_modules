# CLAUDE_SKILLS
<!-- Claude が監査時に使う操作スキル一覧。触ってよいファイルと操作を定義。 -->

## 触ってよいファイルと操作

| ファイル               | 許可操作                        | 禁止操作            |
|------------------------|----------------------------------|---------------------|
| SYSTEM_STATE.md        | 読む / hold・error・stop に変更  | running/idle への変更|
| HOLD_QUEUE.md          | 読む / 承認コメントを追記        | タスクの削除        |
| ERROR_LOG.md           | 読む / 原因コメントを追記        | エントリの削除      |
| CLAUDE_MEMORY.md       | 読む / 監査履歴を更新            | 権限境界の無断変更  |
| CLAUDE_PERSONALITY.md  | 読む / 人格ドリフト検知時に補修  | 禁止事項の削除      |
| CLAUDE_SKILLS.md       | 読む                             | 変更                |

## 触ってはいけないファイル（絶対禁止）
- modules/ 以下（生成物）
- TASK_QUEUE.md
- ROLE_*.md
- MODULE_SCHEMA.md
- scripts/ 以下

## stop / hold の判断基準

| 条件                                           | 対応                                           |
|------------------------------------------------|------------------------------------------------|
| 同一エラーが3回連続（ERROR_LOG で確認）        | SYSTEM_STATE → "hold"                          |
| RUN_LOG が1時間以上更新なし（running 状態）   | SYSTEM_STATE → "hold"                          |
| HOLD_QUEUE に48時間以上未処理タスクが存在      | 人間にエスカレーション（通知のみ）             |
| リレー順序の逆転を検知（RUN_LOG で確認）       | ERROR_LOG にコメント追記 → SYSTEM_STATE → hold |
| 外部公開・認証情報変更の痕跡                   | SYSTEM_STATE → "stop" → 人間に即時通知        |

## 通常監査チェックリスト（1時間サイクル）
1. SYSTEM_STATE.md を読む → stop ならそれ以上の操作をしない
2. RUN_LOG.md で前回監査からの新規エントリを確認
3. HOLD_QUEUE.md で未処理 HOLD を確認
4. ERROR_LOG.md で新規エラーを確認
5. 異常なければ CLAUDE_MEMORY.md の監査履歴を1行追記して終了
6. 異常あれば stop/hold 基準に従い対応
