from ingestion.models import Document


doc = Document(
    text="Hello World",
    source="sample.pdf",
    file_name="sample.pdf",
    file_type="pdf",
)

print(doc)