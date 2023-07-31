import random
def generar_arreglo(lista):
    lista=[]
tam=random.randint(5,10)
lista=[random.randrange(100) for i in range(tam)]

print(lista)
def numero ():
    numero=0
numero = int(input("digita un numero : "))
if numero>=tam:
    print(f"numero")
    
def sum(tam):
    sum+numero
    suma.append 
    return sum 
suma=0

def resta (tam):
    resta= []
    return resta


def obtener_elemento_mayor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor

def obtener_elemento_menor(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor

def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida
print(lista)
print(tam)

