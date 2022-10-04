class Conta:

    #define o construtor
    def __init__(self,numero,titular,saldo,limite):
        self.__numero=numero
        self.__titular= titular
        #variavel privado (__saldo)
        self.__saldo=saldo
        self.__limite=limite


    def __str__(self):
        #str nao usa print, print no main
        return f'\nExtrato bancário: \nTitular: {self.__titular} \nSaldo: R$ {self.__saldo}'
        #print('Extrato bancário:')
        #print('Número: {}\n'.format(self.numero), ('Titular: {}'.format(self.titular)))
        #print('Titular: {}' .format(self.titular))
        #print('Saldo: {}'.format(self.saldo))
        #print('Limite: {}'.format(self.limite))

    def depositar(self,saldo):
        self.__saldo +=  saldo

    def sacar(self, valor):
        if(self.__saldo+self.__limite)>= valor:
            self.__saldo-=valor

    def transferirPara(self,contaDestino, valor):
        self.sacar(valor)
        contaDestino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def numero(self):
        return self.__numero

    @limite.setter
    def limite(self,limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'ITAU':'200', 'CAIXA':'104'}

if __name__ == '__main__':
    contaJoao = Conta(123, 'Joao da Silva', 200,1000)
    contaJoao.depositar(100)

    contaZePedro = Conta(456, 'José Ferreira', 0, 0)
    contaJoao.transferirPara(contaZePedro, 100)

    #contaJoao.sacar(5000)
    #contaJoao.extrato()
    #print(contaJoao)
    #print(contaZePedro)
    #print(contaJoao.titular)
    #print(contaJoao.limite)
    #print(contaJoao.numero)

    contaZePedro.limite=500

    print('\nSaldo R$ ', contaZePedro.saldo)
    print('Limite R$ ', contaZePedro.limite)
    print('Número da conta:', contaZePedro.numero)
    print('Titular da conta:', contaZePedro.titular)
    print('Código do banco: ', Conta.codigos_bancos()['BB'])