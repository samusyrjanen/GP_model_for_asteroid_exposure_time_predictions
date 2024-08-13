import numpy as np
from scipy.interpolate import interp1d
from scipy.ndimage import gaussian_filter1d

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def root_mean_squared_error(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred) ** 2))

def denoise_and_norm(data: np.ndarray, wavelength: np.ndarray, denoising: bool, normalising: bool, sigma_nm: float = 7,
                     normalised_at_wvl: float = 550) -> np.ndarray:
    if denoising:
        if data.ndim == 1:
            data = np.reshape(data, (1, len(data)))

        nm_to_px = 1 / (wavelength[1] - wavelength[0])
        correction = gaussian_filter1d(np.ones(len(wavelength)), sigma=sigma_nm * nm_to_px, mode='constant')
        data_denoised = gaussian_filter1d(data, sigma=sigma_nm * nm_to_px, mode='constant') / correction
    else:
        data_denoised = data

    # Normalised reflectance
    if normalising:
        fun = interp1d(wavelength, data_denoised, kind='cubic')  # v_final differs from v
        v_norm = np.reshape(fun(normalised_at_wvl), (len(data_denoised), 1))
    else:
        v_norm = 1

    return data_denoised / v_norm
