import pandas as pd

# Lista de nombres de archivo
archivos = [
    'Normalized_renato1.csv',
    'Normalized_renato2.csv',
    'Normalized_renato3.csv',
]

# Lista para almacenar todos los datos
datos_totales = []

# Leer cada archivo y agregar los datos a la lista
for archivo in archivos:
    df_actual = pd.read_csv(archivo, header=None)  # Asumiendo que no hay encabezado
    datos_totales.extend(df_actual.iloc[:, 1].tolist())  # Asume que los datos están en la primera columna

# Convertir la lista en un DataFrame
df_total = pd.DataFrame(datos_totales)

# Guardar el DataFrame combinado en un nuevo archivo CSV
df_total.to_csv('Normalized_Signal_no_ergo_Combinado.csv', index=False, header=None)
