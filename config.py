#config.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Configurações do banco de dandos
#para MYSQL:
#mysql://username:password@host:port/database_name
#mysql://root:softgraf@localhost:3306/nome_branco

#para PostgreSQL
#postgrsql://username:password@host:port/database_name

#aqui vamos usar SQLite, entao precisamos de diretorio base do projeto
basedir=os.path.abspath(os.path.dirname(__file__))
print(basedir) #'D:\Curso Python 2\projeto_alchemy'

#uri do sqlite(uniform resource indicator -> caminho)
uri='sqlite:///' + os.path.join(basedir,'database.db')
#print(uri)

#cria a aplicação do flask
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#objeto que representa o banco de dados
db = SQLAlchemy(app)