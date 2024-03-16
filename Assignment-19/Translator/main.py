from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow
from googletrans import Translator


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.translator = Translator()
        self.language = "fa"
        self.ui.btn_persion.setChecked(True)
        self.ui.btn_persion.clicked.connect(partial(self.change_language, "fa"))
        self.ui.btn_english.clicked.connect(partial(self.change_language, "en"))
        self.ui.btn_run.clicked.connect(self.translate_text)

    def change_language(self, new_language):
        self.language = new_language
        if new_language == "fa":
            self.ui.btn_persion.setChecked(True)
            self.ui.btn_english.setChecked(False)
        elif new_language == "en":
            self.ui.btn_english.setChecked(True)
            self.ui.btn_persion.setChecked(False)

    def translate_text(self):
        text = self.ui.textEdit.toPlainText()
        translation = self.translator.translate(text, dest=self.language)
        self.ui.textEdit_2.setText(translation.text)


app = QApplication()
window = MainWindow()
window.show()
app.exec()
