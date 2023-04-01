from tkinter import *

#funciones
def cargar(num):
    global dato1
    global dato2
    global bot
    if dato1 == None:
        dato1 = num
        print("dato1",dato1)
    else:
        dato2 = num
        print("dato2",dato2)


def sumar():
    global dato1
    global dato2
    if  (dato1 != None and dato2 != None):
        resultado.set(dato1+dato2)
        dato1 = None
        dato2 = None

def resta():
    global dato1
    global dato2
    if  (dato1 != None and dato2 != None):
        resultado.set(dato1-dato2)
        dato1 = None
        dato2 = None

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

bot = Button(ventana, width=15, text=1, command= lambda: cargar(1))
bot.grid(padx=5, pady=5, row=2, column=0)
bot = Button(ventana, width=15, text=2, command= lambda: cargar(2))
bot.grid(padx=5, pady=5, row=2, column=1)
bot = Button(ventana, width=15, text=3, command= lambda: cargar(3))
bot.grid(padx=5, pady=5, row=2, column=2)

bot = Button(ventana, width=15, text=4, command= lambda: cargar(4))
bot.grid(padx=5, pady=5, row=3, column=0)
bot = Button(ventana, width=15, text=5, command= lambda: cargar(5))
bot.grid(padx=5, pady=5, row=3, column=1)
bot = Button(ventana, width=15, text=6, command= lambda: cargar(6))
bot.grid(padx=5, pady=5, row=3, column=2)

bot = Button(ventana, width=15, text=7, command= lambda: cargar(7))
bot.grid(padx=5, pady=5, row=4, column=0)
bot = Button(ventana, width=15, text=8, command= lambda: cargar(8))
bot.grid(padx=5, pady=5, row=4, column=1)
bot = Button(ventana, width=15, text=9, command= lambda: cargar(9))
bot.grid(padx=5, pady=5, row=4, column=2)

"""
num=1    
for fila in range(2,5):
    for columna in range(0,3):
        bot = Button(ventana, width=15, text=f"{num}", command= lambda: cargar(num))
        bot.grid(padx=5, pady=5, row=fila, column=columna)
        num +=1
"""
botSuma=Button(ventana, text="+", command= lambda: sumar() , width=15)
botSuma.grid(padx=5, pady=5, row=5, column=0)

bot = Button(ventana, width=15, text=0, command= lambda: cargar(0))
bot.grid(padx=5, pady=5, row=5, column=1)

botResta=Button(ventana, text="-", command= lambda: resta() , width=15)
botResta.grid(padx=5, pady=5, row=5, column=2)


 
ventana.mainloop()