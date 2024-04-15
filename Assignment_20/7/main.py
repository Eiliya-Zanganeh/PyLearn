import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(340, 260)
        self.ui.btn_event_0.setText("🤚")
        self.ui.btn_event_1.setText("✋")
        self.ui.btn_event_0.clicked.connect(partial(self.click, False))
        self.ui.btn_event_1.clicked.connect(partial(self.click, True))
        self.count_game = 0

    def click(self, event):
        self.count_game += 1
        self.ui.count_game.setText(str(self.count_game))
        if event:
            self.ui.User.setText("✋")
        else:
            self.ui.User.setText("🤚")
        self.ui.Computer_1.setText("✋" if random.choice([True, False]) else "🤚")
        self.ui.Computer_2.setText("✋" if random.choice([True, False]) else "🤚")
        stage = [self.ui.User.text(), self.ui.Computer_1.text(), self.ui.Computer_2.text()]
        if stage.count("✋") == 1:
            event_win = "✋"
        elif stage.count("🤚") == 1:
            event_win = "🤚"
        else:
            event_win = None
        if event_win is not None:
            winner = stage.index(event_win)
            if winner == 0:
                self.ui.User_score.setText(str(int(self.ui.User_score.text()) + 1))
            elif winner == 1:
                self.ui.Computer_1_score.setText(str(int(self.ui.Computer_1_score.text()) + 1))
            elif winner == 2:
                self.ui.Computer_2_score.setText(str(int(self.ui.Computer_2_score.text()) + 1))
        if self.count_game == 5:
            self.count_game = 0
            self.ui.count_game.setText(str(self.count_game))
            all_score = [int(self.ui.User_score.text()), int(self.ui.Computer_1_score.text()),
                         int(self.ui.Computer_2_score.text())]
            top_score = max(all_score)
            winners = [index for index, number in enumerate(all_score) if number == top_score]
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Message")
            if len(winners) != 0:
                msg = ""
                for winner in winners:
                    if winner == 0:
                        msg += "User "
                    elif winner == 1:
                        msg += "Computer 1 "
                    elif winner == 2:
                        msg += "Computer 2 "
                    msgBox.setText(msg + "Win .... 😐")
            else:
                msgBox.setText("We Don't Have a Winner .... 😐")
            msgBox.exec()
            self.ui.User_score.setText("0")
            self.ui.Computer_1_score.setText("0")
            self.ui.Computer_2_score.setText("0")


app = QApplication()
window = MainWindow()
window.show()
app.exec()
