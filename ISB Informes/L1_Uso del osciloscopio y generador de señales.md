# Informe Laboratorio 1

## Tabla de contenidos:
 __________________________________________________________________________________________________
- [Objetivos](#Objetivos)
- [Equipo Utilizado](#Equipo_utilizado)
- [Resultados](#Resultados)
- [Conclusiones](#Conclusiones)
__________________________________________________________________________________________________
## Objetivos:
- Adquirir señales conocidas como señal cuadrada, triangular, senoidal, rampa, etc.
- Entender los criterios de selección de la frecuencia de muestreo.
- Manipular y configurar adecuadamente una fuente de alimentación regulable; multímetro digital; Generador de señales y osciloscopio digital.

## Equipo_utilizado:
- Arduino Nano IoT 33
- Generador de Señales
- Osciloscopio
- Computadora con Arduino IDE y acceso a Arduino Cloud

## Resultados:
- Conexión Arduino nano 33 IoT y cable BNC :
  
*pones la pic *

Se conectó el condensador a las entradas A0 del Arduino y a su terminal de Ground.

- Código en Arduino IDE:
*pones la pic *

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




- Comparativa del Efecto del Condensador:

| Estado             | Imagen                           | Descripción                   |
|---------------------------------|---------------------------------|---------------------------------|
|Con condensador|------------------foto---------------|---------------------------------|
|Sin condensador|-----------------foto----------------|---------------------------------|


- Generador de Señales:

| Onda Sinusoidal           | Onda Cuadrada                           | Onda Triangular                   |
|---------------------------------|---------------------------------|---------------------------------|
|foto|------------------foto---------------|---------------------------------|


- Señal obtenida del Osciloscopio:

| Señal          | Imagen                           | Descripción                 |
|---------------------------------|---------------------------------|---------------------------------|
|Onda Sinusoidal|------------------foto---------------|---------------------------------|
|Onda Cuadrada|------------------foto---------------|---------------------------------|
|Onda Traingular|------------------foto---------------|---------------------------------|

- Señal obtenida del Arduino IDE:
  
| Señal          | Imagen                           | Descripción                 |
|---------------------------------|---------------------------------|---------------------------------|
|Onda Sinusoidal|------------------foto---------------|Con condensador|
|Onda Cuadrada|------------------foto---------------|Con condensador|
|Onda Traingular|------------------foto---------------|Con condensador|
|Onda Sinusoidal|------------------foto---------------|Sin condensador|
|Onda Cuadrada|------------------foto---------------|Sin condensador|
|Onda Traingular|------------------foto---------------|Sin condensador|

- Arduino Cloud:
  
Se presentaron problemas en el Arduino Cloud al momento de subir el código al Nano 33 IoT por lo cual no se pudo realizar una lectura con el entorno virtual.

## Conclusiones:
En este experimento, se logró exitosamente plotear señales en el Arduino IDE provenientes del generador de señales. La comparación con las gráficas obtenidas del osciloscopio permitió validar la precisión de las mediciones realizadas por el Arduino. Además, la capacidad de graficar en Arduino Cloud proporciona una alternativa conveniente para monitorear y analizar datos de manera remota, pero en esta oportunidad no se logró obtener una conexión. 
   
