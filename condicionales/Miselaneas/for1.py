def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores


numero_ingresado = int(input("digita un numero : "))
if numero_ingresado <= 0:
 print("Ingresa un número entero positivo válido.")

divisores = encontrar_divisores(numero_ingresado)
print("Los divisores de", numero_ingresado, "son:", divisores)

