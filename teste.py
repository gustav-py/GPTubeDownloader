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






url = 'https://www.youtube.com/watch?v=2q7fzpPDcGg' 
yt = pytube.YouTube(url)  
video = yt.streams.first()
home = os.path.expanduser('~')
for i in tqdm(range(100)):
    time.sleep(0.1)
            
            
salva=video.download(os.path.join(home, 'Videos'))
       
        
print("o video foi salvo em :", salva)
   