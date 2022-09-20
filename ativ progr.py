qlinhas= int (input('Digite q quantidade de linhas:'))
qcolunas = int(input('Digite a quantidade de colunas:'))

matriz=3
linhas=[matriz] * qcolunas
matriz = [linhas] *qlinhas
soma=0
for lin in matriz:
    soma+=sum(lin)
print (soma)
