import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def rms(values):
    """Calcula el valor RMS (Root Mean Square) de un array de valores."""
    return np.sqrt(np.mean(np.square(values)))

def line(x, a, b):
    """Función lineal a*x + b para el ajuste lineal."""
    return a * x + b

# Cargar los datos del CSV
df = pd.read_csv('Medición_no_ergo/Normalized_Signal_no_ergo_Combinado.csv', header=None)
data = df.iloc[:, 0].values  # Asumimos que los datos están en la primera columna

# Parámetros de ventaneo
window_size = 50*10  # Define el tamaño de cada ventana
step_size = 10    # Define el paso entre cada ventana

# Calculo de RMS por ventana
rms_values = []
num_windows = (len(data) - window_size) // step_size + 1

for i in range(num_windows):
    start_index = i * step_size
    end_index = start_index + window_size
    window = data[start_index:end_index]
    rms_value = rms(window)
    rms_values.append(rms_value)

# Graficar los valores RMS
plt.figure(figsize=(10, 5))
plt.plot(rms_values, color='b', label='RMS por ventana')
plt.title('Valor RMS por ventana')
plt.xlabel('Número de ventana')
plt.ylabel('RMS')
plt.grid(True)
plt.legend()
plt.show()

# Ajuste lineal de los datos RMS
x_data = np.arange(len(rms_values))
params, params_covariance = curve_fit(line, x_data, rms_values)

# Graficar el ajuste lineal
plt.figure(figsize=(10, 5))
plt.plot(rms_values, marker='o', linestyle='-', color='b', label='RMS por ventana')
plt.plot(x_data, line(x_data, *params), label='Ajuste lineal: y = {:.2f}x + {:.2f}'.format(params[0], params[1]), color='red')
plt.title('Ajuste Lineal sobre RMS')
plt.xlabel('Número de ventana')
plt.ylabel('RMS')
plt.legend()
plt.grid(True)
plt.show()

print("Parámetros del ajuste lineal: pendiente = {:.6f}, intercepto = {:.2f}".format(params[0], params[1]))
