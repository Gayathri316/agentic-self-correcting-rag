"""
Base OCR Engine
---------------
Defines the interface that every OCR engine must implement.
"""

from abc import ABC, abstractmethod


class BaseOCREngine(ABC):
    """
    Abstract base class for OCR engines.
    """

    @abstractmethod
    def extract_text(self, image_path: str):
        """
        Extract text from an image.

        Returns:
            tuple[str, float]:
                Extracted text and confidence score.
        """
        pass