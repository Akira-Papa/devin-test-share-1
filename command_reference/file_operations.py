"""
ファイル操作関連のコマンド

このモジュールは、ファイルの操作に関連する各種コマンドの実装を提供します。
ファイルの読み込み、書き込み、置換、作成などの機能を含みます。
"""

import os
import shutil
import tempfile
import subprocess
from typing import Optional, List, Tuple

class FileOperations:
    """ファイル操作を管理するクラス
    
    このクラスは、ファイルの読み込み、書き込み、置換、作成などの
    基本的なファイル操作機能を提供します。sudo権限での実行にも対応しています。
    """
    
    @staticmethod
    def _read_file_with_sudo(file_path: str) -> str:
        """sudoを使用してファイルを読み込む"""
        try:
            result = subprocess.run(
                ['sudo', 'cat', file_path],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise PermissionError(f"Failed to read file with sudo: {str(e)}")
            
    @staticmethod
    def _write_file_with_sudo(file_path: str, content: str) -> None:
        """sudoを使用してファイルに書き込む"""
        try:
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(content)
                temp_file.flush()
                
            subprocess.run(
                ['sudo', 'cp', temp_file.name, file_path],
                check=True
            )
            os.unlink(temp_file.name)
            
        except (subprocess.CalledProcessError, IOError) as e:
            raise PermissionError(f"Failed to write file with sudo: {str(e)}")

    @staticmethod
    def open_file(file_path: str, start_line: int = None, end_line: int = None, 
                 sudo: bool = False, symbol_name: str = None) -> str:
        """
        ファイルを表示用に開きます

        Args:
            file_path (str): ファイルの絶対パス
            start_line (int, optional): 開始行番号
            end_line (int, optional): 終了行番号
            sudo (bool): root権限での実行
            symbol_name (str, optional): 表示するシンボル名

        Returns:
            str: ファイルの内容

        Raises:
            FileNotFoundError: ファイルが存在しない場合
            PermissionError: ファイルにアクセスできない場合
            ValueError: 無効な行番号が指定された場合

        使用例:
            ```xml
            <open_file file="/path/to/file" start_line="1" end_line="10" sudo="false" symbol_name="main"/>
            ```
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        try:
            # ファイルの内容を読み込む
            content = FileOperations._read_file_with_sudo(file_path) if sudo else \
                     open(file_path, 'r', encoding='utf-8').read()
                     
            # 行に分割
            lines = content.splitlines()
            
            # 行番号の正規化
            start = (start_line or 1) - 1  # 1-indexed to 0-indexed
            end = end_line if end_line is not None else len(lines)
            
            # 行番号の検証
            if start < 0 or end > len(lines) or start >= end:
                raise ValueError(f"Invalid line range: {start+1} to {end}")
                
            # シンボル名が指定された場合の処理
            if symbol_name:
                # シンボルを含む行を探す（簡易実装）
                symbol_lines = []
                for i, line in enumerate(lines):
                    if symbol_name in line:
                        symbol_lines.append(i)
                        
                if symbol_lines:
                    # シンボルを含む行の前後数行を含める
                    context_lines = 5
                    start = max(0, symbol_lines[0] - context_lines)
                    end = min(len(lines), symbol_lines[-1] + context_lines + 1)
            
            # 指定範囲の行を結合して返す
            return '\n'.join(lines[start:end])
            
        except (IOError, OSError) as e:
            raise PermissionError(f"Failed to read file: {str(e)}")

    @staticmethod
    def str_replace(file_path: str, old_str: str, new_str: str, sudo: bool = False) -> None:
        """
        ファイル内の特定の文字列を置換します

        Args:
            file_path (str): ファイルの絶対パス
            old_str (str): 置換対象の文字列
            new_str (str): 置換後の文字列
            sudo (bool): root権限での実行

        使用例:
            ```xml
            <str_replace path="/path/to/file" sudo="false">
            <old_str>old text</old_str>
            <new_str>new text</new_str>
            </str_replace>
            ```

        注意事項:
            - 置換対象の文字列は一意である必要があります
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            # ファイルの内容を読み込む
            content = FileOperations._read_file_with_sudo(file_path) if sudo else \
                     open(file_path, 'r', encoding='utf-8').read()

            # 置換対象文字列の出現回数をチェック
            occurrences = content.count(old_str)
            if occurrences == 0:
                raise ValueError(f"String not found: {old_str}")
            if occurrences > 1:
                raise ValueError(f"String is not unique: {old_str} (found {occurrences} times)")

            # バックアップファイルを作成
            backup_path = f"{file_path}.bak"
            if sudo:
                FileOperations._write_file_with_sudo(backup_path, content)
            else:
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)

            try:
                # 文字列を置換
                new_content = content.replace(old_str, new_str)

                # 新しい内容を書き込む
                if sudo:
                    FileOperations._write_file_with_sudo(file_path, new_content)
                else:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                # 成功したらバックアップを削除
                os.remove(backup_path)

            except Exception as e:
                # エラーが発生した場合、バックアップから復元
                if os.path.exists(backup_path):
                    if sudo:
                        FileOperations._write_file_with_sudo(file_path, content)
                    else:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                raise e

        except (IOError, OSError) as e:
            raise PermissionError(f"Failed to modify file: {str(e)}")

    @staticmethod
    def create_file(file_path: str, content: str, sudo: bool = False) -> None:
        """
        新しいファイルを作成します

        Args:
            file_path (str): 作成するファイルの絶対パス
            content (str): ファイルの内容
            sudo (bool): root権限での実行

        Raises:
            FileExistsError: ファイルが既に存在する場合
            PermissionError: ファイルを作成できない場合
            OSError: ディレクトリが存在しない場合

        使用例:
            ```xml
            <create_file file="/path/to/file" sudo="false">
            ファイルの内容をここに記述
            </create_file>
            ```
        """
        # ファイルが既に存在するかチェック
        if os.path.exists(file_path):
            raise FileExistsError(f"File already exists: {file_path}")

        # ディレクトリが存在するかチェック
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            raise OSError(f"Directory does not exist: {directory}")

        try:
            # ファイルを作成
            if sudo:
                FileOperations._write_file_with_sudo(file_path, content)
            else:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

            # パーミッションを設定 (644)
            os.chmod(file_path, 0o644)

        except (IOError, OSError) as e:
            raise PermissionError(f"Failed to create file: {str(e)}")
