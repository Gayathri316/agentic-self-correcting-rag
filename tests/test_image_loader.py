from ingestion.image_loader import ImageLoader

loader = ImageLoader()

document = loader.load("data/raw/image.jpg")

print("=" * 50)
print("File :", document.file_name)
print("OCR :", document.ocr_used)
print("=" * 50)
print(document.text)