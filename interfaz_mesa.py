from tkinter import Tk, StringVar
from tkinter.ttk import Label, Combobox, Button

root = Tk()
root.geometry('450x250')

bebida = {'Cafe': 1.20, 'Zumo': 2.20, 'Leche': 1.20, 'Agua': 0.50, 'Nestea': 2}
comanda_bebida = {}

tapas = {'Papas': 2.30, 'Gambas': 3, 'Chocos': 2.50, 'Hamburguesa': 3, 'Nachos': 4}
comanda_tapas = {}


def check_bebidas():  # For checking the value of ComboBox
    global carta_bebida
    carta_bebida = var_drink.get()
    label_drink_price.config(text='Precio: ' + str(bebida[carta_bebida]) + ' €')


def check_tapas():  # For checking the value of ComboBox
    global carta_tapas
    carta_tapas = var_food.get()
    label_tapas_price.config(text='Precio: ' + str(tapas[carta_tapas]) + ' €')


def comprobar_bebidas():
    global lista_bebidas
    lista_bebidas = list(comanda_bebida)
    if carta_bebida in lista_bebidas:
        comanda_bebida[carta_bebida] += 1
    else:
        comanda_bebida[carta_bebida] = 1

    label_lista_drink.config(text=str(comanda_bebida))


def comprobar_tapas():
    global lista_tapas
    lista_tapas = list(comanda_tapas)
    if carta_tapas in lista_tapas:
        comanda_tapas[carta_tapas] += 1
    else:
        comanda_tapas[carta_tapas] = 1

    label_lista_food.config(text=str(comanda_tapas))


# Función para enviar
def enviar():
    a = list(comanda_bebida)
    b = list(comanda_bebida.values())
    c = list(comanda_tapas)
    d = list(comanda_tapas.values())
    e = ''
    f = ''
    for i in range(len(a)):
        e += a[i] + ' : ' + str(b[i]) + '\n'

    for i in range(len(c)):
        f += c[i] + ' : ' + str(d[i]) + '\n'

    print(e, f)


# Funcion para borrar

def borrar():
    global comanda_bebida
    global comanda_tapas
    comanda_bebida = {}
    comanda_tapas = {}

    label_lista_drink.config(text='   ')
    label_lista_food.config(text='  ')


# LAS ETIQUETAS DE LAS COSAS
lbl_titulo = Label(root, text='BEBIDAS')
lbl_titulo.grid(row=0, column=0)

lbl_titulo1 = Label(root, text='TAPAS')
lbl_titulo1.grid(row=0, column=1, padx=30)

# LOS DOS COMBOBOX
var_drink = StringVar()  # To store the value of the Combobox
combo_drink = Combobox(root, values=list(bebida), textvariable=var_drink)
combo_drink.grid(row=1, column=0, pady=10)

var_food = StringVar()  # To store the value of the Combobox
combo_food = Combobox(root, values=list(tapas), textvariable=var_food)
combo_food.grid(row=1, column=1, pady=10)

# ETIQUETAS DE PRECIOS
label_drink_price = Label(root)
label_drink_price.grid(row=2, column=0)

label_tapas_price = Label(root)
label_tapas_price.grid(row=2, column=1)

# DOS BOTONES PARA CONFIRMAR LO QUE ELIGEN
btn_drink = Button(root, text="Confirmar Bebida", command=comprobar_bebidas)
btn_drink.grid(row=3, column=0, pady=15)

btn_food = Button(root, text="Confirmar Tapas", command=comprobar_tapas)
btn_food.grid(row=3, column=1, pady=15)

# BOTONES PARA BORRAR Y ENVIAR

btn_borrar = Button(root, text="Borrar", command=borrar)
btn_borrar.grid(row=6, column=0, pady=15)

btn_enviar = Button(root, text="ENVIAR", command=enviar)
btn_enviar.grid(row=6, column=1, pady=15)

# ETIQUETAS PARA VER LAS LISTAS DE LOS PEDIDOS
label_lista_drink = Label(root)
label_lista_drink.grid(row=4, column=0, columnspan=2)

label_lista_food = Label(root)
label_lista_food.grid(row=5, column=0, columnspan=2)

combo_drink.bind("<<ComboboxSelected>>", lambda event: check_bebidas())

combo_food.bind("<<ComboboxSelected>>", lambda event: check_tapas())

root.mainloop()
