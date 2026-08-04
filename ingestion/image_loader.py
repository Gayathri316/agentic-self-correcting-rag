"""
Image Loader Module
-------------------
Loads image files and extracts text using EasyOCR.
"""

from pathlib import Path

import easyocr

from ingestion.models import Document


class ImageLoader:
    """
    Loads image files and performs OCR.
    """

    def __init__(self):
        # Create OCR model once
        self.reader = easyocr.Reader(['en'])

    def load(self, file_path: str) -> Document:

        result = self.reader.readtext(file_path)

        extracted_text = "\n".join([item[1] for item in result])

        return Document(
            text=extracted_text,
            source=file_path,
            file_name=Path(file_path).name,
            file_type=Path(file_path).suffix.replace(".", ""),
            page_count=1,
            ocr_used=True,
            metadata={}
        )