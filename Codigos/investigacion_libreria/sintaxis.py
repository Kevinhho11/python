from PIL import Image


imagen = Image.open("ejemplo.jpg")


imagen.show()


nueva = imagen.resize((200, 200))


nueva.save("nueva_imagen.jpg")
