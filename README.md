# 💰 Expense Tracker API

A secure and fully-featured RESTful API for tracking personal expenses. Built with **FastAPI**, **SQLAlchemy**, and **JWT Authentication**, this project allows users to manage their expenses with CRUD operations and filter them by various date ranges.

---

## 🚀 Features

- ✅ User registration and login (with JWT auth)
- ✅ Secure password hashing (bcrypt)
- ✅ Create, update, delete, and list expenses
- ✅ Filter expenses by:
  - Past week
  - Past month
  - Last 3 months
  - Custom date range
- ✅ SQLite database support (easily swappable with PostgreSQL)
- ✅ Pydantic schemas for input validation
- ✅ Postman collection for testing included

---

## 📁 Project Structure

```

expense-tracker-api/
├── app/
│   ├── routes/
│   │   ├── auth_routes.py        # /auth/signup and /auth/login
│   │   └── expense_routes.py     # /expenses/ CRUD and filters
│   ├── auth.py                   # JWT logic and password hashing
│   ├── database.py               # SQLAlchemy DB setup
│   ├── deps.py                   # Current user dependency
│   ├── main.py                   # FastAPI app entrypoint
│   ├── models.py                 # ORM models (User, Expense)
│   └── schemas.py                # Pydantic schemas
├── .env                          # Environment config (secret key, DB URL)
├── expense.db                    # SQLite database (auto-created)
├── requirements.txt              # Project dependencies
└── README.md

````

---

## ⚙️ Installation & Setup

### 🔹 1. Clone the Repo
```bash
git clone https://github.com/your-username/expense-tracker-api.git
cd expense-tracker-api
````

### 🔹 2. Create & Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 4. Create `.env` File

```env
SECRET_KEY=your_very_secret_key
DATABASE_URL=sqlite:///./expense.db
```

---

## 🧪 Running the App

### 🟢 Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

### 🔗 Open in Browser:

* API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📫 Postman Testing

1. Import the provided Postman collection: `Expense Tracker API.postman_collection.json`
2. Use the following workflow:

   * `POST /auth/signup` to register
   * `POST /auth/login` to get a token
   * Save the token in Postman as `{{access_token}}` environment variable
   * Use `POST /expenses/` to create expenses
   * Use `GET /expenses/` with filters like:

     * `?filter=week`, `?filter=month`, `?filter=3months`
     * Or custom: `?start=YYYY-MM-DD&end=YYYY-MM-DD`
   * Update/delete using `/expenses/{id}`

---

## 🧠 Expense Categories

You can categorize expenses using the following values:

* `Groceries`
* `Leisure`
* `Electronics`
* `Utilities`
* `Clothing`
* `Health`
* `Others`

---

## 📦 Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [SQLite](https://www.sqlite.org/) (or PostgreSQL)
* [Pydantic](https://docs.pydantic.dev/)
* [python-jose](https://python-jose.readthedocs.io/) (JWT)
* [Passlib](https://passlib.readthedocs.io/) (Password hashing)

---

## 🛠 Potential Improvements

* 🔄 Refresh token support
* 📊 Expense summaries and charts
* 🧾 Monthly reports (PDF/email)
* ☁️ Deployment (Render, Railway, etc.)
* 🔐 OAuth2 or social login

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---


