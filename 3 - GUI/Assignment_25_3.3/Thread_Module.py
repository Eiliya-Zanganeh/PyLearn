import time
from datetime import datetime

import pytz
from PySide6.QtCore import QThread, Signal
from Time_Module import Timer


class StopwatchThread(QThread):
    update_time = Signal(tuple)

    def __init__(self):
        super().__init__()
        self.time = Timer()

    def run(self):
        while True:
            time.sleep(1)
            self.time.update()
            self.update_time.emit(self.time.__str__())

    def reset(self):
        self.time.reset()


class TimerThread(QThread):
    minus_time = Signal(tuple)

    def __init__(self, hour, minute, second):
        super().__init__()
        self.time = Timer(hour, minute, second)

    def run(self):
        while True:
            time.sleep(1)
            self.time.minus()
            self.minus_time.emit(self.time.__str__())


class WorldClock(QThread):
    update_timezone = Signal(list)

    def __init__(self, timezones):
        super().__init__()
        self.timezones = timezones

    def run(self):
        while True:
            outputs = []
            for timezone in self.timezones:
                tz = pytz.timezone(timezone)
                current_time = datetime.now(tz)
                current_time = current_time.strftime("%H:%M:%S")
                outputs.append(current_time)
            self.update_timezone.emit(outputs)
            time.sleep(1)


class AlarmThread(QThread):
    alarm_time = Signal(tuple)

    def __init__(self):
        super().__init__()
        self.clocks = None

    def run(self):
        while True:
            if self.clocks is not None:
                current_time = datetime.now()
                current_time = current_time.strftime("%H : %M : %S")
                times = list(map(lambda result: result[1], self.clocks))
                for t in times:
                    if t == current_time:
                        self.alarm_time.emit(self.clocks[times.index(t)])
            time.sleep(1)

    def set_clock(self, clocks: None):
        self.clocks = clocks
