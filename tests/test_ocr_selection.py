from ingestion.image_loader import ImageLoader

loader = ImageLoader()

document = loader.load("data/raw/image.jpg")   # Your image path

print("=" * 50)
print("File :", document.file_name)
print("OCR Used :", document.metadata["ocr_engine"])
print("Confidence :", document.metadata["ocr_confidence"])
print("=" * 50)

print(document.text)   # <-- This line is important