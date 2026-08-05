from abc import ABC, abstractmethod


class OCREngine(ABC):
    """
    Base class for every OCR engine.
    """

    @abstractmethod
    def extract_text(self, image_path: str):
        pass