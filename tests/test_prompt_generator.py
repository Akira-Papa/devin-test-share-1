"""Unit tests for the OpenAI service prompt generation functionality."""

from unittest.mock import patch, MagicMock, AsyncMock

import pytest

from src.services.openai_service import OpenAIService


@pytest.fixture
def mock_openai_client():
    """Fixture that mocks the OpenAI client for testing."""
    with patch("src.services.openai_service.OpenAI") as mock:
        mock_instance = MagicMock()
        mock_instance.chat.completions.create = AsyncMock(
            return_value=MagicMock(
                choices=[MagicMock(message=MagicMock(content="Test generated prompt"))]
            )
        )
        mock.return_value = mock_instance
        yield mock


@pytest.fixture
def openai_service():
    """Fixture that provides a configured OpenAIService instance for testing."""
    with patch("src.services.openai_service.OpenAI") as mock:
        mock_instance = MagicMock()
        mock_instance.chat.completions.create = AsyncMock(
            return_value=MagicMock(
                choices=[MagicMock(message=MagicMock(content="Test generated prompt"))]
            )
        )
        mock.return_value = mock_instance
        service = OpenAIService()
        yield service


@pytest.mark.asyncio
async def test_generate_prompt(openai_service):
    """Test the prompt generation functionality.

    Args:
        openai_service: OpenAIService instance configured with mocked client.
    """
    context = "Test context"
    requirements = ["req1", "req2"]
    tone = "professional"

    result = await openai_service.generate_prompt(context, requirements, tone)

    assert result == "Test generated prompt"
    assert openai_service.client.chat.completions.create.call_count == 1

    call_args = openai_service.client.chat.completions.create.call_args[1]
    assert len(call_args["messages"]) == 2
    assert call_args["messages"][0]["role"] == "system"
    assert call_args["messages"][1]["role"] == "user"
    assert "professional" in call_args["messages"][0]["content"]
    assert "Test context" in call_args["messages"][1]["content"]
