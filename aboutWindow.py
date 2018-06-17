from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Ui_aboutWindow import Ui_aboutWindow 


class WindowAbout(QDialog, Ui_aboutWindow ):
    flagAbout=False
    def __init__(self, parent=None):
        super(WindowAbout,self).__init__(parent)
        self.setupUi(self)
        #Flag qui indique que la fenetre est ouverte
        self.flagAbout=True

    @pyqtSlot()
    def on_retourBtn_clicked(self):
        self.flagAbout=False
        self.close()

    @pyqtSlot()
    def on_cindyBtn_clicked(self):
        # ------------------------- QMovie avec gif
        self.label_2.setStyleSheet("border-image:url(./Img_rc/cindy.png)")
        # ------------------------- Fin movie

    @pyqtSlot()
    def on_stephBtn_clicked(self):
        # ------------------------- QMovie avec gif
        self.label_5.setStyleSheet("border-image:url(./Img_rc/steph.png)")
        # ------------------------- Fin movie

    @pyqtSlot()
    def on_cyrilBtn_clicked(self):
        # ------------------------- QMovie avec gif
        self.label_7.setStyleSheet("border-image:url(./Img_rc/cyril.png)")
        # ------------------------- Fin movie

    @pyqtSlot()
    def on_loickBtn_clicked(self):
        # ------------------------- QMovie avec gif
        self.label_9.setStyleSheet("border-image:url(./Img_rc/loick.png)")
        # ------------------------- Fin movie
