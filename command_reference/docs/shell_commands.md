# シェル操作関連のコマンド

## シェルコマンドの実行
コマンド名: shell
説明：指定されたディレクトリでbashコマンドを実行します
構文例：`<shell id="shellId" exec_dir="exec_dir">bash command to run in exec_dir</shell>`
パラメータ：
- id: シェルセッションの識別子
- exec_dir: コマンドを実行するディレクトリ（絶対パスが必要）
注意事項：exec_dirは必須で、絶対パスである必要があります

## シェル出力の表示
コマンド名: view_shell
説明：指定されたシェルの最新の出力を表示します
構文例：`<view_shell id="shellId"/>`
パラメータ：
- id: 表示するシェルセッションの識別子

## シェルプロセスへの入力
コマンド名: write_to_shell_process
説明：実行中のシェルプロセスにテキストを送信します
構文例：`<write_to_shell_process id="shellId" press_enter="true">text to send process running on shellId</write_to_shell_process>`
パラメータ：
- id: シェルセッションの識別子
- press_enter: Enterキーを押すかどうか（true/false）
特記事項：Unicodeエスケープシーケンスをサポート（例：\u0003 for Control+C）

## シェルプロセスの終了
コマンド名: kill_shell_process
説明：シェルプロセスを終了します
構文例：`<kill_shell_process id="shellId"/>`
パラメータ：
- id: 終了するシェルセッションの識別子
特記事項：
- 複数のkill_shell_processコマンドを同時に実行可能
- シェル自体は存在し続け、新しいコマンドで再利用可能
