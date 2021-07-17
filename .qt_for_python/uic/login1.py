# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import logologin_rc
import iconelogin_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(485, 335)
        Login.setMinimumSize(QSize(485, 335))
        Login.setMaximumSize(QSize(485, 335))
        icon = QIcon()
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"icone.png", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u"icone.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Disabled, QIcon.On)
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Active, QIcon.Off)
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Active, QIcon.On)
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Selected, QIcon.Off)
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Selected, QIcon.On)
        Login.setWindowIcon(icon)
        Login.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 140, 141, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(160, 180, 141, 21))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 140, 61, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 180, 61, 20))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 230, 75, 23))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 20, 311, 71))
        self.label_2.setPixmap(QPixmap(u"logoprin.png"))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 270, 91, 20))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(390, 270, 75, 23))
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Login)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 485, 21))
        Login.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Login)
        self.statusbar.setObjectName(u"statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login - Gp TubeDownloader", None))
        self.label.setText(QCoreApplication.translate("Login", u"USUARIO :", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"  SENHA :", None))
        self.pushButton.setText(QCoreApplication.translate("Login", u"Entrar", None))
        self.label_2.setText("")
        self.label_6.setText(QCoreApplication.translate("Login", u"Se Cadastre Aqui :", None))
        self.pushButton_2.setText(QCoreApplication.translate("Login", u"Cadastrar", None))
    # retranslateUi

