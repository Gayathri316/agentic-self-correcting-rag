import easyocr

from ocr.base import BaseOCREngine


class EasyOCREngine(BaseOCREngine):

    def __init__(self):
        self.reader = easyocr.Reader(["en"])

    def extract_text(self, image_path: str):

        results = self.reader.readtext(image_path)

        text = "\n".join([item[1] for item in results])

        confidence = 0

        if len(results):

            confidence = sum(item[2] for item in results) / len(results)

        return text, confidence