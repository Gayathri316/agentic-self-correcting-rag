from ingestion.pdf_loader import PDFLoader

loader = PDFLoader()

document = loader.load(
    "data/raw/resume.pdf"
)

print("=" * 50)
print("File Name :", document.file_name)
print("Pages     :", document.page_count)
print("Type      :", document.file_type)
print("OCR Used  :", document.ocr_used)
print("=" * 50)
print(document.text[:1000])   # Print first 1000 characters