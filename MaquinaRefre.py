import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

refrescos = {
    "Aurrera": {"precio": 5, "stock": 5, "img": "aurrera.jpeg"},
    "Coca": {"precio": 8, "stock": 8, "img": "cocacola.jpeg"},
    "Fanta": {"precio": 5, "stock": 5, "img": "fanta.jpeg"},
    "Mexicanada": {"precio": 6, "stock": 5, "img": "mexicanada.jpeg"},
    "Pepsi": {"precio": 5, "stock": 5, "img": "pepsi.jpeg"},
    "Sprit": {"precio": 5, "stock": 5, "img": "sprit.jpeg"}
}

total = 0

def mostrar_imagen():
    r = seleccion.get()
    try:
        img = Image.open(refrescos[r]["img"]).resize((120,200))
        img = ImageTk.PhotoImage(img)
        label_img.configure(image=img, text="")
        label_img.image = img
    except:
        label_img.configure(text="Sin imagen", image=None)

def ingresar():
    global total
    try:
        m = float(entry.get())
        if m not in [0.5,1,2,5,10]:
            messagebox.showerror("Error","Moneda no válida")
            return
        total += m
        label_dinero.configure(text=f"$ {total}")
        entry.delete(0, "end")
    except:
        messagebox.showerror("Error","Valor inválido")

def comprar():
    global total
    r = seleccion.get()

    if r == "":
        messagebox.showerror("Error","Selecciona refresco")
        return

    precio = refrescos[r]["precio"]

    if total < precio:
        messagebox.showerror("Error","Dinero insuficiente")
        return

    if refrescos[r]["stock"] <= 0:
        messagebox.showerror("Error","Sin stock")
        return

    refrescos[r]["stock"] -= 1
    cambio = total - precio
    total = 0

    label_dinero.configure(text="$ 0")
    label_cambio.configure(text=f"Cambio: $ {cambio}")

    actualizar_lista()

    win = ctk.CTkToplevel(root)
    win.geometry("250x300")

    ctk.CTkLabel(win, text="GRACIAS POR SU COMPRA").pack(pady=10)
    ctk.CTkLabel(win, text=f"Cambio: {cambio}").pack()

    try:
        img = Image.open(refrescos[r]["img"]).resize((100,180))
        img = ImageTk.PhotoImage(img)
        l = ctk.CTkLabel(win, image=img, text="")
        l.image = img
        l.pack(pady=10)
    except:
        pass

    ctk.CTkButton(win, text="OK", command=win.destroy).pack(pady=10)

def actualizar_lista():
    for r in refrescos:
        botones[r].configure(text=f"{r} {refrescos[r]['stock']}")

def surtir():
    win = ctk.CTkToplevel(root)
    win.geometry("300x250")

    ctk.CTkLabel(win, text="Refresco").pack(pady=5)

    var = ctk.StringVar(value=list(refrescos.keys())[0])
    menu = ctk.CTkOptionMenu(win, variable=var, values=list(refrescos.keys()))
    menu.pack(pady=5)

    ctk.CTkLabel(win, text="Cantidad").pack(pady=5)
    e = ctk.CTkEntry(win)
    e.pack(pady=5)

    def aplicar():
        try:
            c = int(e.get())
            if c < 0:
                messagebox.showerror("Error","No negativos")
                return
            refrescos[var.get()]["stock"] += c
            actualizar_lista()
            win.destroy()
        except:
            messagebox.showerror("Error","Valor inválido")

    ctk.CTkButton(win, text="OK", command=aplicar).pack(pady=10)

# Ventana principal
root = ctk.CTk()
root.geometry("650x500")

ctk.CTkLabel(root, text="0.5,1,2,5,10").place(x=20,y=10)

label_dinero = ctk.CTkLabel(root, text="$ 0")
label_dinero.place(x=250,y=10)

entry = ctk.CTkEntry(root)
entry.place(x=100,y=40)

ctk.CTkButton(root, text="Ingresar", command=ingresar).place(x=250,y=38)

label_cambio = ctk.CTkLabel(root, text="Cambio: $ 0")
label_cambio.place(x=200,y=80)

seleccion = ctk.StringVar()

botones = {}
for i, r in enumerate(refrescos):
    rb = ctk.CTkRadioButton(root,
                            text=f"{r} {refrescos[r]['stock']}",
                            variable=seleccion,
                            value=r,
                            command=mostrar_imagen)
    rb.place(x=50,y=150+i*30)
    botones[r] = rb

label_img = ctk.CTkLabel(root, text="")
label_img.place(x=350,y=150)

ctk.CTkButton(root, text="Tomar Refresco", command=comprar).place(x=200,y=400)

# Botón para surtir (porque customtkinter no usa menú clásico igual)
ctk.CTkButton(root, text="Surtir", command=surtir).place(x=500,y=10)

root.mainloop()