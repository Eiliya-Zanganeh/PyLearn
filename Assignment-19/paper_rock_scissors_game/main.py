import random
from functools import partial

from PySide6.QtWidgets import QMainWindow, QApplication
from main_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.rock.clicked.connect(partial(self.click, 1))
        self.ui.paper.clicked.connect(partial(self.click, 2))
        self.ui.scissors.clicked.connect(partial(self.click, 3))

    def ai(self):
        return random.randint(1, 3)

    def winner(self, player, ai):
        if player == 1:
            if ai == 1:
                pass
            elif ai == 2:
                self.set_score(0)
            elif ai == 3:
                self.set_score(1)
        elif player == 2:
            if ai == 1:
                self.set_score(1)
            elif ai == 2:
                pass
            elif ai == 3:
                self.set_score(0)
        elif player == 3:
            if ai == 1:
                self.set_score(0)
            elif ai == 2:
                self.set_score(1)
            elif ai == 3:
                pass

    def show_ai_event(self, event):
        if event == 1:
            self.ui.ai.setText("✊")
        elif event == 2:
            self.ui.ai.setText("✋")
        elif event == 3:
            self.ui.ai.setText("✌️")

    def set_score(self, event):
        if event == 0:
            self.ui.ai_score.setText(
                str(
                    int(self.ui.ai_score.text()) + 1
                )
            )
        elif event == 1:
            self.ui.player_score.setText(
                str(
                    int(self.ui.player_score.text()) + 1
                )
            )

    def click(self, event):
        if event == 1:
            self.ui.player.setText("✊")
            ai_event = self.ai()
            self.show_ai_event(ai_event)
            self.winner(event, ai_event)
        elif event == 2:
            self.ui.player.setText("✋")
            ai_event = self.ai()
            self.show_ai_event(ai_event)
            self.winner(event, ai_event)
        elif event == 3:
            self.ui.player.setText("✌️")
            ai_event = self.ai()
            self.show_ai_event(ai_event)
            self.winner(event, ai_event)


app = QApplication()
window = MainWindow()
window.show()
app.exec()
