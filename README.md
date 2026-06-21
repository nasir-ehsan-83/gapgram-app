# 🚀 GapGram Applicatoin

A **production-ready backend API** for a social media platform, built with modern Python technologies.  
This project emphasizes **scalability, security, clean architecture, and real-world backend design**, serving as the backend core for a full-stack application with a React frontend.

---

## 🎯 Project Overview

This application is designed as a **real-world social media backend system**, implementing key engineering principles:

- **Feature-Based Architecture** (self-contained modules)
- Authentication & Authorization with JWT
- Database design & ORM (SQLAlchemy)
- RESTful API best practices
- Clean separation of concerns

**Built using:**
- FastAPI (Python)
- PostgreSQL
- SQLAlchemy ORM
- JWT Authentication (OAuth2)
- React (frontend, in progress)

---

## 🧠 Tech Stack

### Backend
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic v2
- **Authentication:** JWT + OAuth2
- **Password Hashing:** passlib (bcrypt)
- **Migrations:** Alembic

### Frontend (Planned)
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
- 📚 Interactive API Documentation
- 🧩 Feature-Based Architecture
- ✅ Input Validation with Pydantic

### 🚧 In Progress
- 💬 Comments System
- 👥 Follow/Unfollow Users
- 📧 Email Verification

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nasir-ehsan-83/gapgram-app.git
   cd gapgram-app
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp backend/.env.example backend/.env
   # Edit backend/.env with your credentials
   ```

5. **Run the development server:**
   ```bash
   uvicorn backend.app.main:app --reload
   ```

---

## 🏗 Architecture

### Feature-Based Architecture
Each feature is self-contained with its own models, schemas, services, and routes.

**Benefits:**
- ✅ Clear separation of concerns
- ✅ Easy maintenance and scalability
- ✅ Modular development

---

## 👨‍💻 Author
- **Nasir Ahmad Ehsan**
- 🔗 GitHub: nasir-ehsan-83
- 💼 Backend Developer | AI Enthusiast | Systems Programmer

---

## 📜 License
This project is licensed under the MIT License.
