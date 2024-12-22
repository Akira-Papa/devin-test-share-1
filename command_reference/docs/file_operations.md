# ファイル操作関連のコマンド

## ファイルを開く
コマンド名: open_file
説明：ファイルを表示用に開きます
構文例：`<open_file file="/full/path/to/filename" start_line="startLineNumber" end_line="endLineNumber" sudo="sudoMode?" symbol_name="symbolName"/>`
パラメータ：
- file: ファイルの絶対パス
- start_line: 開始行番号（オプション）
- end_line: 終了行番号（オプション）
- sudo: root権限での実行（オプション）
- symbol_name: 表示するシンボル名（オプション）

## ファイル内容の置換
コマンド名: str_replace
説明：ファイル内の特定の文字列を置換します
構文例：`<str_replace path="/full/path/to/filename" sudo="sudoMode?">`
パラメータ：
- path: ファイルの絶対パス
- sudo: root権限での実行（オプション）
使用方法：
- old_strとnew_strタグで置換前後の文字列を指定
- 置換対象の文字列は一意である必要があります

## ファイルのスクロール
コマンド名: scroll_file
説明：既に開いているファイルをスクロールします
構文例：`<scroll_file file="/full/path/to/filename" start_line="startLineNumber" end_line="endLineNumber" sudo="sudoMode?" symbol_name="symbolName"/>`
パラメータ：
- file: ファイルの絶対パス
- start_line: 開始行番号（オプション）
- end_line: 終了行番号（オプション）
- sudo: root権限での実行（オプション）
- symbol_name: 表示するシンボル名（オプション）

## ファイルの作成
コマンド名: create_file
説明：新しいファイルを作成します
構文例：`<create_file file="/full/path/to/filename" sudo="sudoMode?">`
パラメータ：
- file: 作成するファイルの絶対パス
- sudo: root権限での実行（オプション）

## 編集の取り消し
コマンド名: undo_edit
説明：最後のファイル編集を取り消します
構文例：`<undo_edit file="/full/path/to/filename" sudo="sudoMode?"/>`
パラメータ：
- file: 編集を取り消すファイルの絶対パス
- sudo: root権限での実行（オプション）
