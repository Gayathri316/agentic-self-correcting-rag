"""
PDF Loader Module
-----------------
Loads PDF documents and converts them into a Document object.
"""

import fitz  # PyMuPDF

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

        pdf.close()

        return Document(
            text=full_text,
            source=file_path,
            file_name=file_path.split("\\")[-1],
            file_type="pdf",
            page_count=len(pdf),
            ocr_used=False
        )