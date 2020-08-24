from datetime import datetime
import time


class Stopwatch():

    def __init__(self):
        self._start_time = None
        self._stop_time = None
        self._recorded_time = 0

    def start_stopwatch(self):
        self._recorded_time = 0
        return datetime.now()

    def stop_stopwatch(self):
        if self._start_time is not None:
            return datetime.now()

        else:
            return 'Stopwatch has not been started'

    def time_recorded(self):
        if self._start_time is not None and self._stop_time is not None:
            return (self._stop_time - self._start_time).total_seconds()
        else:
            return 'Stopwatch was not recording'


if __name__ == '__main__':
    stopwatch = Stopwatch()
    stopwatch()
