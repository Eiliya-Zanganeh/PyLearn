# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(570, 331)
        MainWindow.setStyleSheet(u"background-color: #1B4242;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 571, 331))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.lbl_USA = QLabel(self.tab)
        self.lbl_USA.setObjectName(u"lbl_USA")
        self.lbl_USA.setGeometry(QRect(30, 80, 221, 71))
        font = QFont()
        font.setPointSize(20)
        self.lbl_USA.setFont(font)
        self.lbl_USA.setLayoutDirection(Qt.LeftToRight)
        self.lbl_USA.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.lbl_USA.setAlignment(Qt.AlignCenter)
        self.lbl_Germany = QLabel(self.tab)
        self.lbl_Germany.setObjectName(u"lbl_Germany")
        self.lbl_Germany.setGeometry(QRect(310, 80, 221, 71))
        self.lbl_Germany.setFont(font)
        self.lbl_Germany.setLayoutDirection(Qt.LeftToRight)
        self.lbl_Germany.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.lbl_Germany.setAlignment(Qt.AlignCenter)
        self.lbl_Iran = QLabel(self.tab)
        self.lbl_Iran.setObjectName(u"lbl_Iran")
        self.lbl_Iran.setGeometry(QRect(170, 210, 221, 71))
        self.lbl_Iran.setFont(font)
        self.lbl_Iran.setLayoutDirection(Qt.LeftToRight)
        self.lbl_Iran.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.lbl_Iran.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 131, 41))
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 30, 131, 41))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 160, 131, 41))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.cmb_clocks = QComboBox(self.tab_2)
        self.cmb_clocks.setObjectName(u"cmb_clocks")
        self.cmb_clocks.setGeometry(QRect(200, 20, 151, 81))
        self.cmb_clocks.setFont(font1)
        self.cmb_clocks.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 10px;\n"
"padding: 20px;")
        self.lbl_alarm_minute = QLineEdit(self.tab_2)
        self.lbl_alarm_minute.setObjectName(u"lbl_alarm_minute")
        self.lbl_alarm_minute.setGeometry(QRect(240, 130, 71, 71))
        self.lbl_alarm_minute.setFont(font)
        self.lbl_alarm_minute.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;\n"
"padding: 20px;")
        self.lbl_alarm_hour = QLineEdit(self.tab_2)
        self.lbl_alarm_hour.setObjectName(u"lbl_alarm_hour")
        self.lbl_alarm_hour.setGeometry(QRect(160, 130, 71, 71))
        self.lbl_alarm_hour.setFont(font)
        self.lbl_alarm_hour.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;\n"
"padding: 20px;")
        self.lbl_alarm_second = QLineEdit(self.tab_2)
        self.lbl_alarm_second.setObjectName(u"lbl_alarm_second")
        self.lbl_alarm_second.setGeometry(QRect(320, 130, 71, 71))
        self.lbl_alarm_second.setFont(font)
        self.lbl_alarm_second.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;\n"
"padding: 20px;")
        self.lbl_alarm_add = QPushButton(self.tab_2)
        self.lbl_alarm_add.setObjectName(u"lbl_alarm_add")
        self.lbl_alarm_add.setGeometry(QRect(110, 230, 101, 41))
        self.lbl_alarm_add.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.lbl_alarm_edit = QPushButton(self.tab_2)
        self.lbl_alarm_edit.setObjectName(u"lbl_alarm_edit")
        self.lbl_alarm_edit.setGeometry(QRect(230, 230, 101, 41))
        self.lbl_alarm_edit.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.lbl_alarm_delete = QPushButton(self.tab_2)
        self.lbl_alarm_delete.setObjectName(u"lbl_alarm_delete")
        self.lbl_alarm_delete.setGeometry(QRect(350, 230, 101, 41))
        self.lbl_alarm_delete.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.lbl_stopwatch = QLabel(self.tab_3)
        self.lbl_stopwatch.setObjectName(u"lbl_stopwatch")
        self.lbl_stopwatch.setGeometry(QRect(180, 40, 221, 71))
        self.lbl_stopwatch.setFont(font)
        self.lbl_stopwatch.setLayoutDirection(Qt.LeftToRight)
        self.lbl_stopwatch.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.lbl_stopwatch.setAlignment(Qt.AlignCenter)
        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(90, 180, 101, 41))
        self.btn_start_stopwatch.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(240, 180, 101, 41))
        self.btn_stop_stopwatch.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.btn_reset_stopwatch = QPushButton(self.tab_3)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(390, 180, 101, 41))
        self.btn_reset_stopwatch.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.lbl_timer_second = QLineEdit(self.tab_4)
        self.lbl_timer_second.setObjectName(u"lbl_timer_second")
        self.lbl_timer_second.setGeometry(QRect(330, 40, 71, 71))
        self.lbl_timer_second.setFont(font)
        self.lbl_timer_second.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;\n"
"padding: 20px;")
        self.lbl_timer_minute = QLineEdit(self.tab_4)
        self.lbl_timer_minute.setObjectName(u"lbl_timer_minute")
        self.lbl_timer_minute.setGeometry(QRect(250, 40, 71, 71))
        self.lbl_timer_minute.setFont(font)
        self.lbl_timer_minute.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;\n"
"padding: 20px;")
        self.lbl_timer_hour = QLineEdit(self.tab_4)
        self.lbl_timer_hour.setObjectName(u"lbl_timer_hour")
        self.lbl_timer_hour.setGeometry(QRect(170, 40, 71, 71))
        self.lbl_timer_hour.setFont(font)
        self.lbl_timer_hour.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;\n"
"padding: 20px;")
        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(240, 180, 101, 41))
        self.btn_stop_timer.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.btn_reset_timer = QPushButton(self.tab_4)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setGeometry(QRect(390, 180, 101, 41))
        self.btn_reset_timer.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(90, 180, 101, 41))
        self.btn_start_timer.setStyleSheet(u"background-color: #092635;\n"
"color: #9EC8B9;\n"
"border-radius: 20px;")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_USA.setText(QCoreApplication.translate("MainWindow", u"00 : 00 : 00", None))
        self.lbl_Germany.setText(QCoreApplication.translate("MainWindow", u"00 : 00 : 00", None))
        self.lbl_Iran.setText(QCoreApplication.translate("MainWindow", u"00 : 00 : 00", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Usa", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Germany", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Iran", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.lbl_alarm_minute.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_alarm_hour.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_alarm_second.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_alarm_add.setText(QCoreApplication.translate("MainWindow", u"Add New Clock", None))
        self.lbl_alarm_edit.setText(QCoreApplication.translate("MainWindow", u"Edit Clock", None))
        self.lbl_alarm_delete.setText(QCoreApplication.translate("MainWindow", u"Delete Clock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.lbl_stopwatch.setText(QCoreApplication.translate("MainWindow", u"00 : 00 : 00", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Stop Watch", None))
        self.lbl_timer_second.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_timer_minute.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_timer_hour.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

