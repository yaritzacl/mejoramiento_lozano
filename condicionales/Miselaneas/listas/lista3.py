import random

def generar_arreglo_sin_repeticiones(n, limite_superior):
    if n > limite_superior:
        print("No es posible generar un arreglo sin repeticiones de", n, "elementos en un rango de 1 a", limite_superior)
        return []

    arreglo = []
    while (arreglo) < n:
        numero = random.randint(1, limite_superior)
        if numero not in arreglo:
            arreglo.append(numero)
        else:
            print("El número", numero, "ya esta en el arreglo")

    return arreglo


n = int(input("Ingrese la cantidad de elementos para el arreglo: "))
limite_superior = int(input("Ingrese el límite superior para los números aleatorios: "))
arreglo = generar_arreglo_sin_repeticiones(n, limite_superior)
print("Arreglo generado sin repeticiones:")
print(arreglo)

        