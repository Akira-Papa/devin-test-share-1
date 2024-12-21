"""Pydantic models for prompt generation and management."""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class PromptBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    context: str
    requirements: List[str]
    tone: Optional[str] = "professional"


class PromptCreate(PromptBase):
    pass


class Prompt(PromptBase):
    id: str
    generated_prompt: str
    created_at: datetime
