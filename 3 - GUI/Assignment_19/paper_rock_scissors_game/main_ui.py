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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QSizePolicy,
    QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 350)
        MainWindow.setStyleSheet(u"background-color: #378CE7;\n"
"border-radius: 10px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.paper = QToolButton(self.centralwidget)
        self.paper.setObjectName(u"paper")
        self.paper.setGeometry(QRect(0, 300, 100, 51))
        font = QFont()
        font.setPointSize(18)
        self.paper.setFont(font)
        self.paper.setStyleSheet(u"background-color: #67C6E3;\n"
"border-radius: 10px;")
        self.rock = QToolButton(self.centralwidget)
        self.rock.setObjectName(u"rock")
        self.rock.setGeometry(QRect(100, 300, 100, 51))
        self.rock.setFont(font)
        self.rock.setStyleSheet(u"background-color: #67C6E3;\n"
"border-radius: 10px;")
        self.scissors = QToolButton(self.centralwidget)
        self.scissors.setObjectName(u"scissors")
        self.scissors.setGeometry(QRect(200, 300, 100, 51))
        self.scissors.setFont(font)
        self.scissors.setStyleSheet(u"background-color: #67C6E3;\n"
"border-radius: 10px;")
        self.player = QToolButton(self.centralwidget)
        self.player.setObjectName(u"player")
        self.player.setEnabled(False)
        self.player.setGeometry(QRect(90, 180, 121, 71))
        self.player.setFont(font)
        self.player.setStyleSheet(u"background-color: #67C6E3;\n"
"border-radius: 10px;")
        self.ai = QToolButton(self.centralwidget)
        self.ai.setObjectName(u"ai")
        self.ai.setEnabled(False)
        self.ai.setGeometry(QRect(90, 80, 121, 71))
        self.ai.setFont(font)
        self.ai.setStyleSheet(u"background-color: #67C6E3;\n"
"border-radius: 10px;\n"
"text-transform: scaleY(-1);")
        self.ai.setAutoRepeat(False)
        self.ai.setPopupMode(QToolButton.DelayedPopup)
        self.ai_score = QLineEdit(self.centralwidget)
        self.ai_score.setObjectName(u"ai_score")
        self.ai_score.setGeometry(QRect(260, 10, 41, 41))
        self.ai_score.setFont(font)
        self.ai_score.setStyleSheet(u"border: 2px solid blue;\n"
"border-redius: 10px;")
        self.ai_score.setAlignment(Qt.AlignCenter)
        self.ai_score.setReadOnly(True)
        self.player_score = QLineEdit(self.centralwidget)
        self.player_score.setObjectName(u"player_score")
        self.player_score.setGeometry(QRect(90, 10, 41, 41))
        self.player_score.setFont(font)
        self.player_score.setStyleSheet(u"border: 2px solid blue;\n"
"border-redius: 10px;")
        self.player_score.setAlignment(Qt.AlignCenter)
        self.player_score.setReadOnly(True)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(0, 10, 81, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u"border: 2px solid blue;\n"
"border-redius: 10px;")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(140, 10, 111, 41))
        self.lineEdit_4.setFont(font1)
        self.lineEdit_4.setStyleSheet(u"border: 2px solid blue;\n"
"border-redius: 10px;")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.paper.setText(QCoreApplication.translate("MainWindow", u"\u270b", None))
        self.rock.setText(QCoreApplication.translate("MainWindow", u"\u270a", None))
        self.scissors.setText(QCoreApplication.translate("MainWindow", u"\u270c\ufe0f", None))
        self.player.setText("")
        self.ai.setText("")
        self.ai_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.player_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Your Score", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"computer score", None))
    # retranslateUi

