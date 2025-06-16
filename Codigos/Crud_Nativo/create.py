from db import get_connection

def crear_jugador(nombre, posicion, equipo):
    jugadores = get_connection()
    nuevo = {
        "nombre": nombre,
        "posicion": posicion,
        "equipo": equipo
    }
    jugadores.insert_one(nuevo)
    print("Jugador creado con éxito")
