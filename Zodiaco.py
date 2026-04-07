import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from datetime import date

ventana = tk.Tk()
ventana.title("Zodiaco Chino")
ventana.geometry("900x500")
ventana.config(bg="white")
tk.Label(ventana, text="Ingrese su Nombre:", bg="white", font=("Arial", 12)).place(x=20, y=30)
Nombre = tk.Entry(ventana, width=30, font=("Arial", 12))
Nombre.place(x=180, y=30)

tk.Label(ventana, text="Ingrese su Día:", bg="white", font=("Arial", 12)).place(x=20, y=80)
fecha = tk.Entry(ventana, width=30, font=("Arial", 12))
fecha.place(x=180, y=80)

tk.Label(ventana, text="Ingrese su Mes:", bg="white", font=("Arial", 12)).place(x=20, y=130)
fecha1 = tk.Entry(ventana, width=30, font=("Arial", 12))
fecha1.place(x=180, y=130)

tk.Label(ventana, text="Ingrese su Año:", bg="white", font=("Arial", 12)).place(x=20, y=180)
fecha2 = tk.Entry(ventana, width=30, font=("Arial", 12))
fecha2.place(x=180, y=180)

lbl_nombre = tk.Label(ventana, text="Nombre: ", bg="white", font=("Arial", 13, "bold"))
lbl_nombre.place(x=450, y=40)

lbl_edad = tk.Label(ventana, text="Edad: ", bg="white", font=("Arial", 13, "bold"))
lbl_edad.place(x=450, y=80)

lbl_signo = tk.Label(ventana, text="Zodiaco Chino: ", bg="white", font=("Arial", 13, "bold"))
lbl_signo.place(x=450, y=120)

lbl_imagen = tk.Label(ventana, bg="white")
lbl_imagen.place(x=550, y=170)

imagen_actual = None

zodiaco_chino = {
    0: ("Mono", "mono.png"),
    1: ("Gallo", "gallo.png"),
    2: ("Perro", "perro.png"),
    3: ("Cerdo", "cerdo.png"),
    4: ("Rata", "rata.png"),
    5: ("Buey", "buey.png"),
    6: ("Tigre", "tigre.png"),
    7: ("Conejo", "conejo.png"),
    8: ("Dragon", "dragon.png"),
    9: ("Serpiente", "serpiente.png"),
    10: ("Caballo", "caballo.png"),
    11: ("Cabra", "cabra.png")
}
def edad():
    global imagen_actual

    try:
        nombre_usuario = Nombre.get().strip()
        dia = int(fecha.get())
        mes = int(fecha1.get())
        anio = int(fecha2.get())
        if nombre_usuario == "":
            messagebox.showerror("Error", "Ingrese su nombre")
            return

        nacimiento = date(anio, mes, dia)
        hoy = date.today()

        if nacimiento > hoy:
            messagebox.showerror("Error", "La fecha de nacimiento no puede ser futura")
            return
        edad_usuario = hoy.year - nacimiento.year
        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad_usuario -= 1

        signo, archivo_imagen = zodiaco_chino[anio % 12]

        lbl_nombre.config(text=f"Nombre: {nombre_usuario}")
        lbl_edad.config(text=f"Edad: {edad_usuario} años")
        lbl_signo.config(text=f"Zodiaco Chino: {signo}")

        if os.path.exists(archivo_imagen):
            img = Image.open(archivo_imagen)
            img = img.resize((220, 220))
            imagen_actual = ImageTk.PhotoImage(img)
            lbl_imagen.config(image=imagen_actual, text="")
        else:
            lbl_imagen.config(image="", text=f"No se encontró:\n{archivo_imagen}", font=("Arial", 12), bg="white")

    except ValueError:
        messagebox.showerror("Error", "Ingrese datos numéricos válidos en día, mes y año")
zodiac = tk.Button(ventana, text="Calcular", width=15, font=("Arial", 12), command=edad)
zodiac.place(x=120, y=250)
print(date.month)
ventana.mainloop()