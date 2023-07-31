def mostrar_menu():
    print("Eliga una opcion ")
    print("1. Agregar diccionario espa-ingles")
    print("2. Agregar diccionario ingles-espa")
    print("3. Utiizar diccionario espa-ingles")
    print("4. Utiizar diccionario ingles-espa")
    print("5. Visualizar diccionario espa-ingles")
    print("6. Visualizar diccionario ingles-espa")
    print("7. Salir")


diccionarioINGS = {
    'dog': 'perro',
    'cat': 'gato',
    'tigre':'tiger',
    'Spider': 'araña',
    'donkey':'burro',
    'Hen': 'gallina',
    'Cock': 'gallo',
    'lion': 'leon'
}

diccionarioESPA = {
    'perro': 'dog',
    'gato': 'cat',
    'tigre':'tiger',
    'araña': 'Spider',
    'burro': 'Donkey',
    'gallina': 'Hen',
    'gallo': 'Cock',
    'leon': 'lion'
}


def agregar_diccionario_esp_ingles():
    palabra_esp = input("Ingrese una palabra en espa: ")
    palabra_ing = input("Ingrese la traduccion de la palabra en ingles: ")
    diccionarioINGS[palabra_ing] = palabra_esp


def agregar_diccionario_ingles_esp():
    palabra_ing = input("Ingrese una palabra en ingles: ")
    palabra_esp = input("Ingrese la traduccion de la palabra en espa: ")
    diccionarioESPA[palabra_esp] = palabra_ing


def utilizar_diccionario_esp_ingles():
    palabra_esp = input("Ingrese una palabra en espa para buscar su traduccion: ")
    if palabra_esp in diccionarioINGS:
        print("La traduccion al ingles es:", diccionarioINGS[palabra_esp])
    else:
        print("La palabra no se encuentra en el diccionario.")


def utilizar_diccionario_ingles_esp():
    palabra_ing = input("Ingrese una palabra en ingles para buscar su traduccion: ")
    if palabra_ing in diccionarioESPA:
        print("La traduccion al espa es:", diccionarioESPA[palabra_ing])
    else:
        print("La palabra no se encuentra en el diccionario.")


def visualizar_diccionario_esp_ingles():
    print("Diccionario espa-ingles:")
    for palabra_ing, palabra_esp in diccionarioINGS.items():
        print(palabra_ing, "---", palabra_esp)


def visualizar_diccionario_ingles_esp():
    print("Diccionario ingles-espa:")
    for palabra_esp, palabra_ing in diccionarioESPA.items():
        print(palabra_esp, "---", palabra_ing)



continuar = True
while continuar:
    mostrar_menu()
    opcion = input("Ingrese el numero de la opcion deseada: ")

    if opcion == "1":
        agregar_diccionario_esp_ingles()
    elif opcion == "2":
        agregar_diccionario_ingles_esp()
    elif opcion == "3":
        utilizar_diccionario_esp_ingles()
    elif opcion == "4":
        utilizar_diccionario_ingles_esp()
    elif opcion == "5":
        visualizar_diccionario_ingles_esp()
    elif opcion == "6":
        visualizar_diccionario_esp_ingles()
    elif opcion == "7":
        print("¡Fin del programa!")
        continuar = False
    else:
        print("Opcion invalida. Por favor, ingrese un numero valido.")
