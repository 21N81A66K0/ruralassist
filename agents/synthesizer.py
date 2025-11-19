import faiss
from tools.embedder import embed_text
from tools.logger import log

VECTOR_DIR = "data/vector_store"
INDEX_PATH = f"{VECTOR_DIR}/faiss.index"
CHUNKS_PATH = f"{VECTOR_DIR}/chunks.txt"


def load_chunks():
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        return f.read().split("===\n")


def clean_chunk(chunk: str) -> str:
    """Basic cleaning of retrieved text."""
    return chunk.replace("\n", " ").strip()


def synthesize_knowledge(query_info: dict) -> dict:
    query = query_info["clean_query"]

    # Load vector index
    index = faiss.read_index(INDEX_PATH)

    # Embed the query
    query_emb = embed_text([query])

    # Retrieve top-k similar chunks
    distances, indices = index.search(query_emb, k=3)

    chunks = load_chunks()

    retrieved = []
    for i in indices[0]:
        if i < len(chunks):
            cleaned = clean_chunk(chunks[i])
            if len(cleaned) > 30:  # discard very tiny chunks
                retrieved.append(cleaned)

    log(f"Retrieved {len(retrieved)} evidence chunks for query: {query}")

    return {
        "query": query,
        "category": query_info["category"],
        "evidence_chunks": retrieved
    }
