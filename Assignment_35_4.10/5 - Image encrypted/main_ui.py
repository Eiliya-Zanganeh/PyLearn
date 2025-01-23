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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 479)
        MainWindow.setStyleSheet(u"background: #1A1A1D")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(6, -1, 791, 471))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.encrypt_input_lbl = QLabel(self.tab)
        self.encrypt_input_lbl.setObjectName(u"encrypt_input_lbl")
        self.encrypt_input_lbl.setGeometry(QRect(10, 10, 301, 421))
        self.encrypt_input_lbl.setStyleSheet(u"background: #3B1C32")
        self.encrypt_output_lbl = QLabel(self.tab)
        self.encrypt_output_lbl.setObjectName(u"encrypt_output_lbl")
        self.encrypt_output_lbl.setGeometry(QRect(470, 10, 301, 421))
        self.encrypt_output_lbl.setStyleSheet(u"background: #3B1C32")
        self.encrypt_select_img_btn = QPushButton(self.tab)
        self.encrypt_select_img_btn.setObjectName(u"encrypt_select_img_btn")
        self.encrypt_select_img_btn.setGeometry(QRect(320, 380, 141, 51))
        font = QFont()
        font.setPointSize(12)
        self.encrypt_select_img_btn.setFont(font)
        self.encrypt_select_img_btn.setStyleSheet(u"background-color: #6A1E55;\n"
"border-radius: 10px")
        self.encrypt_image_btn = QPushButton(self.tab)
        self.encrypt_image_btn.setObjectName(u"encrypt_image_btn")
        self.encrypt_image_btn.setGeometry(QRect(320, 320, 141, 51))
        self.encrypt_image_btn.setFont(font)
        self.encrypt_image_btn.setStyleSheet(u"background-color: #6A1E55;\n"
"border-radius: 10px")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.decrypt_input_lbl = QLabel(self.tab_2)
        self.decrypt_input_lbl.setObjectName(u"decrypt_input_lbl")
        self.decrypt_input_lbl.setGeometry(QRect(10, 10, 301, 421))
        self.decrypt_input_lbl.setStyleSheet(u"background: #3B1C32")
        self.decrypt_output_lbl = QLabel(self.tab_2)
        self.decrypt_output_lbl.setObjectName(u"decrypt_output_lbl")
        self.decrypt_output_lbl.setGeometry(QRect(470, 10, 301, 421))
        self.decrypt_output_lbl.setStyleSheet(u"background: #3B1C32")
        self.decrypt_select_img_btn = QPushButton(self.tab_2)
        self.decrypt_select_img_btn.setObjectName(u"decrypt_select_img_btn")
        self.decrypt_select_img_btn.setGeometry(QRect(320, 380, 141, 51))
        self.decrypt_select_img_btn.setFont(font)
        self.decrypt_select_img_btn.setStyleSheet(u"background-color: #6A1E55;\n"
"border-radius: 10px")
        self.decrypt_image_btn = QPushButton(self.tab_2)
        self.decrypt_image_btn.setObjectName(u"decrypt_image_btn")
        self.decrypt_image_btn.setGeometry(QRect(320, 220, 141, 51))
        self.decrypt_image_btn.setFont(font)
        self.decrypt_image_btn.setStyleSheet(u"background-color: #6A1E55;\n"
"border-radius: 10px")
        self.select_key_btn = QPushButton(self.tab_2)
        self.select_key_btn.setObjectName(u"select_key_btn")
        self.select_key_btn.setGeometry(QRect(320, 320, 141, 51))
        self.select_key_btn.setFont(font)
        self.select_key_btn.setStyleSheet(u"background-color: #6A1E55;\n"
"border-radius: 10px")
        self.selected_key_lbl = QLabel(self.tab_2)
        self.selected_key_lbl.setObjectName(u"selected_key_lbl")
        self.selected_key_lbl.setGeometry(QRect(320, 280, 141, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.selected_key_lbl.setFont(font1)
        self.selected_key_lbl.setStyleSheet(u"background: #3B1C32;\n"
"color: #ffffff")
        self.selected_key_lbl.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Image Encryption App", None))
        self.encrypt_input_lbl.setText("")
        self.encrypt_output_lbl.setText("")
        self.encrypt_select_img_btn.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.encrypt_image_btn.setText(QCoreApplication.translate("MainWindow", u"Encrypt Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Encrypt Image", None))
        self.decrypt_input_lbl.setText("")
        self.decrypt_output_lbl.setText("")
        self.decrypt_select_img_btn.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.decrypt_image_btn.setText(QCoreApplication.translate("MainWindow", u"Decrypt Image", None))
        self.select_key_btn.setText(QCoreApplication.translate("MainWindow", u"Select Key", None))
        self.selected_key_lbl.setText(QCoreApplication.translate("MainWindow", u"No key Selected", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Decrypt Image", None))
    # retranslateUi

