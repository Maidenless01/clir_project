# Qdrant Setup Guide for ITUS Semantic Portal

## Option 1: Qdrant Cloud (Recommended - FREE)

### Step-by-Step Setup:

1. **Create Qdrant Cloud Account**
   - Visit [cloud.qdrant.io](https://cloud.qdrant.io/)
   - Sign up with GitHub/Google
   - Verify email address

2. **Create Free Cluster**
   - Click **"Create Cluster"**
   - Choose **"Free Tier"**:
     - 1GB storage
     - 100k vectors
     - No credit card required
   - Select region (closest to your users)
   - Cluster name: `itus-documents`

3. **Get Cluster URL**
   After cluster creation (2-3 minutes), copy the URL:
   ```
   https://abc123-def456.us-east4-0.gcp.cloud.qdrant.io:6333
   ```

4. **Update render.yaml**
   Replace `YOUR-CLUSTER-ID` in render.yaml with your actual cluster ID.

5. **Deploy to Render**
   - Push changes to GitHub
   - Render will auto-deploy with Qdrant Cloud connection

---

## Option 2: Railway Qdrant (Alternative FREE)

### Quick Railway Deploy:

1. **One-Click Deploy**
   - Visit: https://railway.app/template/qdrant
   - Click **"Deploy Now"**
   - Connect GitHub account
   - Deploy completes in 2-3 minutes

2. **Get Railway Qdrant URL**
   ```
   https://your-app-name.railway.app:6333
   ```

3. **Update Environment Variables**
   In Render dashboard, set:
   ```
   QDRANT_URL=https://your-app-name.railway.app:6333
   ```

---

## Option 3: Render Qdrant Service (Manual)

### Deploy Qdrant on Render:

1. **Create Web Service on Render**
   - Repository: `qdrant/qdrant`
   - Docker deployment
   - Port: 6333

2. **Service Configuration**
   ```yaml
   services:
     - type: web
       name: itus-qdrant
       env: docker
       dockerfilePath: ./Dockerfile
       plan: free
       envVars:
         - key: QDRANT__SERVICE__HTTP_PORT
           value: 6333
       autoDeploy: false
   ```

3. **Get Internal URL**
   ```
   QDRANT_URL=https://itus-qdrant.onrender.com:6333
   ```

---

## Testing Your Setup

### Verify Connection:

1. **Check Qdrant Health**
   ```bash
   curl https://your-qdrant-url/
   ```

2. **Test App Health**
   ```bash
   curl https://your-app.onrender.com/health
   ```

3. **Expected Response**
   ```json
   {
     "status": "ok",
     "qdrant_server_version": "1.15.1",
     "qdrant_client_version": "1.15.1",
     "model_name": "distiluse-base-multilingual-cased-v1",
     "collection_name": "my_multilingual_docs",
     "qdrant_endpoint": "https://your-cluster.qdrant.io:6333"
   }
   ```

---

## Troubleshooting

### Common Issues:

1. **Connection Refused**
   - Verify Qdrant URL includes `:6333` port
   - Check firewall/security settings
   - Ensure HTTPS for cloud instances

2. **Version Mismatch**
   - Check Qdrant Cloud version matches client
   - Update `requirements.txt` if needed

3. **Collection Not Found**
   - App auto-creates collection on first startup
   - Check logs for initialization errors

### Debug Commands:

```bash
# Test Qdrant directly
curl -X GET "https://your-qdrant-url/collections"

# Check app logs
# In Render dashboard → Logs tab
```

---

## Cost Comparison

| Service | Storage | Vectors | Cost |
|---------|---------|---------|------|
| Qdrant Cloud Free | 1GB | 100k | $0 |
| Railway Free | 1GB | ~100k | $0 |
| Render Free | 512MB | ~50k | $0 |

**Recommendation**: Start with **Qdrant Cloud** for best performance and reliability.