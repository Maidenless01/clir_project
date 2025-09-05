# file: app.py
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient, models
from googletrans import Translator
import io
from docx import Document
import PyPDF2
import uuid

from fastapi.responses import HTMLResponse

# --- Configuration ---
MODEL_NAME = "distiluse-base-multilingual-cased-v1"
COLLECTION_NAME = "my_multilingual_docs"

# --- Initialize Model and Database Client ---
print("Loading sentence transformer model...") 
model = SentenceTransformer(MODEL_NAME)
print("✅ Model loaded.")

qdrant_client = QdrantClient("localhost", port=6333)
translator = Translator()

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

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.post("/upload")
async def upload(file: UploadFile = File(...), source: str = Form("uploaded")):
    """
    Upload a .docx, .pdf, or .txt file, extract its text, and index in Qdrant.
    """
    filename = file.filename
    text = ""
    if filename.endswith(".docx"):
        contents = await file.read()
        doc = Document(io.BytesIO(contents))
        text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    elif filename.endswith(".pdf"):
        contents = await file.read()
        reader = PyPDF2.PdfReader(io.BytesIO(contents))
        text = "\n".join([page.extract_text() for page in reader.pages])
    elif filename.endswith(".txt"):
        contents = await file.read()
        text = contents.decode("utf-8")
    else:
        raise HTTPException(status_code=400, detail="Only .docx, .pdf, and .txt files are supported.")

    if not text.strip():
        raise HTTPException(status_code=400, detail="No text found in document.")

    vector = model.encode(text).tolist()
    doc_id = str(uuid.uuid4())
    payload = {"text": text, "source": source, "filename": filename}
    qdrant_client.upsert(
        collection_name=COLLECTION_NAME,
        points=models.Batch(
            ids=[doc_id],
            payloads=[payload],
            vectors=[vector],
        ),
        wait=True,
    )
    return {"status": "success", "id": doc_id, "filename": filename, "text": text}

@app.get("/search")
async def search(q: str):
    """
    Translate the query to English and perform semantic search.
    """
    try:
        translated = (await translator.translate(q, dest="en")).text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error translating query: {e}")

    query_vector = model.encode(translated).tolist()
    try:
        hits = qdrant_client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=1
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
