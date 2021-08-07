from logging import exception
from sqlite3.dbapi2 import Cursor
import time
from PyQt5 import uic, QtWidgets
#from PyQt5
import os
from pathlib import Path
from os import curdir, path
import tkinter
from tkinter import messagebox
from PyQt5.QtCore import showbase
from PyQt5.uic import properties
from pytube import Playlist, YouTube
import sqlite3
from tkinter import *
from tkinter import ttk
from tqdm import tqdm
from time import sleep
import pytube
import sys
import mysql 
from tkinter import *
from tkinter.ttk import *
import time

# mostra as telas e aviso
window = tkinter.Tk()
# Oculta a main Window do tkinter
window.wm_withdraw()

root=Tk()
root.wm_withdraw()

  
    
def video_download():
    
    try:
        inicial.show()
        url = inicial.lineEdit.text()  
        yt = pytube.YouTube(url)

        if inicial.radioButton_5.isChecked():
            video = yt.streams.get_by_itag(17)

        if inicial.radioButton.isChecked():
            video = yt.streams.get_by_itag(18)

        if inicial.radioButton_3.isChecked():
            video = yt.streams.get_by_itag(22)  
        if inicial.radioButton_2.isChecked():
            video = yt.streams.get_by_itag(22)
        if inicial.radioButton_4.isChecked():
            video = yt.streams.get_by_itag(22)     
        home = os.path.expanduser('~')
        
        for i in tqdm(range(100)):
            time.sleep(0.1)
    
            
        salva=video.download(os.path.join(home, 'Videos'))
        messagebox.showinfo("Status", f'                   Download do Video Concluido!!                                              \n SALVO EM : {salva}')
    except :
        if url == (""):
            messagebox.showerror("Aviso","O CAMPO DA URL ESTA VAZIO!")
        else:
            messagebox.showerror("Aviso"," A URL ESTA INVALIDA,OU NAO FOI INFORMADA UMA RESOLUÇÃO!")
    
    

def audio_download():
    try:
        url_audio = inicial.lineEdit.text()  # recebe o inpu do usuario que ira informar A URL
        yt = pytube.YouTube(url_audio)  # ira ler o input recebido
        audio = yt.streams.filter(only_audio=True).first()
        messagebox.showinfo("Status" ,f'Download em andamento aguarde ...')
        for i in tqdm(range(100)):
    
            time.sleep(0.1)
            home = os.path.expanduser('~')
            salva=audio.download(os.path.join(home, 'Videos'))
        messagebox.showinfo("Status", f'                   Download do Audio  Concluido!!                                              \n SALVO EM : {salva}')

    except:
        if url_audio==(""):
            messagebox.showerror("Aviso","O CAMPO DA URL ESTA VAZIO!")
        else:
            messagebox.showerror("Aviso","URL INVALIDA!")


def playlist_download():
    try:
        playlist_urls = inicial.lineEdit.text()  # recebe o inpu do usuario que ira informar A URL
        playlist = Playlist(playlist_urls)
        for url in playlist:
            video = YouTube(url)
            stream = video.streams.first()
            #print(video.title)
            home = os.path.expanduser('~')
            salva=stream.download(os.path.join(home, 'Videos'))
        messagebox.showinfo("Status", f'                   Download da Playlist Concluido!!                                              \n SALVO EM : {salva}')
        
    except:
        if playlist_urls ==(""):
            messagebox.showerror("Aviso","O CAMPO DA URL ESTA VAZIO!")
        else:
             messagebox.showerror("Aviso","A URL INVALIDA OU NAO PERTENCE A UMA PLAYLIST")    
       

def novo_download():
    inicial.lineEdit.setText("")






app = QtWidgets.QApplication([])  # FAZ O PYQT FUNCIONAR

inicial = uic.loadUi("inicial.ui")  # carrega arquivo UI


#inicial.pushButton_2.clicked.connect(video_download)
inicial.pushButton_2.clicked.connect(start)  # quando o campo pusubutton receber um clique ele ira fazer o download
inicial.pushButton.clicked.connect(novo_download)  # quando o campo pusubutton receber um clique ele ira fazer o download
inicial.pushButton_3.clicked.connect(audio_download)
inicial.pushButton_4.clicked.connect(playlist_download)
#login1.pushButton.clicked.connect(Entra_Login)
# MOSTRA O RPOGRAMA
inicial.show()

app.exec()  # EXECUTA APLICAÇÃO
root.mainloop()
window.mainloop()