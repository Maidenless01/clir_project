# 🎓 ITUS Semantic Document Portal

**Intelligent Document Search & Analysis System**

[![Deploy to Google Cloud](https://img.shields.io/badge/Deploy%20to-Google%20Cloud-4285F4?logo=googlecloud)](https://console.cloud.google.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![Qdrant](https://img.shields.io/badge/Qdrant-Vector%20DB-red)](https://qdrant.tech)

## 🚀 Quick Deploy to Google Cloud

### One-Click Deploy:
```bash
.\deploy-simple.bat
```

### Manual Deploy:
```bash
gcloud run deploy itus-semantic-portal \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 2Gi
```

## ✨ Features

- 🔍 **Semantic Search** - Find documents by meaning, not just keywords  
- 🌍 **Multilingual Support** - Works with multiple languages
- 📄 **Document Processing** - PDF, DOCX, TXT file support
- 🎨 **Modern UI** - Clean, institutional design
- ☁️ **Cloud-Ready** - Deploy to Google Cloud with generous free tier
- 🔄 **Auto-Scaling** - Scales to zero when not in use

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

## 📋 Prerequisites

1. **Google Cloud Account** - [Sign up for free](https://cloud.google.com/free) ($300 credit!)
2. **Google Cloud SDK** - [Install here](https://cloud.google.com/sdk/docs/install-windows)
3. **Qdrant Cloud** - Vector database (configured ✅)

## 🎯 Deployment Options

| Method | Difficulty | Best For |
|--------|------------|----------|
| **Cloud Run** | 🟡 Medium | Most users (2M requests/month free) |
| **App Engine** | 🟢 Easy | Traditional apps (28 hours/day free) |

## 💰 Free Tier Limits

- **Google Cloud Run**: 2 million requests/month
- **Google App Engine**: 28 instance hours/day  
- **Qdrant Cloud**: 1GB storage free

## 📚 Documentation

- **[Setup Guide](SETUP_GUIDE.md)** - Step-by-step deployment instructions
- **[Cloud Deployment](CLOUD_DEPLOYMENT.md)** - Detailed Google Cloud configuration
- **[Qdrant Setup](QDRANT_SETUP.md)** - Vector database configuration

## 🆘 Support

Run into issues? Check our guides:
1. Run `.\DEPLOY.bat` for interactive setup
2. Read `SETUP_GUIDE.md` for troubleshooting
3. Check `CLOUD_DEPLOYMENT.md` for advanced configuration

## 📁 Project Structure

```
.
├── app.py                  # Main FastAPI application
├── app.yaml               # Google App Engine configuration
├── cloudrun.yaml          # Google Cloud Run configuration  
├── Dockerfile             # Container configuration
├── build.sh               # Build script
├── deploy-simple.bat      # Easy deployment script
├── DEPLOY.bat             # Interactive deployment menu
├── docker-compose.yml     # Local development with Qdrant
├── index.html             # Frontend web interface
├── index_data.py          # Sample data indexing script
├── requirements.txt       # Python dependencies
├── static/                # CSS and static assets
├── qdrant_storage/        # Local Qdrant data (development only)
└── uploads/               # Uploaded files directory
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