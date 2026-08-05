"""
Image Loader Module
-------------------
Loads image files and extracts text using OCR.
"""

from pathlib import Path

from ingestion.models import Document
from ingestion.image_preprocessor import ImagePreprocessor
from ocr.ocr_manager import OCRManager


class ImageLoader:
    """
    Loads image files and performs OCR.
    """

    def __init__(self):

        self.preprocessor = ImagePreprocessor()

        self.ocr_manager = OCRManager()

    def load(self, file_path: str) -> Document:

        # Step 1
        processed_image = self.preprocessor.preprocess(file_path)

        # Step 2
        extracted_text, confidence, engine = (
            self.ocr_manager.extract_text(processed_image)
        )

        # Step 3
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