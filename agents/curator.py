import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import faiss
from tools.pdf_parser import extract_text_from_pdf
from tools.embedder import embed_text
from tools.logger import log

RAW_DIR = "data/raw"
VECTOR_DIR = "data/vector_store"
INDEX_PATH = os.path.join(VECTOR_DIR, "faiss.index")
CHUNKS_PATH = os.path.join(VECTOR_DIR, "chunks.txt")

def chunk_text(text, chunk_size=300):
    """
    Splits large text into smaller chunks for embedding.
    """
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i+chunk_size])

def build_vector_store():
    os.makedirs(VECTOR_DIR, exist_ok=True)

    all_chunks = []
    log("Scanning PDFs...")

    for fname in os.listdir(RAW_DIR):
        if fname.endswith(".pdf"):
            pdf_path = os.path.join(RAW_DIR, fname)
            log(f"Extracting text from {pdf_path}")
            text = extract_text_from_pdf(pdf_path)
            chunks = list(chunk_text(text))
            all_chunks.extend(chunks)

    log(f"Total chunks: {len(all_chunks)}")

    embeddings = embed_text(all_chunks)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)
    log(f"Vector store saved to {INDEX_PATH}")

    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        for ch in all_chunks:
            f.write(ch + "\n===\n")

    log("Chunks saved successfully.")

if __name__ == "__main__":
    build_vector_store()
