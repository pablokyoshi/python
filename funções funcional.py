

#Funções normais

#def  multiplicar(x,y):
#   return x*y

def iguais(x,y):
    #operador ternário
    return "sim" if x==y else "não"
   
#Funções anonimas
multiplicar=lambda x,y:x*y
iguais = lambda x,y: "Sim" if x==y else "Não"


if __name__ == '__main__':
    
    #print(iguais(2,2))
    print(iguais('Sim','sim'))
    #print(multiplicar(2,3))
#Programação funcional
    
