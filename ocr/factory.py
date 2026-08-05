"""
OCR Factory
-----------
Returns the required OCR engine.
"""

from ocr.easyocr_engine import EasyOCREngine
from ocr.pytesseract_engine import PyTesseractEngine


class OCRFactory:
    """
    Factory class to create OCR engine instances.
    """

    @staticmethod
    def get_engine(name: str):
        """
        Returns the requested OCR engine.

        Supported engines:
        - easyocr
        - pytesseract
        """

        name = name.lower()

        if name == "easyocr":
            return EasyOCREngine()

        elif name == "pytesseract":
            return PyTesseractEngine()

        else:
            raise ValueError(f"Unsupported OCR Engine: {name}")