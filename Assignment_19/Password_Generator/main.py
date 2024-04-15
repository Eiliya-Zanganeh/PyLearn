import random
import string
from functools import partial

from PySide6.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(280, 130)
        self.level = 1
        self.ui.radioButton.clicked.connect(partial(self.change_level, 1))
        self.ui.radioButton_2.clicked.connect(partial(self.change_level, 2))
        self.ui.radioButton_3.clicked.connect(partial(self.change_level, 3))

    def change_level(self, num):
        self.level = num
        self.genarate_password()
        if self.level == 1:
            self.ui.radioButton.setChecked(True)
            self.ui.radioButton_2.setChecked(False)
            self.ui.radioButton_3.setChecked(False)
        elif self.level == 2:
            self.ui.radioButton.setChecked(False)
            self.ui.radioButton_2.setChecked(True)
            self.ui.radioButton_3.setChecked(False)
        elif self.level == 3:
            self.ui.radioButton.setChecked(False)
            self.ui.radioButton_2.setChecked(False)
            self.ui.radioButton_3.setChecked(True)

    def genarate_password(self):
        char_list = []
        if self.level == 1:
            char_list.extend(random.choices(string.ascii_lowercase, k=5))
            char_list.append(random.choice(string.ascii_uppercase))
            char_list.append(random.choice(string.digits))
            char_list.append(random.choice(string.punctuation))
        elif self.level == 2:
            char_list.extend([random.choice(string.ascii_uppercase)] * random.randint(1, 2))
            char_list.extend([random.choice(string.digits)] * random.randint(1, 2))
            char_list.extend([random.choice(string.punctuation)] * random.randint(1, 2))
            char_list.extend(random.choices(string.ascii_lowercase, k=12 - len(char_list)))

        elif self.level == 3:
            char_list.extend([random.choice(string.ascii_uppercase)] * random.randint(1, 3))
            char_list.extend([random.choice(string.digits)] * random.randint(1, 3))
            char_list.extend([random.choice(string.punctuation)] * random.randint(1, 3))
            char_list.extend(random.choices(string.ascii_lowercase, k=20 - len(char_list)))
        random.shuffle(char_list)
        self.ui.lineEdit.setText("".join(char_list))


app = QApplication()
window = MainWindow()
window.show()
app.exec()
