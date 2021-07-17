# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import logcadastro_rc
import iconecad_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(392, 279)
        MainWindow.setMinimumSize(QSize(392, 279))
        MainWindow.setMaximumSize(QSize(392, 279))
        MainWindow.setSizeIncrement(QSize(329, 279))
        icon = QIcon()
        icon.addFile(u"icone.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Disabled, QIcon.On)
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Active, QIcon.Off)
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Active, QIcon.On)
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Selected, QIcon.Off)
        icon.addFile(u":/newPrefix/icone.png", QSize(), QIcon.Selected, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 120, 61, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 160, 47, 13))
        self.label_2.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 120, 113, 20))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 160, 113, 20))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 210, 75, 23))
        self.pushButton.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 30, 311, 81))
        self.label_3.setPixmap(QPixmap(u"logoprin.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 392, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cadastro  - Gp TubeDownloader", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Concluir", None))
        self.label_3.setText("")
    # retranslateUi

