# 検索・解析関連のコマンド

## ファイル内容の検索
コマンド名: find_filecontent
説明：指定されたパスでファイル内容を検索します
構文例：`<find_filecontent path="absolute_path" regex="regexPattern"/>`
パラメータ：
- path: 検索対象のパス（絶対パス）
- regex: 検索パターン（正規表現）

## ファイル名の検索
コマンド名: find_filename
説明：指定されたパスでファイル名を検索します
構文例：`<find_filename path="absolute_path" glob="globPattern1; globPattern2; ..."/>`
パラメータ：
- path: 検索対象のパス（絶対パス）
- glob: 検索パターン（複数指定可能、セミコロンとスペースで区切る）

## 定義への移動
コマンド名: go_to_definition
説明：シンボルの定義位置に移動します
構文例：`<go_to_definition path="/full/path/to/filename" line="line_number" symbol="symbol_name" index="symbol_index"/>`
パラメータ：
- path: ファイルの絶対パス
- line: シンボルが存在する行番号
- symbol: シンボル名
- index: 同一行に複数のシンボルがある場合のインデックス（オプション）

## 参照への移動
コマンド名: go_to_references
説明：シンボルの参照位置に移動します
構文例：`<go_to_references path="/full/path/to/filename" line="line_number" symbol="symbol_name" index="symbol_index"/>`
パラメータ：
- path: ファイルの絶対パス
- line: シンボルが存在する行番号
- symbol: シンボル名
- index: 同一行に複数のシンボルがある場合のインデックス（オプション）

## 型定義への移動
コマンド名: go_to_type_definition
説明：シンボルの型定義位置に移動します
構文例：`<go_to_type_definition path="/full/path/to/filename" line="line_number" symbol="symbol_name" index="symbol_index"/>`
パラメータ：
- path: ファイルの絶対パス
- line: シンボルが存在する行番号
- symbol: シンボル名
- index: 同一行に複数のシンボルがある場合のインデックス（オプション）

## シンボル情報の表示
コマンド名: hover_symbol
説明：シンボルに関する情報を表示します
構文例：`<hover_symbol path="/full/path/to/filename" line="line_number" symbol="symbol_name" index="symbol_index"/>`
パラメータ：
- path: ファイルの絶対パス
- line: シンボルが存在する行番号
- symbol: シンボル名
- index: 同一行に複数のシンボルがある場合のインデックス（オプション）

## 情報収集
コマンド名: gather_information
説明：コードベースに関する質問の回答を収集します
構文例：`<gather_information query="your question here" current_file="optional current file path"/>`
パラメータ：
- query: 質問内容
- current_file: 現在のファイルパス（オプション）

## 画像解析
コマンド名: analyze_image
説明：画像ファイルを解析し、詳細を説明します
構文例：`<analyze_image file="filename">質問内容</analyze_image>`
パラメータ：
- file: 画像ファイル名
- 質問内容：画像に関する具体的な質問（オプション）
