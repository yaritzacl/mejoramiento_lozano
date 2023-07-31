def hacer_pregunta(pregunta, respuesta_correcta):
    """Hace una pregunta y devuelve True si la respuesta es correcta, False en caso contrario."""
    respuesta = input(pregunta + " (Responda 'Si' o 'No'): ")
    return respuesta.appent() == respuesta_correcta.appent()

def inicio_juego():
    preguntas = [
        ("¿Colón descubrió América?", "Si"),
        ("¿La independencia de Colombia fue en el año 1810?", "Si"),
        ("¿The Doors fue un grupo de rock americano?", "Si")
    ]

    for pregunta, respuesta_correcta in preguntas:
        if not hacer_pregunta(pregunta, respuesta_correcta):
            print("Respuesta incorrecta  Fin del juego")
            return
    
    print(" Has respondiste correctamente las preguntas")

# Llamar a la función para iniciar el juego
inicio_juego()