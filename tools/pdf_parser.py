"""
PDF Parser Tool

Parses PDF files and chunks them with overlap for RAG system.
"""

from typing import List
from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file using pdfminer.
    
    Args:
        pdf_path: Path to PDF file
        
    Returns:
        Extracted text from PDF
    """
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return ""


def chunk_text(text: str, chunk_size: int = 300) -> List[str]:
    """
    Split text into chunks of specified size.
    
    Args:
        text: Text to chunk
        chunk_size: Size of each chunk in words
        
    Returns:
        List of text chunks
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)
    return chunks
