#models.py

from config import db
from sqlalchemy.sql import func

#representa uma entidade do banco
#a classe Produto estende a classe Model do pacote db
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer)
    cadastrado = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<Produto: {self.id} desc: {self.descricao} preço: {self.preco} quant: {self.quantidade} data: {self.cadastrado}>'