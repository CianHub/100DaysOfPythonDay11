from datetime import datetime
import time
import threading


class Stopwatch():
    start_time = None
    stop_time = None

    def start_stopwatch(self):
        self.start_time = datetime.now()
        print('Stopwatch started at: ' + str(self.start_time.time())[:-7])

        now = time.time()
        counter = 0

        while self.stop_time is None:

            if time.time() - now > 1:
                now = time.time()
                counter = counter + 1
                print(str(counter) + ' second(s) elapsed')

    def stop_stopwatch(self):
        if self.start_time is not None:
            self.stop_time = datetime.now()
            print('Stopwatch stopped at: ' + str(self.stop_time.time())[:-7])

            self.time_recorded()

    def time_recorded(self):
        if self.stop_time is not None and self.start_time is not None:
            print('Time recorded: ' +
                  str((self.stop_time - self.start_time).total_seconds())[:-7] + ' seconds')
