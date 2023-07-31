def maximo_positivo():
    maximo = int(input("Introduce un número: "))
    numero= int(input("Introduce un número: "))
   
    while  numero > maximo:
          maximo = numero
    
    return maximo

resultado = maximo_positivo()
print("El máximo número positivo ingresado es:", resultado)

