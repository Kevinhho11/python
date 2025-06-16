canasta = ['manzana', 'pera', 'naranja', 'plátano', 'kiwi']
def buscar_elemento(canasta, elemento):
    if elemento in canasta:
        return f"El elemento '{elemento}' se encuentra en la canasta."
    else:
        return f"El elemento '{elemento}' no se encuentra en la canasta."
elemento_a_buscar = input ("Ingresa tu fruta")
print(buscar_elemento(canasta, elemento_a_buscar))  








