from db import get_connection

def listar_jugadores():
    jugadores = get_connection()
    for jugador in jugadores.find():
        print(f"ID: {jugador['_id']}, Nombre: {jugador['nombre']}, Posición: {jugador['posicion']}, Equipo: {jugador['equipo']}")
