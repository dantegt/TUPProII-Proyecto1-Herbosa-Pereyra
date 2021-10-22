# Programación II: Primer Proyecto / Herboza - Pereyra
# Tecnicatura universitaria en Programación UTN FRBB - Octubre 2021

import re
import time

def welcome():
    output = """
    Programación II: Primer Proyecto / Herboza - Pereyra
    ---------------------------------------------------------------------------------------
    Bienvenido al desallorro de ejercicios de Expresiones regulares, Recursión, Colecciones
    e Intercambio de datos JSON XML.
    Elija un ejercicio, [m] ver el menu o ingrese [s] para Salir.
    ---------------------------------------------------------------------------------------"""
    print(output)

def menu():
    menustr = """
    ---------------------------------------------------------------
    MENU DE EJERCICIOS\t\t\t[m] Menu  [s] Salir
    ---------------------------------------------------------------
        > Expresiones Regulares
            [1] Matriculas Argentinas
            [2] Numeros < 1900
            [3] EXTRA: Python Regex
        > Recursión
            [4] Codificar números
            [5] Aplanar lista de listas
            [6] Comparar 2 listas de num
            [7] División entera
            [8] EXTRA: Fibonacci
            [9] EXTRA: Sumar digitos de N
            [0] EXTRA: Sumar valores de lista
        > Colecciones
            [a] map, filter y reduce
            [b] Pi desde suma de N terminos
        > Formato de intercambios de datos
            [c] Buscar Estacion
            [d] Ver Batería JSON
            [e] Ver Batería XML
            [j] Ver JSON
            [x] Ver XML
    ---------------------------------------------------------------
    """
    print(menustr)


def select_option():
    return input("[>] ¿Qué ejercicio desea ver? [m] Menu [s] Salir: ")


def routing(ej):
    option = str(ej).lower()
    if option == "1":
        print("[1] Matriculas Argentinas")
        ej1_patentes_argentinas()
    elif option == "2":
        print("[2] Numeros < 1900")
        ej2_numeros_menor_1900()
    elif option == "3":
        print("[3] EXTRA: Python Regex")
        ej3_extra_python_regex()
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
        menu()
        elegir()
    elif option == "s":
        print("[s] Salir")
        print("Gracias por utilizar nuestro programa :)")
    else:
        print('(x) ERROR: Elija una opcion válida del menu. \n')
        elegir()
    

def elegir():
    routing(select_option())


def ej1_patentes_argentinas():
    enunciado = """
    1. Las matrículas de las aeronaves en Argentina tienen el siguiente formato de acuerdo a su tipo (donde abc significa 3 letras mayúsculas y 123 3 dígitos):
        LV-abc\t\tUso general
        LQ-abc\t\tGubernamental
        LV-X123\t\tExperimentales
        LV-S123\t\tAeronave deportiva liviana
        LV-SX123\tAeronave deportiva liviana experimental

        Matrículas válidas:
        LV-QWE
        LQ-ABE
        LV-X443
        LV-S586
        LV-SX334
        
        Matrículas inválidas:
        LA-123
        LX-ABC
        LV
        LV-344

    Implemente una expresión regular para validar matrículas argentinas.
    """
    solucion = """
    SOLUCION: \\bL[VQ]-[A-Z][A-Z][A-Z]|LV-(X\d\d\d|S\d\d\d|SX\d\d\d)\\b 

    Explicacion: usamos \\b para definir el principio y fin de la patente, usando como ancla los espacios y puntuacion.
    Tomamos en cuenta las similaridades, las diferencias como asi todos los casos que quedan excluidos.
    Desarrollamos el caso de las de uso general y las gubernamentales: L[QV]-[A-Z][A-Z][A-Z]
    Luego desarrollamos los 3 casos de las experimentales y livianas juntas: LV- más las opciones para cada una, separadas por un OR (|)
    """
    print(enunciado)
    input("Presione [ENTER] para ver la solucion...")
    print(solucion)
    elegir()



def ej2_numeros_menor_1900():
    enunciado = """
    2. Diseñe una ER para validar cadenas de números naturales menores a 1900.
    """
    solucion = """
        SOLUCION: \\b(1[0-8]|[0-9])?[0-9]?[0-9]\\b

    Explicacion: usamos \\b para definir el principio y fin del numero, usando como ancla los espacios y puntuacion.
    N tiene 4 cifras / la primera es 1 / la segunda es entre 0 y 8 / 2 numeros cualquiera
    Combinamos los casos de los numeros de 3 o 4 cifras con un OR (|) entre 1 más cualquier cifra entre 0 y 8 ó una cifra 0-9
    Como el caso minimo es un numero de 1 cifra, el resto de las cifras las ponemos con ? porque pueden estar o no.
    """

    print(enunciado)
    input("Presione [ENTER] para ver la solucion...")
    print(solucion)
    elegir()


def ej3_extra_python_regex():
    descripcion = """
    Python tiene un paquete incorporado llamado re, que se puede importar para trabajar con expresiones regulares:
    
        import re

    El módulo re ofrece un conjunto de funciones que nos permite buscar una cadena para una coincidencia:
    
        findall\t\tDevuelve una lista que contiene todas las coincidencias
        search\t\tDevuelve un objeto Match si hubo alguna coincidencia
        split\t\tDevuelve una lista donde la cadena se ha dividido en cada coincidencia
        sub\t\tReemplaza una o más coincidencias con una cadena
    """
    research = """
    Por ejemplo, vamos a utilizar la funcion re.search() para averiguar si el número que le pediremos que ingrese, es menor a 1900.
    En código esto se implementaría:

        re.search(r'\\b(1[0-8]|[0-9])?[0-9]?[0-9]\\b', input_usuario)
    
    Esta función se llama con 2 parametros: re.search([REGEX], [STRING]) donde [REGEX] es la expresión regular
    y [STRING] es la cadena donde se buscará.

    La r delante del [REGEX] evita que el interprete de Python la modifique en caso de usar caracteres de escape como \\
    """
    print(descripcion)
    input("Presione [ENTER] para ver una demostracion...")
    print(research)
    input("Presione [ENTER] para probar re.search()...")
    
    while True:
        print("\n[#] Numero ENTERO es menor a 1900?\n------------------------------------------")
        numero = input("[>] Ingrese un numero ENTERO o [s] para salir: ")
        if not numero.isnumeric():
            if numero == "s":
                break
            else:
                print("[x] Debe ingresar un numero ENTERO")


        if re.search(r'\b(1[0-8]|[0-9])?[0-9]?[0-9]\b', numero):
            print("[v] Ingresó un numero entero MENOR a 1900")
        else:
            print("[^] Ingreso un numero entero IGUAL O MAYOR a 1900")
        time.sleep(1)

    print("\n[!] Aprendimos un poco más sobre el módulo re!\n")
    elegir()

# Programa principal
welcome()
menu()
# Seleccion inicial
routing(select_option())


# To Do
# ----------------------------------------------------
# - Clear Screen
# - Pausa antes de la solucion para los ej Expresion Regular