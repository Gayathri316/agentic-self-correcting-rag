from pathlib import Path

import pytesseract
from PIL import Image

from ocr.base import BaseOCREngine

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class PyTesseractEngine(BaseOCREngine):

    def extract_text(self, image_path: str):

        image = Image.open(image_path)

        text = pytesseract.image_to_string(image)

        print("=" * 50)
        print("TEXT FROM image_to_string():")
        print(repr(text))
        print("=" * 50)

        data = pytesseract.image_to_data(
            image,
            output_type=pytesseract.Output.DICT
        )

        print("WORDS FOUND:")
        print(data["text"])
        print("=" * 50)

        confidences = []

        for conf in data["conf"]:
            try:
                conf = float(conf)
                if conf > 0:
                    confidences.append(conf)
            except ValueError:
                continue

        confidence = (
            sum(confidences) / len(confidences) / 100
            if confidences
            else 0.0
        )

        return text.strip(), confidence