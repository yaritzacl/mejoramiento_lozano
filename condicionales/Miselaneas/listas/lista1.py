def generar_serie_fibonacci_digitos(n):
    if n <= 0:
        return []
    
    fibonacci = [0, 10]

    num = fibonacci[-1] + fibonacci[-2]
    if (int(num)) == n:
            fibonacci.append(num)
         
     

    # return fibonacci


n = int(input("Ingrese la cantidad de dígitos de la serie de Fibonacci que desea generar: "))
fibonacci_series = generar_serie_fibonacci_digitos(n)
print("Serie de Fibonacci generada:")
print(fibonacci_series)

