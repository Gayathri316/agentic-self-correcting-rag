"""
OCR Selection Agent
-------------------
Chooses the best OCR engine based on quality score.
"""

from ocr.factory import OCRFactory
from agents.ocr_quality_agent import OCRQualityAgent


class OCRSelectionAgent:

    def __init__(self):
        self.easyocr = OCRFactory.get_engine("easyocr")
        self.pytesseract = OCRFactory.get_engine("pytesseract")
        self.quality_agent = OCRQualityAgent()

    def select_best_ocr(self, image_path):

        # EasyOCR
        easy_text, easy_conf = self.easyocr.extract_text(image_path)
        easy_score = self.quality_agent.evaluate(
            easy_text,
            easy_conf
        )

        # PyTesseract
        pyt_text, pyt_conf = self.pytesseract.extract_text(image_path)
        pyt_score = self.quality_agent.evaluate(
            pyt_text,
            pyt_conf
        )

        print("\n========== OCR Comparison ==========")
        print(f"EasyOCR Score      : {easy_score:.3f}")
        print(f"PyTesseract Score  : {pyt_score:.3f}")
        print("====================================\n")

        if easy_score >= pyt_score:
            return easy_text, easy_conf, "EasyOCR"

        return pyt_text, pyt_conf, "PyTesseract"