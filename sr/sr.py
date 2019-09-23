import numpy as np
from sr.util import CUTOFF, average_filter, marge_series


class SpectralResidual(object):

    def __init__(self, amp_window_size, series_window_size, score_window_size):
        self.amp_window_size = amp_window_size
        self.series_window_size = series_window_size
        self.score_window_size = score_window_size

    def transform_spectral_residual(self, values):
        """
        Transform a time-series into spectral residual.
        :param values: a list or numpy array of float values.
        :param eps: cut-off of time-series in fourier space. in default, it set to be 10e-8.
        :param n: sliding window size of amplitude. in default, it set to be n = 3.
        :return: spectral residual
        """

        spec = np.fft.fft(values)
        amp = np.abs(spec)

        # cut-off
        eps_index = np.where(amp <= CUTOFF)[0]
        amp[eps_index] = CUTOFF

        # log amplitude
        log_amp = np.log(amp)
        log_amp[eps_index] = 0
        filtered_log_amp = average_filter(log_amp, self.amp_window_size)

        spec.real = spec.real * np.exp(-filtered_log_amp)
        spec.imag = spec.imag * np.exp(-filtered_log_amp)
        spec.real[eps_index] = 0
        spec.imag[eps_index] = 0

        silency_map = np.fft.ifft(spec)
        spectral_residual = np.abs(silency_map)
        return spectral_residual

    def generate_anomaly_score(self, values):

        extended_series = marge_series(values, self.series_window_size, self.series_window_size)
        amp = self.transform_spectral_residual(extended_series)[:len(values)]
        ave_amp = average_filter(amp, self.score_window_size)

        score = (amp - ave_amp) / ave_amp
        return score

