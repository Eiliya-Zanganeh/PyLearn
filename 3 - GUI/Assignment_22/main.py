import sys
from functools import partial
from PySide6.QtWidgets import *
from main_ui import Ui_MainWindow
from database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.database = Database()
        self.show_ui()
        self.setWindowTitle("Todo List")
        self.ui.add_task_btn.clicked.connect(self.insert_task)

    def show_ui(self):
        tasks = self.database.load_tasks()
        for i in range(len(tasks)):

            new_checkbox = QCheckBox()
            new_checkbox.setChecked(tasks[i][3])
            new_checkbox.clicked.connect(partial(self.edit_task_done, tasks[i][0]))

            new_label = QPushButton()
            text: str = tasks[i][1]
            new_label.setText(text)
            self.setFixedWidth(400)
            if tasks[i][3] == 1:
                new_label.setStyleSheet("""
                            background-color: green;
                            padding: 15px;
                            border: 3px solid #89CFF3;
                            border-radius: 10px;
                        """)
            else:
                if tasks[i][4] == 1:
                    new_label.setStyleSheet("""
                                background-color: red;
                                padding: 15px;
                                border: 3px solid #89CFF3;
                                border-radius: 10px;
                            """)
                else:
                    new_label.setStyleSheet("""
                                background-color: #A0E9FF;
                                padding: 15px;
                                border: 3px solid #89CFF3;
                                border-radius: 10px;
                            """)
            new_label.clicked.connect(partial(self.show_description, tasks[i][0]))

            new_btn = QPushButton()
            new_btn.setText("❌")
            new_btn.setStyleSheet("""
                background-color: #A0E9FF;
                padding: 5px;
                border: 3px solid #89CFF3;
                border-radius: 10px;
            """)
            new_btn.clicked.connect(partial(self.delete_task, tasks[i][0]))

            new_btn2 = QPushButton()
            new_btn2.setText("⚠")
            new_btn2.setStyleSheet("""
                background-color: #A0E9FF;
                padding: 5px;
                border: 3px solid #89CFF3;
                border-radius: 10px;
            """)
            new_btn2.clicked.connect(partial(self.edit_task_priority, tasks[i][0]))

            self.ui.tasks_gl.addWidget(new_checkbox, i, 0)
            self.ui.tasks_gl.addWidget(new_label, i, 1)
            self.ui.tasks_gl.addWidget(new_btn, i, 2)
            self.ui.tasks_gl.addWidget(new_btn2, i, 3)

    def insert_task(self):
        title = self.ui.title_tb.text()
        description = self.ui.description_tb.text()
        time = self.ui.time_tb.text()
        self.database.insert_task(title, description, time)
        self.ui.title_tb.setText("")
        self.ui.description_tb.setText("")
        self.ui.time_tb.setText("")
        self.show_ui()

    def edit_task_done(self, id):
        self.database.edit_task_done(id)
        self.show_ui()

    def edit_task_priority(self, id):
        self.database.edit_task_priority(id)
        self.show_ui()

    def delete_task(self, id):
        self.database.delete_task(id)
        while self.ui.tasks_gl.count():
            item = self.ui.tasks_gl.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.show_ui()

    def show_description(self, id):
        data = self.database.show_description(id)
        msgBox = QMessageBox()
        msgBox.setWindowTitle(data[0][1])
        msgBox.setText(f"""
            <h3>id: {data[0][0]}</h3>
            <h3>title: {data[0][1]}</h3>
            <h3>description: {data[0][2]}</h3>
            <h3>is Done: {'✅' if data[0][3] == 1 else '❌'}</h3>
            <h3>priority: {'✅' if data[0][4] == 1 else '❌'}</h3>
            <h3>time: {data[0][5]}</h3>
        """)
        msgBox.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()
    app.exec()
