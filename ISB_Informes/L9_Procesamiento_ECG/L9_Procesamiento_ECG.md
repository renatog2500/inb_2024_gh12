![image](https://github.com/renatog2500/inb_2024_gh12/assets/164541858/6322cb0c-a8e8-425b-a544-9fc7ad17bdd6)# Laboratorio N°8 - Procesamiento EMG

## Tabla de contenidos:
 __________________________________________________________________________________________________
1. [Lista de participantes](#t1)
2. [Introducción](#t2)
3. [Objetivos del laboratorio](#t3)
4. [Metodología](#t4)\
   4.1.[Materiales y Equipo utilizado](#t5)\
   4.2.[Procedimiento](#t6)\
       4.2.1.[Filtrado](#t7)\
       4.2.2.[Elección del filtro](#t8)\
       4.2.3.[Segmentación](#t9)\
       4.2.4.[Extracción de características](#t10)\
7. [Discusión](#t11)
8. [Conclusión](#t12)
9. [Archivos](#t13)
7. [Bibliografía](#t14)
__________________________________________________________________________________________________
## **Lista de participantes** <a name = "t1"></a>
* Jimena Alpiste Espinoza - 74297329
* Jossymar León Mallma - 74905684
* Renato Cardoso Cardenas - 73061678


## Introducción  <a name = "t2"></a>
La electromiografía (EMG) es una técnica versátil que nos permite estudiar las señales eléctricas generadas por la actividad muscular. En ella, se registran los potenciales eléctricos producidos por las corrientes iónicas que fluyen durante la contracción muscular, reflejando así la actividad neuromuscular [1]. Estas señales bioeléctricas son iniciadas por las neuronas motoras del sistema nervioso central, que controlan la función muscular [2].

Las señales EMG pueden clasificarse en dos tipos principales según el método de adquisición: EMG de superficie y EMG intramuscular. La EMG de superficie utiliza electrodos no invasivos colocados sobre la piel, mientras que la EMG intramuscular implica la inserción de electrodos dentro del músculo [3]. Actualmente, se prefieren las señales detectadas en la superficie debido a su carácter no invasivo y su capacidad para obtener información sobre el tiempo o la intensidad de la activación muscular superficial [3].

Las señales electromiográficas (EMG) se consideran altamente útiles como señales electrofisiológicas, tanto en el campo médico como en el de ingeniería. Sin embargo, cada vez que se captura una señal EMG del músculo, esta tiende a contaminarse con varios tipos de ruido. Factores como el movimiento de los electrodos, la actividad muscular cercana, las interferencias electromagnéticas y el ruido inherente de los dispositivos de adquisición pueden introducir artefactos indeseados en la señal [3].

Por lo tanto, un adecuado procesamiento de la señal EMG es crucial para eliminar o minimizar estos ruidos y obtener información confiable y significativa de la actividad neuromuscular. Técnicas avanzadas de procesamiento de señales, como el filtrado, la eliminación de artefactos y la extracción de características, son fundamentales para aprovechar al máximo el potencial de la EMG en aplicaciones médicas, biomecánicas y de ingeniería. 

**Adquisición de señales**

Las señales de electromiografía de superficie (sEMG) se caracterizan por no ser estacionarias, lo que implica que su comportamiento y características no permanecen constantes a lo largo del tiempo. A pesar de esta variabilidad, es posible capturar estas señales utilizando electrodos superficiales, tal como se mencionó anteriormente. 
Estos se pueden clasificar según su diseño y su disposición. En cuanto a la adquisición precisa de estas señales sEMG, el sensor utilizado debe cumplir con el teorema de muestreo de Nyquist-Shannon. Esto significa que la frecuencia de muestreo debe ser al menos el doble de la frecuencia más alta presente en las señales sEMG. Por lo tanto, se recomienda una frecuencia de muestreo superior a 1000 Hz para capturar adecuadamente estas señales [4].


**Pre procesamiento**

Basándonos en la investigación realizada por Moslhi. et. al. Las señales obtenidas a través de electrodos de superficie presentan una amplitud baja y un nivel considerable de ruido, lo que dificulta su análisis directo. Por lo tanto, es necesario realizar una serie de pasos de preparación antes de poder extraer información significativa de estas señales.

Los siguientes puntos han sido obtenidos de la referencia 4. 

* **Filtrado**: En esta etapa, se aplican técnicas de filtrado para eliminar cualquier tipo de interferencia no deseada presente en las señales electromiográficas. Esto ayuda a mejorar la calidad de los datos al eliminar artefactos y ruido, permitiendo un análisis más preciso y confiable.

* **Rectificación**: La rectificación es un proceso esencial que se utiliza para abordar la parte negativa de las señales electromiográficas. Al rectificar las señales, se convierten en valores absolutos, lo que facilita la interpretación de la activación neural y mejora la representación de la señal para su posterior análisis.

* **Normalización**: Dado que las señales electromiográficas pueden variar significativamente entre diferentes individuos, es crucial normalizar la amplitud de estas señales para poder compararlas de manera efectiva. La normalización implica ajustar las señales a un valor de referencia bajo condiciones idénticas, lo que facilita la comparación entre sujetos y mejora la eficiencia computacional en etapas posteriores de procesamiento. Sin embargo, para este laboratorio, no se realizará este análisis, ya que se estarán comparando las mediciones de una misma persona.

* **Segmentación**: La segmentación divide las señales procesadas en segmentos más pequeños, lo que facilita la extracción de características relevantes de cada segmento. Esta división en segmentos permite un análisis más detallado de las señales y ayuda a equilibrar la necesidad de extraer características precisas con la minimización de retrasos computacionales, especialmente en sistemas en tiempo real.

**Extracción de características:** 
La extracción de características es un paso crítico en el análisis de señales electromiográficas, donde se identifican y derivan atributos significativos de los datos preprocesados para mejorar la precisión de la clasificación. Esta etapa implica la selección y extracción de características relevantes de las señales, lo que ayuda a reducir la complejidad de los datos y simplifica los procesos de clasificación posteriores. La extracción de características puede incluir atributos como el dominio del tiempo, dominio de la frecuencia y dominio tiempo-frecuencia, con el objetivo de proporcionar información relevante para la clasificación precisa de las señales electromiográficas.



## **Objetivos del Laboratorio** <a name = "t3"></a>
* Examinar detalladamente cada etapa involucrada en la adquisición y análisis de señales electromiográficas (EMG), con el fin de comprender su funcionamiento y aplicación práctica de manera integral.
* Implementar diferentes técnicas de filtrado para la eliminación de ruido y artefactos presentes en las señales EMG, con el propósito de obtener señales más limpias y precisas para su posterior procesamiento.
* Evaluar y seleccionar el filtro más adecuado para el tratamiento de las señales EMG, mediante la comparación de su desempeño y la aplicación de criterios objetivos.
* Segmentar las señales EMG en ventanas temporales, a fin de facilitar su análisis y extracción de características en intervalos específicos.
* Aplicar métodos de extracción de características relevantes a partir de las señales EMG.
  
## Metodología <a name="t4"></a>
En este laboratorio, nos enfocaremos en el tratamiento de la señal de EMG adquirida previamente utilizando el Kit BITalino. 

### **Materiales y Equipo Utilizado** <a name="t5"></a>
<table align="center">
  <tr>
    <th>Modelo</th>
    <th>Descripción</th>
    <th>Cantidad</th>
  </tr>
  <tr>
    <td>(R)EVOLUTION</td>
    <td>Kit de BITalino</td>
    <td>1</td>
  </tr>
  <tr>
    <td>-</td>
    <td>Laptop</td>
    <td>1</td>
  </tr>
</table>
<p align="center">
  <b>Tabla 1. Materiales y equipos utilizados</b>
</p>

### **Procedimiento** <a name="t6"></a>

## Filtros para el procesamiento de EMG <a name="t7"></a>
El artículo "Surface Electromyography Signal Processing and Classification Techniques" [3] fue creado por Rubana et. al, aborda dos áreas principales en el procesamiento y clasificación de señales de electromiografía de superficie (sEMG). La primera área se enfoca en los métodos de preprocesamiento para eliminar posibles artefactos y ruido de las señales sEMG, con el objetivo de mejorar la calidad de la señal antes de su análisis posterior. La segunda área se centra en una explicación concisa de las diferentes técnicas utilizadas para procesar y clasificar las señales sEMG.

El propósito fundamental de este estudio fue revisar los desarrollos y avances más recientes relacionados con el procesamiento y clasificación de señales sEMG. Los autores realizaron una comparación de diversos métodos de análisis de señales sEMG en términos de su rendimiento, con el objetivo de proporcionar una evaluación más estandarizada y precisa de los hallazgos neurofisiológicos, de rehabilitación y de tecnología asistencial [3].

En el contexto de este laboratorio, este estudio resulta de gran relevancia ya que proporciona una base sólida para seleccionar y aplicar técnicas de filtrado adecuadas a las señales sEMG. En particular, nos enfocaremos en el uso de tres filtros basados en la transformada wavelet discreta (DWT) con diferentes funciones wavelet: Daubechies 2 (db2), Daubechies 4 (db4) y Daubechies 6 (db6), todas aplicadas a un nivel de descomposición 4.

La selección de estos filtros se basa en las recomendaciones y hallazgos presentados en el artículo, donde se destaca la capacidad de la DWT para reducir el ruido y preservar las características importantes de las señales sEMG. Además, el estudio sugiere que el nivel de descomposición 4 proporciona un buen compromiso en la reducción de ruido para diferentes niveles de contaminación de la señal.

**1. Transformada Wavelet Discreta (DWT) con filtro Daubechies 2 (db2):**

***Justificación de uso:*** La DWT con filtro db2 al nivel de descomposición 4 se seleccionó como una opción para filtrar señales EMG debido a su capacidad para reducir el ruido y preservar las características importantes de la señal.

| Parámetro                 | Valor                                                |
|---------------------------|----------------------------------------------------|
| Función wavelet           | Daubechies 2 (db2)                                |
| Nivel de descomposición   | 4                                                 |
| Método de umbralización   | Umbralización universal con estimación de sigma   |

<p align="center">
  <b>Tabla 2. Parametros para el filtro db2</b>
</p>

***Código de implementación***

```python
import pywt
import numpy as np

# Cargar la señal EMG
emg_signal = [...]

# Aplicar la DWT con filtro db2 al nivel de descomposición 4
coefficients = pywt.wavedec(emg_signal, 'db2', level=4)

# Estimar la desviación estándar del ruido
sigma = np.median(np.abs(coefficients[1])) / 0.6745

# Calcular el umbral universal
threshold = sigma * np.sqrt(2 * np.log(len(emg_signal)))

# Realizar la umbralización suave
coefficients_filtered = pywt.threshold(coefficients, threshold, mode='soft')

# Reconstruir la señal filtrada
emg_filtered_db2 = pywt.waverec(coefficients_filtered, 'db2')
```
<div align="center">
    <img src="Imagenes_L8/db2.JPG" alt="wCF14V" width="600">
    <p><b>Figura 1. Comparación visual gráfico filtrado en db2 vs original </b> </p>
</div>

**2.  Transformada Wavelet Discreta (DWT) con filtro Daubechies 4 (db4):**

***Justificación de uso:*** La DWT con filtro db4 al nivel de descomposición 4 se seleccionó debido a su capacidad para proporcionar un buen compromiso en la reducción de ruido y la preservación de características importantes en señales EMG con diferentes niveles de ruido.

| Parámetro                 | Valor                                                |
|---------------------------|----------------------------------------------------|
| Función wavelet           | Daubechies 4 (db4)                                |
| Nivel de descomposición   | 4                                                 |
| Método de umbralización   | Umbralización universal con estimación de sigma   |

<p align="center">
  <b>Tabla 2. Parametros para el filtro db4 </b>
</p>

***Código:***

```python

import pywt
import numpy as np

# Cargar la señal EMG
emg_signal = [...]

# Aplicar la DWT con filtro db4 al nivel de descomposición 4
coefficients = pywt.wavedec(emg_signal, 'db4', level=4)

# Estimar la desviación estándar del ruido
sigma = np.median(np.abs(coefficients[1])) / 0.6745

# Calcular el umbral universal
threshold = sigma * np.sqrt(2 * np.log(len(emg_signal)))

# Realizar la umbralización suave
coefficients_filtered = pywt.threshold(coefficients, threshold, mode='soft')

# Reconstruir la señal filtrada
emg_filtered_db4 = pywt.waverec(coefficients_filtered, 'db4')
```
<div align="center">
    <img src="Imagenes_L8/db4.JPG" alt="wCF14V" width="600">
    <p><b>Figura 2. Comparación visual gráfico filtrado en db4 vs original </b> </p>
</div>

**3. Transformada Wavelet Discreta (DWT) con filtro Daubechies 6 (db6):**

***Justificación del uso:*** La DWT con filtro db6 al nivel de descomposición 4 se seleccionó como otra opción para filtrar señales EMG, proporcionando un equilibrio entre la reducción de ruido y la preservación de características relevantes.


| Parámetro                           | Valor                                                                       |
|-------------------------------------|---------------------------------------------------------------------|
| Función wavelet                 | Daubechies 6 (db6)                                                  |
| Nivel de descomposición   | 4                                                                               |
| Método de umbralización   | Umbralización universal con estimación de sigma   |

<p align="center">
  <b>Tabla 3. Parametros para el filtro db6</b>
</p>

***Código:***

```python
import pywt
import numpy as np

# Cargar la señal EMG
emg_signal = [...]

# Aplicar la DWT con filtro db6 al nivel de descomposición 4
coefficients = pywt.wavedec(emg_signal, 'db6', level=4)

# Estimar la desviación estándar del ruido
sigma = np.median(np.abs(coefficients[1])) / 0.6745

# Calcular el umbral universal
threshold = sigma * np.sqrt(2 * np.log(len(emg_signal)))

# Realizar la umbralización suave
coefficients_filtered = pywt.threshold(coefficients, threshold, mode='soft')

# Reconstruir la señal filtrada
emg_filtered_db6 = pywt.waverec(coefficients_filtered, 'db6')
```
<div align="center">
    <img src="Imagenes_L8/db6.JPG" alt="wCF14V" width="600">
    <p><b>Figura 3. Comparación visual gráfico filtrado en db6 vs original </b> </p>
</div>

## Comparación de filtros  <a name="t8"></a>
En el artículo "Surface electromyography signal denoising via EEMD and improved wavelet thresholds" de Sun et al. [5], los autores comparan el rendimiento de diferentes algoritmos de filtrado de señales EMG utilizando tres métodos cuantitativos: la relación señal-ruido (SNR), que mide la relación entre la energía de la señal y la energía del error; la relación señal-ruido pico (PSNR), que representa la relación entre la máxima potencia posible de una señal y la potencia del ruido que afecta su fidelidad; y el error cuadrático medio (RMSE), que define la energía de la señal de error durante el filtrado. Los autores aplican estos métodos a señales EMG con diferentes niveles de ruido gaussiano blanco y comparan los resultados para determinar qué algoritmo logra el mejor rendimiento de filtrado. Haciendo estas comparaciones, se basan en los valores más altos de SNR y PSNR, y el valor más bajo de RMSE para determinar cuál es el mejor filtro utilizado. Donde el resuldato del código nos indicó que el tercer filtro es el mejor.

***Código:***

```python
import numpy as np

def snr(signal, filtered_signal):
    noise = signal - filtered_signal
    return 10 * np.log10(np.sum(signal**2) / np.sum(noise**2))

def psnr(signal, filtered_signal):
    mse = np.mean((signal - filtered_signal)**2)
    return 20 * np.log10(np.max(signal) / np.sqrt(mse))

def rmse(signal, filtered_signal):
    return np.sqrt(np.mean((signal - filtered_signal)**2))

def compare_filtering_methods(original_signal, filtered_signal1, filtered_signal2, filtered_signal3):
    snr_results = [snr(original_signal, filtered_signal) for filtered_signal in [filtered_signal1, filtered_signal2, filtered_signal3]]
    psnr_results = [psnr(original_signal, filtered_signal) for filtered_signal in [filtered_signal1, filtered_signal2, filtered_signal3]]
    rmse_results = [rmse(original_signal, filtered_signal) for filtered_signal in [filtered_signal1, filtered_signal2, filtered_signal3]]

    best_snr_index = np.argmax(snr_results)
    best_psnr_index = np.argmax(psnr_results)
    best_rmse_index = np.argmin(rmse_results)

    if best_snr_index == best_psnr_index == best_rmse_index:
        best_method = best_snr_index + 1
    else:
        best_method = np.argmax([snr_results[best_snr_index], psnr_results[best_psnr_index], -rmse_results[best_rmse_index]]) + 1

    print(f"SNR Results: {snr_results}")
    print(f"PSNR Results: {psnr_results}")
    print(f"RMSE Results: {rmse_results}")
    print(f"Best Filtering Method: Signal {best_method}")

# Load the original EMG signal and the three filtered signals
original_signal = signal_vm
filtered_signal1 = emg_filtered_db2 
filtered_signal2 = emg_filtered_db4 
filtered_signal3 = emg_filtered_db6 

# Compare the filtering methods
compare_filtering_methods(original_signal, filtered_signal1, filtered_signal2, filtered_signal3)
```
***Resultados***: 

<div align="center">
    <img src="Imagenes_L8/Resultado.JPG" alt="wCF14V" width="800">
    <p><b>Figura 4. Resultado del cálculo de SNR, PSNR, RMSE de cada filtro y cuál es el filtro ganador </b> </p>
</div>


<div align="center">
    <img src="Imagenes_L8/Comparacion_Visual.JPG" alt="wCF14V" width="800">
    <p><b>Figura 5. Comparación visual de los gráficos </b> </p>
</div>


## Segmentación  <a name="t9"></a>

El ventaneo es una técnica crucial para la extracción de características de las señales de electromiografía de superficie (sEMG) con el fin de reconocer movimientos y patrones musculares. Aunque existe una relación entre las regiones de actividad muscular y los movimientos de las extremidades, esta relación no es totalmente directa. La intensidad de la actividad muscular en función de la posición de los músculos activos proporciona una representación más precisa de estos movimientos complejos. En este contexto, la longitud de la ventana determina la cantidad de muestras utilizadas para el reconocimiento, dónde ventanas más grandes mejoran la precisión, pero a costa de una mayor latencia. Basándonos en la investigación del paper “An Improved Feature Extraction Method for Surface Electromyography Based on Muscle Activity Regions”  se emplea un algoritmo de ventana deslizante con una ventana de 1000 ms y un incremento de 200 ms para extraer características de sEMG de manera óptima [6].

Además, esta elección se respalda con lo expuesto en el artículo "A Review of Classification Techniques of EMG Signals during Isotonic and Isometric Contractions" [7], el cual indica que las distintas longitudes de los datos de EMG impactan en su error de clasificación. Se ha confirmado que el rendimiento de la clasificación de características se ve comprometido al emplear segmentos de longitud menor a 128 ms, lo que resulta en un sesgo alto y una variación considerable en las características.

Es importante destacar que en la generación de ventanas de datos se emplean dos métodos principales: adyacentes y superpuestos. En el caso de las ventanas adyacentes, la extracción y clasificación de características se lleva a cabo tras un cierto retraso de procesamiento, denotado como τ, que corresponde al tiempo necesario para calcular la característica y clasificar los datos [7]. Sin embargo, esta técnica presenta el inconveniente de que el procesador queda inactivo durante el tiempo restante de la longitud del segmento, como se menciona en la fuente " Moving Approximate Entropy and its Application to the Electromyographic Control of an Artificial Hand" [8].

Por consiguiente, se opta por el enfoque de ventaneo superpuesto, donde el nuevo segmento se desplaza sobre el segmento actual con un tiempo de incremento menor que la longitud del segmento. Si bien esta elección no mejora la precisión de la clasificación, resulta crucial para la utilización de segmentos de 200 ms a fin de evitar retrasos temporales significativos.[9].


***Código:***

```python
señal_filtrada=emg_filtered_db6
# Definir la duración de la ventana y el aumento en segundos
window_duration = 1.000  # 1000 ms
window_shift = 0.200     # 200 ms

# Convertir la duración de la ventana y el aumento a muestras
sampling_rate = len(señal_filtrada) / time[-1]  # Frecuencia de muestreo en muestras por segundo
window_size = int(window_duration * sampling_rate)
shift_size = int(window_shift * sampling_rate)

segundo=30
# Encontrar el índice a partir del cual la señal comienza desde el segundo 30
start_index = np.searchsorted(time, segundo)

# Segmentar la señal en ventanas a partir del segundo 9
segments = []
for start in range(start_index, len(signal_mv) - window_size + 1, shift_size):
    end = start + window_size
    segment = signal_mv[start:end]
    segments.append(segment)

# Convertir la lista de segmentos a un array numpy
segments = np.array(segments)

# Graficar algunos segmentos para ver los resultados
plt.figure(figsize=(12, 8))
for i in range(6):  # Graficar hasta 10 segmentos
    plt.subplot(5, 2, i + 1)
    plt.plot(np.arange(window_size) / sampling_rate, segments[i])
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Valor EMG')
    plt.title(f'Segmento {i+1} (a partir de {segundo}s)')
    plt.grid(True)

plt.tight_layout()
plt.show()
```

***Resultado***: 

<div align="center">
    <img src="Imagenes_L8/Segmentación.JPG" alt="wCF14V" width="1000">
    <p><b>Figura 6. Segmentación de la onda </b> </p>
</div>


## Extracción de características  <a name="t10"></a>

En el artículo "Surface Electromyography Signal Processing and Classification Techniques" [3], los autores respaldan la elección de la extracción de características en el dominio del tiempo para las señales de electromiografía de superficie (sEMG) en lugar de las técnicas en el dominio de la frecuencia y tiempo-frecuencia, debido a varias ventajas significativas.

En este contexto, las características en el dominio del tiempo, como el valor absoluto medio (MAV), la pendiente del valor absoluto medio, los cambios de signo de pendiente (SSC), las longitudes de forma de onda (WL) y los cruces por cero (ZC), desarrolladas por Hudgins et al., se han demostrado efectivas para representar patrones mioeléctricos. Los autores destacan que la selección de estas características resultó en una tasa de clasificación más alta en comparación con las señales sin procesar [3].

Además, se enfatiza la ventaja de las características en el dominio del tiempo sobre las técnicas de tiempo-frecuencia, ya que estas últimas, debido a su alta dimensionalidad y resolución, a menudo requieren recursos computacionales adicionales para la extracción de características [3].

***Código utilizado para la extracción de características:***

```python
def MAV(segment):
    return np.mean(np.abs(segment))

def MAV_slope(segment):
    mav_values = [np.mean(np.abs(segment[i:i+2])) for i in range(len(segment)-1)]
    return np.mean(np.abs(np.diff(mav_values)))

def SSC(segment):
    return np.sum(np.diff(np.sign(np.diff(segment))) != 0)

def WL(segment):
    return np.sum(np.abs(np.diff(segment)))

def ZC(segment, threshold=0):
    zero_crossings = np.where(np.diff(np.sign(segment)))[0]
    return np.sum(np.abs(segment[zero_crossings]) > threshold)

# Extraer características de los primeros 10 segmentos
features = []
for i in range(10):
    segment = segments[i]
    features.append({
        'MAV': MAV(segment),
        'MAV_slope': MAV_slope(segment),
        'SSC': SSC(segment),
        'WL': WL(segment),
        'ZC': ZC(segment)
    })

# Mostrar las características de los primeros 10 segmentos
#for i, feature_set in enumerate(features, start=1):
#    print(f"Segmento {i}:")
#    for feature_name, value in feature_set.items():
#        print(f"  {feature_name}: {value}")
#    print()

# Lista de colores
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']

# Graficar características
fig, axs = plt.subplots(5, 1, figsize=(12, 10))

mav_values = [f['MAV'] for f in features]
mav_slope_values = [f['MAV_slope'] for f in features]
ssc_values = [f['SSC'] for f in features]
wl_values = [f['WL'] for f in features]
zc_values = [f['ZC'] for f in features]

axs[0].bar(range(1, 11), mav_values, color=colors)
axs[0].set_title('MAV de los primeros 10 segmentos')
axs[0].set_ylabel('MAV')

axs[1].bar(range(1, 11), mav_slope_values, color=colors)
axs[1].set_title('Pendiente MAV de los primeros 10 segmentos')
axs[1].set_ylabel('Pendiente MAV')

axs[2].bar(range(1, 11), ssc_values, color=colors)
axs[2].set_title('SSC de los primeros 10 segmentos')
axs[2].set_ylabel('SSC')

axs[3].bar(range(1, 11), wl_values, color=colors)
axs[3].set_title('WL de los primeros 10 segmentos')
axs[3].set_ylabel('WL')

axs[4].bar(range(1, 11), zc_values, color=colors)
axs[4].set_title('ZC de los primeros 10 segmentos')
axs[4].set_ylabel('ZC')
axs[4].set_xlabel('Segmento')

plt.tight_layout()

plt.show()

```
***Resultado***: 

<div style="display: flex; justify-content: space-around;">
    <img src="Imagenes_L8/Segmentación.JPG" alt="Imagen 1" style="width: 45%; display: inline-block; margin-right: 10px;">
    <img src="Imagenes_L8/Comparación_características.JPG" alt="Imagen 2" style="width: 45%; display: inline-block;">
    <p><b>Figura 7. Comparación de carácteristicas obtenidas </b> </p>
</div>  

***Procesamiento mediante la libreria de opensingals***: 

```python
# Signal Samples
signal = emg_filtered_db6
time = bsnb.generate_time(signal)
# [Baseline Removal]
pre_pro_signal = signal - average(signal)

# [Signal Filtering]
low_cutoff = 10 # Hz
high_cutoff = 300 # Hz

# Application of the signal to the filter.
pre_pro_signal = bsnb.aux_functions._butter_bandpass_filter(pre_pro_signal, low_cutoff, high_cutoff, sr)
# [Application of TKEO Operator]
tkeo = []
for i in range(0, len(pre_pro_signal)):
    if i == 0 or i == len(pre_pro_signal) - 1:
        tkeo.append(pre_pro_signal[i])
    else:
        tkeo.append(power(pre_pro_signal[i], 2) - (pre_pro_signal[i + 1] * pre_pro_signal[i - 1]))
# Plotear la señal y los umbrales
plt.figure(figsize=(12, 6))
plt.plot(time, signal, lw=1, color='black', label='Original')
plt.plot(time, tkeo, lw=1, color='deepskyblue', label='Señal TKEO')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valor EMG')
plt.title('Aplicación del factor TKEO')
plt.legend()
plt.grid(True)
plt.show()

```
<div align="center">
    <img src="Imagenes_L8/original_TKEO.JPG" alt="wCF14V" width="1000">
    <p><b>Figura 8. Comparación de la señal orignal filtrada vs la TKEO </b> </p>
</div>

```python
# Smoothing level [Size of sliding window used during the moving average process (a function of sampling frequency)]
smoothing_level_perc = 20 # Percentage.
smoothing_level = int((smoothing_level_perc / 100) * sr)
# [Signal Rectification]
rect_signal = absolute(tkeo)
# [First Moving Average Filter]
rect_signal = bsnb.aux_functions._moving_average(rect_signal, sr / 10)
# [Second Smoothing Phase]
smooth_signal = []
for i in range(0, len(rect_signal)):
    if smoothing_level < i < len(rect_signal) - smoothing_level:
        smooth_signal.append(mean(rect_signal[i - smoothing_level:i + smoothing_level]))
    else:
        smooth_signal.append(0)
# Plotear la señal y los umbrales
plt.figure(figsize=(12, 6))
# Primer subplot (TKEO)
ax1 = plt.subplot(2, 1, 1)
ax1.plot(time, tkeo, lw=1, color='black', label='TKEO')
ax1.set_ylabel('Valor EMG')
ax1.legend()
ax1.grid(True)
plt.setp(ax1.get_xticklabels(), visible=False)  # Ocultar etiquetas del eje x

# Segundo subplot (Señal Suavizada)
ax2 = plt.subplot(2, 1, 2, sharex=ax1)
ax2.plot(time, smooth_signal, lw=1, color='deepskyblue', label='Señal Suavizada')
ax2.set_xlabel('Tiempo (s)')
ax2.set_ylabel('Valor EMG')
ax2.legend()
ax2.grid(True)
```

<div align="center">
    <img src="Imagenes_L8/Comparación_TKEO_Smooth.JPG" alt="wCF14V" width="1000">
    <p><b>Figura 9. Comparación de la señal TKEO vs la suavizada </b> </p>
</div>

```python
# [Threshold]
avg_pre_pro_signal = average(pre_pro_signal)
std_pre_pro_signal = std(pre_pro_signal)
# Regression function.
def normReg(thresholdLevel):
    threshold_0_perc_level = (- avg_pre_pro_signal) / float(std_pre_pro_signal)
    threshold_100_perc_level = (max(smooth_signal) - avg_pre_pro_signal) / float(std_pre_pro_signal)
    m, b = linregress([0, 100], [threshold_0_perc_level, threshold_100_perc_level])[:2]
    return m * thresholdLevel + b 
    
# Chosen Threshold Level (Example with two extreme values)
threshold_level = 10 # % Relative to the average value of the smoothed signal
threshold_level_norm_10 = normReg(threshold_level)

threshold_level = 80 # % Relative to the average value of the smoothed signal
threshold_level_norm_80 = normReg(threshold_level)

threshold_10 = avg_pre_pro_signal + threshold_level_norm_10 * std_pre_pro_signal
threshold_80 = avg_pre_pro_signal + threshold_level_norm_80 * std_pre_pro_signal

# Plotear la señal y los umbrales
plt.figure(figsize=(12, 6))
plt.plot(time, smooth_signal, lw=1, color='deepskyblue', label='Señal Original')
plt.axhline(y=threshold_10, color='blue', linestyle='--', label=f'Umbral 10% ({threshold_10:.2f})')
plt.axhline(y=threshold_80, color='red', linestyle='--', label=f'Umbral 80% ({threshold_80:.2f})')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valor EMG')
plt.title('Señal EMG con Umbrales de 10% y 80%')
plt.legend()
plt.grid(True)
plt.show()
```

<div align="center">
    <img src="Imagenes_L8\umbrales.JPG" alt="wCF14V" width="1000">
    <p><b>Figura 10. Muestra de los umbrales en la señal suavizada </b> </p>
</div>

```python
# Generation of a square wave reflecting the activation and inactivation periods.
binary_signal = []
for i in range(0, len(time)):
    if smooth_signal[i] >= threshold_10:
        binary_signal.append(1)
    else:
        binary_signal.append(0)
# Plotear la señal y los umbrales
plt.figure(figsize=(12, 6))
plt.plot(time, tkeo, lw=1, color='black', label='TKEO')
plt.plot(time, binary_signal, lw=1, color='deepskyblue', label='Señal binarizada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valor EMG')
plt.legend()
plt.grid(True)
plt.show()
```

<div align="center">
    <img src="Imagenes_L8\Binarizada.JPG" alt="wCF14V" width="1000">
    <p><b>Figura 11. Señal binarizada del TKEO </b> </p>
</div>

```python
activation_data = bsnb.detect_emg_activations(signal, sr, smooth_level=20, threshold_level=10, time_units=True, volts=False, resolution=None, device=device, plot_result=True)
```

<div align="center">
    <img src="Imagenes_L8\deteccion_de_evento.JPG" alt="wCF14V" width="1000">
    <p><b>Figura 12. Detección de eventos de la señal original usando el comando de la libreria opensignals </b> </p>
</div>


## Discusión de los resultados  <a name="t11"></a>

* Comparación de Filtros:
  
El análisis realizado mediante el código implementado muestra que el filtro 3 es el más apropiado según los parámetros predefinidos. Visualmente, no se observa una pérdida significativa de información relevante, logrando filtrar el ruido innecesario en áreas con poca activación muscular. Al examinar la Figura 2, donde la sombra representa la señal original y las señales de color (azul, verde o rojo) representan las señales filtradas, se nota que para los tres filtros, a los 10 segundos, la señal de color es casi imperceptible, indicando una falta de información relevante en esa sección. Sin embargo, a los 30 segundos, la señal filtrada abarca una porción más amplia, lo que sugiere un filtrado adecuado.

En conclusión, aunque no se observan diferencias sustanciales entre los tres filtros utilizados a simple vista, el código ha sido útil, ya que los parámetros establecidos permitieron descartar los otros dos filtros y seleccionar el filtro 3 como el más adecuado.

* Segmentación: 

Para la segmentación, hemos empleado una longitud de ventana de 1000 ms con un desplazamiento de 200 ms. A medida que avanzamos en la segmentación, observamos distintos patrones en los segmentos resultantes.

En el primer segmento, notamos una línea evidente que representa la ausencia de información desde el inicio hasta los primeros 0.4 segundos. Posteriormente, la señal exhibe fluctuaciones representativas.

Al comparar en el segundo segmento, la duración de la señal sin información se reduce a la mitad, comenzando desde el tiempo 0.2 del segmento anterior.

Luego notamos que ya para el tercer segmento las fluctuaciones de la señal comienzan de manera inmediata. Este patrón se repite a lo largo de los 10 segmentos restantes. Este fenómeno refleja el desplazamiento en la segmentación, permitiendo un análisis más exhaustivo de la señal al abarcar una mayor cantidad de información en cada segmento. Este enfoque nos facilita la identificación y descarte de características irrelevantes en la extracción de datos de cada segmento que se realizará en la extracción de características.

* Extracción de características: 

El análisis de las características en el dominio del tiempo es una técnica ampliamente utilizada para evaluar y comprender las señales de electromiografía (EMG). En este estudio, se extrajeron cinco características clave: valor absoluto medio (MAV), pendiente del valor absoluto medio (MAV_slope), cambios de signo de pendiente (SSC), longitud de forma de onda (WL) y cruces por cero (ZC).

El valor absoluto medio (MAV) proporciona una indicación de la amplitud media de la señal EMG. Un valor de MAV más alto sugiere una mayor actividad muscular o una señal con valores más altos en promedio. En los gráficos presentados, los segmentos 2 y 3 muestran los valores más altos de MAV, lo que indica una mayor amplitud de la señal EMG y, por lo tanto, una mayor actividad muscular en esos segmentos.

Para la pendiente del valor absoluto medio (MAV_slope) se observa que el segmento 3 tiene la pendiente de MAV más alta, lo que sugiere un cambio más pronunciado en el valor absoluto medio de la señal en este segmento. Esto nos será útil para detectar transiciones rápidas en la señal.

Los cambios de signo de pendiente (SSC) cuentan los puntos en los que la pendiente de la señal EMG cambia de dirección. Un valor más alto de SSC puede ser indicativo de una señal más compleja o con mayor ruido. Esto es observable en los gráficos del 6 al 10, indicando una actividad muscular más dinámica o una señal más ruidosa en esos segmentos.

La longitud de forma de onda (WL) suma las diferencias absolutas entre puntos adyacentes, proporcionando una medida de la complejidad de la señal EMG. Los valores más elevados para esta característica se presenta en los segmentos  2, 3 y 4.

Finalmente los cruces por cero (ZC) cuentan el número de veces que la señal EMG cruza el eje cero. Un valor más alto de ZC puede indicar una mayor variabilidad o ruido en la señal. En los gráficos, los segmentos 9 y 10 presentan los valores más altos, posiblemente debido a una mayor actividad muscular.

## Conclusiones <a name="t12"></a>

1. El procesamiento adecuado de las señales EMG es fundamental para eliminar ruido y artefactos, y obtener información confiable y significativa de la actividad neuromuscular. Las técnicas como el filtrado, la segmentación y la extracción de características son cruciales en este proceso.

2. La comparación de diferentes filtros basados en la transformada wavelet discreta (DWT) con funciones wavelet db2, db4 y db6 al nivel de descomposición 4, mostró que el filtro db6 fue el más apropiado según los parámetros de relación señal-ruido (SNR), relación señal-ruido pico (PSNR) y error cuadrático medio (RMSE). Aunque visualmente no se observaron diferencias sustanciales entre los filtros, el código implementado permitió seleccionar objetivamente el filtro óptimo.

3. La extracción de características en el dominio del tiempo, como el valor absoluto medio (MAV), la pendiente del valor absoluto medio (MAV_slope), los cambios de signo de pendiente (SSC), la longitud de forma de onda (WL) y los cruces por cero (ZC), proporcionó información valiosa sobre la amplitud, complejidad y variabilidad de la señal EMG en diferentes segmentos. Estas características permitieron detectar patrones de actividad muscular y transiciones en la señal.

4. El análisis de las características extraídas de los segmentos de la señal EMG reveló patrones interesantes, como una mayor amplitud y actividad muscular en ciertos segmentos, una mayor complejidad o ruido en otros, y transiciones rápidas en la señal. Estos hallazgos demuestran la utilidad de las técnicas de procesamiento empleadas para comprender y caracterizar la actividad neuromuscular.

En conclusión, este informe de laboratorio resalta la importancia de un procesamiento adecuado de las señales de electromiografía (EMG) para obtener información confiable y significativa sobre la actividad neuromuscular. A través de la implementación de técnicas de filtrado, segmentación y extracción de características, se logró eliminar el ruido y los artefactos de las señales, seleccionar el filtro óptimo basado en la transformada wavelet discreta (DWT) con la función wavelet db6, segmentar la señal en ventanas deslizantes para un análisis exhaustivo y extraer características relevantes en el dominio del tiempo. Los resultados obtenidos permitieron detectar patrones de actividad muscular, transiciones en la señal y revelar información valiosa sobre la amplitud, complejidad y variabilidad de la señal EMG en diferentes segmentos. Este enfoque sistemático y riguroso en el procesamiento de señales EMG valida la eficacia de las técnicas empleadas y sienta las bases para futuras investigaciones y aplicaciones en el campo de la electromiografía.

## Archivos <a name="t13"></a>

- [Programa de procesamiento de señal EMG (python)](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L8_Procesamiento_EMG/LAB_8.ipynb) 


## Bibliografía: <a name="t14"></a>

[1] M. B. I. Reaz, M. S. Hussain, y F. Mohd-Yasin, “Techniques of EMG signal analysis: detection, processing, classification and applications”, Biological Procedures Online, vol. 8, n.o 1, pp. 11-35, dic. 2006, doi: 10.1251/bpo115.
 
[2] V. Gohel y N. Mehendale, “Review on electromyography signal acquisition and processing”, Biophysical Reviews, vol. 12, n.o 6, pp. 1361-1367, nov. 2020, doi: 10.1007/s12551-020-00770-w.   

[3] R. H. Chowdhury, M. B. I. Reaz, Mohd. A. Mohd. Ali, A. A. A. Bakar, K. Chellappan, y T. G. Chang, “Surface Electromyography Signal Processing and Classification Techniques”, Sensors, vol. 13, n.o 9, pp. 12431-12466, sep. 2013, doi: 10.3390/s130912431.   

[4] A. M. Moslhi, H. H. Aly, y M. ElMessiery, “The Impact of Feature Extraction on Classification Accuracy Examined by Employing a Signal Transformer to Classify Hand Gestures Using Surface Electromyography Signals”, Sensors, vol. 24, n.o 4, p. 1259, feb. 2024, doi: 10.3390/s24041259.

[5] Z. Sun, X. Xi, C. Yuan, Y. Yang, and X. Hua, “Surface electromyography signal denoising via EEMD and improved wavelet thresholds,” Mathematical biosciences and engineering, vol. 17, no. 6, pp. 6945–6962, Jan. 2020, doi: https://doi.org/10.3934/mbe.2020359.
‌
[6] “An Improved Feature Extraction Method for Surface Electromyography Based on Muscle Activity Regions”, IEEE Journals & Magazine | IEEE Xplore, 2023. https://ieeexplore.ieee.org/document/10168895

[7] N. Nazmi, M. A. A. Rahman, S.-I. Yamamoto, S. A. Ahmad, H. Zamzuri, y S. A. Mazlan, “A Review of Classification Techniques of EMG Signals during Isotonic and Isometric Contractions”, Sensors, vol. 16, n.o 8, p. 1304, ago. 2016, doi: 10.3390/s16081304.

[8] S. A. Ahmad, “Moving approximate entropy and its application to the electromyographic control of an artificial hand - ePrints Soton,” Soton.ac.uk, Jun. 2009, doi: https://eprints.soton.ac.uk/66794/1/FinalThesis.pdf.

[9] A. Phinyomark, F. Quaine, S. Charbonnier, C. Serviere, F. Tarpin-Bernard, y Y. Laurillau, “EMG feature evaluation for improving myoelectric pattern recognition robustness”, Expert Systems With Applications, vol. 40, n.o 12, pp. 4832-4840, sep. 2013, doi: 10.1016/j.eswa.2013.02.023. 










