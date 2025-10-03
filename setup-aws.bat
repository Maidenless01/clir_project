@echo off
echo 🚀 ITUS Portal - AWS Setup
echo ==========================

echo Step 1: Install AWS CLI
echo Download from: https://aws.amazon.com/cli/
echo After installation, run: aws configure
pause

echo Step 2: Install AWS SAM CLI (for Lambda option)
echo Download from: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-windows.html
pause

echo Step 3: Choose deployment option:
echo 1) AWS App Runner (Easiest - use web console)
echo 2) AWS Lambda (Serverless)
echo 3) AWS Elastic Beanstalk

set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo Opening AWS App Runner Console...
    start https://console.aws.amazon.com/apprunner/
    echo Follow the GUI steps in the browser
) else if "%choice%"=="2" (
    echo Deploying to AWS Lambda...
    sam build
    sam deploy --guided
) else if "%choice%"=="3" (
    echo Installing Elastic Beanstalk CLI...
    pip install awsebcli
    eb init
    eb create itus-portal
    eb deploy
)

pause