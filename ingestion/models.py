"""
Data models used throughout the document ingestion pipeline.
"""

from pydantic import BaseModel, Field
from typing import Optional
from pathlib import Path


class Document(BaseModel):
    """
    Represents a single document after it has been loaded.
    """

    text: str = Field(
        ...,
        description="Extracted text from the document"
    )

    source: str = Field(
        ...,
        description="Original file path"
    )

    file_name: str = Field(
        ...,
        description="Name of the uploaded file"
    )

    file_type: str = Field(
        ...,
        description="File extension (pdf, docx, png...)"
    )

    page_count: int = Field(
        default=1,
        description="Number of pages"
    )

    ocr_used: bool = Field(
        default=False,
        description="Whether OCR was required"
    )

    metadata: dict = Field(
        default_factory=dict,
        description="Additional document information"
    )