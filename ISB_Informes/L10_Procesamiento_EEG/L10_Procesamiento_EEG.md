# Laboratorio N°10 - Procesamiento EEG

## Tabla de contenidos:
 __________________________________________________________________________________________________
1. [Lista de participantes](#t1)
2. [Introducción](#t2)
3. [Metodología](#t4)\
   3.1.[Adquisición de la señal](#t7)\
   3.2.[Filtrado](#t8)\
   3.3. [Extracción de características](#t10)\
   3.4.[Generación de señales y obtención de características](#t11)
7. [Discusión](#t12)
8. [Conclusión](#t13)
9. [Archivos](#t14)
7. [Bibliografía](#t15)
__________________________________________________________________________________________________
## **Lista de participantes** <a name = "t1"></a>
* Jimena Alpiste Espinoza - 74297329
* Jossymar León Mallma - 74905684
* Renato Cardoso Reategui - 73061678


## Introducción  <a name = "t2"></a>
La electroencefalografía (EEG) es una técnica no invasiva que se utiliza para registrar la actividad eléctrica del cerebro. El EEG mide las fluctuaciones de voltaje resultantes de las corrientes iónicas dentro de las neuronas del cerebro [1]. Estas señales eléctricas se detectan mediante electrodos colocados sobre el cuero cabelludo y se registran en función del tiempo, lo que permite obtener una representación de los patrones de actividad cerebral [2].


<div align="center">
    <img src="Imagenes_L10\Figura1.png" alt="wCF14V" width="400">
    <p><b>Figura 1. Muestras de ondas cerebrales con frecuencias dominantes pertenecientes a las bandas beta, alfa, theta y delta y gamma. Extraído de [3] </b> </p>
</div>

El EEG es capaz de detectar y registrar diferentes tipos de ondas cerebrales, que se clasifican según su frecuencia y amplitud [3] . A continuación se mostrarán los cinco principales tipos de ondas cerebrales en una tabla, basada en la información de la referencia [4]: 

| **Tipo de Onda** | **Frecuencia (Hz)** | **Características y Estado Cerebral** |
|------------------|---------------------|---------------------|
| **Delta**        | 0.5-4               | Ondas de baja frecuencia y alta amplitud observadas durante el sueño profundo y los estados de inconsciencia, destacándose en las regiones frontocentrales de la cabeza. Patológicamente, se presenta en personas despiertas con encefalopatía generalizada y disfunción cerebral focal, relacionada con epilepsia del lóbulo temporal. |
| **Theta**        | 4-8                 | Durante la somnolencia y las primeras etapas del sueño, se manifiesta el ritmo theta, destacándose especialmente en las regiones frontocentrales de la cabeza. A medida que la somnolencia avanza, este ritmo se desplaza gradualmente hacia las áreas posteriores del cerebro, sustituyendo progresivamente al ritmo alfa. En estados emocionales intensos, la actividad de la onda theta se intensifica. Además, su presencia durante los estados de vigilia puede indicar una disfunción cerebral focal. |
| **Alfa**         | 8-13                | Este ritmo se observa durante estados de relajación y vigilia tranquila, así como en actividades mentales poco exigentes. Es predominante en la región occipital de adultos despiertos y constituye un patrón fundamental en el EEG desde temprana edad hasta edades avanzadas en individuos sanos. Las ondas alfa se hacen más notables con los ojos cerrados y durante la relajación mental, disminuyendo cuando se abren los ojos y durante el esfuerzo mental. La amplitud de este ritmo varía entre individuos y también dentro de un mismo individuo en diferentes momentos. En casos de encefalopatía difusa, puede observarse una actividad alfa generalizada que no responde a estímulos, mientras que la disminución del ritmo alfa se considera un indicador de disfunción cerebral generalizada. |
| **Beta**         | 13-30               | Predominante en adultos y niños sin anomalías, es más notable en las regiones frontal y central de la cabeza, disminuyendo hacia las áreas posteriores. Se asocia con estados de alerta, atención activa, concentración y pensamiento activo. Además, muchos medicamentos sedantes como barbitúricos, hidrato de cloral y benzodiazepinas aumentan tanto la amplitud como la frecuencia del ritmo beta en los individuos. La atenuación focal, regional o hemisférica del ritmo beta puede estar relacionada con lesiones corticales, malformaciones, o acumulaciones de líquido subdural, epidural o subgaleal. |
| **Gamma**        | 30-100              | Estas ondas de alta frecuencia están asociadas con la percepción consciente, la integración de información y los procesos cognitivos de alto nivel. Se sugiere que estos ritmos están relacionados con la integración de percepciones sensoriales y la atención. Además, estos ritmos pueden ser útiles para detectar desmielinización y otros problemas de integridad cortical. |

<p align="center">
  <b>Tabla 1. Características de las 5 principales ondas cerebrales. </b>
</p>

Hay varios métodos propuestos en la literatura para la clasificación de señales EEG, los cuales se pueden dividir en cuatro categorías: preprocesamiento, segmentación, extracción de características y clasificación. Este procedimiento se explicará a continuación usando la referencia [1]. Asimismo, estos cuatro pasos del tratamiento de señales ECG se muestran a modo de diagrama en la figura 2. 

<div align="center">
    <img src="Imagenes_L10\Figura2.png" alt="wCF14V" width="500">
    <p><b> Figura 2. Etapas del ánalisis de la Señal EEG. Extraído de [1] </b> </p>
</div>


**Etapas de la clasificación:** 

* **Adquisición**Como se mencionó anteriormente, para adquirir las señales EEG los electrodos se colocan en el cuero cabelludo, donde la data se puede recoger de manera invasiva (con electrodos implantados) o no invasiva (con electrodos en la superficie del cuero cabelludo). La mayoría de los métodos actuales utilizan técnicas no invasivas debido a su menor riesgo y mayor facilidad de uso.
* **Eliminación de ruido**: Las señales EEG suelen contener ruido y artefactos provenientes de diversas fuentes como movimientos musculares, parpadeos y actividad cardíaca. Para obtener datos precisos, es esencial eliminar estos ruidos utilizando técnicas como la regresión, el análisis de componentes independientes (ICA), y la transformación de wavelet, que ayudan a separar y eliminar las fuentes de ruido manteniendo la señal de interés.
*  **Ingeniería de características**: Esta etapa consiste en extraer las características más relevantes de las señales EEG para facilitar su análisis. Para ello se analizan las propiedades espectrales, temporales y de conectividad funcional mediante métodos como el análisis de Fourier y de wavelets. Esto nos permite capturar patrones y dinámicas subyacentes, útiles en aplicaciones como interfaces cerebro-computadora, monitoreo cognitivo y diagnóstico de trastornos neurológicos.
*  **Clasificación**: En esta etapa, las características extraídas se utilizan para clasificar las señales EEG en diferentes categorías. Se aplican algoritmos de machine learning y deep learning, como las máquinas de soporte vectorial (SVM) y las redes neuronales convolucionales (CNN), que pueden aprender a identificar patrones complejos en las señales EEG y realizar tareas como la detección de enfermedades neurológicas, la identificación de estados cognitivos y más.


## **Objetivos del Laboratorio** <a name = "t3"></a>

## Metodología <a name="t4"></a>

## Adquisición de la señal <a name="t7"></a>


## Filtros para el procesamiento de EEG <a name="t8"></a>



***Resultados***: 


***Resultados***: 

## Extracción de características  <a name="t10"></a>



## Generación de señales y obtención de características <a name="t11"></a>




## Discusión de los resultados  <a name="t12"></a>


   
## Conclusiones <a name="t13"></a>

## Archivos <a name="t14"></a>

- [Programa de procesamiento de señal EEG (python)](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L9_Procesamiento_ECG/LAB_9.ipynb) 


## Bibliografía: <a name="t15"></a>

[1] A. Chaddad, Y. Wu, R. Kateb, y A. Bouridane, “Electroencephalography Signal Processing: A Comprehensive Review and Analysis of Methods and Technique” », Sensors, vol. 23, n.o 14, p. 6434, jul. 2023, doi: 10.3390/s23146434.

[2] M. X. Cohen, “Where Does EEG Come From and What Does It Mean?”, Trends In Neurosciences, vol. 40, n.o 4, pp. 208-218, abr. 2017, doi: 10.1016/j.tins.2017.02.004.

[3] P. A. Abhang, B. W. Gawali, y S. C. Mehrotra, “Technological Basics of EEG Recording and Operation of Apparatus”, en Elsevier eBooks, 2016, pp. 19-50. doi: 10.1016/b978-0-12-804490-2.00002-6.

[4] C. S. Nayak and A. C. Anilkumar, "EEG Normal Waveforms," in StatPearls [Internet], Treasure Island (FL): StatPearls Publishing, updated Jul. 24, 2023, Available: https://www.ncbi.nlm.nih.gov/books/NBK539805.









