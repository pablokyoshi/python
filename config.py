#pip install Flask-SQLAlchemy
#python -m pip install --upgrade pip
#pip install mysqlclient

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'softgraf'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:softgraf@localhost:3306/bancodados'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#chaves do google captcha
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LevQikjAAAAABQYrnQ1-TfVP5Ul_8uQhQFCIVxU'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LevQikjAAAAALlzHCyD0XQ9PJJZKPPFlMxdm6Eq'
app.config['RECAPTCHA_OPTIONS'] = {'theme':'white'}

db = SQLAlchemy(app)
lista = []