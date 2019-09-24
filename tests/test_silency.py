import pytest

from sranodec.silency import Silency
from tests.mock.srdata import data, score_normal

spec = Silency(amp_window_size=3, series_window_size=3, score_window_size=5)


@pytest.mark.parametrize(["values", "expected"], [(data, score_normal)])
def test_generate_anomaly_score(values, expected):

    actual = spec.generate_anomaly_score(values)
    for ac, sc in zip(actual, expected):
        assert pytest.approx(ac, abs=0.0000001) == sc
