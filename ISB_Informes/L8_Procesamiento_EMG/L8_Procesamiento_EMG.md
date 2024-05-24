# Laboratorio N°8 - Procesamiento EMG

## Tabla de contenidos:
 __________________________________________________________________________________________________
1. [Lista de participantes](#t1)
2. [Introducción](#t2)
3. [Objetivos del laboratorio](#t3)
4. [Metodología](#t4)\
   4.1.[Materiales y Equipo utilizado](#t5)\
   4.2.[Procedimiento](#t6)
6. [Resultados](#t7)\
   5.1 [Ejercicio ECG](#t8)\
7. [Discusión](#t9)\
8. [Códigos](#t10)\
7. [Bibliografía](#t11)
__________________________________________________________________________________________________
## **Lista de participantes** <a name = "t1"></a>
* Jimena Alpiste Espinoza - 74297329
* Jossymar León Mallma - 74905684
* Renato Cardoso Cardenas - 73061678


## Introducción  <a name = "t2"></a>


## **Objetivos del Laboratorio** <a name = "t3"></a>
* Obtener características estadísticas de la señal: Incluye la extracción de características como la amplitud de la señal, el valor promedio (media), la frecuencia y el valor Root Mean Square (RMS) de la señal EMG.
* Realizar el análisis de las características y compararlo con valores de la literatura: Evalúa las características extraídas y compáralas con valores de referencia disponibles en la literatura. Esto ayuda a entender cómo se comporta la señal en relación con los datos previamente documentados.
* Verificar el comportamiento de la señal EMG: Asegúrate de examinar el comportamiento general de la señal EMG para identificar patrones, tendencias o anomalías que puedan ser relevantes para tu análisis o aplicación específica.
  
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



***Justificación de parámetros para la Señal ECG***
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



## Resultados   <a name="t7"></a>

### **Ejercicio EMG** <a name="t9"></a>
| Campo de actividad | Señal Cruda | Filtro Wavelet |
|-----------------|-------------------------|-----------|
| Bicep Braquial             |![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Lectura_bicep_braquial.png)|![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/WaveLet_Lectura_bicep_braquial.png)|
| Antebrazo en Supinación        |![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Lectura_supinaci%C3%B3n_antebrazo.png)|![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/WaveLet_Lectura_supinaci%C3%B3n_antebrazo.png)|
| Pulgar en supinacion            |![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/Lectura_pulgar_supinaci%C3%B3n_EMG.png)|![Ejemplo](https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L7_Filtrado_DWT/Imagenes_L7/WaveLet_Lectura_pulgar_supinaci%C3%B3n_EMG.png)|

<p align="center">
  <b>Tabla 3. Resumen de la señal filtrada para la data EMG</b>
</p>


## Discusión <a name="t11"></a>




## Bibliografía: <a name="t15"></a>












