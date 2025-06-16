from pymongo import MongoClient

def get_connection():
    # Cambia la URI si usas MongoDB Atlas o usuario/contraseña
    client = MongoClient("mongodb://localhost:27017/")
    db = client["futbol_db"]
    return db["jugadores"]
