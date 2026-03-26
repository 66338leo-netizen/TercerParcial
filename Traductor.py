import tkinter as tk
from tkinter import messagebox

dic_ingles_espanol = {
    "hello": "hola",
    "world": "mundo",
    "cat": "gato",
    "dog": "perro",
    "house": "casa"
}

dic_espanol_ingles = {v: k for k, v in dic_ingles_espanol.items()}


def traducir():
    palabra = entrada.get().strip().lower()

    if not palabra:
        messagebox.showwarning("Aviso", "Escribe una palabra para traducir.")
        return

    idioma = opcion.get()

    if idioma == 1:
        if palabra in dic_ingles_espanol:
            resultado.config(text=f"Traducción: {dic_ingles_espanol[palabra]}")
        else:
            resultado.config(text="Palabra no encontrada.")
    elif idioma == 2: 
        if palabra in dic_espanol_ingles:
            resultado.config(text=f"Traducción: {dic_espanol_ingles[palabra]}")
        else:
            resultado.config(text="Palabra no encontrada.")
    else:
        messagebox.showwarning("Aviso", "Selecciona un idioma.")


def agregar():
    ingles = entrada_ingles.get().strip().lower()
    espanol = entrada_espanol.get().strip().lower()

    if not ingles or not espanol:
        messagebox.showwarning("Aviso", "Escribe la palabra en inglés y en español.")
        return

    dic_ingles_espanol[ingles] = espanol
    dic_espanol_ingles[espanol] = ingles

    messagebox.showinfo("Éxito", f"Se agregó: {ingles} = {espanol}")

    entrada_ingles.delete(0, tk.END)
    entrada_espanol.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Traductor con Diccionario")
ventana.geometry("500x400")

opcion = tk.IntVar()

tk.Label(ventana, text="Palabra a traducir").pack(pady=10)

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

radio1 = tk.Radiobutton(ventana, text="Inglés -> Español", variable=opcion, value=1)
radio1.pack()

radio2 = tk.Radiobutton(ventana, text="Español -> Inglés", variable=opcion, value=2)
radio2.pack()

btn_traducir = tk.Button(ventana, text="Traducir", width=12, command=traducir)
btn_traducir.pack(pady=10)

resultado = tk.Label(ventana, text="Traducción: ", fg="blue")
resultado.pack(pady=10)


tk.Label(ventana, text="Agregar nueva palabra").pack(pady=5)

tk.Label(ventana, text="Inglés").pack()
entrada_ingles = tk.Entry(ventana, width=30)
entrada_ingles.pack(pady=5)

tk.Label(ventana, text="Español").pack()
entrada_espanol = tk.Entry(ventana, width=30)
entrada_espanol.pack(pady=5)

btn_agregar = tk.Button(ventana, text="Agregar", width=12, command=agregar)
btn_agregar.pack(pady=15)

ventana.mainloop()