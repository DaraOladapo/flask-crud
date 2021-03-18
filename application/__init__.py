#imports flask module
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__, template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = '12345'

db = SQLAlchemy(app)

from application import routes