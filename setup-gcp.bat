@echo off
echo 🚀 ITUS Portal - Google Cloud Setup
echo ===================================

echo Step 1: Login to Google Cloud
gcloud auth login

echo Step 2: Set your project
set /p PROJECT_ID="Enter your Google Cloud Project ID: "
gcloud config set project %PROJECT_ID%

echo Step 3: Enable required APIs
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com

echo Step 4: Deploy to Cloud Run
gcloud run deploy itus-semantic-portal --source . --platform managed --region us-central1 --allow-unauthenticated --memory 2Gi --cpu 1

echo ✅ Deployment complete!
echo Your app will be available at the URL shown above.
pause