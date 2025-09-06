# Gold Investment API

This is a **FastAPI-based backend project** that provides insights, chatbot responses, and database-driven APIs for **Digital Gold investments**.

---

## 🚀 Features
- **Chatbot API**: Provides answers to Digital Gold investment questions.
- **Database Integration (SQLite)**: Stores investment transactions locally.
- **Transactions Endpoint**:  
  - `/transactions` → returns all stored transactions in **JSON format**.
- **FastAPI Interactive Docs**: Automatically generated at `/docs` and `/redoc`.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **FastAPI**
- **SQLite3** (local database)
- **Uvicorn** (ASGI server)
- **SQLAlchemy** (for ORM, if extended)

---

## 📂 Project Structure
```
gold_investment_api/
│── main.py           # FastAPI app with endpoints
│── requirements.txt  # Dependencies
│── README.md         # Project documentation
│── static/           # (Optional) static assets
│── .gitignore        # Ignored files (DB, venv, caches, etc.)
```

---

## ⚡ Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/sohanreddy5/gold_investment_api.git
   cd gold_investment_api
   ```

2. **Create and activate virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**  
   ```bash
   uvicorn main:app --reload
   ```

5. **Access APIs**  
   - Base API → http://127.0.0.1:8000  
   - Transactions → http://127.0.0.1:8000/transactions  
   - API docs → http://127.0.0.1:8000/docs  
   - Redoc docs → http://127.0.0.1:8000/redoc  

--
6.Access APIs
•Base API → http://127.0.0.1:8000
•Transactions → http://127.0.0.1:8000/transactions
•API docs → http://127.0.0.1:8000/docs
•Redoc docs → http://127.0.0.1:8000/redoc

## 📝 Example Transaction Response
```json
[
  {
    "id": 1,
    "user": "Sohan",
    "amount": 5000,
    "type": "buy",
    "timestamp": "2025-09-06T12:34:56"
  },
  {
    "id": 2,
    "user": "Ravi",
    "amount": 3000,
    "type": "sell",
    "timestamp": "2025-09-06T13:12:21"
  }
]
```

---

## 📌 Notes
- The database (`gold_transactions.db`) is **ignored in Git** via `.gitignore`.  
- Each user cloning the repo can create their own database by running the server.  
- Extendable for more APIs like **buy/sell gold, user authentication, reports, etc.**
