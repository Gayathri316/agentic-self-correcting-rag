import os

print("Running file:", __file__)
print("Current directory:", os.getcwd())
from ingestion.docx_loader import DOCXLoader

loader = DOCXLoader()

document = loader.load("data/raw/JD.docx")  # Use your exact filename

print("=" * 50)
print("File Name :", document.file_name)
print("Type      :", document.file_type)
print("=" * 50)
print(document.text[:1000])