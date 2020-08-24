import pytest
from unittest.mock import patch
from datetime import datetime

from app import Stopwatch


def test_stopwatch():
    stopwatch = Stopwatch()
    assert stopwatch._start_time is None
    assert stopwatch._stop_time is None
    assert stopwatch._recorded_time is 0


@patch("app.datetime")
def test_start_stopwatch(mocked_class):
    mocked_class.now.return_value = 2
    stopwatch = Stopwatch()
    assert stopwatch.start_stopwatch() is 2


@patch("app.datetime")
def test_stop_stopwatch(mocked_class):
    mocked_class.now.return_value = 2
    stopwatch = Stopwatch()

    stopwatch._start_time = None
    assert stopwatch.stop_stopwatch() == 'Stopwatch has not been started'

    stopwatch._start_time = 3
    assert stopwatch.stop_stopwatch() == 2


def test_time_recorded():
    stopwatch = Stopwatch()

    stopwatch._start_time = None
    assert stopwatch.time_recorded() == 'Stopwatch was not recording'

    stopwatch._stop_time = None
    assert stopwatch.time_recorded() == 'Stopwatch was not recording'

    stopwatch._start_time = None
    stopwatch._stop_time = None
    assert stopwatch.time_recorded() == 'Stopwatch was not recording'

    stopwatch._start_time = datetime.now()
    stopwatch._stop_time = datetime.now()
    assert stopwatch.time_recorded() == (
        stopwatch._stop_time - stopwatch._start_time).total_seconds()
