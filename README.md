* Codigos/

 1. variables_operaciones/


Contiene ejemplos de:

- Operaciones matemáticas: suma, resta, multiplicación, división, etc.
- Operadores de comparación: `==`, `!=`, `>`, `<`, etc.
- Operadores lógicos: `and`, `or`, `not`.
- Funciones básicas con strings, listas y diccionarios.
- Conversión de tipos: `str()`, `list()`, `float()`, etc.

 tipos_datos.py
- Declaración de diferentes tipos de variables: `int`, `float`, `str`, `bool`, `list`.
- Uso de la función `type()` para verificar el tipo de cada variable.

---

2. ciclos/
condicionales/

 ciclos
 condicionales.py
- Ejemplos con bucles `for` y `while`.
- Uso de condicionales `if`, `elif`, `else`.
- Instrucciones especiales como `break`, `continue` y `else` en bucles.

---

3. crud_nativo/

crud.py
- Sistema CRUD básico (Crear, Leer, Actualizar, Eliminar) usando Python puro.
- Puede usarse con MONGO

---

investigacion_libreria/

pillow_investigacion.py
Investigación sobre la librería Pillow

-  Funcionalidad:** Sirve para abrir, modificar y guardar imágenes en Python.
-  Sintaxis básica:**
  python
  from PIL import Image
  imagen = Image.open("ejemplo.jpg")
  imagen.show()
  imagen = imagen.convert("L")
  imagen.save("modificada.jpg")
