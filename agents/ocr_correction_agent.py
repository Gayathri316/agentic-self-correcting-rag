from services.llm_service import LLMService


class OCRCorrectionAgent:

    def __init__(self):
        self.llm = LLMService()

    def correct(
        self,
        text: str,
        confidence: float
    ):
        pass