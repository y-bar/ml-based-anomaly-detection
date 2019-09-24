import numpy as np

np.random.seed(666)


def _make_data():
    signal = np.concatenate([np.random.normal(0.7, 0.05, 10), np.random.normal(1.5, 0.05, 10)])
    return signal


data = _make_data()
score_normal = np.array(
    [
        0.0,
        -0.42754579,
        -0.55870549,
        -0.56280065,
        -0.23401658,
        -0.24234956,
        -0.17393121,
        -0.47974704,
        0.03631342,
        1.89257906,
        1.10706606,
        -0.42807027,
        -0.38545706,
        -0.79601457,
        -0.52192534,
        -0.05124334,
        -0.34376586,
        0.37283275,
        -0.7470411,
        -0.17238451,
    ]
)
