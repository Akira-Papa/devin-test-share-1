"""API routes for prompt generation and management."""

import logging
from datetime import datetime, UTC
from typing import Dict, Any

from fastapi import APIRouter, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from ..config import settings
from ..models.prompt import PromptCreate, Prompt
from ..services.openai_service import OpenAIService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

router = APIRouter()
openai_service = OpenAIService()

client = AsyncIOMotorClient(settings.mongodb_uri)
db = client.prompt_generator
prompts_collection = db.prompts


@router.post("/generate", response_model=Prompt)
async def generate_prompt(prompt_create: PromptCreate):
    """Generate a new prompt based on the provided context and requirements.

    Args:
        prompt_create: The prompt creation request containing context and requirements.

    Returns:
        A Prompt object containing the generated prompt and metadata.

    Raises:
        HTTPException: If prompt generation or storage fails.
    """
    try:
        logger.debug("Received request with data: %s", prompt_create)

        generated_prompt = await openai_service.generate_prompt(
            prompt_create.context, prompt_create.requirements, prompt_create.tone
        )
        logger.debug("Generated prompt: %s", generated_prompt)

        prompt_dict: Dict[str, Any] = prompt_create.model_dump()
        prompt_dict["generated_prompt"] = generated_prompt
        prompt_dict["created_at"] = datetime.now(UTC)

        logger.debug("Inserting document into MongoDB: %s", prompt_dict)
        result = await prompts_collection.insert_one(prompt_dict)
        prompt_dict["id"] = str(result.inserted_id)

        return Prompt(**prompt_dict)
    except Exception as e:
        logger.error("Error in generate_prompt: %s", str(e), exc_info=True)
        error_message = f"Failed to generate prompt: {str(e)}"
        raise HTTPException(status_code=500, detail=error_message) from e
