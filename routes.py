from flask import render_template
from MY AI import app

@app.route("/")
def home():
    return render_template("index.html")
