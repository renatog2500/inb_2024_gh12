# Laboratorio N°7 - Filtrado de las señales DWT

## Tabla de contenidos:
 __________________________________________________________________________________________________
1. [Lista de participantes](#t1)
2. [Introducción](#t2)
3. [Objetivos del laboratorio](#t3)
4. [Metodología](#t4)\
   4.1.[Materiales y Equipo utilizado](#t5)\
   4.2.[Procedimiento](#t6)
5. [Resultados](#t7)\
   5.1 [Ejercicio ECG](#t8)\
   5.2 [Ejercicio EMG ](#t9)\
   5.3 [Ejercicio EEG](#t10)
6. [Discusión](#t11)\
   6.1 [Señal ECG](#t12)\
   6.2 [Señal EMG](#t13)\
   6.3 [Señal EEG](#t14)\
7. [Bibliografía](#t15)
__________________________________________________________________________________________________
## **Lista de participantes** <a name = "t1"></a>
* Jimena Alpiste Espinoza - 74297329
* Jossymar León Mallma - 74905684
* Renato Cardoso Cardenas - 73061678


## Introducción  <a name = "t2"></a>
Las señales biomédicas, tales como el electrocardiograma (EKG) [1], la electromiografía (EMG) [2] y la electroencefalografía (EEG) [3], suelen estar contaminadas por ruido y artefactos, lo que dificulta su análisis e interpretación adecuada. Por lo tanto, es fundamental aplicar técnicas de filtrado a estas señales con el fin de eliminar el ruido y mejorar su calidad.

No obstante, si bien los métodos convencionales de filtrado FIR e IIR, que incluyen los filtros pasa-baja, pasa-alta y pasa-banda, pueden ser efectivos para eliminar parte del ruido presente, su aplicación puede traer consigo ciertas limitaciones. Ya que el uso de estos pueden provocar distorsiones indeseadas en la señal original y, en consecuencia, eliminar componentes de interés relevantes para el análisis posterior.

**Filtros Wavelet**

Frente a las limitaciones de los métodos convencionales de filtrado, los filtros wavelet surgen como una alternativa poderosa para el procesamiento de señales biomédicas. A diferencia de los filtros convencionales que operan en el dominio de la frecuencia, los filtros wavelet operan en el dominio tiempo-frecuencia, permitiendo localizar y separar las señales de interés del ruido en ambos dominios de manera más efectiva [4].

La base fundamental de los filtros wavelet es la transformada wavelet, la cual descompone la señal en versiones escaladas y trasladadas de una función base denominada wavelet madre. Existen diversos tipos de wavelets, como Daubechies, Symlet y Coiflet, cada uno con propiedades específicas que los hacen adecuados para diferentes aplicaciones[4].

Entre las principales ventajas que ofrecen los filtros wavelet sobre otros métodos de filtrado se encuentran las siguientes[4]:

- Permiten un análisis multirresolución, descomponiendo la señal en diferentes bandas de frecuencia, lo que facilita la identificación y separación de componentes de interés.
  
- Son capaces de detectar eventos transitorios y no estacionarios en la señal, lo que es especialmente útil para señales biomédicas que suelen presentar comportamientos no lineales y variaciones temporales complejas.
  
- Pueden eliminar el ruido sin suavizar en exceso bordes y picos, preservando así las características importantes de la señal original.
  
- Son computacionalmente eficientes gracias a la existencia de algoritmos rápidos para el cálculo de la transformada wavelet, lo que los hace adecuados para aplicaciones en tiempo real.

<div align="center">
    <img src="Imagenes_L6/Filtro digital intro.png" alt="wCF14V" width="400">
    <p><b>Figura 1. Representación de un filtro digital</b> - Extraído de [1]</p>
</div>


## **Objetivos  Laboratorio** <a name = "t3"></a>
* Comprender los principios básicos de filtros discretos Wavelet (DTW).
* Filtrar las señales ECG, EMG y EEG para la eliminación de ruidos y artefactos
* Analizar las señales obtenidas y extraer características de interés de cada una. 
  
## Metodología <a name="t4"></a>
En este laboratorio, nos enfocamos en el diseño e implementación de filtros Wavelets con el objetivo de atenuar las frecuencias altas indeseadas, originadas por el ruido presente en las señales ECG, EMG y EEG adquiridas previamente utilizando el Kit BITalino. 

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

***Señal ECG***
Para el ECG, se registró la actividad eléctrica del corazón en diversas condiciones utilizando la primera derivación. Se colocó un electrodo de referencia en la cresta ilíaca para obtener una mejor respuesta contra el ruido. A continuación una breve descripción de las pruebas realizadas: 

**Lectura Basal:** Se registró la actividad eléctrica del corazón en estado de reposo, proporcionando una línea base para comparar las variaciones en otras condiciones.

**Inhalación y Exhalación:** Se monitorea la actividad eléctrica del corazón mientras se realizan ejercicios de respiración controlada, observando los cambios que ocurren con la inhalación y la exhalación.

**Post Ejercicios:** Se registró la actividad eléctrica del corazón inmediatamente después de realizar ejercicios físicos, como polichinelas y planchas, para evaluar la respuesta cardíaca al esfuerzo físico.

***Justifiación de parámetros para la Señal ECG***
En un estudio realizado por Kania et. al. [5], se investigó la aplicación del filtrado wavelet para reducir el ruido en señales EKG de alta resolución. Los autores evaluaron diferentes funciones wavelet madre y niveles de descomposición para determinar los parámetros óptimos que minimizaran el error cuadrático medio (MSE) entre la señal original y la señal filtrada, preservando al mismo tiempo las características morfológicas del EKG.

Los resultados de Kania et al.[5] mostraron que las funciones wavelet db1 (Daubechies de primer orden) con niveles de descomposición del 4 al 6, sym3 (Symlet de tercer orden) con nivel 4, y sym8 (Symlet de octavo orden) con nivel 4, proporcionaron el mejor desempeño en términos de reducción de ruido y preservación de la morfología del EKG. Además, se destacó la ventaja del filtrado wavelet sobre técnicas convencionales como el promediado de latidos, especialmente en casos de arritmia donde el promediado puede distorsionar la señal.

***Parámetros elegidos***

(ACA VA UN CUADRO CON LOS PARÁMETROS UTILIZADOS AL FINAL)


**Señal EMG**
Para el EMG, se tomaron mediciones de los siguiente músculos en distintos estados:

**Actividad muscular del bíceps braquial (brazo):** Durante esta prueba, se registró la actividad eléctrica del bíceps braquial en estados de reposo y contracción. Para minimizar las interferencias, el electrodo de referencia se ubicó en la región del codo.

**Actividad muscular del flexor profundo de los dedos (antebrazo):** En estas mediciones, se registró la actividad eléctrica durante la flexión de los dedos hacia la palma de la mano. Al igual que en el ensayo anterior, el electrodo de referencia se colocó en la región del codo.

**Actividad muscular del flexor radial del caropo (antebrazo)**: En estas mediciones, se registró la actividad eléctrica durante la supinación del antebrazo . Al igual que en el ensayo anterior, el electrodo de referencia se colocó en la región del codo.

***Justifiación de parámetros para la Señal EMG***
En un estudio exhaustivo realizado por Phinyomark et al. [6], se investigó el desempeño de diferentes funciones wavelet madre y niveles de descomposición para el filtrado de ruido en señales EMG, con el objetivo de identificar los parámetros óptimos que minimizaran el error cuadrático medio (MSE) entre la señal original y la señal filtrada. Los autores evaluaron un total de 53 funciones wavelet, incluyendo las familias Daubechies, Symlet, Coiflet, BiorSplines y ReverseBior, así como la wavelet Discreta de Meyer.

Los resultados de Phinyomark et al. [6] revelaron que las funciones wavelet db1 (Daubechies de primer orden), bior1.1 (BiorSplines de primer orden) y rbio1.1 (ReverseBior de primer orden) proporcionaron el mejor desempeño en términos de reducción de ruido, con el mínimo MSE. Además, se encontró que el nivel de descomposición óptimo para el filtrado wavelet de señales EMG era el nivel 4. Los autores también destacaron que wavelets con forma simple y baja frecuencia eran más adecuadas para las características morfológicas de las señales EMG.

***Parámetros elegidos***

(ACA VA UN CUADRO CON LOS PARÁMETROS UTILIZADOS AL FINAL)



**Señal EEG**
Para evaluar la actividad neuronal a partir del electroencefalograma (EEG) utilizamos las señales obtenidas en el Laboratorio 05 a partir de las siguientes pruebas: 
**1. Lectura de la señal Basal:** Para adquirir esta señal el sujeto de prueba debe permanecer en una posición estable  , con ello se registrará la línea base de señal con poco ruido y sin movimientos (respiración normal,sin movimientos oculares/ojos cerrados) durante 30 segundos. Este estado sirve como nuestra prueba de referencia.

**2. Lectura de Ojos Abiertos - Ojos Cerrados:** A continuación el participante repetirá un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambas fases durante 5 segundos. El sujeto debe permanecer en una posición estable y mirando a un poco fijo para evitar ruido en la señal.

**3. Resolución de preguntas :** En esta prueba uno de los compañeros se encontrará leyendo en voz alta una serie de ejercicios obtenidos de [7], los ejercicios se dividiran en dos secciones de preguntas: simples y complejas. El particpante evaluado dbe intentar resolverlas manteniendo una posición estable. Las preguntas realizadas se observan en la Tabla 2.

| Categoría| Pregunta |
| --------- | --------- |
| Simple | Hay 3 pájaros en un árbol; Llegan 7 más. ¿Cuántos pájaros hay ahora?  |
| Simple  | Jonás tiene 5 manzanas y Mary tiene 4. ¿Cuántas manzanas tienen en total?  |
| Simple  | Hanna tiene 9 dólares pero gastó 4. ¿Cuántos dólares le quedan? |
| Compleja   | John anotó 45 puntos para su equipo; 10 más que José. Marie anotó 13 puntos más que John y Joseph juntos. ¿Cuántos puntos obtuvieron en total? |
| Compleja   | El grupo A tiene 24 estudiantes; 13 menos que el grupo B. El grupo C tiene 12 alumnos más que los grupos A y B juntos. ¿Cuál es el número total de estudiantes? |
| Compleja | Una tienda vendió 21 refrescos por la mañana y 13 más que por la tarde. Por la noche vendió 10 más que por la mañana y por la tarde juntas. ¿Cuántos refrescos se vendieron en total? |

<p align="center">
  <b>Tabla 2. Preguntas de lógica y matemáticas utilizadas  </b>
</p>


***Justifiación de parámetros para la Señal EEG***
En un estudio realizado por Hossain et al. [8], se propusieron dos nuevas técnicas para la corrección de artefactos de movimiento en señales de EEG de un solo canal: (i) Descomposición en paquetes wavelet (WPD) y (ii) WPD en combinación con análisis de correlación canónica (WPD-CCA). Los autores investigaron estas técnicas utilizando cuatro familias de paquetes wavelet diferentes (Daubechies, Symlets, Coiflets y Fejer-Korovkin) con tres momentos de desvanecimiento distintos.

Los resultados de Hossain et al. [8] mostraron que la técnica WPD-CCA proporcionó la mejor reducción porcentual de artefactos de movimiento (59.51%) y la mayor relación señal-ruido promedio (30.76 dB) cuando se utilizó el paquete wavelet db1. Entre las técnicas de corrección de artefactos de una sola etapa, WPD con el paquete wavelet db1 produjo el mejor desempeño, logrando una reducción de artefactos del 53.48% y una SNR de 29.26 dB. Además, se propuso un enfoque alternativo utilizando WPD donde se descartó el componente de subbanda de aproximación de frecuencia más baja, reconstruyendo una señal más limpia sumando los componentes de subbanda restantes.


***Parámetros elegidos***

WPD:

- Descomposición de la señal de EEG utilizando paquetes wavelet de las familias Daubechies, Symlet, Coiflet y Fejer-Korovkin con diferentes momentos de desvanecimiento (db1, db2, db3, sym4, sym5, sym6, coif1, coif2, coif3, fk4, fk6, fk8).
- Nivel de descomposición: 4, generando 16 componentes de subbanda.



 
**CÓDIGOS UTILIZADOS**
--------------------------------------------------------------------------------------------------------------
**Código de ploteo para EKG pre y post filtrado:**
```python
import pywt
import numpy as np
import matplotlib.pyplot as plt

def wavelet_denoising(signal, wavelet, level, threshold_method='soft'):
    # Descomposición wavelet
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    
    # Umbralización de coeficientes de detalle
    threshold = np.sqrt(2 * np.log(len(signal)))
    for i in range(1, len(coeffs)):
        coeffs[i] = pywt.threshold(coeffs[i], threshold * np.std(coeffs[i]), mode=threshold_method)
    
    # Reconstrucción de la señal
    denoised_signal = pywt.waverec(coeffs, wavelet)
    
    return denoised_signal

# Cargar señal EKG (reemplaza esto con tu propio código de carga de datos)
ecg_signal = np.loadtxt('ecg_data.txt')

# Parámetros del filtro wavelet
wavelet_type = 'db4'
decomposition_level = 4

# Aplicar filtrado wavelet
denoised_ecg = wavelet_denoising(ecg_signal, wavelet_type, decomposition_level)

# Graficar resultados
plt.figure(figsize=(10, 4))
plt.plot(ecg_signal, label='Señal EKG original')
plt.plot(denoised_ecg, label='Señal EKG filtrada')
plt.legend()
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.title('Filtrado Wavelet de Señal EKG')
plt.show()

```


**Código de ploteo para EMG pre y post filtrado:**
```python
import pywt
import numpy as np
import matplotlib.pyplot as plt

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

# Cargar señal EMG (reemplaza esto con tu propio código de carga de datos)
emg_signal = np.loadtxt('emg_data.txt')

# Parámetros del filtro wavelet óptimos según Phinyomark et al.
wavelet_type = 'db1'  # También puedes probar 'bior1.1' o 'rbio1.1'
decomposition_level = 4

# Aplicar filtrado wavelet
denoised_emg = wavelet_denoising_emg(emg_signal, wavelet_type, decomposition_level)

# Calcular MSE entre señal original y filtrada
mse = np.mean((emg_signal - denoised_emg) ** 2)
print(f"MSE: {mse:.4f}")

# Graficar resultados
plt.figure(figsize=(10, 4))
plt.plot(emg_signal, label='Señal EMG original')
plt.plot(denoised_emg, label='Señal EMG filtrada')
plt.legend()
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.title(f'Filtrado Wavelet de Señal EMG usando {wavelet_type}')
plt.show()

```

**Código de ploteo para EEG pre y post filtrado:**
```python

```

## Resultados   <a name="t7"></a>

### **Ejercicio ECG** <a name="t8"></a>
| Campo de actividad | Señal Cruda | Filtro Wavelet |
|-----------------|-------------------------|-----------|
| Basal             |                        |     |
| Inhalación Exhalación            |                      |      |
| Post Ejercicios            |                      |  |


<p align="center">
  <b>Tabla 2. Resumen de la señal filtrada para la data ECG</b>
</p>


### **Ejercicio EMG** <a name="t9"></a>
| Campo de actividad | Señal Cruda | Filtro Wavelet |
|-----------------|-------------------------|-----------|
| Bicep Braquial             |                        |     |
| Antebrazo en Supinación        |                      |      |
| Pulgar en supinacion            |                      |  |

<p align="center">
  <b>Tabla 3. Resumen de la señal filtrada para la data EMG</b>
</p>


### **Ejercicio EEG** <a name="t10"></a>
| Campo de actividad | Señal Cruda | Filtro Wavelet |
|-----------------|-------------------------|-----------|
| Basal           |                        |     |
| OJOS CERRADOS - ABIERTOS       |                      |      |
| PREGUNTAS COMPLEJAS           |                      |  |


<p align="center">
  <b>Tabla 4. Resumen de la señal filtrada para la data EEG</b>
</p>



## Discusión <a name="t11"></a>


### **ECG** <a name="t12"></a>


### **EMG** <a name="t13"></a>


### **EEG** <a name="t14"></a>




## ** Bibliografía** : <a name="t15"></a>












