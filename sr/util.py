import numpy as np

CUTOFF = 1e-8


def average_filter(values, n=3):

    cumsum = np.cumsum(values, dtype=float)
    cumsum[n:] = cumsum[n:] - cumsum[:-n]
    cumsum[n:] = cumsum[n:] / n

    for i in range(1, n):
        cumsum[i] /= (i + 1)

    return cumsum


def extrapolate_series(values):
    """
    Extrapolates the next value by sum up the slope of the last value with previous values.
    :param values: a list or numpy array of time-series
    :return: the next value of time-series
    """

    last_value = values[-1]
    n = len(values)
    slopes = [(last_value - v) / (n - 1 - i) for i, v in enumerate(values[:-1])]

    return values[1] + sum(slopes)


def marge_series(values, extend_num=5, forward=5):

    extension = [extrapolate_series(values[-forward - 2:-1])] * extend_num

    if isinstance(values, list):
        marge_values = values + extension
    else:
        marge_values = np.append(values, extension)
    return marge_values
