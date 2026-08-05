from ocr.pytesseract_engine import PyTesseractEngine

ocr = PyTesseractEngine()

text, confidence = ocr.extract_text("data/raw/image.jpg")   # Your image

print("=" * 50)
print("Confidence:", confidence)
print("=" * 50)
print(text)