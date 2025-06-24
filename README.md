# 🌙 Late Show API — Flask Code Challenge

## Overview
A RESTful API for managing a Late Night TV show system, built with Flask, PostgreSQL, and JWT authentication.

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Install dependencies
```bash
pipenv install --dev
pipenv shell
```

### 3. PostgreSQL Database Setup
- Ensure PostgreSQL is running.
- Create the database:
```bash
createdb late_show_db
```

### 4. Configure Environment
- Edit `server/config.py` if needed:
  - `SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"`
- Set environment variables:
```bash
export FLASK_APP=server/app.py
export PYTHONPATH=.
export JWT_SECRET_KEY=your-secret-key
```

### 5. Run Migrations
```bash
flask db init        # Only once, if migrations/ does not exist
flask db migrate -m "initial migration"
flask db upgrade
```

### 6. Seed the Database (optional)
```bash
python server/seed.py
```

### 7. Run the Server
```bash
flask run
```

---

## 🔐 Authentication Flow
- Register: `POST /register` with `{ "username": "...", "password": "..." }`
- Login: `POST /login` with `{ "username": "...", "password": "..." }`
- Use the returned JWT token in the `Authorization: Bearer <token>` header for protected routes.

---

## 🛣️ API Routes
| Route                        | Method | Auth? | Description                        |
|------------------------------|--------|-------|------------------------------------|
| /register                    | POST   | ❌    | Register a new user                |
| /login                       | POST   | ❌    | Log in and get JWT token           |
| /episodes                    | GET    | ❌    | List all episodes                  |
| /episodes/<id>               | GET    | ❌    | Get episode + appearances          |
| /episodes/<id>               | DELETE | ✅    | Delete episode + appearances       |
| /guests                      | GET    | ❌    | List all guests                    |
| /appearances                 | POST   | ✅    | Create a new appearance            |

### Sample Request/Response
**Register:**
```json
POST /register
{
  "username": "admin",
  "password": "password123"
}
```
**Login:**
```json
POST /login
{
  "username": "admin",
  "password": "password123"
}
Response: { "access_token": "..." }
```
**Protected Example:**
```http
POST /appearances
Authorization: Bearer <token>
{
  "rating": 5,
  "guest_id": 1,
  "episode_id": 1
}
```

---

## 🧪 Postman Usage
- Import `challenge-4-lateshow.postman_collection.json` into Postman.
- Test all endpoints, including registration, login, and protected routes.
- For protected routes, set the `Authorization` header to `Bearer <token>`.

---

## 📂 Folder Structure
```
server/
  app.py
  config.py
  seed.py
  models/
    user.py guest.py episode.py appearance.py
  controllers/
    auth_controller.py guest_controller.py episode_controller.py appearance_controller.py
migrations/
challenge-4-lateshow.postman_collection.json
README.md
```

---

## 📎 GitHub Repo
[https://github.com/<your-username>/late-show-api-challenge](https://github.com/<your-username>/late-show-api-challenge)

---

## ✅ Submission Checklist
- [x] MVC folder structure
- [x] PostgreSQL used (no SQLite)
- [x] Models + validations complete
- [x] Auth implemented + protected routes
- [x] Seed data works
- [x] All routes work and tested in Postman
- [x] Clean, complete README.md
- [x] GitHub repo pushed and shared

created by JOEL NGIGI
CONTACT: 
Email:ngangajoel254@gmail.com
NO: +254757735896

