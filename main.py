# Programación II: Primer Proyecto / Herboza - Pereyra
# Tecnicatura universitaria en Programación UTN FRBB - Octubre 2021


def welcome():
    print("\nProgramación II: Primer Proyecto / Herboza - Pereyra \n\
--------------------------------------------------------------------------------------- \n\
Bienvenido al desallorro de ejercicios de Expresiones regulares, Recursión, Colecciones \n\
e Intercambio de datos JSON XML. \n\
Elija un ejercicio, [m] ver el menu o ingrese [s] para Salir. \n\
---------------------------------------------------------------------------------------\n\
        ")

def menu():
    print("------------------------------------ \n\
    MENU DE EJERCICIOS \n\
------------------------------------ \n\
    > Expresiones Regulares \n\
        [1] Matriculas Argentinas \n\
        [2] Numeros < 1900 \n\
        [3] EXTRA: Python Regex \n\
    > Recursión \n\
        [4] Codificar números \n\
        [5] Aplanar lista de listas \n\
        [6] Comparar 2 listas de num \n\
        [7] División entera \n\
        [8] EXTRA: Fibonacci \n\
        [9] EXTRA: Sumar digitos de N \n\
        [0] EXTRA: Sumar valores de lista \n\
    > Colecciones \n\
        [a] map, filter y reduce \n\
        [b] Pi desde suma de N terminos \n\
    > Formato de intercambios de datos \n\
        [c] Buscar Estacion \n\
        [d] Ver Batería JSON \n\
        [e] Ver Batería XML \n\
        [j] Ver JSON \n\
        [x] Ver XML \n\n\
    > Navegacion \n\
        [m] Ver Menu \n\
        [s] Salir \n\
------------------------------------ \n\n\
    ")


def select_option():
    return input("[>] ¿Qué ejercicio desea ver?: ")


def routing(ej):
    option = str(ej).lower()
    if option == "1":
        print("[1] Matriculas Argentinas")
        ej1_patentes_argentinas()
    elif option == "2":
        print("[2] Numeros < 1900")
    elif option == "3":
        print("[3] EXTRA: Python Regex")
    elif option == "4":
        print("[4] Codificar números")
    elif option == "5":
        print("[5] Aplanar lista de listas")
    elif option == "6":
        print("[6] Comparar 2 listas de num")
    elif option == "7":
        print("[7] División entera")
    elif option == "8":
        print("[8] EXTRA: Fibonacci")
    elif option == "9":
        print("[9] EXTRA: Sumar digitos de N")
    elif option == "0":
        print("[0] EXTRA: Sumar valores de lista")
    elif option == "a":
        print("[a] map, filter y reduce")
    elif option == "b":
        print("[b] Pi desde suma de N terminos")
    elif option == "c":
        print("[c] Buscar Estacion")
    elif option == "d":
        print("[d] Ver Batería JSON")
    elif option == "E":
        print("[e] Ver Batería XML")
    elif option == "j":
        print("[j] Ver JSON")
    elif option == "x":
        print("[x] Ver XML")
    elif option == "m":
        print("[m] Ver Menu")
    elif option == "s":
        print("[s] Salir")
    else:
        print('(x) ERROR: Elija una opcion válida del menu. \n')
        elegir()

def elegir():
    routing(select_option())


def ej1_patentes_argentinas():
    print("\n1. Las matrículas de las aeronaves en Argentina tienen el siguiente formato de acuerdo a su tipo (donde abc significa 3 letras mayúsculas y 123 3 dígitos):\n")
    print("LV abc\t\tUso general")
    print("LQ abc\t\tGubernamental")
    print("LV-X 123\tExperimentales")
    print("LV-S 123\tAeronave deportiva liviana")
    print("LV-SX 123\tAeronave deportiva liviana experimental\n")
    print("Matrículas válidas:\n\
    LV-QWE\n\
    LQ-ABE\n\
    LV-X443\n\
    LV-S586\n\
    LV-SX334\n")
    print("Matrículas inválidas:\n\
    LA-123\n\
    LX-ABC\n\
    LV\n\
    LV-344\n")
    
    print("Implemente una expresión regular para validar matrículas argentinas.\n")
    print("SOLUCION: \\bL[VQ]-[A-Z][A-Z][A-Z]|LV-(X\d\d\d|S\d\d\d|SX\d\d\d)\\b \n")
    print("\nExplicacion: usamos \\b para definir el principio y fin de la patente, usando como ancla los espacios y puntuacion.")
    print("Tomamos en cuenta las similaridades, las diferencias como asi todos los casos que quedan excluidos.")
    print("Desarrollamos el caso de las de uso general y las gubernamentales: L[QV]-[A-Z][A-Z][A-Z]")
    print("Luego desarrollamos los 3 casos de las experimentales y livianas juntas: LV- más las opciones para cada una, separadas por un OR (|)\n\n")
    elegir()



# Programa principal
welcome()
menu()
# Seleccion inicial
routing(select_option())