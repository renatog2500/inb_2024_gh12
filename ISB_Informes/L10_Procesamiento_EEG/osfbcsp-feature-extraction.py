import numpy as np
from scipy.signal import butter, filtfilt
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from mne.decoding import CSP

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

def apply_csp(X, y, n_components=4):
    csp = CSP(n_components=n_components, reg=None, log=True, norm_trace=False)
    return csp.fit_transform(X, y), csp

def mutual_information(X, y):
    # Simplified mutual information calculation
    return np.abs(np.corrcoef(X.T, y)[0, -1])

def osfbcsp_feature_extraction(X, y, fs, n_bands=4, band_width=4, overlap=2, n_csp_components=4):
    n_channels, n_samples, n_trials = X.shape
    
    # Define frequency bands
    freq_bands = [(6 + i*2, 6 + i*2 + band_width) for i in range(n_bands)]
    
    # Apply bandpass filtering
    X_filtered = np.zeros((n_bands, n_channels, n_samples, n_trials))
    for i, (low, high) in enumerate(freq_bands):
        X_filtered[i] = butter_bandpass_filter(X, low, high, fs)
    
    # Apply CSP to each band
    csp_features = []
    csp_filters = []
    for i in range(n_bands):
        X_band = X_filtered[i].reshape(n_channels, -1).T
        csp_feature, csp_filter = apply_csp(X_band, y, n_components=n_csp_components)
        csp_features.append(csp_feature)
        csp_filters.append(csp_filter)
    
    # Feature selection using mutual information
    mi_scores = [mutual_information(feat, y) for feat in csp_features]
    selected_features = np.concatenate([csp_features[i] for i in np.argsort(mi_scores)[-2:]], axis=1)
    
    # Apply LDA for dimensionality reduction
    lda = LDA(n_components=2)
    final_features = lda.fit_transform(selected_features, y)
    
    return final_features, csp_filters, lda

# Example usage
if __name__ == "__main__":
    # Simulated EEG data
    n_channels, n_samples, n_trials = 22, 1000, 100
    X = np.random.randn(n_channels, n_samples, n_trials)
    y = np.random.randint(0, 2, n_trials)
    fs = 250  # Sampling frequency

    features, csp_filters, lda_model = osfbcsp_feature_extraction(X, y, fs)
    print("Extracted features shape:", features.shape)
