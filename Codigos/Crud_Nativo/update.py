from db import get_connection

def actualizar_jugador(nombre_actual, nuevo_nombre, nueva_posicion, nuevo_equipo):
    jugadores = get_connection()
    result = jugadores.update_one(
        {"nombre": nombre_actual},
        {"$set": {
            "nombre": nuevo_nombre,
            "posicion": nueva_posicion,
            "equipo": nuevo_equipo
        }}
    )
    if result.matched_count:
        print("Jugador actualizado.")
    else:
        print("No se encontró un jugador con ese nombre.")
