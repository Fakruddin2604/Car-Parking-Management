# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'front.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_CarParkingManager(object):
    def setupUi(self, CarParkingManager):
        if not CarParkingManager.objectName():
            CarParkingManager.setObjectName(u"CarParkingManager")
        CarParkingManager.resize(922, 379)
        CarParkingManager.setMinimumSize(QSize(922, 379))
        CarParkingManager.setMaximumSize(QSize(922, 379))
        self.centralwidget = QWidget(CarParkingManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-100, -230, 1021, 611))
        font = QFont()
        font.setPointSize(20)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(30, 30, 36);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.s1 = QPushButton(self.frame)
        self.s1.setObjectName(u"s1")
        self.s1.setGeometry(QRect(520, 370, 111, 51))
        font1 = QFont()
        font1.setFamilies([u"HelveticaRounded LT Std BdCn"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.s1.setFont(font1)
        self.s1.setFocusPolicy(Qt.StrongFocus)
        self.s1.setLayoutDirection(Qt.LeftToRight)
        self.s1.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s1.setCheckable(False)
        self.s2 = QPushButton(self.frame)
        self.s2.setObjectName(u"s2")
        self.s2.setGeometry(QRect(640, 370, 111, 51))
        self.s2.setFont(font1)
        self.s2.setFocusPolicy(Qt.StrongFocus)
        self.s2.setLayoutDirection(Qt.LeftToRight)
        self.s2.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s2.setCheckable(False)
        self.s15 = QPushButton(self.frame)
        self.s15.setObjectName(u"s15")
        self.s15.setGeometry(QRect(760, 550, 111, 51))
        self.s15.setFont(font1)
        self.s15.setFocusPolicy(Qt.StrongFocus)
        self.s15.setLayoutDirection(Qt.LeftToRight)
        self.s15.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s15.setCheckable(False)
        self.s4 = QPushButton(self.frame)
        self.s4.setObjectName(u"s4")
        self.s4.setGeometry(QRect(880, 370, 111, 51))
        self.s4.setFont(font1)
        self.s4.setFocusPolicy(Qt.StrongFocus)
        self.s4.setLayoutDirection(Qt.LeftToRight)
        self.s4.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s4.setCheckable(False)
        self.s5 = QPushButton(self.frame)
        self.s5.setObjectName(u"s5")
        self.s5.setGeometry(QRect(520, 430, 111, 51))
        self.s5.setFont(font1)
        self.s5.setFocusPolicy(Qt.StrongFocus)
        self.s5.setLayoutDirection(Qt.LeftToRight)
        self.s5.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s5.setCheckable(False)
        self.s11 = QPushButton(self.frame)
        self.s11.setObjectName(u"s11")
        self.s11.setGeometry(QRect(760, 490, 111, 51))
        self.s11.setFont(font1)
        self.s11.setFocusPolicy(Qt.StrongFocus)
        self.s11.setLayoutDirection(Qt.LeftToRight)
        self.s11.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s11.setCheckable(False)
        self.s13 = QPushButton(self.frame)
        self.s13.setObjectName(u"s13")
        self.s13.setGeometry(QRect(520, 550, 111, 51))
        self.s13.setFont(font1)
        self.s13.setFocusPolicy(Qt.StrongFocus)
        self.s13.setLayoutDirection(Qt.LeftToRight)
        self.s13.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s13.setCheckable(False)
        self.s8 = QPushButton(self.frame)
        self.s8.setObjectName(u"s8")
        self.s8.setGeometry(QRect(880, 430, 111, 51))
        self.s8.setFont(font1)
        self.s8.setFocusPolicy(Qt.StrongFocus)
        self.s8.setLayoutDirection(Qt.LeftToRight)
        self.s8.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s8.setCheckable(False)
        self.s6 = QPushButton(self.frame)
        self.s6.setObjectName(u"s6")
        self.s6.setGeometry(QRect(640, 430, 111, 51))
        self.s6.setFont(font1)
        self.s6.setFocusPolicy(Qt.StrongFocus)
        self.s6.setLayoutDirection(Qt.LeftToRight)
        self.s6.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s6.setCheckable(False)
        self.s10 = QPushButton(self.frame)
        self.s10.setObjectName(u"s10")
        self.s10.setGeometry(QRect(640, 490, 111, 51))
        self.s10.setFont(font1)
        self.s10.setFocusPolicy(Qt.StrongFocus)
        self.s10.setLayoutDirection(Qt.LeftToRight)
        self.s10.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s10.setCheckable(False)
        self.s3 = QPushButton(self.frame)
        self.s3.setObjectName(u"s3")
        self.s3.setGeometry(QRect(760, 370, 111, 51))
        self.s3.setFont(font1)
        self.s3.setFocusPolicy(Qt.StrongFocus)
        self.s3.setLayoutDirection(Qt.LeftToRight)
        self.s3.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s3.setCheckable(False)
        self.s7 = QPushButton(self.frame)
        self.s7.setObjectName(u"s7")
        self.s7.setGeometry(QRect(760, 430, 111, 51))
        self.s7.setFont(font1)
        self.s7.setFocusPolicy(Qt.StrongFocus)
        self.s7.setLayoutDirection(Qt.LeftToRight)
        self.s7.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s7.setCheckable(False)
        self.s16 = QPushButton(self.frame)
        self.s16.setObjectName(u"s16")
        self.s16.setGeometry(QRect(880, 550, 111, 51))
        self.s16.setFont(font1)
        self.s16.setFocusPolicy(Qt.StrongFocus)
        self.s16.setLayoutDirection(Qt.LeftToRight)
        self.s16.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s16.setCheckable(False)
        self.s14 = QPushButton(self.frame)
        self.s14.setObjectName(u"s14")
        self.s14.setGeometry(QRect(640, 550, 111, 51))
        self.s14.setFont(font1)
        self.s14.setFocusPolicy(Qt.StrongFocus)
        self.s14.setLayoutDirection(Qt.LeftToRight)
        self.s14.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s14.setCheckable(False)
        self.s9 = QPushButton(self.frame)
        self.s9.setObjectName(u"s9")
        self.s9.setGeometry(QRect(520, 490, 111, 51))
        self.s9.setFont(font1)
        self.s9.setFocusPolicy(Qt.StrongFocus)
        self.s9.setLayoutDirection(Qt.LeftToRight)
        self.s9.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s9.setCheckable(False)
        self.s12 = QPushButton(self.frame)
        self.s12.setObjectName(u"s12")
        self.s12.setGeometry(QRect(880, 490, 111, 51))
        self.s12.setFont(font1)
        self.s12.setFocusPolicy(Qt.StrongFocus)
        self.s12.setLayoutDirection(Qt.LeftToRight)
        self.s12.setStyleSheet(u"\n"
"background-color: rgb(64, 255, 80);\n"
"color: rgb(0,0,0);\n"
"\n"
"\n"
"")
        self.s12.setCheckable(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 260, 921, 71))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(25)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgba(255, 255, 255, 225);")
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(180, 390, 231, 41))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setBold(True)
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"border-radius: 15px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.ENTRYBUTTON = QPushButton(self.frame)
        self.ENTRYBUTTON.setObjectName(u"ENTRYBUTTON")
        self.ENTRYBUTTON.setGeometry(QRect(190, 460, 91, 41))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setBold(True)
        self.ENTRYBUTTON.setFont(font4)
        self.ENTRYBUTTON.setStyleSheet(u"background-color: rgb(255, 155, 113);\n"
"border-radius: 20px;\n"
"color: rgba(0, 0, 0, 200);\n"
"\n"
"QPushButton{\n"
"background-color: rgba(255, 155, 113,50);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgba(255, 155, 113,25);\n"
"}\n"
"")
        self.EXITBUTTON = QPushButton(self.frame)
        self.EXITBUTTON.setObjectName(u"EXITBUTTON")
        self.EXITBUTTON.setGeometry(QRect(310, 460, 91, 41))
        self.EXITBUTTON.setFont(font4)
        self.EXITBUTTON.setStyleSheet(u"background-color: rgb(255, 155, 113);\n"
"border-radius: 20px;\n"
"color: rgba(0, 0, 0, 200);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 510, 321, 71))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(15)
        font5.setBold(True)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color: rgba(255, 255, 255, 225);")
        self.label_2.setAlignment(Qt.AlignCenter)
        CarParkingManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(CarParkingManager)

        QMetaObject.connectSlotsByName(CarParkingManager)
    # setupUi

    def retranslateUi(self, CarParkingManager):
        CarParkingManager.setWindowTitle(QCoreApplication.translate("CarParkingManager", u"Car Parking Manager", None))
        self.s1.setText(QCoreApplication.translate("CarParkingManager", u"1", None))
        self.s2.setText(QCoreApplication.translate("CarParkingManager", u"2", None))
        self.s15.setText(QCoreApplication.translate("CarParkingManager", u"15", None))
        self.s4.setText(QCoreApplication.translate("CarParkingManager", u"4", None))
        self.s5.setText(QCoreApplication.translate("CarParkingManager", u"5", None))
        self.s11.setText(QCoreApplication.translate("CarParkingManager", u"11", None))
        self.s13.setText(QCoreApplication.translate("CarParkingManager", u"13", None))
        self.s8.setText(QCoreApplication.translate("CarParkingManager", u"8", None))
        self.s6.setText(QCoreApplication.translate("CarParkingManager", u"6", None))
        self.s10.setText(QCoreApplication.translate("CarParkingManager", u"10", None))
        self.s3.setText(QCoreApplication.translate("CarParkingManager", u"3", None))
        self.s7.setText(QCoreApplication.translate("CarParkingManager", u"7", None))
        self.s16.setText(QCoreApplication.translate("CarParkingManager", u"16", None))
        self.s14.setText(QCoreApplication.translate("CarParkingManager", u"14", None))
        self.s9.setText(QCoreApplication.translate("CarParkingManager", u"9", None))
        self.s12.setText(QCoreApplication.translate("CarParkingManager", u"12", None))
        self.label.setText(QCoreApplication.translate("CarParkingManager", u"CAR PARKING MANAGEMENT", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("CarParkingManager", u"Vehicle Number", None))
        self.ENTRYBUTTON.setText(QCoreApplication.translate("CarParkingManager", u"Entry", None))
        self.EXITBUTTON.setText(QCoreApplication.translate("CarParkingManager", u"Exit", None))
        self.label_2.setText("")
    # retranslateUi

