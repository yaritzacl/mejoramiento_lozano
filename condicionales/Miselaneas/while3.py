
def invertir_numero(n):
    numero = n
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero
numero1 = int(input("Ingrese un numero de hasta 9 digitos: "))
numero_invertido = invertir_numero (numero1)
print(f"El número {numero1} es un numero al revez  {numero_invertido} ")


