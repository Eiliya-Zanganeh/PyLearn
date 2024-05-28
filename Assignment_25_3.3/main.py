from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from main_ui import Ui_MainWindow
from Thread_Module import StopwatchThread, TimerThread, WorldClock, AlarmThread
from Database_Module import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stopwatch = StopwatchThread()
        self.stopwatch.update_time.connect(self.update_stopwatch)
        self.timer = None

        timezones = ["America/New_York", "Europe/Berlin", "Asia/Tehran"]
        self.world_clock = WorldClock(timezones)
        self.world_clock.update_timezone.connect(self.show_world_clock)
        self.world_clock.start()

        self.database = Database()
        self.clocks = None
        self.alarm = AlarmThread()
        self.alarm.alarm_time.connect(self.alarm_run)
        self.load_clock()
        self.clock_idx = 0
        self.current_clock(0)
        self.ui.cmb_clocks.currentIndexChanged.connect(self.current_clock)
        self.ui.lbl_alarm_add.clicked.connect(self.add_clock)
        self.ui.lbl_alarm_delete.clicked.connect(self.delete_clock)
        self.ui.lbl_alarm_edit.clicked.connect(self.edit_clock)
        self.alarm.start()

        self.ui.btn_start_stopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(self.reset_stopwatch)

        self.ui.btn_start_timer.clicked.connect(self.start_timer)
        self.ui.btn_stop_timer.clicked.connect(self.stop_timer)
        self.ui.btn_reset_timer.clicked.connect(self.reset_timer)

    def start_stopwatch(self):
        self.stopwatch.start()

    def update_stopwatch(self, new_text):
        self.ui.lbl_stopwatch.setText(" : ".join(new_text))

    def stop_stopwatch(self):
        self.stopwatch.terminate()

    def reset_stopwatch(self):
        self.stopwatch.reset()
        self.ui.lbl_stopwatch.setText("00 : 00 : 00")

    def start_timer(self):
        if self.timer is None:
            try:
                hour = int(self.ui.lbl_timer_hour.text())
                minute = int(self.ui.lbl_timer_minute.text())
                second = int(self.ui.lbl_timer_second.text())
                if 60 > second >= 0 and 60 > minute >= 0 and hour >= 0:
                    if hour == 0 and minute == 0 and second == 0:
                        msgBox = QMessageBox()
                        msgBox.setWindowTitle("attention !")
                        msgBox.setText("Please enter hour and minute and second 😐")
                        msgBox.exec()
                    else:
                        self.timer = TimerThread(hour, minute, second)
                        self.timer.minus_time.connect(self.update_timer)
                        self.timer.start()
                else:
                    self.reset_timer()
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("attention !")
                    msgBox.setText("Please enter Valid hour and minute and second 😐")
                    msgBox.exec()
            except:
                self.reset_timer()
                msgBox = QMessageBox()
                msgBox.setWindowTitle("attention !")
                msgBox.setText("Please enter Valid hour and minute and second 😐")
                msgBox.exec()
        else:
            self.timer.start()

    def update_timer(self, new_text):
        if new_text == ('00', '00', '00'):
            self.reset_timer()
        else:
            self.ui.lbl_timer_hour.setText(new_text[0])
            self.ui.lbl_timer_minute.setText(new_text[1])
            self.ui.lbl_timer_second.setText(new_text[2])

    def stop_timer(self):
        if self.timer is not None:
            self.timer.terminate()

    def reset_timer(self):
        self.stop_timer()
        self.timer = None
        self.ui.lbl_timer_hour.setText("00")
        self.ui.lbl_timer_minute.setText("00")
        self.ui.lbl_timer_second.setText("00")

    def show_world_clock(self, times):
        self.ui.lbl_USA.setText(times[0])
        self.ui.lbl_Germany.setText(times[1])
        self.ui.lbl_Iran.setText(times[2])

    def current_clock(self, idx):
        try:
            time = self.clocks[idx][1]
            hour, minute, second = time.split(" : ")
            self.clock_idx = idx
            self.ui.lbl_alarm_hour.setText(hour)
            self.ui.lbl_alarm_minute.setText(minute)
            self.ui.lbl_alarm_second.setText(second)
        except:
            self.ui.lbl_alarm_hour.setText("00")
            self.ui.lbl_alarm_minute.setText("00")
            self.ui.lbl_alarm_second.setText("00")

    def load_clock(self):
        self.clocks = self.database.load_clocks()
        self.alarm.set_clock(self.clocks)
        self.ui.cmb_clocks.clear()
        self.ui.cmb_clocks.addItems(map(lambda val: val[1], self.clocks))

    def add_clock(self):
        try:
            hour = int(self.ui.lbl_alarm_hour.text())
            minute = int(self.ui.lbl_alarm_minute.text())
            second = int(self.ui.lbl_alarm_second.text())
            if 60 > second >= 0 and 60 > minute >= 0 and 24 > hour >= 0:
                self.database.insert_clock(f"{hour:02} : {minute:02} : {second:02}")
                self.load_clock()
                msgBox = QMessageBox()
                msgBox.setWindowTitle("attention !")
                msgBox.setText("Clock Added 😐")
                msgBox.exec()
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("attention !")
                msgBox.setText("Please enter Valid hour and minute and second 😐")
                msgBox.exec()
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("attention !")
            msgBox.setText("Please enter Valid hour and minute and second 😐")
            msgBox.exec()

    def delete_clock(self):
        idx = self.clocks[self.clock_idx][0]
        self.database.delete_clock(idx)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("attention !")
        msgBox.setText("Clock removed 😐")
        msgBox.exec()
        self.load_clock()

    def edit_clock(self):
        try:
            idx = self.clocks[self.clock_idx][0]
            hour = int(self.ui.lbl_alarm_hour.text())
            minute = int(self.ui.lbl_alarm_minute.text())
            second = int(self.ui.lbl_alarm_second.text())
            if 60 > second >= 0 and 60 > minute >= 0 and 24 > hour >= 0:
                self.database.edit_clock(idx, f"{hour:02} : {minute:02} : {second:02}")
                self.load_clock()
                msgBox = QMessageBox()
                msgBox.setWindowTitle("attention !")
                msgBox.setText("Clock Edited 😐")
                msgBox.exec()
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("attention !")
                msgBox.setText("Please enter Valid hour and minute and second 😐")
                msgBox.exec()
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("attention !")
            msgBox.setText("Please enter Valid hour and minute and second 😐")
            msgBox.exec()

    def alarm_run(self, clock):
        self.database.delete_clock(clock[0])
        self.load_clock()
        msgBox = QMessageBox()
        msgBox.setWindowTitle("attention !")
        msgBox.setText(clock[1])
        msgBox.exec()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
