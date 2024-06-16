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


<div align="center">
    <img src="Imagenes_L9\Figura_1.png" alt="wCF14V" width="500">
    <p><b>Figura 1. Señal de ECG de latido cardíaco normal. Extraído de [2] </b> </p>
</div>



<div align="center">
    <img src="Imagenes_L9\Figura_2.png" alt="wCF14V" width="300">
    <p><b> Figura 2.Diagrama de la clasificación de la señal ECG. Extraído de [2] </b> </p>
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











