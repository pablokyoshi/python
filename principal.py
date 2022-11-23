#principal.py
#exemplo de orm (object relational-mapping = mapeamento objeto-relacional)

from model import Produto
from config import db, app

with app.app_context():
    db.drop_all()
    db.create_all()

#cria entidade
tv= Produto(descricao='TVSAMSUNG', preco = 1999.90, quantidade=10)

#sem id
print('ID: ', tv.id)
print('Descricao', tv.descricao)


with app.app_context():
    # salva no banco
    db.session.add(tv) #add objeto no banco
    db.session.commit() #confirma que é para salvar
    #agora tem id gerado pelo banco
    print('ID', tv.id)

    #alterando os dados
    tv.descricao = 'TV LG 50"'
    db.session.add(tv)
    db.session.commit()

    #cria outra entidade
    fogao = Produto(descricao='Fogão SAMSUNG', preco=2999.00, quantidade=10)

    #salva
    db.session.add(fogao)
    db.session.commit()

    #consulta todos os produtos do banco
    produtos = Produto.query.all()
    print(produtos)

    #busca um único registro
    porId= Produto.query.filter_by(id=1).first()
    print(porId)

    porDescricao = Produto.query.filter_by(descricao='Fogão SAMSUNG').all()
    print(porDescricao)

    #apaga
    produto = Produto.query.filter_by(id=2).first()
    if produto:
        db.session.delete(produto)
        db.session.commit()
        print('apagou id=2')
    else:
        print('não apagou')
