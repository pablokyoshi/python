#qlite.py
#PyQt com banco de dados SQLite


import sqlite3

#conecta ou cria o arquivo de banco de dados
con = sqlite3.connect('pablobd.db')

#obtém um cursor
cur = con.cursor()

#função para inserir dados
def inserir_dados():
    #define a tabela
    sql= 'create table contato'\
         '(id integer primary key,' \
         'nome varchar (100),' \
         'email varchar(100),' \
         'telefone varchar(14))'

    #cria a tabela
    cur.execute(sql)

    #sentença para inserir os registros no banco
    sql= 'insert into contato values (null,?, ?, ?)'

    #dados
    lista = [('Joao da Silva', 'joao@gmail.com', '(42) 9123-7777'),
             ('Maria da Silva', 'mary@gmail.com', '(42) 9223-2111'),
             ('Luiz Carlos', 'luiz@gmail.com', '(42) 9870-4561'),
             ]
    #insere os registros
    for tupla in lista:
        cur.execute(sql, tupla)

    #confirma os dados no banco
    con.commit()

#função principal
if __name__ == '__main__':
    inserir_dados()
