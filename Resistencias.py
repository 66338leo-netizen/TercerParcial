import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ----- FUNCION ACTUALIZAR COLORES -----
def actualizar_color(var, label):
    color = var.get()
    if color in colores_hex:
        label.config(bg=colores_hex[color])

# ----- FUNCION CALCULAR -----
def calcular():
    try:
        c1 = lista1.get()
        c2 = lista2.get()
        c3 = lista3.get()
        tol = tolerancia.get()

        if c1 == "Seleccionar" or c2 == "Seleccionar" or c3 == "Seleccionar":
            messagebox.showwarning("Error", "Selecciona todos los colores")
            return

        valor = (colores[c1]*10 + colores[c2]) * multiplicador[c3]

        t = 0.05 if tol == "oro" else 0.10

        maximo = int(valor * (1 + t))
        minimo = int(valor * (1 - t))

        resultado.config(text=f"valor ohm: {valor}\nvalor maximo: {maximo}\nvalor minimo: {minimo}")

    except:
        messagebox.showerror("Error", "Error en cálculo")


# ----- DATOS -----
colores = {
    "negro":0,"cafe":1,"rojo":2,"naranja":3,"amarillo":4,
    "verde":5,"azul":6,"violeta":7,"gris":8,"blanco":9
}

multiplicador = {
    "negro":1,"cafe":10,"rojo":100,"naranja":1000,"amarillo":10000
}

colores_hex = {
    "negro":"black","cafe":"brown","rojo":"red","naranja":"orange",
    "amarillo":"yellow","verde":"green","azul":"blue",
    "violeta":"purple","gris":"gray","blanco":"white"
}

# ----- VENTANA -----
ventana = tk.Tk()
ventana.title("Resistencias")
ventana.geometry("350x600")

# ----- IMAGEN -----
img = Image.open("TablaRes.png")
img = img.resize((250,150))
img = ImageTk.PhotoImage(img)

tk.Label(ventana, image=img).pack(pady=10)

# ----- LISTAS + COLOR -----
frame1 = tk.Frame(ventana)
frame1.pack(pady=5)

lista1 = tk.StringVar(value="Seleccionar")
menu1 = tk.OptionMenu(frame1, lista1, *colores.keys(), command=lambda x: actualizar_color(lista1, color1))
menu1.pack(side="left")

color1 = tk.Label(frame1, width=5, bg="white")
color1.pack(side="left", padx=5)


frame2 = tk.Frame(ventana)
frame2.pack(pady=5)

lista2 = tk.StringVar(value="Seleccionar")
menu2 = tk.OptionMenu(frame2, lista2, *colores.keys(), command=lambda x: actualizar_color(lista2, color2))
menu2.pack(side="left")

color2 = tk.Label(frame2, width=5, bg="white")
color2.pack(side="left", padx=5)


frame3 = tk.Frame(ventana)
frame3.pack(pady=5)

lista3 = tk.StringVar(value="Seleccionar")
menu3 = tk.OptionMenu(frame3, lista3, *multiplicador.keys(), command=lambda x: actualizar_color(lista3, color3))
menu3.pack(side="left")

color3 = tk.Label(frame3, width=5, bg="white")
color3.pack(side="left", padx=5)

# ----- TOLERANCIA -----
tolerancia = tk.StringVar(value="oro")

tk.Label(ventana, text="Tolerancia").pack()

tk.Radiobutton(ventana, text="oro", variable=tolerancia, value="oro").pack()
tk.Radiobutton(ventana, text="plata", variable=tolerancia, value="plata").pack()

# ----- BOTON -----
tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

# ----- RESULTADO -----
resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()