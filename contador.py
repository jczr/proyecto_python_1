# Programa para contar palabras en un archivo de texto
# 1. Pedir al usuario la ruta de un archivo de texto.
# 2. Leer el contenido del archivo.
archivo = input("Ingrese la ruta del archivo de texto: ")
try:
    with open(archivo, 'r') as file:
        texto = file.read()

except FileNotFoundError:
    print(f"El archivo {archivo} no fue encontrado, reitente por favor.")
    exit(1)


# 3. Separar en palabras.
# 4. Contar número total de palabras.

import re 
palabras = re.findall(r"\w+", texto.lower())  #\w+  significa que encuentra todas las palabras, y las convierte a minusculas.
total_palabras = len(palabras)
print(f"El archivo {archivo} tiene {total_palabras} palabras.")


# 5. (Opcional) Mostrar las 10 palabras más frecuentes y su conteo.

from collections import Counter
contador = Counter(palabras)
mas_comunes = contador.most_common(5)
print("palabras mas frecuentes:")
for palabra, freq in mas_comunes:
    print(f"{palabra}: {freq}")


