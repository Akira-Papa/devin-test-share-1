import pytest
from prompt_generator.models.requirement import Requirement
from prompt_generator.models.prompt import Prompt
from prompt_generator.core.prompt_generator import PromptGenerator

@pytest.fixture
def sample_requirement() -> Requirement:
    return Requirement(
        title="テスト要件",
        description="これはテスト用の要件です",
        constraints=["制約1", "制約2"],
        goals=["目標1", "目標2"],
        context="テストコンテキスト"
    )

def test_prompt_generator_basic(sample_requirement: Requirement) -> None:
    generator = PromptGenerator()
    prompt = generator.generate(sample_requirement)

    assert isinstance(prompt, Prompt)
    assert "テスト要件" in prompt.system_prompt
    assert prompt.context == "これはテスト用の要件です"
    assert len(prompt.constraints) == 2
    assert len(prompt.capabilities) >= 2

def test_prompt_generator_minimal() -> None:
    requirement = Requirement(
        title="最小要件",
        description="必須フィールドのみの要件",
        context="最小コンテキスト"
    )

    generator = PromptGenerator()
    prompt = generator.generate(requirement)

    assert isinstance(prompt, Prompt)
    assert "最小要件" in prompt.system_prompt
    assert prompt.constraints == []
    assert len(prompt.capabilities) >= 2
