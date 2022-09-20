Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 5
b = 5
c =a+b
c
10
t=10
y=16
z=t+y
z
26
print
<built-in function print>
print('hello world')
hello world
print ('mejor')
mejor
c = a-a
c
0
c*c
0
c= a*a
c=a/a
c
1.0
print('soma:',1+2)
soma: 3
print('subtração:',3-1)
subtração: 2
c=4/3
c
1.3333333333333333
c=4//3
c
1
9%2
1
#jogo da velha para comentario
2**3
8
#2 elevado a 3
import math
math.pi
3.141592653589793
math 4
SyntaxError: invalid syntax
math.4
SyntaxError: invalid syntax
math.sqrt 16
SyntaxError: invalid syntax
math.sqrt(16)
4.0
math.sqrt(16)
4.0
math.sqrt(16)
4.0
math.pow(2,3)
8.0
c=1.9//2
c
0.0
#RELACIONAL
3<5
True
5>3
True
3>5
False
---------
SyntaxError: invalid syntax
5<=5
True
MI=10
pa=20
mi+pa
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    mi+pa
NameError: name 'mi' is not defined. Did you mean: 'MI'?
mipa
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    mipa
NameError: name 'mipa' is not defined
5 !=6
True
#igualdade
"uva"=="uva"
True
#!= ---diferença
nome = 'Pablo'
print(nome)
Pablo
print('Boa noite',nome)
Boa noite Pablo
print('Boa noite %s',nome)
Boa noite %s Pablo
print('Boa noite %s' % nome)
Boa noite Pablo
print('Boa noite %s. Bem vindo' % nome)
Boa noite Pablo. Bem vindo
fruta='banana'
preco=1.99
print('\n%s=%.2f' % (fruta,preco))

banana=1.99
print('\ns=%.2f' % (fruta,preco))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print('\ns=%.2f' % (fruta,preco))
TypeError: must be real number, not str
print('\n\n\n\n\n\n\n)
      
SyntaxError: unterminated string literal (detected at line 1)
print('\n\n\n\n\n\n\n')
      








a=true
      
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
a = True
      
b = False
      
a and b
      
False
b = True
      
a and b
      
True
a or b
      
True
not a
      
False
not b
      
False
a
      
True
b
      
True
a and b
      
True
b = False
      
a and b
      
False
a or b
      
True
not b
      
True
chover = True
      
terGuardaChuva = True
      
if chover and terGuardaChuva:
      print('não se molhar')

    
não se molhar

================================================== RESTART: D:/Curso Python Pablo/atv 1.py ==================================================
não vai se molhar

================================================== RESTART: D:/Curso Python Pablo/atv 1.py ==================================================
vai se molhar

================================================== RESTART: D:/Curso Python Pablo/atv 1.py ==================================================
vai se molhar

================================================== RESTART: D:/Curso Python Pablo/atv 1.py ==================================================
não vai se molhar

================================================== RESTART: D:/Curso Python Pablo/atv 1.py ==================================================
não vai se molhar

================================================== RESTART: D:/Curso Python Pablo/atv 1.py ==================================================
não vai se molhar
print('\n\n\n\n\n\n\n')
      








lista=[1,2,3,4,5]
      
lista = ['joao', 'mi', 'Pablo']
      
lista = [1,2,3.14,'laranja']
      
lista = [[1,2,3], [4,5], [ 'carro']]
      
lista
      
[[1, 2, 3], [4, 5], ['carro']]
len(lista)
      
3
lista[0]
      
[1, 2, 3]
lista[1]
      
[4, 5]
lista[2]
      
['carro']
lista [2] [0]
      
'carro'
lista[1] [0]
      
4
