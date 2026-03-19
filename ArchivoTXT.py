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

def buscar_palabra():
    nombre=input("Nombre del archivo: ")
    palabra=input("Palabra a Buscar: ")
    try:
        with open(nombre,"r") as archivo:
            contenido=archivo.read()
            if palabra in contenido:
                print("La palabra fue encontrada")
            else: 
                print("La palabra no se encuentra en el archivo")
    except FileExistsError:
        print("El archivo no existe")

def menu():
    while True:
        print("\n---Gestion de Archivos ---")
        print("1.Crear Archivo")
        print("2.Escribir en Archivo")
        print("3.Agregar texto")
        print("4.Leer Archivo")
        print("5.Buscar Palabra")
        print("6. Salir")

        opcion=input("Sleccione una opcion: ")

        if opcion== "1":
            crear_archivo()
        elif opcion== "2":
            escribir_archivo()
        elif opcion== "3":
            agregar_texto()
        elif opcion== "4":
            leer_archivo()
        elif opcion== "5":
            buscar_palabra()
        elif opcion== "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion Invalida")

menu()