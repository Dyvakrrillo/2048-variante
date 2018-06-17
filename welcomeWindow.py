# -*- coding: utf-8 -*-
# main_windows_biblio.py
# utilisation de Qt designer

from tkinter import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Ui_welcomeWindow import Ui_MainWindow
from configWindow import WindowConfig
from instructionsWindow import WindowInstructions
from aboutWindow import WindowAbout
from PyQt5.QtMultimedia import *
from gameModes.grille_4 import *
from gameModes.grille_5 import *
from gameModes.grille_6 import *
from gameModes.grille_7 import *
from gameModes.grille_8 import *

class MainWindowGame(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindowGame,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.playGameBtn.clicked.connect(self.openGame)
        self.ui.instructionsBtn.clicked.connect(self.openInstructions)
        self.ui.configBtn.clicked.connect(self.openConfig)
        self.ui.aboutBtn.clicked.connect(self.openAbout)
        
        self.ui.quitBtn.clicked.connect(self.quit)
        
        # ------------------------- QMovie avec gif
        self.movie = QMovie("./Img_rc/2048.gif",QByteArray(), self )
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.ui.title2048.setMovie(self.movie)
        self.movie.start()
        # ------------------------- Fin movie
        
        #---- Musique automatique
        self.player = QMediaPlayer(self)
        self.sound = QMediaContent(QUrl.fromLocalFile("./music/Seven_Twenty_Default.wav"))
        self.player.setMedia(self.sound)
        self.player.setVolume(100)
        self.show()
        self.player.play()
        
        
    def setRangee(self, r):
        global rangee
        rangee = r

    #Connexion a la fenetre du jeu
    def openGame(self):        
        if (WindowConfig.isFirstEntry(self)): self.jeu = Grille4()
        elif (WindowConfig.getRangee(self)==4 ): self.jeu = Grille4()
        elif (WindowConfig.getRangee(self)==5): self.jeu = Grille5()
        elif (WindowConfig.getRangee(self)==6): self.jeu = Grille6()
        elif (WindowConfig.getRangee(self)==7): self.jeu = Grille7()
        elif (WindowConfig.getRangee(self)==8): self.jeu = Grille8()
        
    #Connexion a la fenetre de reglages
    def openConfig(self):  
        self.configGame = WindowConfig(self.player)
        self.configGame.show()

    #Connexion a la fenetre d'instructions
    def openInstructions(self):        
        self.instructionsWindow= WindowInstructions()
        self.instructionsWindow.show()
        
    #Connexion a la fenetre d'info
    def openAbout(self):
        self.aboutWindow= WindowAbout()
        self.aboutWindow.show()

    def quit(self):
        quitter = QMessageBox.question (self,
                'Quitter',
                "Souhaitez-vous quitter l'application ?",
                QMessageBox.Ok,
                QMessageBox.Cancel)
        if (quitter == QMessageBox.Ok):
            if(WindowAbout.flagAbout):self.aboutWindow.close()
            if(WindowConfig.flagConfig): self.configGame.close()
            if(WindowInstructions.flagInstructions): self.instructionsWindow.close()
            QCoreApplication.instance().quit()
        else:
            pass

    
