from ocr.easyocr_engine import EasyOCREngine


class OCRFactory:

    @staticmethod
    def get_engine(name):

        if name.lower() == "easyocr":
            return EasyOCREngine()

        raise ValueError(f"Unsupported OCR Engine: {name}")