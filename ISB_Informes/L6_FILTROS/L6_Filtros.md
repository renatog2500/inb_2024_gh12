# Laboratorio N°6 - Diseño de Filtros IIR y FIR 

## Tabla de contenidos:
 __________________________________________________________________________________________________
1. [Lista de participantes](#t1)
2. [Introducción](#t2)
3. [Objetivos del laboratorio](#t3)
4. [Metodología](#t4)
6. [Resultados](#t5)
   5.1 [Ejercicio ECG](#t6)\
   5.2 [Ejercicio EMG ](#t7)\
   5.3 [Ejercicio EEG](#t8)\
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




## **Objetivos  Laboratorio** <a name = "t3"></a>
* Comprender los principios básicos de filtros digitales, en particular, los relacionados con los filtros de respuesta infinita al impulso (IRR) y los de respuesta finita al impulso (FIR).
* Filtrar las señales ECG, EMG y EEG para la eliminación de ruidos y artefactos
* Analizar las señales obtenidas y extraer características de interés de cada una. 
  
## Metodología <a name="t4"></a>
aqui colocar el codigo utilizado 




## Resultados   <a name="t5"></a>


## Ejercicio ECG   <a name="t6"></a>
## Ejercicio EMG   <a name="t7"></a>

## Ejercicio EEG   <a name="t8"></a>

### **Visualización de señal eléctrica mediante video y OpenSignalsl** <a name="t7"></a>
A continuación se mostrarán los videos de la señal EEG en OpenSignals. Seguimos el protocolo mencionado previamente, manteniendo las mismas conexiones de electrodos para cada medición. Con esto se asegura la coherencia de los datos recopilados y la fiabilidad de los resultados obtenidos.

(*) Es importante destacar que la prueba 3, al tratarse de una segunda señal basal, no fue considerada para la grabación de video, aunque sí se tomó en cuenta para la representación gráfica mediante Python que se mostrará más adelante.

| Prueba | Señal Ploteada en Open Signals |
| --------- | ---- |
| 1.Lectura de la señal Basal    | [![Miniatura del video](https://img.youtube.com/vi/vVzU5VYG40Y/0.jpg)](https://youtu.be/vVzU5VYG40Y) |
| 2. Lectura de Ojos Abiertos y Cerrados (Fases de 5 segundos)| [![Miniatura del video](https://img.youtube.com/vi/qGDZA1MTl0I/0.jpg)](https://youtu.be/qGDZA1MTl0I) |
| 3. Lectura de la Segunda señal Basal| No se registro video de esta señal basa, pero si se considero para el ploteo |
| 4. Resolución de preguntas Simples | [![Miniatura del video](https://img.youtube.com/vi/dlAMXUPAE9I/0.jpg)](https://youtu.be/dlAMXUPAE9I) |
| 5.Resolución de preguntas Complejas| [![Miniatura del video](https://img.youtube.com/vi/ADb1Umvjf0A/0.jpg)](https://youtu.be/ADb1Umvjf0A) |

<p align="center">
  <b>Tabla 3. Videos mostrando las conexiones electrodos-cuerpo y la señal ploteada en OpenSignals del protocolo.
 </b>
</p>

### **Explicación de la variación de la señal de OpenSignals**

**1. Lectura del Estado Basal:**

Estado de reposo (Lectura Basal):
El cambio abrupto inicial en la señal de EEG durante el estado de reposo puede atribuirse a artefactos de movimiento o ajustes en el sistema de adquisición. Después de este cambio inicial, la señal se vuelve estable y constante, lo que refleja un estado de reposo mental y una actividad cerebral reducida [8]. Según Gu et al. (2020), "durante el estado de reposo, la actividad cerebral espontánea se caracteriza por oscilaciones de baja frecuencia y alta amplitud en las bandas alfa y theta" [9].

**2. Lectura de los ciclos de Ojos Abiertos y Cerrados (Fases de 5 segundos):**

Los picos de gran tamaño observados al abrir o cerrar los ojos se deben a artefactos oculares causados por el movimiento de los ojos y los párpados. Estos artefactos se superponen a la señal de EEG y pueden tener una amplitud mucho mayor que la actividad cerebral subyacente [10]. Plichta et al. (2021) mencionan que "los artefactos oculares, como los parpadeos y los movimientos sacádicos, pueden introducir grandes picos en la señal de EEG" [11].

**3. Segunda lectura en estado de reposo (no se repitio la grabación de video):**

La similitud entre la primera y la segunda lectura en estado basal sugiere que el sujeto pudo relajarse y volver a un estado de reposo mental después de la tarea de abrir y cerrar los ojos. La reproducibilidad de las mediciones basales es importante para evaluar la estabilidad de la señal de EEG a lo largo del tiempo [8].

**4. Resolución de preguntas Simples:**

Los cambios en los picos negativos y positivos de la señal de EEG durante la resolución de preguntas simples pueden estar relacionados con la activación de áreas cerebrales específicas involucradas en el procesamiento cognitivo y la formulación de respuestas [12]. Los pequeños cambios observados durante el razonamiento sugieren una mayor actividad cerebral en comparación con el estado de reposo. Según Bhattacharya et al. (2020), "la resolución de problemas y el razonamiento están asociados con cambios en la actividad oscilatoria en las bandas theta y alfa del EEG" [13].

**5. Resolución de preguntas Complejas:**

Resolución de preguntas complejas:
Los cambios en la señal de EEG durante la resolución de preguntas complejas pueden reflejar una mayor demanda cognitiva y la activación de múltiples áreas cerebrales. La complejidad de las preguntas puede requerir un procesamiento más profundo y una mayor integración de la información, lo que se manifiesta como cambios en la actividad oscilatoria del EEG [14]. Según Pinti et al. (2020), "la resolución de problemas complejos implica la coordinación de múltiples regiones cerebrales y se asocia con cambios en la conectividad funcional medida por el EEG" [15].

### **Visualización de señal eléctrica mediante video y OpenBCI** <a name="t8"></a>

| Prueba | Señal Ploteada en OpenBCI |
| --------- | ---- |
| 1.Lectura de la señal Basal | [![Miniatura del video](https://img.youtube.com/vi/XvO9Swg0UOs/0.jpg)](https://www.youtube.com/watch?v=XvO9Swg0UOs) |
| 2. Lectura de los ciclos de Ojos Abiertos y Cerrados (Fases de 5 segundos)  | [![Miniatura del video](https://img.youtube.com/vi/5O7GbBteY9w/0.jpg)](https://www.youtube.com/watch?v=5O7GbBteY9w) |
| 3. Registro fase de referencia | [![Miniatura del video](https://img.youtube.com/vi/g9LNPO2JDDc/0.jpg)](https://www.youtube.com/watch?v=g9LNPO2JDDc) |
| 4. Ejercicios Matemáticos | [![Miniatura del video](https://img.youtube.com/vi/p1FOJwmLAsk/0.jpg)](https://www.youtube.com/watch?v=p1FOJwmLAsk) |

<p align="center">
  <b>Tabla 4. Videos de la señal ploteada en OpenBCI del protocolo </b>
</p>



### **Ploteo de la señal en Python** 
________________________________________________________________________________________________
### **BITalino: Ploteo de la señal obtenida en Python** <a name="t9"></a>
A continuación se mostrará la señal junto con el código de Python utilizado para su representación:

| Prueba     | Ploteo de la señal en el tiempo y su dominio en frecuencia     |
| -------------- | -------------- |
| **1.Estado de reposo (lectura basal**| <img src="Imagenes_L5/Fase de referencia.png" alt="Electrodos de guía" width="700">|
| **2.Lectura de los ciclos de Ojos Abiertos y Cerrados (Fases de 5 segundos)** | <img src="Imagenes_L5/Abrir_y_ cerrar_los_ojos.png" alt="Electrodos de guía" width="700">|
| **3. Segunda lectura Basal** | <img src="Imagenes_L5/Basal2.png" alt="Electrodos de guía" width="700">|
| **4. Resolución de preguntas Simples** | <img src="Imagenes_L5/Preguntas_Simples.png" alt="Electrodos de guía" width="700">|
| **5. Resolución de preguntas Complejas** |<img src="Imagenes_L5/Preguntas_complejas.png" alt="Electrodos de guía" width="700"> |

<p align="center">
  <b>Tabla 5. Ploteo del protocolo en Python de la señal del BITalino </b>
</p>

**Descripción del código en python:** 
Este código de Python utiliza las bibliotecas pandas, numpy, matplotlib y re para cargar y analizar datos de un archivo de texto que contiene mediciones de un electroencefalograma (EEG), específicamente para un experimento de abrir y cerrar los ojos. El código sigue varios pasos para procesar los datos, realizar una transformada rápida de Fourier (FFT) y visualizar tanto la señal temporal como el espectro de frecuencias. Aquí te explico cada parte del código:

Importación de Librerías: Importa las librerías necesarias para manejo de datos (pandas y numpy), visualización (matplotlib.pyplot), y expresiones regulares (re).
Definición de la Función extraer_nombres_columnas:
  El código abre y lee un archivo especificado, buscando líneas que comienzan con "#" para identificar metadatos relevantes, como los nombres de las columnas y el canal utilizado. Emplea expresiones regulares para extraer eficazmente esta información del texto.
Carga de Datos:
  Utilizamos pandas.read_csv para leer el archivo de OpenSignal, omitiendo las primeras tres filas las cuales no tienen información necesaria para el ploteo. Extraemos las primeras 6 columnas según los canales que tenga el BiTalino.
Procesamiento y Conversión de Datos:
  Selecciona la columna correspondiente al canal utilizado (extraído anteriormente) para las mediciones.
  Convierte los valores de la columna seleccionada de string a int para realizar operaciones matemáticas.
Transformada Rápida de Fourier (FFT):
  El código aplica la Transformada Rápida de Fourier (FFT) a la serie temporal para obtener el espectro de frecuencias. Luego, calcula las frecuencias asociadas con los puntos de la FFT y determina las magnitudes en decibelios de estos resultados para visualizar la amplitud de la señal en una escala logarítmica.
Conversión de Valores Digitales a Analógicos:
  Convierte los valores digitales a voltaje usando las especificaciones del ADC (voltaje de operación y ganancia del sensor) del data sheet del BiTalino [17], donde extraemos los valores de ganancia de 41782, una resolución de 10 bits ya que en los canales A1-A4 usan esa resolución y un voltaje de referencia de 3.3V. Para luego convertir los voltajes a microvoltios para presentar la señal en un rango típico para EEG.
Visualización:
  El código crea figuras para mostrar la señal de EEG tanto en el dominio del tiempo como en el dominio de la frecuencia. Utiliza dos subplots: uno dedicado a la visualización de la señal en el tiempo y el otro al espectro de frecuencias. Para facilitar la interpretación, se añaden títulos, etiquetas y cuadrículas a los gráficos.








## ** Bibliografía** : <a name="t12"></a>








