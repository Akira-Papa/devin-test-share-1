# devin-test-share-1

devin共有用テスト

# プロンプト生成システム

要件定義からAIエージェント向けのシステムプロンプトを生成するPythonベースのモジュラーモノリスシステムです。

## 機能

- 要件定義の構造化されたパース
- システムプロンプトの生成
- 型安全な実装
- バリデーション機能

## 開発環境のセットアップ

```bash
# Poetry のインストール
curl -sSL https://install.python-poetry.org | python3 -

# 依存関係のインストール
poetry install

# 開発環境の有効化
poetry shell
```

## テストの実行

```bash
pytest tests/ --cov=prompt_generator
```

## リンターとフォーマッターの実行

```bash
# コードフォーマット
black .

# 型チェック
mypy .

# リンター
flake8
```
