def saludar():
    print("Hola, bienvenido a funciones")

def saludar_persona(nombre):
    print(f"Hola, {nombre}", "un gusto my bro")

    def suma(a, b):
        resultado = a + b
        return resultado
    
    def verificar_edad(edad):
        if edad >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")
 
    def programa_completo():
      saludar()
    nombre = input("¿Cuál es tu nombre?: ")
    saludar_persona(nombre)

    n1 = int(input("Ingresa un número: "))
    n2 = int(input("Ingresa otro número: "))
    resultado = suma (n1, n2)
    print(f"El resultado de la suma es: {resultado}")
 

 
 