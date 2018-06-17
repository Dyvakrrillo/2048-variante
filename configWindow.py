# -*- coding: utf-8 -*-
# main_windows_biblio.py
# utilisation de Qt designer

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Ui_configWindow import Ui_configWindow
from PyQt5.QtMultimedia import *

class WindowConfig(QWidget, Ui_configWindow):
    
    #Entrée au jeu direct sans acceder au parametres
    global directEntry
    directEntry=0
    
    global rangee
    rangee=4
        
    flagConfig=False
    
    def __init__(self, musicPlayer, parent=None):
        super(WindowConfig,self).__init__(parent)
        self.setupUi(self)
        self.gameModeComboBox.currentIndexChanged.connect(self.setGameMode)
        self.musicComboBox.currentIndexChanged.connect(self.changeMusic)
        self.soundBtn.stateChanged.connect(self.stopMusic)
        
        #Recoit la musique depuis la fenetre principal
        self.player=musicPlayer
        
        #Flag qui indique que la fenetre est ouverte
        self.flagConfig=True
        
        #Background
        palette = self.palette()
        self.setAutoFillBackground(True)
        bgPixmap = QPixmap("./Img_rc/img4.jpg")
        brush = QBrush()
        brush.setTexture(bgPixmap)
        palette.setBrush(QPalette.Background, brush)
        self.setPalette(palette)

        
        
    #Verifie si c'est la premier fois que l'on ouvre la fenetre
    def isFirstEntry(self):
        if (directEntry==0):
            return True
        else:
            return False
            
    #--------------------------Musique automatique    
    def playMusic(self):
        self.player = QMediaPlayer(self)
        self.sound = QMediaContent(QUrl.fromLocalFile("./music/Seven_Twenty_Default.wav"))
        self.player.setMedia(self.sound)
        self.player.setVolume(100)
        self.show()
        self.player.play()
        
    def changeMusic(self):
        #couper la chanson precedente et jouer la nouvelle
        self.player.stop()
        song = self.musicComboBox.currentIndex()
        if(self.soundBtn.isChecked()):
            if (song==0):  self.sound = QMediaContent(QUrl.fromLocalFile("./music/Seven_Twenty_Default.wav"))
            if (song==1):  self.sound = QMediaContent(QUrl.fromLocalFile("./music/Church_of_8_Wheels.wav"))
            if (song==2): self.sound = QMediaContent(QUrl.fromLocalFile("./music/Firefly.wav"))
            if (song==3): self.sound = QMediaContent(QUrl.fromLocalFile("./music/Hi_Q.wav"))
            if (song==4): self.sound = QMediaContent(QUrl.fromLocalFile("./music/Renegade_Jubilee.wav"))
        
            self.player.setMedia(self.sound)
            self.player.setVolume(100)
            self.show()
            self.player.play()
    
    def stopMusic(self):
        if(self.soundBtn.isChecked()):
            self.changeMusic()
        else:
            self.player.stop()
    #-------------------------- Fin Musique

        
    def setGameMode(self):
        global directEntry
        global rangee
        directEntry=1
        if (directEntry>0):
            gameMode = self.gameModeComboBox.currentIndex()
            rangee=gameMode+4
        if(rangee==4): self.labelStr.setText("4x4 2048")
        if(rangee==5): self.labelStr.setText("5x5 4096")
        if(rangee==6): self.labelStr.setText("6x6 8192")
        if(rangee==7): self.labelStr.setText("7x7 16384")
        if(rangee==8): self.labelStr.setText("8x8 32768")


    def getRangee(self):
        return (rangee)
        

        
    @pyqtSlot()
    def on_accepterBtn_clicked(self):
        self.flagConfig=False
        self.close()
        


"""
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    configWindow = QWidget()
    ui = Ui_configWindow()
    ui.setupUi(configWindow)
    configWindow.show()
    sys.exit(app.exec_())
"""
