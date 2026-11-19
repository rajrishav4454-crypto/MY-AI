from flask import render_template, request, jsonify
from __init__ import app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_text = data.get("transcript", "").lower()
    
    # यहाँ आप अपना AI लॉजिक या जवाब सेट कर सकते हैं
    if "hello" in user_text or "नमस्ते" in user_text:
        reply = "नमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?"
    elif "कैसे हो" in user_text:
        reply = "मैं बिल्कुल ठीक हूँ, आप बताइए?"
    else:
        reply = f"आपने कहा: {user_text}"
        
    return jsonify({"reply": reply})
