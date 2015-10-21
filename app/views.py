from flask import render_template, request
from app import app
from utils import greige, send_mail

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/recolor', methods=["POST"])
def recolor():
    uploaded_files = request.files.getlist("files")
    colors = set(request.form.getlist('color'))
    email = request.form.get('email')

    greiged_files = []
    for u_file in uploaded_files:
        f_name, f_extension = u_file.filename.split('.')
        for color in colors:
            if color:
                new_filename = f_name + '_%s.' % color[1:] + f_extension
                greiged_files.append({'name': new_filename, 'file': greige(u_file, color)})

    send_mail(email, greiged_files)
    return ''
