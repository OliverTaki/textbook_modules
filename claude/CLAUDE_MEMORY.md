# CLAUDE_MEMORY
<!-- Claude が監査セッション開始時に読む。監査後に更新する。 -->

## project 固有の記憶

spec_version: v0.2
relay_order: Researcher → Editor → Professor → Critical Thinker → Editor-in-Chief → PM
change_classification:
  通常変更: モジュール生成・編集・ログ記録 → Qwen 自走可
  稟議対象: 新スキル追加・フォーマット変更・新ディレクトリ → HOLD・人間判断
  停止対象: 外部公開・認証情報変更・仕様変更 → stop・人間のみ再起動可

## 監査履歴（最新10件）
<!-- フォーマット: TIMESTAMP | SYSTEM_STATE | RUN_LOG新規エントリ数 | HOLD件数 | 対応内容 -->

2026-03-19T00:00:00Z | idle | 1 | 0 | 初期化確認

## 権限境界（変更禁止）
Claude が触ってよいファイル: SYSTEM_STATE.md / HOLD_QUEUE.md / ERROR_LOG.md / CLAUDE_MEMORY.md / CLAUDE_PERSONALITY.md / CLAUDE_SKILLS.md
Claude が触ってはいけないファイル: modules/ 以下 / TASK_QUEUE.md / ROLE_*.md / scripts/ 以下
