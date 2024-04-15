# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 287)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: #00A9FF")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tasks_gl = QGridLayout()
        self.tasks_gl.setObjectName(u"tasks_gl")

        self.verticalLayout_3.addLayout(self.tasks_gl)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.title_tb = QLineEdit(self.centralwidget)
        self.title_tb.setObjectName(u"title_tb")
        self.title_tb.setStyleSheet(u"background-color:#CDF5FD;\n"
"border-radius: 8px;\n"
"padding: 15px;\n"
"margin-top: 30px;")

        self.verticalLayout_5.addWidget(self.title_tb)

        self.description_tb = QLineEdit(self.centralwidget)
        self.description_tb.setObjectName(u"description_tb")
        self.description_tb.setStyleSheet(u"background-color:#CDF5FD;\n"
"border-radius: 8px;\n"
"padding: 15px;")

        self.verticalLayout_5.addWidget(self.description_tb)

        self.time_tb = QLineEdit(self.centralwidget)
        self.time_tb.setObjectName(u"time_tb")
        self.time_tb.setStyleSheet(u"background-color:#CDF5FD;\n"
"border-radius: 8px;\n"
"padding: 15px;")

        self.verticalLayout_5.addWidget(self.time_tb)

        self.add_task_btn = QPushButton(self.centralwidget)
        self.add_task_btn.setObjectName(u"add_task_btn")
        self.add_task_btn.setStyleSheet(u"background-color: #89CFF3;\n"
"border-radius: 8px;\n"
"padding: 15px;")

        self.verticalLayout_5.addWidget(self.add_task_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_tb.setText("")
        self.title_tb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter task title", None))
        self.description_tb.setText("")
        self.description_tb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter task description", None))
        self.time_tb.setText("")
        self.time_tb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter task time", None))
        self.add_task_btn.setText(QCoreApplication.translate("MainWindow", u"Add New Task", None))
    # retranslateUi

