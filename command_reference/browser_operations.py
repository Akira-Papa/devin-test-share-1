"""
ブラウザ操作関連のコマンド

このモジュールは、ブラウザの操作に関連する各種コマンドの実装を提供します。
実際のブラウザ操作の代わりにモックとして動作し、操作内容をコンソールに出力します。
"""

import os
from typing import Optional, Tuple, List, Union

class BrowserOperations:
    """ブラウザ操作を管理するクラス"""

    @staticmethod
    def navigate(url: str) -> None:
        """
        指定されたURLをブラウザで開きます

        Args:
            url (str): 開くページのURL

        Raises:
            ValueError: URLが無効な場合
            RuntimeError: ページの読み込みに失敗した場合

        使用例:
            ```xml
            <navigate_browser url="https://example.com"/>
            ```
        """
        if not url:
            raise ValueError("URLを指定する必要があります")
        if not url.startswith(("http://", "https://")):
            raise ValueError("無効なURL形式です。http://またはhttps://で始まる必要があります")

        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                
                # URLに移動
                page.goto(url)
                
                # ページの読み込みが完了するまで待機
                page.wait_for_load_state("networkidle")
                
                # ブラウザを閉じる
                browser.close()
                
        except Exception as e:
            raise RuntimeError(f"ページの読み込みに失敗しました: {str(e)}")

    @staticmethod
    def click(box_id: Optional[str] = None, coordinates: Optional[Tuple[int, int]] = None) -> None:
        """
        要素をクリックします

        Args:
            box_id (str, optional): クリックする要素のdevinid属性値
            coordinates (tuple, optional): クリックする座標（x, y）

        Raises:
            ValueError: パラメータが無効な場合
            RuntimeError: クリック操作に失敗した場合

        使用例:
            ```xml
            <click_browser box="button_id"/>
            <click_browser coordinates="100,200"/>
            ```
        """
        if not box_id and coordinates is None:
            raise ValueError("box_idまたはcoordinatesのいずれかを指定する必要があります")
        if coordinates and (not isinstance(coordinates, tuple) or len(coordinates) != 2 or 
                          not all(isinstance(x, int) for x in coordinates)):
            raise ValueError("coordinatesは(x, y)の形式のタプルである必要があります")

        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                
                if box_id:
                    # devinid属性を持つ要素を検索
                    element = page.locator(f'[devinid="{box_id}"]')
                    
                    # 要素が見つかるまで待機してクリック
                    element.wait_for(state="visible")
                    element.click()
                else: 
                    # 座標を指定してクリック
                    page.mouse.click(coordinates[0], coordinates[1])
                
                # クリックの影響が反映されるまで待機
                page.wait_for_timeout(500)
                
                # ブラウザを閉じる
                browser.close()
                
        except Exception as e:
            raise RuntimeError(f"クリック操作に失敗しました: {str(e)}")

    @staticmethod
    def type_text(text: str, box_id: Optional[str] = None, 
                 coordinates: Optional[Tuple[int, int]] = None, 
                 press_enter: bool = False) -> None:
        """
        テキストを入力します

        Args:
            text (str): 入力するテキスト
            box_id (str, optional): 入力する要素のdevinid属性値
            coordinates (tuple, optional): 入力する座標（x, y）
            press_enter (bool): Enterキーを押すかどうか

        Raises:
            ValueError: パラメータが無効な場合
            RuntimeError: テキスト入力に失敗した場合

        使用例:
            ```xml
            <type_browser box="input_id" press_enter="false">入力テキスト</type_browser>
            ```
        """
        if not text:
            raise ValueError("テキストを指定する必要があります")
        if not box_id and coordinates is None:
            raise ValueError("box_idまたはcoordinatesのいずれかを指定する必要があります")
        if coordinates and (not isinstance(coordinates, tuple) or len(coordinates) != 2 or 
                          not all(isinstance(x, int) for x in coordinates)):
            raise ValueError("coordinatesは(x, y)の形式のタプルである必要があります")

        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                
                if box_id:
                    # devinid属性を持つ要素を検索
                    element = page.locator(f'[devinid="{box_id}"]')
                    
                    # 要素が見つかるまで待機
                    element.wait_for(state="visible")
                    
                    # 既存のテキストをクリア
                    element.fill("")
                    
                    # 新しいテキストを入力
                    element.type(text)
                else:
                    # 座標を指定してクリック
                    page.mouse.click(coordinates[0], coordinates[1])
                    
                    # テキストを入力
                    page.keyboard.type(text)
                
                if press_enter:
                    page.keyboard.press("Enter")
                    
                # 入力の影響が反映されるまで待機
                page.wait_for_timeout(500)
                
                # ブラウザを閉じる
                browser.close()
                
        except Exception as e:
            raise RuntimeError(f"テキスト入力に失敗しました: {str(e)}")

    @staticmethod
    def press_key(key_combination: str) -> None:
        """
        キーボードショートカットを実行します

        Args:
            key_combination (str): キーの組み合わせ

        Raises:
            ValueError: キーの組み合わせが無効な場合
            RuntimeError: キー操作に失敗した場合

        使用例:
            ```xml
            <press_key_browser>Control+Enter</press_key_browser>
            ```

        注意事項:
            - 対応キー：Shift, Control, Alt, Enter
            - 複数のキーは+で連結
        """
        if not key_combination:
            raise ValueError("キーの組み合わせを指定する必要があります")
            
        valid_keys = {"Shift", "Control", "Alt", "Enter"}
        keys = key_combination.split("+")
        
        if not keys:
            raise ValueError("キーの組み合わせが無効です")
            
        invalid_keys = [key for key in keys if key not in valid_keys]
        if invalid_keys:
            raise ValueError(f"無効なキーが含まれています: {', '.join(invalid_keys)}。有効なキー: {', '.join(valid_keys)}")

        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                
                # キーの組み合わせを実行
                for key in keys:
                    page.keyboard.down(key)
                    
                for key in reversed(keys):
                    page.keyboard.up(key)
                
                # キー操作の影響が反映されるまで待機
                page.wait_for_timeout(500)
                
                # ブラウザを閉じる
                browser.close()
                
        except Exception as e:
            raise RuntimeError(f"キー操作に失敗しました: {str(e)}")

    @staticmethod
    def get_console() -> str:
        """
        ブラウザのコンソールログを取得します

        Returns:
            str: コンソールログの内容

        Raises:
            RuntimeError: コンソールログの取得に失敗した場合

        使用例:
            ```xml
            <get_browser_console/>
            ```
        """
        try:
            from playwright.sync_api import sync_playwright
            import json

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                
                # コンソールメッセージを収集するリスト
                console_messages = []
                
                # コンソールイベントのリスナーを設定
                page.on("console", lambda msg: console_messages.append({
                    "type": msg.type,
                    "text": msg.text,
                    "location": msg.location
                }))
                
                # ページを再読み込み
                page.reload()
                
                # ページの読み込みが完了するまで待機
                page.wait_for_load_state("networkidle")
                
                # コンソールメッセージを整形
                formatted_messages = []
                for msg in console_messages:
                    location = msg["location"]
                    formatted_msg = f"[{msg['type']}] {msg['text']}"
                    if location:
                        formatted_msg += f" (at {location['url']}:{location['lineNumber']})"
                    formatted_messages.append(formatted_msg)
                
                # ブラウザを閉じる
                browser.close()
                
                return "\n".join(formatted_messages)
                
        except Exception as e:
            raise RuntimeError(f"コンソールログの取得に失敗しました: {str(e)}")

    @staticmethod
    def view_content(reload_window: bool = False) -> str:
        """
        現在のページの内容を表示します

        Args:
            reload_window (bool): ページを再読み込みするかどうか

        Returns:
            str: ページの内容

        Raises:
            RuntimeError: ページ内容の取得に失敗した場合

        使用例:
            ```xml
            <view_browser reload_window="true"/>
            ```
        """
        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                
                if reload_window:
                    # ページを再読み込み
                    page.reload()
                    
                    # 読み込みが完了するまで待機
                    page.wait_for_load_state("networkidle")
                
                # ページの内容を取得
                content = page.content()
                
                # ブラウザを閉じる
                browser.close()
                
                return content
                
        except Exception as e:
            raise RuntimeError(f"ページ内容の取得に失敗しました: {str(e)}")

    @staticmethod
    def take_screenshot(reload_window: bool = False, questions: Optional[str] = None) -> str:
        """
        現在のページのスクリーンショットを取得します

        Args:
            reload_window (bool): ページを再読み込みするかどうか
            questions (str, optional): 視覚的な確認に関する質問

        Returns:
            str: スクリーンショットの情報（Base64エンコードされた画像データ）

        Raises:
            RuntimeError: スクリーンショットの取得に失敗した場合

        使用例:
            ```xml
            <screenshot_browser reload_window="false">確認したい内容</screenshot_browser>
            ```
        """
        try:
            from playwright.sync_api import sync_playwright
            import base64
            import tempfile
            import os

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                
                if reload_window:
                    # ページを再読み込み
                    page.reload()
                    
                    # 読み込みが完了するまで待機
                    page.wait_for_load_state("networkidle")
                
                # 一時ファイルを作成してスクリーンショットを保存
                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
                    page.screenshot(path=tmp.name, full_page=True)
                    
                    # 画像をBase64エンコード
                    with open(tmp.name, "rb") as f:
                        screenshot_data = base64.b64encode(f.read()).decode("utf-8")
                    
                    # 一時ファイルを削除
                    os.unlink(tmp.name)
                
                # ブラウザを閉じる
                browser.close()
                
                return screenshot_data
                
        except Exception as e:
            raise RuntimeError(f"スクリーンショットの取得に失敗しました: {str(e)}")

    @staticmethod
    def run_javascript(code: str) -> str:
        """
        JavaScriptコードを実行します

        Args:
            code (str): 実行するJavaScriptコード

        Returns:
            str: 実行結果

        Raises:
            ValueError: JavaScriptコードが空または無効な場合
            RuntimeError: JavaScriptの実行に失敗した場合

        使用例:
            ```xml
            <run_javascript_browser>console.log("Hi")</run_javascript_browser>
            ```
        """
        if not code or not isinstance(code, str):
            raise ValueError("有効なJavaScriptコードを指定してください")

        try:
            # Playwrightを使用してJavaScriptを実行
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                
                # JavaScriptを実行し、結果を取得
                result = page.evaluate(code)
                
                # ブラウザを閉じる
                browser.close()
                
                return str(result) if result is not None else ""
                
        except Exception as e:
            raise RuntimeError(f"JavaScriptの実行に失敗しました: {str(e)}")

    @staticmethod
    def scroll(direction: str) -> None:
        """
        ページをスクロールします

        Args:
            direction (str): スクロール方向（"up" or "down"）

        Raises:
            ValueError: 無効なスクロール方向が指定された場合
            RuntimeError: スクロール操作に失敗した場合

        使用例:
            ```xml
            <scroll_up_browser/>
            <scroll_down_browser/>
            ```
        """
        if direction not in ["up", "down"]:
            raise ValueError("スクロール方向は'up'または'down'である必要があります")

        try:
            # Playwrightを使用してスクロール
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                
                # ビューポートの高さを取得
                viewport_height = page.viewport_size["height"]
                
                # スクロール量を設定（上方向は負の値）
                scroll_amount = -viewport_height if direction == "up" else viewport_height
                
                # mouse.wheelを使用してスクロール
                page.mouse.wheel(0, scroll_amount)
                
                # スクロールが完了するまで待機
                page.wait_for_timeout(500)
                
                # ブラウザを閉じる
                browser.close()
                
        except Exception as e:
            raise RuntimeError(f"スクロール操作に失敗しました: {str(e)}")

    @staticmethod
    def select_option(box_id: str, index: int) -> None:
        """
        ドロップダウンメニューからオプションを選択します

        Args:
            box_id (str): 選択する要素のdevinid属性値
            index (int): 選択するオプションのインデックス（0から開始）

        Raises:
            ValueError: パラメータが無効な場合
            RuntimeError: オプション選択に失敗した場合

        使用例:
            ```xml
            <select_option_browser box="select_id" index="0"/>
            ```
        """
        if not box_id:
            raise ValueError("box_idを指定する必要があります")
        if index < 0:
            raise ValueError("インデックスは0以上である必要があります")

        try:
            # Playwrightを使用してオプション選択
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                
                # devinid属性を持つ要素を検索
                select_element = page.locator(f'[devinid="{box_id}"]')
                
                # 要素が見つかるまで待機
                select_element.wait_for(state="visible")
                
                # オプションを選択（JavaScriptを使用）
                page.evaluate(f"""
                    (element, index) => {{
                        if (element.tagName.toLowerCase() === 'select') {{
                            element.selectedIndex = index;
                            element.dispatchEvent(new Event('change'));
                        }}
                    }}
                """, select_element, index)
                
                # 選択が反映されるまで待機
                page.wait_for_timeout(500)
                
                # ブラウザを閉じる
                browser.close()
                
        except Exception as e:
            raise RuntimeError(f"オプション選択に失敗しました: {str(e)}")

    @staticmethod
    def restart(url: str) -> None:
        """
        ブラウザを再起動し、指定されたURLを開きます

        Args:
            url (str): 開始ページのURL

        Raises:
            ValueError: URLが無効な場合
            RuntimeError: ブラウザの再起動に失敗した場合

        使用例:
            ```xml
            <restart_browser url="https://www.google.com"/>
            ```
        """
        if not url or not isinstance(url, str):
            raise ValueError("有効なURLを指定してください")

        try:
            # Playwrightを使用してブラウザを再起動
            from playwright.sync_api import sync_playwright
            import re

            # URLの形式を検証
            if not re.match(r'^https?://', url):
                raise ValueError("URLはhttp://またはhttps://で始まる必要があります")

            with sync_playwright() as p:
                # 既存のブラウザインスタンスを終了（存在する場合）
                try:
                    browser = p.chromium.connect_over_cdp()
                    if browser:
                        browser.close()
                except:
                    pass

                # 新しいブラウザを起動
                browser = p.chromium.launch(
                    headless=False,  # ヘッドレスモードを無効化
                    args=['--start-maximized']  # ウィンドウを最大化
                )
                
                # 新しいページを開く
                page = browser.new_page()
                
                # 指定されたURLに移動
                page.goto(url)
                
                # ページの読み込みが完了するまで待機
                page.wait_for_load_state("networkidle")
                
        except Exception as e:
            raise RuntimeError(f"ブラウザの再起動に失敗しました: {str(e)}")

    @staticmethod
    def load_extensions(extensions: List[str]) -> None:
        """
        拡張機能を読み込みます

        Args:
            extensions (List[str]): 拡張機能のディレクトリパスのリスト

        Raises:
            ValueError: 拡張機能のパスが無効な場合
            RuntimeError: 拡張機能の読み込みに失敗した場合

        使用例:
            ```xml
            <load_browser_extensions extensions="/path/to/extension1,/path/to/extension2"/>
            ```
        """
        if not extensions:
            raise ValueError("拡張機能のパスを指定する必要があります")
            
        for ext_path in extensions:
            if not ext_path or not os.path.isabs(ext_path):
                raise ValueError(f"無効な拡張機能パス: {ext_path}。絶対パスで指定する必要があります")
            if not os.path.exists(ext_path):
                raise ValueError(f"拡張機能のパスが存在しません: {ext_path}")
            if not os.path.isdir(ext_path):
                raise ValueError(f"拡張機能のパスはディレクトリである必要があります: {ext_path}")

        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                # 拡張機能のパスを引数として設定
                args = []
                for ext_path in extensions:
                    args.extend(['--load-extension=' + ext_path])
                
                # ブラウザを起動（拡張機能を読み込む）
                browser = p.chromium.launch(
                    headless=False,  # 拡張機能を使用するためにヘッドレスモードを無効化
                    args=args
                )
                
                # 新しいページを開く
                page = browser.new_page()
                
                # 拡張機能が読み込まれるまで待機
                page.wait_for_timeout(2000)  # 2秒待機
                
                # ブラウザを閉じる
                browser.close()
                
        except Exception as e:
            raise RuntimeError(f"拡張機能の読み込みに失敗しました: {str(e)}")
