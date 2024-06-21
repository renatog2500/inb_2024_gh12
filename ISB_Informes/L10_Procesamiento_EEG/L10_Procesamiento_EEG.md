# Laboratorio N°10 - Procesamiento EEG

## Tabla de contenidos:
 __________________________________________________________________________________________________
1. [Lista de participantes](#t1)
2. [Introducción](#t2)
3. [Metodología](#t4)\
   3.1.[Adquisición de la señal](#t7)\
   3.2. [Análisis de componentes independientes (ICA)](#t9)\
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
- Aplicar técnicas avanzadas de filtrado y eliminación de artefactos en las señales EEG para asegurar una señal limpia y lista para análisis detallado.
- Normalizar y alinear las señales EEG durante el preprocesamiento para garantizar consistencia y comparabilidad entre sesiones y sujetos.
- Implementar y optimizar la extracción de características mediante análisis Wavelet y técnicas de feature engineering, mejorando la precisión de los modelos de machine learning en la clasificación de patrones de actividad cerebral.
  
## Metodología <a name="t4"></a>

## Adquisición de la señal <a name="t7"></a>
Para la adquisición de la señal se utilizó la base de datos PhysioNet, específicamente el estudio "EEG During Mental Arithmetic Tasks" [5] . Este estudio registró la actividad cerebral de los sujetos antes y durante la realización de tareas de aritmética mental, las cuales consistían en realizar restas en serie de dos números. Cada prueba comenzó con la comunicación oral de un número de 4 dígitos y otro de 2 dígitos.

Las señales EEG del estudio fueron adquiridas utilizando el sistema Neurocom EEG de 23 canales. Se colocaron electrodos de plata/cloruro de plata en el cuero cabelludo de los sujetos siguiendo el esquema internacional 10/20, con todos los electrodos referenciados a electrodos interconectados en las orejas. Se aplicaron un filtro de paso alto con una frecuencia de corte de 30 Hz y un filtro de muesca de línea eléctrica de 50 Hz para eliminar el ruido. Los segmentos de EEG grabados, cada uno de 60 segundos de duración, estaban libres de artefactos gracias a la aplicación de Análisis de Componentes Independientes (ICA) durante el preprocesamiento de datos, lo que eliminó artefactos de ojos, músculos y pulsaciones cardíacas.

## Análisis de componentes independientes (ICA)<a name="t9"></a>
Como se mencionó anteriormente, para el análisis de los datos de EEG es posible utilizar el método de Análisis de Componentes Independientes (ICA) con el objetivo de identificar y eliminar componentes artefactuales. Los criterios para elegir los índices del EEG a utilizar para el ICA incluyen las siguientes medidas, basándonos en la referencia [6]:

1. **Pendiente Espectral**: Esta medida calcula la pendiente del espectro de potencia de cada componente independiente (IC) en una escala log-log entre 7 y 75 Hz. Se espera que los ICs de origen muscular tengan pendientes positivas, mientras que los ICs de origen neural tengan pendientes negativas.

2. **Periferalidad**: Esta medida evalúa la fortaleza de un IC en cada electrodo y lo muestra como topografías del cuero cabelludo. Al ponderar estas fortalezas por la distancia de un electrodo desde el vértice de la cabeza y sumarlas, se obtiene una medida que será grande para fuentes que se originan cerca de la periferia del casquete y pequeña para fuentes cercanas al centro.

3. **Suavidad Espacial**: Esta medida calcula la diferencia relativa en magnitud entre pares de electrodos ponderada por la distancia entre ellos y suma sobre todos los pares. Se espera que las fuentes mixtas tengan grandes variaciones locales en magnitud y, por lo tanto, un alto valor de suavidad espacial, mientras que los componentes con una sola fuente tendrán pequeñas variaciones locales y un valor bajo de suavidad espacial.

## Filtros para el procesamiento de EEG <a name="t8"></a>



***Resultados***: 

<div align="center">
    <img src="Imagenes_L10\ICA000.png" alt="wCF14V" width="400">
    <p><b>Figura 3. ICA000 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA001.png" alt="wCF14V" width="400">
    <p><b>Figura 4. ICA001 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA002.png" alt="wCF14V" width="400">
    <p><b>Figura 5. ICA002 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA003.png" alt="wCF14V" width="400">
    <p><b>Figura 6. ICA003 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA004.png" alt="wCF14V" width="400">
    <p><b>Figura 7. ICA004 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA005.png" alt="wCF14V" width="400">
    <p><b>Figura 8. ICA005 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA006.png" alt="wCF14V" width="400">
    <p><b>Figura 9. ICA006 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA007.png" alt="wCF14V" width="400">
    <p><b>Figura 10. ICA007 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA008.png" alt="wCF14V" width="400">
    <p><b>Figura 11. ICA008 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA009.png" alt="wCF14V" width="400">
    <p><b>Figura 12. ICA009 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA010.png" alt="wCF14V" width="400">
    <p><b>Figura 13. ICA010 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA011.png" alt="wCF14V" width="400">
    <p><b>Figura 14. ICA011 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA012.png" alt="wCF14V" width="400">
    <p><b>Figura 15. ICA012 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA013.png" alt="wCF14V" width="400">
    <p><b>Figura 16. ICA013 </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L10\ICA014.png" alt="wCF14V" width="400">
    <p><b>Figura 17. ICA014 </b> </p>
</div>
### Aplicación de los Criterios para la selección de los ICAs

Para seleccionar los ICAs más adecuados para el análisis, utilicé los siguientes criterios basados en las recomendaciones para el uso del ICA en EEG:

- **ICA006**: Presenta una actividad más concentrada, lo que sugiere una fuente centralizada, típicamente neural.
- **ICA003**: Muestra una actividad concentrada en el centro y la parte inferior del casquete, lo que sugiere una fuente neural.
- **ICA002**: Actividad centralizada, sugiriendo una fuente neural.
- **ICA000**: Similar a los anteriores, con actividad centralizada.
- **ICA001**: Muestra una actividad concentrada y centralizada.
- **ICA008**: Actividad dispersa pero con cierta concentración en el centro, lo que sugiere una mezcla con una mayor probabilidad de contener fuentes neuronales.
- **ICA012**: Actividad dispersa pero con mayor concentración central, sugiriendo una mayor probabilidad de ser neural.


## Extracción de características  <a name="t10"></a>

*Extracción de Características de Señales EEG usando OSFBCSP

Nos basaremos en la investigación realizada por Shang et. al. en donde implementan el método de extracción de características haciendo uso del modelo OSFBCSP.

*Descripción del Método

El proceso de extracción de características de las señales EEG se realiza utilizando el método OSFBCSP (Overlapping Sub-band Filter Banks Common Spatial Pattern). Este método consta de tres etapas principales:

1. Filtrado multi-banda
2. Cálculo de características usando el algoritmo CSP
3. Selección de características

*Parámetros de Extracción de Características

| Parámetro | Valor/Descripción |
|-----------|-------------------|
| Número de sub-bandas | 4 |
| Ancho de banda de cada sub-banda | 4 Hz |
| Superposición entre sub-bandas | 2 Hz |
| Sub-banda 1 | 6-10 Hz |
| Sub-banda 2 | 8-12 Hz |
| Sub-banda 3 | 10-14 Hz |
| Sub-banda 4 | 12-16 Hz |
| Método de filtrado espacial | Common Spatial Pattern (CSP) |
| Selección de características | Basada en información mutua |
| Reducción de dimensionalidad | Análisis Discriminante Lineal (LDA) |


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

[5] "EEG during Mental Arithmetic Tasks V1.0.0", 17 de diciembre de 2018. https://physionet.org/content/eegmat/1.0.0/

[6] Dhani Dharmaprani, Hoang K. Nguyen, Trent W. Lewis, Dylan DeLosAngeles, John O. Willoughby, and Kenneth J. Pope. "A comparison of independent component analysis algorithms and measures to discriminate between EEG and artifact components". In 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), 825–828. Orlando, FL, USA, 2016. IEEE. doi:10.1109/EMBC.2016.7590828.



