# ITUS Semantic Portal - Google Cloud Deployment Guide

## 🚀 Google Cloud Free Tier Deployment

Deploy your ITUS Semantic Document Portal to Google Cloud with generous free tier limits:
- ✅ **2 million requests/month** free
- ✅ **$300 credit** for new users
- ✅ **Automatic scaling** to zero
- ✅ **Global edge network**

## 🎯 Deployment Options

### Option 1: Google Cloud Run (Recommended)
**Best for:** Most users, generous free tier, automatic scaling

**Free Tier:** 2 million requests/month, 400,000 GB-seconds compute time

**Steps:**
```bash
# Deploy directly from source (easiest)
gcloud run deploy itus-semantic-portal \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 2Gi
```

### Option 2: Google App Engine
**Best for:** Traditional web applications, fully managed

**Free Tier:** 28 instance hours/day for F1 instances

**Steps:**
```bash
gcloud app deploy app.yaml
```

### Option 3: Google Cloud Run + Docker
**Best for:** Advanced users who want container control

**Steps:**
```bash
# Build and push container
gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/itus-portal
gcloud run deploy --image gcr.io/$GOOGLE_CLOUD_PROJECT/itus-portal
```

## 📋 Prerequisites

### Google Cloud Setup
1. Create [Google Cloud Account](https://cloud.google.com/free) - Get $300 credit!
2. Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install-windows)
3. Initialize: `gcloud init`

## 🔧 Configuration Files

- `app.yaml` - Google App Engine configuration
- `cloudrun.yaml` - Google Cloud Run configuration  
- `Dockerfile` - Container configuration
- `deploy-simple.bat` - Easy deployment script

## 🚦 Quick Start (Easiest Method)

### One-Command Deploy:
```bash
# Set your project ID first
gcloud config set project YOUR_PROJECT_ID

# Deploy directly from source (recommended)
gcloud run deploy itus-semantic-portal \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 2Gi \
    --cpu 1
```

### Using Deployment Script:
```bash
# Run the easy deployment script
.\deploy-simple.bat
```

## 💰 Cost Estimation (Free Tier Limits)

| Service | Free Tier Limit | Overage Cost |
|---------|-----------------|--------------|
| Cloud Run | 2M requests/month | $0.40/1M requests |
| App Engine | 28 hours/day | ~$0.05/hour |
| Cloud Build | 120 minutes/day | $0.003/minute |

## 🔐 Environment Variables

Your deployment includes these environment variables:
- `MODEL_NAME`: distiluse-base-multilingual-cased-v1
- `COLLECTION_NAME`: my_multilingual_docs  
- `QDRANT_URL`: Your Qdrant Cloud URL
- `QDRANT_API_KEY`: Your Qdrant API key

## 🚀 Deployment Scripts

Use the provided scripts for easy deployment:
- `.\deploy-simple.bat` - Simple Google Cloud Run deployment
- `.\DEPLOY.bat` - Interactive deployment menu