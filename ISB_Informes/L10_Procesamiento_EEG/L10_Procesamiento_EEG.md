# Laboratorio N°10 - Procesamiento EEG

## Tabla de contenidos:
 __________________________________________________________________________________________________
1. [Lista de participantes](#t1)
2. [Introducción](#t2)
3. [Objetivos del laboratorio](#t3)
4. [Metodología](#t4)\
   4.1.[Materiales y Equipo utilizado](#t5)\
   4.2.[Procedimiento](#t6)\
       4.2.1.[Adquisición de la señal](#t7)\
       4.2.3.[Filtrado](#t8)\
       4.2.4.[Obtención de la variabilidad de la frecuencia cardíaca (HRV)](#t9)\
       4.2.5.[Extracción de características](#t10)\
       4.2.6.[Generación de señales y obtención de características](#t11)
7. [Discusión](#t12)
8. [Conclusión](#t13)
9. [Archivos](#t14)
7. [Bibliografía](#t15)
__________________________________________________________________________________________________
## **Lista de participantes** <a name = "t1"></a>
* Jimena Alpiste Espinoza - 74297329
* Jossymar León Mallma - 74905684
* Renato Cardoso Cardenas - 73061678


## Introducción  <a name = "t2"></a>
La electroencefalografía (EEG) es una técnica no invasiva que se utiliza para registrar la actividad eléctrica del cerebro. El EEG mide las fluctuaciones de voltaje resultantes de las corrientes iónicas dentro de las neuronas del cerebro [1]. Estas señales eléctricas se detectan mediante electrodos colocados sobre el cuero cabelludo y se registran en función del tiempo, lo que permite obtener una representación de los patrones de actividad cerebral [2].


<div align="center">
    <img src="Imagenes_L10\Figura_1.png" alt="wCF14V" width="500">
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
    <img src="Imagenes_L10\Figura_1.png" alt="wCF14V" width="500">
    <p><b>Figura 2. Muestras de ondas cerebrales con frecuencias dominantes pertenecientes a las bandas beta, alfa, theta y delta y gamma. Extraído de [1] </b> </p>
</div>

<div align="center">
    <img src="Imagenes_L9\Figura_2.png" alt="wCF14V" width="300">
    <p><b> Figura 2. Etapas del ánalisis de la Señal EEG. Extraído de [4] </b> </p>
</div>

**Etapas de la clasificación:** 


## **Objetivos del Laboratorio** <a name = "t3"></a>

## Metodología <a name="t4"></a>
En este laboratorio, nos enfocaremos en el tratamiento de la señal de EEG adquirida previamente utilizando el Kit BITalino. 

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

## **Procedimiento** <a name="t6"></a>

## Adquisición de la señal <a name="t7"></a>

Para capturar las señales ECG, se empleó el dispositivo BITalino junto con su sensor ECG de tres electrodos. Se siguió el procedimiento detallado en la guía BiTalino,**(BITalino HOME-GUIDE #2 ELECTROCARDIOGRAPHY (ECG) Exploring Cardiac Signals at the Skin Surface")** [8], como referencia para posicionar correctamente los electrodos en el sujeto de prueba. A continuación, se presentan los protocolos de conexión específicos utilizados en cada prueba llevada a cabo en este laboratorio:

| Figura 3. Colocación de electrodos para la derivación I referencia[8].                                                                                                   | Figura 4. Colocación de los electrodos en el laboratorio para la derivación I                                                                                                     |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| ![Electrodos de guía](Imagenes_L9/Figura_3.png) | <img src="Imagenes_L9/Figura_4.png" alt="Electrodos de guía" width="700"> |


**Protocolo:**


## Filtros para el procesamiento de ECG <a name="t8"></a>



***Resultados***: 



## Obtención de la variabilidad de la frecuencia cardíaca (HRV):  <a name="t9"></a>


***Resultados***: 

## Extracción de características  <a name="t10"></a>


***Mostramos como obtenemos dichas características del BioSignal***: 

## Generación de señales y obtención de características <a name="t11"></a>

### Reposo


## Discusión de los resultados  <a name="t12"></a>


   
## Conclusiones <a name="t13"></a>

## Archivos <a name="t14"></a>

- [Programa de procesamiento de señal EEG (python)](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L9_Procesamiento_ECG/LAB_9.ipynb) 


## Bibliografía: <a name="t15"></a>











