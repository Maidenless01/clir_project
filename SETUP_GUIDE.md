# ITUS Semantic Portal - Google Cloud Setup Guide

## 🎯 Google Cloud Deployment (Best Free Tier!)

### Why Choose Google Cloud:
- ✅ **2 million requests/month** free (most generous!)
- ✅ **$300 credit** for new users  
- ✅ **Automatic scaling** to zero cost
- ✅ **Container-based** (more flexible)
- ✅ **Global edge network**

## 🚀 Easy Setup Methods

### Method 1: One-Click Deploy (Recommended)
```bash
# Just run this command!
.\deploy-simple.bat
```

### Method 2: Manual Deploy  
```bash
# 1. Login and setup
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# 2. Deploy (one command!)
gcloud run deploy itus-semantic-portal \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 2Gi
```

### Method 3: Interactive Menu
```bash
# Choose your deployment option
.\DEPLOY.bat
```

---

## 🔧 Prerequisites Checklist

### Required:
- [ ] Google Account (free to create)
- [ ] Google Cloud SDK installed
- [ ] Project created in Google Cloud Console

### Setup Steps:
1. **Create Google Cloud Account**: [cloud.google.com/free](https://cloud.google.com/free)
2. **Install Google Cloud SDK**: [cloud.google.com/sdk/docs/install-windows](https://cloud.google.com/sdk/docs/install-windows)
3. **Create Project**: Go to [console.cloud.google.com](https://console.cloud.google.com)

---

## 💡 Deployment Options Comparison

| Method | Difficulty | Free Tier | Best For |
|--------|------------|-----------|----------|
| **Cloud Run** | 🟡 Medium | 2M requests/month | Most users |
| **App Engine** | 🟢 Easy | 28 hours/day | Traditional apps |
| **Docker + Cloud Run** | 🔴 Advanced | 2M requests/month | Power users |

---

## 🆘 Troubleshooting

### Common Issues:
1. **"gcloud not found"** → Install Google Cloud SDK first
2. **"Permission denied"** → Run `gcloud auth login`
3. **"Project not found"** → Create project in Google Cloud Console first

### Quick Fixes:
```bash
# Fix authentication
gcloud auth login

# Set correct project
gcloud config set project YOUR_PROJECT_ID

# Enable required services
gcloud services enable cloudbuild.googleapis.com run.googleapis.com
```

---

## 🎉 After Deployment

Your app will be available at:
- **Google Cloud Run**: `https://itus-semantic-portal-xxxxxxx-uc.a.run.app`

### Test Your Deployment:
1. Visit `/health` endpoint first
2. Try the main app interface  
3. Upload a test document
4. Perform a search query

### Success Checklist:
- [ ] Health check responds with "healthy"
- [ ] Main interface loads
- [ ] File upload works
- [ ] Search returns results
- [ ] Qdrant connection active