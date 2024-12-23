# デプロイメント関連のコマンド

## フロントエンドのデプロイ
コマンド名: deploy_frontend
説明：フロントエンドアプリケーションをデプロイします
構文例：`<deploy_frontend dir="siteDirectory"/>`
パラメータ：
- dir: デプロイするサイトのディレクトリパス
注意事項：デプロイ後にウェブサイトが正常に読み込まれることを確認する必要があります

## バックエンドのデプロイ
コマンド名: deploy_backend
説明：Pythonバックエンドアプリケーションをデプロイします
構文例：
- デプロイ：`<deploy_backend dir="projectDirectory"/>`
- ログ表示：`<deploy_backend logs="True"/>`
パラメータ：
- dir: プロジェクトディレクトリパス
- logs: ログを表示するかどうか（True/False）

## ポートの公開
コマンド名: expose_port
説明：ローカルポートをインターネットに公開します
構文例：`<expose_port local_port="local_port"/>`
パラメータ：
- local_port: 公開するローカルポート番号

## プルリクエストの表示
コマンド名: gh_view_pr
説明：GitHubのプルリクエストを表示します
構文例：`<gh_view_pr repo="owner/repo" pull_number="X"/>`
パラメータ：
- repo: リポジトリ名（owner/repo形式）
- pull_number: プルリクエスト番号
