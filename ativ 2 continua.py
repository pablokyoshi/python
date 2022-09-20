Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============
Traceback (most recent call last):
  File "D:/Curso Python Pablo/aula 2/tela 1.py", line 12, in <module>
    botao=tk.Button(janela,text="Sair", height=5,wigth=35)
  File "C:\Users\PC 203\AppData\Local\Programs\Python\Python310\lib\tkinter\__init__.py", line 2679, in __init__
    Widget.__init__(self, master, 'button', cnf, kw)
  File "C:\Users\PC 203\AppData\Local\Programs\Python\Python310\lib\tkinter\__init__.py", line 2601, in __init__
    self.tk.call(
_tkinter.TclError: unknown option "-wigth"

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

================ RESTART: D:/Curso Python Pablo/aula 2/tela 1.py ===============

frutas=['banana','laranja','uva']instância
janela=tk.Tk()
#Adiciona um título
janela.title("Bem vindo ao Tkinter")

texto=tk.Label(janela, text=("Este é um Label"),font=("Arial Bold",200))
texto.grid(column=0,row=0)

botao=tk.Button(janela,text='Sair', height=5,width=35, command=janela.destroy)
botao.grid(column=0, row=1)


janela.geometry('1960x500')


#Inicia GUI
janela.mainloop()


frutas=['banana','laranja','uva']instância
janela=tk.Tk()
#Adiciona um título
janela.title("Bem vindo ao Tkinter")

texto=tk.Label(janela, text=("Este é um Label"),font=("Arial Bold",200))
texto.grid(column=0,row=0)

botao=tk.Button(janela,text='Sair', height=5,width=35, command=janela.destroy)
botao.grid(column=0, row=1)


janela.geometry('1960x500')


#Inicia GUI
janela.mainloop()
SyntaxError: invalid syntax





































































frutas = ['banana','laranja','uva']
frutas[0]
'banana'
frutas[1]
'laranja'
frutas[2]
'uva'
range(10)
range(0, 10)
numeros=[0,1,2,3,4,5,6,7,8,9]
len(numeros)
10
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in lista:
    print(x)

    
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    for n in lista:
NameError: name 'lista' is not defined. Did you mean: 'list'?
for n in numeros:
    print(x)

Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    print(x)
NameError: name 'x' is not defined
for n in numeros:
    print(n)

0
1
2
3
4
5
6
7
8
9

frutas
['banana', 'laranja', 'uva']
for n in frutas:
    print(x)

Traceback (most recent call last):
  File "<pyshell#47>", line 2, in <module>
    print(x)
NameError: name 'x' is not defined
for n in frutas:
    print(n)

banana
laranja
uva
range(0,10)
range(0, 10)
for n in range(10):
    print(n)

0
1
2
3
4
5
6
7
8
9
for x in range(10):
    print(x)

0
1
2
3
4
5
6
7
8
9
fpr x in range (100):
SyntaxError: invalid syntax
    for x in range (100):
SyntaxError: unexpected indent
for x in range (100):
    print(100)

100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
for x in range (100):
    print(x)

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
ascii(65)
'65'










ord('A')
65
ord('mi')
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    ord('mi')
TypeError: ord() expected a character, but string of length 2 found
ord('m')
109
ord('z')
122
ord('Z')
90
chr(90)
'Z'
range(65,90)
range(65, 90)
range(65,91)
range(65, 91)
for x in range(65,91):
    print(x)

65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
for x in range(65,91)
SyntaxError: expected ':'

for x in range(65,91):
    print(chr(x))

A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
for x in range(97,123):
    print(chr(x))

a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
for x in range(65,91):
    print(chr(x)),end='')
    
SyntaxError: unmatched ')'
for x in range(65,91):
    print(chr(x),end='')

    
ABCDEFGHIJKLMNOPQRSTUVWXYZ
for x in range(65,91):
    print(chr(x),end='   ')

    
A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   
for x in range(65,91):
    print(chr(x),end=' x x ')

    
A x x B x x C x x D x x E x x F x x G x x H x x I x x J x x K x x L x x M x x N x x O x x P x x Q x x R x x S x x T x x U x x V x x W x x X x x Y x x Z x x 
for x in range(65,91,97,123):
    print(chr(x),end='   ')

    
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    for x in range(65,91,97,123):
TypeError: range expected at most 3 arguments, got 4
for x in range(65,123):
    print(chr(x),end='   ')

    
A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   [   \   ]   ^   _   `   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z   
import time

for x in range(65,123):
    print(chr(x),end='   ')

    
A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   [   \   ]   ^   _   `   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z   
for x in range(65,123):
    print(chr(x),end='   ')
    time.sleep(0.5)

    
A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   [   \   ]   ^   _   `   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z   
for x in range(65,91):
    for x in range (97,123):
    print(chr(x),end='   ')
    time.sleep(0.1)
    
SyntaxError: expected an indented block after 'for' statement on line 2
for x in range(65,91):
    for x in range (97,123):
    print(chr(x),end='   ')
    time.sleep(0.1)
    
SyntaxError: expected an indented block after 'for' statement on line 2
for x in range(65,123):
    print(chr(x),end='   ')
    time.sleep(1)

    
A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   [   \   ]   ^   _   `   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z   
import random

random.randrange(1,101)
44

random.randrange(1,101)
65
random.randrange(1,101)
4
random.randrange(1,101)
63
random.randrange(100,101)
100
for in range(10):
    
SyntaxError: invalid syntax

for in range(10):
    
SyntaxError: invalid syntax
print(random.randrange(1,101))for in range(10):
    
SyntaxError: invalid syntax
for in range(10):
    
SyntaxError: invalid syntax
for in range(10):
    
SyntaxError: invalid syntax
for in range(10): print(random.randrange(1,101))
SyntaxError: invalid syntax
for in range(10):
    
SyntaxError: invalid syntax
for x in range(10):
    print(random.randrange(1,101))

    
50
2
96
83
81
61
96
81
64
51
for x in range(10):
    print(random.randrange(65,91))

    
87
81
80
77
86
87
76
83
87
71
for x in range(10):
    num=random.randrange(65,91)
    print(letra)

    
Traceback (most recent call last):
  File "<pyshell#138>", line 3, in <module>
    print(letra)
NameError: name 'letra' is not defined
for x in range(10):
    num=random.randrange(65,91)
    letra=chr(num)
    print(letra)

    
Y
L
A
I
C
J
B
H
L
B

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================
GUXPJBDEWH

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================
YaQhHgUaNh
#ponto flutuante= float = decimal ex:12.20

lista=['10',10,10.3,'aaa','ola']
a=5
lista[2]
10.3
lista[4]
'ola'
lista[0]
'10'
for x in lista:
        print (x)

        
10
10
10.3
aaa
ola
for in lista:
    
SyntaxError: invalid syntax
    for x in lista:
        
SyntaxError: unexpected indent
for x in lista:
    print(x)

    
10
10
10.3
aaa
ola
lista=['php','python','java']
for x in lista:
    print(x)

    
php
python
java
lista.append('cc++')
lista.append('react')
lista
['php', 'python', 'java', 'cc++', 'react']
length(lista)
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    length(lista)
NameError: name 'length' is not defined
len(lista)
5
lista.count('java')
1
'php' in lista
True
'cloujure'not in lista
True
'php' not in lista
False
del (lista[3])

lista
['php', 'python', 'java', 'react']
lista.index('react')
3
valores=[1,2,3,4,5]
for x in valores:
    print(x)

    
1
2
3
4
5
for x in valores:
    print(x)*2

    
1
Traceback (most recent call last):
  File "<pyshell#178>", line 2, in <module>
    print(x)*2
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
for x in valores:
    print((x)*(2))

    
2
4
6
8
10
#list compregension
#list compregension
print(x*2 for x in valores)
<generator object <genexpr> at 0x000001E0FB2D6960>
print([x*2 for x in valores])
[2, 4, 6, 8, 10]
valores
[1, 2, 3, 4, 5]
for x in valores:
    print(x)

    
1
2
3
4
5
lista=[1,2,3,4,5]
tupla=(1,2,3,4,5)

#tupla é imutavel, nao da para adicionar nem retirar, lista pode


#tupla é imutavel, nao da para adicionar nem retirar, lista pode conferir

for x in tupla:
        print(x)

        
1
2
3
4
5
for x in tupla:
        lista.append(x)

        
lista
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
tuple(lista)
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
list(tupla)
[1, 2, 3, 4, 5]
tuple
<class 'tuple'>
tupla
(1, 2, 3, 4, 5)
lista
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
del[6,7,8,9]
SyntaxError: cannot delete literal
del[6]
SyntaxError: cannot delete literal
del[lista(6,7,8,9)]
SyntaxError: cannot delete function call
del[lista(6)]
SyntaxError: cannot delete function call
del(lista[6,7,8,9])
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    del(lista[6,7,8,9])
TypeError: list indices must be integers or slices, not tuple
Traceback (most recent call last):
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
del(lista[6])
del(lista[67])
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    del(lista[67])
IndexError: list assignment index out of range
del(lista[7])
del(lista[8])
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    del(lista[8])
IndexError: list assignment index out of range
lista
[1, 2, 3, 4, 5, 1, 3, 5]
del(lista[6])
del(lista[6])
lista
[1, 2, 3, 4, 5, 1]
del(lista[6])
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    del(lista[6])
IndexError: list assignment index out of range
del(lista[5])
lista
[1, 2, 3, 4, 5]
input('Digite seu nome')
Digite seu nome Plabo
' Plabo'
nome=input('Digite seu nome: ')
Digite seu nome: Plabo Koloshi
nome
'Plabo Koloshi'
nome
'Plabo Koloshi'
for x in nome:
    print(x, end=' ')

    
P l a b o   K o l o s h i 

import turtle

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================
Traceback (most recent call last):
  File "D:/Curso Python Pablo/aula 2/ativ 2.py", line 5, in <module>
    p.bgcolor('black')
AttributeError: type object 'Turtle' has no attribute 'bgcolor'. Did you mean: '_color'?

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================
Traceback (most recent call last):
  File "D:/Curso Python Pablo/aula 2/ativ 2.py", line 4, in <module>
    p.speed(0)
  File "C:\Users\PC 203\AppData\Local\Programs\Python\Python310\lib\turtle.py", line 2168, in speed
    return self._speed
AttributeError: 'int' object has no attribute '_speed'

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================
Traceback (most recent call last):
  File "D:/Curso Python Pablo/aula 2/ativ 2.py", line 13, in <module>
    t.left(90)
NameError: name 't' is not defined

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================
Traceback (most recent call last):
  File "D:/Curso Python Pablo/aula 2/ativ 2.py", line 10, in <module>
    cor=cores[resto]
IndexError: list index out of range

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================

============================================================================================ RESTART: D:/Curso Python Pablo/aula 2/ativ 2.py ===========================================================================================
