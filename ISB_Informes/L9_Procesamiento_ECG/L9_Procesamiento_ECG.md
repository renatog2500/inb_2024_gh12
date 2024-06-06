# Laboratorio N°9 - Procesamiento ECG

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
Cuando el impulso cardíaco se transmite a través del corazón, la corriente eléctrica se extiende hacia los tejidos circundantes. Una pequeña fracción de esta corriente se disemina hacia la superficie corporal. Al colocar electrodos en la piel en diferentes áreas alrededor del corazón, es posible registrar los potenciales eléctricos generados por esta corriente; este registro se conoce como electrocardiograma (ECG) [1].
El ECG es una modalidad de diagnóstico no invasiva que tiene un impacto clínico sustancial en la investigación de la gravedad de las enfermedades cardiovasculares.  Dado que refleja la actividad eléctrica dentro del corazón durante la contracción, el momento en que ocurre y su forma proporciona mucha información sobre el estado del corazón [2]. En la figura 1, se muestra el registro esquemático de un latido cardíaco normal, en este se observan las ondas P, Q , R, T y U. 

<div align="center">
    <img src="Imagenes_L8\deteccion_de_evento.JPG" alt="wCF14V" width="1000">
    <p><b>Figura 1. Señal de ECG de latido cardíaco normal. Extraído de [2] </b> </p>
</div>

Esta herramienta se utiliza cada vez más para monitorear pacientes que toman antiarrítmicos y otros medicamentos, como parte integral de la evaluación preoperatoria de pacientes sometidos a cirugía no cardíaca, y para evaluar a personas en ocupaciones de alto riesgo y a quienes practican deportes [3]. Estas aplicaciones requieren una determinación adecuada de los aspectos morfológicos y de intervalo de la señal de ECG registrada, que son susceptibles a diversos tipos de ruidos predominantes, como la desviación de la línea base, los artefactos musculares, los artefactos musculares (MA), el ruido del electromiograma (EMG), el ruido blanco gaussiano aditivo (AWGN), la interferencia de la línea eléctrica (PLI), y otros ruidos diversos como el ruido compuesto (CN), el ruido aleatorio, los artefactos de movimiento de electrodos (EM) y el ruido de instrumentación. Estos ruidos dificultan la determinación de anomalías morfológicas específicas en las señales del ECG, complicando el diagnóstico preciso de enfermedades [4].

Por lo tanto, un adecuado procesamiento de la señal ECG es crucial para eliminar o minimizar estos ruidos y obtener información confiable y significativa de la actividad cardíaca. Técnicas avanzadas de procesamiento de señales, como el filtrado, la eliminación de artefactos y la extracción de características, son fundamentales para aprovechar al máximo el potencial de la ECG en aplicaciones médicas y de ingeniería.

Hay varios métodos propuestos en la literatura para la clasificación de señales ECG, los cuales se pueden dividir en cuatro categorías: preprocesamiento, segmentación, extracción de características y clasificación. Este procedimiento se explicará a continuación usando las referencias [2] y [5]. Asimismo, estos cuatro pasos del tratamiento de señales ECG se muestran a modo de diagrama en la figura 2, donde A, B, C y D simulan las clasificaciones finales de los latidos analizados.

<div align="center">
    <img src="Imagenes_L8\deteccion_de_evento.JPG" alt="wCF14V" width="1000">
    <p><b> Figura 2.Diagrama de la clasificación de la señal ECG. Extraído de [2] </b> </p>
</div>

**Etapas de la clasificación:** 

1. **Preprocesamiento**:  En esta etapa se busca detectar y atenuar frecuencias relacionadas con artefactos en la señal de ECG, además de realizar normalización y mejora de la señal. Algunos métodos comunes son el uso de filtros digitales recursivos de respuesta finita al impulso (FIR), transformada wavelet y filtros adaptativos.
2. **Segmentación**: El objetivo de esta etapa es dividir la señal de ECG en segmentos más pequeños que representen mejor la actividad eléctrica del corazón. Los métodos más estudiados se enfocan en la detección del complejo QRS o pico R. Algunas técnicas empleadas son filtros digitales, redes neuronales, algoritmos genéticos, transformada wavelet, bancos de filtros, entre otros.
3. **Extracción de características**: Esta es una etapa crucial, donde se busca obtener un conjunto de valores representativos y no redundantes (características) a partir de los segmentos de ECG. Algunas características comunes son intervalos entre ondas (intervalo RR), amplitudes, duración de ondas, transformadas tiempo-frecuencia, análisis de componentes independientes (ICA), entre otras.
4. **Clasificación**:En esta etapa, se asigna una categoría o diagnóstico a cada segmento de la señal ECG mediante el uso de algoritmos que utilizan las características extraídas. Este paso es crucial para la identificación de arritmias y otros problemas cardíacos. Entre los clasificadores más comunes se encuentran Support Vector Machine (SVM), que busca encontrar el hiperplano que mejor separa las clases en el espacio de características; Artificial Neural Network (ANN), modelos computacionales inspirados en el cerebro humano capaces de aprender patrones complejos; K-Nearest Neighbours (KNN), que clasifica un punto basado en la mayoría de las clases de sus K vecinos más cercanos; y Decision Tree (DT), que utiliza una estructura jerárquica de decisiones para dividir el espacio de características en regiones con decisiones simples. Estos clasificadores son ampliamente utilizados debido a su efectividad en la clasificación de señales ECG, proporcionando diagnósticos precisos y rápidos para diversas condiciones cardíacas .

**Heart Rate Variability (HRV)**
El Heart Rate Variability (HRV) o Variabilidad de la Frecuencia Cardíaca es una medida que evalúa las variaciones en el tiempo entre latidos cardíacos consecutivos. Específicamente, el HRV se basa en el análisis de los intervalos R-R en el electrocardiograma (ECG).

Los intervalos R-R se refieren al tiempo transcurrido entre dos ondas R consecutivas en el ECG. Estas ondas R representan la despolarización ventricular en cada ciclo cardíaco. Por lo tanto, el intervalo R-R corresponde al tiempo entre dos despolarizaciones ventriculares sucesivas, lo que equivale al período entre latidos cardíacos [6].

Al analizar las fluctuaciones en los intervalos R-R, el HRV proporciona información valiosa sobre la capacidad del sistema nervioso autónomo para modular la frecuencia cardíaca. Una mayor variabilidad en los intervalos R-R indica una mejor regulación autonómica del corazón, lo que refleja un equilibrio saludable entre las ramas simpática y parasimpática del sistema nervioso autónomo [7].

Algunas razones por las cuales la HRV es una medida significativa, según la información obtenida de [6], incluyen:

* **Reflejo de la actividad autonómica**: La HRV es un indicador clave de la regulación autonómica del corazón, permitiendo evaluar el equilibrio entre el sistema nervioso simpático y parasimpático. Cambios en la HRV pueden indicar desequilibrios en esta regulación, lo que puede estar asociado con diversas condiciones de salud.
* **Pronóstico de enfermedades cardiovasculares**: La HRV se ha relacionado con el riesgo de eventos cardiovasculares adversos, como infartos de miocardio y muerte súbita cardíaca.
* **Evaluación de la adaptabilidad del corazón**: La capacidad del corazón para ajustar su frecuencia en respuesta a estímulos fisiológicos y emocionales se refleja en la HRV. Una HRV adecuada sugiere una adaptabilidad saludable del corazón a diferentes situaciones.
* **Monitorización de la salud y el estrés** La HRV puede utilizarse como una herramienta para evaluar el impacto del estrés, la fatiga y otras condiciones en el sistema cardiovascular. Cambios en la HRV pueden indicar alteraciones en la respuesta del cuerpo a factores estresantes

En la siguiente tabla, elaborada utilizando la referencia [7], se explicará en detalle cómo se relacionan los cambios en el HRV con diversas patologías. La variabilidad del HRV se mide utilizando el SDNN (Standard Deviation of NN intervals), una medida crucial en el análisis del Heart Rate Variability. El SDNN se refiere a la desviación estándar de los intervalos NN (intervalos entre latidos normales) en un registro de ECG. A diferencia de los intervalos RR, que incluyen todos los latidos sucesivos, los intervalos NN excluyen los latidos ectópicos o artefactos, proporcionando así una medida más precisa de la variabilidad en condiciones normales. El SDNN refleja todas las variaciones cíclicas presentes en el registro, incluyendo las de origen fisiológico y patológico. Un SDNN alto indica una alta variabilidad en los intervalos entre latidos, lo que generalmente se asocia con un buen estado de salud y una capacidad de adaptación eficiente del sistema nervioso autónomo. Por otro lado, un SDNN bajo indica una baja variabilidad en los intervalos entre latidos, lo que puede ser un signo de estrés, fatiga, enfermedad cardiovascular o disfunción autonómica.

| Cambio en el HRV                        | Relación con Patologías                                                                                      | Magnitud del Cambio                                          |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Reducción significativa del HRV         | Indicador de enfermedades cardíacas, riesgo elevado de muerte súbita, insuficiencia cardíaca congestiva.     | HRV total significativamente menor (<50 ms SDNN)             |
| Reducción moderada del HRV              | Asociado con condiciones de estrés, fatiga, depresión, y enfermedades crónicas no específicas.               | HRV moderadamente reducido (50-100 ms SDNN)                  |
| Incremento del HRV                      | Frecuentemente observado en atletas bien entrenados, indicando un sistema cardiovascular saludable y una alta capacidad de adaptación autónoma. | HRV elevado (>100 ms SDNN)                                   |
| Variabilidad circadiana reducida        | Relacionada con desórdenes del sueño, diabetes, y disfunción autonómica.                                      | Variabilidad circadiana significativamente reducida          |

<p align="center">
  <b> Tabla 1. Cambios en el HRV y su Relación con Patologías </b>
</p>


## **Objetivos del Laboratorio** <a name = "t3"></a>

  
## Metodología <a name="t4"></a>
En este laboratorio, nos enfocaremos en el tratamiento de la señal de ECG adquirida previamente utilizando el Kit BITalino. 

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
  <b>Tabla 2. Materiales y equipos utilizados</b>
</p>

### **Procedimiento** <a name="t6"></a>

## Filtros para el procesamiento de ECG <a name="t7"></a>




## Comparación de filtros  <a name="t8"></a>



## Segmentación  <a name="t9"></a>


## Extracción de características  <a name="t10"></a>


***Procesamiento mediante la libreria de opensingals***: 


## Discusión de los resultados  <a name="t11"></a>



## Conclusiones <a name="t12"></a>



## Archivos <a name="t13"></a>

- [Programa de procesamiento de señal EMG (python)](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L8_Procesamiento_EMG/LAB_8.ipynb) 


## Bibliografía: <a name="t14"></a>











