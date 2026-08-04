"""
PDF Loader Module
-----------------
Loads PDF documents and converts them into a Document object.
"""

import fitz  # PyMuPDF
from pathlib import Path

from ingestion.models import Document


class PDFLoader:
    """
    Loads PDF files and extracts text.
    """

    def load(self, file_path: str) -> Document:
        """
        Reads a PDF file and returns a Document object.
        """

        pdf = fitz.open(file_path)

        full_text = ""

        for page in pdf:
            full_text += page.get_text()

        metadata = pdf.metadata
        page_count = pdf.page_count

        pdf.close()

        return Document(
            text=full_text,
            source=file_path,
            file_name=Path(file_path).name,
            file_type="pdf",
            page_count=page_count,
            ocr_used=False,
            metadata={
                "title": metadata.get("title"),
                "author": metadata.get("author"),
                "producer": metadata.get("producer"),
                "creator": metadata.get("creator"),
            },
        )