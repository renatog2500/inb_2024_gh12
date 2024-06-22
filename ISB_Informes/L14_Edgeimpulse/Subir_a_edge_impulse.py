import requests
import os
import pandas as pd
import numpy as np

api_key = 'ei_4aefce2f31d32bc9d81c758dfacdc12c8a47dfa19a1c99aad8046b23eac06940'
# Ruta del archivo CSV
file_path = 'C:/Users/Jossymar/Desktop/Introduccion a señales/github/inb_2024_gh12/lectura_eeg2.csv'

# Leer el archivo CSV como un DataFrame
dataframe = pd.read_csv(file_path)

# Suponiendo que el archivo tiene una columna de tiempo en segundos llamada 'time'
# Si no, ajusta el código según tus datos
sampling_rate = 1000  # Hz, ajustar según la frecuencia de muestreo de tus datos
window_size = 3 * sampling_rate  # 3 segundos de datos


# Dividir el DataFrame en ventanas de 3 segundos
num_windows = len(dataframe) // window_size

for i in range(num_windows):
    window_df = dataframe.iloc[i * window_size:(i + 1) * window_size]
    
    # Guardar la ventana como un archivo CSV temporal
    temp_csv_path = f'eeg2_window_{i}.csv'
    window_df.to_csv(temp_csv_path, index=False)
    
    # Etiqueta para la subida
    label = 'EEG_2'

    # Subir el archivo CSV temporal a Edge Impulse
    with open(temp_csv_path, 'rb') as file:
        res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                            headers={
                                'x-label': label,
                                'x-api-key': api_key,
                            },
                            files={'data': (os.path.basename(temp_csv_path), file, 'application/csv')}
                            )
    
    if res.status_code == 200:
        print(f'Successfully uploaded {temp_csv_path} to Edge Impulse\n', res.status_code, res.content)
    else:
        print(f'Failed to upload {temp_csv_path} to Edge Impulse\n', res.status_code, res.content)
    
    # Eliminar el archivo CSV temporal después de la subida
    os.remove(temp_csv_path)

