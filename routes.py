from flask import render_template, request, jsonify
from __init__ import app
from google import genai

AQ.Ab8RN6I5RCWtJ3HqcIcpTqq8Rl3-05jqmeTGl9TQuppFEgBSRg
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_text = data.get("transcript", "")
    
    if not user_text:
        return jsonify({"reply": "मैं आपकी बात सुन नहीं पाया, कृपया दोबारा बोलें।"})

    try:
        # Gemini AI से जवाब मांगना (छोटे और बोलने लायक जवाब के लिए निर्देश के साथ)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"तुम एक स्मार्ट वॉइस असिस्टेंट हो। इस बात का छोटा, स्पष्ट और प्राकृतिक भाषा में (बिना * या # जैसे सिंबल के) हिंदी या हिंग्लिश में जवाब दो: {user_text}"
        )
        reply = response.text
    except Exception as e:
        print("AI Error:", e)
        reply = "माफ़ करें, अभी सर्वर से जुड़ने में कुछ समस्या आ रही है।"
        
    return jsonify({"reply": reply})
