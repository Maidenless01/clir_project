# ITUS Semantic Portal - Complete Setup Guide

## 🎯 Choose Your Platform

### Option A: AWS App Runner (Recommended for Beginners)
**Why choose this:**
- ✅ Easiest setup (just click buttons)
- ✅ 5,000 compute minutes/month free
- ✅ Auto-scales to zero cost
- ✅ Direct GitHub integration

**Setup Steps:**
1. **Create AWS Account**: [aws.amazon.com/free](https://aws.amazon.com/free/)
2. **Go to App Runner**: [console.aws.amazon.com/apprunner](https://console.aws.amazon.com/apprunner/)
3. **Create Service**:
   - Source: "Source code repository"
   - Repository: Connect GitHub → Select `clir_project`
   - Branch: `main`
   - Configuration file: `apprunner.yaml` (auto-detected)
4. **Click Deploy** - Done! 🎉

### Option B: Google Cloud Run (Most Generous Free Tier)
**Why choose this:**
- ✅ 2 million requests/month free
- ✅ $300 credit for new users
- ✅ Better for high traffic
- ✅ Container-based (more flexible)

**Setup Steps:**
1. **Create Google Account**: [cloud.google.com/free](https://cloud.google.com/free)
2. **Install Google Cloud SDK**: 
   - Download: [cloud.google.com/sdk](https://cloud.google.com/sdk)
   - Run installer, follow prompts
3. **Run Setup Script**: Double-click `setup-gcp.bat`
4. **Follow prompts** - Done! 🎉

---

## 🚀 Quick Start Commands

### For Google Cloud (Recommended):
```bash
# 1. Login and setup
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# 2. Enable services
gcloud services enable cloudbuild.googleapis.com run.googleapis.com

# 3. Deploy (one command!)
gcloud run deploy itus-semantic-portal \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 2Gi
```

### For AWS Lambda (Serverless):
```bash
# 1. Install SAM CLI
# Download: https://docs.aws.amazon.com/serverless-application-model/

# 2. Configure AWS
aws configure

# 3. Deploy
sam build
sam deploy --guided
```

---

## 🔧 Prerequisites Checklist

### General:
- [ ] GitHub account (you have this ✅)
- [ ] Your code is pushed to GitHub (you have this ✅)

### For AWS:
- [ ] AWS Account ([Sign up](https://aws.amazon.com/free/))
- [ ] Credit card (for account verification, won't charge)

### For Google Cloud:
- [ ] Google Account
- [ ] Google Cloud SDK installed
- [ ] Project created in Google Cloud Console

---

## 💡 Which Should You Choose?

| Feature | AWS App Runner | Google Cloud Run |
|---------|---------------|------------------|
| **Setup Difficulty** | 🟢 Easiest (GUI) | 🟡 Medium (CLI) |
| **Free Tier** | 5,000 minutes/month | 2M requests/month |
| **Scaling** | Auto (to zero) | Auto (to zero) |
| **Best For** | Beginners | Developers |

---

## 🆘 Need Help?

### Common Issues:
1. **"Command not found"** → Install the CLI tools first
2. **"Permission denied"** → Run `gcloud auth login` or `aws configure`
3. **"Project not found"** → Create project in cloud console first

### Getting Started Right Now:
1. **Easiest**: Use AWS App Runner (just web interface)
2. **Most free**: Google Cloud Run (use `setup-gcp.bat`)
3. **Most flexible**: AWS Lambda (use `setup-aws.bat`)

---

## 🎉 After Deployment

Your app will be available at:
- **AWS App Runner**: `https://xxxxxxx.us-east-1.awsapprunner.com`
- **Google Cloud Run**: `https://itus-semantic-portal-xxxxxxx-uc.a.run.app`
- **AWS Lambda**: `https://xxxxxxx.execute-api.region.amazonaws.com/Prod/`

Test it by visiting `/health` endpoint first!