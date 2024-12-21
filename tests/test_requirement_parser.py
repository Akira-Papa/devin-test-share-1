import pytest
from prompt_generator.models.requirement import Requirement
from prompt_generator.core.requirement_parser import RequirementParser


def test_requirement_parser_valid_input() -> None:
    raw_data = {
        "title": "テスト要件",
        "description": "これはテスト用の要件です",
        "constraints": ["制約1", "制約2"],
        "goals": ["目標1", "目標2"],
        "context": "テストコンテキスト",
    }

    requirement = RequirementParser.parse(raw_data)
    assert isinstance(requirement, Requirement)
    assert requirement.title == "テスト要件"
    assert requirement.description == "これはテスト用の要件です"
    assert len(requirement.constraints) == 2
    assert len(requirement.goals) == 2


def test_requirement_parser_minimal_input() -> None:
    raw_data = {"title": "最小要件", "description": "必須フィールドのみの要件", "context": "最小コンテキスト"}

    requirement = RequirementParser.parse(raw_data)
    assert isinstance(requirement, Requirement)
    assert requirement.title == "最小要件"
    assert requirement.constraints == []
    assert requirement.goals == []
