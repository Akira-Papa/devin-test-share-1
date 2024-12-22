# ユーティリティ関連のコマンド

## 待機
コマンド名: wait
説明：指定された時間だけ待機します
構文例：`<wait for="user/browser/shell/etc" seconds="seconds"/>`
パラメータ：
- for: 待機対象（user/browser/shell/etc）
- seconds: 待機時間（秒）

## ユーザーへのメッセージ送信
コマンド名: message_user
説明：ユーザーにメッセージを送信します
構文例：
- 通常メッセージ：`<message_user>メッセージ内容</message_user>`
- 添付付きメッセージ：`<message_user attachments="comma_separated_filenames">メッセージ内容</message_user>`
パラメータ：
- attachments: 添付ファイル名（カンマ区切り、オプション）

## 質問
コマンド名: ask
説明：人間のエンジニアリングマネージャーに質問します
構文例：`<ask>質問内容</ask>`
注意事項：絶対に必要な場合のみ使用してください

## シークレットの一覧表示
コマンド名: list_secrets
説明：アクセス可能なシークレットのキーを一覧表示します
構文例：`<list_secrets/>`

## 認証リクエスト
コマンド名: request_auth
説明：ユーザーに権限とキーの付与を要求します
構文例：`<request_auth>メッセージ内容</request_auth>`
注意事項：
- ユーザーからの権限とキーが必要な場合のみ使用
- sudoの使用には権限要求は不要
