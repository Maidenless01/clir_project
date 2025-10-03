@echo off
cls
echo.
echo     ██╗████████╗██╗   ██╗███████╗    ██████╗  ██████╗ ██████╗ ████████╗ █████╗ ██╗     
echo     ██║╚══██╔══╝██║   ██║██╔════╝    ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     
echo     ██║   ██║   ██║   ██║███████╗    ██████╔╝██║   ██║██████╔╝   ██║   ███████║██║     
echo     ██║   ██║   ██║   ██║╚════██║    ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══██║██║     
echo     ██║   ██║   ╚██████╔╝███████║    ██║     ╚██████╔╝██║  ██║   ██║   ██║  ██║███████╗
echo     ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
echo.
echo                    🚀 Google Cloud Deployment Setup 🚀
echo     ========================================================================
echo.
echo     Choose your deployment option:
echo.
echo     1) � Google Cloud Run      (Recommended - Most generous free tier)
echo     2) � Google App Engine     (Fully managed platform)
echo     3) � Google Cloud Run + Docker (Advanced)
echo     4) 📚 View setup guides     (Detailed instructions)
echo     5) ❌ Exit
echo.
set /p choice="     Enter your choice (1-5): "

if "%choice%"=="1" (
    echo.
    echo     � Setting up Google Cloud Run...
    echo     ========================================================================
    call deploy-simple.bat
    
) else if "%choice%"=="2" (
    echo.
    echo     🟦 Setting up Google App Engine...
    echo     ========================================================================
    echo.
    echo     📋 Steps to follow:
    echo     1. Install Google Cloud SDK: https://cloud.google.com/sdk
    echo     2. Login: gcloud auth login
    echo     3. Set project: gcloud config set project YOUR_PROJECT_ID
    echo     4. Deploy: gcloud app deploy app.yaml
    echo.
    pause
    
) else if "%choice%"=="3" (
    echo.
    echo     � Setting up Google Cloud Run with Docker...
    echo     ========================================================================
    echo.
    echo     📋 Steps to follow:
    echo     1. Build: docker build -t gcr.io/PROJECT_ID/itus-portal .
    echo     2. Push: docker push gcr.io/PROJECT_ID/itus-portal
    echo     3. Deploy: gcloud run deploy --image gcr.io/PROJECT_ID/itus-portal
    echo.
    pause
    
) else if "%choice%"=="4" (
    echo.
    echo     📚 Opening setup guides...
    echo     ========================================================================
    start SETUP_GUIDE.md
    start CLOUD_DEPLOYMENT.md
    
) else if "%choice%"=="5" (
    echo.
    echo     👋 Goodbye! Come back when you're ready to deploy!
    exit /b
    
) else (
    echo.
    echo     ❌ Invalid choice. Please run the script again.
)

echo.
echo     ========================================================================
echo     🎉 Thanks for using ITUS Portal Google Cloud deployment!
echo     📧 Need help? Check SETUP_GUIDE.md for detailed instructions
echo     ========================================================================
pause