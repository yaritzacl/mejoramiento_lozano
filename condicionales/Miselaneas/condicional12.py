def son_tres_iguales(numero1, numero2, numero3):
    return numero1 == numero2 == numero3

def son_dos_iguales(numero1, numero2, numero3):
    return (numero1 == numero2) or (numero1 == numero3) or (numero2 == numero3)

def son_numeros_distintos(numero1, numero2, numero3):
    return (numero1 == numero2) or (numero1 == numero3) or (numero2 == numero3)



def num():
        num1 = float(input("Ingrese el 1 numero: "))
        num2 = float(input("Ingrese el 2 numero: "))
        num3 = float(input("Ingrese el 3 numero: "))
        
        if son_tres_iguales(num1, num2, num3):
            print("Los tres números son iguales")
        elif son_dos_iguales(num1, num2, num3):
            print("Hay dos números iguales")
        elif son_numeros_distintos(num1, num2, num3):
            print("Los tres números son distintos")
num()

