# Semantic Cross-Lingual Document Search

This project is a powerful semantic search engine that allows you to search for documents using queries in any language. It leverages a multilingual sentence embedding model to understand the meaning behind your words, providing highly relevant results even if the query language doesn't match the document language.

## Features

-   **Cross-Lingual Search:** Search your documents using queries in various languages (e.g., French, Spanish, German) and get relevant results from your English document base.
-   **File Upload:** Easily upload and index documents in various formats (`.docx`, `.pdf`, `.txt`).
-   **Semantic Understanding:** Goes beyond keyword matching to find documents that are contextually related to your query.
-   **Simple Web Interface:** A clean and straightforward UI for uploading files and searching.
-   **Dockerized:** The entire application stack (including the Qdrant vector database) is containerized for easy setup and deployment.

## Tech Stack

-   **Backend:** Python with FastAPI
-   **Vector Database:** Qdrant
-   **ML Model:** `distiluse-base-multilingual-cased-v1` from Sentence-Transformers
-   **Translation:** Google Translate API via `googletrans-py`
-   **Containerization:** Docker & Docker Compose
-   **Frontend:** Plain HTML, CSS, and JavaScript

## Getting Started

### Prerequisites

-   Docker and Docker Compose installed on your machine.
-   Python 3.7+ (for running the indexing script locally if needed).

### Installation & Running the App

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd clir_project
    ```

2.  **Start the services:**

    This command will start the Qdrant vector database in a Docker container.

    ```bash
    docker-compose up -d
    ```

3.  **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Indexing Script (Optional):**

    The `index_data.py` script populates the database with a few sample documents. You can run it to have some data to start with.

    ```bash
    python index_data.py
    ```

5.  **Start the FastAPI application:**

    ```bash
    uvicorn app:app --reload
    ```
    or
    ```bash
    python -m uvicorn app:app --reload
    ```

7.  **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

1.  **Upload Documents:**
    -   Click the "Choose File" button.
    -   Select a `.docx`, `.pdf`, or `.txt` file.
    -   Click "Upload".
    -   The file content will be indexed, and a confirmation will be displayed.

2.  **Search Documents:**
    -   Type your search query in the search box. You can use any language.
    -   Click "Search".
    -   The top matching documents will be displayed, along with a snippet of their content and a link to the original file.

## Deployment on Render

This project is configured for easy deployment on [Render](https://render.com/). 

### Quick Deploy

1. **Fork/Clone this repository** to your GitHub account
2. **Set up Qdrant Cloud** (recommended) or external Qdrant instance:
   - Sign up at [Qdrant Cloud](https://cloud.qdrant.io/)
   - Create a cluster and get your connection URL
3. **Deploy to Render**:
   - Connect your GitHub repo to Render
   - Use the included `render.yaml` configuration
   - Set environment variables (see below)

### Environment Variables for Render

Set these in your Render service dashboard:

```
MODEL_NAME=distiluse-base-multilingual-cased-v1
COLLECTION_NAME=my_multilingual_docs
QDRANT_URL=https://your-cluster-id.europe-west3-0.gcp.cloud.qdrant.io:6333
# OR if using self-hosted Qdrant:
QDRANT_HOST=your-qdrant-host
QDRANT_PORT=6333
```

### Manual Render Setup

If not using `render.yaml`, create a new Web Service with:
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn app:app --host 0.0.0.0 --port $PORT --worker-class uvicorn.workers.UvicornWorker`
- **Environment**: Python 3.11

### Qdrant Setup Options

**Option 1: Qdrant Cloud (Recommended for production)**
- Sign up at [cloud.qdrant.io](https://cloud.qdrant.io/)
- Create a cluster
- Set `QDRANT_URL` to your cluster URL

**Option 2: Self-hosted Qdrant**
- Deploy Qdrant on another service (Railway, DigitalOcean, etc.)
- Set `QDRANT_HOST` and `QDRANT_PORT`

## Project Structure

```
.
├── app.py                  # The main FastAPI application logic
├── build.sh               # Render build script
├── render.yaml            # Render service configuration
├── docker-compose.yml      # Docker Compose configuration for the Qdrant service
├── index.html              # The frontend web interface
├── index_data.py           # Script to index initial sample data
├── requirements.txt        # Python dependencies
├── static/                 # CSS and static assets
├── qdrant_storage/         # Directory where Qdrant persists its data (local only)
└── uploads/                # Directory where uploaded files are stored
```

## Troubleshooting

### Corrupted Qdrant Data

If you encounter errors related to Qdrant data corruption, you can reset the Qdrant storage and re-index your data.

1.  **Stop the Docker containers:**

    ```bash
    docker-compose down
    ```

2.  **Delete the Qdrant storage directory:**

    ```bash
    rm -rf qdrant_storage
    ```

3.  **Restart the services:**

    ```bash
    docker-compose up -d
    ```

4.  **Re-index your data:**

    If you have an indexing script, run it again. For example:

    ```bash
    python index_data.py
    ```

    You will also need to re-upload any files you had previously indexed.