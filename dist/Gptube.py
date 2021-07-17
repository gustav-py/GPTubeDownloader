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

# mostra as telas e aviso
window = tkinter.Tk()
# Oculta a main Window do tkinter
window.wm_withdraw()

root=Tk()
root.wm_withdraw()

def Entra_Login():
    try:
        login1.show()
        cadastro.close()
        Usuarios=login1.lineEdit.text()
        Senhas= login1.lineEdit_2.text()
        
        banco=sqlite3.connect('GptubeBanco.db')
        cursor1=banco.cursor()
        cursor1.execute("SELECT Usuarios from CadasUsu WHERE Usuarios='{}'".format(Usuarios))
        Usuario_db=cursor1.fetchall() 
        Usuario_verifica=Usuario_db[0][0]
        
        cursor2=banco.cursor()
        cursor2.execute("SELECT Senhas from CadasUsu WHERE Senhas='{}'".format(Senhas))
        Senhas_db=cursor2.fetchall()
        Senhas_verifica=Senhas_db[0][0]
        #print(Senhas_verifica)
        #banco.close()
        if Usuario_verifica==Usuarios:
            inicial.show()
            login1.close()
    except:
        messagebox.showinfo("Atenção!", " Login Inválido!!")

def cadastro_usu():
    cadastro.show()
     
    
    Usuarios=cadastro.lineEdit.text()
    Senhas=cadastro.lineEdit_2.text()
   
    try:
       
        banco=sqlite3.connect('GptubeBanco.db')
        cursor=banco.cursor()
        cursor.execute("INSERT INTO CadasUsu VALUES ('"+Usuarios+"','"+Senhas+"')")
        banco.commit()
        banco.close()
        
        messagebox.showinfo("Status","cadastro concluido")
        cadastro.lineEdit.setText("")
        cadastro.lineEdit_2.setText("")

    except sqlite3.Error as erro:
        print("erro ao inserir dados  : " ,erro)    
    
def video_download():
    inicial.close()
   

    
    try:
        
        url = inicial.lineEdit.text()  
        yt = pytube.YouTube(url)  
        video = yt.streams.first()
        home = os.path.expanduser('~')
        
        for i in tqdm(range(100)):
            time.sleep(0.1)
            
            
        salva=video.download(os.path.join(home, 'Videos'))
       
        
        messagebox.showinfo("Status", f'                   Download do Video Concluido!!                                              \n SALVO EM : {salva}')
    except:
        if url == (""):
            messagebox.showerror("Aviso","O CAMPO DA URL ESTA VAZIO!")
        else:
            messagebox.showerror("Aviso"," A URL ESTA INVALIDA!")

    
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
    

def botaoSair():
    login1.show()
    inicial.close()



app = QtWidgets.QApplication([])  # FAZ O PYQT FUNCIONAR
login1 = uic.loadUi("login1.ui")  # carrega arquivo UI
inicial = uic.loadUi("inicial.ui")  # carrega arquivo UI
cadastro=uic.loadUi("cadastro.ui")

inicial.pushButton_2.clicked.connect(video_download)  # quando o campo pusubutton receber um clique ele ira fazer o download
inicial.pushButton.clicked.connect(novo_download)  # quando o campo pusubutton receber um clique ele ira fazer o download
inicial.pushButton_3.clicked.connect(audio_download)
inicial.pushButton_4.clicked.connect(playlist_download)
login1.pushButton.clicked.connect(Entra_Login)
login1.pushButton_2.clicked.connect(cadastro.show) # abre tela de cadastro
cadastro.pushButton.clicked.connect(cadastro_usu)

inicial.pushButton_5.clicked.connect(botaoSair)

  # MOSTRA O RPOGRAMA
login1.show()

app.exec()  # EXECUTA APLICAÇÃO
root.mainloop()