@echo off
echo 🚀 Simple Google Cloud Deploy
echo ==============================

echo Step 1: Login to Google Cloud
gcloud auth login

echo Step 2: Set project (replace YOUR_PROJECT_ID with your actual project ID)
set /p PROJECT_ID="Enter your Google Cloud Project ID: "
gcloud config set project %PROJECT_ID%

echo Step 3: Enable required services
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com

echo Step 4: Deploy your app
gcloud run deploy itus-semantic-portal ^
    --source . ^
    --platform managed ^
    --region us-central1 ^
    --allow-unauthenticated ^
    --memory 2Gi ^
    --cpu 1

echo ✅ Done! Your app is live!
pause