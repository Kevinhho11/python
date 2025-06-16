from db import get_connection

def eliminar_jugador(nombre):
    jugadores = get_connection()
    result = jugadores.delete_one({"nombre": nombre})
    if result.deleted_count:
        print("🗑️ Jugador eliminado.")
    else:
        print("❌ No se encontró un jugador con ese nombre.")
