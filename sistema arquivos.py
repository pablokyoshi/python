#sistemas_arquivos.py:
#os.path.basename(arq) = apenas o arquivo
#os.path.dirname() = apenas o caminho
#os.path.exist() = se existe true or false
#os.path.getsize() = tamanho em bytes

import os.path
import glob

lista = sorted(glob.glob('c:\\windows\\*'))
for arq in lista:
    print(os.path.getsize(arq))
