import os



def crear_archivo():
    nombre=input("Nombre del archivo: ")
    with open(nombre,"w")as archivo:
        print("Archivo creado correctamente")


def escribir_archivo():
    nombre=input("Nombre del archivo: ")
    texto=input("Texto a escribir: ")
    with open(nombre,"w")as archivo:
        archivo.write(texto)
        print("Texto guardado correctamente")


def agregar_texto():
    nombre=input("Nombre del archivo: ")
    texto=input("Texto a agregar: ")
    with open(nombre,"a")as archivo:
        archivo.write("\n" + texto)
        print("Texto agregado correctamente")


def leer_archivo():
    nombre=input("Nombre del archivo: ")
    try:
        with open(nombre,"r") as archivo:
            contenido=archivo.readlines()
            os.system("cls")
            print("\nContenido del archivo: ")
            print(contenido)
            print("--------------------------------")
            archivo.seek(0)
            for linea in contenido:
                print(linea.strip())

    except FileNotFoundError:
        print("El archivo no existe")

leer_archivo()

