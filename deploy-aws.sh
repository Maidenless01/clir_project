#!/bin/bash
# AWS Deployment Script

echo "🚀 ITUS Portal - AWS Deployment Options"
echo "========================================"

echo "Choose deployment option:"
echo "1) AWS App Runner (Recommended for beginners)"
echo "2) AWS Elastic Beanstalk"
echo "3) AWS Lambda + API Gateway (Serverless)"
echo "4) AWS ECS with Fargate"

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo "📦 Deploying to AWS App Runner..."
        echo "1. Go to AWS Console → App Runner"
        echo "2. Create service from GitHub repository"
        echo "3. Use apprunner.yaml configuration"
        echo "4. Service will auto-deploy from GitHub"
        ;;
    2)
        echo "📦 Deploying to Elastic Beanstalk..."
        pip install awsebcli
        eb init
        eb create itus-portal
        eb deploy
        ;;
    3)
        echo "📦 Deploying to AWS Lambda..."
        pip install aws-sam-cli
        sam build
        sam deploy --guided
        ;;
    4)
        echo "📦 Deploying to AWS ECS..."
        echo "1. Build Docker image"
        docker build -t itus-portal .
        echo "2. Push to ECR and deploy via ECS"
        ;;
esac