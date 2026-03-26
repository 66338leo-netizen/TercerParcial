import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk




ventana=tk.Tk()
ventana.title("Zodiaco")
ventana.geometry("800x400")

tk.Label(ventana,text="Ingrese sus datos: ").grid(row=0,column=0,padx=10,pady=10)

Nombre=tk.Entry(ventana,width=30)
Nombre.grid(row=0,column=1,padx=10,pady=10)

zodiac=tk.Button(ventana,text="Calcular", width=12)
zodiac.grid(row=2,column=0,pady=10)

ventana.mainloop()