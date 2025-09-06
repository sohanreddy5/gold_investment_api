from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random
import sqlite3

app = FastAPI(title="Digital Gold Chatbot")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

# Database setup
DB_NAME = "gold_transactions.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            gold_type TEXT,
            amount_spent REAL,
            gold_purchased_g REAL,
            price_per_gram REAL,
            transaction_status TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Descriptive replies
gold_safety_replies = [
    "Digital Gold is a safe investment. It’s stored securely in banks, liquid, and protects your wealth against inflation. 🛡️",
    "Investing in Digital Gold is convenient and risk-free. You can buy even 1 rupee worth, and it’s insured and fully redeemable. 💰",
    "Digital Gold acts as a financial shield. You can start small, diversify, and benefit from market stability. 🌟"
]

gold_buy_replies = [
    "Great! Digital Gold is super convenient. Let me show you the current price per gram and you can decide how much to buy. 💎",
    "Digital Gold is instantly tradable and fully insured. Let’s check today’s price and then you can pick your amount to invest! 💰",
    "Ready to shine your portfolio with Digital Gold? First, here’s the current price per gram, then enter your desired amount. 🌟"
]

# Home route
@app.get("/", response_class=HTMLResponse)
def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ask question API
@app.post("/ask-question")
def ask_question(user_id: str = Form(...), query: str = Form(...)):
    query_lower = query.lower()
    if "buy" in query_lower or "purchase" in query_lower:
        reply = random.choice(gold_buy_replies)
        current_price = random.randint(10000, 12000)
        return {
            "message": f"{reply}\n💰 Current Digital Gold Price: ₹{current_price}/g",
            "next_step": True,
            "show_types": True,
            "current_price": current_price
        }
    elif "gold" in query_lower:
        reply = random.choice(gold_safety_replies)
        return {"message": reply, "next_step": False, "show_types": False}
    else:
        return {
            "message": "I specialize in Digital Gold investments only. You can ask questions like 'Is Digital Gold safe?' or 'I want to buy Digital Gold'. I'll give detailed guidance!",
            "next_step": False,
            "show_types": False
        }

# Buy gold API
@app.post("/buy-gold")
def buy_gold(
    user_id: str = Form(...),
    amount: float = Form(...),
    gold_type: str = Form(...),
    price_per_gram: float = Form(...)
):
    try:
        grams = amount / price_per_gram

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (user_id, gold_type, amount_spent, gold_purchased_g, price_per_gram, transaction_status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, gold_type, amount, grams, price_per_gram, "Success"))
        conn.commit()
        conn.close()

        return {
            "message": f"🎉 Transaction successful! You bought {grams:.4f}g of {gold_type} at ₹{price_per_gram}/g for a total of ₹{amount}. Your digital gold is safely stored and insured!",
            "transaction": {
                "user_id": user_id,
                "gold_type": gold_type,
                "amount_spent": amount,
                "gold_purchased_g": grams,
                "price_per_gram": price_per_gram,
                "transaction_status": "Success"
            }
        }

    except Exception as e:
        return {
            "message": f"❌ Transaction failed due to: {str(e)}. Please try again.",
            "transaction": None
        }

# 🔥 New API to view all transactions
@app.get("/transactions")
def get_transactions():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    conn.close()

    # Convert to dict list
    transactions = [
        {
            "id": row[0],
            "user_id": row[1],
            "gold_type": row[2],
            "amount_spent": row[3],
            "gold_purchased_g": row[4],
            "price_per_gram": row[5],
            "transaction_status": row[6]
        }
        for row in rows
    ]

    return {"transactions": transactions}
