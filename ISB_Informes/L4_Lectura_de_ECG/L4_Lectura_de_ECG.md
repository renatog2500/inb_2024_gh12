# Laboratorio N°4 - Uso de BITalino para ECG

## Tabla de contenidos:
 __________________________________________________________________________________________________
1. [Lista de participantes](#t1)
2. [Introducción](#t2)
3. [Objetivos del laboratorio](#t3)
4. [Materiales y Equipo Utilizado](#t4)
5. [Protocolo de conexión](#t5)
6. [Resultados](#t6)\
   6.1 [Visualización de la señal mediante video y OpenSignals ](#t7)\
   6.2 [Ploteo de la señal en Python](#t8)\
   6.3 [Archivos de la señal ploteada en Python y datos de la señal](#t9)
7. [Conclusiones](#t10)
8. [Bibliografía](#t11)
__________________________________________________________________________________________________
## **Lista de participantes** <a name = "t1"></a>
* Jimena Alpiste Espinoza - 74297329
* Jossymar León Mallma - 
* Renato Cardoso Cardenas - 

## Introducción  <a name = "t2"></a>
[insertar parrafo de intro]

## **Objetivos del Laboratorio** <a name = "t3"></a>
* Adquirir señales biomédicas de ECG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales ECG del software OpenSignals (r)evolution
  
## **Materiales y equipos** <a name="t4"></a>
| Modelo          | Descripción                                    | Cantidad |
|:----------------:|-----------------------------------------------|----------|
| (R)EVOLUTION    | Kit de BITalino                                | 1        |
| -               | Laptop                                         | 1        |

<p align="center">
  <b>Materiales y equipos</b>
</p>

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


## ** Protocolo de conexión** <a name="t5"></a>
Se hizo uso del dispositivo Bitalino en conjunto con su sensor EMG de tres electrodos para la obtención de señales electromiográficas, como se evidencia en la imagen que se muestra posteriormente.

<p align="justify">
<p align="center"><img src="../Imágenes/BitTalino.jpg" width="400" height="266"></p>
</p>

El siguiente procedimiento consiste en colocar los electrodos EMG en el usuario de prueba. Para ello se utilizó la **Guía De BITalino en EMG** elaborada por **pluX** brindada por el laboratorio.


## **Resultados** <a name="t6"></a>
### **Visualización de señal eléctrica mediante video y OpenSignalsl** <a name="t7"></a>






### **Ploteo de la señal en Python** <a name="t8"></a>
- Código en Python:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# Cargar datos desde el archivo de texto según la ubicación del 
archivo = "Ubicación/del/archivo/Lectura_pulgar_supinación_EMG.txt"
def extraer_nombres_columnas(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            if linea.startswith("#"):
                matches = re.findall(r'column":\s*\[(.*?)\]', linea)
                if matches:
                    # Extraer la lista de nombres de columna de la línea
                    column_names = [name.strip().strip('"') for name in matches[0].split(',')]
                    return column_names,
                else:
                    continue


                    
#Me devuelve una tupla pues esta en "(...)"
column_name=extraer_nombres_columnas(archivo)

nombres_columnas=column_name[0]  # Imprime la lista: ['nSeq', 'I1', 'I2', 'O1', 'O2', 'A1']

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
Lectura_EMG = datos.iloc[:, 5]

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
- [Programa de ploteo (python)](https://github.com/renatog2500/inb_2024_gh12/blob/be701a0d1b2c92ef9167bfc775c26846401e695d/Software/Ploteo_de_datos_lab3.py)

## **Conclusiones** <a name="t10"></a>

//////////////////////

## **Bibliografía** <a name="t11"></a>



