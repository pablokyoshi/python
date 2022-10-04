#funcional_map.py

#objetivo: converter uma lista de strings para inteiros

lista=['1','3','5','7']
#print(int(lista[0]))
nova_lista=[]
#1.usando loop for
for x in lista:
    nova_lista.append(int(x))
   # print(nova_lista)
    #print(int(x))
print('Ciclo for: ', nova_lista)

#2.usando compreensão de lista(list comprehension)

r=[int(a) for a in lista]
print('List Comprehension: ', nova_lista)

#3. usando map com função nomeada
def converter(x): return int(x)

nova_lista = list(map(converter,lista))
print('map com função:',nova_lista)

#4. usando map com funcção anonima (lambda)
nova_lista = list(map(lambda x: int(x), lista))
print('map com lambda:' , nova_lista)

#4b. Outro exemplo com lambda
lista2 = ['1.0', '3.1', '5.5', '7.7', '8.2']
nova_lista = list(map(lambda x,y: [int(x), float(y)], lista, lista2))
print('ex 1:', nova_lista)

#4c. outro exemplo
numeros = (1,2,3)
resultado = list(map(lambda a: a+a, numeros))
print('ex2:',resultado)

#4d mais um exemplo, soma numeros com numeros2
numeros2 = [4,5,6]
resultado = list(map(lambda a,b: a+b, numeros, numeros2))
print ('ex3:' ,resultado)
