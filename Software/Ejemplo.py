import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz, lfilter, iirfilter, butter
import pywt

# Cargar los datos desde el archivo TXT
archivo_txt = "C:/Users/Equipo/OneDrive/Escritorio/Introduccion_a_señales_biomedicas/Github/inb_2024_gh12/Documentación/EMG/Lectura_antebrazo_supinación_EMG.txt"
datos_emg = np.loadtxt(archivo_txt)
ecg = datos_emg[:, 5]  # Sexta columna

VCC = 3.3  # Operating voltage
G_EMG = 1009  # Sensor gain
n_bits = 10  # Number of bits for ADC

# Convert ADC to EEG(V)
#Lectura = (Lectura / ((2**n_bits) - 0.5)) * VCC / G_EEG
ecg = ((((ecg)/(2**n_bits))-1/2)*VCC)/G_EMG

# Convert EEG(V) to EEG(uV)
ecg = ecg * 1e3

# Crear un arreglo de tiempo en segundos
frecuencia_muestreo = 1000
tiempo = np.arange(len(ecg)) / frecuencia_muestreo

# Frecuencia de corte de los filtros
cutoff_frequency_fir = 20 / (frecuencia_muestreo / 2) # Normalización de la frecuencia de corte


#Declaramos la frecuencia de corte para un filtro pasa banda
frecuencia_low_cut=50/ (frecuencia_muestreo / 2)
frecuencia_high_cut=400/ (frecuencia_muestreo / 2)

fs = 1000
# Diseñar filtros
num_taps = 101 # Número de coeficientes
fir_filter = firwin(num_taps, [frecuencia_low_cut, frecuencia_high_cut], window="hamming" ,pass_zero=False)
iir_filter = iirfilter(N=4, Wn=[frecuencia_low_cut, frecuencia_high_cut], btype='band', ftype='butter')

# Diseño del filtro rechazo de banda
# Parámetros del filtro
# Frecuencia de muestreo en Hz
notch_freq = 60  # Frecuencia a rechazar en Hz
bandwidth = 0.005  # Ancho de banda alrededor de la frecuencia a rechazar
f1 = notch_freq - bandwidth / 2
f2 = notch_freq + bandwidth / 2

# Crear filtro rechaza banda con ventana de Hamming
fir_coeff_notch = firwin(num_taps, [f1, f2], window='hamming', pass_zero=True, fs=fs)


# Respuesta en frecuencia del filtro FIR
w, h = freqz(fir_filter, worN=8000)
plt.figure(figsize=(9, 9))
plt.subplot(3, 1, 1)
plt.plot(0.5*frecuencia_muestreo*w/np.pi, np.abs(h), 'b')
plt.title('Respuesta en Frecuencia del Filtro FIR (hamming)')
plt.xlabel('Frecuencia [Hz]')
plt.grid(True)

# Respuesta en frecuencia del filtro IIR (Butterworth)
w, h = freqz(*butter(4, Wn=[frecuencia_low_cut, frecuencia_high_cut], btype='band'))
plt.subplot(3, 1, 2)
plt.plot(0.5*frecuencia_muestreo*w/np.pi, np.abs(h), 'g')
plt.title('Respuesta en Frecuencia del Filtro IIR (Butterworth) pasabanda')
plt.xlabel('Frecuencia [Hz]')
plt.grid(True)



w, h = freqz(fir_coeff_notch, worN=8000)
plt.subplot(3, 1, 3)
plt.plot(0.5*frecuencia_muestreo*w/np.pi, np.abs(h), 'g')
plt.title('Respuesta en Frecuencia del Filtro rechazabanda')
plt.xlabel('Frecuencia [Hz]')
plt.grid(True)
plt.tight_layout()

# Aplicar los filtros
ecg_x = lfilter(fir_coeff_notch, 1.0, ecg)
ecg_fir = lfilter(fir_filter, 1.0, ecg)
ecg_iir = lfilter(iir_filter[0], iir_filter[1], ecg)
#ecg_wavelet, _ = pywt.dwt(ecg, wavelet_filter)

# Define el intervalo de tiempo que deseas visualizar (segundos)
inicio_segundo = 0
fin_segundo = 18
inicio_muestra = int(inicio_segundo * frecuencia_muestreo)
fin_muestra = int(fin_segundo * frecuencia_muestreo)

# Crear gráficos de las señales filtradas
plt.figure(figsize=(12, 9))
plt.subplot(3, 1, 1)
plt.plot(tiempo[inicio_muestra:fin_muestra], ecg[inicio_muestra:fin_muestra], lw=1, color='blue')
plt.title('Valor ECG (Original')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(tiempo[inicio_muestra:fin_muestra], ecg_fir[inicio_muestra:fin_muestra], lw=1, color='red')
plt.title('Valor ECG del Filtro FIR (hanning) pasabanda')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(tiempo[inicio_muestra:fin_muestra], ecg_iir[inicio_muestra:fin_muestra], lw=1, color='green')
plt.title('Valor ECG Filtro IIR (Butterworth) pasabanda')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.grid(True)


plt.tight_layout()
plt.show()