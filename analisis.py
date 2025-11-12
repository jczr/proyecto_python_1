import pandas as pd
import matplotlib.pyplot as plt

# Abrir el archivo CSV
df = pd.read_csv('datos.csv', header=None)

# Mostrar información básica del DataFrame
print("Primeras filas del DataFrame:")
print(df.head())
"""
print("\nInformación del DataFrame:")
print(df.info())
print("\nEstadísticas descriptivas:")
print(df.describe())
"""
df.columns=['Emp','CC']
print("\nMedia de cada columna:")
print(f"Media de 'Emp': {df['Emp'].mean()}")
print(f"Media de 'CC': {df['CC'].mean()}")

print(f"desviacion std de 'Emp': {df['Emp'].std()}")

print("Media de EMP:")
print(df['Emp'].median())

# Crear scatter plot de Emp vs CC
plt.figure(figsize=(8, 6))
plt.scatter(df['CC'], df['Emp'], alpha=0.6)
plt.xlabel('CC')
plt.ylabel('Emp')
plt.title('Scatter Plot 2025: Emp vs CC')
plt.grid(True, alpha=0.3)
plt.show()

