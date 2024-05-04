import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz, lfilter, iirfilter, butter
import pywt
from scipy import signal
# Cargar los datos desde el archivo TXT
archivo_txt = "C:/Users/Equipo/OneDrive/Escritorio/Introduccion_a_señales_biomedicas/Github/inb_2024_gh12/ISB_Informes/L4_Lectura_de_ECG/ECG_L4/Post_ejercicio.txt"
datos_emg = np.loadtxt(archivo_txt)
ecg = datos_emg[:, 5]  # Sexta columna

VCC = 3.3  # Operating voltage
G_EMG = 1100  # Sensor gain
n_bits = 10  # Number of bits for ADC

# Convert ADC to EEG(V)
#Lectura = (Lectura / ((2**n_bits) - 0.5)) * VCC / G_EEG
#ecg = ((((ecg)/(2**n_bits))-1/2)*VCC)/G_EMG

# Convert EEG(V) to EEG(uV)
#ecg = ecg * 1e3

# Crear un arreglo de tiempo en segundos
frecuencia_muestreo = 1000
tiempo = np.arange(len(ecg)) / frecuencia_muestreo

N=2**10 # 10 bits

X3 = np.fft.fft(ecg,N)
X3 = X3[0:N//2]
X3m = np.abs(X3)
F = np.linspace(0,1000/2,N//2)

band = [25, 457]  # Frecuencias de corte para el rechazo
trans_width = 0.3  # Anchura de la banda de transición en Hz
numtaps = 401      # Número de coeficientes del filtro (orden + 1)

# Diseño del filtro
taps = firwin(numtaps, [band[0] - trans_width, band[1] + trans_width], pass_zero=True, fs=1000)
# Aplicación del filtro
filtered_data = lfilter(taps, 1.0, ecg)

# Respuesta en frecuencia
freq, response = freqz(taps, worN=8000, fs=1000)
amplitude = np.abs(response)

N=2**10 # 10 bits

X4 = np.fft.fft(filtered_data,N)
X4 = X4[0:N//2]
X4m = np.abs(X4)
F = np.linspace(0,1000/2,N//2)

plt.plot(F, X3m)
plt.grid(linestyle=":")
plt.title("Analisis espectral de las señales")
plt.xlabel("Frecuencias (hz)")
plt.ylabel("FFT (db)")

peaks, properties = signal.find_peaks(X3m, height=100)
plt.plot(F[peaks],properties["peak_heights"],"x")
plt.text(F[peaks][0],properties["peak_heights"][0], f"{np.round(F[peaks][0],2)} hz")
plt.text(F[peaks][1],properties["peak_heights"][1], f"{np.round(F[peaks][1],2)} hz")

plt.show()
# Señal filtrada
# Define el intervalo de tiempo que deseas visualizar (segundos)
inicio_segundo = 5
fin_segundo = 8
inicio_muestra = int(inicio_segundo * frecuencia_muestreo)
fin_muestra = int(fin_segundo * frecuencia_muestreo)
plt.plot(filtered_data[inicio_muestra:fin_muestra], label='Filtered Signal', color='orange')
plt.title('Señal Filtrada')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()

plt.plot(F, X4m)
plt.grid(linestyle=":")
plt.title("Analisis espectral de las señales")
plt.xlabel("Frecuencias (hz)")
plt.ylabel("FFT (db)")

peaks, properties = signal.find_peaks(X4m, height=100)
plt.plot(F[peaks],properties["peak_heights"],"x")
plt.text(F[peaks][0],properties["peak_heights"][0], f"{np.round(F[peaks][0],2)} hz")
plt.text(F[peaks][1],properties["peak_heights"][1], f"{np.round(F[peaks][1],2)} hz")

plt.show()