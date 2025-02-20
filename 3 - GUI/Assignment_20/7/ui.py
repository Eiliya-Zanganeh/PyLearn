# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QSizePolicy,
    QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(340, 260)
        MainWindow.setStyleSheet(u"background-color: #1E5287;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_event_0 = QToolButton(self.centralwidget)
        self.btn_event_0.setObjectName(u"btn_event_0")
        self.btn_event_0.setGeometry(QRect(70, 190, 91, 61))
        font = QFont()
        font.setPointSize(20)
        self.btn_event_0.setFont(font)
        self.btn_event_0.setStyleSheet(u"background-color: #158A8C;\n"
"border-radius: 20px;")
        self.btn_event_1 = QToolButton(self.centralwidget)
        self.btn_event_1.setObjectName(u"btn_event_1")
        self.btn_event_1.setGeometry(QRect(170, 190, 91, 61))
        self.btn_event_1.setFont(font)
        self.btn_event_1.setStyleSheet(u"background-color: #158A8C;\n"
"border-radius: 20px;")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 71, 31))
        self.lineEdit.setStyleSheet(u"background-color: #158A8C;\n"
"border: none;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.User = QLineEdit(self.centralwidget)
        self.User.setObjectName(u"User")
        self.User.setGeometry(QRect(120, 120, 91, 61))
        self.User.setFont(font)
        self.User.setStyleSheet(u"background-color: #158A8C;")
        self.User.setAlignment(Qt.AlignCenter)
        self.User.setReadOnly(True)
        self.count_game = QLineEdit(self.centralwidget)
        self.count_game.setObjectName(u"count_game")
        self.count_game.setGeometry(QRect(270, 50, 61, 41))
        self.count_game.setStyleSheet(u"background-color: #158A8C;")
        self.count_game.setAlignment(Qt.AlignCenter)
        self.count_game.setReadOnly(True)
        self.Computer_2 = QLineEdit(self.centralwidget)
        self.Computer_2.setObjectName(u"Computer_2")
        self.Computer_2.setGeometry(QRect(170, 50, 91, 61))
        self.Computer_2.setFont(font)
        self.Computer_2.setStyleSheet(u"background-color: #158A8C;")
        self.Computer_2.setAlignment(Qt.AlignCenter)
        self.Computer_2.setReadOnly(True)
        self.Computer_1 = QLineEdit(self.centralwidget)
        self.Computer_1.setObjectName(u"Computer_1")
        self.Computer_1.setGeometry(QRect(70, 50, 91, 61))
        self.Computer_1.setFont(font)
        self.Computer_1.setStyleSheet(u"background-color: #158A8C;")
        self.Computer_1.setAlignment(Qt.AlignCenter)
        self.Computer_1.setReadOnly(True)
        self.User_score = QLineEdit(self.centralwidget)
        self.User_score.setObjectName(u"User_score")
        self.User_score.setGeometry(QRect(80, 10, 31, 31))
        self.User_score.setStyleSheet(u"background-color: #158A8C;\n"
"border: none;")
        self.User_score.setAlignment(Qt.AlignCenter)
        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(120, 10, 71, 31))
        self.lineEdit_8.setStyleSheet(u"background-color: #158A8C;\n"
"border: none;")
        self.lineEdit_8.setAlignment(Qt.AlignCenter)
        self.Computer_1_score = QLineEdit(self.centralwidget)
        self.Computer_1_score.setObjectName(u"Computer_1_score")
        self.Computer_1_score.setGeometry(QRect(190, 10, 31, 31))
        self.Computer_1_score.setStyleSheet(u"background-color: #158A8C;\n"
"border: none;")
        self.Computer_1_score.setAlignment(Qt.AlignCenter)
        self.Computer_2_score = QLineEdit(self.centralwidget)
        self.Computer_2_score.setObjectName(u"Computer_2_score")
        self.Computer_2_score.setGeometry(QRect(300, 10, 31, 31))
        self.Computer_2_score.setStyleSheet(u"background-color: #158A8C;\n"
"border: none;")
        self.Computer_2_score.setAlignment(Qt.AlignCenter)
        self.lineEdit_10 = QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(230, 10, 71, 31))
        self.lineEdit_10.setStyleSheet(u"background-color: #158A8C;\n"
"border: none;")
        self.lineEdit_10.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_event_0.setText("")
        self.btn_event_1.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.count_game.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.User_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"Computer 1:", None))
        self.Computer_1_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Computer_2_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"Computer 2:", None))
    # retranslateUi

