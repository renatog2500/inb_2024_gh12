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
    <img src="Imagenes_L7/wavelet.png" alt="wCF14V" width="400">
    <p><b>Figura 1. Representación del wavelet </b> </p>
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

- **Lectura Basal:** Se registró la actividad eléctrica del corazón en estado de reposo, proporcionando una línea base para comparar las variaciones en otras condiciones.

- **Inhalación y Exhalación:** Se monitorea la actividad eléctrica del corazón mientras se realizan ejercicios de respiración controlada, observando los cambios que ocurren con la inhalación y la exhalación.

- **Post Ejercicios:** Se registró la actividad eléctrica del corazón inmediatamente después de realizar ejercicios físicos, como polichinelas y planchas, para evaluar la respuesta cardíaca al esfuerzo físico.


***Justificación de parámetros para la Señal ECG***

En un estudio realizado por Kania et. al. [5], se investigó la aplicación del filtrado wavelet para reducir el ruido en señales EKG de alta resolución. Los autores evaluaron diferentes funciones wavelet madre y niveles de descomposición para determinar los parámetros óptimos que minimizaran el error cuadrático medio (MSE) entre la señal original y la señal filtrada, preservando al mismo tiempo las características morfológicas del EKG.

Los resultados de Kania et al.[5] mostraron que las funciones wavelet db1 (Daubechies de primer orden) con niveles de descomposición del 4 al 6, sym3 (Symlet de tercer orden) con nivel 4, y sym8 (Symlet de octavo orden) con nivel 4, proporcionaron el mejor desempeño en términos de reducción de ruido y preservación de la morfología del EKG. Además, se destacó la ventaja del filtrado wavelet sobre técnicas convencionales como el promediado de latidos, especialmente en casos de arritmia donde el promediado puede distorsionar la señal.

***Parámetros elegidos***
| Función Wavelet | Nivel  | Umbral | 
| --------------- | -----  | ------ |
|       sym8      |   4    |  $\sigma \sqrt{2 \log N}$|

Donde: donde σ es la desviación estándar del ruido y 𝑁 es la longitud de la señal


**Señal EMG**
Para el EMG, se tomaron mediciones de los siguiente músculos en distintos estados:

- **Actividad muscular del bíceps braquial (brazo):** Durante esta prueba, se registró la actividad eléctrica del bíceps braquial en estados de reposo y contracción. Para minimizar las interferencias, el electrodo de referencia se ubicó en la región del codo.

- **Actividad muscular del flexor profundo de los dedos (antebrazo):** En estas mediciones, se registró la actividad eléctrica durante la flexión de los dedos hacia la palma de la mano. Al igual que en el ensayo anterior, el electrodo de referencia se colocó en la región del codo.

- **Actividad muscular del flexor radial del caropo (antebrazo)**: En estas mediciones, se registró la actividad eléctrica durante la supinación del antebrazo . Al igual que en el ensayo anterior, el electrodo de referencia se colocó en la región del codo.

***Justificación de parámetros para la Señal EMG***

En un estudio exhaustivo realizado por Phinyomark et al. [6], se investigó el desempeño de diferentes funciones wavelet madre y niveles de descomposición para el filtrado de ruido en señales EMG, con el objetivo de identificar los parámetros óptimos que minimizaran el error cuadrático medio (MSE) entre la señal original y la señal filtrada. Los autores evaluaron un total de 53 funciones wavelet, incluyendo las familias Daubechies, Symlet, Coiflet, BiorSplines y ReverseBior, así como la wavelet Discreta de Meyer.

Los resultados de Phinyomark et al. [6] revelaron que las funciones wavelet db1 (Daubechies de primer orden), bior1.1 (BiorSplines de primer orden) y rbio1.1 (ReverseBior de primer orden) proporcionaron el mejor desempeño en términos de reducción de ruido, con el mínimo MSE. Además, se encontró que el nivel de descomposición óptimo para el filtrado wavelet de señales EMG era el nivel 4. Los autores también destacaron que wavelets con forma simple y baja frecuencia eran más adecuadas para las características morfológicas de las señales EMG.

***Parámetros elegidos***

| Función Wavelet | Nivel  | Umbral | 
| --------------- | -----  | ------ |
|       db1      |   4    |  $\sigma \sqrt{2 \log N}$  |

Donde: donde σ es la desviación estándar del ruido y 𝑁 es la longitud de la señal



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


***Justificación de parámetros para la Señal EEG***

En un estudio realizado por Hossain et al. [8], se propusieron dos nuevas técnicas para la corrección de artefactos de movimiento en señales de EEG de un solo canal: (i) Descomposición en paquetes wavelet (WPD) y (ii) WPD en combinación con análisis de correlación canónica (WPD-CCA). Los autores investigaron estas técnicas utilizando cuatro familias de paquetes wavelet diferentes (Daubechies, Symlets, Coiflets y Fejer-Korovkin) con tres momentos de desvanecimiento distintos.

Los resultados de Hossain et al. [8] mostraron que la técnica WPD-CCA proporcionó la mejor reducción porcentual de artefactos de movimiento (59.51%) y la mayor relación señal-ruido promedio (30.76 dB) cuando se utilizó el paquete wavelet db1. Entre las técnicas de corrección de artefactos de una sola etapa, WPD con el paquete wavelet db1 produjo el mejor desempeño, logrando una reducción de artefactos del 53.48% y una SNR de 29.26 dB. Además, se propuso un enfoque alternativo utilizando WPD donde se descartó el componente de subbanda de aproximación de frecuencia más baja, reconstruyendo una señal más limpia sumando los componentes de subbanda restantes.

***Parámetros elegidos***

| Función Wavelet | Nivel  | Umbral | 
| --------------- | -----  | ------ |
|       db1      |   6    |  $\sigma \sqrt{2 \log N}$|

Donde: donde σ es la desviación estándar del ruido y 𝑁 es la longitud de la señal

WPD:

- Descomposición de la señal de EEG utilizando paquetes wavelet de las familias Daubechies, Symlet, Coiflet y Fejer-Korovkin con diferentes momentos de desvanecimiento (db1, db2, db3, sym4, sym5, sym6, coif1, coif2, coif3, fk4, fk6, fk8).
- Nivel de descomposición: 4, generando 16 componentes de subbanda.



 
**CÓDIGOS UTILIZADOS**
--------------------------------------------------------------------------------------------------------------
**Código de ploteo para EKG pre y post filtrado:**
```python
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
G_EMG = 1100  # Sensor gain
n_bits = 10  # Number of bits for ADC

# Convert ADC to EEG(V)
#Lectura = (Lectura / ((2**n_bits) - 0.5)) * VCC / G_EEG
emg_v = ((((emg)/(2**n_bits))-1/2)*VCC)/G_EMG

# Convert EEG(V) to EEG(uV)
emg_signal = emg_v * 1e6


# Parámetros del filtro wavelet óptimos según Phinyomark et al.
wavelet_type = 'syms8'  # También puedes probar 'bior1.1' o 'rbio1.1'
decomposition_level = 4

# Aplicar filtrado wavelet
denoised_emg = wavelet_denoising_emg(emg_signal, wavelet_type, decomposition_level)

# Calcular MSE entre señal original y filtrada
mse = np.mean((emg_signal - denoised_emg) ** 2)
print(f"MSE: {mse:.4f}")

# Plotear la señal de EMG en el dominio del tiempo
plt.figure()
plt.subplot(121) 
plt.plot(emg_signal[0:15], label='Señal ECG original')
plt.title('Señal orignal de ECG Lectura de la prueba de preguntas complejas')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid(True)

plt.subplot(122)
plt.plot(emg.index[0:15000], denoised_emg[0:15000],label='Señal ECG filtrada',color="orange")
plt.title(f'Filtrado Wavelet de Señal ECG usando {wavelet_type}')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid(True)

plt.show() 

```


**Código de ploteo para EMG pre y post filtrado:**
```python
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
G_EMG = 1009  # Sensor gain
n_bits = 10  # Number of bits for ADC

# Convert ADC to EEG(V)
#Lectura = (Lectura / ((2**n_bits) - 0.5)) * VCC / G_EEG
emg_v = ((((emg)/(2**n_bits))-1/2)*VCC)/G_EMG

# Convert EEG(V) to EEG(uV)
emg_signal = emg_v * 1e6


# Parámetros del filtro wavelet óptimos según Phinyomark et al.
wavelet_type = 'db1'  # También puedes probar 'bior1.1' o 'rbio1.1'
decomposition_level = 4

# Aplicar filtrado wavelet
denoised_emg = wavelet_denoising_emg(emg_signal, wavelet_type, decomposition_level)

# Calcular MSE entre señal original y filtrada
mse = np.mean((emg_signal - denoised_emg) ** 2)
print(f"MSE: {mse:.4f}")

# Plotear la señal de EMG en el dominio del tiempo
plt.figure()
plt.subplot(121) 
plt.plot(emg_signal[0:15], label='Señal EMG original')
plt.title('Señal orignal de EMG Lectura de la prueba de preguntas complejas')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid(True)

plt.subplot(122)
plt.plot(emg.index[0:15000], denoised_emg[0:15000],label='Señal EMG filtrada',color="orange")
plt.title(f'Filtrado Wavelet de Señal EMG usando {wavelet_type}')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid(True)

plt.show() 

```

**Código de ploteo para EEG pre y post filtrado:**
```python
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
plt.plot(emg.index[0:15000], denoised_emg[0:15000],label='Señal EEG filtrada',color="orange")
plt.title(f'Filtrado Wavelet de Señal EEG usando {wavelet_type}')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.grid(True)

plt.show() 

```

## Resultados   <a name="t7"></a>

### **Ejercicio ECG** <a name="t8"></a>
| Campo de actividad | Señal Cruda | Filtro Wavelet |
|--------------------|-------------------------|-----------|
| Basal              |![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Lectura_ECG_basal.png)|![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Wavelet_Lectura_ECG_basal.png)|
| Inhalación Exhalación            |![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Lectura_ECG_inhalaci%C3%B3n_exhalaci%C3%B3n.png)|![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Wavelet_Lectura_ECG_inhalaci%C3%B3n_exhalaci%C3%B3n.png)|
| Post Ejercicios            |![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Lectura_ECG_post_ejercicio.png)|![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Wavelet_Lectura_ECG_post_ejercicio.png)|


<p align="center">
  <b>Tabla 2. Resumen de la señal filtrada para la data ECG</b>
</p>


### **Ejercicio EMG** <a name="t9"></a>
| Campo de actividad | Señal Cruda | Filtro Wavelet |
|-----------------|-------------------------|-----------|
| Bicep Braquial             |![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Lectura_bicep_braquial.png)|![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/WaveLet_Lectura_bicep_braquial.png)|
| Antebrazo en Supinación        |![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Lectura_supinaci%C3%B3n_antebrazo.png)|![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/WaveLet_Lectura_supinaci%C3%B3n_antebrazo.png)|
| Pulgar en supinacion            |![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Lectura_pulgar_supinaci%C3%B3n_EMG.png)|![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/WaveLet_Lectura_pulgar_supinaci%C3%B3n_EMG.png)|

<p align="center">
  <b>Tabla 3. Resumen de la señal filtrada para la data EMG</b>
</p>


### **Ejercicio EEG** <a name="t10"></a>
| Campo de actividad | Señal Cruda | Filtro Wavelet |
|-----------------|-------------------------|-----------|
| Basal           |![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Lectura_EEG_referencial.png)|![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Wavelet_Lectura_EEG_referencial.png)|
| OJOS CERRADOS - ABIERTOS       |![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Lectura_EEG_Prueba_ojos_abiertos_cerrado_5s.png)|![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Wavelet_Lectura_EEG_Prueba_ojos_abiertos_cerrado_5s.png)|
| PREGUNTAS COMPLEJAS           |![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Lectura_EEG_Prueba_Preguntas_complejas.png)|![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Wavelet_Lectura_EEG_Prueba_Preguntas_complejas.png)|


<p align="center">
  <b>Tabla 4. Resumen de la señal filtrada para la data EEG</b>
</p>

## Discusión <a name="t11"></a>


### **ECG** <a name="t12"></a>

Según los resultados esperados guíandonos de la literatura mencionada en la justificación, se aplicó la filtración wavelet para la eliminación de ruido de las señales de ECG y se comparó con los resultados de la medición original, donde obtuvimos una señal filtrada final usando la función sym8 con un nivel de descomposicón de 4. Donde comparando con el MSE del ruido pudimos corroborar que la señal filtrada es óptima y no se pierde mucha información.

### **EMG** <a name="t13"></a>

Para evaluación de los resultados obtenidos para la reducción de ruido de las señales de EMG, nos guiamos directamente del estudio mencionado en la justificación donde se hacen diferentes pruebas para obtener la mejor opción de las funciones wavelet y sus niveles de descomposición. Para el procesamiento de la señal, elegimos una función wavelet de db1 con 4 niveles de descomposición, donde pudimos observar que la señal tuvo una atenuación ligera, sin embargo no hubo una perdida de información signifcativa concluyendo que el filtro elegido es óptimo para las señales EMG. 

### **EEG** <a name="t14"></a>

Para evaluación de los resultados obtenidos para la reducción de ruido de las señales de EEG, nos guiamos directamente del estudio mencionado en la justificación donde se hacen diferentes pruebas para obtener la mejor opción de las funciones wavelet y sus niveles de descomposición. Para el procesamiento de la señal, aplicamos la técnica mencionada WPD y elegimos una función wavelet de db1 con 4 niveles de descomposición, donde pudimos observar que un ploteo no muy común donde si se le hace un acercamientos e pueden ver pequeñas mesetas donde irián los picos usuales, sin embargo no hubo una perdida de información signifcativa concluyendo que el filtro elegido es óptimo para las señales EMG. 


## ** Bibliografía** : <a name="t15"></a>

[1] S. Ari, M. K. Das y A. Chacko, “ECG signal enhancement using S-Transform”, Comput. Biol. Medicine, vol. 43, n.º 6, pp. 649–660, julio de 2013. Accedido el 17 de mayo de 2024. [En línea]. Disponible: https://doi.org/10.1016/j.compbiomed.2013.02.015

[2] Chowdhury RH, Reaz MB, Ali MA, Bakar AA, Chellappan K, Chang TG. Surface electromyography signal processing and classification techniques. Sensors (Basel). 2013 Sep 17;13(9):12431-66. doi: 10.3390/s130912431. PMID: 24048337; PMCID: PMC3821366.

[3] Brophy, Eoin et al. “Denoising EEG Signals for Real-World BCI Applications Using GANs.” Frontiers in neuroergonomics vol. 2 805573. 13 Jan. 2022, doi:10.3389/fnrgo.2021.805573

[4] Wahab MF, O'Haver TC. Wavelet transforms in separation science for denoising and peak overlap detection. J Sep Sci. 2020; 43: 1998–2010. https://doi.org/10.1002/jssc.202000013

[5] M. Kania, M. Fereniec y R. Maniewski, “Wavelet Denoising for Multi-lead High Resolution ECG Signals”, MEAS. SCI. REV., vol. 7, n.º 4, pp. 30–33, 2007. Accedido el 17 de mayo de 2024. [En línea]. Disponible: https://www.measurement.sk/2007/S2/Kania.pdf

[6] A. Phinyomark, C. Limsakul, and P. Phukpattaranont, “An optimal wavelet function based on wavelet denoising for multifunction myoelectric control,” May 2009, doi: https://doi.org/10.1109/ecticon.2009.5137236.

[7] J. Molina del Río, M. A. Guevara, M. Hernández González, et al., "EEG correlation during the solving of simple and complex logical–mathematical problems," Cogn Affect Behav Neurosci, vol. 19, pp. 1036–1046, 2019. https://doi.org/10.3758/s13415-019-00703-5  

[8] Md Shafayet Hossain et al., “Motion Artifacts Correction from Single-Channel EEG and fNIRS Signals Using Novel Wavelet Packet Decomposition in Combination with Canonical Correlation Analysis,” Sensors, vol. 22, no. 9, pp. 3169–3169, Apr. 2022, doi: https://doi.org/10.3390/s22093169.











