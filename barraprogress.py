"""
import time
from time import sleep
from PyQt5 import uic, QtWidgets
from pytube.extract import video_info_url
from Gptube import video_download


def progresso():
    barraprogresso.progressBar.setValue(10)
    sleep(1)
    barraprogresso.progressBar.setValue(20)
    sleep(1)
    barraprogresso.progressBar.setValue(30)
    sleep(1)
    barraprogresso.progressBar.setValue(40)
    sleep(1)
    barraprogresso.progressBar.setValue(100)




app = QtWidgets.QApplication([])  # FAZ O PYQT FUNCIONAR
barraprogresso = uic.loadUi("barraprogresso.ui")


barraprogresso.pushButton.clicked.connect(video_download)
barraprogresso.show()
app.exec()  # EXECUTA APLICAÇÃO
"""