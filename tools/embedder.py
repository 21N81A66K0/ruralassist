from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model

def embed_text(text_list):
    """
    Takes a list of strings and returns embedding vectors.
    """
    model = get_model()
    return model.encode(text_list, show_progress_bar=True)
