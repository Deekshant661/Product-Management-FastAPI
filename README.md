# Product Management App (FastAPI + React)

A simple full-stack **Product Management CRUD application** built using **FastAPI** for the backend and **React** for the frontend.
The app allows users to **create, view, update, delete, search, filter, and sort products**, with data stored in a database.

---

##  Features

* Create, Read, Update, Delete (CRUD) products
* FastAPI backend with SQLAlchemy ORM
* React frontend with Axios
* Sorting, searching, and filtering
* CORS enabled for frontend-backend communication

---

## Tech Stack

### Frontend

* React
* Axios
* HTML, CSS, JavaScript

### Backend

* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn

### Database

* Postgre SQL

---

## 📁 Project Structure

```
fastApi-crud/
│
├── frontend/        # React app
├── main.py          # FastAPI entry point
├── models.py        # Pydantic models
├── database.py      # DB connection
├── database_models.py
└── .gitignore
```

---

## ✅ Prerequisites

* Python 3.10+
* Node.js 18+
* Git

---

## Backend Setup (FastAPI)

Open terminal in project root:

```bash
python -m venv myenv
```

Activate virtual environment:

**Windows**

```bash
myenv\Scripts\activate
```

**Mac/Linux**

```bash
source myenv/bin/activate
```

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

Run backend:

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

Swagger Docs:

```
http://localhost:8000/docs
```

---

## Frontend Setup (React)

Open another terminal:

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## 🔗 API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | /products      | Get all products  |
| GET    | /products/{id} | Get product by id |
| POST   | /products      | Add product       |
| PUT    | /products/{id} | Update product    |
| DELETE | /products/{id} | Delete product    |

---

## 🧪 Sample Product JSON

```json
{
  "id": 1,
  "name": "Phone",
  "description": "Smartphone",
  "price": 699.99,
  "quantity": 10
}
```

---

##  Notes

* Backend must be running before frontend
* `node_modules` and `myenv` are ignored using `.gitignore`
* CORS configured for `http://localhost:3000`

---

## 📌 Future Improvements

* Authentication (Login / Signup)
* Pagination
* Deployment
* Cloud database

---


