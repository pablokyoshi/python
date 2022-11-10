class Produto:
    def __init__ (self, descricao, preco, quantidade, id=None):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade = quantidade

    def __str__(self):
        return f'Código: {self.id} \tDescrição: {self.descricao} \tPreço unitário: R$ {self.preco:.2f} \tQuantidade: {self.quantidade}'

    @property
    def id(self):
        return self.__id
    @property
    def preco(self):
        return self.__preco
    @property
    def quantidade(self):
        return self.__quantidade
    @property
    def descricao(self):
        return self.__descricao
    @id.setter
    def id(self, id):
        self.__id=id

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

