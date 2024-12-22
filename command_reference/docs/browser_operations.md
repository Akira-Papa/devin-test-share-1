# ブラウザ操作関連のコマンド

## ブラウザでのページ表示
コマンド名: navigate_browser
説明：指定されたURLをブラウザで開きます
構文例：`<navigate_browser url="url"/>`
パラメータ：
- url: 開くページのURL

## 要素のクリック（ID指定）
コマンド名: click_browser
説明：指定されたID属性を持つ要素をクリックします
構文例：`<click_browser box="ID"/>`
パラメータ：
- box: クリックする要素のdevinid属性値

## 要素のクリック（座標指定）
コマンド名: click_browser
説明：指定された座標をクリックします
構文例：`<click_browser coordinates="x,y"/>`
パラメータ：
- coordinates: クリックする座標（x,y形式）

## マウスの移動
コマンド名: move_mouse
説明：マウスカーソルを指定された座標に移動します
構文例：`<move_mouse coordinates="x,y"/>`
パラメータ：
- coordinates: 移動先の座標（x,y形式）

## テキスト入力（ID指定）
コマンド名: type_browser
説明：指定されたID属性を持つ要素にテキストを入力します
構文例：`<type_browser box="ID" press_enter="False">入力テキスト</type_browser>`
パラメータ：
- box: 入力する要素のdevinid属性値
- press_enter: Enter キーを押すかどうか（オプション）
- 入力テキスト：複数行可能

## キー入力
コマンド名: press_key_browser
説明：キーボードショートカットを実行します
構文例：`<press_key_browser>Control+Enter</press_key_browser>`
特記事項：
- 複数のキーを同時に押す場合は+で連結
- 対応キー：Shift, Control, Alt, Enter

## コンソールログの取得
コマンド名: get_browser_console
説明：ブラウザのコンソールログを取得します
構文例：`<get_browser_console/>`

## ブラウザ内容の表示
コマンド名: view_browser
説明：現在のページの内容を表示します
構文例：`<view_browser reload_window="True/False"/>`
パラメータ：
- reload_window: ページを再読み込みするかどうか

## スクリーンショット取得
コマンド名: screenshot_browser
説明：現在のページのスクリーンショットを取得します
構文例：`<screenshot_browser reload_window="True/False">質問内容</screenshot_browser>`
パラメータ：
- reload_window: ページを再読み込みするかどうか
- 質問内容：視覚的な確認に関する質問

## JavaScript実行
コマンド名: run_javascript_browser
説明：JavaScriptコードを実行します
構文例：`<run_javascript_browser>console.log("Hi")</run_javascript_browser>`

## ページスクロール
コマンド名: scroll_up_browser, scroll_down_browser
説明：ページを上下にスクロールします
構文例：
- `<scroll_up_browser/>`
- `<scroll_down_browser/>`

## オプション選択
コマンド名: select_option_browser
説明：ドロップダウンメニューからオプションを選択します
構文例：`<select_option_browser box="ID" index="INDEX"/>`
パラメータ：
- box: 選択する要素のdevinid属性値
- index: 選択するオプションのインデックス（0から開始）

## ブラウザの再起動
コマンド名: restart_browser
説明：ブラウザを再起動し、指定されたURLを開きます
構文例：`<restart_browser url="https://www.google.com"/>`
パラメータ：
- url: 開始ページのURL

## 拡張機能の読み込み
コマンド名: load_browser_extensions
説明：指定された拡張機能を読み込みます
構文例：`<load_browser_extensions extensions="comma_separated_absolute_paths"/>`
パラメータ：
- extensions: 拡張機能のディレクトリパス（カンマ区切り）
