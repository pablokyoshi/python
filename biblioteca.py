#leitor_csv

#biblioteca para leitura de arquivo .csv do excel
import csv


def gravar_csv():
    tabela=(('PRODUTO', 'UNIDADE','PREÇO UNITARIO','QUANTIDADE ESTOQUE', 'VALOR TOTAL'),
            ('Açucar', '2kg', 3.59, 10, 35.90),
            ('Biscoitor', '200gr', 1.19, 10, 11.90),

            )
    #criar arquivo para gravação
    saida=csv.writer(open('tabela.csv', 'w', newline=''))

    #escreve as tuplas no arquivo
    saida.writerows(tabela)

if(__name__=='__main__'):
    gravar_csv()
