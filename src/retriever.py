from sentence_transformers import SentenceTransformer
import chromadb
from config.config_loader import load_config

cfg = load_config()

# Load embedding model once (this is safe to cache)
model = SentenceTransformer(cfg["embedding"]["model"])


def get_collection():
    """
    Always reconnect to Chroma and fetch the latest collection.
    Prevents stale references after reset/delete/rebuild.
    """
    client = chromadb.PersistentClient(path=cfg["database"]["path"])
    return client.get_or_create_collection(
        cfg["database"]["collection_name"]
    )


def retrieve(query, top_k=None):
    """
    Retrieve relevant code snippets for a query.
    """
    collection = get_collection()

    k = top_k or cfg["retrieval"]["top_k"]

    # Embed query
    q_emb = model.encode([query]).tolist()[0]

    # Query Chroma
    result = collection.query(
        query_embeddings=[q_emb],
        n_results=k
    )

    return result