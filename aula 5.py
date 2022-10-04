#arquivo_texto.py

import sys

#podemos abrir um arquivo nos seguintes modos:
#'r'= read = somente para leitura
#'w'= write = somente para gravação, mas apaga o conteúdo existente
#'a'= append = gravação, porém não apaga o conteúdo existente

#tipo de arquivo:
#texto ou binário ('b')

#função para gravar
def gravar():
    frutas = ['banana', 'laranja', 'uva']
#abre arquivopara escrita
    arquivo = open('frutas.txt','w')

    for f in frutas:
        arquivo.write(f+'\n')
        
#fecha arquivo
    arquivo.close()

#função para ler
def ler ():
    arquivo = open('frutas.txt', 'r') #abre o arquivo
    for linha in arquivo: #le cada linha do arquivo
        print(linha, end='')
#fecha arquivo
    arquivo.close()

#função para anexar
def anexar():
    arquivo = open('frutas.txt','a')
    arquivo.write('melancia\n');
    arquivo.write('abacaxi\n');

    #fecha arquivo
    arquivo.close()

    
def ler_csv():
    arquivo = open('california_housing_train.csv') #modo='r'
    i=0
    total=0
    
    for linha in arquivo:
        if(i==0):
            total_colunas=len(linha.split(','))
            
        else:
            valor = linha.split(',')[8]
            total +=float(valor)
            
        i+=1
        
    print('Total de linhas:',i)
    print('Valor media/total:R$ %.2f' % (total/i))
    arquivo.close()

#função principal
if (__name__=='__main__'):
    #gravar()
    #ler()
    #anexar()
    ler_csv()
