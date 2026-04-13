import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

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
        label_img.config(image=img)
        label_img.image = img
    except:
        label_img.config(text="Sin imagen")

def ingresar():
    global total
    try:
        m = float(entry.get())
        if m not in [0.5,1,2,5,10]:
            messagebox.showerror("Error","Moneda no válida")
            return
        total += m
        label_dinero.config(text=f"$ {total}")
        entry.delete(0, tk.END)
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

    label_dinero.config(text="$ 0")
    label_cambio.config(text=f"Cambio: $ {cambio}")

    actualizar_lista()

    # ventana compra
    win = tk.Toplevel(root)
    tk.Label(win,text="GRACIAS POR SU COMPRA").pack()
    tk.Label(win,text=f"Cambio: {cambio}").pack()

    try:
        img = Image.open(refrescos[r]["img"]).resize((100,180))
        img = ImageTk.PhotoImage(img)
        l = tk.Label(win,image=img)
        l.image = img
        l.pack()
    except:
        pass

    tk.Button(win,text="OK",command=win.destroy).pack()

def actualizar_lista():
    for r in refrescos:
        botones[r].config(text=f"{r} {refrescos[r]['stock']}")

def surtir():
    win = tk.Toplevel(root)

    tk.Label(win,text="Refresco").pack()
    var = tk.StringVar(value=list(refrescos.keys())[0])
    tk.OptionMenu(win,var,*refrescos.keys()).pack()

    tk.Label(win,text="Cantidad").pack()
    e = tk.Entry(win)
    e.pack()

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

    tk.Button(win,text="OK",command=aplicar).pack()

root = tk.Tk()
root.geometry("650x500")

menu = tk.Menu(root)
op = tk.Menu(menu, tearoff=0)
op.add_command(label="Surtir", command=surtir)
menu.add_cascade(label="Opciones", menu=op)
root.config(menu=menu)

tk.Label(root,text="0.5,1,2,5,10").place(x=20,y=10)

label_dinero = tk.Label(root,text="$ 0")
label_dinero.place(x=250,y=10)

entry = tk.Entry(root)
entry.place(x=100,y=40)

tk.Button(root,text="Ingresar",command=ingresar).place(x=250,y=38)

label_cambio = tk.Label(root,text="Cambio: $ 0")
label_cambio.place(x=200,y=80)
seleccion = tk.StringVar()

botones = {}
for i,r in enumerate(refrescos):
    rb = tk.Radiobutton(root,text=f"{r} {refrescos[r]['stock']}",
                        variable=seleccion,value=r,
                        command=mostrar_imagen)
    rb.place(x=50,y=150+i*30)
    botones[r] = rb

label_img = tk.Label(root)
label_img.place(x=350,y=150)

tk.Button(root,text="Tomar Refresco",command=comprar).place(x=200,y=400)
root.mainloop()