#tabeladb.py
#pip install pyqt5

from os.path import exists
from PyQt5.QtWidgets import *
from PyQt5.QtSql import*

import sys

if not exists ('pablobd.db'):
    print('bancodados,db não existe')
    sys.exit()

app=QApplication([])

db =QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('pablobd.db')
db.open()#conecta com o banco de dados

#cria uma tabela de dados
model = QSqlTableModel(None,db) # cria um modelo
model.setTable ('contato')
model.select() #select * from Contato

view = QTableView()
view.setModel(model)
view.show()

app.exec_()
