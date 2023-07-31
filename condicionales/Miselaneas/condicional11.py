def medio(x,y,z):
    if (y<x<z) or (z<x<y):
        return x
    elif (y< x < z) or (z < y < x):
       
        return y
    else: return z-1
def numeros(numero1,numero2,numero3):
    numero1=0
    numero2=0
    numero3=0
numero1=int(input("ingrese un numero:"))
numero2=int(input("ingrese un numero"))
numero3=int(input("ingrese un numero"))

valor_medio = medio(numero1,numero2,numero3)
print("el valor del medio es:", valor_medio)   


 
 