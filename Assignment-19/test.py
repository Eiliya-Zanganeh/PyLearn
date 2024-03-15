from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import numpy

app = QApplication([])
loader = QUiLoader()
window = loader.load("mainwindow.ui")
window.show()

app.exec()