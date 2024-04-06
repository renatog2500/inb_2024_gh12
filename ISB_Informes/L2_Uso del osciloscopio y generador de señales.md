# Laboratorio N°2 - Adquisión de señales y graficación en Arduino

## Tabla de contenidos:
 __________________________________________________________________________________________________
- [Objetivos](#Objetivos)
- [Equipo Utilizado](#Equipo_utilizado)
- [Resultados](#Resultados)
- [Discusión](#Discusión)
- [Conclusiones](#Conclusiones)
- [Bibliografía](#Bibliografía)
__________________________________________________________________________________________________
## Objetivos:
- Adquirir señales conocidas como señal cuadrada, triangular, senoidal, rampa, etc.
- Entender los criterios de selección de la frecuencia de muestreo.
- Manipular y configurar adecuadamente una fuente de alimentación regulable; multímetro digital; Generador de señales y osciloscopio digital.

## Equipo_utilizado:
| Modelo          | Descripción                                    | Cantidad |
|-----------------|-----------------------------------------------|----------|
| AFG1022         | Generador de señales                          | 1        |
| TBS 1000C Series| Osciloscopio digital                          | 1        |
| -               | Cable BNC Male-Male                           | 1        |
| -               | Punta de osciloscopio con conector BNC (Male)| 1        |
| -               | Par de cables Male-Male                       | 1        |
| SAMD            | Arduino 33 IoT                                | 1        |


## Resultados:
- Conexión Arduino nano 33 IoT y cable BNC :

<p align="center">
  <img src="../Imágenes/Circuito.png" alt="Figura 1. Conexiones del Arduino">
</p>
<p align="center">Figura 1. Conexiones del Arduino</p>

Se estableció la conexión del Arduino Nano 33 IoT en el protoboard, junto con un condensador, para configurar un filtro RC. Este filtro se empleó en conjunto con un cable BNC para analizar la señal sinusoidal proveniente del generador de señales

- Código en Arduino IDE:
```C++
unsigned long lastMsg = 0;
float F = 3;          // Frecuencia de la señal en Hz
double Fs = 10 * F;      // Frecuencia de muestreo en Hz (10 veces la frecuencia de la señal)
double Ts_ms = (1 / Fs) * 1000;  // Período de muestreo en milisegundos (recíproco de la frecuencia de muestreo)

void setup() {
  Serial.begin(9600);
  while (!Serial);  // Esperar hasta que se inicie la comunicación serial
}

void loop() {
  unsigned long now = millis();  

 
  if (now - lastMsg > Ts_ms) {
    lastMsg = now;  

    double signal_analogica = analogRead(A0);  
    Serial.println(signal_analogica);                                 
  }
}
```
<p align="center">Figura 2. Código para el ploteo de las señales</p>


- Generador de Señales:

Se configuro el generador de señales para proporcionar una señal sinusoidal de 2 Hz de frecuencia, con 3.3V de amplitud y 0V de offset


| Onda Sinusoidal          | Onda Cuadrada                                    | Onda Triangular |
|-----------------|-----------------------------------------------|----------|
| ![](../Imágenes/Generador_Onda_Sinusoidal.png)   | ![](../Imágenes/Generador_Onda_cuadrada.png)                        | ![](../Imágenes/Generador_Onda_Triangular.png)      |

<p align="center">Tabla 1. Configuración del generador de ondas para el ploteo de señales</p>

- Señal obtenida del Osciloscopio:

| Señal          | Imagen                                                                               | Descripción                                                                                      |
|----------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Onda Sinusoidal | ![](../Imágenes/Osciloscopio_Onda_sinusoidal.png)           | Para esta onda tuvimos que configurarla con una frecuencia de 2Hz, una amplitud de 3.3v. Donde se puede apreciar una atenuación de aproximadamente 50 mV y una frecuencia detectada de 1.9 Hz |
| Onda Cuadrada  | ![](../Imágenes/Osciloscopio_Onda_cuadrada.png)              | Para esta onda tuvimos que configurarla con una frecuencia de 2Hz, una amplitud de 3.3v. Del mismo modo, se apreció una atenuación junto a ruido en las zonas altas de la onda. |
| Onda Triangular| ![](../Imágenes/Osciloscopio_Onda_triangular.png)            | Para esta onda tuvimos que configurarla con una frecuencia de 2Hz, una amplitud de 3.3v. En esta señal, se observó la variación de la amplitud y frecuencia se ven afectados, debido al ruido que se puede apreciar en la imagen. |

<p align="center">Tabla 2. Señales en el osciloscopio</p>

- Señal obtenida del Arduino IDE:

| Señal          | Con Condensador                           | Sin Condensador                |
|---------------------------------|---------------------------------|---------------------------------|
|Onda Sinusoidal|![Onda Sinusoidal](../Imágenes/Sinusoidal_cap.png)|![Onda Sinusoidal](../Imágenes/Sinusoidal.png)|
|Onda Cuadrada|![Onda Cuadrada](../Imágenes/Cuadrada_cap.png)|![Onda Cuadrada](../Imágenes/Cuadrada.png)|
|Onda Traingular|![Onda Traingular](../Imágenes/Triangulo_cap.png)|![Onda Traingular](../Imágenes/Triangulo.png)|
<p align="center">Tabla 3. Efecto del Condensador en el Arduino IDE</p>

En el circuito, el condensador actúa como un filtro pasa alta, permitiendo el paso de frecuencias más altas mientras atenúa las frecuencias más bajas. Esto afecta el proceso de detección y registro de la señal por parte del Arduino proveniente del generador. 

- Arduino Cloud:
  
Se presentaron problemas en el Arduino Cloud al momento de subir el código al Nano 33 IoT por lo cual no se pudo realizar una lectura con el entorno virtual.


## Discusión:
Fuentes de Error: 
Hay algunas razones posibles por las que ves picos extraños e irregulares la señal cuando se agrega un capacitor de 470uF a tu circuito de filtro RC. A continuación se muestran algunas posibles causas:

1.  Diseño de filtro incorrecto: El circuito de filtro RC está diseñado para suavizar la señal de salida de su Arduino Nano reduciendo los componentes de alta frecuencia de la señal. Si los valores de la resistencia y el condensador no se eligen correctamente, es posible que el filtro no funcione como se esperaba y que vea picos extraños en la señal de salida [1].
2.   Ruido: Es posible que el condensador esté captando ruido del entorno o de la fuente de alimentación. Este ruido puede ser amplificado por el circuito de filtro RC y aparecer como picos en la señal de salida [2].
3.   Fugas de condensadores: Los condensadores pueden perder carga con el tiempo, especialmente si son viejos o han sido sometidos a altas temperaturas. Esta fuga puede hacer que el capacitor se descargue lentamente, lo que resulta en una caída de voltaje en el capacitor y provoca picos en la señal de salida [3].
4.   Fuente de alimentación insuficiente: Si la fuente de alimentación no puede proporcionar suficiente corriente al circuito, el voltaje puede caer bajo carga, lo que provoca que el condensador se descargue y provoque picos en la señal de salida.[4]





## Conclusiones:
En este experimento, se logró exitosamente plotear señales en el Arduino IDE provenientes del generador de señales. La comparación con las gráficas obtenidas del osciloscopio permitió validar la precisión de las mediciones realizadas por el Arduino. Además, la capacidad de graficar en Arduino Cloud proporciona una alternativa conveniente para monitorear y analizar datos de manera remota, pero en esta oportunidad no se logró obtener una conexión. 

## Bibliografía:
[1] “La respuesta natural de un circuito RC (artículo) | Khan Academy,” Khan Academy, 2023. https://es.khanacademy.org/science/electrical-engineering/ee-circuit-analysis-topic/ee-natural-and-forced-response/a/ee-rc-natural-response (accessed Apr. 06, 2024).

[2] N. Arias-Prado, E. Escamilla-Hernández, M. Nakano-Miyatake, and H. Perez-Meana, “Desarrollo de un sistema para cancelación activa de ruido,” Pädi Boletín Científico de Ciencias Básicas e Ingenierías del ICBI, vol. 10, no. Especial4, pp. 173–180, Oct. 2022, doi: https://doi.org/10.29057/icbi.v10iEspecial4.9138.

[3] I. S. Ike, I. Sigalas, and S. Iyuke, “Understanding performance limitation and suppression of leakage current or self-discharge in electrochemical capacitors: a review,” Physical Chemistry Chemical Physics, vol. 18, no. 2, pp. 661–680, Jan. 2016, doi: https://doi.org/10.1039/c5cp05459a.

[4] M. Mauerer, A. Tuysuz, and J. W. Kolar, “Voltage/current measurement performance and power supply rejection in all-digital Class-D power amplifiers,” Oct. 2016, doi: https://doi.org/10.1109/iecon.2016.7793041.


