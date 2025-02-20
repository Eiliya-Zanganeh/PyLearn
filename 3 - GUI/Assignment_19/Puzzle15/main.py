import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from main_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buttons = [
            [self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
            [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8],
            [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
            [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16]
        ]
        numbers_list = list(range(1, 17))
        random.shuffle(numbers_list)
        self.empty_btn = []
        for row in range(4):
            for button in range(4):
                num = numbers_list[row * 4 + button]
                self.buttons[row][button].setText(str(num))
                self.buttons[row][button].clicked.connect(partial(self.play, row, button))
                if num == 16:
                    self.buttons[row][button].setVisible(False)
                    self.empty_btn.extend([row, button])

    def play(self, i, j):
        if (
                self.empty_btn[0] == i and (self.empty_btn[1] - 1 == j or self.empty_btn[1] + 1 == j) or
                self.empty_btn[1] == j and (self.empty_btn[0] - 1 == i or self.empty_btn[0] + 1 == i)
        ):
            self.buttons[self.empty_btn[0]][self.empty_btn[1]].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText("16")

            self.buttons[self.empty_btn[0]][self.empty_btn[1]].setVisible(True)
            self.buttons[i][j].setVisible(False)

            self.empty_btn = [i, j]
            if self.check_win():
                msgBox = QMessageBox()
                msgBox.setWindowTitle("You Win")
                msgBox.setText("You Win 😐")
                msgBox.exec_()
                self.__init__()

    def check_win(self):
        index = 1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                index += 1

        return True


app = QApplication()
window = MainWindow()
window.show()
app.exec()
