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

# Cargar los datos desde el archivo TXT
archivo = "C:/Users/Equipo/OneDrive/Escritorio/Introduccion_a_señales_biomedicas/Github/inb_2024_gh12/ISB_Informes/L5_Lectura_de_EEG/EEG_L5/BiTalino/Prueba_Preguntas_complejas.txt"

#Del código de ploteo de datos del laboratorio de emg
nombres_columnas,Entrada=extraer_nombres_columnas(archivo)
datos = pd.read_csv(archivo, sep='\t', skiprows=3, header=None, usecols=[0, 1 ,2,3,4,5])
datos.columns = nombres_columnas
Lectura = datos[Entrada]
# Convertir los datos a números
emg = Lectura.apply(pd.to_numeric)

emg.index = emg.index / 1000
VCC = 3.3  # Operating voltage
G_EMG = 41782  # Sensor gain
n_bits = 10  # Number of bits for ADC

# Convert ADC to EEG(V)
#Lectura = (Lectura / ((2**n_bits) - 0.5)) * VCC / G_EEG
emg_v = ((((emg)/(2**n_bits))-1/2)*VCC)/G_EMG

# Convert EEG(V) to EEG(uV)
emg_signal = emg_v * 1e6


# Parámetros del filtro wavelet óptimos según Phinyomark et al.
wavelet_type = 'db1'  # También puedes probar 'bior1.1' o 'rbio1.1'
decomposition_level = 6

# Aplicar filtrado wavelet
denoised_emg = wavelet_denoising_emg(emg_signal, wavelet_type, decomposition_level)

# Calcular MSE entre señal original y filtrada
mse = np.mean((emg_signal - denoised_emg) ** 2)
print(f"MSE: {mse:.4f}")

# Plotear la señal de EMG en el dominio del tiempo
plt.figure()
plt.subplot(121) 
plt.plot(emg_signal[0:15], label='Señal EEG original')
plt.title('Señal orignal de EEG Lectura de la prueba de preguntas complejas')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid(True)

plt.subplot(122)
plt.plot(emg.index[0:15000], denoised_emg[0:15000],label='Señal EMG filtrada',color="orange")
plt.title(f'Filtrado Wavelet de Señal EEG usando {wavelet_type}')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid(True)

plt.show() 
