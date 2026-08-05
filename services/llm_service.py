"""
LLM Service
-----------
Provides a reusable interface for interacting with Gemini.
"""

import os

from dotenv import load_dotenv
from google import genai


class LLMService:
    """
    Wrapper around Gemini API.
    """

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env"
            )

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-2.5-flash-lite"
        self.model = os.getenv("GEMINI_MODEL")

    def generate(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text.strip()