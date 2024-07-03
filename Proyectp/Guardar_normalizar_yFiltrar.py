import pywt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

def wavelet_denoising_emg(signal, wavelet, level, threshold_method='universal'):
    # Descomposición wavelet
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    
    # Estimación del umbral usando el método universal
    threshold = np.sqrt(2 * np.log(len(signal)))
    
    # Umbralización suave de los coeficientes de detalle
    for i in range(1, len(coeffs)):
        coeffs[i] = pywt.threshold(coeffs[i], threshold * np.median(np.abs(coeffs[i])) / 0.6745, mode='soft')
    
    # Reconstrucción de la señal
    denoised_signal = pywt.waverec(coeffs, wavelet)
    
    return denoised_signal

def extraer_nombres_columnas(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            if linea.startswith("#"):
                columnas = re.findall(r'column":\s*\[(.*?)\]', linea)
                entrada = re.findall(r'label":\s*\[(.*?)\]', linea)
                if columnas and entrada:
                    column_names = [name.strip().strip('"') for name in columnas[0].split(',')]
                    entrada = [name.strip().strip('"') for name in entrada[0].split(',')]
                    return column_names, entrada[0]

def calcular_rms_ventanas(signal, window_size):
    rms_values = []
    for start in range(0, len(signal), window_size):
        end = min(start + window_size, len(signal))
        window = signal[start:end]
        rms = np.sqrt(np.mean(window**2))
        rms_values.append(rms)
    return np.array(rms_values)

# Cargar los datos desde el archivo TXT
archivo = "renato3.txt"
nombres_columnas, Entrada = extraer_nombres_columnas(archivo)
datos = pd.read_csv(archivo, sep='\t', skiprows=3, header=None, usecols=[0, 1, 2, 3, 4, 5])
datos.columns = nombres_columnas
Lectura = datos[Entrada]

# Convertir los datos a números
emg = Lectura.apply(pd.to_numeric)
emg.index = emg.index / 1000
VCC = 3.3  # Operating voltage
G_EMG = 1009  # Sensor gain
n_bits = 10  # Number of bits for ADC

# Convertir ADC a EMG(V)
emg_v = ((((emg)/(2**n_bits))-1/2)*VCC)/G_EMG

# Convertir EMG(V) a EMG(uV)
emg_signal = emg_v * 1e3

# Parámetros del filtro wavelet óptimos según Phinyomark et al.
wavelet_type = 'db1'  # También puedes probar 'bior1.1' o 'rbio1.1'
decomposition_level = 4 

# Aplicar filtrado wavelet
denoised_emg = wavelet_denoising_emg(emg_signal, wavelet_type, decomposition_level)

# Calcular MVC (puedes ajustar esta parte según tu necesidad o valor medido previamente)
mvc = max(denoised_emg)  # Suponiendo que mvc es el máximo valor de la señal denoised_emg

# Normalizar la señal filtrada respecto al MVC
normalized_emg = denoised_emg / mvc

# Guardar la señal normalizada en un archivo CSV
normalized_emg_df = pd.DataFrame(normalized_emg)
normalized_emg_df.to_csv("Normalized_renato3.csv", index=True)
