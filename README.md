# apiwriting
#  Deployment API (FastAPI)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![Status](https://img.shields.io/badge/status-learning-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A simple **FastAPI-based deployment simulation API** that demonstrates REST API design, background processing, and service architecture.

---

##  Features

- Create deployment jobs
- Track deployment status
- Background processing (simulated async)
- Delete deployments
- Logging support
- Environment configuration
- Auto-generated API docs

---

##  Architecture Overview

  POST /deployments
              │
              ▼
     +------------------+
     |   FastAPI App    |
     +------------------+
              │
              ▼
  In-Memory Storage (dict)
              │
              ▼
  Background Thread Worker
              │
       (Simulated delay)
              │
              ▼
    Status → "deployed"

    ---

## Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic
- Threading (for background processing)

---

##  Project Structure

---

## Setup Instructions

### Clone repo

```bash
git clone <your-repo-url>
cd <your-repo-folder>

python -m venv venv
venv\Scripts\activate - Windows
source venv/bin/activate - Mac/ Linux
pip install fastapi uvicorn

To Run the API just run: uvicorn app:app --reload

http://127.0.0.1:8000 - App runs on

**Swagger UI**:
http://127.0.0.1:8000/docs

**ReDoc**:
http://127.0.0.1:8000/redoc

These are the endpoints:

**API Endpoints**
Create Deployment - POST /deployments
Get Deployment - GET /deployments/{deployment_id}
List Deployments - GET /deployments
Delete Deployment - DELETE /deployments/{deployment_id}
Home - GET /home

curl -X POST http://127.0.0.1:8000/deployments \
-H "Content-Type: application/json" \
-d '{"app_name":"demo","version":"1.0"}'

**Docker Build and Run**
docker build -t deployment-api .
docker run -p 8000:8000 deployment-api

Future improvements:
Replace threading with FastAPI BackgroundTasks
 Add database (SQLite/Postgres)
 Add authentication (JWT)
 Add CI/CD pipeline
 Add unit tests (pytest)
