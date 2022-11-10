#vehiculo.py

#classe mãe = super classe
class Veiculo:
    #construtor da classe
    def __init__ (self, marca,modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    #sobescrita de função oultin-- função pronta
    def __str__ (self):
        return 'Veiculo placa:' + self.placa

    def ligar(self):
        print('Veiculo ligado ...')

    def abastecer(self):
        print('Veiculo abastecendo ...')

#classe filha = sub classe
#carro é um veiculo
class Carro(Veiculo):
    def __str__ (self):
        return 'Carro placa: ' +self.placa

    def ligar(self):
        print('Carro ligado ...')

    def abastecer(self):
        print('Carro abastecendo ...')
    

#motocicleta é um veiculo
class Motocicleta(Veiculo):
    def __init__ (self, marca,modelo, placa, ano, cilindrada):
        
        super(). __init__(marca,modelo,placa, ano)
        self.cilindrada= cilindrada
    

    def __str__ (self):
        return f'Moto cilindrada: {self.cilindrada}'



