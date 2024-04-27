# Laboratorio N°5 - Uso de BITalino para EEG

## Tabla de contenidos:
 __________________________________________________________________________________________________
1. [Lista de participantes](#t1)
2. [Introducción](#t2)
3. [Objetivos del laboratorio](#t3)
4. [Materiales y Equipo Utilizado](#t4)
5. [Protocolo de conexión](#t5)
6. [Resultados y discusión](#t6)\
   6.1 [Visualización de la señal mediante video y OpenSignals ](#t7)\
   6.2 [Ploteo de la señal en Python](#t8)\
   6.3 [Archivos de la señal ploteada en Python y datos de la señal](#t9)\
   6.4 [Ploteo de la señal en OpenBCI GUI](#t10)
8. [Bibliografía](#t11)
__________________________________________________________________________________________________
## **Lista de participantes** <a name = "t1"></a>
* Jimena Alpiste Espinoza - 74297329
* Jossymar León Mallma - 74905684
* Renato Cardoso Cardenas - 73061678


## Introducción  <a name = "t2"></a>




**Señal de un Electroencefalograma**: 


## **Objetivos del Laboratorio** <a name = "t3"></a>
* Adquirir señales biomédicas de EEG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales EEG del software OpenSignals (r)evolution
  
## **Materiales y Equipo Utilizado** <a name="t4"></a>
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

## Protocolo de conexión <a name="t5"></a>
Para capturar las señales ECG, se empleó el dispositivo BITalino junto con su sensor ECG de tres electrodos. Se siguió el procedimiento detallado en la guía BiTalino,**(BITalino HOME-GUIDE #2 ELECTROCARDIOGRAPHY (ECG) Exploring Cardiac Signals at the Skin Surface")** [4], como referencia para posicionar correctamente los electrodos en el sujeto de prueba. A continuación, se presentan los protocolos de conexión específicos utilizados en cada prueba llevada a cabo en este laboratorio:

| Figura 2. Colocación de electrodos para la derivación I referencia[4].                                                                                                   | Figura 3. Colocación de los electrodos en el laboratorio para la derivación I                                                                                                     |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| ![Electrodos de guía](Imagenes_L4/electrodos_guia.png) | <img src="Imagenes_L4/posicion _usada_electrodos.png" alt="Electrodos de guía" width="700"> |


**Protocolo para las pruebas realizadas:**
El protocolo seguido para evaluar la ***  en vivo con el encefalograma fue el de la guía experimental de BITalino [X]:

1. Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal,sin movimientos oculares/ojos cerrados) durante 30 segundos.
2. Repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambasfases durante cinco segundos.
3. Registrar otra fase basal de 30 segundos (paso 1).
4. Que uno de tus compañeros lea en voz alta una serie de ejercicios matemáticos (se dividió en dos secciones: preguntas simples y complejas) y resuelve cada uno de ellos mentalmente enfocando tu mirada en unpunto específico para evitar artefactos.
5. Detener la grabación
------------------------

## Resultados y discusión  <a name="t6"></a>

### **Visualización de señal eléctrica mediante video y OpenSignalsl** <a name="t7"></a>
A continuación se mostrarán los videos de la señal EEG en OpenSignals. Seguimos el protocolo mencionado previamente, manteniendo las mismas conexiones de electrodos para cada medición. Con esto se asegura la coherencia de los datos recopilados y la fiabilidad de los resultados obtenidos.

(*) Es importante destacar que la prueba 3, al tratarse de una segunda señal basal, no fue considerada para la grabación de video, aunque sí se tomó en cuenta para la representación gráfica mediante Python que se mostrará más adelante.

| Prueba   | Señal Ploteada en Open Signals   | Descripción    |
| --------- | ---- | --------- |
| 1.Lectura de la señal Basal  | [![Miniatura del video](https://img.youtube.com/vi/-wfPedZAewY/0.jpg)](https://www.youtube.com/watch?v=-wfPedZAewY&list=PL1Sr3jz1xOr2I_mcd2os0of3MUAfD8h60&index=2)    | En la prueba 1 se tomo señales ECG del sujeto de prueba en estado de reposo.|
| 2. Lectura de los ciclos de Ojos Abiertos y Cerrados (Fases de 5 segundos)  | [![Miniatura del video](https://img.youtube.com/vi/tKcrb_DEtSk/0.jpg)](https://www.youtube.com/watch?v=tKcrb_DEtSk&list=PL1Sr3jz1xOr2I_mcd2os0of3MUAfD8h60&index=10)   | En la 2da prueba el sujeto realizó ciclos de inhalación y exhalación de intervalos de 5 segundos durante 30 segundos, se tomó la lectura del comportamiento de la señal ECG. |
| 4. Resolución de preguntas Simples |[![Miniatura del video](https://img.youtube.com/vi/TCozf52vHHc/0.jpg)](https://www.youtube.com/watch?v=TCozf52vHHc&list=PL1Sr3jz1xOr2I_mcd2os0of3MUAfD8h60&index=5 "Haz clic para ver el video")   | El sujeto fue sometido a una serie de ejercicios físicos que incluyeron la realización de planchas y polichinelas. Luego de completar estos ejercicios, se procedió a tomar la señal del electrocardiograma (ECG).   |
| 5.Resolución de preguntas Complejas | [![Miniatura del video](https://img.youtube.com/vi/QQnHKHVdN3U/0.jpg)](https://www.youtube.com/watch?v=QQnHKHVdN3U&list=PL1Sr3jz1xOr2I_mcd2os0of3MUAfD8h60&index=4 "Haz clic para ver el video") | Se llevó a cabo una nueva toma de la señal del electrocardiograma (ECG) del sujeto en reposo después de completar la serie de ejercicios.   |


<p align="center">
  <b>Tabla 2. Videos de las pruebas realizadas </b>
</p>


### **Explicación de la variación de la señal**


**1. Lectura del Estado Basal:**
**2. Lectura de los ciclos de Ojos Abiertos y Cerrados (Fases de 5 segundos):**
**3. Segunda lectura en estado de reposo (no se repitio la grabación de video):**
**4. Resolución de preguntas Simples:**
**5. Resolución de preguntas Complejas:**

### **Ploteo de la señal en Python** <a name="t8"></a>

| Prueba     | Ploteo de la señal en el tiempo y su dominio en frecuencia     |
| -------------- | -------------- |
| **1.Estado de reposo (lectura basal**| <img src="Imagenes_L4/Basal_1.png" alt="Electrodos de guía" width="700">|
| **2.Lectura de los ciclos de Ojos Abiertos y Cerrados (Fases de 5 segundos)** | <img src="Imagenes_L4/ciclo_inhalation_exhalation.png" alt="Electrodos de guía" width="700">|
| **3. Segunda lectura Basal** | <img src="Imagenes_L4/Basal_2_post_Inhalación.png" alt="Electrodos de guía" width="700">|
| **4. Resolución de preguntas Simples** | <img src="Imagenes_L4/Post_ejercicio.png" alt="Electrodos de guía" width="700">|
| **5. Resolución de preguntas Complejas** |<img src="Imagenes_L4/Basal_3_Post_ejercició.png" alt="Electrodos de guía" width="700"> |

<p align="center">
  <b>Tabla 3. Ploteo del protocolo en Python </b>
</p>



**- Código en Python para ploteo de señales de BiTalino:**
```python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# Cargar datos desde el archivo de texto según la ubicación del 
archivo = "C:/Users/Equipo/OneDrive/Escritorio/Introduccion_a_señales_biomedicas/Github/inb_2024_gh12/Documentación/EMG/Lectura_antebrazo_supinación_EMG.txt"
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
nombres_columnas,Entrada=extraer_nombres_columnas(archivo) #Aquí te devuelve la lista como un string dentro de otra lista y también el nombre del canal usado
#print(nombres_columnas) Imprime la lista: ['nSeq', 'I1', 'I2', 'O1', 'O2', 'A1']
print(type(Entrada))
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
print(datos)
#Comprobado el resultado solo escogemos la columna "A1", la cual usamos para nuestra medición
Lectura_EMG = datos[Entrada]

# Convertir los datos a números
Lectura_EMG = Lectura_EMG.apply(pd.to_numeric)

# Calculate FFT
fft_result = np.fft.fft(Lectura_EMG)

# Calculate frequencies
frequencies = np.fft.fftfreq(len(Lectura_EMG), d=1/1000)

# Compute the FFT magnitude
magnitudes_db = -20*np.log10(np.abs(fft_result))

#print(Lectura_EMG)
Lectura_EMG.index = Lectura_EMG.index / 1000

# Plotear la señal de EMG en el dominio del tiempo
plt.figure(figsize=(13,9))
plt.subplot(211)
plt.plot(Lectura_EMG)
plt.title("Lectura del pulgar supinación EMG en el dominio del tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.grid(True)

# Plotear el espectro de amplitud de la FFT (escala logarítmica - decibelios)
plt.subplot(212)
plt.plot(frequencies[:len(frequencies)//2], magnitudes_db[:len(frequencies)//2])
plt.title("Espectro de amplitud de la FFT (escala logarítmica - decibelios)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.grid(True)

plt.show()

```

**-Código de ploteo para señal de OpenBCI:**
```python
import pandas as pd
import matplotlib.pyplot as plt


def interpret16bitAsInt32(two_byte_value):
    # Asumimos que two_byte_value es un entero de 16 bits y extrae los bytes
    high_byte = (two_byte_value >> 8) & 0xFF
    low_byte = two_byte_value & 0xFF
    
    # Combina los bytes en un nuevo entero de 16 bits
    newInt = (high_byte << 8) | low_byte
    
    # Extiende el signo si es necesario
    if newInt & 0x8000:  # Si el bit de signo está establecido
        newInt = newInt - 0x10000  # Extiende el signo a 32 bits
        
    return newInt

# Cargar datos desde el archivo de texto según la ubicación del archivo
archivo = "C:/Users/Equipo/OneDrive/Escritorio/Introduccion_a_señales_biomedicas/Github/inb_2024_gh12/ISB_Informes/L5_Lectura_de_EEG/EEG_L5/EEG_Casco/OpenBCI-RAW-mate_Grupo_12.txt"

# Definir las constantes del ADC
vref = 4.5  # Voltaje de referencia en volts
ganancia = 24  # Ganancia del ADC
resolucion = 16  # Resolución en bits

# Calcular el voltaje por bit en volts
voltaje_por_bit = vref / (ganancia) /(2**16 - 1)

# Load the data
data = pd.read_csv(archivo, skiprows=5, usecols=range(1, 17))

# Convertir los datos a enteros si no lo son ya
data = data.applymap(int)

# Aplica la función de interpretación a cada elemento
data_signed_32 = data.applymap(interpret16bitAsInt32)

data_centered = data_signed_32.sub(data_signed_32.mean(axis=0), axis=1)

# Convertir de bits a voltaje y luego a microvoltios
data_uV = data_centered * voltaje_por_bit * 1e6  # Multiplica por 1e6 para convertir de V a uV

# Imprimir los primeros datos transformados
print(data_uV)

#Se convierten los ms en segundos
data_uV.index = data_uV.index / 1000

# Plotting
fig, axes = plt.subplots(16, 1, figsize=(150, 100))  # Crea una figura y un conjunto de subplots
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
    '#bcbd22', '#17becf', '#1b9e77', '#d95f02',
    '#7570b3', '#e7298a', '#66a61e', '#e6ab02',
]

for i in range(16):
    axes[i].plot(data_uV.iloc[:, i],color=colors[i])
    axes[i].set_title(f'EXG Channel {i+1}', fontsize=8)
    axes[i].grid(True)

# Configuración de la figura
fig.tight_layout()
fig.subplots_adjust(top=0.95)

# Agrega un título general a la figura completa
fig.suptitle("EEG Channel Outputs para estado de preguntas matematicas", fontsize=14)

# Configurar etiquetas para toda la figura (ajuste las coordenadas según sea necesario)
fig.text(0.5, 0.005, 'Time', ha='center', va='center', fontsize=12)
fig.text(0.005, 0.5, 'Amplitude (uV)', ha='center', va='center', rotation='vertical', fontsize=12)

plt.show()
```

### **Archivos de la señal ploteada en Python y datos de la señal** <a name="t9"></a>
- [Documentos (.txt)](https://github.com/renatog2500/inb_2024_gh12/tree/main/ISB_Informes/L4_Lectura_de_ECG/ECG_L4)
- [Programa de ploteo (python)](colocar link) COLOCAR EL ARCHIVOOO

## **Ploteo de la señal en OpenBCI GUI** : <a name="t10"></a>

-Crear una tabla en el que se vea los videos ( persona con señal )  y las señales ploteadas en pyhton 
- Explicar lo que se ve en la señal 

## ** Bibliografía** : <a name="t11"></a>


‌


