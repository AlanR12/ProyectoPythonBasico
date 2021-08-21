import json, os
import colorama
from colorama import Fore,Style
colorama.init()

def Crear(ruta):
    try:
        file = open(ruta,"x")
        print(Fore.GREEN + Style.BRIGHT + "¡Se ha creado el archivo '{}' con exito!".format(ruta)+Style.RESET_ALL)
        file.close()
    except FileExistsError:
        print(Fore.YELLOW + "El archivo '{}' ya ha sido creado".format(ruta)+Style.RESET_ALL) 

def Archivo_Vacio(ruta):
    file = open(ruta,"r")
    file.seek(0,os.SEEK_END)
    if file.tell() == False:
        print(Fore.YELLOW + "Archivo '{}' vacío".format(ruta)+Style.RESET_ALL)
        file.close()
        return True
    else:
        print("El archivo '{}' contiene datos".format(ruta))
        return False

def Leer_Datos(ruta,datos):
    file = open(ruta,"r")
    if Archivo_Vacio(ruta):
        return datos
    else:
        print(Fore.BLUE + Style.BRIGHT +"Leyendo Datos..."+Style.RESET_ALL)
        datos = json.load(file)
        return datos

def Agregar_Datos(ruta,datos):
    file = open(ruta,"w")
    json.dump(datos,file,indent = 4)
    file.close()