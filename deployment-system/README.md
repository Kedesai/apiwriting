# 🚀 Deployment Management System (FastAPI + SQLite)

A production-style backend API built using **FastAPI**, **SQLAlchemy**, and **SQLite** to simulate a deployment management system.

This project demonstrates real-world backend concepts including:
- Modular architecture
- Service layer design
- Background processing
- Database integration
- RESTful API design

---

## Features

- Create deployment jobs
- Track deployment status lifecycle (`pending → running → success`)
- Store deployments in a real database (SQLite)
- Background processing using threads
- Delete deployments
- Scalable project structure (routes, services, models, db)

---

## Architecture Overview
## Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- Threading

---

## Project Structure
Setup Instructions

### 1️ Clone the repository

```bash
git clone <your-repo-url>
cd deployment-system

python -m venv venv

venv\Scripts\activate - windows
source venv/bin/activate - linux / mac

pip install fastapi uvicorn sqlalchemy

uvicorn app.main:app --reload

API Base URL
http://127.0.0.1:8000

API Endpoints
 Create Deployment
POST /deployments

Get Deployment by ID
GET /deployments/{deployment_id}

 List All Deployments
GET /deployments

 Delete Deployment
DELETE /deployments/{deployment_id}

 Deployment Lifecycle
Each deployment goes through:
pending → running → success

Example Request:


curl -X POST "http://127.0.0.1:8000/deployments" \
-H "Content-Type: application/json" \
-d '{
  "app_name": "demo-app",
  "project_id": 123,
  "version": "1.0",
  "environment": "dev",
  "initiated_by": "user1"
}'

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

Database

SQLite database file: deployments.db
Managed via SQLAlchemy ORM
Tables auto-created on startup


docker build -t deployment-system .
docker run -p 8000:8000 deployment-system
