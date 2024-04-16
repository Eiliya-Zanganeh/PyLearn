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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(100, 42)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #FF204E;color: #DFF5FF;")
        self.actionNew_ame = QAction(MainWindow)
        self.actionNew_ame.setObjectName(u"actionNew_ame")
        font1 = QFont()
        font1.setPointSize(10)
        self.actionNew_ame.setFont(font1)
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionRed = QAction(MainWindow)
        self.actionRed.setObjectName(u"actionRed")
        self.actionYellow = QAction(MainWindow)
        self.actionYellow.setObjectName(u"actionYellow")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSolve = QAction(MainWindow)
        self.actionSolve.setObjectName(u"actionSolve")
        self.actionGreen = QAction(MainWindow)
        self.actionGreen.setObjectName(u"actionGreen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabel_gl = QGridLayout()
        self.tabel_gl.setObjectName(u"tabel_gl")

        self.gridLayout.addLayout(self.tabel_gl, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 100, 22))
        self.menuNew_Game = QMenu(self.menubar)
        self.menuNew_Game.setObjectName(u"menuNew_Game")
        self.menuThem = QMenu(self.menubar)
        self.menuThem.setObjectName(u"menuThem")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuExit = QMenu(self.menubar)
        self.menuExit.setObjectName(u"menuExit")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuNew_Game.menuAction())
        self.menubar.addAction(self.menuThem.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.menuNew_Game.addAction(self.actionNew_ame)
        self.menuNew_Game.addAction(self.actionOpen_File)
        self.menuNew_Game.addAction(self.actionSolve)
        self.menuThem.addAction(self.actionRed)
        self.menuThem.addAction(self.actionYellow)
        self.menuThem.addAction(self.actionGreen)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuExit.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudoku Game", None))
        self.actionNew_ame.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionRed.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.actionYellow.setText(QCoreApplication.translate("MainWindow", u"Yellow", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSolve.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        self.actionGreen.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.menuNew_Game.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.menuThem.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuExit.setTitle(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

