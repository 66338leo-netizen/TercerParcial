import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

archivo = "pedidos.txt"

app = ctk.CTk()
app.geometry("900x520")
app.title("Practica Pizzas")
nombre = ctk.StringVar()
direccion = ctk.StringVar()
telefono = ctk.StringVar()
num_pizzas = ctk.StringVar()

tamano = ctk.StringVar(value="Chica")

ing_jamon = ctk.IntVar()
ing_pina = ctk.IntVar()
ing_champ = ctk.IntVar()

precios = {"Chica":40, "Mediana":80, "Grande":120}

pedido_actual = []

def obtener_ingredientes():
    lista = []
    if ing_jamon.get(): lista.append("Jamon")
    if ing_pina.get(): lista.append("Piña")
    if ing_champ.get(): lista.append("Champiñones")
    return ",".join(lista)

def calcular_subtotal():
    try:
        cantidad = int(num_pizzas.get())
    except:
        return 0

    precio = precios[tamano.get()]
    extras = (ing_jamon.get() + ing_pina.get() + ing_champ.get()) * 10
    return (precio + extras) * cantidad

def agregar():
    if nombre.get() == "" or num_pizzas.get() == "":
        messagebox.showwarning("Error","Faltan datos")
        return

    subtotal = calcular_subtotal()

    datos = (
        tamano.get(),
        obtener_ingredientes(),
        int(num_pizzas.get()),
        subtotal
    )

    pedido_actual.append(datos)

    tabla.insert("", "end", values=datos)

def quitar():
    seleccion = tabla.selection()
    if seleccion:
        index = tabla.index(seleccion)
        tabla.delete(seleccion)
        pedido_actual.pop(index)

def terminar():
    if not pedido_actual:
        messagebox.showwarning("Error", "No hay pedidos")
        return

    total_actual = sum(item[3] for item in pedido_actual)

    fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(archivo, "a") as f:
        f.write(f"\n--- Pedido ---\n")
        f.write(f"Cliente: {nombre.get()}\n")
        f.write(f"Direccion: {direccion.get()}\n")
        f.write(f"Telefono: {telefono.get()}\n")
        f.write(f"Fecha: {fecha}\n")
        for item in pedido_actual:
            f.write(f"{item}\n")
        f.write(f"Total: {total_actual}\n")

    messagebox.showinfo("Total", f"Total a pagar: ${total_actual}")
    texto = ""
    total_dia = 0

    try:
        with open(archivo, "r") as f:
            for linea in f:
                if "Total:" in linea:
                    monto = int(linea.strip().split(":")[1])
                    total_dia += monto
                    texto += f"{linea}"
    except:
        pass

    texto += f"\nVentas totales del día: ${total_dia}"
    label_ventas.configure(text=texto)

    pedido_actual.clear()
    tabla.delete(*tabla.get_children())

frame_top = ctk.CTkFrame(app, width=860, height=100)
frame_top.place(x=20, y=20)

frame_opciones = ctk.CTkFrame(app, width=530, height=150)
frame_opciones.place(x=20, y=130)

frame_tabla = ctk.CTkFrame(app, width=520, height=200)
frame_tabla.place(x=20, y=300)

frame_ventas = ctk.CTkFrame(app, width=300, height=360)
frame_ventas.place(x=560, y=130)
ctk.CTkLabel(frame_top, text="Nombre").place(x=20,y=20)
ctk.CTkEntry(frame_top, textvariable=nombre, width=150).place(x=90,y=20)

ctk.CTkLabel(frame_top, text="Dirección").place(x=260,y=20)
ctk.CTkEntry(frame_top, textvariable=direccion, width=150).place(x=330,y=20)

ctk.CTkLabel(frame_top, text="Teléfono").place(x=520,y=20)
ctk.CTkEntry(frame_top, textvariable=telefono, width=150).place(x=590,y=20)

ctk.CTkLabel(frame_opciones, text="Tamaño Pizza").place(x=20,y=10)

ctk.CTkRadioButton(frame_opciones,text="Chica $40",variable=tamano,value="Chica").place(x=20,y=40)
ctk.CTkRadioButton(frame_opciones,text="Mediana $80",variable=tamano,value="Mediana").place(x=20,y=70)
ctk.CTkRadioButton(frame_opciones,text="Grande $120",variable=tamano,value="Grande").place(x=20,y=100)

ctk.CTkLabel(frame_opciones, text="Ingredientes").place(x=180,y=10)

ctk.CTkCheckBox(frame_opciones,text="Jamon $10",variable=ing_jamon).place(x=180,y=40)
ctk.CTkCheckBox(frame_opciones,text="Piña $10",variable=ing_pina).place(x=180,y=70)
ctk.CTkCheckBox(frame_opciones,text="Champiñones $10",variable=ing_champ).place(x=180,y=100)
ctk.CTkLabel(frame_opciones, text="Num. Pizzas").place(x=360,y=40)
ctk.CTkEntry(frame_opciones, textvariable=num_pizzas, width=60).place(x=360,y=70)
ctk.CTkButton(frame_opciones,text="Agregar", command=agregar).place(x=360,y=110)

tabla = ttk.Treeview(frame_tabla, columns=("tam","ing","num","sub"), show="headings")
tabla.heading("tam", text="Tamaño")
tabla.heading("ing", text="Ingredientes")
tabla.heading("num", text="Num")
tabla.heading("sub", text="Subtotal")

tabla.place(x=10, y=10, width=800, height=150)

ctk.CTkButton(frame_tabla,text="Quitar", command=quitar).place(x=100,y=170)
ctk.CTkButton(frame_tabla,text="Terminar", command=terminar).place(x=300,y=170)
ctk.CTkLabel(frame_ventas, text="Ventas del día").place(x=80,y=10)
label_ventas = ctk.CTkLabel(frame_ventas, text="", justify="left")
label_ventas.place(x=20, y=50)

app.mainloop()