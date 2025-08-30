# file: app.py
from fastapi import FastAPI, HTTPException
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

# --- Configuration ---
MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"
COLLECTION_NAME = "my_multilingual_docs"

# --- Initialize Model and Database Client ---
# This will be loaded once when the application starts
print("Loading sentence transformer model...")
model = SentenceTransformer(MODEL_NAME)
print("✅ Model loaded.")

qdrant_client = QdrantClient("localhost", port=6333)

app = FastAPI(
    title="Semantic Cross-Lingual Search API",
    description="Search for English documents using a query in any language.",
    version="2.0.0",
)

@app.get("/search")
def search(q: str):
    """
    Performs semantic cross-lingual search.
    - q: The search query in any supported language.
    """
    # 1. Encode the incoming query into a vector
    query_vector = model.encode(q).tolist()

    # 2. Use the vector to search for similar documents in Qdrant
    try:
        hits = qdrant_client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=3  # Return the top 3 most similar results
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching Qdrant: {e}")

    # 3. Format and return the results
    results = [
        {"score": hit.score, "payload": hit.payload} for hit in hits
    ]
    
    return {
        "original_query": q,
        "results": results
    }