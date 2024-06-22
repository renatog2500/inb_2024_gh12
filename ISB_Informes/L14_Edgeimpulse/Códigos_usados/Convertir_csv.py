import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, iirfilter
import re
import pandas as pd
#import pywt

# Cargar los datos desde el archivo TXT
archivo = "C:/Users/Equipo/OneDrive/Escritorio/Introduccion_a_señales_biomedicas/Github/inb_2024_gh12/Documentación/EMG/Lectura_bicep_braquial_EMG.txt"
# Cargar datos desde el archivo de texto según la ubicación del 
#archivo = "C:/Users/Jossymar/Desktop/Introduccion a señales/github/inb_2024_gh12/Documentación/EMG/Lectura_bicep_braquial_EMG.txt"

def extraer_nombres_columnas(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            if linea.startswith("#"):
                columnas = re.findall(r'column":\s*\[(.*?)\]', linea)
                entrada = re.findall(r'label":\s*\[(.*?)\]', linea)
                if columnas:
                    if entrada:
                        # Extraer la lista de nombres de columna de la línea
                        column_names = [name.strip().strip('"') for name in columnas[0].split(',')]
                        # Extraemos los canales usados
                        entrada = [name.strip().strip('"') for name in entrada[0].split(',')]
                        return column_names, entrada [0]
                    else:
                        continue
                else:
                    continue


                    
#Me devuelve una tupla pues esta en "(...)"
nombres_columnas, Entrada=extraer_nombres_columnas(archivo) #Aquí te devuelve la lista como un string dentro de otra lista y también el nombre del canal usado
#print(nombres_columnas) Imprime la lista: ['nSeq', 'I1', 'I2', 'O1', 'O2', 'A1']
#print(Entrada)
#Leyendo el TxT que nos da OpenSignal, podemos entender que las columnas para nuestro Dataframe serán las siguientes:
#Se le coloca una columna "NaN" debido a que en el txt cada ultimo valor de fila tiene un espacio que lee como NaN
#nombres_columnas = ["nSeq", "I1", "I2", "O1", "O2", "A1"]

#Una vez tenemos claro, convertirmos nuestro TXT un dataframe
#Eliminamos las 3 primeras filas
#Declaramos la separación de tabulación
#Se elimina la ultima fila debido a que en el txt cada ultimo valor de fila tiene un espacio que se lee como NaN
datos = pd.read_csv(archivo, sep='\t', skiprows=3, header=None, usecols=[0, 1 ,2,3,4,5])

#Declaramos las columnas para poder tener una mejor observación del resultado
datos.columns = nombres_columnas

#Imprimimos el Dataframe resultante para ver si se obtuvo un buen resultado
#print(datos.columns)
#Comprobado el resultado solo escogemos la columna "A1", la cual usamos para nuestra medición
Lectura = datos[Entrada]
#print(Lectura)
# Convertir los datos a números
Lectura = Lectura.apply(pd.to_numeric)

"""
#Convertimos los valores digitales de una resoluciónde 10 bit a una analógica para un EEG
# Define the constants from the transfer function image
VCC = 3.3  # Operating voltage
G_EEG = 41782  # Sensor gain
n_bits = 10  # Number of bits for ADC

# Convert ADC to EEG(V)
Lectura = (Lectura / (2**n_bits) - 0.5) * VCC / G_EEG

# Convert EEG(V) to EEG(uV)
Lectura = Lectura * 1e6

# Crear un arreglo de tiempo en segundos
frecuencia_muestreo = 1000
tiempo = np.arange(len(Lectura))
"""


VCC = 3.3  # Operating voltage
G_EMG = 1009  # Sensor gain
n_bits = 10  # Number of bits for ADC

# Convert ADC to EEG(V)
#Lectura = (Lectura / ((2**n_bits) - 0.5)) * VCC / G_EEG
ecg = ((((Lectura)/(2**n_bits))-1/2)*VCC)/G_EMG

# Convert EEG(V) to EEG(uV)
ecg = ecg * 1e3

# Crear un arreglo de tiempo en segundos
frecuencia_muestreo = 1000
tiempo = np.arange(len(ecg)) 

# Frecuencia de corte de los filtros
cutoff_frequency_fir = 25 / (frecuencia_muestreo / 2)
cutoff_frequency_iir= 25 / (frecuencia_muestreo/2) # Normalización de la frecuencia de corte
cutoff_frequency_iir1 = 482 / (frecuencia_muestreo / 2)

# Diseñar filtros
num_taps = 101
fir_filter = firwin(num_taps, cutoff_frequency_fir,window="hamming")
iir_filter = iirfilter(N=4, Wn=[cutoff_frequency_iir,cutoff_frequency_iir1], btype='band', ftype='butter')


# Aplicar los filtros
#ecg_fir = lfilter(fir_filter, 1.0, Lectura)
ecg_iir = lfilter(iir_filter[0], iir_filter[1], ecg)
#ecg_wavelet, _ = pywt.dwt(ecg, wavelet_filter)

# Convertir ecg_iir a uen DataFrame
df_ecg_iir = pd.DataFrame({'timestamp': tiempo, 'Signal': ecg_iir})

# Guardar el DataFrame en un archivo CSV
df_ecg_iir.to_csv('emg2_Jossymar.csv', index=False)

print("Archivo ecg_iir.csv guardado exitosamente.")
