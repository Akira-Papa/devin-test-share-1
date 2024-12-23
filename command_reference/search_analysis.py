"""
検索・解析関連のコマンド

このモジュールは、ファイルの検索や解析に関連する各種コマンドの実装を提供します。
実際の検索・解析の代わりにモックとして動作し、操作内容をコンソールに出力します。
"""

import os
import re
import glob
from typing import List, Dict, Optional, Union

class SearchAnalysis:
    """検索・解析操作を管理するクラス"""

    @staticmethod
    def find_filecontent(path: str, regex: str) -> List[Dict[str, Union[str, int]]]:
        """
        指定されたパスでファイル内容を検索します

        Args:
            path (str): 検索対象のパス（絶対パス）
            regex (str): 検索パターン（正規表現）

        Returns:
            List[Dict[str, Union[str, int]]]: マッチした内容のリスト
            各辞書には以下のキーが含まれます：
            - file: ファイルパス
            - line: 行番号
            - content: マッチした行の内容

        Raises:
            ValueError: パスまたは正規表現が無効な場合
            FileNotFoundError: パスが存在しない場合

        使用例:
            ```xml
            <find_filecontent path="/path/to/search" regex="pattern"/>
            ```
        """
        if not path:
            raise ValueError("検索パスを指定する必要があります")
        if not os.path.exists(path):
            raise FileNotFoundError(f"指定されたパスが存在しません: {path}")
        if not regex:
            raise ValueError("検索パターンを指定する必要があります")
            
        try:
            re.compile(regex)
        except re.error:
            raise ValueError(f"無効な正規表現パターン: {regex}")
            
        print(f"[Search mock] パス '{path}' で正規表現 '{regex}' を使用して検索")
        
        # モックの検索結果を返す
        return [
            {
                "file": os.path.join(path, "example.txt"),
                "line": 1,
                "content": "サンプルマッチ行1"
            },
            {
                "file": os.path.join(path, "example.txt"),
                "line": 2,
                "content": "サンプルマッチ行2"
            }
        ]

    @staticmethod
    def find_filename(path: str, glob_patterns: List[str]) -> List[str]:
        """
        指定されたパスでファイル名を検索します

        Args:
            path (str): 検索対象のパス（絶対パス）
            glob_patterns (List[str]): 検索パターンのリスト

        Returns:
            List[str]: マッチしたファイル名のリスト

        Raises:
            ValueError: パスまたはパターンが無効な場合
            FileNotFoundError: パスが存在しない場合

        使用例:
            ```xml
            <find_filename path="/path/to/search" glob="pattern1; pattern2"/>
            ```

        注意事項:
            - 複数のパターンはセミコロンとスペースで区切る
        """
        if not path:
            raise ValueError("検索パスを指定する必要があります")
        if not os.path.exists(path):
            raise FileNotFoundError(f"指定されたパスが存在しません: {path}")
        if not glob_patterns:
            raise ValueError("検索パターンを指定する必要があります")
            
        print(f"[Search mock] パス '{path}' でパターン {glob_patterns} を使用してファイル名を検索")
        
        # モックの検索結果を返す
        return [
            os.path.join(path, "example1.txt"),
            os.path.join(path, "example2.txt"),
            os.path.join(path, "subdir", "example3.txt")
        ]

    @staticmethod
    def go_to_definition(path: str, line: int, symbol: str, index: Optional[int] = None) -> Dict[str, Union[str, int]]:
        """
        シンボルの定義位置に移動します

        Args:
            path (str): ファイルの絶対パス
            line (int): シンボルが存在する行番号
            symbol (str): シンボル名
            index (int, optional): 同一行の複数シンボルのインデックス（1から開始）

        Returns:
            Dict[str, Union[str, int]]: 定義位置の情報
            辞書には以下のキーが含まれます：
            - file: 定義が存在するファイルパス
            - line: 定義が存在する行番号
            - column: 定義が存在する列番号
            - symbol: シンボル名

        Raises:
            ValueError: パラメータが無効な場合
            FileNotFoundError: ファイルが存在しない場合

        使用例:
            ```xml
            <go_to_definition path="/path/to/file" line="10" symbol="function_name"/>
            ```
        """
        if not path:
            raise ValueError("ファイルパスを指定する必要があります")
        if not os.path.exists(path):
            raise FileNotFoundError(f"指定されたファイルが存在しません: {path}")
        if not symbol:
            raise ValueError("シンボル名を指定する必要があります")
        if line < 1:
            raise ValueError("行番号は1以上である必要があります")
        if index is not None and index < 1:
            raise ValueError("インデックスは1以上である必要があります")
            
        print(f"[Search mock] シンボル '{symbol}' の定義を検索（ファイル: {path}, 行: {line}, インデックス: {index}）")
        
        # モックの検索結果を返す
        return {
            "file": path,
            "line": 42,
            "column": 4,
            "symbol": symbol
        }

    @staticmethod
    def go_to_references(path: str, line: int, symbol: str, index: Optional[int] = None) -> List[Dict[str, Union[str, int]]]:
        """
        シンボルの参照位置に移動します

        Args:
            path (str): ファイルの絶対パス
            line (int): シンボルが存在する行番号
            symbol (str): シンボル名
            index (int, optional): 同一行の複数シンボルのインデックス（1から開始）

        Returns: 
            List[Dict[str, Union[str, int]]]: 参照位置のリスト
            各辞書には以下のキーが含まれます：
            - file: 参照が存在するファイルパス
            - line: 参照が存在する行番号
            - column: 参照が存在する列番号
            - symbol: シンボル名

        Raises:
            ValueError: パラメータが無効な場合
            FileNotFoundError: ファイルが存在しない場合

        使用例:
            ```xml
            <go_to_references path="/path/to/file" line="10" symbol="function_name"/>
            ```
        """
        if not path:
            raise ValueError("ファイルパスを指定する必要があります")
        if not os.path.exists(path):
            raise FileNotFoundError(f"指定されたファイルが存在しません: {path}")
        if not symbol:
            raise ValueError("シンボル名を指定する必要があります")
        if line < 1:
            raise ValueError("行番号は1以上である必要があります")
        if index is not None and index < 1:
            raise ValueError("インデックスは1以上である必要があります")
            
        print(f"[Search mock] シンボル '{symbol}' の参照を検索（ファイル: {path}, 行: {line}, インデックス: {index}）")
        
        # モックの検索結果を返す
        return [
            {
                "file": path,
                "line": 10,
                "column": 8,
                "symbol": symbol
            },
            {
                "file": os.path.join(os.path.dirname(path), "another_file.py"),
                "line": 15,
                "column": 12,
                "symbol": symbol
            }
        ]

    @staticmethod
    def hover_symbol(path: str, line: int, symbol: str, index: Optional[int] = None) -> str:
        """
        シンボルに関する情報を表示します

        Args:
            path (str): ファイルの絶対パス
            line (int): シンボルが存在する行番号
            symbol (str): シンボル名
            index (int, optional): 同一行の複数シンボルのインデックス（1から開始）

        Returns:
            str: シンボルの情報（型、定義、ドキュメントなど）

        Raises:
            ValueError: パラメータが無効な場合
            FileNotFoundError: ファイルが存在しない場合

        使用例:
            ```xml
            <hover_symbol path="/path/to/file" line="10" symbol="function_name"/>
            ```
        """
        if not path:
            raise ValueError("ファイルパスを指定する必要があります")
        if not os.path.exists(path):
            raise FileNotFoundError(f"指定されたファイルが存在しません: {path}")
        if not symbol:
            raise ValueError("シンボル名を指定する必要があります")
        if line < 1:
            raise ValueError("行番号は1以上である必要があります")
        if index is not None and index < 1:
            raise ValueError("インデックスは1以上である必要があります")
            
        try:
            import jedi
            
            # Jediを使用してシンボルの情報を取得
            script = jedi.Script(path=path)
            definitions = script.infer(line, column=None)
            
            if not definitions:
                raise RuntimeError(f"シンボル '{symbol}' の情報が見つかりません")
            
            # インデックスが指定されている場合は該当する定義を返す
            if index is not None:
                if index > len(definitions):
                    raise ValueError(f"インデックス {index} が範囲外です（定義数: {len(definitions)}）")
                definition = definitions[index - 1]
            else:
                definition = definitions[0]
            
            # シンボル情報の取得
            symbol_type = definition.type
            symbol_def = str(definition.get_line_code()).strip()
            docstring = definition.docstring() or "ドキュメントがありません"
            
            # パラメータ情報の取得
            params = []
            if hasattr(definition, 'params'):
                for param in definition.params:
                    param_name = param.name
                    param_type = param.annotation.get_type_hint() if param.annotation else "不明"
                    param_default = param.default.get_safe_value() if param.default else "なし"
                    params.append(f"- {param_name}: 型={param_type}, デフォルト値={param_default}")
            
            # 戻り値の型情報の取得
            return_type = "不明"
            if hasattr(definition, 'return_annotation') and definition.return_annotation:
                return_type = definition.return_annotation.get_type_hint()
            
            # 情報を整形して返す
            result = f"""
型: {symbol_type}
定義: {symbol_def}
ドキュメント: {docstring}
"""
            
            if params:
                result += "\nパラメータ:\n" + "\n".join(params)
            
            result += f"\n戻り値の型: {return_type}"
            
            return result.strip()
            
        except Exception as e:
            raise RuntimeError(f"シンボル情報の取得に失敗しました: {str(e)}")

    @staticmethod
    def gather_information(query: str, current_file: Optional[str] = None) -> str:
        """
        コードベースに関する質問の回答を収集します

        Args:
            query (str): 質問内容
            current_file (str, optional): 現在のファイルパス

        Returns:
            str: 収集した情報（検索結果、関連コード、説明など）

        Raises:
            ValueError: パラメータが無効な場合
            FileNotFoundError: 指定されたファイルが存在しない場合

        使用例:
            ```xml
            <gather_information query="質問内容" current_file="/path/to/file"/>
            ```
        """
        if not query:
            raise ValueError("質問内容を指定する必要があります")
        if current_file and not os.path.exists(current_file):
            raise FileNotFoundError(f"指定されたファイルが存在しません: {current_file}")
            
        print(f"[Search mock] 質問 '{query}' に関する情報を収集")
        if current_file:
            print(f"[Search mock] 現在のファイル: {current_file}")
            
        # モックの情報を返す
        return f"""
検索結果:
1. 関連するコード:
   ```python
   def example_function():
       # 質問に関連する実装例
       pass
   ```

2. 関連するドキュメント:
   - 機能の説明
   - 使用方法の例
   - 注意事項

3. 類似の実装:
   - 他のモジュールでの類似機能
   - ベストプラクティス

4. 回答:
   {query}に関する詳細な説明...
"""

    @staticmethod
    def analyze_image(file: str, questions: Optional[str] = None) -> str:
        """
        画像ファイルを解析し、詳細を説明します

        Args:
            file (str): 画像ファイル名（絶対パス）
            questions (str, optional): 画像に関する具体的な質問

        Returns:
            str: 解析結果（画像の内容、特徴、質問への回答など）

        Raises:
            ValueError: パラメータが無効な場合
            FileNotFoundError: 画像ファイルが存在しない場合
            RuntimeError: 画像の解析に失敗した場合

        使用例:
            ```xml
            <analyze_image file="image.png">画像に関する質問</analyze_image>
            ```
        """
        if not file:
            raise ValueError("画像ファイルを指定する必要があります")
        if not os.path.exists(file):
            raise FileNotFoundError(f"指定された画像ファイルが存在しません: {file}")

        try:
            import base64
            from openai import OpenAI
            from PIL import Image
            import io

            # OpenAI APIクライアントの初期化
            api_key = os.getenv("OpenAI_API_OPENAI_API_KEY")
            if not api_key:
                raise RuntimeError("OpenAI APIキーが設定されていません")

            client = OpenAI(api_key=api_key)

            # 画像ファイルの読み込みと基本情報の取得
            with Image.open(file) as img:
                width, height = img.size
                format_name = img.format
                mode = img.mode

                # 画像をbase64エンコード
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format=img.format)
                img_byte_arr = img_byte_arr.getvalue()
                base64_image = base64.b64encode(img_byte_arr).decode('utf-8')

            # プロンプトの生成
            if questions: 
                prompt = f"""
以下の画像について、次の質問に詳しく答えてください：

{questions}

また、以下の情報も含めて分析してください：
- 画像の種類と主な要素
- 重要なテキストや視覚的特徴
- 色使い、コントラスト、明瞭度
- 画像の目的や用途
"""
            else:
                prompt = """
この画像について、以下の点を詳しく分析してください：

1. 画像の基本的な内容と主要な要素
2. 重要なテキストや記号
3. レイアウトや構成
4. 色使い、コントラスト、画質
5. 画像の目的や用途
6. 特筆すべき特徴や詳細

できるだけ具体的に、日本語で説明してください。
"""

            # OpenAI Vision APIを使用して画像解析
            response = client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/{format_name.lower()};base64,{base64_image}",
                                    "detail": "high"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=1000
            )

            # 解析結果の整形
            analysis = response.choices[0].message.content
            
            return f"""
画像解析結果:

1. 基本情報:
   - ファイル名: {os.path.basename(file)}
   - サイズ: {width}x{height}px
   - 形式: {format_name}
   - カラーモード: {mode}

2. 解析内容:
{analysis}
"""

        except Exception as e:
            raise RuntimeError(f"画像の解析に失敗しました: {str(e)}")
