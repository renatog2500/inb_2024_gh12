import numpy as np
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def line_length(signal, window_size):
    return np.sum(np.abs(np.diff(signal.reshape(-1, window_size))), axis=1)

def median_decay_memory_normalization(feature, window_size=118, lambda_decay=0.99):
    z = np.zeros_like(feature)
    N = np.zeros_like(feature)
    
    for k in range(len(feature)):
        if k < window_size:
            z[k] = np.median(feature[:k+1])
        else:
            z[k] = (1 - lambda_decay) * np.median(feature[k-window_size:k]) + lambda_decay * z[k-1]
        
        if z[k] != 0:
            N[k] = feature[k] / z[k]
        else:
            N[k] = feature[k]
    
    return N

def normalize_eeg(eeg_signal, fs, lowcut=1, highcut=30, window_size=1):
    # Aplicar filtro paso banda
    filtered_signal = butter_bandpass_filter(eeg_signal, lowcut, highcut, fs)
    
    # Calcular la característica de longitud de línea
    samples_per_window = int(window_size * fs)
    ll_feature = line_length(filtered_signal, samples_per_window)
    
    # Aplicar normalización
    normalized_feature = median_decay_memory_normalization(ll_feature)
    
    return normalized_feature

# Ejemplo de uso
if __name__ == "__main__":
    # Simulamos una señal EEG
    fs = 256  # Frecuencia de muestreo
    t = np.linspace(0, 10, fs*10)  # 10 segundos de señal
    eeg_signal = np.sin(2*np.pi*10*t) + 0.5*np.random.randn(len(t))
    
    # Normalizamos la señal
    normalized_signal = normalize_eeg(eeg_signal, fs)
    
    print("Forma de la señal normalizada:", normalized_signal.shape)
    print("Primeros 5 valores normalizados:", normalized_signal[:5])
