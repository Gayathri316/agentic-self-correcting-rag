from config.settings import OCR_CONFIDENCE_THRESHOLD
from ocr.factory import OCRFactory


class OCRManager:
    """
    Handles OCR extraction and confidence reporting.
    """

    def __init__(self):
        self.engine = OCRFactory.get_engine("easyocr")

    def extract_text(self, image_path):

        text, confidence = self.engine.extract_text(image_path)

        return text, confidence, "EasyOCR"