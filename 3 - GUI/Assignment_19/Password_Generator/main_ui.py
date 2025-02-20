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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QRadioButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(280, 130)
        MainWindow.setStyleSheet(u"background-color: #070F2B;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 80, 161, 31))
        self.lineEdit.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 10px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 30, 61, 20))
        self.radioButton.setStyleSheet(u"background-color: #9290C3;\n"
"border-radius: 8px")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(110, 30, 61, 20))
        self.radioButton_2.setStyleSheet(u"background-color: #9290C3;\n"
"border-radius: 8px")
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(200, 30, 61, 20))
        self.radioButton_3.setStyleSheet(u"background-color: #9290C3;\n"
"border-radius: 8px")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Genarator :|", None))
        self.lineEdit.setText("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"low", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"middle", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"high", None))
    # retranslateUi

