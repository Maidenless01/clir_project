#!/bin/bash
# Google Cloud Deployment Script

echo "🚀 ITUS Portal - Google Cloud Deployment Options"
echo "================================================"

echo "Choose deployment option:"
echo "1) Google Cloud Run (Recommended)"
echo "2) Google App Engine"
echo "3) Google Kubernetes Engine (GKE)"

read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo "📦 Deploying to Cloud Run..."
        # Build and deploy
        gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/itus-portal
        gcloud run deploy itus-semantic-portal \
            --image gcr.io/$GOOGLE_CLOUD_PROJECT/itus-portal \
            --platform managed \
            --region us-central1 \
            --memory 2Gi \
            --cpu 1 \
            --allow-unauthenticated
        ;;
    2)
        echo "📦 Deploying to App Engine..."
        gcloud app deploy app.yaml
        ;;
    3)
        echo "📦 Deploying to GKE..."
        echo "1. Create GKE cluster"
        gcloud container clusters create itus-cluster --num-nodes=1
        echo "2. Build and push image"
        docker build -t gcr.io/$GOOGLE_CLOUD_PROJECT/itus-portal .
        docker push gcr.io/$GOOGLE_CLOUD_PROJECT/itus-portal
        echo "3. Deploy with kubectl"
        kubectl apply -f cloudrun.yaml
        ;;
esac