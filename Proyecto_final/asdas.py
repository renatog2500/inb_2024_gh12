import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('Medición_no_ergo/Normalized_Signal_no_ergo_Combinado.csv', header=None)  # Asegúrate de ajustar la ruta del archivo

# Asumimos que los datos están en la primera columna
data = df.iloc[:, 0]

# Invertir los valores de la columna
data_invertida = data.iloc[::-1].reset_index(drop=True)

# Asignar los datos invertidos de vuelta al DataFrame original
df.iloc[:, 0] = data_invertida

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv('ruta_del_archivo_invertido.csv', index=False, header=None)  # Ajusta la ruta como sea necesario
