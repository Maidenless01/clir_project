# ITUS Semantic Portal - Cloud Deployment Guide

## 🚀 Free Tier Cloud Deployment Options

### AWS Free Tier Options

#### Option 1: AWS App Runner (Recommended for beginners)
- ✅ **Free Tier**: 2,000 build minutes/month + 5,000 compute minutes/month
- ✅ **Auto-scaling**: Scales to zero when not used
- ✅ **Easy setup**: Direct GitHub integration

**Steps:**
1. Go to [AWS App Runner Console](https://console.aws.amazon.com/apprunner/)
2. Create service → Source: GitHub
3. Select your repository
4. Use `apprunner.yaml` configuration
5. Deploy automatically

#### Option 2: AWS Elastic Beanstalk
- ✅ **Free Tier**: t3.micro instance included
- ✅ **Managed**: Automatic scaling and health monitoring

**Steps:**
```bash
pip install awsebcli
eb init
eb create itus-portal
eb deploy
```

#### Option 3: AWS Lambda + API Gateway (Serverless)
- ✅ **Free Tier**: 1M requests/month + 400,000 GB-seconds compute
- ✅ **Serverless**: Pay only for actual usage

**Steps:**
```bash
pip install aws-sam-cli
sam build
sam deploy --guided
```

### Google Cloud Free Tier Options

#### Option 1: Google Cloud Run (Recommended)
- ✅ **Free Tier**: 2 million requests/month
- ✅ **Containerized**: Scales to zero
- ✅ **Fast deployment**: Direct from source

**Steps:**
```bash
gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/itus-portal
gcloud run deploy itus-semantic-portal \
    --image gcr.io/$GOOGLE_CLOUD_PROJECT/itus-portal \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
```

#### Option 2: Google App Engine
- ✅ **Free Tier**: 28 instance hours/day
- ✅ **Managed**: Automatic scaling

**Steps:**
```bash
gcloud app deploy app.yaml
```

## 📋 Prerequisites

### AWS Setup
1. Create [AWS Account](https://aws.amazon.com/free/)
2. Install [AWS CLI](https://aws.amazon.com/cli/)
3. Configure credentials: `aws configure`

### Google Cloud Setup
1. Create [Google Cloud Account](https://cloud.google.com/free)
2. Install [Google Cloud SDK](https://cloud.google.com/sdk)
3. Initialize: `gcloud init`

## 🔧 Configuration Files

- `apprunner.yaml` - AWS App Runner configuration
- `template.yaml` - AWS SAM/Lambda configuration
- `app.yaml` - Google App Engine configuration
- `cloudrun.yaml` - Google Cloud Run configuration
- `Dockerfile` - Container configuration for all platforms

## 🚦 Quick Start

### For AWS (App Runner - Easiest):
1. Push your code to GitHub
2. Go to AWS App Runner Console
3. Create service from your GitHub repo
4. Use the `apprunner.yaml` config
5. Deploy!

### For Google Cloud (Cloud Run - Recommended):
```bash
# Set your project ID
export GOOGLE_CLOUD_PROJECT=your-project-id

# Deploy directly from source
gcloud run deploy itus-semantic-portal \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
```

## 💰 Cost Estimation (Free Tier Limits)

| Platform | Service | Free Tier Limit | Overage Cost |
|----------|---------|-----------------|--------------|
| AWS | App Runner | 5,000 compute min/month | ~$0.06/hour |
| AWS | Lambda | 1M requests/month | $0.20/1M requests |
| AWS | Elastic Beanstalk | t3.micro included | ~$8.5/month (t3.small) |
| GCP | Cloud Run | 2M requests/month | $0.40/1M requests |
| GCP | App Engine | 28 hours/day | ~$0.05/hour |

## 🔐 Environment Variables

All configurations include these environment variables:
- `MODEL_NAME`: Sentence transformer model
- `COLLECTION_NAME`: Qdrant collection name  
- `QDRANT_URL`: Your Qdrant Cloud URL
- `QDRANT_API_KEY`: Your Qdrant API key

## 🚀 Deployment Scripts

Use the provided scripts for easy deployment:
- `./deploy-aws.sh` - Interactive AWS deployment
- `./deploy-gcp.sh` - Interactive Google Cloud deployment