import sys
import numpy as np
from functools import partial
from PySide6.QtWidgets import *
from main_ui import Ui_MainWindow
from sudoku_genarator import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_win = True

        self.cells = [[None for i in range(9)] for j in range(9)]
        self.cells = np.array(self.cells)

        self.ui.actionNew_ame.triggered.connect(self.new_game)
        self.ui.actionOpen_File.triggered.connect(self.open_file)
        self.ui.actionExit.triggered.connect(lambda: exit(0))
        self.ui.actionRed.triggered.connect(partial(self.change_theme, "red"))
        self.ui.actionYellow.triggered.connect(partial(self.change_theme, "yellow"))
        self.ui.actionGreen.triggered.connect(partial(self.change_theme, "green"))
        self.ui.actionHelp.triggered.connect(self.help)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionSolve.triggered.connect(self.solve)

        self.new_game()

    def new_game(self):
        self.game = generate_sudoku()
        self.board = empty_cell(self.game, 40)
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setStyleSheet("""
                    width: 40px;
                    height: 40px;
                    background-color: #5D0E41;
                    color: #EABE6C;
                    border: 3px solid #141E46; 
                    border-radius: 5px;
                    text-align: center;
                    font-size: 20px;
                """)
                if (self.board[i, j] != 0):
                    new_cell.setText(str(self.board[i, j]))
                    new_cell.setReadOnly(True)
                else:
                    new_cell.setReadOnly(False)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.cells[i][j] = new_cell
                self.ui.tabel_gl.addWidget(new_cell, i, j)

    def open_file(self):
        try:
            x = QFileDialog.getOpenFileName(self, 'Open file')
            with open(x[0], 'r') as f:
                for i, line in enumerate(f.readlines()):
                    line = line.split(" ")
                    last_index = len(line) - 1
                    line[last_index] = line[last_index].strip("\n")
                    for j, cell in enumerate(line):
                        self.cells[i][j].setText(cell)
                        if int(cell) == 0:
                            self.cells[i][j].setReadOnly(False)
                        else:
                            self.cells[i][j].setReadOnly(True)
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error ❌")
            msgBox.setText("""
                <h3>Can Not Open File</h3>
            """)
            msgBox.exec()

    def check(self):
        for i in self.cells:
            for j in i:
                j.setStyleSheet("""
                                   width: 40px;
                                   height: 40px;
                                   background-color: #5D0E41;
                                   color: #EABE6C;
                                   border: 3px solid #141E46;
                                   border-radius: 5px;
                                   text-align: center;
                                   font-size: 20px;
                               """)

        def check_row_or_colum(cells):
            win = True
            for i in cells:
                row = []
                bad_arg = None
                for j in i:
                    if (j.text() == ''):
                        win = False
                    if ((j.text() in row) and (j.text() != '')):
                        bad_arg = j.text()
                    else:
                        row.append(j.text())
                for j in i:
                    if j.text() == bad_arg:
                        win = False
                        j.setStyleSheet("""
                            width: 40px;
                            height: 40px;
                            background-color: red;
                            color: #EABE6C;
                            border: 3px solid #141E46; 
                            border-radius: 5px;
                            text-align: center;
                            font-size: 20px;
                        """)
            return win

        row_win = check_row_or_colum(self.cells)
        col_win = check_row_or_colum(self.cells.T)
        if row_win and col_win:
            self.win()

    def win(self):
        if (self.is_win):
            for i in self.cells:
                for j in i:
                    j.setStyleSheet("""
                                       width: 40px;
                                       height: 40px;
                                       background-color: green;
                                       color: #EABE6C;
                                       border: 3px solid #141E46;
                                       border-radius: 5px;
                                       text-align: center;
                                       font-size: 20px;
                                   """)
            msgBox = QMessageBox()
            msgBox.setWindowTitle("You Win 😐")
            msgBox.setText("""
                <h3>You Win 😐</h3>
            """)
            msgBox.exec()

    def change_theme(self, theme):
        if theme == 'red':
            self.setStyleSheet("""
                background-color: #FF204E;
                color: #DFF5FF;
            """)
        elif theme == 'yellow':
            self.setStyleSheet("""
                background-color: #FDA403;
                color: #DFF5FF;
            """)
        elif theme == 'green':
            self.setStyleSheet("""
                background-color: #4CCD99;
                color: #DFF5FF;
            """)

    def validation(self, i, j, text):
        if text not in [str(num) for num in range(1, 10)]:
            self.cells[i][j].setText("")
        else:
            self.check()

    def help(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Help ⚠")
        msgBox.setText("""
            <h3>Sudoku Help</h3>
        """)
        msgBox.exec()

    def about(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("About ⚠")
        msgBox.setText("""
            <h3>Eiliya Zanganeh</h3>
        """)
        msgBox.exec()

    def solve(self):
        self.is_win = False
        for i_idx, i in enumerate(self.cells):
            for j_idx, j in enumerate(i):
                j.setText(str(self.game[i_idx][j_idx]))
                j.setReadOnly(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
