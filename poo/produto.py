class Produto:

    #construtor da classe
    def __init__(self, nome):
        self.nome = nome

    #funções ou métodos
    def imprimir(self):
        print(self.nome)

if __name__== '__main__':
    p1 = Produto('Bolacha')
    print(p1.nome)
    #p1.imprimir()

    p2 = Produto('Leite')
    #p2.imprimir()
    print(p2.nome)