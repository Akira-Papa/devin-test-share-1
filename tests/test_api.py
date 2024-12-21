"""Integration tests for the prompt generation API endpoints."""

import logging
from unittest.mock import patch, MagicMock, AsyncMock

import pytest
from bson import ObjectId
from fastapi.testclient import TestClient

from src.main import app

# Configure logging for tests
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

client = TestClient(app)


@pytest.fixture
def mock_openai_service():
    """Fixture that mocks the OpenAI service for testing."""
    with patch("src.api.routes.openai_service") as mock:
        mock.generate_prompt = AsyncMock(return_value="Generated test prompt")
        yield mock


@pytest.fixture
def mock_mongodb():
    """Fixture that mocks the MongoDB collection for testing."""
    with patch("src.api.routes.prompts_collection") as mock:
        mock.insert_one = AsyncMock(return_value=MagicMock(inserted_id=ObjectId()))
        yield mock


@pytest.mark.asyncio
async def test_generate_prompt(mock_openai_service):
    """Test the prompt generation endpoint.

    Args:
        mock_openai_service: Mocked OpenAI service fixture.
    """
    test_data = {
        "context": "Test context",
        "requirements": ["req1", "req2"],
        "tone": "professional",
    }

    logger.debug("Sending test request with data: %s", test_data)
    response = client.post("/api/v1/generate", json=test_data)
    logger.debug("Received response: %s - %s", response.status_code, response.text)

    assert response.status_code == 200
    assert "generated_prompt" in response.json()
    assert "id" in response.json()
    assert response.json()["generated_prompt"] == "Generated test prompt"

    mock_openai_service.generate_prompt.assert_called_once_with(
        test_data["context"], test_data["requirements"], test_data["tone"]
    )
