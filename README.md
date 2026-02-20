# 🚀 Production-Ready FastAPI REST API

A secure, scalable REST API built with FastAPI, SQLAlchemy, and
PostgreSQL.

## 📌 Features

-   JWT Authentication
-   Password hashing (bcrypt)
-   PostgreSQL integration
-   SQLAlchemy ORM
-   Role-based access control (Admin/User)
-   Rate limiting per endpoint
-   API versioning (/api/v1)
-   Swagger documentation (/docs)
-   OpenAPI schema (/openapi.json)

------------------------------------------------------------------------

## ⚙️ Installation

### 1️⃣ Clone Repository

git clone `<your-repo-url>`{=html} cd your-project

### 2️⃣ Create Virtual Environment

python -m venv venv source venv/bin/activate \# macOS/Linux
venv`\Scripts`{=tex}`\activate     `{=tex}\# Windows

### 3️⃣ Install Dependencies

pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose
passlib\[bcrypt\] slowapi python-multipart

------------------------------------------------------------------------

## 🛢 Database Setup (PostgreSQL)

CREATE DATABASE mydb;

Update DATABASE_URL inside main.py:

DATABASE_URL = "postgresql://postgres:password@localhost:5432/mydb"

------------------------------------------------------------------------

## ▶️ Run the Server

uvicorn main:app --reload

Server will start at: http://127.0.0.1:8000

------------------------------------------------------------------------

## 📘 API Documentation

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

------------------------------------------------------------------------

## 🔐 Authentication Flow

### Register

POST /api/v1/register

{ "username": "viren", "password": "securepassword", "role": "admin" }

------------------------------------------------------------------------

### Login

POST /api/v1/login

username=viren password=securepassword

Response:

{ "access_token": "your.jwt.token", "token_type": "bearer" }

------------------------------------------------------------------------

### Access Protected Route

Authorization: Bearer `<your_token>`{=html}

GET /api/v1/profile

------------------------------------------------------------------------

## 👑 Role-Based Access

Admin-only route: GET /api/v1/admin-only

Returns 403 if user is not admin.

------------------------------------------------------------------------

## 🚦 Rate Limiting

-   5 requests/minute for registration
-   10 requests/minute for login

Returns 429 Too Many Requests if exceeded.

------------------------------------------------------------------------

## 🧩 API Versioning

All endpoints use: /api/v1

------------------------------------------------------------------------

## 🔒 Security Highlights

-   Password hashing with bcrypt
-   JWT token expiration
-   Protected routes with dependency injection
-   Role-based authorization
-   Rate limiting protection

------------------------------------------------------------------------

## 📦 Production Improvements (Next Steps)

-   Refresh Tokens
-   Redis-based rate limiting
-   Docker + Docker Compose
-   Alembic migrations
-   Logging & Monitoring
-   Environment variables (.env)
-   HTTPS deployment
-   CI/CD integration

------------------------------------------------------------------------

## 📜 License

MIT License

------------------------------------------------------------------------

## 🏆 Why This Project Matters

This project demonstrates backend architecture, authentication system
design, secure API development, and production-level best practices.
