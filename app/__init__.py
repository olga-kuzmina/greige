from flask import Flask
from flask_mail import Mail


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
mail = Mail(app)

from app import views