import colorama
from colorama import Fore, Style
import Funciones as heladeria
import Archivo as file
from os import system

colorama.init()

def Menu(historial,popularidad):
    aux = {}
    heladeria.Titulo()
    print("\n"*3)
    system('pause')
    system('cls')
    while True:
        print("Seleccione una opcion del menu")
        print("-"*27)
        print ("| {:<24}|\n| {:24}|\n| {:<24}|\n| {:<24}|".format('1)Ordenar','2)Historial de ordenes','3)Calcular Popularidad','4)Salir'))
        print("-"*27)
        op = int(input(""))
        if op == 1:
            orden,cont_popularidad = heladeria.leer_orden()
            if len(popularidad) == 0:
                popularidad.update(cont_popularidad)
            else:
                aux.update(cont_popularidad)
                for m in popularidad:
                    for n in popularidad[m]:
                        popularidad[m][n] = popularidad[m][n] + aux[m][n] 
            system('pause')
            system('cls')
            if len(orden) == 1:
                print(Fore.YELLOW + "Orden vacía\n"+Style.RESET_ALL)    
            else:
                print(Fore.GREEN + Style.BRIGHT +"Orden Registrada\n"+Style.RESET_ALL)
                heladeria.imprime_orden(orden)
                historial.append(orden)
                file.Agregar_Datos(ruta,historial)
                file.Agregar_Datos(ruta2,popularidad)
        elif op == 2:
            system('cls')
            if len(historial) == 0:
                print(Fore.YELLOW + "Lista vacía\n"+Style.RESET_ALL)
            else:
                heladeria.imprime_historial(historial)
                system('pause')
                system('cls')
        elif op == 3:
            system('cls')
            if len(historial) == 0:
                print(Fore.YELLOW + "Todavía no hay ordenes\n"+Style.RESET_ALL)
            else:
                heladeria.imprime_popularidad(popularidad)
                system('pause')
                system('cls')
        elif op == 4:
            exit(1)
        else:
            system('cls')
            print(Fore.RED + Style.BRIGHT +"Opción Invalida\n"+Style.RESET_ALL)


ruta = "Historial.json"
ruta2 = "Popularidad.json"
file.Crear(ruta)
file.Crear(ruta2)
historial = []
popularidad = {}
historial = file.Leer_Datos(ruta,historial)
popularidad = file.Leer_Datos(ruta2,popularidad)
print()
system('pause')
system('cls')
Menu(historial,popularidad)
