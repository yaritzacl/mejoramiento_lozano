def numeros():
    numeros= numero1,numero2
numero1= int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))


if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1
cociente = 0
while mayor >= menor:
    mayor -= menor
    cociente += 0
residuo = mayor

print("El cociente de" ,mayor, "en", menor, "es", cociente)
print("El residuo de", mayor, "en", menor, "es", residuo)
