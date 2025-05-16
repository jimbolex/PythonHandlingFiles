try:
    # Segundo parametro de la funcion Open para escribir en archivos:
    # w = Escribe informacion. Si el archivo ya existe y ya tiene informacion, la borra y escribe de nuevo.
    # a = Escribe agregando informacion y no borra datos existentes del archivo.
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write("texto prueba 1\n")
    archivo.write("texto prueba 2\n")
    archivo.write("texto prueba 3\n")
    archivo.write("texto prueba 4 con un texto con acento como árbol\n")
except Exception as e:
    print(e)
finally:
    archivo.close()