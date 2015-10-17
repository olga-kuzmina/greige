from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recolor', methods=["POST"])
def recolor():
    uploaded_files = request.files.getlist("files")
    return ""
