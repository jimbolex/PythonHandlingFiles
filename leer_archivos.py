try:
    archivo = open('prueba.txt', 'r', encoding='utf8')

    # Leer archivo completo
    # print(archivo.read())

    # Iterar lineas de un archivo
    # for linea in archivo:
    #     print(linea)

    # Leer lineas como un arreglo o lista
    # print(archivo.readlines())

    # Leer linea especifica de un arreglo o lista
    print(archivo.readlines()[0])
except Exception as e:
    print(e)
finally:
    archivo.close()