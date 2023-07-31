def obtener_calificacion(nota):
    if nota < 0 or nota > 10:
        return "Nota no valida"
    elif nota < 5:
        return "Insuficiente"
    elif nota < 7:
        return "Suficiente"
    elif nota < 9:
        return "Bien"
    elif nota < 10:
        return "Notable"
    else:
        return "Sobresaliente"

nota = float(input("Ingrese la nota (0-10): "))
print("Por favor, ingrese un valor numérico válido.")

calificacion = obtener_calificacion(nota)
print("La calificacion es:", calificacion)
