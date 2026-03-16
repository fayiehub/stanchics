# Stanchics API — Backend Setup Guide

FastAPI backend for the Stanchics Women in Tech community, Nairobi Kenya.
Handles membership signups, contact form submissions, newsletter subscriptions, and community feedback.

---

## Table of Contents

1. [Project Structure](#1-project-structure)
2. [Prerequisites](#2-prerequisites)
3. [Open the Project](#3-open-the-project)
4. [Create a Virtual Environment](#4-create-a-virtual-environment)
5. [Install Dependencies](#5-install-dependencies)
6. [Install the ODBC Driver](#6-install-the-odbc-driver)
7. [Set Up Azure SQL Database](#7-set-up-azure-sql-database)
8. [Configure Environment Variables](#8-configure-environment-variables)
9. [Run the API Locally](#9-run-the-api-locally)
10. [Verify Everything Works](#10-verify-everything-works)
11. [API Endpoints Reference](#11-api-endpoints-reference)
12. [Deploy to Azure App Service](#12-deploy-to-azure-app-service)
13. [Connect the Frontend](#13-connect-the-frontend)
14. [Troubleshooting](#14-troubleshooting)

---

## 1. Project Structure

```
stanchics-api/
├── app/
│   ├── __init__.py               # Package marker
│   ├── main.py                   # FastAPI app entry point — CORS, routers, startup
│   ├── config.py                 # Settings loaded from .env file
│   ├── database.py               # SQLAlchemy engine, session, table creation
│   ├── models/
│   │   ├── __init__.py           # Registers all models with SQLAlchemy
│   │   ├── member.py             # members table
│   │   ├── contact.py            # contact_submissions table
│   │   ├── newsletter.py         # newsletter_subscribers table
│   │   └── feedback.py           # feedback table
│   ├── routers/
│   │   ├── __init__.py           # Exports all routers
│   │   ├── members.py            # POST /api/members, GET /api/members
│   │   ├── contact.py            # POST /api/contact, GET /api/contact
│   │   ├── newsletter.py         # POST /api/newsletter
│   │   └── feedback.py           # POST /api/feedback, GET /api/feedback
│   ├── schemas/
│   │   └── __init__.py           # Pydantic request/response validation models
│   └── services/
│       ├── __init__.py           # Package marker
│       └── mailchimp.py          # Mailchimp newsletter sync helper
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variable template — copy to .env
├── startup.txt                   # Azure App Service startup command
└── AZURE_SETUP.md                # Full Azure infrastructure setup guide
```

---

## 2. Prerequisites

Make sure the following are installed on your machine before starting.

| Tool | Minimum Version | Download |
|---|---|---|
| Python | 3.11 | https://www.python.org/downloads |
| Git | Any recent | https://git-scm.com/downloads |
| Azure CLI | Any recent | https://learn.microsoft.com/en-us/cli/azure/install-azure-cli |
| VS Code | Any recent | https://code.visualstudio.com |

Verify all installs by running these in your terminal:

```bash
python --version
git --version
az --version
```

All three should print version numbers without errors.
If `python` does not work, try `python3`.

---

## 3. Open the Project

Navigate into the backend folder and open it in VS Code:

```bash
cd stanchics-api
code .
```

Your VS Code explorer should show the structure from Section 1.
If any files are missing, refer to the full file list shared during project setup.

---

## 4. Create a Virtual Environment

A virtual environment keeps this project's dependencies isolated from everything
else on your machine. Run this once from inside the `stanchics-api/` folder:

```bash
python -m venv venv
```

Then activate it. You must run this activation command every time you open
a new terminal for this project:

```bash
# macOS / Linux
source venv/bin/activate

# Windows — Command Prompt
venv\Scripts\activate.bat

# Windows — PowerShell
venv\Scripts\Activate.ps1
```

You will know it is active when your terminal prompt starts with `(venv)`.

> **VS Code tip:** Press `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`), type
> `Python: Select Interpreter`, and choose the option that says `venv`.
> VS Code will then activate the environment automatically in its
> integrated terminal from that point on.

---

## 5. Install Dependencies

With your virtual environment active, install all required packages:

```bash
pip install -r requirements.txt
```

This installs:

| Package | Purpose |
|---|---|
| `fastapi` | The web framework |
| `uvicorn` | The server that runs FastAPI |
| `sqlalchemy` | Database ORM (talks to Azure SQL) |
| `pyodbc` | Low-level Azure SQL connection driver |
| `pydantic` + `pydantic-settings` | Request validation and settings management |
| `httpx` | HTTP client for Mailchimp API calls |
| `python-dotenv` | Loads your .env file |
| `slowapi` | Rate limiting |

Installation takes 1–2 minutes. You should see `Successfully installed ...`
at the end with no red errors.

---

## 6. Install the ODBC Driver

The ODBC Driver is required to connect Python to Azure SQL.
It is installed at the **system level** — not inside the virtual environment.

### macOS

```bash
brew install msodbcsql17
```

If you do not have Homebrew, install it first: https://brew.sh

### Windows

Download and run the installer from Microsoft:
https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server

Select **ODBC Driver 17 for SQL Server**.

### Ubuntu / Debian Linux

```bash
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list \
  | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
```

### Verify the driver installed

```bash
# macOS / Linux
odbcinst -q -d -n "ODBC Driver 17 for SQL Server"

# Windows — check Add/Remove Programs for:
# "Microsoft ODBC Driver 17 for SQL Server" 
```

---

## 7. Set Up Azure SQL Database

You need an Azure account and a SQL database before the API can run.
Follow **Steps 1 through 3** in `AZURE_SETUP.md` (included in this project).

After completing those steps you will have:

- An Azure SQL server address, i.e. `stanchics-sql-server.database.windows.net`
- A database named `stanchics`
- A username and password for the server
- Your IP address whitelisted in the Azure firewall

You will need all four of these details in the next step.

> **Want to skip Azure for now and test locally?**
> You can use SQLite instead — no Azure account needed.
> In Section 8, set your DATABASE_URL to:
> `sqlite:///./stanchics.db`
> This creates a local file-based database. Fine for development, not production.

---

## 8. Configure Environment Variables

The API reads all its configuration from a `.env` file.
This file is never committed to Git because it contains secrets.

**Create your `.env` file** by copying the example template:

```bash
# macOS / Linux
cp .env.example .env

# Windows — Command Prompt
copy .env.example .env

# Windows — PowerShell
Copy-Item .env.example .env
```

**Open `.env` in VS Code** and replace the placeholder values:

```env
# Your Azure SQL connection string from Section 7
DATABASE_URL=mssql+pyodbc://YOUR_USER:YOUR_PASSWORD@YOUR_SERVER.database.windows.net/stanchics?driver=ODBC+Driver+17+for+SQL+Server

# Mailchimp — optional, leave as-is to skip for now
MAILCHIMP_API_KEY=your-mailchimp-api-key
MAILCHIMP_LIST_ID=your-audience-list-id
MAILCHIMP_DC=us21

# Email address that receives contact form notifications
CONTACT_RECIPIENT_EMAIL=your-email@example.com

# URLs allowed to call this API (your frontend addresses)
ALLOWED_ORIGINS=http://localhost:5500,http://127.0.0.1:5500

APP_ENV=development
SECRET_KEY=replace-this-with-a-generated-value
```

**Generate a secure SECRET_KEY** by running:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the printed output and paste it as your `SECRET_KEY` value.

> **Mailchimp is optional.** If you leave those fields as placeholders the API
> skips Mailchimp sync silently — all other functionality works normally.

---

## 9. Run the API Locally

With your virtual environment active and `.env` filled in, start the server:

```bash
uvicorn app.main:app --reload --port 8000
```

- `--reload` automatically restarts the server when you save any file
- `--port 8000` runs it on port 8000

**Expected output:**

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Application startup complete.
```

**On the very first run**, the app automatically creates all four database tables:

- `members`
- `contact_submissions`
- `newsletter_subscribers`
- `feedback`

No SQL scripts needed — this happens on startup automatically.

---

## 10. Verify Everything Works

With the server running, open your browser and check the following.

### Health check

```
http://localhost:8000/health
```

Expected response:

```json
{ "status": "ok", "service": "Stanchics API" }
```

### Interactive API docs

```
http://localhost:8000/docs
```

This opens Swagger UI — a full interactive interface to test every endpoint
without needing the frontend at all.

### Test an endpoint step by step

1. Go to `http://localhost:8000/docs`
2. Click `POST /api/newsletter` to expand it
3. Click **Try it out**
4. Paste this into the request body:
   ```json
   { "email": "test@example.com", "source": "local_test" }
   ```
5. Click **Execute**
6. You should see a `201` status and this response:
   ```json
   { "message": "You're on the list! We'll be in touch soon." }
   ```

A `201` response confirms both the API and the database connection are working.

---

## 11. API Endpoints Reference

| Method | Endpoint | Description | Called by |
|---|---|---|---|
| GET | `/health` | Health check | Azure App Service |
| POST | `/api/members` | Register a new community member | Community page join form |
| GET | `/api/members` | List all members | Internal admin |
| POST | `/api/contact` | Submit a contact message | Contact page form |
| GET | `/api/contact` | List all contact submissions | Internal admin |
| POST | `/api/newsletter` | Subscribe to newsletter | Home, Events, and Footer forms |
| POST | `/api/feedback` | Submit community feedback | Community page feedback form |
| GET | `/api/feedback` | List all feedback submissions | Internal admin |

All `POST` endpoints return `201 Created` on success.
Invalid or missing fields return `422 Unprocessable Entity` with a description
of exactly what went wrong.

---

## 12. Deploy to Azure App Service

Once the API is working locally, follow these steps to deploy it.

### Step 1 — Log in to Azure

```bash
az login
```

A browser window will open. Sign in with your Azure account.

### Step 2 — Create an App Service Plan (free tier)

```bash
az appservice plan create \
  --name stanchics-plan \
  --resource-group stanchics-rg \
  --sku F1 \
  --is-linux
```

### Step 3 — Create the Web App

```bash
az webapp create \
  --name stanchics-api \
  --resource-group stanchics-rg \
  --plan stanchics-plan \
  --runtime "PYTHON:3.11"
```

Your API will be accessible at: `https://stanchics-api.azurewebsites.net`

### Step 4 — Set environment variables on Azure

```bash
az webapp config appsettings set \
  --name stanchics-api \
  --resource-group stanchics-rg \
  --settings \
    DATABASE_URL="your-full-azure-sql-connection-string" \
    MAILCHIMP_API_KEY="your-key" \
    MAILCHIMP_LIST_ID="your-list-id" \
    MAILCHIMP_DC="us21" \
    ALLOWED_ORIGINS="https://your-frontend.azurestaticapps.net" \
    APP_ENV="production" \
    SECRET_KEY="your-generated-secret"
```

### Step 5 — Set the startup command

```bash
az webapp config set \
  --name stanchics-api \
  --resource-group stanchics-rg \
  --startup-file "uvicorn app.main:app --host 0.0.0.0 --port 8000"
```

This command is also saved in `startup.txt` in this project for reference.

### Step 6 — Deploy via Git

```bash
# Initialise git if you have not already done so
git init
git add .
git commit -m "Initial Stanchics API deployment"

# This command prints your Azure Git remote URL
az webapp deployment source config-local-git \
  --name stanchics-api \
  --resource-group stanchics-rg

# Add the printed URL as a remote, then push
git remote add azure <URL-PRINTED-BY-THE-COMMAND-ABOVE>
git push azure main
```

### Step 7 — Verify the deployment

```bash
# Stream live logs to confirm the app started correctly
az webapp log tail \
  --name stanchics-api \
  --resource-group stanchics-rg
```

Then open in your browser:
`https://stanchics-api.azurewebsites.net/health`

Expected: `{"status": "ok", "service": "Stanchics API"}`

---

## 13. Connect the Frontend

Once deployed, open `stanchics-frontend/js/main.js` and update the `API_BASE`
constant at the top of the file:

```javascript
// Find this line near the top of main.js and update to your live URL:
const API_BASE = 'https://stanchics-api.azurewebsites.net';
```

Also confirm your frontend's URL is listed in `ALLOWED_ORIGINS` in your
Azure App Settings (Step 4 above). Without this the browser will block all
API requests with a CORS error.

---

## 14. Troubleshooting

**`ModuleNotFoundError` when running uvicorn**

Your virtual environment is not active. Run the activation command for your
OS (Section 4) and try again.

---

**`[08001] Unable to connect to data source`**

Check three things:
1. ODBC Driver 17 for SQL Server is installed (Section 6)
2. The username, password, and server address in `.env` exactly match your Azure SQL setup
3. Your IP address is whitelisted in the Azure SQL firewall (AZURE_SETUP.md Step 3c)

---

**Connection timeout on first run**

Azure SQL free tier auto-pauses after a period of inactivity. The first
connection after a pause can take 20–30 seconds. Wait and try again —
subsequent requests will be fast.

---

**`CORS error` in the browser**

Your frontend URL is not in `ALLOWED_ORIGINS`. Update the value in your `.env`
(for local) or Azure App Settings (for production) to include the exact URL
of your frontend with no trailing slash.

---

**Port 8000 is already in use**

Run the server on a different port:

```bash
uvicorn app.main:app --reload --port 8001
```

---

**Changes are not reflected after saving a file**

Make sure you started uvicorn with `--reload`. Without it you need to manually
stop (`Ctrl+C`) and restart the server after every change.

---

*For full Azure infrastructure setup — creating the resource group, SQL server,
and database from scratch — refer to `AZURE_SETUP.md` included in this project.*
