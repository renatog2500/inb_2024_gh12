# Laboratorio N°6 - Diseño de Filtros IIR y FIR 

## Tabla de contenidos:
 __________________________________________________________________________________________________
1. [Lista de participantes](#t1)
2. [Introducción](#t2)
3. [Objetivos del laboratorio](#t3)
4. [Metodología](#t4)
6. [Resultados](#t5)\
   5.1 [Ejercicio ECG](#t6)\
   5.2 [Ejercicio EMG ](#t7)\
   5.3 [Ejercicio EEG](#t8)
7. [Discusión](#t9)\
   6.1 [Señal ECG](#t10)\
   6.2 [Señal EMG](#t11)\
   6.3 [Señal EEG](#t12)\
8. [Bibliografía](#t13)
__________________________________________________________________________________________________
## **Lista de participantes** <a name = "t1"></a>
* Jimena Alpiste Espinoza - 74297329
* Jossymar León Mallma - 74905684
* Renato Cardoso Cardenas - 73061678


## Introducción  <a name = "t2"></a>

**Filtros Digitales**

En el procesamiento de señales, los filtros digitales surgen como una herramienta que permite manipular las características de las señales como la forma, amplitud, frecuencia o fase de una onda de interés . Los objetivos comunes del filtrado son mejorar la calidad de una señal que requiera suprimir el ruido , extraer información relevante o la separación de señales combinadas [1]. 

Mediante algoritmos matemáticos implementados en hardware o software, los filtros digitales pueden adaptarse de manera flexible a diferentes requisitos de filtrado, ofreciendo una solución precisa y adaptable para una amplia gama de aplicaciones en el procesamiento de señales. En comparación con los filtros analógicos, estos se prefieren en una amplia gama de aplicaciones biomédicas por las siguientes ventajas [1]: 
- Ofrecen  una respuesta de fase  lineal, una característica que no es posible lograr con los filtros analógicos.
- Su rendimiento no se ve afectado por cambios ambientales, como las variaciones térmicas. Lo cual elimina la necesidad de realizar ajustes o calibraciones periódicas para mantener su funcionamiento óptimo.
- Permiten filtrar varias señales o canales de entrada sin necesidad de replicar el hardware, lo que resulta en una mayor eficiencia y flexibilidad.
- Tanto los datos filtrados como los no filtrados pueden ser almacenados para su posterior uso, brindando una mayor capacidad de procesamiento y análisis.

<div align="center">
     <img src="Imagenes_L6/Filtro digital intro.png" alt="wCF14V">
    <p><b>Figura 1. Representación de un filtro digital </b> - Extraído de [1] </p>
</div>
## **Objetivos  Laboratorio** <a name = "t3"></a>
* Comprender los principios básicos de filtros digitales, en particular, los relacionados con los filtros de respuesta infinita al impulso (IRR) y los de respuesta finita al impulso (FIR).
* Filtrar las señales ECG, EMG y EEG para la eliminación de ruidos y artefactos
* Analizar las señales obtenidas y extraer características de interés de cada una. 
  
## Metodología <a name="t4"></a>
aqui colocar el codigo utilizado 
**-Código de ploteo para EEG y adquisición de las ondas cerebrales:**
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz, lfilter, iirfilter, butter
import pywt

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
```

**-Código de ploteo para EMG y ECG:**
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz, lfilter, iirfilter, butter
import pywt

# Cargar los datos desde el archivo TXT
archivo_txt = "C:/Users/Equipo/OneDrive/Escritorio/Introduccion_a_señales_biomedicas/Github/inb_2024_gh12/ISB_Informes/L4_Lectura_de_ECG/ECG_L4/Post_ejercicio.txt"
datos_emg = np.loadtxt(archivo_txt)
ecg = datos_emg[:, 5]  # Sexta columna

VCC = 3.3  # Operating voltage
G_EMG = 1100  # Sensor gain
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
cutoff_frequency_fir = 25 / (frecuencia_muestreo / 2)
cutoff_frequency_iir= 20 / (frecuencia_muestreo/2) # Normalización de la frecuencia de corte
#cutoff_frequency_iir = 25 / (frecuencia_muestreo / 2)

# Diseñar filtros
num_taps = 101
fir_filter = firwin(num_taps, cutoff_frequency_fir,window="hamming")
iir_filter = iirfilter(N=4, Wn=cutoff_frequency_iir, btype='low', ftype='butter')


# Respuesta en frecuencia del filtro FIR
w, h = freqz(fir_filter, worN=8000)
plt.figure(figsize=(9, 9))
plt.subplot(3, 1, 1)
plt.plot(0.5*frecuencia_muestreo*w/np.pi, np.abs(h), 'b')
plt.title('Respuesta en Frecuencia del Filtro FIR')
plt.xlabel('Frecuencia [Hz]')
plt.grid(True)

# Respuesta en frecuencia del filtro IIR (Butterworth)
w, h = freqz(*butter(4, cutoff_frequency_iir, btype='low'))
plt.subplot(3, 1, 2)
plt.plot(0.5*frecuencia_muestreo*w/np.pi, np.abs(h), 'g')
plt.title('Respuesta en Frecuencia del Filtro IIR (Butterworth)')
plt.xlabel('Frecuencia [Hz]')
plt.grid(True)
plt.tight_layout()
# El filtro Wavelet no es un filtro en el dominio de la frecuencia 

# Aplicar los filtros
ecg_fir = lfilter(fir_filter, 1.0, ecg)
ecg_iir = lfilter(iir_filter[0], iir_filter[1], ecg)
#ecg_wavelet, _ = pywt.dwt(ecg, wavelet_filter)

# Define el intervalo de tiempo que deseas visualizar (segundos)
inicio_segundo = 5
fin_segundo = 8
inicio_muestra = int(inicio_segundo * frecuencia_muestreo)
fin_muestra = int(fin_segundo * frecuencia_muestreo)

# Crear gráficos de las señales filtradas
plt.figure(figsize=(12, 9))
plt.subplot(3, 1, 1)
plt.plot(tiempo[inicio_muestra:fin_muestra], ecg[inicio_muestra:fin_muestra], lw=1, color='blue')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valor ECG (Original)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(tiempo[inicio_muestra:fin_muestra], ecg_fir[inicio_muestra:fin_muestra], lw=1, color='red')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valor ECG (FIR Filtro)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(tiempo[inicio_muestra:fin_muestra], ecg_iir[inicio_muestra:fin_muestra], lw=1, color='green')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valor ECG (IIR Filtro)')
plt.grid(True)


plt.tight_layout()
plt.show()
```

## Resultados   <a name="t5"></a>

### **Ejercicio ECG** <a name="t6"></a>


### **Ejercicio EMG** <a name="t7"></a>


### **Ejercicio EEG** <a name="t8"></a>


## Discusión <a name="t9"></a>


### **ECG** <a name="t10"></a>


### **EMG** <a name="t11"></a>


### **EEG** <a name="t12"></a>



## ** Bibliografía** : <a name="t13"></a>








