import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde el archivo de texto según la ubicación del archivo
archivo = 'C:/Users/Equipo/OneDrive/Escritorio/Introduccion_a_señales_biomedicas/Github/inb_2024_gh12/ISB_Informes/L5_Lectura_de_EEG/EEG_L5/EEG_Casco/OpenBCI-RAW-2024-04-26_12-42-53.txt'
columnas = ["Ch 0", "Ch 1", "Ch 2", "Ch 3", "Ch 4", "Ch 5", "Ch 6", "Ch 7", "Ch 8", "Ch 9", "Ch 10", "Ch 11", "Ch 12", "Ch 13", "Ch 14", "Ch 15"]

# Definir las constantes del ADC
vref = 4.5  # Voltaje de referencia en volts
ganancia = 12  # Ganancia del ADC
resolucion = 24  # Resolución en bits

# Calcular el voltaje por bit en volts
voltaje_por_bit = vref / (ganancia * (2**resolucion - 1))

# Load the data
data = pd.read_csv(archivo, skiprows=5, usecols=range(1, 17))

# Convertir de bits a voltaje y luego a microvoltios
data = data * voltaje_por_bit * 1e6  # Multiplica por 1e6 para convertir de V a uV

# Imprimir los primeros datos transformados
print(data.head())

# Plotting
plt.figure(figsize=(250, 100))  # Tamaño de figura más razonable
for i in range(16):
    plt.subplot(16, 1, i+1)
    plt.plot(data.iloc[:, i])
    plt.title(f'EXG Channel {i}')
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud (uV)")
    plt.grid(True)
    plt.grid(True)

plt.tight_layout()
plt.show()
