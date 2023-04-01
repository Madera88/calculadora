from tkinter import *

#funciones
def cargar(num):
    if(resultado.get() == 0):
        resultado.set(num)
    else:
        aux = resultado.get()
        aux = str(aux)+str(num)
        resultado.set(float(aux))

def sumar():
    global dato1
    global dato2
    global simbolo
    aux = resultado.get()
    if  (dato1 == None ):
        dato1=aux
        simbolo="+"
        resultado.set(0)
    else:
        dato2=aux

def resta():
    global dato1
    global dato2
    global simbolo
    aux = resultado.get()
    if  (dato1 == None ):
        dato1=aux
        simbolo="-"
        resultado.set(0)
    else:
        dato2=aux

def multiplicacion():
    global dato1
    global dato2
    global simbolo
    aux = resultado.get()
    if  (dato1 == None ):
        dato1=aux
        simbolo="*"
        resultado.set(0)
    else:
        dato2=aux

def division():
    global dato1
    global dato2
    global simbolo
    aux = resultado.get()
    if  (dato1 == None ):
        dato1=aux
        simbolo="/"
        resultado.set(0)
    else:
        dato2=aux

def resultadoOperacion():

    global dato1
    global dato2
    global simbolo
    global resultado
    
    if( simbolo =="+"):
        sumar()
        resultado.set(dato1+dato2)
        dato1=None
        dato2=None
    elif( simbolo =="-"):
        resta()
        resultado.set(dato1-dato2)
        dato1=None
        dato2=None
    elif( simbolo =="*"):
        resta()
        resultado.set(dato1*dato2)
        dato1=None
        dato2=None
    elif( simbolo =="/"):
        resta()
        resultado.set(dato1/dato2)
        dato1=None
        dato2=None

def limpiar():
    global dato1
    global dato2
    global simbolo
    global resultado
    dato1 = None
    dato2 = None
    simbolo = None
    resultado.set(0)

    

# creamos la ventana
ventana = Tk()

# Tamaño
ventana.geometry("400x300")
# no modificable
ventana.resizable(0,0)
# titulo
ventana.title("Mi Calculadora")


resultado=IntVar()
dato1 = None
dato2 = None
simbolo = None

display=Label(ventana , width=26, textvariable=resultado)
display.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans",18),
    padx=10,
    pady=10,   
    border=2
)
display.grid(column=0, row=0,columnspan=3, padx=5, pady=5)
Label(ventana).grid(row=1)

#FILA BOTONES 1
bot = Button(ventana, width=15, text=1, command= lambda: cargar(1))
bot.grid(padx=5, pady=5, row=2, column=0)
bot = Button(ventana, width=15, text=2, command= lambda: cargar(2))
bot.grid(padx=5, pady=5, row=2, column=1)
bot = Button(ventana, width=15, text=3, command= lambda: cargar(3))
bot.grid(padx=5, pady=5, row=2, column=2)

#FILA BOTONES 2
bot = Button(ventana, width=15, text=4, command= lambda: cargar(4))
bot.grid(padx=5, pady=5, row=3, column=0)
bot = Button(ventana, width=15, text=5, command= lambda: cargar(5))
bot.grid(padx=5, pady=5, row=3, column=1)
bot = Button(ventana, width=15, text=6, command= lambda: cargar(6))
bot.grid(padx=5, pady=5, row=3, column=2)

#FILA BOTONES 3
bot = Button(ventana, width=15, text=7, command= lambda: cargar(7))
bot.grid(padx=5, pady=5, row=4, column=0)
bot = Button(ventana, width=15, text=8, command= lambda: cargar(8))
bot.grid(padx=5, pady=5, row=4, column=1)
bot = Button(ventana, width=15, text=9, command= lambda: cargar(9))
bot.grid(padx=5, pady=5, row=4, column=2)

#FILA BOTONES 4
botSuma=Button(ventana, text="+", command= lambda: sumar() , width=15)
botSuma.grid(padx=5, pady=5, row=5, column=0)
bot = Button(ventana, width=15, text=0, command= lambda: cargar(0))
bot.grid(padx=5, pady=5, row=5, column=1)
botResta=Button(ventana, text="-", command= lambda: resta() , width=15)
botResta.grid(padx=5, pady=5, row=5, column=2)

#FILA BOTONES 5
botResultado=Button(ventana, text="x", command= lambda: multiplicacion() , width=15)
botResultado.grid(padx=5, pady=5, row=6, column=0)

botResultado=Button(ventana, text="/", command= lambda: division() , width=15)
botResultado.grid(padx=5, pady=5, row=6, column=1)

botResultado=Button(ventana, text="=", command= lambda: resultadoOperacion() , width=15)
botResultado.grid(padx=5, pady=5, row=6, column=2)


botResultado=Button(ventana, text="Borrar", command= lambda: limpiar() , width=15)
botResultado.grid(padx=5, pady=5, row=7, column=1)


 
ventana.mainloop()