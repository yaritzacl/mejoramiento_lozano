def contar_cifras(numero):
    # Verificar si el número está dentro del rango
    if numero < 0 or numero > 9999:
        print("Error: ingrese un número que este entre 0 y 9,999.")
        return

    # Contar la cantidad de cifras en el número
    if numero == 0:
        cifras = 1
    else:
        cifras = 0
        while numero > 0:
            cifras += 1
            numero //= 10

    # Mostrar el resultado
    print(f"El número tiene {cifras} cifras.")

# Pedir al usuario que ingrese un número
numero_ingresado = int(input("Ingrese un número entre 0 y 9,999: "))
if contar_cifras(numero_ingresado):
 
 
  print("Error: Ingrese un número válido.")