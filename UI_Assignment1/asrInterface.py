# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QPixmap, QPalette
from PyQt5.QtWidgets import QInputDialog, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 792)
        MainWindow.setStyleSheet("background-color: rgb(11, 14, 50);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(QtCore.QRect(20, 260, 464, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(204, 204, 240);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)

        self.tips_label1=QtWidgets.QLabel(self.centralwidget)
        self.tips_label1.setGeometry(QtCore.QRect(40, 715, 30, 20))
        self.tips_label1.setFont(font)
        self.tips_label1.setStyleSheet("color: rgb(204, 204, 240);")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)

        self.tips_label2 = QtWidgets.QLabel(self.centralwidget)
        self.tips_label2.setGeometry(QtCore.QRect(35, 675, 60, 25))
        self.tips_label2.setFont(font)
        self.tips_label2.setStyleSheet("color: rgb(204, 204, 240);")


        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)

        self.tips=QtWidgets.QComboBox(self.centralwidget)
        self.tips.setGeometry(QtCore.QRect(60, 700, 420, 51))
        self.tips.addItems(["Enjoy music by saying \"music\"",
                            "Take some notes by saying \"note pad\"",
                            "Browse a web page by saying \"browser\"",
                            "Change the volume by saying \"up\" or \"down\"",
                            "Switch music by saying \"next\" or \"previous\""])

        self.tips.setStyleSheet("font-family:Calibri;border:0px;background-color: rgb(11, 14, 50);font:21px;color:rgb(204, 204, 240);")


        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(165, 110, 161, 121))
        self.voiceFig.setText("")
        self.gif = QMovie("siri.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")


        self.label_7=QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(125, 450, 504, 51))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(204, 204, 240);")
        self.input= QtWidgets.QLineEdit(self.centralwidget)
        self.input.setAlignment(Qt.AlignCenter)
        self.input.setGeometry(QtCore.QRect(127, 510, 250, 51))
        self.input.setStyleSheet("color:rgb(204, 204, 240) ;border:1px solid rgb(101, 127, 255);border-radius: 4px;")
        self.input.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label.setText(_translate("MainWindow", "Hello! How can I help?"))

        self.label_7.setText(_translate("MainWindow", "You can also type here:"))
        self.tips_label1.setText(_translate("MainWindow", "↪"))
        self.tips_label2.setText(_translate("MainWindow", "tips"))

