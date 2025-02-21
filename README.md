# 🚀 FastAPI Modular Project with Poetry & SQLAlchemy

This is a **modular FastAPI project** structured like Nest.js, using **Poetry** for dependency management and **SQLAlchemy** for database interactions.

---

## 💂️ Project Structure

```
📚 app
 ┓ 📚 core              # Core configuration (DB, settings, dependencies)
 ┓ 📚 modules           # Modular structure for features
 ┗📚 user            # Example module (User)
    ┓ 📚 controllers   # API routes for users
    ┓ 📚 models        # SQLAlchemy models
    ┓ 📚 schemas       # Pydantic schemas
    ┓ 📚 services      # Business logic
    ┓ 📚 repository    # DB queries
 ┓ 📚 migrations        # Alembic migrations
 ┓ 📚 main.py           # FastAPI entry point
 ┗ 📚 config.py         # Application settings
```

---

## 🚀 Setup & Installation

### 1️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 2️⃣ Install Dependencies with Poetry
```sh
poetry install
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file:
```
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your-secret-key
```

### 4️⃣ Run Database Migrations
```sh
alembic upgrade head
```

### 5️⃣ Start the FastAPI Server
```sh
uvicorn app.main:app --reload
```

---

## 🛠️ Features

✅ **FastAPI** - Modern, fast (high-performance) web framework  
✅ **Poetry** - Dependency management  
✅ **SQLAlchemy** - ORM for database interactions  
✅ **Pydantic** - Data validation and serialization  
✅ **Alembic** - Database migrations  
✅ **Modular Architecture** - Similar to Nest.js  

---

## 📞 API Endpoints

| Method | Endpoint       | Description             |
|--------|--------------|-------------------------|
| GET    | `/users/`    | Get all users          |
| POST   | `/users/`    | Create a new user      |

---

## 🐟 License

This project is licensed under the MIT License.

---

💡 **Need help?** Open an issue or contribute to the project! 🚀

