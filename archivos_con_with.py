# Usar la palabra reservada with ayuda a abrir y cerrar archivos sin definir el comando close
with open('prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())