"""
デプロイメント関連のコマンド

このモジュールは、アプリケーションのデプロイに関連する各種コマンドの実装を提供します。
実際のデプロイの代わりにモックとして動作し、操作内容をコンソールに出力します。
"""

import os
import time
from typing import Optional, Dict, Union

class Deployment:
    """デプロイメント操作を管理するクラス"""

    @staticmethod
    def deploy_frontend(directory: str) -> Dict[str, str]:
        """
        フロントエンドアプリケーションをデプロイします

        Args:
            directory (str): デプロイするサイトのディレクトリパス

        Returns:
            Dict[str, str]: デプロイ情報
            辞書には以下のキーが含まれます：
            - url: デプロイされたサイトのURL
            - status: デプロイのステータス

        Raises:
            ValueError: ディレクトリパスが無効な場合
            FileNotFoundError: ディレクトリが存在しない場合
            RuntimeError: デプロイに失敗した場合

        使用例:
            ```xml
            <deploy_frontend dir="/path/to/site"/>
            ```

        注意事項:
            デプロイ後にウェブサイトが正常に読み込まれることを確認する必要があります
        """
        if not directory:
            raise ValueError("デプロイするディレクトリを指定する必要があります")
        if not os.path.exists(directory):
            raise FileNotFoundError(f"指定されたディレクトリが存在しません: {directory}")
        if not os.path.isdir(directory):
            raise ValueError(f"指定されたパスはディレクトリではありません: {directory}")
            
        print(f"[Deploy mock] フロントエンドアプリケーションをデプロイ: {directory}")
        print("[Deploy mock] ビルド処理を実行...")
        time.sleep(1)  # デプロイ処理のシミュレーション
        print("[Deploy mock] デプロイ完了")
        
        # モックのデプロイ情報を返す
        return {
            "url": "https://example.com/deployed-frontend",
            "status": "success"
        }

    @staticmethod
    def deploy_backend(directory: Optional[str] = None, logs: bool = False) -> Dict[str, Union[str, int]]:
        """
        Pythonバックエンドアプリケーションをデプロイします


        Args:
            directory (str, optional): プロジェクトディレクトリパス
            logs (bool): ログを表示するかどうか

        Returns:
            Dict[str, Union[str, int]]: デプロイ情報
            辞書には以下のキーが含まれます：
            - url: デプロイされたAPIのURL
            - port: 使用されているポート番号
            - status: デプロイのステータス
            - logs: ログ情報（logsがTrueの場合のみ）

        Raises:
            ValueError: ディレクトリパスが無効な場合
            FileNotFoundError: ディレクトリが存在しない場合
            RuntimeError: デプロイに失敗した場合

        使用例:
            ```xml
            <deploy_backend dir="/path/to/project"/>
            <deploy_backend logs="true"/>
            ```
        """
        if directory:
            if not os.path.exists(directory):
                raise FileNotFoundError(f"指定されたディレクトリが存在しません: {directory}")
            if not os.path.isdir(directory):
                raise ValueError(f"指定されたパスはディレクトリではありません: {directory}")
                
            print(f"[Deploy mock] バックエンドアプリケーションをデプロイ: {directory}")
            print("[Deploy mock] 依存関係をインストール...")
            time.sleep(1)  # インストール処理のシミュレーション
            print("[Deploy mock] デプロイ完了")
            
        if logs:
            print("[Deploy mock] ログを表示:")
            print("2024-01-24 12:00:01 INFO  サーバー起動")
            print("2024-01-24 12:00:02 INFO  データベース接続確立")
            print("2024-01-24 12:00:03 INFO  APIエンドポイント準備完了")
            
        # モックのデプロイ情報を返す
        result = {
            "url": "https://api.example.com",
            "port": 8000,
            "status": "running"
        }
        
        if logs:
            result["logs"] = """
2024-01-24 12:00:01 INFO  サーバー起動
2024-01-24 12:00:02 INFO  データベース接続確立
2024-01-24 12:00:03 INFO  APIエンドポイント準備完了
"""
            
        return result

    @staticmethod
    def expose_port(local_port: int) -> Dict[str, Union[str, int]]:
        """
        ローカルポートをインターネットに公開します

        Args:
            local_port (int): 公開するローカルポート番号（1-65535）

        Returns:
            Dict[str, Union[str, int]]: 公開情報
            辞書には以下のキーが含まれます：
            - local_port: ローカルポート番号
            - public_url: 公開されたURL
            - status: 公開のステータス

        Raises:
            ValueError: ポート番号が無効な場合
            RuntimeError: ポートの公開に失敗した場合

        使用例:
            ```xml
            <expose_port local_port="8080"/>
            ```
        """
        if not isinstance(local_port, int):
            raise ValueError("ポート番号は整数である必要があります")
        if local_port < 1 or local_port > 65535:
            raise ValueError("ポート番号は1から65535の範囲である必要があります")
            
        print(f"[Port mock] ローカルポート {local_port} を公開...")
        time.sleep(1)  # 公開処理のシミュレーション
        print("[Port mock] トンネリング設定完了")
        
        # モックの公開情報を返す
        return {
            "local_port": local_port,
            "public_url": f"https://example.com:{local_port}",
            "status": "active"
        }

    @staticmethod
    def view_pr(repo: str, pull_number: int) -> Dict[str, Union[str, int, list, dict]]:
        """
        GitHubのプルリクエストを表示します

        Args:
            repo (str): リポジトリ名（owner/repo形式）
            pull_number (int): プルリクエスト番号

        Returns:
            Dict[str, Union[str, int, list, dict]]: プルリクエストの情報
            辞書には以下のキーが含まれます：
            - title: PRのタイトル
            - number: PR番号
            - state: PRの状態（open/closed/merged）
            - author: 作成者
            - created_at: 作成日時
            - updated_at: 更新日時
            - commits: コミット情報のリスト
            - files: 変更ファイルの情報
            - comments: コメント情報

        Raises:
            ValueError: パラメータが無効な場合
            RuntimeError: PRの取得に失敗した場合

        使用例:
            ```xml
            <gh_view_pr repo="owner/repo" pull_number="123"/>
            ```
        """
        if not repo or "/" not in repo:
            raise ValueError("リポジトリ名は'owner/repo'形式である必要があります")
        if pull_number < 1:
            raise ValueError("PR番号は1以上である必要があります")

        try:
            import subprocess
            import json
            from datetime import datetime

            # GitHub CLIを使用してPR情報を取得
            fields = [
                "title",
                "number",
                "state",
                "author",
                "createdAt",
                "updatedAt",
                "commits",
                "files",
                "comments",
                "body",
                "baseRefName",
                "headRefName",
                "mergeable",
                "reviewDecision"
            ]

            result = subprocess.run(
                ["gh", "pr", "view", str(pull_number),
                 "--repo", repo,
                 "--json", ",".join(fields)],
                capture_output=True,
                text=True,
                check=True
            )

            # JSON形式の結果をパース
            pr_data = json.loads(result.stdout)

            # コミット情報の取得
            commits_result = subprocess.run(
                ["gh", "pr", "view", str(pull_number),
                 "--repo", repo,
                 "--json", "commits"],
                capture_output=True,
                text=True,
                check=True
            )
            commits_data = json.loads(commits_result.stdout)["commits"]

            # 変更ファイル情報の取得
            files_result = subprocess.run(
                ["gh", "pr", "view", str(pull_number),
                 "--repo", repo,
                 "--json", "files"],
                capture_output=True,
                text=True,
                check=True
            )
            files_data = json.loads(files_result.stdout)["files"]

            # レビューコメントの取得
            reviews_result = subprocess.run(
                ["gh", "pr", "view", str(pull_number),
                 "--repo", repo,
                 "--json", "reviews"],
                capture_output=True,
                text=True,
                check=True
            )
            reviews_data = json.loads(reviews_result.stdout)["reviews"]

            # 情報を整形して返す
            return {
                "title": pr_data["title"],
                "number": pr_data["number"],
                "state": pr_data["state"],
                "author": pr_data["author"]["login"],
                "created_at": pr_data["createdAt"],
                "updated_at": pr_data["updatedAt"],
                "base_branch": pr_data["baseRefName"],
                "head_branch": pr_data["headRefName"],
                "mergeable": pr_data["mergeable"],
                "review_decision": pr_data["reviewDecision"],
                "body": pr_data["body"],
                "commits": [{
                    "sha": commit["oid"],
                    "message": commit["messageHeadline"],
                    "author": commit["authors"][0]["login"] if commit["authors"] else "unknown",
                    "created_at": commit["committedDate"]
                } for commit in commits_data],
                "files": {
                    "changed": len(files_data),
                    "additions": sum(f["additions"] for f in files_data),
                    "deletions": sum(f["deletions"] for f in files_data),
                    "files": [{
                        "path": f["path"],
                        "additions": f["additions"],
                        "deletions": f["deletions"],
                        "status": f["status"]
                    } for f in files_data]
                },
                "reviews": [{
                    "author": review["author"]["login"],
                    "state": review["state"],
                    "submitted_at": review["submittedAt"],
                    "body": review["body"]
                } for review in reviews_data],
                "comments": [{
                    "author": comment["author"]["login"],
                    "body": comment["body"],
                    "created_at": comment["createdAt"]
                } for comment in pr_data["comments"]]
            }

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"GitHub CLIコマンドの実行に失敗しました: {e.stderr}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"GitHub APIのレスポンスの解析に失敗しました: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"PRの取得に失敗しました: {str(e)}")
