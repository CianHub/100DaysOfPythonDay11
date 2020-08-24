
import pytest
from unittest.mock import patch
from datetime import datetime

from app import Stopwatch


def test_stopwatch():
    stopwatch = Stopwatch()
    assert stopwatch._start_time is None
    assert stopwatch._stop_time is None


@patch("app.Stopwatch.get_now")
def test_start_stopwatch(mocked_class):
    mocked_class.return_value = 2
    stopwatch = Stopwatch()
    assert stopwatch.start_stopwatch() is 2
