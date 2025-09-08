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

6.  **Access the application:**

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

## Project Structure

```
.
├── app.py                  # The main FastAPI application logic
├── docker-compose.yml      # Docker Compose configuration for the Qdrant service
├── index.html              # The frontend web interface
├── index_data.py           # Script to index initial sample data
├── requirements.txt        # Python dependencies
├── qdrant_storage/         # Directory where Qdrant persists its data
└── uploads/                # Directory where uploaded files are stored
```
