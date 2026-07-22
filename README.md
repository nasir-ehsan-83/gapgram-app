# 🚀 AfghanGap Application

A **production-ready backend API** for a social media platform, built with modern Python technologies.  
This project emphasizes **scalability, security, clean architecture, and real-world backend design**, serving as the backend core for a full-stack application with a React frontend.

---

## 🎯 Project Overview

This application is designed as a **real-world social media backend system**, implementing key engineering principles:

- **Feature-Based Architecture** (self-contained modules)
- **FastAPI Modern Lifespan** for clean database initialization & teardown
- Authentication & Authorization with JWT
- Database design & ORM (SQLAlchemy Async Engine)
- RESTful API best practices with structured Error Handlers
- Clean separation of concerns

---

## 🧠 Tech Stack

### Backend
- **Framework:** FastAPI
- **Package Manager:** Poetry 2.0+ (Modern standard)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy (Async)
- **Validation:** Pydantic v2
- **Authentication:** JWT 
- **Password Hashing:** passlib (bcrypt)
- **Migrations:** Alembic
- **Containerization:** Docker

### Frontend (In Progress)
- React
- Axios
- Tailwind CSS

---

## ✨ Features

### ✅ Completed
- 🔐 User Authentication (Register, Login)
- 🔑 JWT-based Authorization
- 🔒 Secure Password Hashing
- 👤 User Management (CRUD)
- 📝 Posts (Create, Read, Update, Delete)
- 👍 Voting System (Like/Unlike)
- 🗄 PostgreSQL Integration
- 🌐 RESTful API
- ⚙️ Global Structured Error Handling System
- 📚 Interactive API Documentation (Swagger/ReDoc)
- 🧩 Feature-Based Architecture
- ✅ Input Validation with Pydantic v2

### 🚧 In Progress
- 💬 Comments System
- 👥 Follow/Unfollow Users
- 📧 Email Verification

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Poetry 2.0+
- PostgreSQL or Docker

### Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nasir-ehsan-83/afghan-gap.git
   cd afghan-gap/server
   ```

2. **Install dependencies via Poetry:**
   ```bash
   poetry install
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your local credentials
   ```

4. **Run the development server via Launcher:**
   ```bash
   poetry run python3 run.py
   ```
   *The server will start on `http://0.0.0` with auto-reload enabled.*

### Docker Deployment

You can containerize the application easily using the provided multi-stage production Dockerfile:

1. **Build the Docker Image:**
   ```bash
   docker build -t gapgram-backend .
   ```

2. **Run the Container:**
   ```bash
   docker run -p 8000:8000 --env-file .env gapgram-backend
   ```

---

## 🏗 Architecture

### Feature-Based Architecture
Each feature is self-contained under `src/modules/` with its own models, schemas, repositories, services, and routes. Shared utilities and system-wide configurations are modularly stored under `src/common/` and `src/core/`.

**Benefits:**
- ✅ Clear separation of concerns
- ✅ Easy maintenance and scalability
- ✅ Highly modular development & effortless unit testing

---

## 👨‍💻 Author
- **Nasir Ahmad Ehsan**
- 🔗 GitHub: [nasir-ehsan-83](https://github.com/nasir-ehsan-83)
- 💼 Backend Engineer | Systems Programmer | AI Enthusiast

---

## 📜 License
This project is licensed under the MIT License.
