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
from PySide6.QtWidgets import (QApplication, QMainWindow, QRadioButton, QSizePolicy,
    QTextEdit, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 240)
        MainWindow.setStyleSheet(u"background-color: #222831;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 10, 241, 221))
        self.textEdit.setStyleSheet(u"background-color: #76ABAE;")
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(400, 10, 241, 221))
        self.textEdit_2.setStyleSheet(u"background-color: #76ABAE;")
        self.textEdit_2.setReadOnly(True)
        self.btn_run = QToolButton(self.centralwidget)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setGeometry(QRect(280, 150, 91, 71))
        font = QFont()
        font.setPointSize(15)
        self.btn_run.setFont(font)
        self.btn_run.setStyleSheet(u"background-color: #378CE7;\n"
"border-radius: 20px;")
        self.btn_english = QRadioButton(self.centralwidget)
        self.btn_english.setObjectName(u"btn_english")
        self.btn_english.setGeometry(QRect(290, 60, 61, 20))
        self.btn_english.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-radius: 10px;")
        self.btn_persion = QRadioButton(self.centralwidget)
        self.btn_persion.setObjectName(u"btn_persion")
        self.btn_persion.setGeometry(QRect(290, 100, 61, 20))
        self.btn_persion.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-radius: 10px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Translator", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.btn_english.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.btn_persion.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0627\u0631\u0633\u06cc", None))
    # retranslateUi

