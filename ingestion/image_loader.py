"""
Image Loader Module
-------------------
Loads image files and extracts text using the best OCR engine.
"""

from pathlib import Path

from ingestion.models import Document
from ingestion.image_preprocessor import ImagePreprocessor
from agents.ocr_selection_agent import OCRSelectionAgent


class ImageLoader:
    """
    Loads image files and performs OCR.
    """

    def __init__(self):
        # Initialize image preprocessor
        self.preprocessor = ImagePreprocessor()

        # Initialize OCR Selection Agent
        self.ocr_agent = OCRSelectionAgent()

    def load(self, file_path: str) -> Document:
        """
        Preprocess image and extract text using the best OCR engine.
        """

        # Step 1: Preprocess image
        processed_image = self.preprocessor.preprocess(file_path)

        # Step 2: Let the OCR agent decide the best engine
        extracted_text, confidence, engine = (
            self.ocr_agent.select_best_ocr(processed_image)
        )

        # Step 3: Return Document
        return Document(
            text=extracted_text,
            source=file_path,
            file_name=Path(file_path).name,
            file_type=Path(file_path).suffix.replace(".", ""),
            page_count=1,
            ocr_used=True,
            metadata={
                "ocr_engine": engine,
                "ocr_confidence": confidence,
                "processed_image": str(processed_image),
            },
        )