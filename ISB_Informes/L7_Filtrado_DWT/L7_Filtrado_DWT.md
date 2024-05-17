# Laboratorio N°7 - Filtrado de las señales DWT

## Tabla de contenidos:
 __________________________________________________________________________________________________
1. [Lista de participantes](#t1)
2. [Introducción](#t2)
3. [Objetivos del laboratorio](#t3)
4. [Metodología](#t4)
6. [Resultados](#t5)\
   5.1 [Ejercicio ECG](#t6)\
   5.2 [Ejercicio EMG ](#t7)\
   5.3 [Ejercicio EEG](#t8)
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

**Filtros Digitales**


<div align="center">
    <img src="Imagenes_L6/Filtro digital intro.png" alt="wCF14V" width="400">
    <p><b>Figura 1. Representación de un filtro digital</b> - Extraído de [1]</p>
</div>


## **Objetivos  Laboratorio** <a name = "t3"></a>
* Comprender los principios básicos de filtros digitales, en particular, los relacionados con los filtros de respuesta infinita al impulso (IRR) y los de respuesta finita al impulso (FIR).
* Filtrar las señales ECG, EMG y EEG para la eliminación de ruidos y artefactos
* Analizar las señales obtenidas y extraer características de interés de cada una. 
  
## Metodología <a name="t4"></a>
En este laboratorio, nos enfocamos en el diseño e implementación de filtros digitales FIR e IIR con el objetivo de atenuar las frecuencias altas indeseadas, originadas por el ruido presente en las señales ECG, EMG y EEG adquiridas previamente utilizando el Kit BITalino. 

**Materiales y Equipo Utilizado**
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

## **Procedimiento**

***Uso de filtros Wavelets***

**Uso en señal ECG**

En un estudio realizado por Kania et al. [], se investigó la aplicación del filtrado wavelet para reducir el ruido en señales EKG de alta resolución. Los autores evaluaron diferentes funciones wavelet madre y niveles de descomposición para determinar los parámetros óptimos que minimizaran el error cuadrático medio (MSE) entre la señal original y la señal filtrada, preservando al mismo tiempo las características morfológicas del EKG.

Los resultados de Kania et al. [] mostraron que las funciones wavelet db1 (Daubechies de primer orden) con niveles de descomposición del 4 al 6, sym3 (Symlet de tercer orden) con nivel 4, y sym8 (Symlet de octavo orden) con nivel 4, proporcionaron el mejor desempeño en términos de reducción de ruido y preservación de la morfología del EKG. Además, se destacó la ventaja del filtrado wavelet sobre técnicas convencionales como el promediado de latidos, especialmente en casos de arritmia donde el promediado puede distorsionar la señal.

*Parámetros*

(ACA VA UN CUADRO CON LOS PARÁMETROS UTILIZADOS AL FINAL)

*Señal pre y post procesada*

(IMAGEN DE LA SEÑAL ANTES Y DESPUÉS DEL FILTRADO)


**Uso en señal EMG:**

En un estudio exhaustivo realizado por Phinyomark et al. [], se investigó el desempeño de diferentes funciones wavelet madre y niveles de descomposición para el filtrado de ruido en señales EMG, con el objetivo de identificar los parámetros óptimos que minimizaran el error cuadrático medio (MSE) entre la señal original y la señal filtrada. Los autores evaluaron un total de 53 funciones wavelet, incluyendo las familias Daubechies, Symlet, Coiflet, BiorSplines y ReverseBior, así como la wavelet Discreta de Meyer.

Los resultados de Phinyomark et al. [] revelaron que las funciones wavelet db1 (Daubechies de primer orden), bior1.1 (BiorSplines de primer orden) y rbio1.1 (ReverseBior de primer orden) proporcionaron el mejor desempeño en términos de reducción de ruido, con el mínimo MSE. Además, se encontró que el nivel de descomposición óptimo para el filtrado wavelet de señales EMG era el nivel 4. Los autores también destacaron que wavelets con forma simple y baja frecuencia eran más adecuadas para las características morfológicas de las señales EMG.

*Parámetros*

(ACA VA UN CUADRO CON LOS PARÁMETROS UTILIZADOS AL FINAL)

*Señal pre y post procesada*

(IMAGEN DE LA SEÑAL ANTES Y DESPUÉS DEL FILTRADO)


**Uso en señal EEG**

Justificación de parámetos 

*Parámetros*

(ACA VA UN CUADRO CON LOS PARÁMETROS UTILIZADOS AL FINAL)

*Señal pre y post procesada*

(IMAGEN DE LA SEÑAL ANTES Y DESPUÉS DEL FILTRADO)

 
**CÓDIGOS UTILIZADOS**
--------------------------------------------------------------------------------------------------------------
**Código de ploteo para EKG pre y post filtrado:**
```python
import pywt
import numpy as np
import matplotlib.pyplot as plt

def wavelet_denoising(signal, wavelet, level, threshold_method='soft'):
    # Descomposición wavelet
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    
    # Umbralización de coeficientes de detalle
    threshold = np.sqrt(2 * np.log(len(signal)))
    for i in range(1, len(coeffs)):
        coeffs[i] = pywt.threshold(coeffs[i], threshold * np.std(coeffs[i]), mode=threshold_method)
    
    # Reconstrucción de la señal
    denoised_signal = pywt.waverec(coeffs, wavelet)
    
    return denoised_signal

# Cargar señal EKG (reemplaza esto con tu propio código de carga de datos)
ecg_signal = np.loadtxt('ecg_data.txt')

# Parámetros del filtro wavelet
wavelet_type = 'db4'
decomposition_level = 4

# Aplicar filtrado wavelet
denoised_ecg = wavelet_denoising(ecg_signal, wavelet_type, decomposition_level)

# Graficar resultados
plt.figure(figsize=(10, 4))
plt.plot(ecg_signal, label='Señal EKG original')
plt.plot(denoised_ecg, label='Señal EKG filtrada')
plt.legend()
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.title('Filtrado Wavelet de Señal EKG')
plt.show()

```


**Código de ploteo para EMG pre y post filtrado:**
```python
import pywt
import numpy as np
import matplotlib.pyplot as plt

def wavelet_denoising_emg(signal, wavelet, level, threshold_method='universal'):
    # Descomposición wavelet
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    
    # Estimación del umbral usando el método universal
    threshold = np.sqrt(2 * np.log(len(signal)))
    
    # Umbralización suave de los coeficientes de detalle
    for i in range(1, len(coeffs)):
        coeffs[i] = pywt.threshold(coeffs[i], threshold * np.median(np.abs(coeffs[i])) / 0.6745, mode='soft')
    
    # Reconstrucción de la señal
    denoised_signal = pywt.waverec(coeffs, wavelet)
    
    return denoised_signal

# Cargar señal EMG (reemplaza esto con tu propio código de carga de datos)
emg_signal = np.loadtxt('emg_data.txt')

# Parámetros del filtro wavelet óptimos según Phinyomark et al.
wavelet_type = 'db1'  # También puedes probar 'bior1.1' o 'rbio1.1'
decomposition_level = 4

# Aplicar filtrado wavelet
denoised_emg = wavelet_denoising_emg(emg_signal, wavelet_type, decomposition_level)

# Calcular MSE entre señal original y filtrada
mse = np.mean((emg_signal - denoised_emg) ** 2)
print(f"MSE: {mse:.4f}")

# Graficar resultados
plt.figure(figsize=(10, 4))
plt.plot(emg_signal, label='Señal EMG original')
plt.plot(denoised_emg, label='Señal EMG filtrada')
plt.legend()
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.title(f'Filtrado Wavelet de Señal EMG usando {wavelet_type}')
plt.show()

```
## Resultados   <a name="t5"></a>

### **Ejercicio ECG** <a name="t6"></a>
| Campo | Señal Cruda | Filtro IIR | Filtro FIR |
|-----------|-----------|-----------|-----------|
| Basal   | <img src="Imagenes_L6/Imagenes_ECG/Basal_ECG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_ECG/basal_ECG_butter.png" alt="Electrodos de guía"  > | <img src="Imagenes_L6/Imagenes_ECG/basal_ECG_hanni.png" alt="Electrodos de guía" >|
| Respiración   | <img src="Imagenes_L6/Imagenes_ECG/in_ex_ECG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_ECG/in_ex_ECG_butt.png" alt="Electrodos de guía" >| <img src="Imagenes_L6/Imagenes_ECG/in_ex_ECG_hanni.png" alt="Electrodos de guía"> |
| Post Ejercicios   | <img src="Imagenes_L6/Imagenes_ECG/post_ECG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_ECG/post_ECG_butt.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_ECG/post_ECG_hann.png" alt="Electrodos de guía"> |

<p align="center">
  <b>Tabla 2. Resumen de la señal filtrada con filtros FIR e IIR para la data ECG</b>
</p>


### **Ejercicio EMG** <a name="t7"></a>
| Campo | Señal Cruda | Filtro IIR | Filtro FIR |
|-----------|-----------|-----------|-----------|
| Bicep Braquial   | <img src="Imagenes_L6/Imagenes_EMG/bicep_EMG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_EMG/bicep_EMG_butt.png" alt="Electrodos de guía"  > | <img src="Imagenes_L6/Imagenes_EMG/bicep_EMG_black.png" alt="Electrodos de guía" >|
| Antebrazo supinación  | <img src="Imagenes_L6/Imagenes_EMG/antebrazo_EMG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_EMG/antebrazo_EMG_butt.png" alt="Electrodos de guía" >| <img src="Imagenes_L6/Imagenes_EMG/antebrazo_EMG_black.png" alt="Electrodos de guía"> |
| Pulgar en supinación   | <img src="Imagenes_L6/Imagenes_EMG/pulgar_EMG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_EMG/pulgar_EMG_butt.png" alt="Electrodos de guía">  | <img src="Imagenes_L6/Imagenes_EMG/pulgar_EMG_black.png" alt="Electrodos de guía"> |

<p align="center">
  <b>Tabla 3. Resumen de la señal filtrada con filtros FIR e IIR para la data EMG</b>
</p>


### **Ejercicio EEG** <a name="t8"></a>
| Campo | BASAL | OJOS CERRADOS - ABIERTOS | PREGUNTAS COMPLEJAS |
|-----------|-----------|-----------|-----------|
| Señal Cruda ---------------Filtro IIR --------------Filtro FIR ondas delta ------Filtro FIR ondas tetha ------Filtro FIR ondas alfa------ Filtro FIR ondas beta ------Filtro FIR ondas gamma | <img src="Imagenes_L6/Imagenes_EEG/Fase_referencia_30seg_filtrada.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_EEG/Prueba_ojos_abiertos_cerrado_5s_filtrada.png" alt="Electrodos de guía" >   | <img src="Imagenes_L6/Imagenes_EEG/Prueba_Preguntas_complejas_filtrada.png" alt="Electrodos de guía" > |

<p align="center">
  <b>Tabla 4. Resumen de la señal filtrada con filtros FIR e IIR para la data EEG</b>
</p>



## Discusión <a name="t9"></a>


### **ECG** <a name="t10"></a>
Basal: Antes del filtrado, la señal de EKG contiene ruido de baja frecuencia, como la deriva de la línea base, y ruido de alta frecuencia, como la interferencia electromagnética. Estos ruidos dificultan la identificación de las ondas características del EKG, como las ondas P, QRS y T.

IIR: Después del filtrado con un filtro IIR, el ruido de baja y alta frecuencia se atenúa, lo que resulta en una señal más limpia. Las ondas P, QRS y T son más prominentes y fáciles de identificar. Sin embargo,se observa una ligera distorsión de la forma de onda debido a la fase no lineal del filtro IIR.

FIR:Con un filtro FIR, se ve una atenuación similar del ruido de baja y alta frecuencia. La señal resultante también es más limpia, con las ondas P, QRS y T claramente visibles. A diferencia del filtro IIR, el filtro FIR no introduce distorsión de fase, por lo que la forma de onda se preserva mejor.


### **EMG** <a name="t11"></a>

Basal: La señal EMG contiene ruido de baja frecuencia que pueden ser debidos a artefactos en movimiento y ruido de alta frecuencia debido a interferencias electromagnéticas. Este ruido puede ocultar la información relevante relacionada con la actividad muscular. 

IIR: Después del filtrado con un filtro IIR, se observa una reducción del ruido de baja y alta frecuencia, lo que resulta en una señal más limpia. Las componentes espectrales características del EMG, que contienen información sobre la frecuencia y amplitud de la actividad muscular, son más evidentes. 

FIR: Después del filtrado con un filtro FIR, se observa atenuación similar del ruido de baja y alta frecuencia. La señal resultante también es más limpia, con las componentes espectrales del EMG claramente visibles.

### **EEG** <a name="t12"></a>

Basal: Observamos una gran cantidad de ruido en las señales al momento de plotear cada una. Lo cual dificulta su lectura de informaciòn. 

IIR: La señal EEG, después de pasar por un filtro Butterworth, nos permite reconocer las magnitudes de las oscilaciones en distintos rangos de frecuencia, tales como delta, theta, alpha, beta y gamma. Este diagrama nos facilita la medición de la amplitud en microvoltios (uV) o en unidades relativas.

FIR: Cuando aplicamos la ventana Hamming en el análisis de una señal EEG, estamos seleccionando una ventana específica para la respuesta de frecuencia. Esto influye en la percepción y el análisis de las oscilaciones en la señal EEG. Esperaríamos poder distinguir las ondas alfa, delta, beta y gamma; sin embargo, en algunos casos, podríamos notar que la calidad de la señal no es óptima y la identificación de la banda de frecuencia con mayor amplitud en momentos específicos no es clara. Esto resalta la importancia de comprender las diferencias entre las ventanas Hamming y Hann, y cómo afectan el procesamiento de la señal.


## ** Bibliografía** : <a name="t13"></a>


[1] E. C. Ifeachor and B. W. Jervis, "Digital signal processing: a practical approach," Pearson Education, pp. 367-379, 2002.

[2] M. Parker, “Finite Impulse Response (FIR) Filters,” Elsevier eBooks, pp. 41–57, Jan. 2017, doi: https://doi.org/10.1016/b978-0-12-811453-7.00005-6.

[3] M. Parker, “Infinite Impulse Response (IIR) Filters,” Elsevier eBooks, pp. 75–82, Jan. 2017, doi: https://doi.org/10.1016/b978-0-12-811453-7.00008-1.

[4] P. Ramesh Babu, "Digital Signal Processing", 4th ed. Chennai: Scitech Publication (India) Pvt. Ltd, 2008.

[5] Renatog2500, "L4_Lectura_de_ECG", GitHub, 2024. [Online]. Available: https://github.com/renatog2500/inb_2024_gh12/blob/main/ISB_Informes/L4_Lectura_de_ECG/L4_Lectura_de_ECG.md. [Accessed: May 05, 2024].

[6] N. Das y M. Chakraborty, "Performance Analysis of FIR and IIR Filters for ECG Signal Denoising based on SNR," en 2017 IEEE International Conference on Intelligent Techniques in Control, Optimization and Signal Processing (INCOS), 2017, pp. 1-6, doi: 10.1109/ITCOSP.2017.8303099.  https://sci-hub.se/https://ieeexplore.ieee.org/abstract/document/8234487 

[7] BITalino, “Electrocardiography (ECG) Sensor Data Sheet”, Lisboa, DataSheet, 2020. https://www.bitalino.com/storage/uploads/media/revolution-ecg-sensor-datasheet-revb-1.pdf 

[8] T. Roland, S. Amsuess, M. Russold y W. Baumgartner, “Ultra-Low-Power Digital Filtering for Insulated EMG Sensing”, Sensors, vol. 19, n.º 4, p. 959, febrero de 2019. Accedido el 5 de mayo de 2024. [En línea]. Disponible: https://doi.org/10.3390/s19040959 

[9] S. Tiwari, S. Goel, y A. Bhardwaj, "Classification of imagined speech of vowels from EEG signals using multi-headed CNNs feature fusion network", Digital Signal Processing, vol. 148, p. 104447, 2024, doi: 10.1016/j.dsp.2024.104447. https://www.sciencedirect.com/science/article/pii/S1051200424000721 

[10] J. G. Proakis y D. G. Manolakis, "Digital Signal Processing: Principles, Algorithms, and Applications", 4th ed., Prentice-Hall, 2007.https://www.academia.edu/75221190/Digital_signal_processing_principles_algorithms_and_applications?auto=download 









