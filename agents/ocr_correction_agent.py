"""
OCR Correction Agent
--------------------
Uses Gemini to correct OCR mistakes while preserving the original meaning.
"""

from services.llm_service import LLMService


class OCRCorrectionAgent:
    """
    AI agent that corrects OCR errors.
    """

    def __init__(self):
        self.llm = LLMService()

    def correct(self, text: str, confidence: float) -> str:
        """
        Correct OCR text only when confidence is low.
        """

        # If OCR is already good, return original text
        if confidence >= 0.60:
            return text

        prompt = f"""
You are an OCR correction assistant.

Correct only OCR spelling mistakes.

Rules:
1. Do NOT add new information.
2. Do NOT remove information.
3. Preserve formatting.
4. If unsure, leave the word unchanged.

OCR Text:

{text}

Return only the corrected text.
"""

        corrected = self.llm.generate(prompt)

        return corrected