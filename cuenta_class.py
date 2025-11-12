# Programa para contar palabras en un archivo de texto
import re
from collections import Counter

class ContadorDePalabras:
    """Clase para contar palabras en archivos de texto."""
    
    def __init__(self):
        """Inicializa el contador."""
        self.texto = ""
        self.archivo = ""
    
    def leer_archivo(self, ruta_archivo):
        """
        Lee el contenido de un archivo de texto.
        
        Args:
            ruta_archivo (str): Ruta del archivo a leer
            
        Returns:
            bool: True si se leyó correctamente, False si hubo error
            
        Raises:
            FileNotFoundError: Si el archivo no existe
        """
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as file:
                self.texto = file.read()
                self.archivo = ruta_archivo
                return True
        except FileNotFoundError:
            print(f"El archivo {ruta_archivo} no fue encontrado.")
            return False
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return False
    
    def contar_palabras(self):
        """
        Cuenta el número total de palabras en el texto.
        
        Returns:
            int: Número total de palabras encontradas
        """
        if not self.texto:
            return 0
        
        palabras = re.findall(r"\w+", self.texto.lower())
        return len(palabras)
    
    def obtener_palabras_mas_frecuentes(self, cantidad=10):
        """
        Obtiene las palabras más frecuentes en el texto.
        
        Args:
            cantidad (int): Número de palabras más frecuentes a retornar
            
        Returns:
            list: Lista de tuplas (palabra, frecuencia) ordenadas por frecuencia
        """
        if not self.texto:
            return []
        
        palabras = re.findall(r"\w+", self.texto.lower())
        contador = Counter(palabras)
        return contador.most_common(cantidad)
    
    def mostrar_resultados(self, cantidad_frecuentes=10): #10 es el valor por defecto
        """
        Muestra los resultados del conteo de palabras.
        
        Args:
            cantidad_frecuentes (int): Número de palabras frecuentes a mostrar
        """
        total_palabras = self.contar_palabras()
        print(f"El archivo {self.archivo} tiene {total_palabras} palabras.")
        
        mas_comunes = self.obtener_palabras_mas_frecuentes(cantidad_frecuentes)
        if mas_comunes:
            print("palabras mas frecuentes:")
            for palabra, freq in mas_comunes:
                print(f"{palabra}: {freq}")


# Programa principal
if __name__ == "__main__":
    # 1. Pedir al usuario la ruta de un archivo de texto.
    archivo = input("Ingrese la ruta del archivo de texto: ")
    
    # 2. Crear instancia del contador y leer el archivo.
    contador = ContadorDePalabras()
    
    if contador.leer_archivo(archivo):
        # 3. Mostrar resultados
        contador.mostrar_resultados(cantidad_frecuentes=3) #3 es opcioneal, si no se incluye mostrara 10 pues asi se definio en la clase
    else:
        exit(1)