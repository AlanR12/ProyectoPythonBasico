from os import system
import operator
import colorama
from colorama import Fore,Style

colorama.init()

def leer_orden():
    cont_tipo_helado = {
        'yogurt':{
            'fresa':0,
            'vainilla':0,
            'chocolate':0
        },
        'cremoso':{
            'chocolate':0,
            'fresa':0,
            'vainilla':0,
            'rompope':0,
            'oreo con chocolate':0
        },
        'cremoso especial':{
            'amareto':0,
            'crema irlandés':0,
            'chocolate belga':0,
            'mora azul':0,
            'cajeta':0,
            'tequila':0,
            'menta con chocolate':0,
            'capuchino':0,
            'chocolate amargo':0
        }
    }

    pedir = True
    nombre = input("Escriba su nombre\n")
    orden = []
    while pedir:
        op = int(input("¿Desea ordenar algo?\t0 = No\t1 = Si\n"))
        if op == 0:
            pedir = False
        elif op == 1:
            system('cls')
            orden_hecha, cont_tipo_helado = helado(cont_tipo_helado)
            orden.append(orden_hecha)
        else:
            print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
    orden.insert(0,nombre)
    return orden,cont_tipo_helado
        
def helado(cont_tipo_helado):
    helado = {}
    sabores = []
    toppings = []
    total = 0
    tope_bls = 4
    k = 0
    pedir = False
    while pedir == False:
        menu_helados()
        tp_helado = int(input("¿Qué tipo de helado desea pedir?\n1)yogurt\t2)cremoso\t3)cremoso especial\n"))
        system('cls')
        if tp_helado == 1:
            helado['tipo de helado'] = 'yogurt'
            menu_yogurt()
            precio_helado = 50
            pedir = True
        elif tp_helado == 2:
            helado['tipo de helado'] = 'cremoso'
            menu_cremoso()
            tope_bls = 3
            precio_helado = 40
            pedir = True
        elif tp_helado == 3:
            helado['tipo de helado'] = 'cremoso especial'
            menu_cremoso_especial()
            precio_helado = 70
            pedir = True
        else:
            system('cls')
            print(Fore.RED + "Opción Inválida\n\n"+Style.RESET_ALL)
    while pedir:
        op = int(input("¿Cuántas bolas de helado va a querer?\nNota: {} bolas máx\n".format(tope_bls)))
        if op > 0 and op <= tope_bls: 
            while k<op:
                op2 = int(input("¿Qué sabor desea llevar?\n"))
                if op2 == 1:
                    if tp_helado == 1:
                        sabores.append('fresa')
                        cont_tipo_helado['yogurt']['fresa']+=1
                        total = total + precio_helado
                        k+=1
                    elif tp_helado == 2:
                        sabores.append('chocolate')
                        cont_tipo_helado['cremoso']['chocolate']+=1
                        total = total + precio_helado
                        k+=1
                    elif tp_helado == 3:
                        sabores.append('amareto')
                        cont_tipo_helado['cremoso especial']['amareto']+=1
                        total = total + precio_helado
                        k+=1
                elif op2 == 2:
                    if tp_helado == 1:
                        sabores.append('vainilla')
                        cont_tipo_helado['yogurt']['vainilla']+=1
                        total = total + precio_helado
                        k+=1
                    elif tp_helado == 2:
                        sabores.append('fresa')
                        cont_tipo_helado['cremoso']['fresa']+=1
                        total = total + precio_helado
                        k+=1
                    elif tp_helado == 3:
                        sabores.append('crema irlandés')
                        cont_tipo_helado['cremoso especial']['crema irlandés']+=1
                        total = total + precio_helado
                        k+=1
                elif op2 == 3:
                    if tp_helado == 1:
                        sabores.append('chocolate')
                        cont_tipo_helado['yogurt']['chocolate']+=1
                        total = total + precio_helado
                        k+=1
                    elif tp_helado == 2:
                        sabores.append('vainilla')
                        cont_tipo_helado['cremoso']['vainilla']+=1
                        total = total + precio_helado
                        k+=1
                    elif tp_helado == 3:
                        sabores.append('chocolate belga')
                        cont_tipo_helado['cremoso especial']['chocolate belga']+=1
                        total = total + precio_helado
                        k+=1
                elif op2 == 4:
                    if tp_helado == 1:
                        print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
                    elif tp_helado == 2:
                        sabores.append('rompope')
                        cont_tipo_helado['cremoso']['rompope']+=1
                        total = total + precio_helado
                        k+=1
                    elif tp_helado == 3:
                        sabores.append('mora azul')
                        cont_tipo_helado['cremoso especial']['mora azul']+=1
                        total = total + precio_helado
                        k+=1
                elif op2 == 5:
                    if tp_helado == 1:
                        print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
                    elif tp_helado == 2:
                        sabores.append('oreo con chocolate')
                        cont_tipo_helado['cremoso']['oreo con chocolate']+=1
                        total = total + precio_helado
                        k+=1
                    elif tp_helado == 3:
                        sabores.append('cajeta')
                        cont_tipo_helado['cremoso especial']['cajeta']+=1
                        total = total + precio_helado
                        k+=1
                elif op2 == 6:
                    if tp_helado == 1:
                        print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
                    elif tp_helado == 2:
                        print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
                    elif tp_helado == 3:
                        sabores.append('tequila')
                        cont_tipo_helado['cremoso especial']['tequila']+=1
                        total = total + precio_helado
                        k+=1
                elif op2 == 7:
                    if tp_helado == 1:
                        print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
                    elif tp_helado == 2:
                        print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
                    elif tp_helado == 3:
                        sabores.append('menta con chocolate')
                        cont_tipo_helado['cremoso especial']['menta con chocolate']+=1
                        total = total + precio_helado
                        k+=1
                elif op2 == 8:
                    if tp_helado == 1:
                        print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
                    elif tp_helado == 2:
                        print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
                    elif tp_helado == 3:
                        sabores.append('capuchino')
                        cont_tipo_helado['cremoso especial']['capuchino']+=1
                        total = total + precio_helado
                        k+=1
                elif op2 == 9:
                    if tp_helado == 1:
                        print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
                    elif tp_helado == 2:
                        print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
                    elif tp_helado == 3:
                        sabores.append('chocolate amargo')
                        cont_tipo_helado['cremoso especial']['chocolate amargo']+=1
                        total = total + precio_helado
                        k+=1
                else:
                    print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
    helado['sabores'] = sabores

    system('cls')
    menu_envases()
    while pedir:
        op = int(input("¿En qué envase desea que le sirvamos su helado?\n"))
        if op > 0 and op < 4:
            if op == 1:
                helado['envase'] = 'vaso'
                total = total + 10
            elif op == 2:
                helado['envase'] = 'cono'
                total = total + 15
            elif op == 3:
                helado['envase'] = 'canastilla'
                total = total +30
            break
        else:
            print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
    system('cls')
    k=0
    while pedir:
        op = int(input("¿Desea agregar algún topping?\t0 = No\t1 = Si\n"))
        if op == False:
            toppings.append('ninguno')
            helado['toppings'] = toppings
            print(Fore.BLUE + Style.BRIGHT +"Saliendo..."+Style.RESET_ALL)
            break
        elif op == True:
            menu_toppings()
            while pedir:
                print("¿Cuántos toppings desea?\nNota: 4 máx",end='')
                if tp_helado == 3:
                    print(Fore.YELLOW + ",tiene 2 incluidos",end=''+Style.RESET_ALL)
                op = int(input('\n'))
                if op > 0 and op < 5:
                    while k<op:
                        op2 = int(input("¿Qué topping desea poner?\n"))
                        if op2 == 1:
                            toppings.append('mango')
                            k+=1
                        elif op2 == 2:
                            toppings.append('zarzamora')
                            k+=1
                        elif op2 == 3:
                            toppings.append('fresa')
                            k+=1
                        elif op2 == 4:
                            toppings.append('chispas de chocolate')
                            k+=1
                        elif op2 == 5:
                            toppings.append('granola')
                            k+=1
                        elif op2 == 6:
                            toppings.append('chocolate liquido')
                            k+=1
                        elif op2 == 7:
                            toppings.append('rompope')
                            k+=1
                        elif op2 == 8:
                            toppings.append('cajeta')
                            k+=1
                        elif op2 == 9:
                            toppings.append('licor de cereza') 
                            k+=1
                        else:
                            print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
                        if tp_helado == 3:
                            if k>2:
                                total = total + 10
                        elif k>0:
                            total = total + 10
                    break
                else:
                    print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción Inválida"+Style.RESET_ALL)
    helado['toppings'] = toppings
    helado['precio'] = total
    return helado,cont_tipo_helado

def imprime_orden(orden):
    print(Fore.CYAN+"-"*15,"ORDEN","-"*15+Style.RESET_ALL)
    print("Nombre:{}\n".format(orden[0]))
    for h in range(1,len(orden)):
        print("Helado {}".format(h))
        for k in orden[h]:
            print("{}: {}".format(k,orden[h][k]))
        print()
    print(Fore.CYAN+"-"*38+Style.RESET_ALL)
    print()

def imprime_popularidad(cont_tipo_helado):
    titulo_yogurt = '----------- YOGURT -----------'
    titulo_cremoso = '----------- CREMOSO ----------'
    titulo_cremoso_especial = '------ CREMOSO ESPECIAL ------'
    titulos = [titulo_yogurt,titulo_cremoso,titulo_cremoso_especial]
    k = 0
    print(Fore.BLUE + Style.BRIGHT +"    .:Tabla de Popularidad:.\n"+Style.RESET_ALL)
    for x in cont_tipo_helado:
        print("{}".format(titulos[k]))
        dicc = sorted(cont_tipo_helado[x].items(),key = operator.itemgetter(1),reverse=True)
        for t in range(len(dicc)):
            print("| {:<20}    {:<2} |".format(dicc[t][0],dicc[t][1]))
        k+=1
    print("-"*30)
    print("\n\n")

def imprime_historial(historial):
    print(Fore.BLUE + Style.BRIGHT +"\t    .:HISTORIAL:."+Style.RESET_ALL)
    print()
    for k in historial:
        imprime_orden(k)


def menu_helados():
    yogurt = ['fresa','vainilla','chocolate','','','','','','']
    cremoso = ['chocolate','fresa','vainilla','rompope','oreo con chocolate','','','','']
    cremoso_especial = ['amareto','crema irlandés','chocolate belga','mora azul','cajeta','tequila','menta con chocolate','capuchino','chocolate amargo']
    print("-"*9,Fore.GREEN+ Style.BRIGHT +"YOGURT"+Style.RESET_ALL,"-"*9,"-"*8,Fore.YELLOW + Style.BRIGHT +"CREMOSO"+Style.RESET_ALL,"-"*9,"-"*4,Fore.RED + Style.BRIGHT +"CREMOSO ESPECIAL"+Style.RESET_ALL,"-"*4)
    print("|      {:17}  |".format('Precio: $50'),"      {:17} |".format('Precio: $40'),"      {:17}   |".format('Precio: $70'))
    for i in range(len(cremoso_especial)):
        print("| {:<22}  |".format(yogurt[i])," {:<22} |".format(cremoso[i])," {:<24} |".format(cremoso_especial[i]))
    print("-"*81)
    print()

def menu_yogurt():
    yogurt = ['1.fresa','2.vainilla','3.chocolate']
    print("-"*9,Fore.GREEN + Style.BRIGHT +"YOGURT"+Style.RESET_ALL,"-"*9)
    print("|      {:17} |".format('Precio: $50'))
    for k in yogurt:
        print("| {:<22} |".format(k))
    print("-"*26)
    print()

def menu_cremoso():
    cremoso = ['1.chocolate','2.fresa','3.vainilla','4.rompope','5.oreo con chocolate']
    print("-"*8,Fore.YELLOW + Style.BRIGHT +"CREMOSO"+Style.RESET_ALL,"-"*9)
    print("|      {:17} |".format('Precio: $40'))
    for k in cremoso:
        print("| {:<22} |".format(k))
    print("-"*26)
    print()

def menu_cremoso_especial():
    cremoso_especial = ['1.amareto','2.crema irlandés','3.chocolate belga','4.mora azul','5.cajeta','6.tequila','7.menta con chocolate','8.capuchino','9.chocolate amargo']
    print("-"*4,Fore.RED + Style.BRIGHT +"CREMOSO ESPECIAL"+Style.RESET_ALL,"-"*4)
    print("|      {:17} |".format('Precio: $70'))
    for k in cremoso_especial:
        print("| {:<22} |".format(k))
    print("-"*26)
    print()

def menu_toppings():
    toppings = ['1.mango','2.zarzamora','3.fresa','4.chispas de chocolate','5.granola','6.chocolate liquido','7.rompope','8.cajeta','9.licor de cereza']
    print("-"*8,"TOPPINGS","-"*8)
    print("|      {:17} |".format('Precio: $10'))
    for k in toppings:
        print("| {:<22} |".format(k))
    print("-"*26)
    print()

def menu_envases():
    envase = ['1.vaso','2.cono','3.canastilla']
    precio = [10,15,30]
    print("-"*7,"ENVASE","-"*7)
    for k in range(len(envase)):
        print("| {:<12} | ${:<2} |".format(envase[k],precio[k]))
    print("-"*22)
    print()

def Titulo():
    print(Fore.BLUE + Style.BRIGHT +'''
     _____ _    ____               _   _      _           _       
    | ____| |  |  _ \ ___ _   _   | | | | ___| | __ _  __| | ___  
    |  _| | |  | |_) / _ \ | | |  | |_| |/ _ \ |/ _` |/ _` |/ _ \ 
    | |___| |  |  _ <  __/ |_| |  |  _  |  __/ | (_| | (_| | (_) |
    |_____|_|  |_| \_\___|\__, |  |_| |_|\___|_|\__,_|\__,_|\___/ 
                          |___/                                   
    ''' + Style.RESET_ALL)
    print('''
                         ------------ 
                        < Bienvenido >
                         ------------ 
                           \\
                            \\
                                .--.
                               |o_o |
                               |:_/ |
                              //   \ \\
                             (|     | )
                            /'\_   _/'\\
                            \___)=(___/
    ''')