from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient, models

MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"
COLLECTION_NAME = "my_multilingual_docs"

# 1. Initialize the Sentence Transformer model
print("Loading sentence transformer model...")
model = SentenceTransformer(MODEL_NAME)
print("✅ Model loaded.")

# 2. Sample documents in English
documents = [
    {"text": "The black cat gracefully jumped over the lazy brown dog.", "source": "internal"},
    {"text": "Artificial intelligence is rapidly changing the tech industry.", "source": "blog_post"},
    {"text": "A serene sunset painted the sky with vibrant colors over the lake.", "source": "gallery"},
    {"text": "Learning a new programming language is a rewarding challenge.", "source": "tutorial"},
    {"text": "Global financial markets reacted to the latest economic news.", "source": "news_feed"},
]

# 3. Initialize Qdrant client
client = QdrantClient(url="http://localhost:6333")

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