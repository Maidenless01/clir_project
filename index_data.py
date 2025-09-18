from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient, models
from app import MODEL_NAME, COLLECTION_NAME
import json
import urllib.request
import importlib.metadata as importlib_metadata
import os

# 1. Initialize the Sentence Transformer model
print("Loading sentence transformer model...")
model = SentenceTransformer(MODEL_NAME)
print("✅ Model loaded.")
# Version expectations
EXPECTED_QDRANT_SERVER_VERSION = os.getenv("QDRANT_VERSION", "1.15.1")
EXPECTED_QDRANT_CLIENT_VERSION = os.getenv("QDRANT_CLIENT_VERSION", EXPECTED_QDRANT_SERVER_VERSION)

def _get_qdrant_server_version(host: str = "localhost", port: int = 6333) -> str | None:
    try:
        with urllib.request.urlopen(f"http://{host}:{port}") as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("version")
    except Exception:
        return None

def _check_qdrant_versions() -> None:
    server_version = _get_qdrant_server_version("localhost", 6333)
    client_version = importlib_metadata.version("qdrant-client")
    print(f"Qdrant versions → server={server_version}, client={client_version}, expected={EXPECTED_QDRANT_SERVER_VERSION}")
    if not server_version:
        raise RuntimeError("Cannot reach Qdrant at http://localhost:6333. Is the container running?")
    if server_version.lstrip("v") != str(EXPECTED_QDRANT_SERVER_VERSION).lstrip("v") or client_version != str(EXPECTED_QDRANT_CLIENT_VERSION):
        raise RuntimeError(
            "Qdrant version mismatch. Align docker image tag and Python client. "
            f"Server={server_version}, Client={client_version}, Expected={EXPECTED_QDRANT_SERVER_VERSION}"
        )

_check_qdrant_versions()

# 2. Sample documents in English
documents = [
    {"text": "The black cat gracefully jumped over the lazy brown dog.", "source": "internal"},
    {"text": "Artificial intelligence is rapidly changing the tech industry.", "source": "blog_post"},
    {"text": "A serene sunset painted the sky with vibrant colors over the lake.", "source": "gallery"},
    {"text": "Learning a new programming language is a rewarding challenge.", "source": "tutorial"},
    {"text": "Global financial markets reacted to the latest economic news.", "source": "news_feed"},
]

# 3. Initialize Qdrant client
client = QdrantClient("localhost", port=6333)

# 4. Create a Qdrant collection to store vectors
# The vector size must match the model's output dimension
vector_size = model.get_sentence_embedding_dimension()

client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
)
print(f"Collection '{COLLECTION_NAME}' created.")

# 5. Encode the documents and upload them to Qdrant
print("Encoding documents into vectors...")
vectors = model.encode([doc["text"] for doc in documents])
print("✅ Documents encoded.")

print("Uploading vectors to Qdrant...")
client.upsert(
    collection_name=COLLECTION_NAME,
    points=models.Batch(
        ids=list(range(len(documents))),  # Simple sequential IDs
        payloads=documents,               # The original text data as payload
        vectors=vectors.tolist(),         # The encoded vectors
    ),
    wait=True,
)
print("✅ Upload complete.")
