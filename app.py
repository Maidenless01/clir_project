# file: app.py
import os
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient, models
from googletrans import Translator
import json
import urllib.request
import importlib.metadata as importlib_metadata
import io
from docx import Document
from pypdf import PdfReader
import uuid
import aiofiles

from fastapi.responses import HTMLResponse

# --- Configuration ---
MODEL_NAME = os.getenv("MODEL_NAME", "distiluse-base-multilingual-cased-v1")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "my_multilingual_docs")
EXPECTED_QDRANT_SERVER_VERSION = os.getenv("QDRANT_VERSION", "1.15.1")
EXPECTED_QDRANT_CLIENT_VERSION = os.getenv("QDRANT_CLIENT_VERSION", EXPECTED_QDRANT_SERVER_VERSION)
UPLOADS_DIR = "uploads"

# --- Initialize Model and Database Client ---
print("Loading sentence transformer model...")
model = SentenceTransformer(MODEL_NAME)
print("✅ Model loaded.")

qdrant_client = QdrantClient("localhost", port=6333)
translator = Translator()

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

# Enforce version compatibility on startup
_check_qdrant_versions()

# Ensure Qdrant collection exists at startup
vector_size = model.get_sentence_embedding_dimension()
try:
    qdrant_client.get_collection(COLLECTION_NAME)
except Exception:
    qdrant_client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
    )
    print(f"Collection '{COLLECTION_NAME}' created.")

app = FastAPI(
    title="Semantic Cross-Lingual Search API",
    description="Search for English documents using a query in any language.",
    version="3.0.0",
)

# Create uploads directory if it doesn't exist
os.makedirs(UPLOADS_DIR, exist_ok=True)

# Mount the uploads directory to serve static files
app.mount(f"/{UPLOADS_DIR}", StaticFiles(directory=UPLOADS_DIR), name="uploads")

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.get("/health")
def health():
    server_version = _get_qdrant_server_version("localhost", 6333)
    client_version = importlib_metadata.version("qdrant-client")
    return {
        "status": "ok",
        "qdrant_server_version": server_version,
        "qdrant_client_version": client_version,
        "expected_qdrant_version": EXPECTED_QDRANT_SERVER_VERSION,
        "model_name": MODEL_NAME,
        "collection_name": COLLECTION_NAME,
    }

@app.post("/upload")
async def upload(file: UploadFile = File(...), source: str = Form("uploaded")):
    """
    Upload a .docx, .pdf, or .txt file, extract its text, and index in Qdrant.
    """
    filename = file.filename
    doc_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOADS_DIR, f"{doc_id}_{filename}")

    contents = await file.read()
    # Save the file
    async with aiofiles.open(file_path, 'wb') as out_file:
        await out_file.write(contents)
    
    # Reset file pointer to read again for text extraction
    await file.seek(0)
    contents = await file.read()

    text = ""
    if filename.endswith(".docx"):
        doc = Document(io.BytesIO(contents))
        text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    elif filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(contents))
        text = "\n".join([page.extract_text() for page in reader.pages])
    elif filename.endswith(".txt"):
        text = contents.decode("utf-8")
    else:
        raise HTTPException(status_code=400, detail="Only .docx, .pdf, and .txt files are supported.")

    if not text.strip():
        raise HTTPException(status_code=400, detail="No text found in document.")

    vector = model.encode(text).tolist()
    
    payload = {"text": text, "source": source, "filename": filename, "file_path": file_path}
    qdrant_client.upsert(
        collection_name=COLLECTION_NAME,
        points=models.Batch(
            ids=[doc_id],
            payloads=[payload],
            vectors=[vector],
        ),
        wait=True,
    )
    return {"status": "success", "id": doc_id, "filename": filename, "text": text, "file_path": file_path}

@app.get("/search")
async def search(q: str, limit: int = 5):
    """
    Translate the query to English and perform semantic search.
    """
    try:
        translated_response = await translator.translate(q, dest="en")
        translated = translated_response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error translating query: {e}")

    query_vector = model.encode(translated).tolist()
    try:
        hits = qdrant_client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=limit
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching Qdrant: {e}")

    results = [
        {"score": hit.score, "payload": hit.payload} for hit in hits
    ]
    return {
        "original_query": q,
        "translated_query": translated,
        "results": results
    }
