
# Gold Investment Chatbot & API  

This project is a **Digital Gold Investment platform** built with **FastAPI** for the backend, a **SQLite database** for storage, and a **simple frontend (HTML, CSS, JS)** for user interaction.  

It allows users to:  
- Ask questions about **gold investment** through a **chatbot**.  
- **Buy gold** using the API, with details securely stored in the database.  
- View transactions stored in **SQLite**.  

---

## 🔌 APIs Used  

### 1. **Chatbot API**  
**Endpoint:** `/ask-question` (POST)  
- Takes a user’s question as input.  
- Returns a descriptive answer about gold investment.  
- Example:  
  ```json
  { "question": "Is gold a safe investment?" }
  ```
  Response:  
  ```json
  { "answer": "Yes, gold is considered a safe investment, especially during inflation." }
  ```

---

### 2. **Buy Gold API**  
**Endpoint:** `/buy-gold` (POST)  
- Accepts details like user ID, amount to invest, gold type, and current price per gram.  
- Calculates how many grams of gold are purchased.  
- Stores transaction in the **SQLite database** (`gold_transactions.db`).  
- Example:  
  ```json
  { "user_id": "sohan123", "amount": 2000, "gold_type": "Digital Gold", "price_per_gram": 6000 }
  ```
  Response:  
  ```json
  {
    "message": "🎉 You bought 0.3333g of Digital Gold at ₹6000/g for ₹2000. Safely stored and insured!",
    "db_entry": {
      "user_id": "sohan123",
      "gold_type": "Digital Gold",
      "amount_spent": 2000,
      "gold_purchased_g": 0.3333,
      "price_per_gram": 6000,
      "transaction_status": "Success"
    }
  }
  ```

---

## 🖥️ Technologies Used  

### Backend (Server Side)  
- **FastAPI** → Framework for APIs  
- **Uvicorn** → ASGI server to run the app  
- **SQLite** → Lightweight database for storing transactions  
- **Python** → Main programming language  

### Frontend (Client Side)  
- **HTML** → Structure of the chatbot page  
- **CSS** → Styling for chatbot interface  
- **JavaScript** → Sends questions & transactions to the backend APIs and displays responses  

---

## 📦 Requirements  

To run this project, you need:  
- **Python 3.9+**  
- **pip** (Python package installer)  
- Required dependencies (install with):  
  ```bash
  pip install -r requirements.txt
  ```

Main libraries in `requirements.txt`:  
- fastapi  
- uvicorn  
- sqlite3 (built-in with Python)  
- python-multipart (for form data handling)  

---

## 🤖 The Chatbot  

The chatbot is a **rule-based assistant** built into the FastAPI backend.  
- It receives user questions via `/ask-question`.  
- Responds with descriptive answers about **digital gold**, safety, investment strategies, etc.  
- The frontend (`index.html`) provides a simple chat-like interface where users can type questions.  

This is not AI-powered (like ChatGPT), but rather a **pre-programmed, knowledge-based chatbot** focused on **gold investment guidance**.  

---

## ▶️ How to Run  

1. Clone the repo and enter the folder:
   ```bash
   git clone https://github.com/your-username/gold_investment_api.git
   cd gold_investment_api
   ```

2. Activate virtual environment (if set up):  
   ```bash
   source venv/bin/activate   # Mac/Linux  
   venv\Scripts\activate      # Windows  
   ```

3. Run the FastAPI server:  
   ```bash
   uvicorn main:app --reload
   ```

4. Open in browser:  
   ```
   http://127.0.0.1:8000
   ```

---

## 💾 Accessing the Database  

We use **SQLite**, and the database file is `gold_transactions.db`.  

To view saved transactions:  

```bash
sqlite3 gold_transactions.db
```

Inside the SQLite shell:  
```sql
.tables                -- shows tables
SELECT * FROM transactions;
.exit                  -- to quit
```
