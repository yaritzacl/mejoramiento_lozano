def suma_divisores(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma

def es_perfecto(num):
    return num == suma_divisores(num)

# Ejemplo de uso
numero = int(input("digita un numero : "))
if es_perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
