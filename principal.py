#principal.py

from veiculo import Veiculo, Carro, Motocicleta

if __name__ == '__main__':
    veiculo = Veiculo('Marca','Modelo','Placa', 2022)
    veiculo.ligar()
    veiculo.abastecer()
    print(veiculo)

#é um carro e veiculo, polimorfismo de classe
    carro= Carro('WV', 'Polo', 'PYHT -1234',2020)
    carro.ligar()
    carro.abastecer()
    print(carro)

    moto= Motocicleta ('YAMAHA', 'CG', 'MMMM-2334', 2018,6)
    moto.ligar()
    moto.abastecer()
    print(moto)

    lista= [veiculo, carro, moto, 'banana', 123, 1.0]
    for item in lista:
        if (isinstance(item, Motocicleta)):
            print('é um moto')
        elif (isinstance(item, Carro)):
            print('é um carro')
        elif (isinstance(item, Veiculo)):
            print('é um veiculo')
        elif (isinstance(item,str)):
            print('é uma string')
        elif (isinstance(item,int)):
            print('é um inteiro')
        elif (isinstance(item, float)):
            print('é um float')
        else:
            print('tipo desconhecido')
            
