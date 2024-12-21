from prompt_generator.utils.validators import validate_requirement, validate_prompt


def test_validate_requirement_valid() -> None:
    """有効な要件データのバリデーションをテストする"""
    valid_data = {
        "title": "テスト要件",
        "description": "これはテスト用の要件です",
        "constraints": ["制約1", "制約2"],
        "goals": ["目標1", "目標2"],
        "context": "テストコンテキスト",
    }
    assert validate_requirement(valid_data) is True


def test_validate_requirement_invalid() -> None:
    """無効な要件データのバリデーションをテストする"""
    invalid_data = {
        "title": "テスト要件",
        # descriptionが欠落
        "constraints": ["制約1", "制約2"],
    }
    assert validate_requirement(invalid_data) is False


def test_validate_prompt_valid() -> None:
    """有効なプロンプトデータのバリデーションをテストする"""
    valid_data = {
        "system_prompt": "テストプロンプト",
        "context": "テストコンテキスト",
        "constraints": ["制約1", "制約2"],
        "capabilities": ["機能1", "機能2"],
        "metadata": {"key": "value"},
    }
    assert validate_prompt(valid_data) is True


def test_validate_prompt_invalid() -> None:
    """無効なプロンプトデータのバリデーションをテストする"""
    invalid_data = {
        "system_prompt": "テストプロンプト",
        # contextが欠落
        "constraints": ["制約1", "制約2"],
    }
    assert validate_prompt(invalid_data) is False
