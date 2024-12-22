"""
シェル操作関連のコマンド

このモジュールは、シェル操作に関連する各種コマンドの実装を提供します。
プロセス管理、出力キャプチャ、入力送信、プロセス終了などの機能を含みます。
"""

import subprocess
import signal
import os
import time
from typing import Dict, List, Optional

class ShellCommands:
    """シェルコマンドの実行を管理するクラス
    
    このクラスは、シェルコマンドの実行、プロセス管理、出力の取得、
    プロセスへの入力送信、プロセスの終了処理などの機能を提供します。
    
    Attributes:
        _process_dict (Dict[str, subprocess.Popen]): シェルIDとプロセスの対応を管理
        _output_dict (Dict[str, List[str]]): シェルIDと出力履歴の対応を管理
    """
    
    _process_dict: Dict[str, subprocess.Popen] = {}
    _output_dict: Dict[str, List[str]] = {}
    
    @staticmethod
    def execute(shell_id: str, exec_dir: str, command: str) -> None:
        """
        指定されたディレクトリでbashコマンドを実行します

        Args:
            shell_id (str): シェルセッションの識別子
            exec_dir (str): コマンドを実行するディレクトリ（絶対パス）
            command (str): 実行するbashコマンド

        Raises:
            ValueError: shell_idが空の場合
            FileNotFoundError: 実行ディレクトリが存在しない場合
            RuntimeError: プロセスの起動に失敗した場合

        使用例:
            ```xml
            <shell id="shellId" exec_dir="/path/to/dir">ls -la</shell>
            ```
        
        注意事項:
            - exec_dirは必須で、絶対パスである必要があります
        """
        if not shell_id:
            raise ValueError("shell_id must not be empty")
            
        if not os.path.exists(exec_dir):
            raise FileNotFoundError(f"Directory not found: {exec_dir}")
            
        try:
            # 既存のプロセスを終了
            if shell_id in ShellCommands._process_dict:
                ShellCommands.kill_process(shell_id)
            
            # 新しいプロセスを開始
            process = subprocess.Popen(
                command,
                shell=True,
                cwd=exec_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                stdin=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                preexec_fn=os.setsid  # プロセスグループを作成
            )
            
            ShellCommands._process_dict[shell_id] = process
            ShellCommands._output_dict[shell_id] = []
            
        except subprocess.SubprocessError as e:
            raise RuntimeError(f"Failed to execute command: {str(e)}")

    @staticmethod
    def view_output(shell_id: str) -> str:
        """
        指定されたシェルの最新の出力を表示します

        Args:
            shell_id (str): 表示するシェルセッションの識別子

        Returns:
            str: シェルの出力内容

        Raises:
            ValueError: shell_idが空の場合
            RuntimeError: プロセスが存在しない場合

        使用例:
            ```xml
            <view_shell id="shellId"/>
            ```
        """
        if not shell_id:
            raise ValueError("shell_id must not be empty")
            
        if shell_id not in ShellCommands._process_dict:
            raise RuntimeError(f"No process found for shell_id: {shell_id}")
            
        process = ShellCommands._process_dict[shell_id]
        output_buffer = []
        
        # 新しい出力を読み込む
        while True:
            # 出力をポーリング
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                output_buffer.append(output.strip())
                ShellCommands._output_dict[shell_id].append(output.strip())
        
        return "\n".join(output_buffer) if output_buffer else ""

    @staticmethod
    def write_to_process(shell_id: str, text: str, press_enter: bool = True) -> None:
        """
        実行中のシェルプロセスにテキストを送信します

        Args:
            shell_id (str): シェルセッションの識別子
            text (str): 送信するテキスト
            press_enter (bool): Enterキーを押すかどうか

        Raises:
            ValueError: shell_idが空の場合
            RuntimeError: プロセスが存在しないか、入力の送信に失敗した場合

        使用例:
            ```xml
            <write_to_shell_process id="shellId" press_enter="true">command text</write_to_shell_process>
            ```

        特記事項:
            - Unicodeエスケープシーケンスをサポート（例：\u0003 for Control+C）
        """
        if not shell_id:
            raise ValueError("shell_id must not be empty")
            
        if shell_id not in ShellCommands._process_dict:
            raise RuntimeError(f"No process found for shell_id: {shell_id}")
            
        process = ShellCommands._process_dict[shell_id]
        
        try:
            # Unicodeエスケープシーケンスを処理
            processed_text = text.encode().decode('unicode-escape')
            
            # 入力を送信
            process.stdin.write(processed_text)
            if press_enter:
                process.stdin.write("\n")
            process.stdin.flush()
            
        except (IOError, ValueError) as e:
            raise RuntimeError(f"Failed to write to process: {str(e)}")

    @staticmethod
    def kill_process(shell_id: str) -> None:
        """
        シェルプロセスを終了します

        Args:
            shell_id (str): 終了するシェルセッションの識別子

        Raises:
            ValueError: shell_idが空の場合

        使用例:
            ```xml
            <kill_shell_process id="shellId"/>
            ```

        特記事項:
            - 複数のkill_shell_processコマンドを同時に実行可能
            - シェル自体は存在し続け、新しいコマンドで再利用可能
            - プロセスグループ全体を終了させる
            - 通常の終了(SIGTERM)を試み、応答がない場合は強制終了(SIGKILL)
        """
        if not shell_id:
            raise ValueError("shell_id must not be empty")
            
        if shell_id in ShellCommands._process_dict:
            process = ShellCommands._process_dict[shell_id]
            
            try:
                # プロセスグループ全体を終了
                os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                
                # 最大3秒待機
                for _ in range(30):
                    if process.poll() is not None:
                        break
                    time.sleep(0.1)
                    
                # 強制終了
                if process.poll() is None:
                    os.killpg(os.getpgid(process.pid), signal.SIGKILL)
                    
            except (ProcessLookupError, OSError):
                pass  # プロセスが既に終了している場合は無視
                
            finally:
                # 辞書からエントリを削除
                del ShellCommands._process_dict[shell_id]
                if shell_id in ShellCommands._output_dict:
                    del ShellCommands._output_dict[shell_id]
