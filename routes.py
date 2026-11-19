from flask import render_template
from __init__ import app

@app.route("/")
def home():
    return render_template("index.html")
