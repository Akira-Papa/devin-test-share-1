"""Service for generating prompts using OpenAI's GPT models."""

from typing import List
from openai import OpenAI

from ..config import settings


class OpenAIService:
    """Service class for interacting with OpenAI's GPT models to generate prompts."""

    def __init__(self):
        """Initialize the OpenAI service with API credentials."""
        self.client = OpenAI(api_key=settings.openai_api_key)

    def _create_system_message(self, tone: str) -> str:
        """Create a system message for the GPT model.

        Args:
            tone: The desired tone for the generated prompt.

        Returns:
            A formatted system message string.
        """
        return f"You are a professional prompt engineer. Generate prompts in a {tone} tone."

    def _create_user_message(self, context: str, requirements: List[str]) -> str:
        """Create a user message containing the prompt requirements.

        Args:
            context: The context for prompt generation.
            requirements: List of specific requirements for the prompt.

        Returns:
            A formatted user message string.
        """
        requirements_text = "\n".join([f"- {req}" for req in requirements])
        return (
            f"Context: {context}\n\n"
            f"Requirements:\n{requirements_text}\n\n"
            "Please generate a prompt that meets these requirements."
        )

    async def generate_prompt(
        self, context: str, requirements: List[str], tone: str
    ) -> str:
        """Generate a prompt using OpenAI's GPT model.

        Args:
            context: The context for prompt generation.
            requirements: List of specific requirements for the prompt.
            tone: The desired tone for the generated prompt.

        Returns:
            The generated prompt string.

        Raises:
            ValueError: If prompt generation fails.
        """
        try:
            system_message = self._create_system_message(tone)
            user_message = self._create_user_message(context, requirements)

            response = await self.client.chat.completions.create(
                model=settings.model_name,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message},
                ],
            )
            return response.choices[0].message.content
        except Exception as e:
            raise ValueError(f"Failed to generate prompt: {str(e)}") from e
