import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz, lfilter, iirfilter, butter


# Cargar los datos desde el archivo TXT
archivo_txt = "C:/Users/Equipo/OneDrive/Escritorio/Introduccion_a_señales_biomedicas/Github/inb_2024_gh12/ISB_Informes/L5_Lectura_de_EEG/EEG_L5/BiTalino/Prueba_ojos_abiertos_cerrado_5s.txt"
datos = np.loadtxt(archivo_txt)
lectura = datos[:, 5]  # Sexta columna

fs = 1000
VCC = 3.3  # Operating voltage
G = 41782  # Sensor gain
n_bits = 10  # Number of bits for ADC

# Convert ADC to EEG(V)
#Lectura = (Lectura / ((2**n_bits) - 0.5)) * VCC / G_EEG
lectura = ((((lectura)/(2**n_bits))-1/2)*VCC)/G

# Convert EEG(V) to EEG(uV)
lectura = lectura * 1e6

# Crear un arreglo de tiempo en segundos
tiempo = np.arange(len(lectura)) / fs

# Frecuencia de corte de los filtros
cutoff_frequency = 60 / (fs / 2) # Normalización de la frecuencia de corte
iir_filter = iirfilter(N=5, Wn=[cutoff_frequency], btype='low', ftype='butter')

#Todo esto es para otros módulos para filtrar
    # #Declaramos la frecuencia de corte para un filtro pasa banda
    # frecuencia_low_cut=0.2/ (fs / 2)
    # frecuencia_high_cut=4/ (fs / 2)

    # Diseño del filtro rechazo de banda
    # Parámetros del filtro

    # Frecuencia de muestreo en Hz
    # notch_freq = 60  # Frecuencia a rechazar en Hz
    # bandwidth = 0.005  # Ancho de banda alrededor de la frecuencia a rechazar
    # f1 = notch_freq - bandwidth / 2
    # f2 = notch_freq + bandwidth / 2

#Declaramos la frecuencia de corte para un filtro pasa banda
wc_delta=[0.2/ (fs / 2), 4/ (fs / 2)]
wc_tetha=[4/ (fs / 2), 8/ (fs / 2)]
wc_alfa=[8/ (fs / 2), 12/ (fs / 2)]
wc_beta=[12/ (fs / 2), 24/ (fs / 2)]
wc_gamma=[24/ (fs / 2), 48/ (fs / 2)]

# Diseñar filtros
num_taps = 101 # Número de coeficientes
fir_filter_delta = firwin(num_taps, wc_delta, window="hann" ,pass_zero=False)

fir_filter_tetha = firwin(num_taps, wc_tetha, window="hann" ,pass_zero=False)

fir_filter_alfa = firwin(num_taps, wc_alfa, window="hann" ,pass_zero=False)

fir_filter_beta = firwin(num_taps, wc_beta, window="hann" ,pass_zero=False)

fir_filter_gamma = firwin(num_taps, wc_gamma, window="hann" ,pass_zero=False)




# Respuesta en frecuencia del filtro FIR
w, h = freqz(fir_filter_delta, worN=8000)
plt.figure(figsize=(9, 9))
plt.subplot(6, 1, 2)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.title('Respuesta en Frecuencia del Filtro FIR (hanning)')
plt.xlabel('Frecuencia [Hz]')
plt.grid(True)

# Respuesta en frecuencia del filtro IIR (Butterworth)
w, h = freqz(*butter(4, Wn=[cutoff_frequency], btype='low'))
plt.subplot(6, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'g')
plt.title('Respuesta en Frecuencia del Filtro IIR (Butterworth) pasabaja')
plt.xlabel('Frecuencia [Hz]')
plt.grid(True)

w, h = freqz(fir_filter_tetha, worN=8000)

plt.subplot(6, 1, 3)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'r')
plt.title('Respuesta en Frecuencia del Filtro FIR (hanning)')
plt.xlabel('Frecuencia [Hz]')
plt.grid(True)

w, h = freqz(fir_filter_alfa, worN=8000)

plt.subplot(6, 1, 4)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'brown')
plt.title('Respuesta en Frecuencia del Filtro FIR (hanning)')
plt.xlabel('Frecuencia [Hz]')
plt.grid(True)

w, h = freqz(fir_filter_beta, worN=8000)

plt.subplot(6, 1, 5)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'pink')
plt.title('Respuesta en Frecuencia del Filtro FIR (hanning)')
plt.xlabel('Frecuencia [Hz]')
plt.grid(True)

w, h = freqz(fir_filter_gamma, worN=8000)

plt.subplot(6, 1, 6)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'black')
plt.title('Respuesta en Frecuencia del Filtro FIR (hanning)')
plt.xlabel('Frecuencia [Hz]')
plt.grid(True)

plt.tight_layout()

# Aplicar los filtros
eeg_iir = lfilter(iir_filter[0], iir_filter[1], lectura)

eeg_fir_delta = lfilter(fir_filter_delta, 1.0, eeg_iir)
eeg_fir_tetha = lfilter(fir_filter_tetha, 1.0, eeg_iir)
eeg_fir_alfa = lfilter(fir_filter_alfa, 1.0, eeg_iir)
eeg_fir_beta = lfilter(fir_filter_beta, 1.0, eeg_iir)
eeg_fir_gamma = lfilter(fir_filter_gamma, 1.0, eeg_iir)

# Define el intervalo de tiempo que deseas visualizar (segundos)
inicio_segundo = 25
fin_segundo = 50
inicio_muestra = int(inicio_segundo * fs)
fin_muestra = int(fin_segundo * fs)

# Crear gráficos de las señales filtradas
plt.figure(figsize=(12, 9))
plt.subplot(7, 1, 1)
plt.plot(tiempo[inicio_muestra:fin_muestra], lectura[inicio_muestra:fin_muestra], lw=1, color='blue')
plt.title('Valor EEG (Original) Prueba_ojos_abiertos_cerrado_5s')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (uV)')
plt.grid(True)

plt.subplot(7, 1, 3)
plt.plot(tiempo[inicio_muestra:fin_muestra], eeg_fir_delta[inicio_muestra:fin_muestra], lw=1, color='red')
plt.title('Valor EEG del Filtro FIR (blackman) pasabanda para ondas delta')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (uV)')
plt.grid(True)

plt.subplot(7, 1, 2)
plt.plot(tiempo[inicio_muestra:fin_muestra], eeg_iir[inicio_muestra:fin_muestra], lw=1, color='green')
plt.title('Valor EEG Filtro IIR (Butterworth) pasabaja')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (uV)')
plt.grid(True)

plt.subplot(7, 1, 4)
plt.plot(tiempo[inicio_muestra:fin_muestra], eeg_fir_tetha[inicio_muestra:fin_muestra], lw=1, color='yellow')
plt.title('Valor EEG del Filtro FIR (blackman) pasabanda para ondas tetha')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (uV)')
plt.grid(True)

plt.subplot(7, 1, 5)
plt.plot(tiempo[inicio_muestra:fin_muestra], eeg_fir_alfa[inicio_muestra:fin_muestra], lw=1, color='pink')
plt.title('Valor EEG del Filtro FIR (blackman) pasabanda para ondas alfa')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (uV)')
plt.grid(True)

plt.subplot(7, 1, 6)
plt.plot(tiempo[inicio_muestra:fin_muestra], eeg_fir_beta[inicio_muestra:fin_muestra], lw=1, color='brown')
plt.title('Valor EEG del Filtro FIR (blackman) pasabanda para ondas beta')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (uV)')
plt.grid(True)

plt.subplot(7, 1, 7)
plt.plot(tiempo[inicio_muestra:fin_muestra], eeg_fir_gamma[inicio_muestra:fin_muestra], lw=1, color='black')
plt.title('Valor EEG del Filtro FIR (blackman) pasabanda para ondas gamma')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')

plt.grid(True)
plt.tight_layout()
plt.show()