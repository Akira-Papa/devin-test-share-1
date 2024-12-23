# ユーティリティ関連のコマンド

## 待機
コマンド名: wait
説明：指定された時間だけ待機します。処理の開始と完了時にログを出力します。
構文例：`<wait for="user/browser/shell/etc" seconds="seconds"/>`
パラメータ：
- for: 待機対象（user/browser/shell/etc）
- seconds: 待機時間（秒）
戻り値：なし（None）
エラー：
- ValueError: 待機時間が負の値の場合
- ValueError: targetが空文字列または文字列以外の場合

## ユーザーへのメッセージ送信
コマンド名: message_user
説明：ユーザーにメッセージを送信します。オプションで添付ファイルを含めることができます。
構文例：
- 通常メッセージ：`<message_user>メッセージ内容</message_user>`
- 添付付きメッセージ：`<message_user attachments="comma_separated_filenames">メッセージ内容</message_user>`
パラメータ：
- attachments: 添付ファイル名（カンマ区切り、オプション）
戻り値：なし（None）
エラー：
- ValueError: メッセージが空の場合
- FileNotFoundError: 添付ファイルが存在しない場合

## 質問
コマンド名: ask
説明：人間のエンジニアリングマネージャーに質問します。質問と回答のやり取りをシミュレートします。
構文例：`<ask>質問内容</ask>`
パラメータ：
- question: 質問内容（必須）
戻り値：str（回答内容）
エラー：
- ValueError: 質問が空の場合
注意事項：
- 絶対に必要な場合のみ使用してください
- 質問内容は具体的かつ明確に記述してください

## シークレットの一覧表示
コマンド名: list_secrets
説明：アクセス可能なシークレットのキーを一覧表示します。環境変数として設定されているシークレットのみを表示します。
構文例：`<list_secrets/>`
戻り値：list（利用可能なシークレットキーのリスト）
利用可能なシークレット：
- Google認証関連（GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET）
- MongoDB接続情報（MONGODB_URI）
- Gmail SMTP設定（EMAIL_SERVER_HOST, PORT, USER, PASSWORD, FROM）
- OpenAI API設定（OPENAI_API_KEY）
- AWS設定（ACCESS_KEY_ID, SECRET_ACCESS_KEY, REGION）
- Serverless設定（SERVERLESS_ACCESS_KEY）

## 認証リクエスト
コマンド名: request_auth
説明：ユーザーに権限とキーの付与を要求します。要求内容と承認待ちステータスを表示します。
構文例：`<request_auth>メッセージ内容</request_auth>`
パラメータ：
- message: 要求メッセージ（必須）
戻り値：なし（None）
エラー：
- ValueError: メッセージが空の場合
注意事項：
- ユーザーからの権限とキーが必要な場合のみ使用
- sudoの使用には権限要求は不要
- 要求理由を具体的に説明してください
