import pandas as pd
import matplotlib.pyplot as plt


def interpret16bitAsInt32(two_byte_value):
    # Asume que two_byte_value es un entero de 16 bits y extrae los bytes
    high_byte = (two_byte_value >> 8) & 0xFF
    low_byte = two_byte_value & 0xFF
    
    # Combina los bytes en un nuevo entero de 16 bits
    newInt = (high_byte << 8) | low_byte
    
    # Extiende el signo si es necesario
    if newInt & 0x8000:  # Si el bit de signo está establecido
        newInt = newInt - 0x10000  # Extiende el signo a 32 bits
        
    return newInt


# Asumiendo que 'data' es un DataFrame de pandas con los datos del ADC

# Cargar datos desde el archivo de texto según la ubicación del archivo
archivo = "C:/Users/Equipo/OneDrive/Escritorio/Introduccion_a_señales_biomedicas/Github/inb_2024_gh12/ISB_Informes/L5_Lectura_de_EEG/EEG_L5/EEG_Casco/OpenBCI-RAW-mate_Grupo_12.txt"

# Definir las constantes del ADC
vref = 4.5  # Voltaje de referencia en volts
ganancia = 24  # Ganancia del ADC
resolucion = 24  # Resolución en bits

# Calcular el voltaje por bit en volts
voltaje_por_bit = vref / (ganancia) /(2**24 - 1)

# Load the data
data = pd.read_csv(archivo, skiprows=5, usecols=range(1, 17))

# Convertir los datos a enteros si no lo son ya
data = data.applymap(int)

# Aplica la función de interpretación a cada elemento
data_signed_32 = data.applymap(interpret16bitAsInt32)

data_centered = data_signed_32.sub(data_signed_32.mean(axis=0), axis=1)

# Convertir de bits a voltaje y luego a microvoltios
data_uV = data_centered * voltaje_por_bit * 1e6  # Multiplica por 1e6 para convertir de V a uV

# Imprimir los primeros datos transformados
print(data_uV)

#print(Lectura)
data_uV.index = data_uV.index / 1000

# Plotting
fig, axes = plt.subplots(16, 1, figsize=(150, 100))  # Crea una figura y un conjunto de subplots
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
    '#bcbd22', '#17becf', '#1b9e77', '#d95f02',
    '#7570b3', '#e7298a', '#66a61e', '#e6ab02',
]

for i in range(16):
    axes[i].plot(data_uV.iloc[:, i],color=colors[i])
    axes[i].set_title(f'EXG Channel {i+1}', fontsize=8)
    axes[i].grid(True)

# Configuración de la figura
fig.tight_layout()
fig.subplots_adjust(top=0.95)

# Agrega un título general a la figura completa
fig.suptitle("EEG Channel Outputs para estado de preguntas matematicas", fontsize=14)

# Configurar etiquetas para toda la figura (ajuste las coordenadas según sea necesario)
fig.text(0.5, 0.005, 'Time', ha='center', va='center', fontsize=12)
fig.text(0.005, 0.5, 'Amplitude (uV)', ha='center', va='center', rotation='vertical', fontsize=12)

plt.show()