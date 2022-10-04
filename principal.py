from produto import *
# * é coringa, importa qualquer arquivo classe

def entrada():
    p1 = Produto()
    p1.id = int(input('Id:'))
    p1.descricao = input('Descrição: ')
    p1.preco = float(input('Preço: '))
    p1.quantidade = int(input('Quantidade: '))
    return p1


if __name__ == '__main__':

    print('## Cadastro de Produtos ##')
    p1 = entrada()
    print(p1)