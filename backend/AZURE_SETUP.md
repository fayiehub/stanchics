# Stanchics — Azure Setup & Deployment Guide

## Overview

| Component | Azure Service | Tier |
|---|---|---|
| Python API (FastAPI) | Azure App Service | Free F1 |
| Database | Azure SQL Database | Free 32GB |
| Frontend (HTML) | Azure Static Web Apps | Free |

Total monthly cost at these tiers: **$0**

---

## Prerequisites

Install these on your local machine before starting:

1. **Azure CLI** — https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
2. **Python 3.11+** — https://www.python.org/downloads/
3. **Git** — https://git-scm.com/downloads

Verify installs:
```bash
az --version
python --version
git --version
```

---

## Step 1 — Create an Azure Account & Log In

1. Go to https://azure.microsoft.com/free and create a free account (requires a credit card for verification, but you won't be charged on free tiers).
2. Log in from your terminal:

```bash
az login
```

A browser window will open. Sign in with your Azure account. Once done, your terminal will show your subscription details.

---

## Step 2 — Create a Resource Group

A resource group is a logical container for all your Stanchics Azure resources.

```bash
az group create \
  --name stanchics_group \
  --location westeurope
```

> You can use `eastus` or `westeurope` — both have free tier availability. Stick with one for the whole project.

---

## Step 3 — Create the Azure SQL Database

### 3a. Create the SQL Server

```bash
az sql server create \
  --name stanchics-sql-server \
  --resource-group stanchics_group \
  --location westeurope \
  --admin-user adminusername \
  --admin-password "<insert-strong-password>"
``` 

> **Save the password.** You'll need it for your `.env` file.

### 3b. Create the Database (free tier)

```bash
az sql db create \
  --resource-group stanchics_group \
  --server stanchics-sql-server \
  --name stanchics \
  --edition GeneralPurpose \
  --family Gen5 \
  --capacity 2 \
  --compute-model Serverless \
  --auto-pause-delay 60 \
  --use-free-limit \
  --free-limit-exhaustion-behavior AutoPause
```

> `--use-free-limit` enables the free 32GB tier. `AutoPause` pauses the DB when idle so you stay within the free limit.

### 3c. Allow your IP to connect (for local development)

```bash
# Get your public IP
MY_IP=$(curl -s https://api.ipify.org)

az sql server firewall-rule create \
  --resource-group stanchics_group \
  --server stanchics-sql-server \
  --name AllowMyIP \
  --start-ip-address $MY_IP \
  --end-ip-address $MY_IP
```

### 3d. Allow Azure services to connect (required for App Service)

```bash
az sql server firewall-rule create \
  --resource-group stanchics_group \
  --server stanchics-sql-server \
  --name AllowAzureServices \
  --start-ip-address 0.0.0.0 \
  --end-ip-address 0.0.0.0
```

### 3e. Get your connection string

```bash
az sql db show-connection-string \
  --server stanchics-sql-server \
  --name stanchics \
  --client odbc
```

Copy the output and replace `<username>` and `<password>` with your actual credentials. It will look like:

```
Driver={ODBC Driver 17 for SQL Server};Server=tcp:stanchics-sql-server.database.windows.net,1433;Database=stanchics;Uid=stanchicsadmin;Pwd=YourStr0ngP@ssword!;Encrypt=yes;TrustServerCertificate=no;
```

For SQLAlchemy (used in the Python app), format it as:
```
mssql+pyodbc://stanchicsadmin:YourStr0ngP@ssword!@stanchics-sql-server.database.windows.net/stanchics?driver=ODBC+Driver+17+for+SQL+Server
```

---

## Step 4 — Set Up the Python API Locally

### 4a. Install ODBC Driver (required for Azure SQL)

**macOS:**
```bash
brew install msodbcsql17
```

**Ubuntu/Debian:**
```bash
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql17
```

**Windows:** Download from https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server

### 4b. Set up the project

```bash
cd stanchics-api

# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
source venv/Scripts/activate  # git bash on windows

# Install dependencies
pip install -r requirements.txt
```

### 4c. Configure environment variables

```bash
# Copy the example file
cp .env.example .env

# Open .env and fill in:
# - DATABASE_URL  (from Step 3e)
# - MAILCHIMP_API_KEY (optional — skip for now)
# - MAILCHIMP_LIST_ID (optional — skip for now)
# - ALLOWED_ORIGINS (your frontend URL, e.g. http://localhost:5500)
```

### 4d. Run locally

```bash
uvicorn app.main:app --reload --port 8000
```

Visit:
- API root: http://localhost:8000
- Swagger docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

The first run will automatically create the three database tables (`members`, `contact_submissions`, `newsletter_subscribers`).

---

## Step 5 — Deploy the API to Azure App Service

### 5a. Create the App Service Plan (free tier)

```bash
az appservice plan create \
  --name stanchics-plan \
  --resource-group stanchics_group \
  --sku F1 \
  --is-linux
```

### 5b. Create the Web App

```bash
az webapp create \
  --name stanchics-api \
  --resource-group stanchics_group \
  --plan stanchics-plan \
  --runtime "PYTHON:3.11"
```

Your API will be available at: `https://stanchics-api.azurewebsites.net`

### 5c. Set environment variables on Azure

```bash
az webapp config appsettings set \
  --name stanchics-api \
  --resource-group stanchics_group \
  --settings \
    DATABASE_URL="mssql+pyodbc://stanchicsadmin:YourStr0ngP@ssword!@stanchics-sql-server.database.windows.net/stanchics?driver=ODBC+Driver+17+for+SQL+Server" \
    MAILCHIMP_API_KEY="your-key" \
    MAILCHIMP_LIST_ID="your-list-id" \
    MAILCHIMP_DC="us21" \
    ALLOWED_ORIGINS="https://YOUR-FRONTEND-URL.azurestaticapps.net" \
    APP_ENV="production" \
    SECRET_KEY="generate-a-long-random-string-here"
```

> Generate a secret key: `python -c "import secrets; print(secrets.token_hex(32))"`

### 5d. Set the startup command

```bash
az webapp config set \
  --name stanchics-api \
  --resource-group stanchics_group \
  --startup-file "uvicorn app.main:app --host 0.0.0.0 --port 8000"
```

### 5e. Deploy via Git (simplest method)

```bash
# Initialise git in your project (if not already)
git init
git add .
git commit -m "Initial Stanchics API"

# Add Azure as a remote
az webapp deployment source config-local-git \
  --name stanchics-api \
  --resource-group stanchics_group

# The command above prints a Git URL — use it:
git remote add azure https://stanchics-api.scm.azurewebsites.net/stanchics-api.git

# Push to deploy
git push azure main
```

### 5f. Verify deployment

```bash
# Stream live logs
az webapp log tail \
  --name stanchics-api \
  --resource-group stanchics_group
```

Visit https://stanchics-api.azurewebsites.net/health — it should return `{"status": "ok"}`.

---

## Step 6 — Deploy the Frontend (HTML) to Azure Static Web Apps

### 6a. Create a Static Web App

```bash
az staticwebapp create \
  --name stanchics-frontend \
  --resource-group stanchics_group \
  --location westeurope \
  --sku Free
```

### 6b. Deploy your HTML file

The easiest way to upload a single `index.html` is via the Azure Portal:

1. Go to https://portal.azure.com
2. Search for "stanchics-frontend" → your Static Web App
3. Click **"Browse"** to open the deployment centre
4. Or use the Azure Static Web Apps CLI:

```bash
npm install -g @azure/static-web-apps-cli

swa deploy ./  \
  --app-name stanchics-frontend \
  --resource-group stanchics_group \
  --env production
```

Your frontend URL will be something like: `https://stanchics-frontend.azurestaticapps.net`

### 6c. Update CORS on your API

Go back and update the `ALLOWED_ORIGINS` setting to include your real frontend URL:

```bash
az webapp config appsettings set \
  --name stanchics-api \
  --resource-group stanchics_group \
  --settings ALLOWED_ORIGINS="https://stanchics-frontend.azurestaticapps.net"
```

---

## Step 7 — Wire the Frontend to the API

In `index.html`, find the `// TODO` comments in the JavaScript section and replace them:

```javascript
// Replace this pattern:
// TODO: POST to /api/newsletter { email }

// With:
const API_BASE = "https://stanchics-api.azurewebsites.net";

async function postToAPI(endpoint, data) {
  const res = await fetch(`${API_BASE}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "Something went wrong.");
  }
  return res.json();
}

// Newsletter signup:
await postToAPI("/api/newsletter", { email, source: "home_hero" });

// Join form:
await postToAPI("/api/members", { full_name, email, job_title, company, linkedin_url, why_joining });

// Contact form:
await postToAPI("/api/contact", { full_name, email, subject, message });
```

---

## Step 8 — Set Up Mailchimp (optional, but recommended)

1. Create a free account at https://mailchimp.com
2. Go to **Account → Extras → API Keys** → Create a key
3. Go to **Audience → Audience dashboard** → find your **Audience ID** (also called List ID)
4. Your data centre is the prefix in your API key after the dash — e.g. if your key ends in `-us21`, your DC is `us21`
5. Add these to your Azure App Settings (Step 5c)

---

## API Endpoints Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/members` | Register a new member (Join form) |
| `GET` | `/api/members` | List all members (internal) |
| `POST` | `/api/contact` | Submit a contact message |
| `GET` | `/api/contact` | List all contact submissions (internal) |
| `POST` | `/api/newsletter` | Subscribe to newsletter |
| `GET` | `/health` | Health check (used by Azure) |

Full interactive docs available at `/docs` (development only).

---

## Database Tables Created Automatically

| Table | Purpose |
|---|---|
| `members` | All community membership signups |
| `contact_submissions` | All contact form messages |
| `newsletter_subscribers` | All email newsletter signups |

Tables are created automatically on first startup — no manual SQL needed.

---

## Troubleshooting

**"Connection refused" when running locally**
→ Check your `DATABASE_URL` in `.env`. Make sure your IP is whitelisted (Step 3c).

**"ODBC Driver not found"**
→ Install ODBC Driver 17 for SQL Server (Step 4a).

**CORS errors in the browser**
→ Make sure `ALLOWED_ORIGINS` in your Azure App Settings includes your exact frontend URL (no trailing slash).

**App Service shows "Application Error"**
→ Run `az webapp log tail` to see live logs. Most common cause: wrong `DATABASE_URL` format.

**Free tier limits**
→ Azure SQL free tier includes 32GB storage and 100,000 vCore-seconds/month. For a community site at this stage, you'll never come close to hitting these limits.
