# Laboratorio N°4 - Uso de BITalino para ECG

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
   6.3 [Archivos de la señal ploteada en Python y datos de la señal](#t9)
7. [Señal del Promsim4](#t10)
8. [Conclusiones](#t11)
9. [Bibliografía](#t12)
__________________________________________________________________________________________________
## **Lista de participantes** <a name = "t1"></a>
* Jimena Alpiste Espinoza - 74297329
* Jossymar León Mallma - 
* Renato Cardoso Cardenas - 73061678


https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L4_Lectura_de_ECG/Imagenes_L4/video_ejercicios_jossymar.mp4
## Introducción  <a name = "t2"></a>
[insertar parrafo de intro]

## **Objetivos del Laboratorio** <a name = "t3"></a>
* Adquirir señales biomédicas de ECG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales ECG del software OpenSignals (r)evolution
  
## **Materiales y equipos** <a name="t4"></a>
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
Para capturar las señales ECG, se empleó el dispositivo BITalino junto con su sensor ECG de tres electrodos. Se siguió el procedimiento detallado en la guía BiTalino,**(BITalino HOME-GUIDE #2 ELECTROCARDIOGRAPHY (ECG) Exploring Cardiac Signals at the Skin Surface")** [1], como referencia para posicionar correctamente los electrodos en el sujeto de prueba. A continuación, se presentan los protocolos de conexión específicos utilizados en cada prueba llevada a cabo en este laboratorio:

| Figura X. Colocación de electrodos para la derivación I referencia[1].                                                                                                   | Figura X. Colocación de los electrodos en el laboratorio para la derivación I                                                                                                     |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| ![Electrodos de guía](Imagenes_L4/electrodos_guia.png) | <img src="Imagenes_L4/posicion _usada_electrodos.png" alt="Electrodos de guía" width="700"> |


La derivación 1 en un ECG es una de las vistas básicas utilizadas para monitorear la actividad eléctrica del corazón. La colocación adecuada de los electrodos es fundamental para capturar con precisión esta actividad. En la Figura X se muestra la colocación de los electrodos para esta derivación. En esta configuración, se utilizaron tres electrodos: 
* IN+ (rojo) se coloca en la muñeca izquierda .
* IN- (negro) se coloca en la muñeca derecha.
* REF (blanco) se coloca en la cresta ilíaca.\

Cabe resaltar que las ubicaciones mencionadas se mantuvieron para todas las pruebas: 

- Prueba 1: Lectura del Estado Basal
- Prueba 2: Lectura de los ciclos de Inhalación y Exhalación (Fases de 5 segundos) 
- Prueba 3: Segunda lectura en estado de reposo
- Prueba 4: Lectura posterior a la realización de ejercicio intenso. Ejercicios realizados: planchas y polichinelas

https://github.com/renatog2500/inb_2024_gh12/assets/130946164/7802253f-a10b-4bd8-b5fc-664aa1a81318
  
- Prueba 5: Tercera lectura en estado de reposo
- Prueba 6: Lectura de los ciclos de Inhalación y Exhalación prolongada (Fases de 10 segundos)





## Resultados y discusión  <a name="t6"></a>
### **Visualización de señal eléctrica mediante video y OpenSignalsl** <a name="t7"></a>

<table align="center">
  <tr>
    <th> PRUEBA </th>
    <th> VIDEO </th>
    <th> DESCRIPCIÓN </th>
  </tr>
  <tr>
    <th> 1.Lectura de la señal Basal </th>
    <td> [![](https://markdown-videos-api.jorgenkh.no/youtube/gG2bqgt_6po)](https://youtu.be/gG2bqgt_6po)</td>
    <td> En la prueba 1 se tomo señales ECG del sujeto de prueba en estado de reposo.</td>
  </tr>
   <tr>
    <th> 2. Lectura de los ciclos de Inhalación y Exhalación (Fases de 5 segundos)</th>
    <td>https://github.com/renatog2500/inb_2024_gh12/assets/130946164/dc749f45-d7ee-46b9-a4ab-283b90a89cf0</td>
    <td>En la 2da prueba el sujeto realizó ciclos de inhalación y exhalación de intervalos de 5 segundos durante 30 segundos, se tomó la lectura del comportamiento de la señal ECG.</td>
  </tr>
   <tr>
    <th> 3. Segunda lectura en estado de repos</th>
    <td>https://github.com/renatog2500/inb_2024_gh12/assets/130946164/dc749f45-d7ee-46b9-a4ab-283b90a89cf0</td>
    <td> Se volvió a realizar la captura de la señal del electrocardiograma (ECG) del sujeto después de la sesión de ejercicios de inhalación y exhalación. </td>
  </tr>
   <tr>
    <th> 4. Lectura posterior a la realización de ejercicios </th>
    <td>https://github.com/renatog2500/inb_2024_gh12/assets/130946164/dc749f45-d7ee-46b9-a4ab-283b90a89cf0</td>
    <td>El sujeto fue sometido a una serie de ejercicios físicos que incluyeron la realización de planchas y polichinelas. Luego de completar estos ejercicios, se procedió a tomar la señal del electrocardiograma (ECG). </td>
  </tr>
   <tr>
    <th> 5.Tercera lectura en estado de reposo </th>
    <td>https://github.com/renatog2500/inb_2024_gh12/assets/130946164/dc749f45-d7ee-46b9-a4ab-283b90a89cf0</td>
    <td>Se llevó a cabo una nueva toma de la señal del electrocardiograma (ECG) del sujeto en reposo después de completar la serie de ejercicios. </td>
  </tr>
     <th> 6.Inhalación y exhalación prolongada durante 10 segundos</th>
    <td>https://github.com/renatog2500/inb_2024_gh12/assets/130946164/dc749f45-d7ee-46b9-a4ab-283b90a89cf0</td>
    <td>En la sexta prueba, el sujeto llevó a cabo ciclos de inhalación y exhalación en intervalos de 10 segundos. Durante este proceso, se registró y analizó el comportamiento de la señal del electrocardiograma (ECG).

</td>
  </tr>
</table>
<p align="center">
  <b>Tabla 2. Pruebas realizadas</b>
</p>


### **Explicación de la variación de la señal**

**1. Estado de reposo (lectura basal):** Durante el estado de reposo, la señal EKG presenta un patrón regular y estable, reflejando la actividad eléctrica normal del corazón. Las ondas P, QRS y T se observan claramente, y los intervalos entre ellas son consistentes [1].

**2.Inhalación y exhalación en series de 5 segundos durante 30 segundos:** Durante la inspiración, se produce un aumento en la frecuencia cardíaca y una disminución en la variabilidad de la frecuencia cardíaca (VFC). Esto se debe a la estimulación del sistema nervioso simpático y la inhibición del sistema nervioso parasimpático. Durante la espiración, se observa una disminución en la frecuencia cardíaca y un aumento en la VFC, lo que refleja la activación del sistema nervioso parasimpático [2], [3].

**3. Lectura basal después de la respiración controlada:** Después de la respiración controlada, la señal EKG vuelve a un patrón similar al observado en la lectura basal inicial. Sin embargo, pueden presentarse ligeras variaciones debido a los efectos residuales de la respiración controlada en el sistema nervioso autónomo [1], [3].

**4. Lectura posterior a una serie de ejercicios:** Después del ejercicio, se observa un aumento significativo en la frecuencia cardíaca y cambios en la morfología de las ondas del EKG. La onda T puede aparecer invertida o aplanada, y el segmento ST puede presentar una depresión o elevación. Estos cambios se deben a la activación del sistema nervioso simpático y al aumento de las demandas metabólicas del corazón durante el ejercicio [4], [5].

**5. Lectura basal después del ejercicio:** Después del ejercicio, la señal EKG gradualmente vuelve a un patrón similar al de la lectura basal inicial. Sin embargo, la frecuencia cardíaca puede permanecer elevada durante un período de tiempo, y la morfología de las ondas puede tardar en normalizarse. Esto se debe a la recuperación gradual del sistema nervioso autónomo y al restablecimiento del equilibrio simpático-parasimpático [4], [5].

**6. Inhalación y exhalación prolongada durante 10 segundos:** Durante la inhalación prolongada, se observa un aumento sostenido en la frecuencia cardíaca y una disminución en la VFC, similar a lo observado en las series de respiración más cortas. Durante la exhalación prolongada, se produce una disminución sostenida en la frecuencia cardíaca y un aumento en la VFC. Estos cambios son más pronunciados en comparación con las series de respiración más cortas debido a la mayor duración de la estimulación de los sistemas nerviosos simpático y parasimpático [2], [3].


### **Ploteo de la señal en Python** <a name="t8"></a>
- Código en Python:
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
### **Archivos** <a name="t9"></a>
- [Documentos (.txt)](https://github.com/renatog2500/inb_2024_gh12/tree/be701a0d1b2c92ef9167bfc775c26846401e695d/Documentaci%C3%B3n/EMG)
- [Programa de ploteo (python)](https://github.com/renatog2500/inb_2024_gh12/blob/main/Software/Ploteo_de_datos_lab.py)





## Señal del Promsim4 : <a name="t10"></a>
<table align="center">
  <tr>
    <th> Simulación </th>
    <th> Toma </th>
    <th> Descripción </th>
  </tr>
  <tr>
    <th> Paso 1. RSN (adulto): Frecuencia Respiratoria Normal en Adultos</th>
    <td>video </td>
    <td> En la prueba 1 se tomo señales ECG del sujeto de prueba en estado de reposo.</td>
  </tr>
   <tr>
    <th> Paso 2. Onda de presión venosa central (CVP)</th>
    <td> video 2 </td>
    <td>En la 2da prueba el sujeto realizó ciclos de inhalación y exhalación de intervalos de 5 segundos durante 30 segundos, se tomó la lectura del comportamiento de la señal ECG.</td>
  </tr>
   <tr>
    <th> Paso 3. Taquicardia ventricular a 160 lpm </th>
    <td>https://github.com/renatog2500/inb_2024_gh12/assets/130946164/dc749f45-d7ee-46b9-a4ab-283b90a89cf0</td>
    <td> Se volvió a realizar la captura de la señal del electrocardiograma (ECG) del sujeto después de la sesión de ejercicios de inhalación y exhalación. </td>
  </tr>
   <tr>
    <th> Paso 4. Fibrilación ventricular severa </th>
    <td>https://github.com/renatog2500/inb_2024_gh12/assets/130946164/dc749f45-d7ee-46b9-a4ab-283b90a89cf0</td>
    <td>El sujeto fue sometido a una serie de ejercicios físicos que incluyeron la realización de planchas y polichinelas. Luego de completar estos ejercicios, se procedió a tomar la señal del electrocardiograma (ECG). </td>
  </tr>
   <tr>
    <th> Paso 5. Asistolia </th>
    <td>https://github.com/renatog2500/inb_2024_gh12/assets/130946164/dc749f45-d7ee-46b9-a4ab-283b90a89cf0</td>
    <td>Se llevó a cabo una nueva toma de la señal del electrocardiograma (ECG) del sujeto en reposo después de completar la serie de ejercicios. </td>
  </tr>
</table>
<p align="center">
  <b>Tabla 2. Pruebas realizadas</b>
</p>

## **Conclusiones** <a name="t11"></a>

//////////////////////

## **Bibliografía** <a name="t12"></a>
[1] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1888690/

[2] https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2017.00258/full

[3] https://academic.oup.com/eurheartj/article/17/3/354/485572

[4] https://www.sciencedirect.com/science/article/pii/S073510970700232X

[5] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4493772/ 


