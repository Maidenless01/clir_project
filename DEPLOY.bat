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
echo                          🚀 Cloud Deployment Setup 🚀
echo     ========================================================================
echo.
echo     Choose your preferred cloud platform:
echo.
echo     1) 🟢 AWS App Runner     (Easiest - Web GUI setup)
echo     2) 🔵 Google Cloud Run   (Most generous free tier)  
echo     3) 🟡 AWS Lambda         (Serverless - pay per use)
echo     4) 📚 View setup guides  (Detailed instructions)
echo     5) ❌ Exit
echo.
set /p choice="     Enter your choice (1-5): "

if "%choice%"=="1" (
    echo.
    echo     🟢 Setting up AWS App Runner...
    echo     ========================================================================
    echo.
    echo     📋 Steps to follow:
    echo     1. Create AWS account: https://aws.amazon.com/free/
    echo     2. Go to App Runner Console (opening now...)
    echo     3. Create Service ^> Source Code Repository
    echo     4. Connect GitHub ^> Select this repository
    echo     5. Click Deploy!
    echo.
    start https://console.aws.amazon.com/apprunner/
    echo     ✅ AWS Console opened in your browser!
    
) else if "%choice%"=="2" (
    echo.
    echo     🔵 Setting up Google Cloud Run...
    echo     ========================================================================
    call setup-gcp.bat
    
) else if "%choice%"=="3" (
    echo.
    echo     🟡 Setting up AWS Lambda...
    echo     ========================================================================
    call setup-aws.bat
    
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
echo     🎉 Thanks for using ITUS Portal deployment setup!
echo     📧 Need help? Check SETUP_GUIDE.md for detailed instructions
echo     ========================================================================
pause