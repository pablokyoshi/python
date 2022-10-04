class Produto:

    def __init__(self,id, descricao, preco, quantidade):
        self.__id=id
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade = quantidade

#construtor padrão
    def __init__(self):
        pass

    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    def __str__ (self):
        return f'ID: {self.__id} \tDescrição: {self.__descricao} \tPreço: R${self.__preco:.2f} \tQuantidade: {self.__quantidade}'

    @id.setter
    def id(self, id):
        self.__id = id

    @descricao.setter
    def descricao(self,descricao):
        self.__descricao = descricao

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @quantidade.setter
    def quantidade(self,quantidade):
        self.__quantidade = quantidade
