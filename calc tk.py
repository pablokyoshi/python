#calc_tk
import tkinter as tk#Graphics user interface GUI
from tkinter import font,ttk

#inicializa a variavel global erro
erro = False

def verifica_erro():
    global erro
    if erro:
        entrada.set('')
        erro=False
    
def digita(c):
    verifica_erro()
    entrada.set(entrada.get() + c)


def digita0():
    digita('0')
    
def digita1():
    digita('1')
    
def digita2():
    digita('2')
    
def digita3():
    digita('3')
    
def digita4():
    digita('4')
    
def digita5():
    digita('5')
    
def digita6():
    digita('6')
    
def digita7():
    digita('7')
    
def digita8():
    digita('8')
    
def digita9():
    digita('9')

def validar(crc):
    verifica_erro()
    if crc=='-' and not entrada.get():
        entrada.set('-')
    elif entrada.get() and entrada.get()[-1] not in ',-+/x*':
        entrada.set(entrada.get() + crc)
    
def digita_back():
    verifica_erro()
    entrada.set(entrada.get()[0:-1])

def digita_clear():
    verifica_erro()
    entrada.set('')
    
def digita_mult():
    validar('x')

def digita_div():
    validar('/')
    
def digita_menos():
    validar('-')

def digita_igual():
    global erro
    try:
        if entrada.get():
            r = entrada.get().replace(',','.')
            r = entrada.get().replace('x','*')
            r= str(eval(r))
            r=r.replace('.',',')
            entrada.set(r)
    except Exception as e:
        entrada.set("Erro")
        erro=True
        
        
def digita_mais():
    validar('+')

def digita_virg():
    validar(',')

def digita_enter(evento):
    digita_igual()
    
def acao_keypress(evento):
    global erro
    c=evento.char

    if erro:
        entrada.set('')
        erro = False
    try:
        if c=='.':
            c=','
        if c in '0123456789':
            entrada.set(entrada.get() + c)
        elif c == '-' and len (entrada.get())==0:
            entrada.set('-')
        elif c in ',+-/*' and len(entrada.get())>0 and entrada.get() [-1] not in ',+-/*':
            entrada.set(entrada.get() +c)
        elif evento.keycode==8: ##8 é o backspace
            entrada.set(entrada.get()[0:-1])
        elif c=='=':
                r = entrada.get().replace(',','.')
                r = str(eval(r))
                r = r.replace('.',',')
                entrada.set(r)
        elif c =="c":
             entrada.set("")
       
    except Exception as e:
        entrada.set(e)
        erro = True
        
    #elif evento.keycode==61: ##61 é o igual
        #entrada.set(entrada.get()[0:-1])
        

calc = tk.Tk()
calc.title('Calc Tk 1.0')
calc.config(width=245, height=310)
calc.resizable(0,0)

entrada=tk.StringVar()
#visor da calc
visor = ttk.Entry(calc, width=22, textvariable=entrada,
                  justify=tk.RIGHT, font=font.Font(family='Bernard MT Condensed',size=15),
                  state='disable'
                  )
visor.place(x=10,y=10)
visor.focus()

visor.bind('<KeyPress>',acao_keypress)

#Backspace Clear +
btBack = tk.Button(calc, text='Backspace', height=2, width=16, command=digita_back, font=font.Font(family='Bernard MT Condensed',size=10))
btBack.place(x=9,y=60)

btClear = tk.Button(calc, text='C', height=2, width=5, command=digita_clear)
btClear.place (x=130, y=60)

btMais = tk.Button(calc, text='+', height=2, width=5, command=digita_mais)
btMais.place(x=190, y=60)

#7,8,9
bt7 = tk.Button(calc, text='7', height=2, width=5,command=digita7)
bt7.place(x=10, y=110)

bt8 = tk.Button(calc, text='8', height=2, width=5,command=digita8)
bt8.place(x=70, y=110)

bt9 = tk.Button(calc, text='9', height=2, width=5,command=digita9)
bt9.place(x=130, y=110)

btMenos = tk.Button(calc, text='-', height=2, width=5,command=digita_menos)
btMenos.place(x=190, y=110)
##
bt6 = tk.Button(calc, text='6', height=2, width=5,command=digita6)
bt6.place(x=10, y=160)

bt5 = tk.Button(calc, text='5', height=2, width=5,command=digita5)
bt5.place(x=70, y=160)

bt4 = tk.Button(calc, text='4', height=2, width=5,command=digita4)
bt4.place(x=130, y=160)

btX = tk.Button(calc, text='x', height=2, width=5,command=digita_mult)
btX.place(x=190, y=160)
###

bt3 = tk.Button(calc, text='3', height=2, width=5,command=digita3)
bt3.place(x=10, y=210)

bt2 = tk.Button(calc, text='2', height=2, width=5,command=digita2)
bt2.place(x=70, y=210)

bt1 = tk.Button(calc, text='1', height=2, width=5,command=digita1)
bt1.place(x=130, y=210)

btdiv = tk.Button(calc, text='/', height=2, width=5,command=digita_div)
btdiv.place(x=190, y=210)
####

bt0 = tk.Button(calc, text='0', height=2, width=5,command=digita0)
bt0.place(x=10, y=260)

btVirgula= tk.Button(calc, text=',', height=2, width=5,command=digita_virg)
btVirgula.place(x=70, y=260)

btIgual= tk.Button(calc, text='=', height=2, width=14,command=digita_igual)
btIgual.place(x=128, y=260)

calc.bind('<Return>', digita_enter)
calc.mainloop()
