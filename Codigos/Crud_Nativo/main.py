from create import crear_jugador
from read import listar_jugadores
from update import actualizar_jugador
from delete import eliminar_jugador

def menu():

    while True:
        print("\n--- MENÚ CRUD JUGADORES DE FÚTBOL (MongoDB) ---")
        print("1. Crear jugador")
        print("2. Listar jugadores")
        print("3. Actualizar jugador")
        print("4. Eliminar jugador")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            posicion = input("Posición: ")
            equipo = input("Equipo: ")
            crear_jugador(nombre, posicion, equipo)

        elif opcion == "2":
            listar_jugadores()

        elif opcion == "3":
            nombre_actual = input("Nombre actual del jugador a actualizar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_posicion = input("Nueva posición: ")
            nuevo_equipo = input("Nuevo equipo: ")
            actualizar_jugador(nombre_actual, nuevo_nombre, nueva_posicion, nuevo_equipo)

        elif opcion == "4":
            nombre = input("Nombre del jugador a eliminar: ")
            eliminar_jugador(nombre)

        elif opcion == "5":
            print(" ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
